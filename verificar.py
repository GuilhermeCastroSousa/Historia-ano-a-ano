"""
Checklist executável do catálogo. Roda antes de salvar a planilha, sempre.

Converte em código o que antes era uma lista em prosa no protocolo.md. Erros
de montagem já aconteceram: linhas que perderam 'publicado' e 'Título' por um
desalinhamento de tupla, e linhas boas apagadas durante a correção. Nenhum dos
dois teria passado por aqui.

Uso:
    python verificar.py                       # confere a planilha atual
    python verificar.py --anterior backup.xlsx   # e compara com a versão anterior

Sai com código 0 se tudo passou, 1 se houve falha. Nunca escreve nada.
"""

import argparse
import os
import re
import sys

import openpyxl

PLANILHA = "playlist-historia-v2.xlsx"
ABA = "Catálogo"

COLUNAS = ["Século/Período", "Ano", "Mês", "Dias", "Região", "Tema", "Subtema",
           "Canal", "Título", "Link", "publicado", "ano_inicio", "ano_fim",
           "video_id", "confianca", "status", "travado", "notas", "lote"]

CONFIANCAS = {"alta", "média", "chute", "n/a"}
STATUS = {"ok", "revisar"}

# Rótulos de linha que não fica na linha do tempo. Os dois têm a mesma forma
# (anos vazios, confianca 'n/a', travado 'sim') e ordenam no fim da planilha,
# mas dizem coisas diferentes:
#   Extra     — é história, mas sem período que dê para fixar (recepção do
#               passado no presente, ou assunto que atravessa milênios).
#   Aleatório — não é história. O canal publicou, o catálogo registra, mas o
#               vídeo não trata de período histórico nenhum (ficção, cultura
#               de internet). Entrou na adoção do canal Thersites the Historian.
# Não são deriváveis dos anos como o resto da Lista A: quem classifica escolhe
# qual dos dois, porque a diferença está no assunto, não na datação.
SEM_PERIODO = {"Extra", "Aleatório"}

PREFIXO_LINK = "https://www.youtube.com/watch?v="
PARTES_PREFIXO_LINK = [
    ("esquema 'https://'", "https://"),
    ("'www.'", "www."),
    ("domínio 'youtube.com'", "youtube.com"),
    ("caminho '/watch?v='", "/watch?v="),
]


def parte_divergente(link):
    """Aponta qual pedaço do prefixo canônico do link não bateu."""
    acumulado = ""
    for nome, parte in PARTES_PREFIXO_LINK:
        acumulado += parte
        if not link.startswith(acumulado):
            return nome
    return None


LIMIAR_PANORAMA = 300


def _rotulo_ano(a):
    """Ano no estilo da Lista A: negativo vira 'N a.C.', positivo fica nu."""
    return f"{abs(a)} a.C." if a < 0 else str(a)


