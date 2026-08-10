---
description: Marca um canal como encerrado em canais.json e registra o estado final
---

O canal terminou. Registre o encerramento.

Se eu não disse qual canal, use o que estiver `em andamento` no `canais.json`.
Se houver mais de um, pergunte.

## O que fazer

1. **Levante os números do canal**, direto da planilha (coluna `Canal`) e do
   `canais.json`: total de linhas, faixa de lotes, quantas em `revisar`,
   distribuição de confiança, e a data do vídeo mais recente coletado.

2. **Rode `python verificar.py`** e me diga o resultado.

3. **Avise, sem bloquear:** se houver linha em `revisar` desse canal, ou se o
   portão falhar, ou se a Lista C do `vocabulario-canonico.md` estiver
   desatualizada, **diga isso em voz alta antes de encerrar** — mas encerre
   assim mesmo, se eu pedi. A decisão é minha; o seu papel é não me deixar
   fechar às cegas.

   O motivo de existir esse aviso: a parada só dispara como parte do loop de
   coleta. Com o canal encerrado, o loop para e a pendência vira permanente.
   Aconteceu com o Kings and Generals — 109 linhas ficaram órfãs e só foram
   revisadas numa passada avulsa, semanas depois.

4. **Atualize o `canais.json`**: `status` para `encerrado`, `encerrado_em` com
   a data de hoje, `ultimo_lote` conferido contra a planilha, e um
   `observacoes` curto com o que a próxima pessoa precisa saber (buracos em
   lotes, rótulos criados por causa desse canal, séries longas, decisões de
   escopo). Não invente: só o que aconteceu de fato.

5. **Atualize o `CLAUDE.md`** para refletir que o canal saiu de cena e qual é o
   estado geral agora.

## O que o encerramento muda na prática

`status = encerrado` autoriza o `coletar.py` a **parar de paginar** assim que
encontra uma página inteira já conhecida, na próxima vez que esse canal for
coletado. Isso só é seguro porque um canal encerrado foi consumido até o fim —
não há vídeo antigo desconhecido abaixo. Por isso **não marque encerrado um
canal que foi abandonado no meio**: use outro status, ou deixe `em andamento`.

Revisitar depois é só rodar `python coletar.py @Handle` de novo. Ele vai pegar
só o que foi publicado desde a última coleta, gravar um lote parcial (3 vídeos
viram um lote de 3, e está certo) e continuar a numeração única de lotes.

## Responda com

- canal, faixa de lotes, total de linhas
- pendências encontradas, se houver — e o que eu perdi ao encerrar com elas
- o que você escreveu em `observacoes`
- resultado do `verificar.py`
