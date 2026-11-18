#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subir_playlist.py — sobe uma lista de vídeos do YouTube (CSV ou .txt) para uma
playlist sua, na ordem em que aparecem no arquivo.

Usa SOMENTE a YouTube Data API oficial. Não raspa nada, não usa cookie de conta
logada, não automatiza navegador.

POR QUE OAUTH E NÃO A CHAVE DE SEMPRE
─────────────────────────────────────
A chave de API (~/.chaves/youtube.txt, usada pelo coletar.py) só autoriza
LEITURA. Escrever numa playlist é ação em nome da sua conta, e para isso o
YouTube exige OAuth 2.0. Por isso este script tem credenciais próprias:

    ~/.chaves/client_secret.json   você baixa do Google Cloud Console (uma vez)
    ~/.chaves/token-youtube.json   o script cria sozinho na 1ª autorização

Nenhum dos dois entra no repositório (ver .gitignore).

COMO USAR
─────────
    python subir_playlist.py lista.csv --playlist PLxxxxxxxx
    python subir_playlist.py lista.csv --nova "História — ano a ano"
    python subir_playlist.py lista.csv --playlist PLxxx --simular
    python subir_playlist.py --playlists          # lista suas playlists e sai

O arquivo de entrada pode ser:
  • um CSV com uma coluna de links ou de IDs (o script acha a coluna sozinho,
    ou você aponta com --coluna NOME);
  • um .txt com um link por linha.

SEGURO DE REPETIR
─────────────────
Antes de subir qualquer coisa, o script lê o que JÁ está na playlist e pula
esses vídeos. Então:
  • rodar duas vezes o mesmo arquivo não duplica nada;
  • se parar no meio (quota, queda de internet), é só rodar de novo que ele
    retoma de onde estava;
  • mandar um arquivo novo depois só acrescenta o que falta, no fim da playlist.

QUOTA
─────
Cada inserção custa 50 unidades e a quota é 10.000/dia. Descontando a leitura
da playlist, dá **199 vídeos por dia** — medido na prática, não estimado. Faça
os arquivos de 199 linhas que cada um fecha um dia redondo.

