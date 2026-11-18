---
description: Roda o próximo lote do catálogo de história, do zero à gravação
---

Rode o próximo lote seguindo o `CLAUDE.md`.

Sequência obrigatória:

1. `python coletar.py` para gerar o `lote-NN.md`.
   **Em revisita de canal `encerrado`, use `--desde AAAA-MM-DD`** com a
   `ultima_coleta` que o canal tinha antes desta rodada — sem isso a parada
   antecipada esconde os vídeos novos das páginas seguintes (ver `CLAUDE.md`).
2. Leia o arquivo inteiro antes de classificar
3. Copie a planilha para `backups\playlist-AAAA-MM-DD-HHMM.xlsx`
4. Classifique as 25 linhas. Antes de propor termo novo,
   `python consultar.py <termo>` — procura na planilha, não na Lista C, que só
   é regenerada nas aprovações
5. `python gravar.py classificacao.json lote-NN.md` — **não escreva script de
   gravação próprio.** O `gravar.py` calcula `Século/Período`,
   `ano_inicio`/`ano_fim`, `Link` e `travado`, confere os ids contra o arquivo
   de lote e reordena a planilha pela chave completa (`ano_inicio`, `ano_fim`,
   `Mês`, `Dias`). O `protocolo.md` registra o mesmo bug de ordenação três
   vezes, sempre num script escrito na hora
6. `python verificar.py --anterior backups\<o backup que você acabou de fazer>`
7. Se sair 1, restaure do backup e me diga o que falhou. Não salve com falha.
8. `python exportar_csv.py`, depois de o portão passar

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
