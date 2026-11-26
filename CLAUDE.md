# Catálogo de história — instruções de sessão

Cataloga vídeos de história do YouTube numa planilha ordenada pelo período que o
vídeo **trata**, não pela data de publicação. Ordem: 20000 a.C. até hoje, numa
linha do tempo só.

**Leia antes de qualquer coisa:** `protocolo.md` (manual de operação) e
`vocabulario-canonico.md` (listas fechadas de período, região, tema e subtema).
Os dois são a fonte de verdade. Este arquivo não os repete — só cobre o que muda
por você estar rodando com acesso de escrita ao disco.

**O histórico narrativo de cada canal (ciclos, temas introduzidos, fact-checks,
correções, pendências) mora em `canais.json`, campo `observacoes`.** Não repita
esse conteúdo aqui: este arquivo entra em toda requisição da sessão e crescer é
caro. Ao fechar um ciclo ou um canal, escreva o relato completo no `canais.json`
e, aqui, no máximo uma linha se houver uma **armadilha operacional** nova.

---

## Estado: vinte canais adotados, todos encerrados e **todos em dia**

`verificar.py` (sem `--anterior`) confere limpo nesse estado: **5567 linhas, 0
`revisar`, checklist ok**. **Nenhum canal está `em andamento`** — a próxima
sessão precisa adotar um canal novo ou reabrir um dos vinte antes de rodar
`/lote` ou `/rodada`.

| Canal | Lotes | Chave / comando de reabertura |
|---|---|---|
| Kings and Generals | 0-76, 232-233 | `@KingsandGenerals` |
| Thersites the Historian | 40-75, 234-235 | `@ThersitestheHistorian` |
| Ancient Americas | 77-78, 236 | `@AncientAmericas` |
| Historia Civilis | 79-82 | `@HistoriaCivilis` |
| Cambrian Chronicles | 83-84, 237 | `@CambrianChronicles` |
| The History of Rome (Mike Duncan) | 85-86 | `--playlist PLe1Vkrjzhwzq1an-AHk4lljmnkiUN2WUe` |
| The History of Byzantium Podcast | 87-102, 238 | `@TheHistoryofByzantiumPodcast` |
| SandRhoman History | 103-109, 239 | `@SandRhomanHistory` |
| The Shogunate | 110-121, 240 | `@theshogunate` |
| The Histories | 122, 241 | `@TheHistoriesYT` |
| GatesOfKilikien | 123-124, 242 | `@gatesofkilikien` |
| Revolutions (Mike Duncan) | 125-138 | `--playlist PLIjP3HEQ0F-8B6x_9l4bJef2q4hFvb9s0` |
| Magistra Vitae | 139-140, 231, 243 | `@MagistraVitae` |
| Ryan M Reeves | 141-148, 244 | `@ryanreevesm` |
| HistoryMarche | 149-158, 245 | `@historymarche` |
| History with Cy | 159-167, 246 | `@historywithcy` |
| Epic History | 168-171 | `@EpichistoryTv` |
| Invicta | 172-183, 247 | `@invictahistory` |
| History of Philosophy Without Any Gaps | 184-214, 248 | `@HistoryofPhilosophywithoutGaps` |
| ESOTERICA | 215-230, 249 | `@TheEsotericaChannel` |

Detalhe de cada canal — séries longas, buracos de lote, temas introduzidos,
correções de aprovação, o relato da reabertura — em `canais.json`.

## Reabertura de 17/11/2026: lotes 232-249, 152 linhas

Os vinte canais foram reabertos **só para o que publicaram desde a última
coleta**, com `coletar.py --desde`. Todos verificados em dia depois (varredura
completa do uploads, zero pendente). Quatro não tinham nada catalogável:
Historia Civilis, The History of Rome, Revolutions e Epic History (este
publicou 39 vídeos, todos Short ou live).

Os dossiês das cinco paradas estão em `paradas/parada-NNN-NNN.md` — um por
rodada de quatro lotes, com vocabulário novo, fact-check e as cinco linhas
sorteadas. **`/aprovar` rodou em 17/11/2026 sobre os 18 lotes de uma vez:** as
152 linhas estão travadas, a Lista C foi regenerada (515 → 525 temas-raiz, 10
novos) e seis correções foram aplicadas antes da trava — três de faixa apontadas
pelo fact-check (`HARdgJjiR7s` Povo Romani 1000 → 500; `t6VFz7kXiLc` Reino de
Kent 455 → 449; `OUJAl2VK1pw` Safo 630 → 612 a.C.) e três de tema, com
autorização explícita para sobrescrever célula travada (as resenhas de precisão
histórica saíram de `Resenhas de ficção` para `História na cultura popular >
Cinema`).

