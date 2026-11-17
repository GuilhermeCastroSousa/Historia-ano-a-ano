"""
Coleta um lote de vídeos novos de um canal do YouTube e monta o arquivo de
evidências para classificação.

Usa SOMENTE a YouTube Data API oficial, com a sua chave. Não raspa nada.
As transcrições foram removidas de propósito: não existe forma autorizada de
baixar legendas de vídeos de terceiros, e fazê-lo viola os Termos de Serviço.
As evidências vêm de título, capítulos, descrição e tags — tudo dado público
entregue pela própria API.

Antes de rodar, uma vez só:
    pip install openpyxl

Como usar:
    1. Salve sua chave da API num arquivo chamado  chave.txt  (só a chave).
    2. Ajuste o bloco CONFIGURAÇÃO abaixo.
    3. python coletar.py
    4. Suba o arquivo gerado (lote-XX.md) na conversa com o Claude.

Coletar de uma playlist específica em vez do canal inteiro:
    python coletar.py --playlist ID_DA_PLAYLIST --nome "Nome para o Canal"
(ID_DA_PLAYLIST é o trecho depois de "list=" na URL. --nome é obrigatório na
primeira coleta — é o que vai para a coluna Canal e para canais.json; não é o
nome do canal do YouTube que subiu os vídeos, que pode não ter nada a ver
com história. Ver protocolo.md.)

Coletar só o que o canal publicou a partir de uma data:
    python coletar.py @Handle --desde 2026-07-31
(Para revisita de canal encerrado cuja primeira página já ficou toda
conhecida: a parada antecipada pararia antes dos vídeos novos das páginas
seguintes. O corte por data desliga essa parada e, em troca, encerra a
varredura quando aparece uma página só com vídeos anteriores ao corte —
assim um acervo antigo nunca coletado não entra de carona. Ver buscar_lote.)

Inserir um vídeo avulso, sem paginar o canal inteiro:
    python coletar.py --video ID_OU_LINK --canal @Handle
(--canal é a chave exata que já existe em canais.json — @Handle ou
"playlist:ID". O canal precisa já estar adotado; vídeo de canal novo entra
pelo fluxo normal acima, não por aqui. Gera um lote-NN.md de 1 vídeo, sujeito
às mesmas checagens de sempre — dedup, Short, live, exclusivo — e confere que
o vídeo realmente pertence ao canal indicado antes de aceitar.)
"""

import datetime
import json
import os
import re
import sys
import urllib.parse
import urllib.request

# O console do Windows costuma abrir em cp1252, que não representa todo
# caractere Unicode que um título de vídeo pode trazer (achado no canal
# Cambrian Chronicles, lote 84: um título quebrou o script com
# UnicodeEncodeError bem no meio da coleta, antes de gravar qualquer
# arquivo). Isso é falha de EXIBIÇÃO, não de dado — o arquivo lote-NN.md
# já abre com encoding="utf-8" explícito (ver mais abaixo) e nunca teve
# esse problema. Reconfigurar stdout evita que um título "impresentável"
# no terminal derrube a coleta inteira.
for _fluxo in (sys.stdout, sys.stderr):
    if hasattr(_fluxo, "reconfigure"):
        _fluxo.reconfigure(encoding="utf-8", errors="replace")

# ─────────────────────────── CONFIGURAÇÃO ───────────────────────────

CANAL = "@AncientAmericas"        # @handle do canal, ou ID que começa com UC...
                                  # pode ser trocado na linha de comando:
                                  #     python coletar.py @OutroCanal
                                  # Canais já encerrados estão em canais.json.
TAMANHO_LOTE = 25                # quantos vídeos novos por rodada
DURACAO_MINIMA = 181             # segundos. Abaixo disso é Short e é descartado.
PLANILHA = "playlist-historia-v2.xlsx"
# Fica FORA da pasta do projeto de propósito, para nunca entrar num commit.
# Pode ser trocado pela variável de ambiente YOUTUBE_API_KEY_FILE.
ARQUIVO_CHAVE = os.environ.get(
    "YOUTUBE_API_KEY_FILE",
    os.path.join(os.path.expanduser("~"), ".chaves", "youtube.txt"),
)
ARQUIVO_DESCARTES = "descartados.txt"    # Shorts e exclusivos já vistos e recusados
ARQUIVO_CATALOGADOS = "catalogados.txt"  # ids ja enviados para classificacao (dedup sem a planilha)
ARQUIVO_CANAIS = "canais.json"           # estado por canal: status, faixa de lotes, datas

