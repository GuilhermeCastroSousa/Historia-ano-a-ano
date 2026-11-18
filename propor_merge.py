# -*- coding: utf-8 -*-
"""Proposta de fusao de temas, versao final. NAO escreve na planilha.

Camadas por FORCA DA EVIDENCIA, nao por gosto:
  A1  fusao que o humano fez em 2+ linhas, com 60%+ de maioria
  A2  fusao com maioria simples (50-60%) -- conferir
  A3  fusao vista em uma linha so -- evidencia fraca, provavelmente certa
  R   renomeacao: o destino nem existe como tema no catalogo
  B   padrao de aspecto ('Sociedade X' -> X), verificavel pelo nome
  C   lista de trabalho: onde eu nao arrisco palpite
"""
import collections
import os
import re
import sys

os.chdir(r"C:\Users\guilh\Historia-ano-a-ano")
sys.path.insert(0, os.getcwd())

import openpyxl
import ordenar as O

for f in (sys.stdout,):
    if hasattr(f, "reconfigure"):
        f.reconfigure(encoding="utf-8", errors="replace")

REF = r"C:\Users\guilh\Downloads\História do Mundo (1).xlsx"
SAIDA = "merge-temas-proposta.md"

rows = O.ordenar(O.carregar())
porid = {r["video_id"]: r for r in rows}
por_tema = collections.Counter(r["Tema"] for r in rows)
regiao_do_tema = {}
for t in por_tema:
    c = collections.Counter(r["regiao_historica"] for r in rows if r["Tema"] == t)
    regiao_do_tema[t] = c.most_common(1)[0][0]

wb = openpyxl.load_workbook(REF, read_only=True)
ws = wb[wb.sheetnames[0]]
it = ws.iter_rows(values_only=True)
cab = list(next(it))
ref = []
for r in it:
    d = dict(zip(cab, r))
    m = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", str(d.get("Link") or ""))
    if m and m.group(1) in porid:
        d["video_id"] = m.group(1)
        ref.append(d)

destinos = collections.defaultdict(collections.Counter)
for d in ref:
    dele = (d.get("Tema") or "").strip()
    if dele:
        destinos[porid[d["video_id"]]["Tema"]][dele] += 1

A1, A2, A3, R = {}, {}, {}, {}
sem_maioria = []
# Primeiro: quantas origens apontam para cada destino. É isso que separa
# fusão de renomeação -- e NÃO o destino ser um nome novo, que era o erro da
# versão anterior: 'Mesopotâmia Antiga' é nome novo e recebe sete origens.
preferido = {}
for origem, cont in destinos.items():
    destino, n = cont.most_common(1)[0]
    if destino != origem:
        preferido[origem] = (destino, n, sum(cont.values()))
quantas_origens = collections.Counter(d for d, _, _ in preferido.values())

for origem, (destino, n, total) in preferido.items():
    frac = n / total
    if quantas_origens[destino] == 1 and destino not in por_tema:
        R[origem] = (destino, n, total)       # um origem, nome novo: renomeação
    elif total >= 2 and frac >= 0.6:
        A1[origem] = (destino, n, total)
    elif total >= 2 and frac >= 0.5:
        A2[origem] = (destino, n, total)
    elif total == 1:
        A3[origem] = (destino, n, total)
    else:
        sem_maioria.append((origem, destino, n, total))

ASPECTOS = ("sociedade", "comércio", "exército", "religião", "cultura material",
            "marinha", "literatura")
B = {}
for t in por_tema:
    if t in A1 or t in A2 or t in A3 or t in R:
        continue
    tl = t.lower()
    prefixo = next((p for p in ASPECTOS if tl.startswith(p)), None)
    if not prefixo:
        continue
    resto = re.sub(r"^" + prefixo + r"\s*(de|da|do|na|no)?\s*", "", tl)
    chaves = {w for w in re.findall(r"\w{5,}", resto)
              if w not in ("antiga", "antigo", "antigos")}
    for nucleo in sorted(por_tema, key=lambda x: -por_tema[x]):
        if (nucleo == t or por_tema[nucleo] < por_tema[t] * 2
                or regiao_do_tema[nucleo] != regiao_do_tema[t]):
            continue
        if chaves & {w for w in re.findall(r"\w{5,}", nucleo.lower())
                     if w not in ("antiga", "antigo", "antigos")}:
            B[t] = nucleo
            break

