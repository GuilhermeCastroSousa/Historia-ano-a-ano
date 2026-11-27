# -*- coding: utf-8 -*-
"""Confere se cada entrada de REGIAO_POR_TEMA ainda se paga.

    python conferir_regiao.py

Uma entrada só se paga quando diz algo que a coluna Região NÃO sabe dizer.
`Dácios -> Dácia` se paga: a Região é 'Leste Europeu' e só o tema sabe que
aquilo é Dácia. Já um tema cujo conteúdo VIAJA faz a entrada virar um padrão, e
o padrão atropela a Região que foi escolhida episódio por episódio — foi o que
pôs a campanha de Alexandre inteira na Grécia e Dürer na Itália.

Reparte as entradas em três:

  PORTADORAS   a ponte da Região não acerta nenhuma linha do tema. A entrada é
               a única fonte da região histórica. Tem que ficar.
  REDUNDANTES  a ponte acerta 100%. A entrada não muda nada hoje; fica como
               seguro para lote novo que venha com Região grossa.
  CANDIDATAS   a ponte acerta parte. A entrada é um padrão e está sobrescrevendo
               a minoria. Cada uma dessas pede uma decisão.

Sobre uma CANDIDATA, duas coisas são verdade de graça e não precisam de medição:
tirar a entrada não pode mexer nas linhas que concordavam com ela (por
construção elas chegam à mesma região pela ponte), e depois de 500 a.C. a
`chave()` do `ordenar.py` não usa a região, então tirar não reordena nada ali —
só muda o rótulo. O que precisa de medição é se a ORDEM dele quer o tema junto:
rode `python ordenar.py --conferir <planilha ordenada à mão>` com e sem a
entrada e compare região e concordância de pares. Foi assim que `Pré-Socráticos`
ficou: a Região está certa linha por linha (jônios na Anatólia, itálicos na
Magna Grécia) e mesmo assim a ordem dele os quer num bloco só.

O script não escreve em nada. Exit 0 sempre: é relatório, não portão.
"""
import collections
import sys

import ordenar


def ponte(r):
    return ordenar.PONTE_REGIAO.get(r["Região"], r["Região"] or "Global")


def main():
    rows = ordenar.carregar()
    por_tema = collections.defaultdict(list)
    for r in rows:
        por_tema[r["Tema"]].append(r)

    portadoras, redundantes, candidatas, orfas = [], [], [], []
    for tema, imposta in ordenar.REGIAO_POR_TEMA.items():
        linhas = por_tema.get(tema)
        if not linhas:
            orfas.append((tema, imposta))
            continue
        c = collections.Counter(ponte(r) for r in linhas)
        acerto = c.get(imposta, 0)
        resto = {k: v for k, v in c.items() if k != imposta}
        alvo = (portadoras if acerto == 0
                else redundantes if acerto == len(linhas)
                else candidatas)
        alvo.append((len(linhas) - acerto, len(linhas), tema, imposta, resto))

    print(f"{len(ordenar.REGIAO_POR_TEMA)} entradas em REGIAO_POR_TEMA, "
          f"{len(rows)} linhas na planilha\n")

    print(f"PORTADORAS   {len(portadoras):3} entradas, "
          f"{sum(n for _p, n, *_ in portadoras):5} linhas  (a ponte não acerta nenhuma)")
    print(f"REDUNDANTES  {len(redundantes):3} entradas, "
          f"{sum(n for _p, n, *_ in redundantes):5} linhas  (a ponte acerta todas)")
    print(f"CANDIDATAS   {len(candidatas):3} entradas, "
          f"{sum(p for p, *_ in candidatas):5} linhas sobrescritas")
    if orfas:
        print(f"SEM LINHA    {len(orfas):3} entradas que nenhum tema usa hoje")

    if candidatas:
        print("\nCANDIDATAS, da que mais sobrescreve para a que menos:")
        print("  (não é erro por si — é onde a tabela está sendo padrão)")
        for perdidas, n, tema, imposta, resto in sorted(candidatas, reverse=True):
            cauda = ", ".join(f"{k}:{v}" for k, v in
                              sorted(resto.items(), key=lambda kv: -kv[1]))
            print(f"  {perdidas:4}/{n:<5} {tema[:34]:35} tabela={imposta[:16]:17} "
                  f"Região diz {cauda}")

    if orfas:
        print("\nSEM LINHA (herdadas de temas fundidos; ficam como seguro):")
        for tema, imposta in sorted(orfas)[:20]:
            print(f"    {tema[:40]:41} -> {imposta}")
        if len(orfas) > 20:
            print(f"    ... e {len(orfas) - 20} outras")
    return 0


if __name__ == "__main__":
    sys.exit(main())
