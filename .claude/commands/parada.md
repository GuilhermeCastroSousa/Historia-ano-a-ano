---
description: Parada de revisão a cada quatro lotes — vocabulário, fact-check e amostra
---

Faça a parada de revisão dos últimos quatro lotes, conforme o `protocolo.md`,
seção "Rotina de quatro lotes".

Escreva o dossiê em `paradas/parada-NNN-NNN.md`, além de apresentar aqui — numa
rodada longa o relato da primeira parada não sobrevive até a última se morar só
na conversa, e as pendências se perdem entre sessões.

**1. Vocabulário**
- Lista única de todos os termos novos acumulados nos quatro lotes
- Sobreposições: temas que deveriam ser um só, subtemas duplicados, termos que
  viraram tema e região ao mesmo tempo (`python consultar.py <termo>` acha as
  que a memória não acha)
- Regiões usadas por aproximação porque a Lista B não tinha a certa

**2. Fact-check**
Escolha as datações de maior risco — as `chute` e as que você inferiu de
conhecimento geral — e verifique uma amostra com search. Reporte o que bateu e
o que não bateu, com a fonte.

**3. Amostra para o humano**
`python amostra.py NNN NNN NNN NNN` sorteia as 5 com semente fixa derivada dos
lotes — o sorteio não é escolha de quem apresenta, e é reproduzível. O script
imprime a classificação e a nota; **você acrescenta a evidência** do
`lote-NN.md` (capítulos e datas citadas), que ele não tem. Apresente assim:

```
[n] Título
    CLASSIFIQUEI: período | Ano | Mês | Dias | Região > Tema > Subtema | confiança/status
    EVIDÊNCIA: os capítulos e as datas citadas do lote-NN.md
```

Não escolha as mais fáceis. Se alguma das 5 for uma decisão que você tomou com
pouca base, diga isso na hora de apresentar.

**4. Estado**
Contagem por lote, por status e por confiança. Pendências abertas.

Não trave nada e não mexa no vocabulário ainda — espere eu conferir as 5 linhas.