mapa = {}
for camada in (A1, A2, A3, R):
    for o, (d, _, _) in camada.items():
        mapa.setdefault(o, d)
for o, d in B.items():
    mapa.setdefault(o, d)


def fragmentos(m):
    return sum(1 for a, b in zip(rows, rows[1:])
               if (a["regiao_historica"], m.get(a["Tema"], a["Tema"]))
               != (b["regiao_historica"], m.get(b["Tema"], b["Tema"]))) + 1


def acerto(m):
    return sum(1 for d in ref
               if (d.get("Tema") or "").strip()
               == m.get(porid[d["video_id"]]["Tema"], porid[d["video_id"]]["Tema"]))


frag_antes, frag_depois = fragmentos({}), fragmentos(mapa)
temas_depois = len({mapa.get(t, t) for t in por_tema})
linhas = sum(por_tema[t] for t in mapa)
so_A1 = {o: d for o, (d, _, _) in A1.items()}

L = ["# Proposta de fusão de temas — para você aprovar linha por linha\n",
     "Saiu do cruzamento da sua planilha ordenada à mão com a v2. **Nada foi",
     "aplicado em planilha nenhuma.** Marque `x` na coluna `ok?` do que",
     "aprovar e me devolva o arquivo; o que ficar em branco não entra.\n",
     "Fusão aplicada **não perde informação**: o tema antigo vira o `Subtema`",
     "da linha. É o que você fez nos 290 — Tema é a civilização, Subtema é o",
     "detalhe.\n",
     "As camadas estão separadas por **força da evidência**, não por gosto meu.",
     "Aprove por camada se quiser ir rápido: A1 e R são as seguras.\n",
     "| se tudo for aprovado | |", "|---|---|",
     f"| temas-raiz | {len(por_tema)} → {temas_depois} |",
     f"| trechos contíguos na v3 | {frag_antes} → {frag_depois} |",
     f"| linhas afetadas | {linhas} |",
     f"| tema igual ao seu, nos 290 | {acerto({})}/{len(ref)} "
     f"({acerto({})/len(ref):.0%}) → {acerto(mapa)}/{len(ref)} "
     f"({acerto(mapa)/len(ref):.0%}) |",
     f"| idem, só com A1 aprovada | → {acerto(so_A1)}/{len(ref)} "
     f"({acerto(so_A1)/len(ref):.0%}) |"]


def tabela(titulo, nota, dados, com_contagem=True):
    L.append(f"\n## {titulo}\n")
    L.extend(nota)
    L.append("")
    L.append("| ok? | tema atual | passa a ser | linhas | você fez em |"
             if com_contagem else "| ok? | tema atual | passa a ser | linhas |")
    L.append("|---|---|---|---|---|" if com_contagem else "|---|---|---|---|")
    for o in sorted(dados, key=lambda x: -por_tema[x]):
        v = dados[o]
        if com_contagem:
            d, n, tot = v
            L.append(f"|  | `{o}` | `{d}` | {por_tema[o]} | {n}/{tot} |")
        else:
            L.append(f"|  | `{o}` | `{v}` | {por_tema[o]} |")


tabela("A1 — você fez, com maioria clara",
       ["Fusão aplicada por você em 2 ou mais linhas daquele tema, em 60% ou",
        "mais das que revisou. É a camada com evidência direta e é a que eu",
        "aplicaria sem hesitar."], A1)
tabela("A2 — você fez, por maioria simples",
       ["Entre 50% e 60% das linhas revisadas. Vale conferir: pode ser que o",
        "tema seja transversal e a decisão dependa do vídeo."], A2)