A quota zera à meia-noite no horário do Pacífico, ou seja, por volta das 4h-5h
da manhã no horário de Brasília. Quando ela acaba, o script para com uma
mensagem dizendo quantos faltaram; rode de novo no dia seguinte.
"""

import argparse
import csv
import os
import re
import time
import sys

PASTA_CHAVES = os.path.join(os.path.expanduser("~"), ".chaves")
CLIENT_SECRET = os.path.join(PASTA_CHAVES, "client_secret.json")
TOKEN = os.path.join(PASTA_CHAVES, "token-youtube.json")

ESCOPO = ["https://www.googleapis.com/auth/youtube"]

CUSTO_INSERCAO = 50  # unidades de quota por playlistItems.insert


def erro(msg):
    print(f"\nERRO: {msg}\n", file=sys.stderr)
    sys.exit(1)


# ─────────────────────────────── autenticação ───────────────────────────────

def autenticar():
    """Devolve um cliente da API já autorizado na sua conta.

    Na primeira vez abre o navegador para você aprovar. Depois disso reusa o
    token salvo e renova sozinho quando expira.
    """
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        erro("faltam bibliotecas. Rode:\n"
             "    python -m pip install google-auth-oauthlib google-api-python-client")

    cred = None
    if os.path.exists(TOKEN):
        cred = Credentials.from_authorized_user_file(TOKEN, ESCOPO)

    if not cred or not cred.valid:
        renovado = False
        if cred and cred.expired and cred.refresh_token:
            try:
                cred.refresh(Request())
                renovado = True
            except Exception:
                # Acontece quando o app OAuth está em "Testing": o Google
                # invalida o refresh token a cada 7 dias. Basta autorizar de
                # novo (ou publicar o app — ver GUIA.md).
                print("O token expirou. Vou pedir a autorização de novo.")
                cred = None
        if not renovado:
            if not os.path.exists(CLIENT_SECRET):
                erro(f"não encontrei {CLIENT_SECRET}.\n"
                     "Crie uma credencial OAuth do tipo 'Desktop app' no Google Cloud\n"
                     "Console (mesmo projeto da chave de API), baixe o JSON e salve\n"
                     "nesse caminho. O passo a passo está no GUIA.md.")
            fluxo = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, ESCOPO)
            print("Abrindo o navegador para você autorizar o acesso à sua conta...")
            cred = fluxo.run_local_server(port=0)
        os.makedirs(PASTA_CHAVES, exist_ok=True)
        with open(TOKEN, "w", encoding="utf-8") as f:
            f.write(cred.to_json())
        print(f"Token salvo em {TOKEN} — as próximas execuções não pedem login.")

    return build("youtube", "v3", credentials=cred)


# ──────────────────────────── leitura do arquivo ────────────────────────────

# Um id de vídeo do YouTube: 11 caracteres de [A-Za-z0-9_-].
ID_SOLTO = re.compile(r"^[A-Za-z0-9_-]{11}$")
ID_EM_LINK = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:[^ ]*&)?v=|embed/|shorts/|live/)|youtu\.be/)"
    r"([A-Za-z0-9_-]{11})"
)


def extrair_id(texto):
    """Tira o video_id de um link, ou aceita o id cru. Devolve None se não for."""
    if not texto:
        return None
    texto = texto.strip().strip('"').strip("'")
    if ID_SOLTO.match(texto):
        return texto
    m = ID_EM_LINK.search(texto)
    return m.group(1) if m else None


def ler_entrada(caminho, coluna=None):
    """Lê o arquivo e devolve a lista de video_ids, na ordem, sem repetição.

    Aceita CSV (acha sozinho a coluna com mais links, ou usa --coluna) e .txt
    com um link por linha.
    """
    if not os.path.exists(caminho):
        erro(f"não encontrei o arquivo {caminho}")

    with open(caminho, encoding="utf-8-sig", newline="") as f:
        bruto = f.read()

    ids = []

    if caminho.lower().endswith((".csv", ".tsv")):
        delim = "\t" if caminho.lower().endswith(".tsv") else None
        if delim is None:
            try:
                delim = csv.Sniffer().sniff(bruto[:4096], delimiters=",;\t").delimiter
            except csv.Error:
                delim = ","
        linhas = list(csv.reader(bruto.splitlines(), delimiter=delim))
        if not linhas:
            erro("o arquivo está vazio.")

        cabecalho = linhas[0]
        corpo = linhas[1:]

        # Se o "cabeçalho" já é um link, o arquivo não tem cabeçalho.
        if any(extrair_id(c) for c in cabecalho):
            corpo = linhas
            cabecalho = None

        if coluna is not None:
            if not cabecalho or coluna not in cabecalho:
                erro(f"coluna '{coluna}' não existe. Colunas: {cabecalho}")
            alvo = cabecalho.index(coluna)
        else:
            # Escolhe a coluna que produz mais ids válidos.
            larg = max(len(l) for l in corpo) if corpo else 0
            placar = [sum(1 for l in corpo if i < len(l) and extrair_id(l[i]))
                      for i in range(larg)]
            if not placar or max(placar) == 0:
                erro("não encontrei nenhum link ou id do YouTube no arquivo.")
            alvo = placar.index(max(placar))
            if cabecalho and alvo < len(cabecalho):
                print(f"Coluna usada: '{cabecalho[alvo]}' (posição {alvo + 1}).")

        brutos = [l[alvo] for l in corpo if alvo < len(l)]
    else:
        brutos = bruto.splitlines()

    vistos = set()
    ignoradas = 0
    for item in brutos:
        vid = extrair_id(item)
        if not vid:
            if item.strip():
                ignoradas += 1
            continue
        if vid in vistos:
            continue
        vistos.add(vid)
        ids.append(vid)

    if ignoradas:
        print(f"Aviso: {ignoradas} linha(s) sem link reconhecível foram ignoradas.")
    if not ids:
        erro("nenhum vídeo válido encontrado no arquivo.")
    return ids


# ──────────────────────────────── playlists ─────────────────────────────────

def listar_playlists(yt):
    """Todas as playlists da conta autorizada."""
    saida, token = [], None
    while True:
        r = yt.playlists().list(part="snippet,contentDetails", mine=True,
                                maxResults=50, pageToken=token).execute()
        for p in r.get("items", []):
            saida.append((p["id"], p["snippet"]["title"],
                          p["contentDetails"]["itemCount"]))
        token = r.get("nextPageToken")
        if not token:
            break
    return saida


def criar_playlist(yt, titulo, privacidade="private"):
    r = yt.playlists().insert(
        part="snippet,status",
        body={"snippet": {"title": titulo},
              "status": {"privacyStatus": privacidade}},
    ).execute()
    return r["id"]


def ids_ja_na_playlist(yt, playlist_id):
    """Video_ids que já estão na playlist. É o que torna o script repetível."""
    dentro, token = set(), None
    while True:
        r = yt.playlistItems().list(part="contentDetails", playlistId=playlist_id,
                                    maxResults=50, pageToken=token).execute()
        for item in r.get("items", []):
            dentro.add(item["contentDetails"]["videoId"])
        token = r.get("nextPageToken")
        if not token:
            break
    return dentro


def inserir(yt, playlist_id, video_id):
    yt.playlistItems().insert(
        part="snippet",
        body={"snippet": {"playlistId": playlist_id,
                          "resourceId": {"kind": "youtube#video",
                                         "videoId": video_id}}},
    ).execute()


def motivo_do_erro(exc):
    """Extrai o 'reason' da resposta de erro da API, quando existe."""
    try:
        import json
        corpo = json.loads(exc.content.decode("utf-8"))
        return corpo["error"]["errors"][0].get("reason", "")
    except Exception:
        return ""


# ────────────────────────────────── main ────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description="Sobe uma lista de vídeos do YouTube para uma playlist sua, na ordem.")
    p.add_argument("arquivo", nargs="?", help="CSV ou .txt com os links/ids")
    p.add_argument("--playlist", help="id da playlist de destino (começa com PL)")
    p.add_argument("--nova", metavar="TITULO",
                   help="cria uma playlist nova com esse título e sobe nela")
    p.add_argument("--publica", action="store_true",
                   help="com --nova, cria pública (o padrão é privada)")
    p.add_argument("--coluna", help="nome da coluna do CSV que tem os links")
    p.add_argument("--limite", type=int, metavar="N",
                   help="sobe no máximo N vídeos nesta execução")
    p.add_argument("--simular", action="store_true",
                   help="mostra o que faria, sem escrever nada na sua conta")
    p.add_argument("--playlists", action="store_true",
                   help="lista suas playlists com id e contagem, e sai")
    args = p.parse_args()

    yt = autenticar()

    if args.playlists:
        print()
        for pid, titulo, n in listar_playlists(yt):
            print(f"  {pid}  {n:>4} vídeos  {titulo}")
        print()
        return

    if not args.arquivo:
        erro("informe o arquivo de entrada (ou use --playlists).")
    if not args.playlist and not args.nova:
        erro("informe o destino: --playlist <id> ou --nova \"<título>\".")

    ids = ler_entrada(args.arquivo, args.coluna)
    print(f"{len(ids)} vídeo(s) únicos lidos de {args.arquivo}.")

    if args.nova:
        if args.simular:
            print(f"[simulação] criaria a playlist \"{args.nova}\".")
            playlist_id, ja_dentro = "(simulada)", set()
        else:
            playlist_id = criar_playlist(
                yt, args.nova, "public" if args.publica else "private")
            print(f"Playlist criada: {playlist_id}  \"{args.nova}\"")
            ja_dentro = set()
    else:
        playlist_id = args.playlist
        try:
            ja_dentro = ids_ja_na_playlist(yt, playlist_id)
        except Exception as e:
            erro(f"não consegui ler a playlist {playlist_id}. "
                 f"Confira o id e se ela é sua.\n{e}")
        print(f"A playlist já tem {len(ja_dentro)} vídeo(s).")

    faltam = [v for v in ids if v not in ja_dentro]
    pulados = len(ids) - len(faltam)
    if pulados:
        print(f"{pulados} já estava(m) na playlist — serão pulados.")
    if not faltam:
        print("Nada a fazer: a playlist já tem todos os vídeos da lista.")
        return

    if args.limite:
        faltam = faltam[:args.limite]

    custo = len(faltam) * CUSTO_INSERCAO
    print(f"A subir: {len(faltam)} vídeo(s) — custo estimado {custo} unidades de quota.")
    if len(faltam) > 199:
        print("Aviso: o teto é 199 por dia (10.000 unidades / 50 por inserção, "
              "menos a leitura da playlist). O script vai parar quando a quota "
              "acabar e você retoma amanhã com o mesmo comando.")

    if args.simular:
        print("\n[simulação] nada foi escrito. Ordem de inserção:")
        for i, v in enumerate(faltam, 1):
            print(f"  {i:>4}. https://www.youtube.com/watch?v={v}")
        return

    try:
        from googleapiclient.errors import HttpError
    except ImportError:
        erro("faltam bibliotecas do Google. Veja as instruções acima.")

    subidos, falhas, acabou_quota = 0, [], False
    for i, vid in enumerate(faltam, 1):
        for tentativa in range(4):
            try:
                inserir(yt, playlist_id, vid)
                subidos += 1
                print(f"  [{i}/{len(faltam)}] ok  {vid}")
                break
            except HttpError as e:
                motivo = motivo_do_erro(e)
                if motivo == "quotaExceeded":
                    # Cota diária. Não adianta insistir hoje.
                    acabou_quota = True
                    break
                if motivo in ("rateLimitExceeded", "backendError",
                              "internalServerError") and tentativa < 3:
                    # Limite por segundo ou soluço do servidor: espera e repete.
                    espera = 2 ** tentativa
                    print(f"  [{i}/{len(faltam)}] {motivo} — esperando {espera}s")
                    time.sleep(espera)
                    continue
                falhas.append((vid, motivo or str(e)))
                print(f"  [{i}/{len(faltam)}] FALHOU  {vid}  ({motivo or 'erro'})")
                break
        if acabou_quota:
            print(f"\nCota diária esgotada depois de {subidos} vídeo(s) nesta execução.")
            print(f"Faltam {len(faltam) - subidos}. Rode o mesmo comando amanhã — "
                  "ele retoma exatamente daqui, sem duplicar nada.")
            break
        time.sleep(0.2)

    print(f"\nSubidos nesta execução: {subidos}")
    if falhas:
        print(f"Falharam {len(falhas)} (vídeo privado, removido ou restrito):")
        for vid, motivo in falhas:
            print(f"  {vid}  — {motivo}")
    print(f"Playlist: https://www.youtube.com/playlist?list={playlist_id}")


if __name__ == "__main__":
    main()