# ────────────────────────────────────────────────────────────────────

API = "https://www.googleapis.com/youtube/v3/"


def erro(msg):
    print(f"\nERRO: {msg}\n")
    sys.exit(1)


def ler_chave():
    if not os.path.exists(ARQUIVO_CHAVE):
        erro(f"não encontrei o arquivo {ARQUIVO_CHAVE}. Crie-o com a sua chave da API dentro.")
    chave = open(ARQUIVO_CHAVE, encoding="utf-8").read().strip()
    if not chave:
        erro(f"o arquivo {ARQUIVO_CHAVE} está vazio.")
    return chave


def api(recurso, **params):
    """Chama a YouTube Data API e devolve o JSON."""
    params["key"] = CHAVE
    url = API + recurso + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        corpo = e.read().decode("utf-8", "ignore")
        if e.code == 403 and "quotaExceeded" in corpo:
            erro("cota diária da API esgotada. Ela reseta à meia-noite no horário do Pacífico.")
        if e.code == 400 and "keyInvalid" in corpo:
            erro("a chave da API foi recusada. Confira o conteúdo de chave.txt.")
        erro(f"a API respondeu {e.code}.\n{corpo[:400]}")
    except urllib.error.URLError as e:
        erro(f"não consegui falar com a API. Confira a conexão.\n{e.reason}")


def ids_ja_registrados():
    """Lê a planilha e devolve o conjunto de video_id já catalogados."""
    if not os.path.exists(PLANILHA):
        print(f"aviso: {PLANILHA} não encontrada — tratando todos os vídeos como novos.")
        return set()
    import openpyxl
    ws = openpyxl.load_workbook(PLANILHA, read_only=True)["Catálogo"]
    linhas = ws.iter_rows(values_only=True)
    cabecalho = next(linhas)
    if "video_id" not in cabecalho:
        erro("a planilha não tem coluna 'video_id'.")
    col = cabecalho.index("video_id")
    return {str(l[col]).strip() for l in linhas if l[col]}


def ler_lista(caminho):
    """Le um arquivo de ids, um por linha. Devolve conjunto vazio se nao existir."""
    if not os.path.exists(caminho):
        return set()
    with open(caminho, encoding="utf-8") as f:
        return {l.strip() for l in f if l.strip()}


def gravar_lista(caminho, ids):
    with open(caminho, "a", encoding="utf-8") as f:
        for i in ids:
            f.write(i + "\n")


def ler_descartados():
    return ler_lista(ARQUIVO_DESCARTES)


def gravar_descartados(ids):
    gravar_lista(ARQUIVO_DESCARTES, ids)


# ───────────────────────── estado por canal ─────────────────────────

def ler_canais():
    """Le canais.json. Devolve {} se nao existir — canal novo se registra sozinho."""
    if not os.path.exists(ARQUIVO_CANAIS):
        return {}
    with open(ARQUIVO_CANAIS, encoding="utf-8") as f:
        return json.load(f)


