"""
Mede a ordem gerada pelo `ordenar.py` contra uma planilha ordenada à mão.

Três números, porque nenhum deles sozinho diz o que importa:

1. ERA e REGIÃO certas — quantas linhas caíram na era e na região histórica
   que o humano usou. É o teste do vocabulário.
2. CONCORDÂNCIA DE PARES (tau de Kendall) — de todos os pares de vídeos, em
   quantos a minha ordem concorda com a dele sobre quem vem antes. É o teste da
   ordem, e é o que mais importa: 1,0 é ordem idêntica, 0 é moeda.
3. VIZINHANÇA PRESERVADA — dos pares que ele deixou lado a lado, quantos
   continuam lado a lado. É o teste da experiência de quem assiste: é aqui que
   se vê se um bloco de civilização foi partido no meio.

Uso: python ordenar.py --conferir "caminho/da/planilha.xlsx"
"""

import collections
import re
import sys

import openpyxl


def ler_referencia(caminho):
    wb = openpyxl.load_workbook(caminho, read_only=True)
    ws = wb[wb.sheetnames[0]]
    it = ws.iter_rows(values_only=True)
    cab = list(next(it))
    ref = []
    for r in it:
        d = dict(zip(cab, r))
        m = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", str(d.get("Link") or ""))
        if not m:
            continue
        for k in ("Período", "Região", "Tema", "Subtema"):
            if isinstance(d.get(k), str):
                d[k] = d[k].strip() or None
        d["video_id"] = m.group(1)
        ref.append(d)
    return ref


def tau(a, b):
    """Concordância de pares entre duas listas dos mesmos ids."""
    pos_b = {v: i for i, v in enumerate(b)}
    ordem = [pos_b[v] for v in a]
    n = len(ordem)
    concorda = discorda = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ordem[i] < ordem[j]:
                concorda += 1
            else:
                discorda += 1
    total = concorda + discorda
    return (concorda - discorda) / total if total else 0.0, concorda, total


def conferir(rows, caminho):
    ref = ler_referencia(caminho)
    meu = {r["video_id"]: r for r in rows}
    comuns = [r for r in ref if r["video_id"] in meu]
    print(f"\n{'='*66}\nCONFERINDO contra {caminho}")
    print(f"{len(ref)} linhas na referência · {len(comuns)} cruzaram com a v3")
    if not comuns:
        return

    # 1. era e região
    acerto_era = acerto_reg = 0
    erros_reg = collections.Counter()
    for r in comuns:
        m = meu[r["video_id"]]
        era_ref = str(r["Período"] or "").strip().lower()
        if era_ref and era_ref.split("(")[0].strip() in m["era"].lower():
            acerto_era += 1
        if (r["Região"] or "").strip() == m["regiao_historica"]:
            acerto_reg += 1
        else:
            erros_reg[(r["Região"], m["regiao_historica"])] += 1
    print(f"\n1. era igual à dele:    {acerto_era:>4}/{len(comuns)} "
          f"({acerto_era/len(comuns):.0%})")
    print(f"   região igual à dele: {acerto_reg:>4}/{len(comuns)} "
          f"({acerto_reg/len(comuns):.0%})")
    if erros_reg:
        print("   maiores divergências de região (dele -> minha):")
        for (a, b), n in erros_reg.most_common(8):
            print(f"     {n:>3}  {a} -> {b}")

    # 2. tau
    ordem_dele = [r["video_id"] for r in comuns]
    ordem_minha = sorted(ordem_dele, key=lambda v: meu[v]["ordem"])
    t, conc, total = tau(ordem_dele, ordem_minha)
    print(f"\n2. concordância de pares: {t:+.3f}  "
          f"({conc} de {total} pares na mesma ordem = {conc/total:.0%})")

    # 3. vizinhança
    pos = {v: i for i, v in enumerate(ordem_minha)}
    juntos = sum(1 for a, b in zip(ordem_dele, ordem_dele[1:])
                 if abs(pos[a] - pos[b]) == 1)
    print(f"3. vizinhança preservada: {juntos}/{len(ordem_dele)-1} "
          f"({juntos/(len(ordem_dele)-1):.0%}) dos pares que ele deixou "
          f"lado a lado")

    # blocos dele partidos pela minha ordem
    blocos = []
    for r in comuns:
        k = (r["Período"], r["Região"])
        if not blocos or blocos[-1][0] != k:
            blocos.append([k, []])
        blocos[-1][1].append(r["video_id"])
    partidos = 0
    for k, ids in blocos:
        if len(ids) < 2:
            continue
        p = sorted(pos[i] for i in ids)
        if p[-1] - p[0] != len(p) - 1:
            partidos += 1
    print(f"   blocos (era+região) dele que a minha ordem parte: "
          f"{partidos} de {sum(1 for _, i in blocos if len(i) > 1)}")

    # 4. O teste que separa estrutura de acabamento: a SEQUÊNCIA de blocos.
    # Se o passeio geográfico está na ordem dele, a experiência de quem assiste
    # está certa, e o que sobra é ajuste fino dentro do bloco — que é
    # exatamente o que ele disse que vai fazer à mão.
    seq_dele, vistos = [], set()
    for r in comuns:
        k = (str(r["Período"] or "").split("(")[0].strip(), r["Região"])
        if k not in vistos:
            vistos.add(k)
            seq_dele.append(k)
    primeira_minha = {}
    for v in ordem_minha:
        m = meu[v]
        r = next(x for x in comuns if x["video_id"] == v)
        k = (str(r["Período"] or "").split("(")[0].strip(), r["Região"])
        primeira_minha.setdefault(k, pos[v])
    seq_ordenada = sorted(seq_dele, key=lambda k: primeira_minha[k])
    t2, c2, tt2 = tau(seq_dele, seq_ordenada)
    print(f"\n4. sequência dos blocos: {t2:+.3f} "
          f"({c2} de {tt2} pares de blocos na mesma ordem = {c2/tt2:.0%})")
    print("   ordem dos blocos que a v3 produz, contra a dele:")
    for i, k in enumerate(seq_ordenada[:40], 1):
        marca = "  " if seq_dele.index(k) == i - 1 else "<-"
        print(f"     {i:>2} {marca} {k[1]}  [{k[0][:20]}]")
    print("="*66)
