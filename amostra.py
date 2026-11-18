"""
Sorteia as cinco linhas da parada de revisão, de uma janela de lotes.

Existe porque a amostra da parada é o único ponto em que alguém de fora olha o
que foi produzido — e quem apresenta não pode escolher quais linhas mostrar. A
semente é derivada dos números de lote, então o sorteio é reproduzível: rodar
de novo na mesma janela dá as mesmas cinco linhas, e dá para conferir depois
que não houve escolha.

Imprime também o bloco de estado da janela (contagem por lote, confiança,
status e temas usados), que é o item 4 da parada.

Como usar:
    python amostra.py 232 233 234 235
    python amostra.py 248 249            # ciclo curto, por esgotamento
"""

import collections
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import openpyxl

from verificar import ABA, PLANILHA

for _fluxo in (sys.stdout,):
    if hasattr(_fluxo, "reconfigure"):
        _fluxo.reconfigure(encoding="utf-8", errors="replace")

QUANTAS = 5


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    try:
        lotes = [int(a) for a in sys.argv[1:]]
    except ValueError:
        print("ERRO: os argumentos são números de lote.\n")
        sys.exit(1)

    if not os.path.exists(PLANILHA):
        print(f"ERRO: não achei {PLANILHA}.")
        sys.exit(1)

    ws = openpyxl.load_workbook(PLANILHA, read_only=True)[ABA]
    linhas = ws.iter_rows(values_only=True)
    cab = list(next(linhas))
    rows = [dict(zip(cab, r)) for r in linhas if r[cab.index("video_id")]]
    janela = [r for r in rows if r["lote"] in lotes]

    if not janela:
        print(f"ERRO: nenhuma linha nos lotes {lotes}.")
        sys.exit(1)
    print(f"lotes {lotes} -> {len(janela)} linhas na janela")

    # Semente fixa derivada dos lotes: o sorteio não é escolha de quem apresenta.
    random.seed("-".join(map(str, sorted(lotes))))
    quantas = min(QUANTAS, len(janela))
    for i, r in enumerate(random.sample(janela, quantas), 1):
        print()
        print(f"[{i}] {r['Título']}")
        print(f"    id {r['video_id']} · lote {r['lote']} · "
              f"publicado {r['publicado']}")
        print(f"    CLASSIFIQUEI: {r['Século/Período']} | Ano={r['Ano']} | "
              f"Mês={r['Mês']} | Dias={r['Dias']} | {r['Região']} > "
              f"{r['Tema']} > {r['Subtema'] or '(sem subtema)'} | "
              f"{r['confianca']}/{r['status']}")
        print(f"    NOTA: {r['notas']}")

    print("\n=== ESTADO DA JANELA ===")
    for campo in ("lote", "confianca", "status"):
        cont = collections.Counter(r[campo] for r in janela)
        print(f"  {campo}: "
              f"{dict(sorted(cont.items(), key=lambda kv: str(kv[0])))}")
    temas = sorted({r["Tema"] for r in janela})
    print(f"  temas usados ({len(temas)}): {', '.join(temas)}")
    travadas = sum(1 for r in janela if r["travado"] == "sim")
    print(f"  travadas: {travadas} de {len(janela)} "
          f"(antes do /aprovar, só Extra e Aleatório)")
    print("\nA evidência de cada linha está no lote-NN.md correspondente — a")
    print("parada tem que apresentar a nota JUNTO com os capítulos e as datas")
    print("citadas do arquivo de lote, não só a nota.")


if __name__ == "__main__":
    main()
