"""
Grava um lote classificado na planilha, reordenando o catálogo inteiro.

Existe porque o `protocolo.md` registra o MESMO bug três vezes — lotes 81, 85
e 171 — sempre por um script de gravação escrito na hora que ordenava as
linhas novas por uma chave incompleta (só `ano_inicio`/`ano_fim`, sem
`Mês`/`Dias`) ou simplesmente apensava no fim sem ordenar nada. A lição
registrada lá ("vale considerar extrair um módulo compartilhado se aparecer
uma terceira vez") é isto.

Reaproveita `periodo()`, `parse_ano()` e `num()` do `verificar.py`, em vez de
reescrever a escada da Lista A — reimplementar essa lógica a cada lote é como
o erro volta.

Uso:
    python gravar.py classificacao.json lote-NN.md

O JSON é uma lista de objetos, um por vídeo do lote:

    [{"video_id": "abc12345678",
      "Ano": "1942 - 1945",          # '*' para Extra/Aleatório
      "Mes": "8 - 9",                # '*' quando não se aplica
      "Dias": "*",
      "Regiao": "Pacífico",
      "Tema": "Segunda Guerra Mundial",
      "Subtema": "Guerra do Pacífico",   # opcional
      "confianca": "alta",
      "status": "ok",
      "notas": "...",
      "periodo": "Extra"}]           # opcional: só 'Extra' ou 'Aleatório'

O que o script decide sozinho, e portanto NÃO se escreve no JSON:
`Século/Período` (escada da Lista A pelo ponto médio, ou o valor de `periodo`
quando a linha fica fora da linha do tempo), `ano_inicio`/`ano_fim` (parser de
`Ano`), `Link` (do video_id), `travado` ('sim' só para Extra/Aleatório — toda
outra linha nasce destravada e só o /aprovar trava), e `Canal`/`Título`/
`publicado`/`lote`, que vêm do próprio `lote-NN.md`.

Confere antes de escrever: o conjunto de ids do JSON tem que ser exatamente o
do arquivo de lote (a armadilha do desalinhamento de tupla, que já custou 14
linhas sem `publicado`/`Título`), nenhum id já presente na planilha, campos
obrigatórios preenchidos, e a forma da linha fora da linha do tempo.
"""

import json
import os
import re
import sys

import openpyxl

from verificar import (ABA, COLUNAS, CONFIANCAS, PLANILHA, SEM_PERIODO, STATUS,
                       num, parse_ano, periodo)

PREFIXO_LINK = "https://www.youtube.com/watch?v="

for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")


def erro(msg):
    print(f"\nERRO: {msg}\n")
    sys.exit(1)


def ler_lote(caminho):
    """Tira do lote-NN.md o número do lote, o nome do canal e, por vídeo,
    id, título e data de publicação."""
    texto = open(caminho, encoding="utf-8").read()

    m = re.search(r"^#\s*Lote\s*\d+\s*[—-]\s*(.+?)\s*$", texto, re.M)
    if not m:
        erro(f"{caminho}: não achei o cabeçalho '# Lote NN — Nome do canal'.")
    canal = m.group(1).strip()
    canal = re.sub(r"\s*\(vídeo avulso\)\s*$", "", canal)

    m = re.search(r"^lote:\s*(\d+)\s*$", texto, re.M)
    if not m:
        erro(f"{caminho}: não achei a linha 'lote: NN'.")
    lote = int(m.group(1))

    videos = {}
    for bloco in re.finditer(
            r"^###\s+(\S{11})\s*·\s*(.+?)\s*$\n^publicado:\s*(\d{4}-\d{2}-\d{2})",
            texto, re.M):
        videos[bloco.group(1)] = {"Título": bloco.group(2).strip(),
                                  "publicado": bloco.group(3)}
    if not videos:
        erro(f"{caminho}: não achei nenhum bloco '### <id> · <título>'.")
    return canal, lote, videos


