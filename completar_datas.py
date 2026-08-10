"""
Preenche a coluna 'publicado' das linhas antigas do catálogo (lote 0), que foram
catalogadas à mão antes do sistema existir e por isso não têm data de publicação.

Roda uma vez só. Gasta pouquíssima cota: uma chamada a cada 50 vídeos.

Uso:
    python completar_datas.py
"""

import openpyxl
import coletar          # reaproveita a chave, a função api() e as configurações

PLANILHA = coletar.PLANILHA

coletar.CHAVE = coletar.ler_chave()

wb = openpyxl.load_workbook(PLANILHA)
ws = wb["Catálogo"]
cab = [c.value for c in ws[1]]
for obrigatoria in ("video_id", "publicado"):
    if obrigatoria not in cab:
        coletar.erro(f"a planilha não tem a coluna '{obrigatoria}'.")
col_id, col_pub = cab.index("video_id") + 1, cab.index("publicado") + 1

faltando = {}
for linha in ws.iter_rows(min_row=2):
    vid = linha[col_id - 1].value
    if vid and not linha[col_pub - 1].value:
        faltando.setdefault(str(vid).strip(), []).append(linha[col_pub - 1])

if not faltando:
    print("\nTodas as linhas já têm data de publicação. Nada a fazer.\n")
    raise SystemExit

ids = list(faltando)
print(f"\n{len(ids)} linhas sem data de publicação. Buscando na API…")

encontrados = 0
for i in range(0, len(ids), 50):
    bloco = ids[i:i + 50]
    r = coletar.api("videos", part="snippet", id=",".join(bloco))
    for item in r.get("items", []):
        data = item["snippet"]["publishedAt"][:10]
        for celula in faltando.get(item["id"], []):
            celula.value = data
        encontrados += 1
    print(f"  {min(i + 50, len(ids))}/{len(ids)}")

wb.save(PLANILHA)

sumidos = len(ids) - encontrados
print(f"\nPronto: {encontrados} datas preenchidas.")
if sumidos:
    print(f"{sumidos} vídeos não foram encontrados — provavelmente removidos "
          f"do YouTube ou tornados privados. Continuam sem data.")
print(f"Planilha salva: {PLANILHA}\n")
