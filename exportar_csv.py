"""
Gera um espelho .csv do catálogo, para o Git conseguir mostrar diferença.

O .xlsx é binário: o GitHub não exibe o conteúdo nem compara duas versões
dele. O .csv gerado aqui é o mesmo catálogo em texto, então cada lote novo
aparece como um diff legível — quais linhas entraram, quais mudaram.

O .csv é derivado, nunca a fonte. Quem manda é sempre o .xlsx: se os dois
divergirem, rode este script de novo. Nunca edite o .csv à mão.

Uso:
    python exportar_csv.py
"""

import csv
import datetime
import os
import sys

import openpyxl

PLANILHA = "playlist-historia-v2.xlsx"
SAIDA = "playlist-historia-v2.csv"


def texto(valor):
    """Devolve a célula como string estável, para o diff não oscilar à toa."""
    if valor is None:
        return ""
    if isinstance(valor, datetime.datetime):
        return valor.strftime("%Y-%m-%d")
    if isinstance(valor, datetime.date):
        return valor.isoformat()
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor))
    return str(valor)


def main():
    if not os.path.exists(PLANILHA):
        print(f"\nERRO: não encontrei {PLANILHA} nesta pasta.\n")
        sys.exit(1)

    ws = openpyxl.load_workbook(PLANILHA, read_only=True, data_only=True).active

    linhas = 0
    # newline="" é exigência do módulo csv; lineterminator="\n" mantém o
    # arquivo com quebra de linha Unix, para o diff não virar ruído no Git.
    with open(SAIDA, "w", encoding="utf-8-sig", newline="") as f:
        escritor = csv.writer(f, lineterminator="\n")
        for linha in ws.iter_rows(values_only=True):
            escritor.writerow([texto(c) for c in linha])
            linhas += 1

    print(f"{SAIDA}: {linhas} linhas ({linhas - 1} vídeos + cabeçalho)")


if __name__ == "__main__":
    main()