def montar(entrada, canal, lote, videos):
    """Transforma uma entrada do JSON na linha completa da planilha."""
    vid = entrada.get("video_id")
    if vid not in videos:
        erro(f"{vid!r} não está no arquivo de lote.")

    rotulo_manual = entrada.get("periodo")
    ano = str(entrada.get("Ano", "*")).strip()

    if rotulo_manual:
        if rotulo_manual not in SEM_PERIODO:
            erro(f"{vid}: 'periodo' só aceita {sorted(SEM_PERIODO)}, veio "
                 f"{rotulo_manual!r}. O resto da Lista A sai da escada, nunca à mão.")
        if ano != "*":
            erro(f"{vid}: {rotulo_manual} tem que ter Ano='*', veio {ano!r}.")
        ai = af = None
        rotulo = rotulo_manual
    else:
        lido = parse_ano(ano)
        if lido is None:
            erro(f"{vid}: campo Ano ilegível para o parser — {ano!r}.")
        ai, af = lido
        if ai is None:
            erro(f"{vid}: Ano='*' sem 'periodo' — uma linha sem anos precisa "
                 f"dizer se é 'Extra' ou 'Aleatório'.")
        if ai > af:
            erro(f"{vid}: Ano={ano!r} dá {ai}..{af} — início depois do fim.")
        rotulo = periodo(ai, af)

    fora = rotulo in SEM_PERIODO
    conf = entrada.get("confianca")
    status = entrada.get("status")
    if fora:
        conf, status = "n/a", "ok"
    if conf not in CONFIANCAS:
        erro(f"{vid}: confianca inválida ({conf!r}).")
    if status not in STATUS:
        erro(f"{vid}: status inválido ({status!r}).")
    if conf in ("média", "chute") and status != "revisar":
        erro(f"{vid}: confianca {conf} exige status 'revisar' numa linha nova.")
    if conf == "n/a" and not fora:
        erro(f"{vid}: confianca 'n/a' só em linha Extra/Aleatório.")

    for campo, valor in (("Regiao", entrada.get("Regiao")),
                         ("Tema", entrada.get("Tema"))):
        if not valor:
            erro(f"{vid}: '{campo}' vazio.")

    return {
        "Século/Período": rotulo,
        "Ano": ano,
        "Mês": str(entrada.get("Mes", "*") or "*"),
        "Dias": str(entrada.get("Dias", "*") or "*"),
        "Região": entrada["Regiao"],
        "Tema": entrada["Tema"],
        "Subtema": entrada.get("Subtema") or None,
        "Canal": canal,
        "Título": videos[vid]["Título"],
        "Link": PREFIXO_LINK + vid,
        "publicado": videos[vid]["publicado"],
        "ano_inicio": ai,
        "ano_fim": af,
        "video_id": vid,
        "confianca": conf,
        "status": status,
        # travado='sim' marca trabalho humano. Extra/Aleatório nasce travado
        # por design; toda outra linha só é travada pelo /aprovar.
        "travado": "sim" if fora else None,
        "notas": entrada.get("notas") or None,
        "lote": lote,
    }


INF = float("inf")


def chave(r):
    """A chave COMPLETA de ordenação do verificar.py. Nunca só os dois anos."""
    return (r["ano_inicio"] if r["ano_inicio"] is not None else INF,
            r["ano_fim"] if r["ano_fim"] is not None else INF,
            num(r["Mês"]), num(r["Dias"]))


def main():
    if len(sys.argv) != 3:
        erro("uso: python gravar.py classificacao.json lote-NN.md")
    caminho_json, caminho_lote = sys.argv[1], sys.argv[2]
    for p in (caminho_json, caminho_lote, PLANILHA):
        if not os.path.exists(p):
            erro(f"não achei {p}.")

    canal, lote, videos = ler_lote(caminho_lote)
    entradas = json.load(open(caminho_json, encoding="utf-8"))
    if not isinstance(entradas, list):
        erro("o JSON tem que ser uma lista de objetos, um por vídeo.")

    ids_json = [e.get("video_id") for e in entradas]
    if len(ids_json) != len(set(ids_json)):
        erro("video_id repetido dentro do próprio JSON.")
    if set(ids_json) != set(videos):
        faltam = sorted(set(videos) - set(ids_json))
        sobram = sorted(set(ids_json) - set(videos))
        erro(f"o JSON não bate com {caminho_lote} — "
             f"faltam {faltam or 'nenhum'}, sobram {sobram or 'nenhum'}.")

    wb = openpyxl.load_workbook(PLANILHA)
    if ABA not in wb.sheetnames:
        erro(f"{PLANILHA} não tem a aba {ABA!r}.")
    ws = wb[ABA]

    cab = [c.value for c in ws[1]]
    if cab != COLUNAS:
        erro(f"cabeçalho inesperado.\n  esperado: {COLUNAS}\n  achado:   {cab}")

    antigas = []
    for linha in ws.iter_rows(min_row=2, values_only=True):
        r = dict(zip(COLUNAS, linha))
        if r["video_id"]:
            antigas.append(r)

    ja = {r["video_id"] for r in antigas}
    repetidos = sorted(ja & set(ids_json))
    if repetidos:
        erro(f"ids já presentes na planilha: {repetidos}")

    novas = [montar(e, canal, lote, videos) for e in entradas]
    todas = sorted(antigas + novas, key=chave)   # sort estável: empate mantém a ordem

    if len(todas) != len(antigas) + len(novas):
        erro("contagem de linhas não fecha depois da ordenação.")

    # Reescreve valor por valor com cell.value — `ws.cell(r, c, value=v)` não
    # limpa a célula quando o valor é None e já corrompeu linhas neste projeto.
    for i, r in enumerate(todas, start=2):
        for j, col in enumerate(COLUNAS, start=1):
            ws.cell(row=i, column=j).value = r[col]

    wb.save(PLANILHA)

    print(f"\n{canal} · lote {lote}")
    print(f"  {len(antigas)} linhas antes · {len(novas)} novas · {len(todas)} agora")
    conf = {}
    st = {}
    for r in novas:
        conf[r["confianca"]] = conf.get(r["confianca"], 0) + 1
        st[r["status"]] = st.get(r["status"], 0) + 1
    print(f"  confiança {conf} · status {st}")
    print(f"\nAgora rode: python verificar.py --anterior backups\\<o backup deste lote>\n")


if __name__ == "__main__":
    main()
