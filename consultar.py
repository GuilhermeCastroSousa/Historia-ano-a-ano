"""
Procura um termo na planilha, em Tema, Subtema e Título.

Existe por causa de uma armadilha com histórico no projeto: tema-raiz novo
proposto sem procurar sinônimo ou tradução alternativa na Lista C inteira.
Já aconteceu dos dois jeitos — `Gladiadores Romanos` contra `Gladiadores`,
`Besteiros Genoveses` contra `Balestreiros Genoveses`, `Revolução Russa`
contra `Revolução Russa de 1905`, `Fenícia Antiga` contra `Civilização
Fenícia`. Em todos, a sessão conferiu "de memória" e não achou.

**Antes de propor qualquer termo novo, rode isto.** Procura na planilha, que
é a fonte de verdade — e não na Lista C do `vocabulario-canonico.md`, que só é
regenerada nas aprovações e por isso não conhece os termos do ciclo em
andamento.

Como usar:
    python consultar.py gladiador
    python consultar.py "besteir|balestreir" "genoves"
    python consultar.py "guerra civil"

O argumento é expressão regular, sem diferenciar maiúsculas. Passe variações
de tradução e sinônimos na mesma chamada, separados por `|`.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import openpyxl

from verificar import ABA, PLANILHA

for _fluxo in (sys.stdout,):
    if hasattr(_fluxo, "reconfigure"):
        _fluxo.reconfigure(encoding="utf-8", errors="replace")

LIMITE_TITULOS = 14


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if not os.path.exists(PLANILHA):
        print(f"ERRO: não achei {PLANILHA}.")
        sys.exit(1)

    ws = openpyxl.load_workbook(PLANILHA, read_only=True)[ABA]
    linhas = ws.iter_rows(values_only=True)
    cab = list(next(linhas))
    rows = [dict(zip(cab, r)) for r in linhas if r[cab.index("video_id")]]

    for termo in sys.argv[1:]:
        try:
            rx = re.compile(termo, re.I)
        except re.error as e:
            print(f"\n===== {termo!r} ===== expressão inválida: {e}")
            continue
        print(f"\n===== {termo!r} =====")

        temas = sorted({r["Tema"] for r in rows
                        if r["Tema"] and rx.search(str(r["Tema"]))})
        if temas:
            print("  TEMA:")
            for t in temas:
                ex = [r for r in rows if r["Tema"] == t]
                regioes = sorted({r["Região"] for r in ex})
                print(f"    {t}  ({len(ex)} linhas · {', '.join(regioes[:4])})")
                print(f"      ex.: {ex[0]['Ano']} · {str(ex[0]['Título'])[:58]}")

        subs = sorted({(r["Tema"], r["Subtema"]) for r in rows
                       if r["Subtema"] and rx.search(str(r["Subtema"]))})
        if subs:
            print("  SUBTEMA:")
            for t, s in subs:
                n = sum(1 for r in rows
                        if r["Tema"] == t and r["Subtema"] == s)
                print(f"    {t} > {s}  ({n})")

        tit = [r for r in rows if r["Título"] and rx.search(str(r["Título"]))]
        if tit:
            print(f"  TÍTULO ({len(tit)}):")
            for r in tit[:LIMITE_TITULOS]:
                print(f"    {str(r['Ano']):<22} {r['Região']:<16} "
                      f"{r['Tema']} > {r['Subtema'] or '-'}")
                print(f"      {str(r['Título'])[:60]} "
                      f"[{str(r['Canal'])[:20]}]")
            if len(tit) > LIMITE_TITULOS:
                print(f"    ... e mais {len(tit) - LIMITE_TITULOS}")

        if not (temas or subs or tit):
            print("  (nada na planilha)")


if __name__ == "__main__":
    main()