As pendências que **não** foram aplicadas estão no `vocabulario-canonico.md`,
"Sobreposições ainda por resolver" — sete sobreposições de vocabulário, todas
dependendo de sobrescrever linha travada de ciclo anterior ou de reclassificar
linha antiga.

## Ressalvas ainda abertas

- **Dois canais foram marcados `encerrado` sem estarem esgotados, e o acervo
  antigo deles segue fora do catálogo:** Invicta (**1009** vídeos catalogáveis
  de 2013-2019 nunca coletados) e Kings and Generals (**204**, de 2017-2019).
  Conferido por título: não são reupload. A causa é estrutural — ver a armadilha
  "esgotamento que se auto-confirma" no `protocolo.md`. Os outros 18 canais
  foram auditados com varredura completa e estão íntegros. Reabrir esse acervo é
  decisão pendente do humano: são ~41 lotes só no Invicta.
- **A proposta de fusão de temas (`merge-temas-proposta.md`) está aplicada,
  menos a camada B.** Em 26/11/2026 entraram **A1** (17 fusões), **R** (6
  renomeações), **A3** (26), metade da **A2** e o tema-raiz novo **`Roma
  antiga`** (69 linhas, a resposta ao que travou a camada B): **525 → 482
  temas-raiz**, 321 linhas em três passadas, e o tema passou a bater com a
  planilha que o humano ordenou à mão em 254/290 (88%), contra 50% antes. Cada
  passada tem seu JSON em `merges/`, com a autorização citada e o que ficou de
  fora. O que não entrou: `Vida urbana` → `Império Hitita` (transversal —
  Quioto e Alexandria iriam para um tema de 2 linhas sobre hititas) e os dois
  itens samurai da camada B (o destino eram 41 resenhas de videogame). A lista
  de trabalho **C** da proposta é inventário, nunca foi proposta.
- **Escolher entre tema-raiz neutro e tema-raiz de fase** (`Roma antiga` ×
  `República Romana`) segue a regra em `vocabulario-canonico.md`, seção
  "Tema-raiz: a civilização ou uma fase dela?". Não crie neutro novo por
  simetria — ver a armadilha "padrão de aspecto" no `protocolo.md`.
- **`Levante` é termo novo da Lista B** (61 termos), de 26/11/2026: use para
  Canaã, Fenícia levantina, Ugarit e Filisteia. `Judeia` segue para o que é
  especificamente judaico e `Oriente Médio` para Mesopotâmia. Entrou porque
  `Oriente Médio` não distinguia Canaã de Mesopotâmia e a `PONTE_REGIAO` do
  `ordenar.py` só sabia apontar para Mesopotâmia — 18 linhas foram
  reclassificadas. Ver a armadilha "fundir um tema geográfico dentro de um
  tema temático" no `protocolo.md`.
- **A Lista C do `vocabulario-canonico.md` não cobre os lotes 107-109**
  (SandRhoman History). Antes de propor um tema que pode já existir, confira o
  `observacoes` desse canal em `canais.json`.
- **Das três pendências que o portão barrava, duas foram fechadas em
  26/11/2026 e uma fica.** `xDV0UEgmEbQ` (HPI 60, lote 200) saiu de
  `Extra`/`n/a` para `Panorama (973 - 1860)`/`média`, pela convenção de que
  conteúdo conceitual sem evento datável entra pela faixa ampla do conceito —
  a recepção vai de al-Bīrūnī (973-1048) a Schopenhauer; o rótulo é o que a
  escada calcula. A compilação "Hannibal PARTS 18-20" (`OtqFPmkBiqI`, lote
  151) teve a faixa **conferida e mantida**: a suspeita era o início estar um
  ano adiantado, e o próprio catálogo resolve — a Parte 18 é a Batalha de
  Cumae e o título dela diz 215 a.C., e a compilação anterior, PARTS 14-17,
  fecha em 215. **Fica `TbVfFq16gK8`** (HistoryMarche, Basílio II Part 7, lote
  152): a dúvida é se o vídeo trata da batalha certa, e isso não se resolve com
  a evidência permitida — a descrição é só bibliografia, o título não tem data
  e o projeto não usa transcrição. A linha já está honesta, com `chute` e nota.
  Não é mais o portão que barra; é a falta de evidência.
