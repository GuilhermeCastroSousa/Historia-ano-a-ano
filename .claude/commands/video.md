---
description: Insere um vídeo avulso de um canal já adotado, fora do loop normal de lote
---

Insira um único vídeo no catálogo, seguindo o `CLAUDE.md`.

Se eu não disse **qual vídeo** (id ou link) e **de qual canal** (a chave
exata que aparece em `canais.json`, ex.: `@MagistraVitae`), pergunte os dois
antes de rodar qualquer coisa. Não adivinhe o canal pelo conteúdo do vídeo —
`--canal` é obrigatório e tem que bater com o `channelId` real do vídeo, ou o
`coletar.py` recusa sozinho.

Vídeo de canal que **não está** em `canais.json` não entra por aqui: primeiro
se adota o canal com `python coletar.py @Handle` (mesmo que só para registrar
— não precisa virar uma rodada completa).

## Sequência obrigatória

1. `python coletar.py --video <id_ou_link> --canal <chave>` para gerar o
   `lote-NN.md` (lote de 1 vídeo). O script já recusa sozinho, sem gravar
   nada na planilha:
   - vídeo já catalogado, no ledger ou nos descartados (dedup)
   - canal não adotado em `canais.json`
   - vídeo que pertence a outro canal do YouTube (confere `channelId`)
   - Short, live, ou exclusivo de membros/teaser — nesses três casos ele já
     escreveu o id em `descartados.txt` antes de recusar, porque são os
     mesmos critérios que valeriam num lote normal

   Leia a mensagem de erro inteira antes de tentar de novo — ela diz qual
   dessas checagens barrou.

2. Leia o `lote-NN.md` gerado inteiro antes de classificar.

3. Copie a planilha para `backups\playlist-AAAA-MM-DD-HHMM.xlsx`.

4. Classifique a linha: `Ano`, `Região`, `Tema`, `Subtema`, `confianca`,
   `status`, `notas`. Se propuser tema/subtema/região novo, preencha marcado
   `revisar` e explique na resposta — nunca insira em silêncio, mesmo sendo
   uma linha só.

5. `python gravar.py classificacao.json lote-NN.md` — **não escreva script de
   inserção próprio.** Ele cuida da posição: reordena a v2 pela chave completa
   (`ano_inicio`, `ano_fim`, `Mês`, `Dias`). O `protocolo.md` registra três
   bugs de ordenação vindos de script de inserção escrito na hora, e um deles
   foi exatamente num lote de um vídeo.

6. `python verificar.py --anterior backups\<o backup que você acabou de fazer>`

7. Se sair 1, restaure do backup e me diga o que falhou. Não salve com falha.

8. `python exportar_csv.py` e `python ordenar.py --gravar` — o segundo regera a
   ordem de exibição na `playlist-historia-v3.xlsx`. Um vídeo avulso quase
   sempre muda a posição de exibição de outros, porque pode abrir ou fechar um
   bloco.

## Antes de responder

Mesma checagem de confiança do `/lote`: se marcou `alta`, alguma data do
bloco de evidência cai dentro da faixa `ano_inicio..ano_fim` que a linha
declara? Datas de título/tags sozinhas não sustentam `alta` — teto `média`.
Sem nenhuma data, `chute`.

Essa linha nasce **sem travar** (`travado` vazio) — travar é trabalho do
`/aprovar`, não da inserção, mesmo sendo um lote de 1.

## Responda com

- vídeo (id, título), canal, lote gerado
- classificação proposta e a linha do Excel onde entrou
- termos novos propostos, se houver
- resultado da checagem de confiança
- o que o `verificar.py` avisou