def periodo(ai, af):
    """Lista A: rótulo calculado pelo ponto médio. Nunca escolhido no olho.

    Faixa de LIMIAR_PANORAMA anos ou mais não passa pelo ponto médio: a média
    de uma faixa larga não é um período, é aritmética. Um vídeo sobre a marinha
    bizantina (330-1453) caía em '800 - 900', e os Ilírios (1000 a.C.-600 d.C.)
    em 'Apogeu da República' — rótulos que o vídeo não trata. Esses casos
    mostram a própria faixa. Ver protocolo.md, 'Extra virou balde'.
    """
    if ai is None or af is None:
        return "Extra"
    if af - ai >= LIMIAR_PANORAMA:
        return f"Panorama ({_rotulo_ano(ai)} - {_rotulo_ano(af)})"
    m = (ai + af) / 2
    if m <= -1100: return "Antiguidade remota (até 1100 a.C.)"
    if m <= -800:  return "Período homérico (1100 a.C. - 800 a.C.)"
    if m <= -500:  return "Época Arcaica (800 a.C. - 500 a.C.)"
    if m <= -250:  return "Apogeu Grego (500 a.C. - 250 a.C.)"
    if m <= 0:     return "Apogeu da República (250 a.C. - 0)"
    if m <= 250:   return "Apogeu Romano (0 - 250)"
    if m <= 500:   return "Antiguidade Tardia (250 - 500)"
    if m < 1900:
        i = int(m // 100) * 100
        return f"{i} - {i + 100}"
    if m < 1925:   return "1900 - 1925"
    if m < 1950:   return "1925 - 1950"
    if m < 2000:   return "1950 - 2000"
    return "2000+"


def num(v):
    """Primeiro número de um campo como '8 - 9', '02 - 09', '6.0', '*'."""
    if v is None:
        return 0
    m = re.match(r"\s*0*(\d+)", str(v))
    return int(m.group(1)) if m else 0


def parse_ano(txt):
    """Lê o campo texto `Ano` e devolve (ini, fim), ou None se não souber ler.

    O protocolo diz que `ano_inicio`/`ano_fim` saem do parser de `Ano`. Se os
    dois discordam, um dos lados está errado e ninguém percebia: até a revisão
    das pendentes (28/07/2026) havia 66 divergências silenciosas no catálogo.
    """
    if txt is None:
        return None
    s = str(txt).strip()
    if s in ("*", ""):
        return (None, None)

    m = re.fullmatch(r"(\d{3,4})s", s)          # década: '800s' → 800-809
    if m:
        a = int(m.group(1))
        return (a, a + 9)

    def um(tok):
        tok = tok.strip()
        mm = re.fullmatch(r"(\d+)\s*a\.?\s*C\.?", tok, re.I)
        if mm:
            return -int(mm.group(1))
        mm = re.fullmatch(r"(\d+)\s*d\.?\s*C\.?", tok, re.I)
        if mm:
            return int(mm.group(1))
        mm = re.fullmatch(r"(\d+)", tok)
        if mm:
            return int(mm.group(1))
        return None

    partes = re.split(r"\s[-–—]\s", s)
    if len(partes) == 2:
        a, b = um(partes[0]), um(partes[1])
        return (a, b) if a is not None and b is not None else None
    if len(partes) == 1:
        a = um(partes[0])
        if a is not None:
            return (a, a)
    return None


def carregar(caminho):
    if not os.path.exists(caminho):
        print(f"ERRO: {caminho} não encontrada.")
        sys.exit(1)
    wb = openpyxl.load_workbook(caminho, read_only=True)
    if ABA not in wb.sheetnames:
        print(f"ERRO: {caminho} não tem a aba '{ABA}'.")
        sys.exit(1)
    ws = wb[ABA]
    linhas = ws.iter_rows(values_only=True)
    cab = list(next(linhas))
    return cab, [dict(zip(cab, r)) for r in linhas]


def verificar(caminho, anterior=None):
    cab, rows = carregar(caminho)
    falhas = []
    avisos = []

    def falha(msg):
        falhas.append(msg)

    # ── estrutura ──
    if cab != COLUNAS:
        falha(f"cabeçalho mudou.\n    esperado: {COLUNAS}\n    achado:   {cab}")
        return falhas, avisos, rows

    # ── video_id ──
    ids = [r["video_id"] for r in rows]
    vazios = [i for i, v in enumerate(ids, 2) if not v]
    if vazios:
        falha(f"video_id vazio nas linhas {vazios}")
    repetidos = {v for v in ids if v and ids.count(v) > 1}
    if repetidos:
        falha(f"video_id repetido: {sorted(repetidos)}")

    # colisão com descartados
    if os.path.exists("descartados.txt"):
        desc = {l.strip() for l in open("descartados.txt", encoding="utf-8") if l.strip()}
        col = desc & set(ids)
        if col:
            falha(f"ids que estão no catálogo E em descartados.txt: {sorted(col)}")

    # ── campos obrigatórios ──
    for r in rows:
        vid = r["video_id"]
        for c in ("Região", "Tema", "Canal", "Título", "Link", "publicado", "lote"):
            if r[c] in (None, ""):
                falha(f"{vid}: '{c}' vazio")
        if r["confianca"] not in CONFIANCAS:
            falha(f"{vid}: confianca inválida ({r['confianca']!r})")
        if r["status"] not in STATUS:
            falha(f"{vid}: status inválido ({r['status']!r})")

    # ── link tem que bater com o video_id (armadilha da URL falsa) ──
    for r in rows:
        link, vid = str(r["Link"] or ""), r["video_id"]
        if vid and vid not in link:
            falha(f"{vid}: Link não contém o video_id — {link!r}")
        if link and not link.startswith(PREFIXO_LINK):
            parte = parte_divergente(link)
            avisos.append(f"{vid}: Link fora do padrão — {parte} não bate — {link!r}")

    # ── o texto `Ano` tem que bater com ano_inicio/ano_fim ──
    # São o mesmo dado em duas formas: `Ano` é o que o humano lê, os inteiros
    # são o que ordena a planilha. Divergência silenciosa entre eles deixa a
    # linha aparecendo num lugar e dizendo outro.
    for r in rows:
        lido = parse_ano(r["Ano"])
        if lido is None:
            falha(f"{r['video_id']}: campo Ano ilegível para o parser — {r['Ano']!r}")
        elif lido != (r["ano_inicio"], r["ano_fim"]):
            falha(f"{r['video_id']}: Ano={r['Ano']!r} vira {lido[0]}..{lido[1]}, "
                  f"mas a planilha traz {r['ano_inicio']}..{r['ano_fim']}")

    # ── Século/Período é calculado, não escolhido ──
    # Única exceção: linha sem período (Extra / Aleatório). Aí a escada não tem
    # o que calcular e quem classifica escolhe entre os dois — a diferença está
    # no assunto do vídeo, não na datação. Ver SEM_PERIODO, no topo.
    for r in rows:
        if r["Século/Período"] in SEM_PERIODO:
            continue
        esperado = periodo(r["ano_inicio"], r["ano_fim"])
        if r["Século/Período"] != esperado:
            falha(f"{r['video_id']}: Século/Período é {r['Século/Período']!r}, "
                  f"a escada dá {esperado!r}")

    # ── ordenação ──
    INF = float("inf")
    def chave(r):
        return (r["ano_inicio"] if r["ano_inicio"] is not None else INF,
                r["ano_fim"] if r["ano_fim"] is not None else INF,
                num(r["Mês"]), num(r["Dias"]))
    for a, b in zip(rows, rows[1:]):
        if chave(a) > chave(b):
            falha(f"fora de ordem: {a['video_id']} antes de {b['video_id']}")
            break

    # ── Extras e Aleatórios ──
    # Mesma forma para os dois: sem anos, confianca 'n/a', travado. Um vídeo que
    # não fica na linha do tempo não tem data a estimar, então não há confiança
    # a registrar — e sem esta checagem uma linha poderia ficar meio dentro,
    # meio fora (rótulo de fora, anos de dentro).
    for r in rows:
        rotulo = r["Século/Período"]
        fora = rotulo in SEM_PERIODO
        sem_ano = r["ano_inicio"] is None and r["ano_fim"] is None
        if fora != sem_ano:
            falha(f"{r['video_id']}: {rotulo!r} e anos vazios têm que andar juntos")
        if fora:
            if r["confianca"] != "n/a":
                falha(f"{r['video_id']}: {rotulo} tem que ter confianca 'n/a'")
            if r["travado"] != "sim":
                falha(f"{r['video_id']}: {rotulo} tem que entrar travado")

    # ── confiança x status ──
    # confianca registra a origem da data (o quão bem embasada ela é); status
    # registra o fluxo de revisão (se um humano ainda precisa olhar a linha).
    # São eixos diferentes: uma linha 'chute'/'média' normalmente pede revisão,
    # mas travado='sim' significa que um humano já revisou e aprovou o palpite
    # — nesse caso status='ok' é legítimo mesmo com confianca baixa.
    for r in rows:
        if r["confianca"] in ("média", "chute") and r["status"] != "revisar" and r["travado"] != "sim":
            falha(f"{r['video_id']}: confianca {r['confianca']} exige status 'revisar' (ou travado='sim')")

    # ── comparação com a versão anterior ──
    if anterior:
        _, antes = carregar(anterior)
        # A versão anterior pode estar suja — já apareceu backup com linhas
        # fantasma (todas as células vazias) porque uma remoção zerou células em
        # vez de apagar linhas, e a dimensão gravada no .xlsx ficou obsoleta.
        # Sem este filtro o portão morria com TypeError em vez de acusar. Portão
        # que quebra não é portão: ele tem que sobreviver a entrada ruim e
        # reportar.
        fantasmas = [r for r in antes if not r["video_id"]]
        if fantasmas:
            avisos.append(f"{anterior}: {len(fantasmas)} linha(s) sem video_id "
                          f"na versão anterior, ignoradas na comparação")
            antes = [r for r in antes if r["video_id"]]
        mapa = {r["video_id"]: r for r in antes}
        travadas_alteradas, sumidas, novas_pre_travadas = [], [], []
        for vid, r0 in mapa.items():
            atual = next((r for r in rows if r["video_id"] == vid), None)
            if atual is None:
                sumidas.append(vid)
                continue
            if r0.get("travado") == "sim":
                dif = [c for c in COLUNAS if r0[c] != atual[c]]
                if dif:
                    travadas_alteradas.append(f"{vid} ({', '.join(dif)})")
        if travadas_alteradas:
            falha("linhas TRAVADAS alteradas: " + "; ".join(travadas_alteradas))
        # ── linha nova não pode chegar travada ──
        # travado='sim' marca trabalho humano (protocolo.md, "Linhas travadas"):
        # Extra é travado por design na criação; toda outra linha só deve ganhar
        # travado='sim' via /aprovar ou correção humana detectada num diff
        # posterior. Uma linha que não existia na versão anterior e já chega
        # travada não passou por isso — o gate confiança×status vira decorativo,
        # porque qualquer linha nasce "aprovada" antes de qualquer humano olhar.
        for r in rows:
            vid = r["video_id"]
            if vid in mapa:
                continue
            if r["Século/Período"] not in SEM_PERIODO and r["travado"] == "sim":
                novas_pre_travadas.append(vid)
        if novas_pre_travadas:
            falha("linha(s) nova(s) chegam travado='sim' sem passar por /aprovar: "
                  + ", ".join(sorted(novas_pre_travadas)))
        if sumidas:
            fora = [v for v in sumidas
                    if not (os.path.exists("descartados.txt")
                            and v in open("descartados.txt", encoding="utf-8").read())]
            if fora:
                falha(f"linhas sumiram sem ir para descartados.txt: {fora}")
            else:
                avisos.append(f"{len(sumidas)} linha(s) removida(s), já em descartados.txt")
        novas = len(rows) - (len(antes) - len(sumidas))
        print(f"  anterior: {len(antes)} linhas · agora: {len(rows)} · "
              f"novas: {novas} · removidas: {len(sumidas)}")

    return falhas, avisos, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("planilha", nargs="?", default=PLANILHA)
    ap.add_argument("--anterior", help="versão anterior, para comparar linhas travadas")
    args = ap.parse_args()

    print(f"\nVerificando {args.planilha}")
    falhas, avisos, rows = verificar(args.planilha, args.anterior)

    import collections
    # 'lote' vazio já vira falha em campos obrigatórios, mas essa checagem só
    # aparece depois — este resumo roda antes e não pode confiar que todo
    # 'lote' é comparável (None vs int quebra o sorted() por padrão).
    lotes = collections.Counter(r["lote"] for r in rows)
    print(f"  {len(rows)} linhas · "
          f"lotes {dict(sorted(lotes.items(), key=lambda kv: (kv[0] is None, kv[0])))}")
    print(f"  status {dict(collections.Counter(r['status'] for r in rows))} · "
          f"confiança {dict(collections.Counter(r['confianca'] for r in rows))}")

    for a in avisos:
        print(f"  aviso: {a}")

    if falhas:
        print(f"\n{len(falhas)} FALHA(S) — não salve a planilha assim:\n")
        for f in falhas:
            print(f"  - {f}")
        print()
        sys.exit(1)

    print("\n  checklist passou.\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
