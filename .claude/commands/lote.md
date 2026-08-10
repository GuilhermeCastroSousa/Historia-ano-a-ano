---
description: Roda o próximo lote do catálogo de história, do zero à gravação
---

Rode o próximo lote seguindo o `CLAUDE.md`.

Sequência obrigatória:

1. `python coletar.py` para gerar o `lote-NN.md`
2. Leia o arquivo inteiro antes de classificar
3. Copie a planilha para `backups\playlist-AAAA-MM-DD-HHMM.xlsx`
4. Classifique as 25 linhas
5. Grave usando `cell.value = v`, **nunca** `ws.cell(row, col, value=v)` —
   esse último não limpa célula quando o valor é `None` e já corrompeu
   linhas antigas neste projeto
6. `python verificar.py --anterior backups\<o backup que você acabou de fazer>`
7. Se sair 1, restaure do backup e me diga o que falhou. Não salve com falha.

Antes de me responder, faça esta checagem e inclua o resultado:

**Para cada linha que você marcou `confianca = alta`, alguma data citada no
bloco de evidência daquele vídeo cai dentro da faixa `ano_inicio..ano_fim` que
a linha declara?** Se não cair nenhuma, a linha não pode ser `alta` — datas de
títulos de vídeos linkados e do bloco fixo que o canal repete na série não
valem. Sem data própria, o teto é `média`; sem nenhuma data, é `chute`.

Esse erro já aconteceu em 8 de 13 linhas `alta` num lote.

Responda com:
- linhas antes, linhas depois, quantas entraram
- quantas ficaram `ok` e quantas `revisar`
- termos novos propostos (tema, subtema, região)
- o resultado da checagem de confiança acima
- qualquer coisa que o `verificar.py` tenha avisado