- **Corrigir linha travada é possível, e já foi feito duas vezes.** Na aprovação
  dos lotes 232-249, três linhas `Extra` (que nascem travadas por design)
  tiveram Tema e Subtema corrigidos com autorização explícita do humano. Em
  26/11/2026, a aplicação das camadas A1 e R da proposta de fusão de temas
  mexeu em **155 linhas**, a maioria travada de ciclos antigos, sob a
  autorização por escrito que abriu a reorganização ("todo o catálogo está
  destravado para esta revisão"). Nos dois casos o caminho foi o mesmo. O
  `verificar.py` acusa "linhas TRAVADAS alteradas" de qualquer jeito — ele
  compara valores, não motivos. O caminho é a checagem manual que o
  `protocolo.md` descreve: comparar a planilha nova com o backup e confirmar que
  **a única linha travada com qualquer diferença é exatamente a autorizada, e só
  nas células que deveriam mudar**. Só depois disso a falha do portão vale como
  falso-positivo esperado. Sem essa checagem, registre como pendente.
- **Pendências de vocabulário não bloqueantes** (sobreposições, nomes parecidos,
  clusters a consolidar) estão em `vocabulario-canonico.md`, "Sobreposições ainda
  por resolver". Não travam lote nenhum. **Triadas em 26/11/2026:** duas que
  tinham resposta por regra já escrita foram resolvidas (Heródoto saiu de
  `Extra`; a linha antiga do Skanderbeg ganhou o subtema que a nova já tinha).
  O resto ficou com o motivo anotado — `Guerra Civil Espanhola` é empate entre
  duas convenções do projeto, a Parte 1 dos Estados Combatentes está em
  confiança `alta` e encurtar a faixa seria sobrescrever evidência com palpite,
  e `Espanha` como termo de região são 94 linhas de trabalho editorial.
  **"A linha está travada" não é mais motivo para não corrigir** — o
  `conferir_travadas.py` cobre isso.

## Convenções que valem para qualquer canal

- **Live não entra**, mesma regra dos Shorts. O `coletar.py` filtra pela parte
  `liveStreamingDetails` da API — nunca `snippet.liveBroadcastContent` nem
  heurística de duração/título. Descoberto tarde no Thersites the Historian (202
  linhas de live entraram nos lotes 40-56; os buracos são permanentes).
- **Olhe uma amostra crua antes de classificar 25 linhas de um canal novo.** Os
  filtros que bastam para um canal podem deixar passar metade de outro.
- **Conteúdo biográfico/conceitual sem evento datável vai para a linha do tempo**
  (vida inteira do pensador, ou faixa ampla do conceito cross-era), nunca
  `Extra`/`Aleatório` por padrão — só administrivia real do canal vira `Extra >
  Avisos do canal`. Fixado com o humano nos canais de filosofia e esoterismo; ver
  `protocolo.md`.
- **Reupload é comum** (mesmo título/número, `video_id` diferente) e não é bug de
  dedup — visto no Byzantium, Revolutions, Shogunate, Ryan M Reeves, Magistra
  Vitae. Reavalie a faixa de forma independente, não copie a do par.

## Como adotar ou reabrir um canal

```
python coletar.py @Handle
```
Registra o canal em `canais.json` sozinho na primeira coleta. Para playlist:
`python coletar.py --playlist ID --nome "..."` (o `--nome` só na adoção). Em
revisita, lote parcial — às vezes de 1 vídeo — é o esperado.

**Em revisita de canal encerrado, use `--desde AAAA-MM-DD`** com a
`ultima_coleta` que o canal tinha *antes* desta rodada:

```
python coletar.py @Handle --desde 2026-07-31
```

Sem isso, a parada antecipada que `status: encerrado` liga para na primeira
página inteiramente conhecida — e depois do primeiro lote de uma revisita essa
página fica toda conhecida, escondendo os vídeos novos das páginas seguintes.
Foi o que travou o lote 233. O corte por data desliga essa parada e, em troca,
encerra a varredura quando aparece uma página só com vídeos anteriores ao corte,
então um acervo antigo nunca coletado não entra de carona nem vai para
`descartados.txt`.

**Vídeo avulso** (comando `/video`): `python coletar.py --video ID_OU_LINK
--canal @Handle`. A chave tem que já existir em `canais.json` — vídeo de canal
novo não passa por aqui, adote o canal primeiro.

**No PowerShell, use aspas no handle** (`"@Handle"`): sem elas, `@` vira operador
de splatting e o argumento some, caindo no `CANAL` hardcoded do script.

**Cuidado ao rodar `coletar.py` sem argumento:** a constante `CANAL` no topo do
script é hardcoded e **não acompanha** o canal `em andamento` do `canais.json` —
hoje ainda aponta para `@AncientAmericas` (lote 77). Rodar sem handle explícito
coleta do canal errado.

`catalogados.txt` e `descartados.txt` são compartilhados de propósito —
indexados por `video_id`, único no YouTube inteiro — e a numeração de lote é
única entre todos os canais, para o catálogo continuar sendo uma linha do tempo
só. A coluna `Canal` da planilha é a chave de agrupamento; o nome tem que bater
exatamente com a chave `nome` de `canais.json`.

---

## O loop (para um canal novo)

```
python coletar.py                      # gera lote-NN.md
                                       # classificar as 25 linhas
python gravar.py classificacao.json lote-NN.md
python verificar.py --anterior backups/playlist-AAAA-MM-DD.xlsx
                                       # só salvar se sair 0
python exportar_csv.py                 # espelho .csv, depois de gravar
python ordenar.py --gravar             # regera a v3, a ordem de exibição
```

## Duas camadas: v2 é o dado, v3 é o produto

A **v2** (`playlist-historia-v2.xlsx`) é a fonte de verdade, ordenada por
`ano_inicio`, com as invariantes do `verificar.py`. A **v3**
(`playlist-historia-v3.xlsx`) é **derivada** dela pelo `ordenar.py` e ordenada
para quem assiste em sequência: agrupa por civilização enquanto as datas são
largas, vira cronologia única em 500 a.C., e dentro de cada bloco o Panorama
abre, os Eventos vêm por data e o Temático fecha.

**Classifique na v2, sempre.** Nada se decide na v3 e nada se lê dela para
decidir dado. Ajuste manual de posição na v3 é perdido na próxima execução —
se uma linha caiu no lugar errado, conserte a coluna que a põe lá (`Tema`,
`Região`, ou a regra de `tipo`), não a posição.

As colunas novas da v3 (`ordem`, `era`, `tipo`, `regiao_historica`) são todas
derivadas. O modelo está nas Listas E, F e G do `vocabulario-canonico.md`; a
medição contra a planilha que o humano ordenou à mão está no `protocolo.md`,
seção "Duas camadas".

**`gravar.py` é o jeito de gravar um lote.** Recebe um JSON com os quatro campos
decididos por linha (`Ano`, `Regiao`, `Tema`, `Subtema`, mais `confianca`,
`status`, `notas`) e cuida do resto: calcula `Século/Período` pela escada,
`ano_inicio`/`ano_fim` pelo parser, monta o `Link`, puxa `Canal`/`Título`/
`publicado`/`lote` do próprio `lote-NN.md`, confere que o conjunto de ids bate
com o arquivo de lote, e **reordena a planilha inteira pela chave completa**
(`ano_inicio`, `ano_fim`, `Mês`, `Dias`). Ele existe porque o `protocolo.md`
registra o mesmo bug de ordenação três vezes — lotes 81, 85 e 171 —, sempre num
script de gravação escrito na hora. Não escreva outro.

**`exportar_csv.py` roda sempre que a planilha muda**, logo depois do
`verificar.py` passar. O `.csv` é derivado — o `.xlsx` é que manda. Ele existe
porque o Git não consegue mostrar diferença dentro de um arquivo binário: sem o
espelho, o histórico do repositório vira uma sequência de "binary files differ"
e ninguém consegue ver quais linhas entraram em cada lote. Nunca editar o `.csv`
à mão.

## Ferramentas, além do loop

| Script | Para que | Quando |
|---|---|---|
| `gravar.py` | grava o lote na v2 e reordena pela chave completa | todo lote |
| `ordenar.py` | deriva a v3, a ordem de exibição, com seu próprio portão | depois de gravar |
| `conferir_ordem.py` | mede a ordem gerada contra uma planilha ordenada à mão | ao mexer no modelo |
| `consultar.py` | procura um termo em Tema, Subtema e Título **na planilha** | antes de propor termo novo |
| `amostra.py` | sorteia as 5 linhas da parada, semente fixa pelos lotes | toda parada |
| `auditar.py` | varre o uploads inteiro e acha buraco de cobertura | antes de encerrar; depois de revisita |
| `exportar_csv.py` | espelho `.csv` | depois de gravar |
| `aplicar_merge.py` | aplica uma camada aprovada de `merge-temas-proposta.md` (JSON em `merges/`) | só com aprovação por escrito |
| `conferir_travadas.py` | confere que só as linhas e células autorizadas mudaram | sempre que mexer em linha travada |

Nenhum deles escreve na planilha, menos o `gravar.py` e o `aplicar_merge.py`
(este só com aprovação por escrito, e seguido do `conferir_travadas.py`). O
`auditar.py` não
escreve em arquivo nenhum — nem em `catalogados.txt`, nem em `descartados.txt`.

A cada quatro lotes, uma parada: validação de vocabulário, fact-check por amostra
e **cinco linhas sorteadas apresentadas ao humano** com a evidência ao lado.
Essa amostra não é opcional. É o único ponto em que alguém de fora olha o que foi
produzido — sem ela, quem classifica, valida e aprova é a mesma parte.

---

## Regras que só existem porque há escrita em disco

**Nunca leia, imprima ou copie `chave.txt`.** É a chave da YouTube Data API. Ela
já vazou uma vez neste projeto. Não precisa dela para classificar: o `coletar.py`
a lê sozinho. Se aparecer em algum output, avise e pare.

**Backup antes de gravar, sempre.**
```
copy playlist-historia-v2.xlsx backups\playlist-AAAA-MM-DD-HHMM.xlsx
```
Antes, a planilha antiga sobrevivia porque a nova chegava por download. Com
escrita direta isso acabou. Sem backup não há como o `verificar.py` conferir
linhas travadas, nem como voltar atrás.

**`verificar.py` é um portão, não um relatório.** Saiu 1, não salva. Ele checa
`video_id` único e preenchido, colisão com `descartados.txt`, campos
obrigatórios, link batendo com o id, `Século/Período` igual ao que a escada
calcula, ordenação, forma dos Extras, coerência confiança/status e linhas
travadas intactas.

**Apagar linha exige mandar o id para `descartados.txt`** no mesmo commit. Id
que some do catálogo sem ir para os descartados volta a ser coletado como novo.

**Não edite `catalogados.txt` à mão.** O `coletar.py` grava nele sozinho. É o que
permite a planilha local ficar desatualizada sem gerar recoleta silenciosa.

---

## O que decidir e o que não decidir

Decida quatro campos: `Ano`, `Região`, `Tema`, `Subtema`. Mês e dias só quando o
vídeo trata de período curto e determinado.

Não decida: `Século/Período` sai da escada da Lista A pelo ponto médio, nunca no
olho. `ano_inicio`/`ano_fim` saem do parser. `publicado`, `video_id` e `lote` vêm
do arquivo de lote.

**Termo novo:** um search rápido para conferir a forma padrão em português,
preencher a célula com a sugestão marcada `revisar`, seguir em frente. A lista
completa sai na parada do quarto lote — não pare a rodada por causa disso. Antes
de propor tema-raiz novo, procure sinônimos e traduções alternativas na Lista C
**inteira**, não só no ciclo em andamento: já houve duplicata dos dois jeitos.

**Só erro crítico interrompe.** A lista está no `protocolo.md`, seção "Rotina de
quatro lotes". Fora dela, acumula.

---

## Armadilhas com histórico neste projeto

Estão detalhadas no `protocolo.md`. As que mais reincidiram:

- **Descrição e tags recicladas entre episódios.** Canais repetem o mesmo bloco.
  Já apareceram tags de Vicksburg/1863 num vídeo de Atlanta/1864. **Capítulos
  ganham de tags e de descrição sempre que houver conflito.** Cuidado também com
  número real citado no bloco "Related Videos:", que descreve *outro* vídeo.
- **Desalinhamento de tupla ao montar linhas em lote.** Já custou 14 linhas sem
  `publicado`/`Título`, e mais 3 linhas apagadas durante a correção. Conte os
  campos de cada linha **antes** de montar a planilha, e confira o conjunto de
  ids contra o `lote-NN.md`.
- **Regex de data míope.** Já ignorou anos de três dígitos e `centuries` no
  plural. Todo padrão novo de data se testa contra a faixa inteira do catálogo,
  de 20000 a.C. a hoje (o limite mudou de 3300 a.C. na adoção do canal Ancient
  Americas, lote 77 — povoamento das Américas).
- **Frase evocativa não é data, e ponta de faixa não se estende por inferência**
  de gênero ou formato do episódio. Ache o evento real por trás da frase.
- **A fonte erra.** Quando o vídeo contradiz o fato conhecido, vale o fato, e a
  divergência vai para `notas`.

---

## Sem transcrições, sem contornos

Só a YouTube Data API oficial. Evidência = título, capítulos, descrição e tags.
Baixar legendas de terceiros exige OAuth do dono do vídeo; raspar o endpoint
interno viola os Termos de Serviço. Nunca usar cookies de conta logada nem proxy
para contornar bloqueio — troca um bloqueio de IP temporário por risco de
suspensão da conta.
