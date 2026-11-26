# -*- coding: utf-8 -*-
r"""Aplica na v2 uma camada aprovada do `merge-temas-proposta.md`.

    python aplicar_merge.py merges/a1-r.json

O JSON tem duas chaves, as duas opcionais:

    {"fusao":       {"tema antigo": "tema novo", ...},
     "renomeacao":  {"nome velho": "nome novo", ...},
     "rotulo":      "A1 e R, aprovadas em 26/11/2026"}

**Fusão e renomeação não são a mesma coisa**, e é por isso que o arquivo separa
as duas: numa fusão o tema antigo é informação que precisa sobreviver em algum
lugar; numa renomeação é só outro nome para a mesma coisa, e guardá-lo seria
ruído. Quem decide em qual lista cada par entra é o `propor_merge.py`, contando
quantas origens apontam para cada destino.

REGRA DO SUBTEMA NA FUSÃO, medida contra as 84 linhas da planilha que o humano
ordenou à mão que caem na camada A1:

  - Subtema vazio -> recebe o tema antigo. Medido: as 23 linhas em que ele pôs
    exatamente o tema antigo no Subtema são todas, e só, as que estavam sem
    subtema (`Esparta`, `Civilização Micênica`, `Corinto`, `Colonização grega`,
    `Civilização Minoica`).
  - Subtema cheio -> PRESERVA o que já está lá. Aqui ele não preservou (12 de
    ~39): reescreveu à mão, caso a caso, com a forma curta da civilização
    (`Suméria`, `Assíria`, `Atenas`) ou uma palavra nova e editorial
    (`Cultura`, `Arte`, `Ur`, `Yahweh`). Não há regra a extrair disso, e
    empurrar o tema antigo por cima destruiria `Império Neo-Sumério (Ur III)`,
    `Guerras Messênias`, `Cuneiforme`. Preservar é a opção que não perde nada;
    a reescrita editorial fica para ele.

Renomeação não toca no Subtema.

ATENÇÃO: isto escreve na planilha e quase certamente vai mexer em linha
travada, porque qualquer tema com história tem linhas de ciclos já aprovados.
Então, na ordem:

  1. backup   copy playlist-historia-v2.xlsx backups\playlist-AAAA-MM-DD-HHMM.xlsx
  2. este script (grava, e deixa os ids em merges/<nome>-ids.txt)
  3. python verificar.py --anterior <backup>      -> vai falhar em TRAVADAS
  4. python conferir_travadas.py <backup> merges/<nome>-ids.txt
     -> só se este sair 0 a falha do passo 3 vale como falso-positivo
  5. python exportar_csv.py  &&  python ordenar.py --gravar
"""
import collections
import json
import os
import sys

import openpyxl

from verificar import ABA, COLUNAS, PLANILHA

NOTA_FUSAO = (" | Tema fundido em '{novo}' em {data} ({rotulo}). {subtema}")
NOTA_RENOME = (" | Tema renomeado de '{velho}' para '{novo}' em {data} "
               "({rotulo}). Subtema intacto.")


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip())
        return 2
    caminho = argv[1]
    with open(caminho, encoding="utf-8") as f:
        spec = json.load(f)
    fusao = spec.get("fusao", {})
    renome = spec.get("renomeacao", {})
    rotulo = spec.get("rotulo", os.path.basename(caminho))
    data = spec.get("data", "data não declarada")
    if not fusao and not renome:
        print("o JSON não traz nem 'fusao' nem 'renomeacao'")
        return 2
    colisao = set(fusao) & set(renome)
    if colisao:
        print(f"tema em 'fusao' E em 'renomeacao': {sorted(colisao)}")
        return 2
    # Um destino que também é origem faria o resultado depender da ordem.
    cadeia = (set(fusao) | set(renome)) & (set(fusao.values())
                                           | set(renome.values()))
    if cadeia:
        print(f"destino que também é origem (fusão em cadeia): {sorted(cadeia)}"
              f"\nresolva a cadeia no JSON antes de aplicar")
        return 2

    wb = openpyxl.load_workbook(PLANILHA)
    ws = wb[ABA]
    if [c.value for c in ws[1]] != COLUNAS:
        print("cabeçalho inesperado na planilha")
        return 2
    ic = {c: i + 1 for i, c in enumerate(COLUNAS)}

    contagem, mudadas, nao_achados = collections.Counter(), [], []
    presentes = set()
    for linha in range(2, ws.max_row + 1):
        cel_tema = ws.cell(row=linha, column=ic["Tema"])
        velho = cel_tema.value
        if velho not in fusao and velho not in renome:
            continue
        presentes.add(velho)
        cel_sub = ws.cell(row=linha, column=ic["Subtema"])
        cel_notas = ws.cell(row=linha, column=ic["notas"])
        if velho in fusao:
            novo = fusao[velho]
            if cel_sub.value:
                texto = f"Subtema preservado ('{cel_sub.value}')."
                contagem["fusão · subtema preservado"] += 1
            else:
                cel_sub.value = velho
                texto = "O tema antigo virou o Subtema."
                contagem["fusão · tema antigo virou subtema"] += 1
            cel_notas.value = (cel_notas.value or "") + NOTA_FUSAO.format(
                novo=novo, data=data, rotulo=rotulo, subtema=texto)
        else:
            novo = renome[velho]
            cel_notas.value = (cel_notas.value or "") + NOTA_RENOME.format(
                velho=velho, novo=novo, data=data, rotulo=rotulo)
            contagem["renomeação"] += 1
        cel_tema.value = novo
        mudadas.append(ws.cell(row=linha, column=ic["video_id"]).value)

    nao_achados = sorted((set(fusao) | set(renome)) - presentes)
    print(f"{rotulo}")
    for k, n in sorted(contagem.items()):
        print(f"  {n:>4}  {k}")
    print(f"  {len(mudadas):>4}  linhas no total")
    if nao_achados:
        print(f"\naviso: {len(nao_achados)} tema(s) do JSON não existem na "
              f"planilha e foram ignorados:")
        for t in nao_achados:
            print(f"      {t}")
    if not mudadas:
        print("\nnada a fazer — planilha não gravada")
        return 1

    wb.save(PLANILHA)
    ids = os.path.splitext(caminho)[0] + "-ids.txt"
    with open(ids, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(mudadas) + "\n")
    print(f"\n{PLANILHA} gravada. Ids em {ids}.")
    print(f"Agora: python conferir_travadas.py <backup> {ids}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
