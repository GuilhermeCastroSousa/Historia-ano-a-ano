---
description: Roda até 4 lotes seguidos (25 vídeos cada, nunca um lote de 100) sem pausar para perguntar, e encerra com a parada de revisão
---

Rode uma rodada completa: até 4 lotes de 25, um atrás do outro, sem parar para
perguntar nada no meio — e feche com a parada de revisão. Siga `CLAUDE.md`,
`protocolo.md` e `vocabulario-canonico.md` o tempo todo, exatamente como em
`/lote` e `/parada`; este comando só encadeia os dois sem pausas manuais.

**Cada lote continua sendo um lote de 25, não um lote de 100.** Rode
`python coletar.py` quatro vezes em sequência (uma por lote), cada vez
gerando o próprio `lote-NN.md`, cada vez com seu próprio backup e sua
própria checagem `verificar.py` antes de seguir para o próximo. Nunca junte
a classificação de mais de 25 vídeos numa só gravação.

## Loop (repita até 4 vezes)

Para cada lote:

1. `python coletar.py` para gerar o `lote-NN.md`
2. Leia o arquivo inteiro antes de classificar
3. Copie a planilha para `backups\playlist-AAAA-MM-DD-HHMM.xlsx`
4. Classifique as 25 linhas
5. Grave usando `cell.value = v`, **nunca** `ws.cell(row, col, value=v)` —
   esse último não limpa célula quando o valor é `None` e já corrompeu
   linhas antigas neste projeto
6. `python verificar.py --anterior backups\<o backup que você acabou de fazer>`

**Checagem de confiança antes de seguir para o próximo lote:** para cada
linha marcada `confianca = alta`, confirme que alguma data citada no bloco de
evidência daquele vídeo cai dentro da faixa `ano_inicio..ano_fim` declarada.
Datas de títulos de vídeos linkados e do bloco fixo que o canal repete na
série não valem. Sem data própria, o teto é `média`; sem nenhuma data, é
`chute`. Rebaixe antes de gravar, não depois.

### O que NÃO pausa o loop

Decisão duvidosa não é motivo de parada — é o motivo de existir a parada no
fim. Termo novo sem forma óbvia, data incerta, vídeo estranho: classifique
com a confiança que a evidência sustenta (`revisar` quando for `média` ou
`chute`), registre o raciocínio em `notas`, e siga. Isso é exatamente o que
`protocolo.md` já manda ("só erro crítico interrompe") — este comando só
torna explícito que vale para os quatro lotes inteiros, não só um.

### O que PARA o loop

- **`verificar.py` sai com 1** (erro real de estrutura/dado, não incerteza de
  classificação): pare tudo imediatamente. Restaure a planilha do backup
  daquele lote (`copy backups\<arquivo> playlist-historia-v2.xlsx`), não
  tente os lotes seguintes, e relate exatamente o que falhou e em qual lote.
- **`coletar.py` retorna 0 vídeos novos** (canal esgotou no meio da rodada):
  pare o loop nesse ponto — não force um quarto lote que não existe. Isso já
  é padrão neste projeto (mini-ciclo por esgotamento, ver `CLAUDE.md` para
  vários exemplos: Cambrian Chronicles, The Histories, HistoryMarche etc.).
  Trate os lotes já rodados como o ciclo inteiro e siga direto para a parada.
- Qualquer outro erro que impeça gravar a planilha com segurança (arquivo
  travado, coluna faltando, etc.).

Se o loop parar por erro real, **não rode a parada** — relate o problema e
espere instrução.

## Parada (ao final do loop, só se todos os lotes rodados saíram limpos)

Depois do último lote da rodada (4, ou menos por esgotamento), rode a
sequência de `/parada` sobre os lotes que entraram nesta rodada:

1. **Vocabulário** — lista única de todos os termos novos acumulados nos
   lotes desta rodada, sobreposições, regiões usadas por aproximação.
2. **Fact-check** — escolha as datações de maior risco (as `chute` e as
   inferidas de conhecimento geral) e verifique uma amostra com busca
   externa. Reporte o que bateu e o que não bateu, com a fonte.
3. **Amostra para o humano** — sorteie 5 linhas entre as da rodada e
   apresente cada uma com período/Ano/Região/Tema/Subtema/confiança e a
   evidência do `lote-NN.md`. Não escolha as mais fáceis; sinalize as que
   você decidiu com pouca base.
4. **Estado** — contagem por lote, por status e por confiança. Pendências
   abertas.

Não trave nada e não mexa no vocabulário ainda — a parada é para eu
conferir as 5 linhas. `/aprovar` continua sendo um passo manual separado,
depois que eu responder sobre a amostra.

## Resposta final

Ao terminar (por completar os 4 lotes ou por esgotamento no meio), inclua:

- quantos lotes rodaram nesta rodada, e por que parou nesse número (4
  completos, ou esgotamento em qual lote)
- linhas antes da rodada, linhas depois, quantas entraram no total
- quantas ficaram `ok` e quantas `revisar`, por lote e no total
- termos novos propostos (tema, subtema, região) da rodada inteira
- o resultado da checagem de confiança `alta` (linha por linha, não só o
  total)
- qualquer coisa que o `verificar.py` tenha avisado em qualquer lote
- o relatório da parada (vocabulário, fact-check, amostra, estado)