tabela("A3 — você fez, mas em uma linha só",
       ["Evidência fraca por construção: havia um vídeo só daquele tema na sua",
        "fatia. A maioria me parece certa — `Império Acadiano` em `Mesopotâmia",
        "Antiga`, `Egina` e `Delfos` em `Grécia antiga` —, mas é palpite meu",
        "sobre um caso único, não padrão medido."], A3)
tabela("R — renomeação, não fusão",
       ["Aqui o destino **não existe** como tema no catálogo: você não juntou",
        "dois temas, deu outro nome ao mesmo assunto. Barato e seguro de",
        "aplicar, e um deles corrige grafia (`Nurágica`, não `Nuráguica` — a",
        "sua planilha tem o erro, a v2 está certa; confirme qual você quer)."], R)
tabela("B — padrão de aspecto",
       ["`Sociedade X`, `Exército X`, `Comércio X` absorvidos por `X`, na mesma",
        "região. Não é palpite sobre o assunto: o nome do tema já diz que ele é",
        "um aspecto de outro, e é o que você fez com `Sociedade Mesopotâmica` e",
        "`Sociedade Egípcia Antiga`. **Confira a direção**: pus `Exército",
        "Romano` em `Império Romano` e `Religião Romana` em `República",
        "Romana` porque é onde está a massa de linhas de cada um, mas os dois",
        "atravessam República e Império."], B, com_contagem=False)

L.append("\n## C — Onde eu não arrisco palpite\n")
L.append("Regiões com muitos temas de 1 ou 2 linhas. Fundir aqui é decisão")
L.append("editorial sua: não tenho como saber se `Samos` deve virar subtema de")
L.append("`Grécia antiga` ou seguir tema próprio. Listo para você decidir.\n")
for reg in sorted({r for r in regiao_do_tema.values()},
                  key=lambda r: -sum(por_tema[t] for t in por_tema
                                     if regiao_do_tema[t] == r)):
    pequenos = sorted(t for t in por_tema
                      if regiao_do_tema[t] == reg and por_tema[t] <= 2
                      and t not in mapa)
    if len(pequenos) < 5:
        continue
    nucleo = max((t for t in por_tema if regiao_do_tema[t] == reg),
                 key=lambda t: por_tema[t])
    L.append(f"**{reg}** — {len(pequenos)} temas de 1-2 linhas. "
             f"Núcleo possível: `{nucleo}` ({por_tema[nucleo]} linhas).  ")
    L.append("  " + ", ".join("`" + t + "`" for t in pequenos[:14])
             + (" ..." if len(pequenos) > 14 else "") + "\n")

L.append("\n## O que eu tentei e descartei\n")
L.append("**Casar temas por palavra em comum na mesma região.** Produziu lixo:")
L.append("`Primeira Guerra Mundial ← Guerra de Sucessão Espanhola`,")
L.append("`Dinastia Zhou ← Dinastia Han`, `Guerra Civil Americana ← Guerra")
L.append("Fria`. 'Guerra' e 'dinastia' não dizem nada sobre o assunto. Método")
L.append("abandonado — e é por isso que não existe uma camada cobrindo os 460")
L.append("temas que você não revisou: para eles não há evidência, só analogia.\n")
if sem_maioria:
    L.append("**Temas transversais sem destino único** — você dividiu caso a")
    L.append("caso, e quem decide é a região ou o subtema, não o tema:\n")
    for origem, destino, n, tot in sorted(sem_maioria, key=lambda x: -x[3]):
        L.append(f"- `{origem}`: {n} de {tot} revisadas iriam para `{destino}`, "
                 f"o resto para outros destinos")

open(SAIDA, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print(f"A1={len(A1)} A2={len(A2)} A3={len(A3)} R={len(R)} B={len(B)} "
      f"descartadas={len(sem_maioria)}")
print(f"temas {len(por_tema)} -> {temas_depois} · trechos {frag_antes} -> "
      f"{frag_depois} · linhas {linhas}")
print(f"tema igual ao dele: {acerto({})} -> {acerto(mapa)} de {len(ref)} "
      f"(só A1: {acerto(so_A1)})")
print(f"{SAIDA} escrito.")