def gravar_canais(dados):
    with open(ARQUIVO_CANAIS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        f.write("\n")


def estado_do_canal(dados, canal):
    return (dados.get("canais") or {}).get(canal, {})


def registrar_coleta(canal, nome, numero_lote):
    """Anota a coleta em canais.json: canal novo entra, canal velho e' atualizado.

    Nao mexe em `status`: quem encerra e' o comando /encerrar, nao a coleta.
    """
    dados = ler_canais()
    dados.setdefault("canais", {})
    reg = dados["canais"].setdefault(canal, {})
    reg.setdefault("nome", nome)
    reg.setdefault("status", "em andamento")
    reg.setdefault("primeiro_lote", numero_lote)
    reg["ultimo_lote"] = numero_lote
    reg["ultima_coleta"] = datetime.date.today().isoformat()
    gravar_canais(dados)
    return reg


def playlist_de_uploads(canal):
    """Descobre a playlist que contem todos os videos publicados pelo canal."""
    if canal.startswith("UC") and len(canal) == 24:
        r = api("channels", part="contentDetails,snippet", id=canal)
    else:
        r = api("channels", part="contentDetails,snippet", forHandle=canal.lstrip("@"))
    itens = r.get("items") or []
    if not itens:
        erro(f"canal '{canal}' nao encontrado. Confira o @handle.")
    info = itens[0]
    return (info["contentDetails"]["relatedPlaylists"]["uploads"],
            info["snippet"]["title"])


def resolver_playlist_explicita(playlist_id, nome_forcado):
    """Confirma que uma playlist dada por ID existe; usa --nome, nunca o
    nome do canal do YouTube que a hospeda (pode ser irrelevante para
    história — foi o caso da playlist "History of Rome", hospedada num
    canal de 225 vídeos sem nenhuma outra relação com o catálogo)."""
    r = api("playlists", part="snippet", id=playlist_id)
    itens = r.get("items") or []
    if not itens:
        erro(f"playlist '{playlist_id}' nao encontrada. Confira o ID (o trecho depois de 'list=' na URL).")
    if not nome_forcado:
        erro("coleta por playlist exige --nome \"Nome para o Canal\" na primeira vez "
             "(o nome do canal do YouTube que hospeda os vídeos nem sempre é o nome certo pra planilha).")
    return playlist_id, nome_forcado


RE_VIDEO_ID = re.compile(r"^[\w-]{11}$")


def extrair_video_id(txt):
    """Aceita o id puro (11 caracteres) ou uma URL do YouTube em qualquer
    formato comum (watch?v=, youtu.be/, /shorts/), com ou sem parâmetros
    extras (&list=, &t=, etc.)."""
    txt = txt.strip()
    if RE_VIDEO_ID.match(txt):
        return txt
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", txt)
    if m:
        return m.group(1)
    erro(f"não consegui reconhecer um video_id em '{txt}'. Use o id puro "
         f"(11 caracteres) ou o link completo (watch?v=... ou youtu.be/...).")


def canal_id_de(chave_canal):
    """Resolve o channelId real por trás de uma chave de canais.json (@Handle
    ou UC...). Usado só para conferir que um --video pertence de fato ao
    canal indicado — nunca chamado para o fluxo normal de coleta."""
    if chave_canal.startswith("UC") and len(chave_canal) == 24:
        return chave_canal
    r = api("channels", part="id", forHandle=chave_canal.lstrip("@"))
    itens = r.get("items") or []
    if not itens:
        erro(f"canal '{chave_canal}' não encontrado ao conferir o vídeo. Confira o @handle.")
    return itens[0]["id"]


# Vídeos só para membros/apoiadores: o catálogo não os inclui.
RE_EXCLUSIVO = re.compile(r"(?i)\b(?:youtube\s+|patreon\s+)?(?:member|patron)s?\s+exclusive\b")

# Teasers e trailers: material promocional de vídeo exclusivo, nao entra no catalogo.
RE_TEASER = re.compile(r"(?i)\b(?:intro\s+)?(?:teaser|trailer|sneak\s+peek)\b")


def duracao_segundos(iso):
    """Converte a duracao da API (ex.: PT1H3M35S) em segundos."""
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


def detalhes(ids):
    """Busca titulo, descricao, tags, duracao e se foi live (50 por chamada).

    `liveStreamingDetails` so vem preenchido para video que foi (ou sera)
    transmissao ao vivo — e' o teste autoritativo, nao heuristica de titulo nem
    de duracao. `snippet.liveBroadcastContent` NAO serve: depois que a live
    termina ele volta para 'none'.
    """
    saida = []
    for i in range(0, len(ids), 50):
        r = api("videos", part="snippet,contentDetails,liveStreamingDetails",
                id=",".join(ids[i:i + 50]))
        for item in r.get("items", []):
            sn = item["snippet"]
            saida.append({
                "id": item["id"],
                "titulo": sn["title"],
                "descricao": sn.get("description", ""),
                "tags": sn.get("tags", []),
                "publicado": sn["publishedAt"][:10],
                "duracao": item["contentDetails"].get("duration", ""),
                "live": bool(item.get("liveStreamingDetails")),
                "canal_id": sn.get("channelId"),
            })
    return saida


def buscar_lote(playlist, conhecidos, quantos, incremental=False, desde=None):
    """Percorre os uploads do mais recente ao mais antigo.

    Ignora o que ja esta na planilha, descarta Shorts/lives/exclusivos e para
    quando juntar 'quantos' videos longos. Devolve (aprovados, ids_descartados).

    `incremental=True` liga a parada antecipada: a varredura para na primeira
    pagina inteiramente ja conhecida. So e' seguro em canal ENCERRADO, porque
    a playlist de uploads vem do mais novo para o mais antigo — se o canal foi
    consumido ate o fim, uma pagina toda conhecida significa que dali para
    baixo e' tudo antigo e ja visto. Num canal ainda em andamento isso
    perderia videos antigos que ficaram para tras, entao a varredura vai ate
    o fim. Quem decide e' o `status` em canais.json, nao um palpite.

    `desde="AAAA-MM-DD"` restringe a coleta ao que foi PUBLICADO a partir
    dessa data, e substitui a parada antecipada por uma parada por data: a
    varredura segue pagina a pagina (nao para numa pagina toda conhecida) e
    encerra quando uma pagina so traz videos novos mais antigos que o corte.
    Existe porque a parada antecipada mente em canal que foi marcado
    `encerrado` sem ter sido esgotado de verdade: no Kings and Generals a
    primeira pagina ficava toda conhecida depois de um lote, e os 21 videos
    novos das paginas seguintes eram invisiveis — enquanto 204 videos de
    2017-2019 nunca coletados continuavam no fim da lista. Com o corte por
    data, da' para pegar so o que o canal publicou desde a ultima coleta sem
    arrastar esse acervo antigo.
    """
    aprovados, descartados = [], []
    curtos, exclusivos, lives, antigos = [], [], [], 0
    pagina, vistos, chamadas = None, 0, 0
    parou_cedo = parou_por_data = False

    while len(aprovados) < quantos:
        r = api("playlistItems", part="contentDetails", playlistId=playlist,
                maxResults=50, **({"pageToken": pagina} if pagina else {}))
        chamadas += 1
        candidatos = [it["contentDetails"]["videoId"] for it in r.get("items", [])]
        vistos += len(candidatos)
        novos = [v for v in candidatos if v not in conhecidos]
        so_antigos = bool(novos)

        if novos:
            chamadas += 1
            for v in detalhes(novos):
                if desde and v["publicado"] < desde:
                    # Fora da janela pedida: nao entra no lote e nao vai para
                    # descartados.txt — nao foi recusado, so nao foi pedido.
                    antigos += 1
                    continue
                so_antigos = False
                if RE_EXCLUSIVO.search(v["titulo"]) or RE_TEASER.search(v["titulo"]):
                    exclusivos.append(v["id"])
                    descartados.append(v["id"])
                elif v.get("live"):
                    lives.append(v["id"])
                    descartados.append(v["id"])
                elif duracao_segundos(v["duracao"]) < DURACAO_MINIMA:
                    curtos.append(v["id"])
                    descartados.append(v["id"])
                elif len(aprovados) < quantos:
                    aprovados.append(v)
        elif incremental and candidatos:
            # pagina inteira ja conhecida num canal encerrado: dali para baixo
            # e' tudo mais antigo e ja visto.
            parou_cedo = True
            break

        if desde and so_antigos:
            # Uploads vem em ordem cronologica: se os videos novos desta
            # pagina ja sao todos mais antigos que o corte, dali para baixo
            # tambem sao.
            parou_por_data = True
            break

        pagina = r.get("nextPageToken")
        if not pagina:
            break

    print(f"  {vistos} videos percorridos em {chamadas} chamadas · "
          f"{len(aprovados)} aprovados · {len(curtos)} Shorts · "
          f"{len(exclusivos)} exclusivos de membros · {len(lives)} lives")
    if desde:
        print(f"  corte por data: so videos publicados a partir de {desde} · "
              f"{antigos} novos mais antigos ignorados (nao descartados)")
    if parou_cedo:
        print("  parada antecipada: pagina inteira ja conhecida (canal encerrado)")
    if parou_por_data:
        print("  parada por data: pagina so com videos anteriores ao corte")
    return aprovados[:quantos], descartados


# ───────────────────── compressao das evidencias ─────────────────────

RE_CAPITULO = re.compile(r"^\s*\(?(\d{1,2}:\d{2}(?::\d{2})?)\)?\s*[-–—:.]?\s*(.{2,80})$")
RE_TEMPO = re.compile(r"^\s*\(?\d{1,2}:\d{2}")
RE_URL = re.compile(r"https?://\S+|www\.\S+")
RE_CORTE = re.compile(
    r"(?i)^\s*(sources?|bibliograph|credits?|support us|patreon|merch|"
    r"our other|follow us|music|produced by|written by|narrat|#\w+)")
RE_DATA = re.compile(
    r"\b\d{1,4}\s*(?:BCE?|AD|CE)\b"
    r"|\b(?:1[0-9]{3}|20[0-9]{2})s?\b"
    # anos de 1-3 dígitos: só em contexto de data, para não capturar contagens.
    # (a) intervalo tipo "772-804" ou "(772-780)":
    r"|\b[1-9]\d{0,2}\s*[-–—]\s*[1-9]\d{0,3}\b"
    # (b) precedidos de preposição típica de ano: "in 782", "of 793", "by 800":
    r"|\b(?:in|of|by|from|until|to|around|circa|c\.|year)\s+[1-9]\d{2}\b"
    r"|\b\d{1,2}(?:st|nd|rd|th)\s+centur(?:y|ies)\b"
    # século em algarismo romano do lado inglês: "XI century", "the XV centuries".
    # (?-i:...) porque com o re.I global, "mid century" bateria (m/i/d são
    # letras romanas válidas) — algarismo romano só conta em maiúsculas.
    r"|(?-i:\b[IVXLCDM]+\s+centur(?:y|ies)\b)"
    # século/duração por extenso: "for two centuries", "over 200 years".
    # Achado no canal Cambrian Chronicles (lote 83): descrições em prosa dizem
    # "for two centuries" e "in over 200 years" sem nenhum outro numero na
    # evidencia, e nenhum dos padroes acima cobre nem numero por extenso nem
    # "N years" (só "century/centuries").
    r"|\b(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+centur(?:y|ies)\b"
    r"|\b(?:over|more than|nearly|almost|about)\s+\d{2,4}\s+years?\b"
    r"|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b"
    # estação do ano + ano: "By Spring 542", "In the Summer of 533". Achado no
    # canal The History of Byzantium Podcast (lote 100-102): "By Spring 542"
    # não batia com nenhum padrão acima porque a preposição ("by") não fica
    # colada no número — "Spring" entra no meio e quebra a adjacência exigida
    # pelo padrão (b). Estação por si só, como mês, aciona a janela de
    # contexto que já pega o ano vizinho.
    r"|\b(?:Spring|Summer|Autumn|Fall|Winter)\b"
    r"|\bséculo\s+[IVXL]+\b|\b(?:a\.?C\.?|d\.?C\.?)\b",
    re.I)


def capitulos(descricao, limite=20):
    achados = []
    for linha in descricao.splitlines():
        m = RE_CAPITULO.match(linha)
        if m:
            achados.append(f"{m.group(1)} {m.group(2).strip()}")
    return achados[:limite]


def limpar_descricao(descricao, limite=250):
    """Tira capitulos, links e o rodape promocional. Sobra a sinopse."""
    linhas = []
    for linha in descricao.splitlines():
        if RE_CORTE.match(linha):
            break
        if RE_TEMPO.match(linha):        # capitulos ja saem em campo proprio
            continue
        linha = RE_URL.sub("", linha)
        if linha.strip():
            linhas.append(linha.strip())
    texto = re.sub(r"\s+", " ", " ".join(linhas)).strip()
    return " ".join(texto.split()[:limite])


def mencoes_de_data(texto, limite=14, janela=8):
    """Trechos curtos ao redor de cada data, sem repetir nem sobrepor.

    A busca roda sobre o texto inteiro, nao palavra a palavra: expressoes como
    "218 BC" ou "3rd century AD" ocupam mais de uma palavra e seriam perdidas.
    """
    palavras = texto.split()
    pos, cursor = [], 0
    for p in palavras:
        cursor = texto.index(p, cursor)
        pos.append(cursor)
        cursor += len(p)

    trechos, datas_vistas, cobertos = [], set(), set()
    for m in RE_DATA.finditer(texto):
        chave = re.sub(r"\s+", " ", m.group().lower()).strip(".,;:")
        if chave in datas_vistas:
            continue
        i = max((k for k in range(len(pos)) if pos[k] <= m.start()), default=0)
        if i in cobertos:
            continue
        datas_vistas.add(chave)
        ini, fim = max(0, i - janela), min(len(palavras), i + janela + 1)
        trechos.append(" ".join(palavras[ini:fim]))
        cobertos.update(range(ini, fim))
        if len(trechos) >= limite:
            break
    return trechos


def comprimir(v):
    """Transforma um video inteiro em ~200 palavras de evidencia util."""
    p = [f"### {v['id']} · {v['titulo']}",
         f"publicado: {v['publicado']} · duracao: {v['duracao']}"]

    caps = capitulos(v["descricao"])
    if caps:
        p.append("capitulos: " + " | ".join(caps))

    desc = limpar_descricao(v["descricao"])
    if desc:
        p.append("descricao: " + desc)

    if v["tags"]:
        p.append("tags: " + " · ".join(v["tags"][:25]))

    datas = mencoes_de_data(" ".join(caps) + " " + desc)
    if datas:
        p.append("datas citadas:\n" + "\n".join(f"  - …{d}…" for d in datas))
    else:
        p.append("datas citadas: (nenhuma encontrada — classificar pelo assunto)")

    return "\n".join(p)


def proximo_numero_lote():
    """Maior lote já registrado na planilha (ou no ledger), mais um.

    Nao usa gaps em arquivos lote-NN.md no disco: esses arquivos sao
    evidencia de trabalho e podem ser apagados depois de processados,
    o que fazia essa funcao reaproveitar numeros de lote ja usados
    (coleta silenciosamente errada — o proximo lote saia rotulado
    "lote: 1" mesmo com a planilha ja no lote 16).
    """
    maior = 0
    if os.path.exists(PLANILHA):
        import openpyxl
        ws = openpyxl.load_workbook(PLANILHA, read_only=True)["Catálogo"]
        linhas = ws.iter_rows(values_only=True)
        cabecalho = next(linhas)
        if "lote" in cabecalho:
            col = cabecalho.index("lote")
            valores = [l[col] for l in linhas if isinstance(l[col], (int, float))]
            if valores:
                maior = int(max(valores))
    return maior + 1


def proximo_arquivo():
    numero = proximo_numero_lote()
    arquivo = f"lote-{numero:02d}.md"
    if os.path.exists(arquivo):
        erro(f"{arquivo} já existe no disco mas seria o próximo lote ({numero}) "
             f"pela planilha. Resolva a colisão antes de rodar de novo.")
    return arquivo


# ──────────────────────────────── main ────────────────────────────────

if __name__ == "__main__":
    # O canal pode vir da linha de comando, ou uma playlist explícita via
    # --playlist ID [--nome "..."]. `catalogados.txt` e `descartados.txt`
    # continuam compartilhados de propósito: são indexados por video_id, que é
    # único no YouTube inteiro, então servem a qualquer canal/playlist sem
    # risco de colisão. A numeração de lote também segue única, para o
    # catálogo continuar sendo uma linha do tempo só.
    modo_video = "--video" in sys.argv
    if modo_video:
        i = sys.argv.index("--video")
        if i + 1 >= len(sys.argv):
            erro("--video precisa do id ou link do vídeo logo depois.")
        video_arg = sys.argv[i + 1]
        if "--canal" not in sys.argv:
            erro("--video exige --canal <chave>, a mesma chave que já existe em "
                 "canais.json (ex.: @MagistraVitae ou playlist:ID). Vídeo de canal "
                 "novo entra pelo fluxo normal: python coletar.py @Handle.")
        j = sys.argv.index("--canal")
        if j + 1 >= len(sys.argv):
            erro("--canal precisa de um valor logo depois.")
        CHAVE_CANAL = sys.argv[j + 1]

        CHAVE = ler_chave()

        dados_canais = ler_canais()
        estado = estado_do_canal(dados_canais, CHAVE_CANAL)
        if not estado:
            erro(f"'{CHAVE_CANAL}' não está em canais.json. Adote o canal primeiro "
                 f"(python coletar.py @Handle) antes de inserir um vídeo avulso dele.")
        nome_canal = estado["nome"]
        video_id = extrair_video_id(video_arg)

        print(f"\n--video {video_id} · canal {CHAVE_CANAL} ({nome_canal})\n")

        catalogados = ids_ja_registrados()
        ja_enviados = ler_lista(ARQUIVO_CATALOGADOS)
        descartes_antigos = ler_descartados()
        conhecidos = catalogados | ja_enviados | descartes_antigos
        if video_id in conhecidos:
            erro(f"{video_id} já está catalogado, no ledger ou nos descartados. Nada a fazer.")

        encontrados = detalhes([video_id])
        if not encontrados:
            erro(f"vídeo '{video_id}' não encontrado pela API (removido, privado, ou id errado).")
        v = encontrados[0]

        if not CHAVE_CANAL.startswith("playlist:"):
            canal_id_esperado = canal_id_de(CHAVE_CANAL)
            if v["canal_id"] != canal_id_esperado:
                erro(f"'{v['titulo']}' ({video_id}) pertence a outro canal do YouTube "
                     f"(channelId {v['canal_id']}), não a {CHAVE_CANAL} "
                     f"({canal_id_esperado}). Confira o link antes de tentar de novo.")

        if RE_EXCLUSIVO.search(v["titulo"]) or RE_TEASER.search(v["titulo"]):
            gravar_descartados([video_id])
            erro(f"'{v['titulo']}' parece exclusivo de membros/teaser pelo título — "
                 f"descartado, não entraria no catálogo nem num lote normal.")
        if v.get("live"):
            gravar_descartados([video_id])
            erro(f"'{v['titulo']}' foi (ou será) transmissão ao vivo — descartado, live não entra no catálogo.")
        if duracao_segundos(v["duracao"]) < DURACAO_MINIMA:
            gravar_descartados([video_id])
            erro(f"'{v['titulo']}' tem menos de {DURACAO_MINIMA}s — é Short, descartado.")

        bloco = comprimir(v)
        sem_data = 1 if "nenhuma encontrada" in bloco else 0

        arquivo = proximo_arquivo()
        numero = int(re.search(r"\d+", arquivo).group())
        hoje = datetime.date.today().isoformat()
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(f"# Lote {numero:02d} — {nome_canal} (vídeo avulso)\n\n")
            f.write(f"lote: {numero}\n")
            f.write(f"coletado em: {hoje}\n")
            f.write(f"1 video (inserção manual via --video) · {sem_data} sem "
                    f"nenhuma data na evidencia · 0 descartados\n\n---\n\n")
            f.write(bloco)

        gravar_lista(ARQUIVO_CATALOGADOS, [video_id])
        reg = registrar_coleta(CHAVE_CANAL, nome_canal, numero)

        print(f"Pronto: {arquivo}")
        print(f"1 video · {v['titulo'][:70]}")
        print(f"canais.json atualizado: {CHAVE_CANAL} · status '{reg['status']}' · "
              f"lotes {reg['primeiro_lote']}-{reg['ultimo_lote']}")
        print("Suba esse arquivo na conversa junto com a planilha.\n")
        sys.exit(0)

    modo_playlist = "--playlist" in sys.argv
    if modo_playlist:
        i = sys.argv.index("--playlist")
        if i + 1 >= len(sys.argv):
            erro("--playlist precisa do ID da playlist logo depois (o trecho depois de 'list=' na URL).")
        playlist_id_cli = sys.argv[i + 1]
        nome_cli = None
        if "--nome" in sys.argv:
            j = sys.argv.index("--nome")
            if j + 1 >= len(sys.argv):
                erro("--nome precisa de um valor logo depois.")
            nome_cli = sys.argv[j + 1]
        # Chave própria em canais.json — nunca reaproveita @handle, porque a
        # playlist pode não pertencer a um canal de história (ver
        # resolver_playlist_explicita).
        CHAVE_CANAL = f"playlist:{playlist_id_cli}"
    else:
        if len(sys.argv) > 1:
            CANAL = sys.argv[1]
        CHAVE_CANAL = CANAL

    # --desde AAAA-MM-DD: coletar so o que o canal publicou a partir dessa
    # data. Desliga a parada antecipada, que nao e' confiavel em canal
    # marcado `encerrado` sem esgotamento real (ver buscar_lote).
    DESDE = None
    if "--desde" in sys.argv:
        i = sys.argv.index("--desde")
        if i + 1 >= len(sys.argv):
            erro("--desde precisa de uma data AAAA-MM-DD logo depois.")
        DESDE = sys.argv[i + 1]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", DESDE):
            erro(f"--desde espera AAAA-MM-DD, veio {DESDE!r}.")

    CHAVE = ler_chave()

    estado = estado_do_canal(ler_canais(), CHAVE_CANAL)
    encerrado = estado.get("status") == "encerrado"
    if not estado:
        print(f"\n{CHAVE_CANAL} · lote de {TAMANHO_LOTE} · NOVO\n")
    elif encerrado:
        print(f"\n{CHAVE_CANAL} · lote de {TAMANHO_LOTE} · revisita "
              f"(encerrado em {estado.get('encerrado_em', '?')}, "
              f"lotes {estado.get('primeiro_lote', '?')}-"
              f"{estado.get('ultimo_lote', '?')}) · parada antecipada "
              f"{'desligada (corte por data)' if DESDE else 'desligada (playlist explícita)' if modo_playlist else 'ligada'}\n")
    else:
        print(f"\n{CHAVE_CANAL} · lote de {TAMANHO_LOTE} · em andamento "
              f"(último lote: {estado.get('ultimo_lote', '?')})\n")

    catalogados = ids_ja_registrados()
    ja_enviados = ler_lista(ARQUIVO_CATALOGADOS)
    descartes_antigos = ler_descartados()
    conhecidos = catalogados | ja_enviados | descartes_antigos
    print(f"ja catalogados: {len(catalogados)} na planilha"
          f" · {len(ja_enviados)} no ledger"
          f" · {len(descartes_antigos)} descartados"
          f" · {len(conhecidos)} conhecidos no total")
    if catalogados and not catalogados <= ja_enviados:
        faltam = len(catalogados - ja_enviados)
        print(f"aviso: {faltam} ids estao na planilha mas nao no ledger — registrando agora.")
        gravar_lista(ARQUIVO_CATALOGADOS, catalogados - ja_enviados)

    if modo_playlist:
        playlist, nome_canal = resolver_playlist_explicita(
            playlist_id_cli, nome_cli or estado.get("nome"))
        print(f"playlist encontrada: {nome_canal}")
    else:
        playlist, nome_canal = playlist_de_uploads(CANAL)
        print(f"canal encontrado: {nome_canal}")

    # Playlist explícita: a ordem dos itens é quem a organizou que decide, não
    # necessariamente do mais novo pro mais antigo (aqui era por número de
    # episódio). A parada antecipada de canal encerrado só é segura porque o
    # uploads do canal é garantidamente cronológico — nunca ligar para
    # playlist explícita, mesmo que ela já esteja marcada encerrado.
    videos, descartados = buscar_lote(
        playlist, conhecidos, TAMANHO_LOTE,
        incremental=(encerrado and not modo_playlist and not DESDE),
        desde=DESDE)
    if descartados:
        gravar_descartados(descartados)

    if not videos:
        print("\nNenhum video longo novo. Voce esta em dia com este canal.\n")
        sys.exit(0)

    if encerrado and len(videos) < TAMANHO_LOTE:
        print(f"\nrevisita: {len(videos)} video(s) novo(s) — lote parcial, "
              f"e' o esperado num canal encerrado.")

    blocos, sem_data = [], 0
    for i, v in enumerate(videos, 1):
        bloco = comprimir(v)
        if "nenhuma encontrada" in bloco:
            sem_data += 1
        blocos.append(bloco)
        print(f"  [{i}/{len(videos)}] {v['titulo'][:60]}")

    arquivo = proximo_arquivo()
    numero = int(re.search(r"\d+", arquivo).group())
    hoje = datetime.date.today().isoformat()
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(f"# Lote {numero:02d} — {nome_canal}\n\n")
        f.write(f"lote: {numero}\n")
        f.write(f"coletado em: {hoje}\n")
        f.write(f"{len(videos)} videos · {sem_data} sem nenhuma data na evidencia · "
                f"{len(descartados)} descartados\n\n---\n\n")
        f.write("\n\n".join(blocos))

    gravar_lista(ARQUIVO_CATALOGADOS, [v["id"] for v in videos])
    reg = registrar_coleta(CHAVE_CANAL, nome_canal, numero)

    palavras = sum(len(b.split()) for b in blocos)
    print(f"\nPronto: {arquivo}")
    print(f"{len(videos)} videos · ~{palavras} palavras · {sem_data} sem data na evidencia")
    print(f"canais.json atualizado: {CHAVE_CANAL} · status '{reg['status']}' · "
          f"lotes {reg['primeiro_lote']}-{reg['ultimo_lote']}")
    print("Suba esse arquivo na conversa junto com a planilha.\n")
