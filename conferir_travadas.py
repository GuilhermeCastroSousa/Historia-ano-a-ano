# -*- coding: utf-8 -*-
"""Confere que uma edição autorizada ficou dentro da autorização.

O `verificar.py` compara valores, não motivos: ele acusa "linhas TRAVADAS
alteradas" tanto numa correção que o humano aprovou por escrito quanto numa
sobrescrita acidental. O `protocolo.md` ("Corrigir uma linha travada com
aprovação humana explícita...") resolve isso com uma checagem manual — "a única
linha travada com qualquer diferença é exatamente a autorizada, e só nas células
que deveriam mudar". Este script é essa checagem, feita por máquina, porque a
partir de algumas dezenas de linhas ela não dá mais para fazer no olho.

    python conferir_travadas.py <backup-de-antes> <arquivo-de-ids> [colunas]

  <backup-de-antes>  a cópia da planilha feita ANTES da edição
  <arquivo-de-ids>   um video_id por linha (ou separados por espaço): o
                     conjunto autorizado, exatamente o que podia mudar
  [colunas]          as colunas que podiam mudar, separadas por vírgula.
                     Padrão: Tema,Subtema,notas

Sai 0 só se as três coisas valerem ao mesmo tempo:
  - nenhuma linha FORA do conjunto autorizado mudou;
  - nenhuma linha DO conjunto deixou de mudar (se não mudou, ou a autorização
    estava errada, ou a edição não rodou inteira);
  - nenhuma mudança caiu em coluna fora das permitidas.

Sair 0 aqui é o que transforma a falha do `verificar.py --anterior` em
falso-positivo esperado. Não substitui a autorização: confere que a edição
ficou dentro dela.
"""
import os
import sys

import openpyxl

from verificar import ABA, COLUNAS, PLANILHA

PADRAO = "Tema,Subtema,notas"


def ler(caminho):
    ws = openpyxl.load_workbook(caminho, read_only=True)[ABA]
    it = ws.iter_rows(values_only=True)
    cab = list(next(it))
    if cab != COLUNAS:
        raise SystemExit(f"cabeçalho inesperado em {caminho}")
    return {d["video_id"]: d for d in (dict(zip(cab, r)) for r in it)
            if d["video_id"]}


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip())
        return 2
    antes_arq, ids_arq = argv[1], argv[2]
    permitidas = set((argv[3] if len(argv) > 3 else PADRAO).split(","))
    desconhecidas = permitidas - set(COLUNAS)
    if desconhecidas:
        print(f"coluna que não existe na planilha: {sorted(desconhecidas)}")
        return 2
    with open(ids_arq, encoding="utf-8") as f:
        autorizados = set(f.read().split())
    if not autorizados:
        print(f"{ids_arq} está vazio — sem conjunto autorizado não há o que "
              f"conferir")
        return 2

    antes, agora = ler(antes_arq), ler(PLANILHA)
    print(f"antes: {os.path.basename(antes_arq)} ({len(antes)} ids) · "
          f"agora: {PLANILHA} ({len(agora)} ids)")
    print(f"autorizados: {len(autorizados)} ids · "
          f"colunas que podiam mudar: {', '.join(sorted(permitidas))}")

    sumidos = sorted(set(antes) - set(agora))
    novos = sorted(set(agora) - set(antes))
    difere, fora, coluna_errada = set(), [], []
    for vid, linha_antes in antes.items():
        linha_agora = agora.get(vid)
        if linha_agora is None:
            continue
        mudou = {c for c in COLUNAS if linha_antes[c] != linha_agora[c]}
        if not mudou:
            continue
        difere.add(vid)
        if vid not in autorizados:
            fora.append((vid, sorted(mudou)))
        if mudou - permitidas:
            coluna_errada.append((vid, sorted(mudou - permitidas)))
    nao_mudaram = sorted(autorizados - difere - set(novos))

    print(f"\nlinhas com qualquer diferença: {len(difere)} "
          f"(dentro do autorizado: {len(difere & autorizados)})")
    falhas = []
    if sumidos:
        falhas.append(f"ids que sumiram da planilha: {len(sumidos)} — "
                      f"{', '.join(sumidos[:10])}"
                      f"{' ...' if len(sumidos) > 10 else ''}")
    if novos:
        falhas.append(f"ids novos na planilha: {len(novos)} — "
                      f"{', '.join(novos[:10])}"
                      f"{' ...' if len(novos) > 10 else ''}")
    if fora:
        falhas.append("linhas que mudaram FORA do autorizado: "
                      f"{len(fora)} — " + "; ".join(
                          f"{v} ({', '.join(c)})" for v, c in fora[:10])
                      + (" ..." if len(fora) > 10 else ""))
    if coluna_errada:
        falhas.append("mudança em coluna que não podia mudar: "
                      f"{len(coluna_errada)} — " + "; ".join(
                          f"{v} ({', '.join(c)})" for v, c in coluna_errada[:10])
                      + (" ..." if len(coluna_errada) > 10 else ""))
    if nao_mudaram:
        falhas.append(f"autorizadas que NÃO mudaram: {len(nao_mudaram)} — "
                      f"{', '.join(nao_mudaram[:10])}"
                      f"{' ...' if len(nao_mudaram) > 10 else ''}")

    if falhas:
        print(f"\n{len(falhas)} FALHA(S) — a edição saiu da autorização:\n")
        for f in falhas:
            print(f"  - {f}")
        print("\nRestaure o backup antes de qualquer outra coisa.")
        return 1

    print(f"\n  passou: só o autorizado mudou, e só em "
          f"{', '.join(sorted(permitidas))}.")
    print("  A falha de 'linhas TRAVADAS alteradas' do verificar.py --anterior "
          "é,\n  neste caso, o falso-positivo esperado que o protocolo.md "
          "descreve.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
