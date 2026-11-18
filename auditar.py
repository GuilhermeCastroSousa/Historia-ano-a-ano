"""
Auditoria de cobertura: varre o uploads INTEIRO de cada canal e diz quantos
vídeos o projeto nunca viu. Somente leitura — não grava nada, nem em
`catalogados.txt`, nem em `descartados.txt`, nem em `canais.json`.

POR QUE ESTE SCRIPT EXISTE
──────────────────────────
O `status: encerrado` autoriza o `coletar.py` a parar de paginar na primeira
página inteiramente conhecida. A prova de esgotamento que o projeto usava — "a
coleta seguinte veio com 0 vídeos novos" — rodava com essa mesma parada ligada,
e portanto se auto-confirmava. Rodando este script em 17/11/2026 apareceram
**1216 vídeos catalogáveis nunca coletados**: 1009 no Invicta, 204 no Kings and
Generals e 3 no Thersites, todos em canais marcados "esgotamento real".
Ver `protocolo.md`, "esgotamento que se auto-confirma".

Use antes de confiar que um canal acabou, e depois de uma rodada de revisita
para confirmar que não sobrou nada.

Como usar:
    python auditar.py                      # todos os canais de canais.json
    python auditar.py @Handle [@Outro]     # só esses
    python auditar.py --desde 2026-07-31   # corte de data explícito para todos

O corte de data separa duas coisas que é fácil confundir:
  - vídeo NOVO, publicado depois do corte — o que uma revisita deve pegar;
  - BURACO antigo, publicado antes, que nunca foi coletado.
Sem `--desde`, o corte de cada canal é a `ultima_coleta` dele em `canais.json`
— o que só é útil ANTES de uma revisita, porque a revisita atualiza essa data.

Custo de cota: 1 unidade por página de 50 itens, mais 1 por lote de 50 ids
detalhados. Varrer os vinte canais inteiros custou ~400 unidades das 10.000
diárias.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import coletar as c

for _fluxo in (sys.stdout, sys.stderr):
    if hasattr(_fluxo, "reconfigure"):
        _fluxo.reconfigure(encoding="utf-8", errors="replace")


def varrer(playlist, conhecidos):
    """Percorre a playlist INTEIRA, sem parada antecipada. Devolve
    (total_de_itens, lista_de_videos_desconhecidos_com_detalhes)."""
    pagina, total, ids = None, 0, []
    while True:
        r = c.api("playlistItems", part="contentDetails", playlistId=playlist,
                  maxResults=50, **({"pageToken": pagina} if pagina else {}))
        for it in r.get("items", []):
            total += 1
            vid = it["contentDetails"]["videoId"]
            if vid not in conhecidos:
                ids.append(vid)
        pagina = r.get("nextPageToken")
        if not pagina:
            break
    return total, (c.detalhes(ids) if ids else [])


def classificar(videos, corte):
    """Separa os desconhecidos pelos mesmos filtros do coletar.py e pelo corte
    de data. `corte` pode ser None."""
    caixas = {"novo": [], "antigo": [], "short": [], "live": [], "exclusivo": []}
    for v in videos:
        if c.RE_EXCLUSIVO.search(v["titulo"]) or c.RE_TEASER.search(v["titulo"]):
            caixas["exclusivo"].append(v)
        elif v.get("live"):
            caixas["live"].append(v)
        elif c.duracao_segundos(v["duracao"]) < c.DURACAO_MINIMA:
            caixas["short"].append(v)
        elif corte and v["publicado"] <= corte:
            caixas["antigo"].append(v)
        else:
            caixas["novo"].append(v)
    return caixas


def main():
    argv = sys.argv[1:]
    corte_global = None
    if "--desde" in argv:
        i = argv.index("--desde")
        if i + 1 >= len(argv):
            c.erro("--desde precisa de uma data AAAA-MM-DD logo depois.")
        corte_global = argv[i + 1]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", corte_global):
            c.erro(f"--desde espera AAAA-MM-DD, veio {corte_global!r}.")
        del argv[i:i + 2]

    c.CHAVE = c.ler_chave()
    canais = c.ler_canais().get("canais", {})
    if not canais:
        c.erro("canais.json vazio ou inexistente.")

    alvos = argv or list(canais)
    for chave in alvos:
        if chave not in canais:
            c.erro(f"'{chave}' não está em canais.json.")

    conhecidos = (c.ids_ja_registrados() | c.ler_lista(c.ARQUIVO_CATALOGADOS)
                  | c.ler_descartados())
    print(f"\nconhecidos: {len(conhecidos)} ids "
          f"(planilha ∪ catalogados.txt ∪ descartados.txt)\n")

    resumo = []
    for chave in alvos:
        reg = canais[chave]
        nome = reg.get("nome", chave)
        corte = corte_global or reg.get("ultima_coleta")
        if chave.startswith("playlist:"):
            playlist = chave.split("playlist:", 1)[1]
        else:
            playlist, _ = c.playlist_de_uploads(chave)

        total, desconhecidos = varrer(playlist, conhecidos)
        cx = classificar(desconhecidos, corte)
        resumo.append((nome, chave, total, cx))

        print(f"{nome[:44]:<46} uploads {total:>5} · desconhecidos "
              f"{len(desconhecidos):>4} · catalogáveis: {len(cx['novo']):>3} novos "
              f"+ {len(cx['antigo']):>4} ANTIGOS · descartáveis: "
              f"{len(cx['short'])} Short, {len(cx['live'])} live, "
              f"{len(cx['exclusivo'])} exclusivo · corte {corte}")
        for v in cx["novo"][:40]:
            print(f"      novo    {v['publicado']}  {v['id']}  {v['titulo'][:62]}")
        for v in sorted(cx["antigo"], key=lambda x: x["publicado"],
                        reverse=True)[:10]:
            print(f"      ANTIGO  {v['publicado']}  {v['id']}  {v['titulo'][:62]}")
        if len(cx["antigo"]) > 10:
            print(f"      ANTIGO  ... e mais {len(cx['antigo']) - 10}")

    print("\n=== RESUMO ===")
    novos = antigos = 0
    for nome, chave, total, cx in resumo:
        novos += len(cx["novo"])
        antigos += len(cx["antigo"])
        if cx["novo"] or cx["antigo"]:
            print(f"  {len(cx['novo']):>3} novos · {len(cx['antigo']):>4} antigos"
                  f" · {nome[:50]} ({chave})")
    print(f"\ncatalogáveis pendentes: {novos} novos · {antigos} antigos "
          f"(buraco de cobertura)")
    if antigos:
        print("\nATENÇÃO: vídeo ANTIGO desconhecido significa que o canal NÃO")
        print("foi esgotado, por mais que o status diga 'encerrado'. Ver")
        print("protocolo.md, 'esgotamento que se auto-confirma'.")


if __name__ == "__main__":
    main()
