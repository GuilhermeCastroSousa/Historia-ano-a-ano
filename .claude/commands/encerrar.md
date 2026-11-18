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

## Antes de encerrar: prove o esgotamento, não o presuma

```
python auditar.py @Handle
```

**"A coleta seguinte veio com 0 vídeos novos" não prova nada se o canal já
estava `encerrado`** — esse 0 pode ser a parada antecipada, que o próprio
status liga. É circular, e custou caro: a auditoria de 17/11/2026 achou 1216
vídeos catalogáveis nunca coletados em canais marcados "esgotamento real" —
1009 no Invicta, 204 no Kings and Generals. Ver `protocolo.md`, "esgotamento
que se auto-confirma".

O `auditar.py` varre o uploads inteiro sem parada antecipada e diz quantos
vídeos o projeto nunca viu, separando os publicados depois da última coleta
(novos) dos mais antigos (buraco de cobertura). **Se aparecer qualquer ANTIGO,
o canal não está esgotado** — diga isso antes de encerrar.

## O que o encerramento muda na prática

`status = encerrado` autoriza o `coletar.py` a **parar de paginar** assim que
encontra uma página inteira já conhecida, na próxima vez que esse canal for
coletado. Esse atalho pressupõe que não há vídeo antigo desconhecido abaixo — e
essa premissa já falhou duas vezes. Por isso **não marque encerrado um canal
que foi abandonado no meio**: use outro status, ou deixe `em andamento`.

Revisitar depois é `python coletar.py @Handle --desde AAAA-MM-DD`, com a
`ultima_coleta` anterior à revisita. O `--desde` desliga a parada antecipada e
a troca por uma parada por data: pega o que foi publicado desde o corte, grava
um lote parcial (3 vídeos viram um lote de 3, e está certo) e não arrasta nem
descarta o acervo antigo. **Sem o `--desde`, a partir do segundo lote de uma
revisita a primeira página fica toda conhecida e os vídeos novos das páginas
seguintes ficam invisíveis** — foi o que travou o lote 233.

## Responda com

- canal, faixa de lotes, total de linhas
- pendências encontradas, se houver — e o que eu perdi ao encerrar com elas
- o que você escreveu em `observacoes`
- resultado do `verificar.py`
