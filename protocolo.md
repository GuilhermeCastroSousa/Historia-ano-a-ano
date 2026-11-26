# Protocolo do catálogo de história

Manual de operação do projeto. Junto com `vocabulario-canonico.md`, é o que
garante que qualquer conversa nova classifique do mesmo jeito que a anterior.

---

## Duas camadas

**`playlist-historia-v2.xlsx` é o dado. `playlist-historia-v3.xlsx` é o
produto.** A v2 guarda uma linha por vídeo, ordenada por `ano_inicio`, com as
invariantes que o `verificar.py` confere. A v3 é **derivada** dela pelo
`ordenar.py` e ordenada para quem assiste em sequência. Nada se classifica na
v3; nada se lê da v3 para decidir dado.

O motivo da separação: as duas ordens são incompatíveis e as duas são certas. A
ordem por `ano_inicio` é correta como dado e ruim como playlist — os 27 vídeos
de Mesopotâmia Antiga aparecem em 16 trechos separados, porque uma faixa de
7000 a.C. a 1365 a.C. se intercala com Egito, Canaã e Grécia a cada degrau.
Quem assiste não consegue seguir. A ordem de exibição agrupa por civilização
enquanto as datas são largas e vira cronologia única quando ficam precisas.

| | v2 | v3 |
|---|---|---|
| papel | fonte de verdade | ordem de exibição |
| ordem | `ano_inicio`, `ano_fim`, `Mês`, `Dias` | `ordem`, derivada |
| período | Lista A (ponto médio) | Lista E (eras, pelo início) |
| portão | `verificar.py` | `portao()` do `ordenar.py` |
| quem escreve | `gravar.py` | `ordenar.py` |

O portão da v3 não repete as checagens da v2: confere que a derivação é fiel —
mesmos ids, datas intactas, `ordem` de 1 a n sem furo, `era`/`tipo`/
`regiao_historica` preenchidos. Se a derivação sujar dado da v2, ele recusa
gravar.

**A ordem da v3 nunca é escrita à mão.** É isso que faz vídeo novo de lote cair
no lugar certo sem ajuste manual, e é o que permite espelhar a playlist no
YouTube (`subir_playlist.py --na-ordem`). Ajuste manual na v3 é perdido na
próxima execução do `ordenar.py` — se uma linha ficou no lugar errado, o
conserto é na coluna que a põe lá (tema, região, tipo), não na posição.

O modelo de ordenação — eras, tipo, região histórica, a virada em 500 a.C. e o
passeio geográfico — está documentado nas Listas E, F e G do
`vocabulario-canonico.md` e no cabeçalho do `ordenar.py`. A aderência medida
contra a planilha ordenada à mão pelo humano (290 vídeos, até 500 a.C.) foi de
89% de acerto de era, 84% de região, concordância de pares de +0,643 e
sequência de blocos de +0,672. O `conferir_ordem.py` refaz essa medição.

## O que este sistema faz

Cataloga vídeos de história do YouTube em uma planilha ordenada cronologicamente
pelo período que o vídeo **trata**, não pela data em que foi publicado.

Fluxo de uma rodada:

1. `python coletar.py` — coleta um lote de vídeos novos e gera `lote-NN.md`
2. O `lote-NN.md` e a planilha são levados a uma conversa com o Claude
3. O Claude classifica e devolve a planilha atualizada
4. O humano corrige por amostragem, direto na planilha
5. Volta ao passo 1

---

## Arquivos e ordem de execução

| Arquivo | Papel |
|---|---|
| `playlist-historia-v2.xlsx` | Fonte de verdade. Nunca é regravada do zero. |
| `vocabulario-canonico.md` | Listas fechadas de período, região, tema e subtema. |
| `protocolo.md` | Este arquivo. |
| `coletar.py` | Coleta um lote. Roda a cada rodada. |
| `completar_datas.py` | Preenche datas de publicação faltantes. Roda uma vez. |
| `chave.txt` | Chave da YouTube Data API. Nunca vai para a conversa. |
| `descartados.txt` | Shorts já vistos e recusados. Cresce sozinho. |

---

## Regras de classificação

### O que o Claude decide

Apenas quatro campos: `Ano` (texto legível), `Região`, `Tema` e `Subtema`.
Mês e dias só quando o vídeo trata de um período curto e determinado.

### O que o Claude NÃO decide

- **`Século/Período`** é calculado pelo ponto médio entre `ano_inicio` e
  `ano_fim`, pela escada da Lista A. Nunca escolhido no olho.
- **`ano_inicio` / `ano_fim`** saem do parser de `Ano`, não da intuição.
- **`publicado`, `video_id`, `lote`** vêm do arquivo de lote.

### Vocabulário

Região, Tema e Subtema saem **das listas do `vocabulario-canonico.md`**.
Quando nada serve, o Claude propõe um termo novo ao fim da resposta, em uma
seção separada — nunca o insere calado na planilha. O termo só vira canônico
depois que o humano aprova por escrito.

### Confiança

| Valor | Quando usar |
|---|---|
| `alta` | Capítulos ou descrição trazem datas explícitas do assunto. |
| `média` | Datas inferidas do tema, ou evidência parcial/ambígua. |
| `chute` | Nenhuma data na evidência; a faixa veio do conhecimento geral. |
| `n/a` | Linha `Extra`: não há período a estimar. |

`status` é `revisar` sempre que a confiança for `média` ou `chute`, e também
quando o vídeo não for sobre um período histórico.

**Dúvida alta sobre uma data pede busca online antes de classificar.** Regra
geral, não só de um canal: quando a confiança na data depender de
conhecimento externo que o Claude não tem certeza (biografia de uma pessoa,
data de uma obra, cronologia de uma escola de pensamento), fazer uma busca
de contexto antes de gravar a linha, em vez de arriscar de memória.
Confirmado com o humano por causa do canal de filosofia (onde quase nenhum
vídeo narra data própria — a evidência é a ideia discutida, não um evento),
mas vale para qualquer canal.

### Conteúdo biográfico/conceitual sem evento datável

Canais que tratam de pensadores, obras e escolas de pensamento (filosofia,
mas também biografias em geral) raramente narram uma data própria. Duas
convenções fixadas com o humano em 08/08/2026, na adoção do primeiro canal
de filosofia:

- **Vídeo sobre um pensador específico, sem deixar claro se fala da vida
  inteira ou de uma obra/fase**: usar a vida inteira do pensador
  (nascimento–morte) como faixa padrão. Mesmo critério já usado no catálogo
  para dinastias/impérios inteiros (ex.: `Dinastia júlio-claudiana` cobre a
  dinastia toda, não só o evento em foco). Quando a evidência apontar
  claramente para uma obra ou fase específica, usar essa faixa mais estreita
  em vez da vida inteira.
- **Vídeo sobre um conceito ou escola que atravessa vários pensadores e
  séculos** (ex.: "O que é o Livre-Arbítrio?", citando Aristóteles a Kant):
  fica na **linha do tempo**, com a faixa do pensador mais antigo ao mais
  recente citado — mesmo que isso gere um rótulo `Panorama (X - Y)` muito
  largo pela escada da Lista A. Não vai para `Extra` só por ser uma faixa
  ampla; `Extra` continua reservado para quando não há como fixar nenhum
  período, não para quando o período é só impreciso.

### Linhas travadas

`travado = sim` marca trabalho humano. **Nunca sobrescrever** sem aprovação
escrita e explícita do humano para aquela célula. As linhas do lote 0 são todas
travadas. Quando o humano corrige uma linha, o Claude compara
a planilha recebida com a anterior, detecta as células alteradas e marca
`travado = sim` sozinho.

---

## Colunas

| Coluna | Quem preenche | Observação |
|---|---|---|
| Século/Período | calculado | ponto médio, pela Lista A |
| Ano | Claude | texto: `1942 - 1945`, `431 a.C. - 404 a.C.`, `*` |
| Mês / Dias | Claude | `8 - 9` e `02 - 09`; `*` quando não se aplica |
| Região | Claude | Lista B |
| Tema / Subtema | Claude | Lista C |
| Canal / Título / Link | coletor | |
| publicado | coletor | data no YouTube |
| ano_inicio / ano_fim | parser | inteiros; negativo = a.C. |
| video_id | coletor | chave de deduplicação; **nunca pode ficar vazio** |
| confianca / status | Claude | ver tabela acima |
| travado | processo | `sim` protege da sobrescrita |
| notas | Claude | por que a linha foi marcada |
| lote | coletor | `0` = catálogo manual anterior ao sistema |

Ordenação: por `ano_inicio`, depois `ano_fim`. Nunca pela coluna `Ano`, que é texto.

---

## Checklist de cada lote

Antes de devolver a planilha, conferir:

- [ ] nenhum `video_id` repetido, nenhum vazio
- [ ] `ano_inicio` em ordem crescente do começo ao fim
- [ ] toda linha nova com `lote` e `publicado` preenchidos
- [ ] nenhuma linha `travado = sim` alterada
- [ ] termos novos listados à parte, não inseridos em silêncio
- [ ] contagem de linhas = anterior + vídeos do lote

---

## Decisões já tomadas

- **Shorts não entram.** Duração mínima de 181 segundos, em `DURACAO_MINIMA`.
- **Exclusivos de membros não entram.** Títulos com "Member/Patron Exclusive"
  são descartados pelo `coletar.py` e vão para `descartados.txt`.
- **Transmissões ao vivo não entram.** Mesma regra dos Shorts. O teste é a parte
  `liveStreamingDetails` da API, que só vem preenchida para vídeo que foi (ou
  será) live. **Não usar `snippet.liveBroadcastContent`**: depois que a live
  termina ele volta para `none`, e toda live encerrada passaria como vídeo
  normal. Também não usar heurística de duração nem de título — no canal
  Thersites the Historian o padrão era "feat. [convidado]" em vídeos de 2 a 6
  horas, mas isso é coincidência do canal, não regra. Filtrado no
  `coletar.py`, dentro de `buscar_lote()`.
- **Extras.** Entra com `Século/Período = Extra`, `Ano/Mês/Dias = *`,
  `ano_inicio` e `ano_fim` **vazios**, `confianca = n/a`, `status = ok`,
  `travado = sim`. Vale por tema e subtema. Ordena no fim da planilha.
  **Só dois casos** (apertado na parada dos lotes 30-33): *recepção* — o assunto
  é o artefato moderno ou o método (filme, série, jogo, teoria conspiratória,
  guia de estudo) — e *atemporal* — atravessa milênios sem recorte datável.
  **Panorama não é mais Extra:** faixa larga entra na linha do tempo com rótulo
  `Panorama (X - Y)`. Ver "Extra virou balde", em Armadilhas conhecidas.
- **Aleatório.** Mesma forma do Extra (anos vazios, `confianca = n/a`,
  `status = ok`, `travado = sim`, ordena no fim), mas diz outra coisa: **não é
  história.** O canal publicou, o catálogo registra, e o vídeo não trata de
  período histórico nenhum — ficção de mundo inventado, cultura de internet.
  Criado ao adotar o canal Thersites the Historian (lote 40), que publica fora
  de história com frequência; a decisão do humano foi **todo vídeo do canal
  entra**, e o que não tiver contexto histórico entra como `Aleatório`.
  Diferença prática para o `Extra`: o Extra *é* história sem período fixável
  (recepção, assunto milenar); o Aleatório não é história. **Aleatório não
  recebe anos nem quando existe uma data** — "Mr. Hands, 1960-2005" tem data e
  mesmo assim é `Aleatório`, porque a linha do tempo significa "o período que o
  vídeo trata", e esse vídeo não trata de período histórico.
- **`Extra` e `Aleatório` são os dois únicos rótulos escolhidos a dedo.** Todo o
  resto da Lista A sai da escada. Ver `SEM_PERIODO`, no `verificar.py`: o portão
  pula a checagem da escada para esses dois e exige a forma de linha fora da
  linha do tempo.
- **Faixa de 300 anos ou mais não usa ponto médio.** O rótulo passa a ser a
  própria faixa, `Panorama (330 - 1453)`. Limiar em `LIMIAR_PANORAMA`, no
  `verificar.py`. Vale para toda linha larga, venha ela de onde vier.
- **Idade Média usa séculos**, não rótulos nomeados. `Early/High/Late Middle
  Ages` foram aposentados.
- **Rótulos grecorromanos na Lista A são intencionais.** `Século/Período` é régua
  cronológica para o leitor, não descrição do assunto. Um tema chinês ou da
  estepe pode cair em "Apogeu Romano" — isso é esperado. A interpretação
  histórica mora em `Tema` e `Região`. O degrau `Panorama` não abre exceção a
  isso: ele responde à largura da faixa, não à cultura do assunto.
- **Sem ano na evidência**: o Claude escolhe o período da Lista A e a linha vai
  para `chute` / `revisar`.
- **`NN00s`** (`800s`, `1900s`) vale como década, mas sempre com `revisar`.
- **Sem transcrições.** Não existe forma autorizada de baixar legendas de
  vídeos de terceiros: o endpoint oficial `captions.download` exige OAuth do
  dono do vídeo, e raspar o endpoint interno viola os Termos de Serviço do
  YouTube. O sistema usa só a API oficial. Evidência = título, capítulos,
  descrição e tags.
- **Nunca contornar bloqueio com cookies ou proxy.** Cookies de conta logada
  ligariam a conta Google à raspagem; proxy é evasão ativa. Ambos trocam um
  bloqueio de IP temporário por risco de suspensão de conta.

---

## Convenções de Região por tema

Decididas durante os lotes; valem para todos os lotes futuros.

- Império Otomano → `Turquia`
- Império Franco → `França`
- Guerra Russo-Ucraniana → `Rússia`, com o mês coberto no campo `Mês`
- Império Romano tratando de província específica → a província
  (ex.: Britânia → `Inglaterra`), não `Mediterrâneo`

---

## Rotina de quatro lotes

O ciclo padrão. Lotes 1 a 3 correm sem parada; o quarto fecha a rodada.

| Etapa | O que acontece |
|---|---|
| Lotes N, N+1, N+2 | Classificar e devolver. Termo novo entra preenchido, com `revisar` e nota. |
| Lote N+3 | Idem, e em seguida a **parada**: validação de vocabulário e fact-check dos quatro lotes. |

**Termo novo, no meio da rodada:** um search rápido para conferir a forma padrão em
português, preencher a célula com a sugestão marcada `revisar`, seguir em frente.
A lista completa sai só na parada.

**Só erro crítico interrompe a rodada.** A lista fechada:
`video_id` duplicado, vazio ou colidindo com `descartados.txt` · linha travada
alterada sem pedido · contagem de linhas que não fecha · link malformado ·
perda de dados na planilha · coleta silenciosamente errada. Fora disso, acumula.

**Na parada:** lista única de termos novos, sobreposições de vocabulário,
fact-check por amostra das datações de maior risco, e o bloco de estado.

## Dedup não depende mais da planilha

`catalogados.txt` é o ledger de ids já enviados para classificação. O `coletar.py`
grava nele ao fim de cada rodada e deduplica contra `catalogados.txt ∪
descartados.txt ∪ planilha`. A planilha continua sendo lida quando está presente,
mas uma cópia local desatualizada deixou de gerar recoleta silenciosa.

Se a planilha tiver ids que não estão no ledger, o script avisa e os registra.

## Passagem de bastão entre conversas

Cada rodada acontece numa conversa nova. Para manter a continuidade:

**Subir sempre:** a planilha atual e o `lote-NN.md` da rodada.
(`vocabulario-canonico.md` e `protocolo.md` já estão nos arquivos do projeto.)

**Se o humano editou a planilha à mão**, deve listar quais linhas mudou.
Sem a versão anterior do arquivo, o Claude não detecta a mudança e não
consegue marcar `travado = sim`. Alternativa: o humano marca `travado = sim`
ele mesmo nas linhas que corrigiu.

**Ao fim de cada conversa**, o Claude entrega um bloco de estado para o
humano colar na conversa seguinte: contagem de linhas por lote e por status,
decisões pendentes, bugs abertos e termos aguardando aprovação.

---

## Armadilhas conhecidas

**Estender a ponta de uma faixa por inferência de gênero/formato do
episódio, sem nenhuma palavra da evidência sustentando o novo limite.**
Achado na parada dos lotes 216-219 (canal ESOTERICA, comando `/rodada`): o
episódio final de uma série de 14 aulas sobre Cornélio Agripa se chamava
"Agrippa's Afterlife - Conclusions", e a faixa foi classificada como
`1535-1700` — a morte de Agripa (1535) até a recepção rosacruz do século
seguinte, que o catálogo já documentava para outros vídeos do mesmo canal.
O problema: nenhuma frase da descrição deste episódio específico menciona
esse século XVII. A extensão veio inteiramente do meu palpite sobre o que
"Afterlife/Conclusions" provavelmente cobriria, não de qualquer coisa que o
vídeo realmente disse. Corrigido na aprovação para `1535`, a morte de
Agripa — o único ano que a série (bloco reciclado, repetido nos 14
episódios) efetivamente ancora. Lição: quando a única pista é o *título* do
episódio dentro de uma série (não a descrição em si), a inferência sobre o
que ele cobre é ainda mais frágil que o normal — vale estreitar a faixa
para o que há de mais concreto (aqui, a morte do biografado), não esticar
para a interpretação mais abrangente do título.

**Falha silenciosa.** Já aconteceu duas vezes neste projeto: um link corrompido
que virou URL falsa, e transcrições que falhavam sem dizer por quê. Qualquer
`except` que devolva vazio sem registrar o motivo é bug esperando para
acontecer. Erro tem que aparecer.

**Regex míope de plural.** Mesma família do erro abaixo, outra faixa: o detector
ignorava "1st to 4th **centuries** CE" porque só aceitava `century` no singular.
Um vídeo inteiro sobre o mitraísmo caiu em "nenhuma data encontrada" tendo a
datação escrita na descrição. Corrigido para `centur(?:y|ies)`.

**Regex míope de era moderna.** O detector de datas já ignorou anos de três
dígitos ("772", "782") por só reconhecer 4 dígitos ou era explícita — a Alta
Idade Média inteira ficou no ponto cego, e a confiança era rebaixada sem
motivo. Corrigido. Lição: todo padrão de data deve ser testado contra a faixa
cronológica completa do catálogo, de 3300 a.C. a hoje, não só contra exemplos
modernos.

**Apagar linha some com o `video_id`.** A deduplicação usa os `video_id` da
planilha. Linha apagada é vídeo que volta a ser coletado como novo. Ao excluir
linhas, os ids precisam ir para `descartados.txt` — ou a exclusão tem que virar
regra no `coletar.py`, como foi feito com Shorts e exclusivos de membros.

**Teaser de vídeo exclusivo.** Um teaser de 5min de um documentário de 3h só para
membros passou pelos dois filtros: tinha mais de 181s e a palavra "exclusive"
estava na descrição, não no título. `RE_TEASER` agora barra teaser, trailer e
sneak peek pelo título. Material promocional não é catálogo.

**Tags recicladas de outro episódio.** Descoberta no lote 3. O vídeo sobre a
marcha de Sherman a Atlanta (1864) trazia o bloco inteiro de tags do episódio de
Vicksburg, ano "1863" incluído. A descrição mente com jeito de texto promocional;
as tags mentem com jeito de metadado, e por isso enganam mais. **Capítulos ganham
de tags sempre que houver conflito.**

**Descrição padrão da série engana.** Canais repetem o mesmo parágrafo em todos
os episódios de uma série. Dois vídeos da Guerra Civil Americana traziam
"1854-1861", "1859" e "abril de 1861" na descrição sem que o episódio tratasse
disso — era texto fixo da série. Data que aparece igual em vídeos diferentes do
mesmo tema é suspeita: confira contra os capítulos, que são específicos.

Segundo caso, lote 13: "Battle of Alexandria 30 BC - End of Antony and
Cleopatra" não tinha capítulos. A descrição dizia "in this episode we will
see... 41-40 BC as Octavian had to deal with... the Perusian War" — descrevendo
o episódio ANTERIOR da série (reciclada), não este. Sem capítulos para
desempatar, o título ("30 BC") é que estava certo. Quando não há capítulo, o
título entra como critério de desempate antes de aceitar a descrição.

Terceiro caso, confirmado na parada dos lotes 14-17: o mesmo parágrafo
("aftermath of the first phase of the Russian Invasion of Ukraine in 2022...
this video will focus on the events of August... this video will talk about
the events of the beginning of October...") apareceu **idêntico em pelo menos
5 episódios diferentes** da minissérie retrospectiva "Modern Warfare" sobre a
guerra da Ucrânia, publicados entre junho e agosto de 2023, cada um
supostamente sobre um mês distinto de 2022. Não é um caso isolado — é o modo
como o canal escreve a descrição de toda uma minissérie retrospectiva. Nessas
linhas, mantivemos o ano (razoavelmente estabelecido pelo arco narrativo) mas
recusamos travar em um mês específico sem capítulo datado que desempate.

**Rótulo de série não é o tema — vale o conteúdo.** Confirmado na parada dos
lotes 26-29: `JkyYjpYLORI` ("First Crusade: Battle of Manzikert 1071") usa o
nome da série do canal no título, mas Manzikert (1071) antecede a Primeira
Cruzada (1095) em 24 anos e é história bizantina, não das Cruzadas — o canal
chama de "First Crusade" toda a minissérie de contexto bizantino/seljúcida que
antecede a cruzada em si, não só os episódios da cruzada propriamente dita.
Classificado por engano em `Cruzadas > Primeira Cruzada` / `Oriente Médio` na
classificação original; corrigido na parada para `Império Bizantino` (sem
subtema) / `Turquia`, pelo conteúdo do vídeo, não pelo rótulo da série. Mesmo
princípio já usado sem estar nomeado como armadilha: o Prelúdio nº1 da Frente
Oriental (Segunda Guerra Mundial) foi classificado pelo conteúdo (Revolução
Russa), não pelo rótulo "Eastern Front Week-by-Week". Regra geral: quando o
título/série do canal e o conteúdo do vídeo apontam para temas diferentes, vale
o conteúdo — o nome da série é conveniência de playlist do canal, não
classificação histórica.

**Faixa fechada sobre capítulos truncados.** O `capitulos()` do `coletar.py`
captura no máximo 20 capítulos (`limite=20`). Documentários longos (2h-6h,
comuns nas séries "Full Story"/"Full History" do canal) podem ter dezenas de
capítulos reais; os que ficam de fora do limite não aparecem na evidência.
Caso do lote 16: "The Full History of the Peloponnesian War" tem quase 3h, mas
os capítulos capturados param em 411 a.C. (aos 2h06 de um vídeo de 2h55) — os
~49 minutos finais, que provavelmente cobrem 411-404 a.C. (o fim real da
guerra, com a queda de Atenas), não têm nenhuma evidência. O título "Full
History" não é evidência suficiente para fechar a faixa no fim histórico
canônico do assunto; sem capítulo ou descrição que cubra especificamente o
trecho final, a faixa tem que parar onde a evidência para. Corrigido na
parada dos lotes 14-17 (`Jr8EGJwDCk8`: `431 a.C. - 404 a.C.` virou
`431 a.C. - 411 a.C.`). Mesma lição vale para datas de publicação: um vídeo
publicado dias após o período que ele resume ("we conclude the events of
2023", publicado em 14/01/2024) não ganha o ano da publicação de graça —
`4bEGiozqiv8` teve a faixa `2023 - 2024` estreitada para `2023` pelo mesmo
motivo.

**Numeração de "temporada" do canal não é a numeração histórica.** O subtema
`Segunda Cruzada` do catálogo cobre vídeos de 1119 a 1149 — mas a Segunda
Cruzada histórica é só 1147-1149. O canal chama sua "segunda temporada" de
vídeos sobre Cruzadas (toda a história dos Estados Cruzados depois da
Primeira Cruzada) de "Second Crusade", e diz isso na própria descrição de
cada vídeo ("our series on the Second Crusade"). Vale o rótulo que o canal
usa na descrição do próprio vídeo, não o número do evento histórico real —
mas fique atento, porque os dois nem sempre coincidem.

**A fonte erra.** Um vídeo já narrou "meados do século I" sobre a Muralha de
Adriano, construída em 122. Quando o vídeo contradiz o fato conhecido, vale o
fato — e a divergência vai para `notas`.

**Vídeos com duas camadas de tempo.** Documentários sobre arqueologia falam do
sítio antigo e da escavação moderna. Vale o período do assunto, não o da
escavação, com nota registrando a escolha.

**Truncagem de capítulos pode ser resolvida por um vídeo de lote futuro — sem
reabrir a linha antiga.** Segundo caso do padrão "faixa fechada sobre capítulos
truncados" (ver acima): `FI4eNk69E8Q` ("Guadalcanal Campaign FULL DOCUMENTARY",
lote 18) teve a faixa fechada em `1942` porque os capítulos capturados (limite
de 20 do `coletar.py`) paravam em novembro, embora o título dissesse "FULL" e a
campanha histórica só termine em fevereiro de 1943 (Operação Ke). Dois lotes
depois, `D2Jw_AjaF94` ("End of the Guadalcanal Campaign", lote 20) apareceu
como vídeo próprio do canal cobrindo exatamente esse desfecho. A linha antiga
não foi reaberta nem sua faixa foi estendida — ela continua correta para o que
a EVIDÊNCIA DELA cobria no momento em que foi classificada. A resolução foi
cruzar as notas dos dois lados, deixando explícito que as duas faixas juntas
cobrem a campanha inteira sem se sobrepor, e que a causa da divisão foi o
limite de captura de capítulos, não um erro de leitura. Regra geral: se um
lote novo trouxer o "resto" de uma linha truncada de um lote antigo, não
reabra a linha antiga (a menos que a evidência dela estivesse simplesmente
errada) — documente a complementaridade nas notas dos dois lados. Resolvido na
parada dos lotes 18-21.

**Faixa `chute` que espreme vários processos distintos numa linha só.**
Descrição sem nenhuma data às vezes narra dois ou três eventos históricos
sequenciais no mesmo parágrafo (ex.: "This new video will describe the fall
of the Mongol rule over the lands of Ukraine, how the Polish-Lithuanian
Commonwealth took over and how these events led to the Rise of the
Cossacks... the Bogdan Khmelnytsky's rebellion" — `UQ_ocyTRRIE`, lote 24).
É tentador abrir uma faixa `ano_inicio`/`ano_fim` que cubra o primeiro ao
último desses eventos (nesse caso, quase 300 anos), mas isso mistura
processos que um leitor não reconheceria como "a mesma coisa". Antes de
espremer tudo numa faixa larga, considere: (1) o vídeo tem um evento
central que dá título/foco, mesmo que mencione contexto antes e depois? Se
sim, ancore nele. (2) Se não há foco único, registre a faixa larga mesmo
assim (não é erro), mas marque `chute` e deixe explícito na nota que a
faixa cobre múltiplos processos — não finja precisão que a evidência não
tem. Identificado na parada dos lotes 22-25; não resolvido retroativamente.

**Descrição reciclada nem sempre engana.** A regra "capítulos e título ganham
de descrição reciclada" (ver "Tags recicladas..." acima) parte do pressuposto
de que a recapitulação de uma série NÃO descreve o vídeo atual. Mas em pelo
menos dois casos dos lotes 20-21 (`bIO66-ZKNhQ` "Ottoman Expansion in
Anatolia" e `qBA-jdWQGJs` "Maritsa 1371") a recapitulação batia exatamente
com o conteúdo do próprio episódio — o título e a descrição descreviam o
mesmo evento, sem ambiguidade nenhuma. O teste não é "a descrição é uma
recapitulação?" (quase sempre é, nesses canais seriados), mas sim "essa
recapitulação está descrevendo ESTE vídeo ou outro (anterior/posterior)?".
Frases como "in this episode we will..." ou uma frase final que bate com o
título apontam para o vídeo atual; frases como "in our previous episode..."
ou uma lista de "próximos capítulos" apontam para outro. Resolvido na parada
dos lotes 18-21.

**Regex míope de século romano em inglês.** O `RE_DATA` reconhecia `século XI`
(português) e `11th century` (ordinal inglês), mas não `XI century`/`the XV
century` — a forma como o canal Kings and Generals escreve século em inglês
quando o algarismo é romano. Achado no lote 33 ("Turkification of Anatolia":
"started in the XI century... concluded by the XV century" sem nenhuma outra
data no bloco de evidência — a linha ficou sem nenhuma data própria detectada,
forçando confiança `alta` a se apoiar só em leitura humana da descrição, fora
do padrão automático). Corrigido com `\b[IVXLCDM]+\s+centur(?:y|ies)\b` — mas
com `(?-i:...)` para desligar `re.I` só nesse trecho, porque com case-insensitive
ligado palavras comuns como "mid", "did" e "civil" são compostas inteiramente
de letras romanas válidas (M/I/D/C/V) e bateriam "mid century" como data.
Testado contra a faixa cronológica completa antes de aceitar (regra do caso
"Regex míope de era moderna", acima). Corrigido na parada dos lotes 30-33;
linhas antigas não foram reabertas.

**Lives entraram por 17 lotes sem ninguém notar — 202 linhas.** Achado em
29/07/2026, por observação do humano ("muitos dos vídeos do novo canal são
lives"). O `coletar.py` filtrava Shorts, exclusivos de membros e teasers, mas
nunca tinha filtrado transmissão ao vivo — no Kings and Generals o problema não
existia, então a lacuna nunca apareceu. No Thersites the Historian, **46% do
que foi coletado era live**: 15 dos 25 do lote 40 e 187 dos 400 dos lotes 41-56.
Todas removidas, ids para `descartados.txt`, e o filtro entrou no `coletar.py`.

Três lições:

1. **Filtro de escopo é dependente de canal.** Trocar de canal não é só trocar
   uma constante: os filtros que bastavam para um podem deixar passar metade do
   outro. Ao adotar um canal novo, inspecione uma amostra crua antes de
   classificar 400 linhas.
2. **Teste autoritativo, não heurística.** Dava para "adivinhar" as lives pelo
   padrão "feat. [convidado]" e pela duração de 2-6h, e teria acertado neste
   caso — mas o certo é `liveStreamingDetails`, e a API respondeu 410 ids em 9
   chamadas. Quando existe campo autoritativo, não invente sinal indireto.
3. **Zerar célula não é apagar linha.** A primeira remoção zerou as células e
   deixou a dimensão gravada no `.xlsx` obsoleta. Em modo leitura-escrita o
   arquivo parecia certo; mas o `verificar.py` usa `read_only=True`, e nesse
   modo o `openpyxl` confia na dimensão do XML — resultado: 187 linhas fantasma
   e 2.245 falhas falsas. Use `delete_rows()`. E o portão, que morria com
   `TypeError` ao comparar com um backup contendo essas fantasmas, agora as
   filtra e avisa: **portão que quebra com traceback não é portão.**

**`Ano` e `ano_inicio`/`ano_fim` discordando em silêncio.** Achado na revisão
das 109 pendentes (28/07/2026). São o mesmo dado em duas formas — `Ano` é o
texto que o humano lê, os inteiros são o que ordena a planilha — e o
`verificar.py` nunca conferia um contra o outro. Havia **66 divergências**:

- **54 recém-criadas pela reclassificação dos Extras**, na mesma sessão: a faixa
  foi preenchida e o texto ficou `*`. A linha aparecia na linha do tempo e ao
  mesmo tempo dizia "sem período". Erro do Claude, não herdado.
- **10 divergências antigas**, cinco delas com assinatura clara de parse de
  década aplicado a um século (`Ano='1300 - 1400'` com faixa `1300..1360`).
- **2 textos que o parser nem lia** (`'1914 -1915'` sem espaço, `'1960s - 1998'`
  misturando década e ano).

Corrigidas todas, e o `verificar.py` ganhou `parse_ano()` mais a checagem
`Ano` × faixa, que falha tanto na divergência quanto no texto ilegível. Lição
mais ampla: **campo derivado que ninguém confere é campo que apodrece**. Quando
uma correção em lote mexer num dos dois lados, mexa nos dois — e prefira uma
checagem no portão a uma promessa de lembrar.

Registro à parte, sem correção: o campo `Ano` tem 34 linhas com formatação
divergente que o parser lê sem problema (travessão en/em-dash, `a.C` sem ponto
final, `d.C.` omitido no segundo termo de faixas que cruzam a era — este último
é a maioria, 35 de 40, e virou a convenção adotada). Cosmético, não corrigido.

**Extra virou balde: 54 vídeos datáveis fora da linha do tempo.** Achado na
parada dos lotes 30-33, a partir de uma suspeita do humano. Dos 68 `Extra` do
catálogo, **54 tinham período perfeitamente datável** — 79%. A prova não foi
interpretativa, foi de contradição interna: o mesmo gênero de vídeo, do mesmo
canal, sobre o mesmo assunto, recebeu tratamentos opostos. `Byzantine Navy:
Greek Fire, Tactics, Ships` virou Extra, enquanto `Eastern Roman Army: Tactics,
Structure, Weapons` recebeu `527-1453` com confiança `alta`. `How to Defend
Against the Mongols` virou Extra, enquanto os **nove** episódios regionais da
mesma série (China, Coreia, Índia, Europa, mamelucos, samurais…) receberam faixa
— a faixa do guarda-chuva era a união exata deles.

A causa não foi desleixo, foram duas coisas estruturais:

1. **`Extra` não é uma escolha, é derivado.** `periodo()` devolve `"Extra"`
   quando `ano_inicio`/`ano_fim` estão vazios. Ninguém "marca Extra" — deixa os
   anos em branco e o rótulo cai sozinho. Não havia decisão consciente a
   revisar.
2. **O ponto médio produzia rótulo ruim em faixa larga**, o que dava um
   incentivo real para deixar em branco. Isso já contaminava linhas **não**-Extra:
   `History of the Illyrians` (1000 a.C.–600 d.C.) estava rotulado "Apogeu da
   República". Corrigido com o degrau `Panorama` (ver `vocabulario-canonico.md`,
   Lista A).

Lição para as próximas paradas: **"panorama" e "sem período único" não são
motivo para Extra.** O teste é se o vídeo tem começo e fim no tempo, mesmo
distantes. Só é Extra o que fala da recepção moderna do passado (filme, série,
jogo, teoria conspiratória, método) ou o que atravessa milênios sem recorte.
E cuidado com a assimetria que criou o problema: **as 54 linhas foram
classificadas por quem também decidia se elas mereciam revisão** — Extra nasce
`travado = sim`, então nunca entravam na amostra de cinco linhas da parada.
Categoria que se auto-exclui da revisão cresce sem freio.

**Descrição inteira trocada entre dois vídeos do mesmo lote.** Achado no lote
38: `_qul4SpBjfI` ("Battle of Himera 480 BC - Greco-Carthaginian Sicilian
Wars") trouxe uma descrição inteiramente sobre a evolução do centurião romano
— idêntica, palavra por palavra, à descrição de `WJa5gm7Pkuw` ("Evolution of
the Roman Centurion"), o vídeo seguinte do mesmo lote. Diferente dos casos já
documentados de "descrição reciclada" (que reaproveitam um parágrafo fixo de
abertura de série, ou recapitulam o episódio errado da mesma série), aqui as
duas descrições são sobre **assuntos completamente sem relação** — não é
reciclagem de boilerplate, é uma troca de metadado entre dois vídeos
distintos. Sem capítulos para desempatar, a linha foi classificada só pelo
título (`Battle of Himera 480 BC`), com a descrição descartada por completo e
a confiança rebaixada para `média` (não `alta`) por depender só do título.
Lição: quando a descrição capturada não tem nenhuma relação temática com o
título — nem como recapitulação, nem como contexto — considere a possibilidade
de troca de metadado com outro vídeo do canal, não apenas reciclagem do mesmo
parágrafo.

**`travado='sim'` nascendo junto com a linha, antes do `/aprovar`.** Achado na
parada dos lotes 30-33: as 100 linhas dos quatro lotes já chegaram gravadas
com `travado='sim'` e `status='ok'` — inclusive as `chute`/`média` — mesmo
antes de qualquer humano revisar ou de `/aprovar` rodar uma vez sequer. Isso
não é erro de dado (as classificações em si seguiam corretas), é erro de
processo: o portão "confiança×status" do `verificar.py` (que deveria forçar
`status='revisar'` para toda linha `chute`/`média` sem uma trava humana
legítima) ficou decorativo, porque a única coisa que ele checa —
`travado != 'sim'` — já vinha satisfeita de fábrica. Por `protocolo.md`
("Linhas travadas"), só Extra nasce travada; qualquer outra linha só deveria
ganhar `travado='sim'` pelo `/aprovar` (passo 3) ou por correção humana
detectada num diff contra a versão anterior — nunca na própria gravação do
lote. `verificar.py` ganhou uma checagem nova: linha ausente da versão
`--anterior` (ou seja, nova) e não-Extra que já chega `travado='sim'` agora é
falha. Isso pega o problema na hora — no próprio `verificar.py --anterior
<backup>` de cada lote, antes da gravação — em vez de só na parada seguinte.
Não corrigido retroativamente nas linhas dos lotes 30-33 (já tinham conteúdo
correto; só o timing da trava estava errado, e reabrir teria disparado o
alarme de "linha travada alterada" para uma trava que nunca devia ter existido
naquele momento).

**`alta` inflada por título/tags, sem data própria na descrição ou nos
capítulos.** Achado na parada dos lotes 40-43 (canal Thersites the
Historian): 7 de 25 linhas `alta` do lote 40 tinham a nota "faixa explícita no
título" como única justificativa — nenhuma data numérica na descrição, e em
pelo menos dois casos (`AzwjEsVGKfM`, `Ky5w29lCPRs`) a própria nota já
confessava isso sem que ninguém rebaixasse a confiança. O canal escreve
títulos de prosopografia romana e de campanhas militares com datas exatas e
inequívocas ("Consul 52 and 69 CE", "June 25-July 1, 1862"), o que torna
tentador tratar o título como prova — mas título não é `capítulos` nem
`descrição`, as duas únicas fontes que a tabela de confiança do protocolo
aceita para `alta`. A regra fechada: **`alta` exige um número de ano dentro da
descrição ou dos capítulos do próprio vídeo; título e tags, mesmo quando dão
as duas pontas da faixa, no máximo sustentam `média`.** As 7 linhas foram
rebaixadas na aprovação dos lotes 40-43 (`verificar.py --anterior` não pega
isso sozinho — é checagem de leitura, não de estrutura de dado — por isso a
instrução do `/lote` passou a pedir a conferência linha a linha de toda
`alta` antes de cada resposta).

**`verificar.py` quebrava com traceback, em vez de reportar falha, quando
`lote` vinha vazio.** Achado na gravação do lote 48: um bug de off-by-one
num script de gravação apagou a última linha (`lote=None` entre outras
células limpas), e `python verificar.py --anterior` morreu com
`TypeError: '<' not supported between instances of 'NoneType' and 'int'` em
vez de reportar a falha normalmente. A causa: o resumo impresso em `main()`
faz `sorted(collections.Counter(r['lote'] for r in rows).items())` **antes**
do bloco `if falhas:` — e roda mesmo quando `lote` vazio já foi capturado
como falha em "campos obrigatórios" (`verificar()` faz seu trabalho direito;
é só o `print` de resumo do `main()` que não tinha proteção). Na hora, a
correção foi restaurar do backup sem tocar no script — o bug ficou latente
até a parada dos lotes 48-51 apontar que nunca tinha sido corrigido de fato.
Corrigido com uma chave de ordenação que isola `None` em vez de comparar com
inteiro: `sorted(lotes.items(), key=lambda kv: (kv[0] is None, kv[0]))`.
Testado numa planilha à parte com `lote=None` forçado numa linha: o resumo
agora mostra `None: 1` sem quebrar, seguido da falha normal
`'lote' vazio`, com `sys.exit(1)`. Lição: **qualquer `print`/agregação que
rode antes da checagem `if falhas:` precisa aguentar os mesmos dados sujos
que a própria checagem existe para pegar** — senão o portão vira uma
exceção não tratada bem no momento em que mais precisa aparecer como aviso
claro.

**Número real na evidência, mas irrelevante para o período do vídeo.**
Achado no lote 54 (canal Thersites the Historian): duas linhas tinham um
número explícito na descrição que passaria despercebido como data do assunto,
mas descrevia outra coisa. `R2ET6g5vdP0` ("Claudius: Legitimacy, Weakness...")
tem a descrição "This is a slightly modified version of an old historiographical
essay that I wrote for a class back in **2014**" — 2014 é a data em que o autor
*escreveu o ensaio*, não do reinado de Cláudio (41-54 d.C.), que é o assunto do
vídeo. `jhetL_BCx6w` ("Gerald R. Ford Presidential Deep Dive") tem "In **1980**,
he lost in the Republican primary to Reagan" — 1980 é um evento *pós-presidência*
(a derrota nas primárias), fora da faixa do próprio mandato (1974-1977), que é o
recorte declarado da linha. Nos dois casos, o número é genuíno e verificável,
só não ancora o período que a linha está declarando. Diferente da armadilha
"a fonte erra" (onde o número está errado) e da "descrição padrão da série
engana" (onde o número é de outro episódio) — aqui o número está certo e é do
mesmo vídeo, só descreve um evento diferente do recorte temporal da linha. A
checagem de confiança do `/lote` ("alguma data citada cai dentro da faixa
`ano_inicio..ano_fim` declarada?") pega isso, mas só se quem classifica conferir
a data contra a **faixa**, não só contra a existência de um número no texto.

**Descrição/tags reunidas (boilerplate) de um formato recorrente, não de um
episódio específico — inclusive títulos que escondem um call-in show.**
Achado nos lotes 53-55 (canal Thersites the Historian): vídeos de formatos
soltos ("Call-In Show", streams de perguntas, segmentos "10 or so historical
figures who have fallen through the cracks") repetem a mesma descrição
genérica e o mesmo bloco de tags em vários episódios sem relação de conteúdo
entre si — não é o caso já documentado de "descrição padrão de série" (que
recicla um parágrafo específico de uma minissérie datável), é um parágrafo
genérico reaproveitado para qualquer episódio daquele *formato*. O caso mais
enganoso: `Hq6d1PA9ZJ8`, intitulado "World War I: A General Overview", tem
descrição e tags **idênticas**, palavra por palavra, às de `HCDGMmOxOTY`
("2/21/2021 Call-In Show") do mesmo lote — "Call in and ask whatever question
you want", tags "call in/free form/Discord/any topic". Não é troca de
metadado entre dois vídeos distintos (armadilha já documentada) — é o mesmo
canal batizando um call-in show pelo assunto dominante da conversa daquele
dia, em vez de pela data, enquanto usa o boilerplate padrão de descrição/tags
do formato. Tratado como `Aleatório`/`Cultura de internet` pelo formato real
(confirmado pela descrição e tags idênticas a um call-in show inequívoco do
mesmo lote), não pelo título. Lição: quando a descrição de um vídeo bate
palavra por palavra com a de outro do mesmo lote, mas o **título** diverge,
desconfiar de qual dos dois títulos é o enganoso — não presumir que é sempre
o mais genérico.

**A checagem de `alta` fechada na parada 40-43 não se aplica sozinha —
precisa ser reaplicada em toda parada, sobre a janela inteira, não só sobre
o que a sessão atual classificou.** Achado na parada dos lotes 56-59: ao
reauditar TODAS as linhas `alta` dos quatro lotes (não só as que esta sessão
classificou), apareceram 3 violações num lote (57) classificado numa sessão
anterior — `Es60Jsb5AhM` (Andronicus Ducas, 904-906 CE) e `JuuJueRCr5Y`
(Himerius, 906-912 CE), com faixa inteira só no título e nenhum número na
descrição; e `U66rqgMsbfU` (Samuel J. Tilden, 1876), com o ano só no título
e nas tags. Uma quarta (`-d2DITW2uCs`, Metellus Numidicus) já tinha `datas
citadas: nenhuma encontrada` na extração automática do lote, mas foi
classificada `alta` mesmo assim, apoiada numa década em prosa da descrição
("the 100's and 90's") em vez de um número que ancorasse a faixa declarada
(109-102 a.C.). A regra em si (protocolo já fechado) estava certa; o que
faltou foi aplicá-la de volta sobre linhas que já existiam antes de ela ser
escrita. Lição: a checagem "toda linha `alta`, alguma data na descrição ou
capítulos cai dentro da faixa declarada?" não é só para o lote que acabou de
ser classificado — toda parada de quatro lotes precisa rodá-la contra as
`alta` da janela inteira, porque uma sessão nova não tem como saber se a
sessão anterior aplicou a regra direito.

**Moldura convencional do próprio vídeo pode encurtar uma faixa `chute` sem
que ninguém perceba.** Achado no fact-check da parada dos lotes 60-63: Egina
(`5L6Ow0kgLw4`) tinha `Ano = '800 a.C. - 480 a.C.'`, ancorado no fato de a
descrição do vídeo se autodescrever como sendo sobre o "Archaic period" e
citar a Batalha de Salamina (480 a.C.) como ponto alto. Busca externa mostrou
que a rivalidade naval de Egina com Atenas — o assunto central da descrição
("primarily known as an antagonist of democratic Athens") — só termina de
fato com a expulsão da população aeginetana em 431 a.C., quase 50 anos
depois do corte que eu tinha usado. Diferente de "a fonte erra" (onde um
número citado está errado) e de "faixa chute que espreme vários processos"
(onde o problema é largura demais): aqui a faixa ficou **curta demais**
porque copiei o rótulo de período que o próprio vídeo usa para se descrever
("Archaic period") sem checar se o processo histórico que ele narra
(a rivalidade com Atenas) continua além desse rótulo. Corrigido para
`800 a.C. - 431 a.C.` na aprovação. Lição: quando uma linha `chute`/`média`
se apoia num rótulo de período generico da própria evidência (era, século,
"Archaic period"), o fact-check da parada deve testar se o **assunto real**
do vídeo (não o rótulo) vai além desse recorte, não só se o rótulo em si
está certo.

**Corrigir uma linha travada com aprovação humana explícita esbarra no
mesmo portão que bloqueia correção não autorizada — o `verificar.py` não
distingue as duas.** Achado na aprovação dos lotes 60-63: o humano aprovou
por escrito adicionar o subtema `Guerra Jugurtina` à linha travada
`-d2DITW2uCs` (Metellus Numidicus, lote 57). Rodar `verificar.py --anterior
<backup-de-antes-da-correção>` depois dessa edição reporta a falha padrão
"linhas TRAVADAS alteradas: -d2DITW2uCs (Subtema, notas)" — o script não tem
como saber que essa mudança específica foi autorizada, porque ele só compara
valores, não motivos. Isso já tinha acontecido antes (`Sula`, `Guerras da
Chechênia`, ambos em "Sobreposições ainda por resolver" do
`vocabulario-canonico.md`) e nos dois casos a correção **não foi aplicada**
— ficou registrada como pendente para sempre, porque ninguém queria salvar
com o portão vermelho. Desta vez a correção foi aplicada mesmo assim, depois
de uma checagem manual extra: comparar a planilha nova com o backup e
confirmar que **a única linha travada com qualquer diferença é exatamente a
autorizada, e só nas células que deveriam mudar** (aqui, `Subtema` e
`notas`; nunca `ano_inicio`/`ano_fim`/`Ano`/etc. sem que isso também tivesse
sido pedido). Só depois dessa confirmação manual o resultado do
`verificar.py` foi tratado como falso-positivo esperado, não como motivo
para restaurar o backup. Lição: **o gate não tem um mecanismo de exceção
para correção autorizada de linha travada — quem aplica a correção precisa
fazer a checagem "só essa linha, só essas células" na mão antes de aceitar
o resultado do portão como aviso e não como bloqueio.** Sem essa checagem
manual, é mais seguro seguir o padrão antigo (registrar como pendente, não
editar).

**A checagem "só essas linhas, só essas células" agora é um script:
`conferir_travadas.py`.** Recebe o backup de antes da edição e um arquivo com
um `video_id` por linha — o conjunto autorizado — e compara a planilha nova
com o backup célula por célula, em *todas* as linhas, travadas ou não. Sai 0
só se as três coisas valerem ao mesmo tempo: nenhuma linha fora do conjunto
mudou, nenhuma linha do conjunto deixou de mudar, e nenhuma mudança caiu em
coluna que não devia mudar (as permitidas vêm na linha de comando). Ele nasceu
em 26/11/2026, na aplicação das camadas A1 e R da proposta de fusão de temas,
que mexeu em 155 linhas de uma vez — a maioria travada de ciclos antigos. Com
esse volume a checagem na mão deixa de ser viável, e sem ela a autorização por
escrito não vale nada na prática, porque ninguém consegue conferir que o que
mudou é só o autorizado. **Rodar o `conferir_travadas.py` não substitui a
autorização**; ele confere que a edição ficou dentro dela.

**Nota da linha promete um subtema que a célula não tem.** Achado na parada
dos lotes 64-67: `Sibyrtios` (`zOX04aIJm2g`, lote 64) tinha uma nota dizendo
que essa linha "fecha o trio" do subtema `Segunda Guerra dos Sucessores`
junto com Teutamos e Eudamos — mas o campo `Subtema` da própria linha estava
vazio. As outras duas linhas do "trio" tinham recebido o subtema
corretamente; só esta ficou de fora, provavelmente por desalinhamento entre
escrever a nota (que já tinha o raciocínio certo) e escrever a célula
(esquecida). O `verificar.py` não pega esse tipo de erro porque não lê o
texto livre de `notas` para conferir contra o resto da linha — é uma
inconsistência semântica, não estrutural. Só foi achado porque a parada
releu as notas das linhas novas em busca de fact-check e a incoerência saltou
aos olhos. Lição: ao criar um subtema novo que se aplica a mais de uma linha
do mesmo lote, conferir ao final que **todas** as linhas mencionadas na nota
de qualquer uma delas realmente têm o valor preenchido — não só confiar que
escrever a nota certa implica ter preenchido a célula certa.

**"Rótulo genérico do ciclo" não é o mesmo que "número que ancora um evento
datado" — mesmo quando os dois são um número real na descrição.** Achado na
parada dos lotes 64-67, ao reauditar a linha `alta` mais antiga do canal
Thersites the Historian: `X0ROqOQxlFw` ("Super Tuesday Predictions", lote
60) tinha `alta` apoiada em "2020" citado na descrição ("the various races
and candidates in the 2020 field"). Isso tecnicamente satisfaz a regra
literal ("alguma data citada cai dentro da faixa declarada"), mas é
qualitativamente diferente de "1863" para Sherman ou "917" para Leo Phocas
— aqueles números narram um evento específico que aconteceu naquele ano;
"2020" ali só rotula genericamente o ciclo eleitoral que o vídeo já
anunciava no próprio título. A partir do lote 67 esse critério mais
rigoroso já vinha sendo aplicado sem estar escrito (Howard Schultz, Andrew
Cuomo — "2020" em rótulo de ciclo, mantidos `média`), mas a linha do lote 60
não tinha sido revisitada. Corrigida (rebaixada para `média`) na aprovação
dos lotes 64-67, com aprovação explícita do humano. Lição: a checagem de
`alta` do `/lote` ("existe um número que cai na faixa?") precisa de um
critério mais fino — **o número narra um evento, ou só rotula o assunto que
o título já nomeia?** Só o primeiro caso sustenta `alta`.

**Nome de tema novo parecido demais com um existente de tratamento oposto
convida confusão futura.** Achado na parada dos lotes 68-71: `Jogos retrô`
(16 vídeos, playthroughs/let's-play, `Aleatório`) foi criado três lotes
depois de `História dos videogames` (1 vídeo, retrospectiva histórica real
do console, entra na linha do tempo) ter sido recriado — os dois nomes
começam com "jogos"/"videogames" e tratam do mesmo domínio de assunto
(jogos eletrônicos), mas um é entretenimento puro e o outro é história real
do hardware. Não houve erro de classificação (cada vídeo foi lido e
decidido pelo conteúdo, não pelo nome do tema), mas o par de nomes é uma
armadilha esperando para acontecer numa sessão futura que não abrir o
vocabulário inteiro antes de nomear um tema novo. Lição: ao propor um tema
novo, checar não só se o **conteúdo** já tem um tema (regra já seguida),
mas também se o **nome** que você está prestes a escrever já existe para
algo com tratamento diferente — nomes parecidos por si só já merecem uma
nota no vocabulário, mesmo que a classificação de cada linha esteja
correta.

**Tema novo pode se sobrepor a um tema criado numa parada anterior, não só
ao que a sessão atual já classificou.** Achado na parada dos lotes 72-75:
`França Medieval` (novo, lote 72, 814-1328) cobre praticamente o mesmo
processo histórico que `Formação das Monarquias Nacionais` (criado na
parada anterior, lote 71, 1066-1453, França e Inglaterra) — as duas faixas
se sobrepõem em 1066-1328. O problema não foi falta de checagem: a sessão
que criou `França Medieva` checou o vocabulário vigente e não achou nada
parecido, porque `Formação das Monarquias Nacionais` só existia como uma
linha nova daquele MESMO ciclo de quatro lotes ainda não fechado pela
parada — ou seja, o tema já existia no catálogo, mas a checagem mental de
"isso já existe?" tende a focar no vocabulário já consolidado (a Lista C
regenerada na última parada), não nas linhas novas que outra sessão gravou
no ciclo em andamento. Lição: antes de propor um tema novo, vale checar não
só a Lista C do `vocabulario-canonico.md` (que só é regenerada nas
paradas), mas também os temas usados nos lotes do ciclo corrente ainda não
aprovados — um `grep` pelo nome do assunto na planilha atual, não só no
vocabulário.

**Fontes de conhecimento geral discordam entre si mais do que parece — "a
data mais citada" não é sempre a mais correta.** Achado na parada dos lotes
76-78 (canal Ancient Americas, primeiro num domínio — arqueologia
pré-colombiana — sem nenhum vídeo prévio no catálogo, logo sem histórico de
acerto/erro para calibrar a busca). Ao classificar `chute` sem nenhuma data
na evidência, a busca externa vira a única base — mas para culturas menos
documentadas em português/inglês popular, resultados de busca sobre a mesma
pergunta trazem faixas visivelmente diferentes: a fundação de Tiwanaku
apareceu como "~180 d.C." (datação bayesiana por radiocarbono, a mais
recente), "~110 d.C." (Período Formativo Tardio) e "~300 a.C." (assentamento
inicial) na mesma rodada de busca — usei 300, o extremo mais antigo e menos
sustentado, sem perceber a divergência na hora de classificar. Corrigido
para 200 só na parada seguinte, ao refazer a busca especificamente para
fact-check. Mesmo padrão, risco menor, na Cultura do Cobre Antigo (usei
4000 a.C., quando 3000 a.C. é a faixa mais citada na literatura). Lição:
quando uma primeira busca ao classificar já mostra números discordantes
entre si (não só arredondamentos — divergências de séculos), tratar como
sinal de alerta na hora, não só na parada: preferir a fonte com metodologia
mais recente/explícita (datação bayesiana, radiocarbono, arqueologia
publicada) sobre o número que aparece com mais frequência em texto de
divulgação, e registrar a incerteza na nota mesmo que a linha já vá como
`chute`. Domínio novo para o catálogo = risco maior de precisar dessa
segunda passada.

**Nome de governante no título do vídeo pode ser metonímia para o
sistema/era inteira, não o reinado pessoal — faixa fica curta demais sem
ninguém perceber.** Achado na parada dos lotes 79-82 (canal Historia
Civilis): `Bureaucracy in Cleopatra's Egypt` foi classificado com a faixa
do reinado pessoal de Cleopatra VII (51-30 a.C.), lendo o título ao pé da
letra. Fact-check na parada (resumo do próprio episódio) mostrou que o
vídeo é sobre o sistema burocrático/monetário ptolomaico "no primeiro
século antes de Cristo" de forma geral — "Cleopatra's Egypt" é uma
metonímia popular em inglês para o Egito ptolomaico tardio, não um recorte
estrito do governo dela. Corrigido para `100 a.C. - 30 a.C.` (o século
inteiro). Diferente do caso Egina ("Moldura convencional do próprio vídeo
pode encurtar uma faixa `chute`", acima), onde o rótulo enganoso vinha da
própria descrição do vídeo (um período histórico genérico, "Archaic
period"): aqui o rótulo enganoso é o nome de uma pessoa famosa usado como
atalho popular para todo um sistema/época, e o efeito é o mesmo — faixa
`chute` fechada curta demais porque quem classifica não testou se o
assunto real do vídeo vai além do que o título parece dizer literalmente.
Lição: quando o título de um vídeo institucional/temático usa o nome de um
governante famoso (não um evento datado), perguntar se é o reinado dele
ou o sistema/era que ele representa popularmente antes de fechar a faixa
pelo reinado sozinho.

**Fato confirmado por busca externa pode vir com uma lenda moderna
grudada — separar os dois antes de escrever a nota.** Achado na parada dos
lotes 79-82: a nota original da `Lupercalia` (canal Historia Civilis)
dizia que o festival foi abolido por uma carta do Papa Gelásio I em 494
d.C. (correto) e que ele foi "convertido" no que seria o Dia dos Namorados
ou a Candelária (incorreto — busca externa mostra que essa ligação é
folclore moderno amplamente repetido, sem base documental contemporânea).
O erro não veio de inventar uma data, veio de aceitar uma alegação popular
que sempre acompanha o fato real em fontes de divulgação (History.com,
blogs de paganismo) sem separar "o que é atestado por fonte antiga" de "o
que é lenda moderna recontada com confiança". Corrigido removendo a
alegação da nota, mantendo só o fato verificado. Lição: ao fazer
fact-check de um fato histórico via busca, checar se cada afirmação da
resposta tem a mesma qualidade de fonte — um resumo de busca pode
misturar fato atestado e mito popular na mesma frase, com o mesmo tom de
certeza.

**Chave de ordenação de um script de gravação em lote precisa incluir
`Mês`/`Dias`, não só `ano_inicio`/`ano_fim` — senão uma linha nova pode
ficar fora de ordem contra uma linha antiga do mesmo ano.** Achado ao
gravar o lote 81: o script de gravação ordenava as ~1850 linhas só por
`(ano_inicio, ano_fim)`, mas o `verificar.py` desempata também por
`Mês`/`Dias` (`chave = (ano_inicio, ano_fim, num(Mês), num(Dias))`). A
nova linha de Cannae do Historia Civilis (`Mês=Dias='*'`, ou seja `0,0`)
tem o mesmo `ano_inicio`/`ano_fim` que uma linha já existente do Kings and
Generals sobre a mesma batalha, mas com mês/dia reais (`Mês=8, Dias=02`,
ou seja `8,2`) — a chave completa da linha antiga é maior que a da nova,
então a nova precisava vir *antes*, não depois. O portão pegou o erro
antes da gravação ser aceita (`fora de ordem: gObVeaEzklM antes de
MroGPObEZzk`) e a correção foi reordenar a planilha inteira com a mesma
chave exata do `verificar.py`, sem alterar nenhum valor de célula — mesmo
padrão de "portão que pega o erro na hora, não só na parada seguinte" já
visto para o caso de `travado='sim'` nascendo cedo demais. Lição: todo
script que grava lote novo tem que ordenar pela chave *completa* que o
`verificar.py` usa (`ano_inicio`, `ano_fim`, `Mês`, `Dias`), não só pelos
dois primeiros campos — o risco só aparece quando duas linhas de canais
diferentes cobrem exatamente o mesmo ano com granularidade de data
diferente, o que não é raro em catálogos com múltiplos canais sobre os
mesmos eventos famosos (Cannae, Zama, Teutoburgo já se repetiram entre
Kings and Generals e Historia Civilis neste mesmo ciclo).

**Reincidência da lição acima, forma mais simples: apensar linhas novas
no fim da planilha sem ordenar nada.** Achado ao gravar o lote 85 (canal
"The History of Rome", primeira coleta por playlist explícita — sem
script padrão para esse modo, então a gravação foi um script avulso
escrito na hora). O script escreveu as 25 linhas novas nas primeiras
linhas livres no fim da planilha e chamou `verificar.py` direto, sem
reordenar — o portão pegou (`fora de ordem: -5sZkJpCGH0 antes de
ItwGz43a_ak`) antes de qualquer coisa ser aceita. A causa não foi um
desempate sutil de `Mês`/`Dias` como no lote 81, foi mais básica: nenhuma
ordenação nenhuma, só apêndice cego. Lição reforçada: **todo script de
gravação em lote — inclusive um script avulso escrito na hora para um
modo de coleta novo — reordena a planilha inteira pela chave completa
antes de chamar `verificar.py`, sem exceção.** Escrever a lógica de
`periodo()`/ordenação do zero a cada vez é como esse tipo de erro volta;
vale considerar extrair um módulo compartilhado se aparecer uma terceira
vez.

**Regex míope de duração por extenso: "for two centuries" e "over 200
years" não batiam com nada.** Achado ao adotar o canal Cambrian Chronicles
(lote 83, primeiro lote): a descrição de "The Royal Title that No One Can
Remember" dizia "given to kings... for two centuries... before
vanishing" e "hasn't been figured out in over 200 years" — duas
afirmações de data em prosa, sem nenhum outro número na evidência — mas o
`RE_DATA` do `coletar.py` devolveu "nenhuma encontrada". Mesma família dos
casos já corrigidos (`centur(?:y|ies)` no plural, século romano em
inglês), mas duas lacunas novas: (1) contagem de século por extenso ("two
centuries", não "2 centuries" nem ordinal "2nd century"); (2) duração em
anos sem ser ano absoluto ("over 200 years", diferente de "in 782" ou
"772-804", que já eram cobertos). Corrigido com dois padrões novos:
`\b(?:one|two|...|ten)\s+centur(?:y|ies)\b` e `\b(?:over|more than|nearly|
almost|about)\s+\d{2,4}\s+years?\b`. Testado contra as duas frases reais
antes de aceitar (regra do caso "regex míope de era moderna"). A linha em
si foi classificada corretamente mesmo com a falha (o texto da descrição
já tinha sido lido por inteiro, não só o resumo de "datas citadas"), mas o
resumo automático ficou incorreto até a correção. Lição: descrição em
prosa livre tem muito mais formas de dizer "durante X tempo" do que o
regex prevê — quando um canal novo escreve descrições longas e
narrativas (não boilerplate), vale reler o texto completo, não só a lista
de "datas citadas" extraída, porque o extrator vai continuar tendo pontos
cegos.

**Vídeo cujo título promete um mistério "medieval" pode ser, na
verdade, sobre um evento real e bem datado do século XIX — o mito está no
enquadramento, não no fato.** Achado no mesmo lote 83: "The Mystery of
the Missing Medieval Sea" (Cambrian Chronicles) tem "medieval" no próprio
enquadramento do canal, mas o conteúdo real — confirmado por busca
externa — é sobre o aterro de William Madocks (The Cob), obra de
engenharia de 1808-1811 que drenou um estuário. Não há nada medieval no
fato: o título usa "mystery"/"medieval" como gancho narrativo do formato
do canal (ver também "Wikipedia's Missing Kingdom" e os outros vídeos de
"mistério" do mesmo lote, que têm o mesmo padrão retórico). Diferente do
caso "nome de governante como metonímia" (Historia Civilis, `Bureaucracy
in Cleopatra's Egypt`): ali o problema era estreitar demais a faixa; aqui
o risco é o oposto — aceitar o rótulo "medieval" do título e datar errado
por *séculos*, quando a evidência (nomes próprios, projetos datáveis)
aponta para outra época inteira. Lição: em canais de formato
"mistério/desmascaramento", o título é ativamente enganoso por design —
tratar como pista de gênero (o video vai contestar uma crença), nunca
como pista de período.

**`coletar.py` quebrava com `UnicodeEncodeError` ao imprimir um título
que o console do Windows não sabe representar — falha de exibição, não
de dado.** Achado ao coletar o lote 85 (tentativa) do canal Cambrian
Chronicles: o console abre em cp1252 por padrão no Windows, e um título
de vídeo genuíno (`Ỽ?`, sobre uma letra galesa obsoleta — não era
corrupção, o canal realmente se chama assim) tem caractere fora dessa
página de código. O script morreu no meio do `print` de progresso, antes
de gravar `lote-NN.md`, `catalogados.txt` ou `canais.json` — nada
persistiu, então não houve dado sujo para limpar, mas a coleta inteira
travou até a correção. O arquivo `lote-NN.md` já abre com
`encoding="utf-8"` explícito (nunca teve esse problema); só a exibição no
terminal quebrava. Corrigido reconfigurando `sys.stdout`/`sys.stderr` para
UTF-8 com `errors="replace"` logo no topo do script, antes de qualquer
`print`. Lição: em canal com título fora do inglês/latim básico (acentos
incomuns, alfabetos históricos, emoji), a exibição no console é um ponto
de falha tão real quanto o parser de datas — e como só derruba o processo
sem nunca gravar nada, é mais fácil de notar (o script simplesmente para)
do que de diagnosticar à primeira vista (o traceback aponta para
`encodings/cp1252.py`, não para o código do projeto).

**Um canal pode subir dois vídeos diferentes com o mesmo número e título
de episódio — não é bug de deduplicação, é o canal mesmo.** Achado nos
lotes 95-99 (The History of Byzantium Podcast): quatro pares de vídeos
("Episode 168 - A Guided Tour", "Episode 125 - A Tsar is Born",
"Episode 109 - Leo the Wise?", "John Chrysostom Part 1") apareceram duas
vezes cada, em lotes diferentes, com `video_id` e descrição diferentes
mas o mesmo número/título. A dedup do `coletar.py` é por `video_id`
(único no YouTube inteiro), então os dois passaram — corretamente: são
dois uploads reais e distintos, não o mesmo vídeo coletado duas vezes.
Nos casos observados até agora, uma versão tinha descrição rica com
data e a outra não (ou as duas tinham conteúdo diferente sob o mesmo
título) — cada uma foi classificada pela própria evidência, sem herdar
a data da outra. Lição: "mesmo número de episódio" não é sinal de "já
catalogado" — só `video_id` é. Se o número/título bater com algo já na
planilha, checar o `video_id` antes de supor duplicata.

**Faixa de instituição inteira montada de memória, sem nenhuma busca no
momento da classificação, erra mais do que parece — e só aparece na
parada.** Achado na parada dos lotes 103-106 (canal SandRhoman History):
duas linhas `chute` tiveram a faixa inteira decidida de memória, sem busca
alguma na hora de classificar (diferente do caso já documentado "Fontes de
conhecimento geral discordam entre si", onde uma busca acontecia mas o
resultado escolhido entre vários discordantes era o errado). A Guarda
Varegue (`7BlRu7lkVpM`) foi datada `988-1204` (fundação sob Basílio II até a
Quarta Cruzada) — busca feita só na parada mostrou que a fonte mais
consistente aponta continuidade até a queda de Constantinopla em 1453, e que
1204 vinha de uma única fonte isolada. A Companhia Alemã de Werner de
Urslingen (`_cdWg7biGxo`) foi datada `1338-1354` — busca na parada mostrou
que a companhia foi fundada e dissolvida no mesmo ano (1342), com Werner
voltando à Itália só em 1347 para outra campanha; a faixa "de memória" nem
acertava a década certa. Terceiro caso, mais leve: a White Company
(`D8-KzkExE-s`) foi datada a partir de 1360, mas a companhia só entrou na
Itália em 1361 — 1360 é o ano do Tratado de Brétigny (a causa do
desemprego dos mercenários), não o ano da travessia; erro de um ano só,
mas do mesmo tipo. Lição: quando uma linha `chute` fecha uma faixa de
instituição (não de evento) inteiramente de memória — sem nenhum número na
evidência do vídeo —, vale rodar uma busca rápida já na hora de classificar,
não só guardar para o fact-check da parada; datas de fundação/dissolução de
companhias mercenárias e guardas de elite são especialmente propensas a
confusão com datas adjacentes (ano do contexto que libera os mercenários,
ano de uma campanha posterior do mesmo líder, etc.). Corrigido na aprovação
dos lotes 103-106; as três linhas já estavam travadas — a correção rodou
antes da trava, não depois (protocolo.md, "Linhas travadas": nunca
sobrescrever linha travada sem aprovação explícita).

**Vídeo sem nenhuma evidência própria, mas parte de um par/série com um
vídeo irmão que tem evidência, tenta a mão de copiar a faixa do irmão.**
Achado no lote 112 (canal The Shogunate): `JqkG_hxQLhQ` ("Top 5 Greatest
Samurai Last Stands") não tem nenhuma data nem batalha nomeada na evidência
(capítulos só dizem "Number 5"..."Number 1"), mas o vídeo seguinte do mesmo
lote, `xixZuVkkVQU` ("More Epic Samurai Last Stands"), é uma continuação
explícita ("This is a direct follow up to my previous video...") e cita
batalhas reais e datáveis nos capítulos (Kawanakajima 1561, Shiroyama 1877).
A faixa do irmão foi copiada para a linha sem evidência, com nota registrando
a suposição — diferente da armadilha já documentada "Descrição inteira
trocada entre dois vídeos do mesmo lote" (onde o erro é aceitar metadado
errado sem perceber a troca): aqui a cópia foi deliberada e registrada, não
um engano. Ainda assim é uma faixa inventada, não extraída — o risco é essa
mesma prática acontecer futuramente **sem** a nota explícita, virando uma
faixa `alta`/`média` disfarçada de bem embasada. Lição: quando não houver
nenhuma data própria e a única base for "o vídeo irmão trata do mesmo
assunto", a linha nunca passa de `chute`, a nota tem que dizer explicitamente
que a faixa foi herdada (não justificada por evidência própria), e o caso
vale marcação extra de atenção na parada seguinte — não é o mesmo grau de
certeza que uma linha `chute` apoiada em conhecimento geral do próprio
assunto do vídeo.

**"Vídeo de discussão/debate" não decide sozinho entre linha do tempo e
Extra — o teste é se há um evento datado específico sendo debatido.**
Achado na parada dos lotes 113-116 (canal The Shogunate): o canal produz
vários vídeos que o próprio autor chama de "discussion video" ou que têm
formato de debate, mas eles se dividem em dois grupos bem diferentes.
`Did Oda Nobunaga Really Influence Samurai Warfare at Nagashino? - A
Discussion` (lote 116) debate quem merece crédito por uma inovação tática
numa batalha específica e datada (Nagashino, 1575) — foi para a linha do
tempo, no subtema já existente da própria batalha. Já `When did the Sengoku
Jidai REALLY Start (and End)?` (lote 115) e `The Problem With "Feudal"
Japan` (lote 114) são debates metodológicos amplos — o primeiro sobre qual
data inicial/final do período é a correta, o segundo sobre se o termo
"feudalismo" cabe no Japão — sem nenhum evento único sendo narrado, mesmo
quando a descrição cita números (o primeiro cita "1467 a 1615" explicitamente,
mas como o objeto do debate, não como a faixa do vídeo). Os dois foram para
`Extra`/`Historiografia`. O critério: um debate sobre a interpretação de
UM evento datado entra na linha do tempo (com a data do evento, geralmente
`chute` por falta de número próprio); um debate sobre método, terminologia
ou periodização em si — sem evento único — fica Extra, mesmo padrão de
"Extra virou balde" (o teste continua sendo "o vídeo tem começo e fim no
tempo", não o rótulo "discussão"/"debate" do título). Critério aplicado na
classificação, ainda não confirmado por revisão humana explícita — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver".

**Em faixa `chute` de civilização inteira (Panorama), a data de FIM vem da
memória mais confiável que a de INÍCIO — fact-check deve pesar mais o
início.** Achado na parada/aprovação do lote 122 (canal The Histories, cujo
formato inteiro é "Who were the X?" — etnografia de um povo antigo por
vídeo, sem nenhuma data própria na evidência na maioria dos casos). De 8
faixas `chute`/conhecimento-geral verificadas por busca externa, 3 erraram
— e as 3 erraram exatamente no ano de INÍCIO (Minoicos: 2700 a.C. quando o
consenso é 3000 a.C.; Fenícios: 1200 a.C. quando o padrão mais citado é
1500 a.C.; Pechenegues: fim 1100 d.C. quando o desaparecimento real foi
1122, na Batalha de Beroia — este é o único erro de fim, e por pouco: 22
anos). Em compensação, toda data de FIM ligada a um evento nomeável e
famoso (queda de Tiro para Alexandre, 332 a.C.; absorção na Idade Média
escocesa, ~900 d.C.; fim do Império Vândalo em Tricamarum, 534 d.C.) bateu
de primeira. Padrão plausível: o fim de uma civilização costuma coincidir
com um evento célebre e citável (uma conquista, uma batalha, uma queda de
capital) que a memória geral retém bem; o início costuma ser um processo
gradual (uma cultura "emergindo", uma migração) sem um ano-marco tão
memorável, e por isso mais fácil de errar por arredondamento ou por
confundir o começo do período "clássico"/"áureo" com o começo da
civilização em si. Lição: ao fazer fact-check de faixas `chute` amplas,
prioritizar a verificação do ANO DE INÍCIO sobre o de fim quando o tempo
para checar tudo for limitado — é onde o erro mais provavelmente está.

**Número real no bloco de evidência pode não ser uma data — pode ser o ano de
um filme/produto citado nos créditos.** Achado na classificação do lote 123
(canal GatesOfKilikien): a descrição de "Ancient Greece - The Peloponnese"
tem só uma linha nas "datas citadas" extraídas automaticamente — "Image
Credits: Wikimedia Commons, and the film 300 (2006)". O `(2006)` ali é o ano
de lançamento do filme *300*, citado como crédito de imagem, não uma data do
assunto do vídeo. Diferente da armadilha já documentada "Número real na
evidência, mas irrelevante para o período do vídeo" (onde o número é uma
data genuína do texto, só que sobre outro evento/pessoa) — aqui o número nem
é uma data histórica: é o ano de um produto moderno citado em nota de
atribuição. O regex de extração de "datas citadas" não distingue os dois
casos (ambos batem no padrão `\(\d{4}\)`), então cabe a quem classifica olhar
o contexto ao redor de todo número antes de usá-lo como âncora de confiança.
Sem esse número (o único da evidência inteira), a linha ficou `chute`/Extra
corretamente. Lição: **antes de aceitar um número como data do assunto,
confirmar que o texto ao redor descreve um evento histórico, não um crédito
de imagem/vídeo, uma citação bibliográfica ou qualquer outro metadado
moderno** — filmes, jogos, livros e sites de referência quase sempre têm ano
de publicação, e esse ano cai no mesmo padrão regex que uma data histórica
real.

**Nome de tema existente pode combinar com o ASSUNTO do vídeo e ainda assim
ser o tema errado, quando o FORMATO do vídeo não bate com o dos outros
membros do tema.** Achado na parada dos lotes 123-124 (canal
GatesOfKilikien): as duas partes de "Xi'an (Chang'an)" foram classificadas
em `Vida urbana > Chang'an` na hora — o tema existe, "vida numa cidade" é
exatamente do que os vídeos tratam, e Chang'an é uma cidade, então a decisão
pareceu óbvia. Mas os outros subtemas de `Vida urbana` (Roma, Constantinopla,
Alexandria, Atenas, Hattusa, Quioto) são todos sobre uma fatia estreita da
vida numa cidade **num momento específico** — não sobre a cidade como capital
política através de mais de mil anos de dinastias. As duas partes de Xi'an
somam 840 e 1128 anos cada (`Panorama`), estruturalmente idênticas aos outros
ensaios de "este lugar através da história inteira" que o mesmo canal produz
e que corretamente foram para `Geografia Estratégica` (Xiangyang, Xuzhou).
Corrigido na aprovação: as duas linhas saíram de `Vida urbana > Chang'an`
para `Geografia Estratégica`. Diferente da armadilha já documentada "Rótulo
de série não é o tema — vale o conteúdo" (onde o nome da série do canal
engana sobre QUAL evento está sendo narrado): aqui o nome do tema batia
perfeitamente com o assunto (cidade, vida urbana), e o que enganava era a
**escala temporal e o formato** (ensaio panorâmico vs. recorte de época).
Lição: ao encaixar um vídeo num tema existente, comparar não só se o assunto
bate, mas se a **largura da faixa de anos e o formato narrativo** do vídeo
batem com os outros membros do mesmo tema — um tema pode estar certo no nome
e errado no encaixe.

**`periodo()` devolve `"Extra"` por padrão sempre que os anos vêm vazios —
inclusive para linhas que deveriam ser `Aleatório`.** Achado na aprovação dos
lotes 125-128 (canal Revolutions/Mike Duncan), mas o bug é mais velho que
esta sessão: `6pemEIq1KOo` (lote 77, canal Ancient Americas, já encerrado e
travado) tem o mesmo defeito, achado ao auditar o catálogo inteiro em busca
do mesmo padrão. A função `periodo(ai, af)` do `verificar.py` (reaproveitada
pelos scripts de gravação para calcular `Século/Período`) só sabe fazer duas
coisas: calcular o ponto médio, ou devolver `"Extra"` quando `ai`/`af` são
`None`. Ela **não sabe** que existe uma segunda categoria de linha sem
período (`Aleatório`, para vídeo que não é história) — essa escolha é
exatamente a única parte da Lista A que não é derivável dos anos e cabe a
quem classifica (ver `SEM_PERIODO` no `verificar.py` e "Linhas travadas"
acima). Quem grava a planilha chamando `periodo(None, None)` direto para uma
linha de aviso de canal, resenha ou outro conteúdo não-histórico recebe
`"Extra"` de graça — e o `verificar.py` **não pega isso**, porque tanto
`"Extra"` quanto `"Aleatório"` satisfazem a mesma checagem estrutural (anos
vazios, `confianca = n/a`, `travado = sim`); a diferença está no assunto do
vídeo, que o portão não lê. Corrigido nas 2 linhas desta sessão
(`laM6N_ZnYxs`, introdução do podcast; `M6yv1ftGTj8`, especial de perguntas e
respostas) — célula `Século/Período` isolada, nada mais mudou. **Não
corrigida** em `6pemEIq1KOo` por já estar travada de um ciclo anterior (ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver"). Lição: ao
escrever uma linha `Aleatório` num script de gravação, **setar
`Século/Período = "Aleatório"` explicitamente na hora — nunca deixar o
default do `periodo(None, None)` decidir**, porque ele sempre escolhe
`"Extra"` e o portão não avisa quando isso está errado.

**Título do episódio cita o ano de um documento/lema invocado, não o ano do
próprio episódio.** Achado na parada dos lotes 125-128: o episódio "3.41 -
Bread and the Constitution of 1793" (podcast Revolutions) narra a revolta de
Prairial, em **1795** — "1793" no título é o ano da Constituição de 1793 que
os manifestantes invocavam como lema ("Bread and the Constitution of
1793!"), não o ano do episódio. Busca externa confirmou: a revolta é de
20/mai/1795 (World History Encyclopedia, CHNM). Diferente da armadilha já
documentada "Rótulo de série não é o tema" (nome da série do canal, não de um
documento histórico real) e de "Nome de governante... pode ser metonímia"
(nome de pessoa como atalho popular para um sistema): aqui o título cita o
**ano de um documento histórico genuíno e verificável**, só que não é o ano
do episódio — é o ano do objeto que os personagens DO episódio estão
invocando. Lição: quando o título de um episódio inclui um ano, perguntar se
esse ano descreve **o evento do episódio** ou **algo que o evento do episódio
menciona/invoca** (uma lei, uma constituição, um slogan) antes de aceitar o
número do título como a data do vídeo.

**Faixa `chute` de episódio suplementar/de contexto sem nenhuma data pode
ficar ancorada no ano-rótulo da season, não num evento real de fim.** Achado
na parada dos lotes 129-132 (podcast Revolutions): o episódio "6.08c -
Metternich" (sem nenhuma data na descrição, só "after the fall of Napoleon")
recebeu a faixa `1814-1830` — 1814 é real (Congresso de Viena), mas 1830 não
é o fim de nada na vida de Metternich, é só o ano-título da season em que o
episódio está inserido (Revoluções de 1830). Metternich continuou no poder
até 1848. Mesmo padrão em "5.20 - The Sea Wolf" (Thomas Cochrane no Peru,
faixa `1818-1820` sem nenhuma data própria) e "7.31 - The Assembly of the
Damned" (faixa `1849` sem citar país nem evento). Diferente da armadilha já
documentada "Moldura convencional do próprio vídeo pode encurtar uma faixa
chute" (onde o rótulo enganoso vem da PRÓPRIA evidência do vídeo, tipo
"Archaic period"): aqui não há rótulo nenhum na evidência — a armadilha é
usar o **limite da season/ciclo do canal** como se fosse um limite do
próprio evento, na ausência total de evidência. Essas três linhas foram
aprovadas mesmo assim (não há erro factual, só base fraca), mas registradas
como decisão de baixa confiança na apresentação da amostra. Lição: para
episódio de contexto/suplemento sem nenhuma data, ancorar o fim da faixa no
que a evidência realmente sustenta (mesmo que vago, tipo "para o resto da
vida da pessoa" ou "sem fim claro, deixar em aberto com nota") — não no ano
que a season do canal usa como rótulo, que é conveniência de playlist, não
data do assunto.

**Tema-raiz novo proposto sem checar o lote imediatamente anterior da mesma
fonte, mesmo dentro do mesmo ciclo em aberto.** Achado na parada dos lotes
133-135 (podcast Revolutions): o lote 134 criou o tema `Revolução Russa` para
os episódios 10.1-10.21 da Season 10; o lote seguinte (135), classificado
numa conversa diferente, propôs um SEGUNDO tema-raiz — `Revolução Russa de
1905` — para os episódios 10.22-10.46, sem conferir que o lote anterior já
tinha aberto um tema para o mesmo arco narrativo contínuo (mesma season,
mesmo podcast, sem intervalo entre os episódios). Os dois foram fundidos na
parada, em `Revolução Russa de 1905` (ver `vocabulario-canonico.md`, "Estado
atual" e "Sobreposições ainda por resolver"). Diferente das armadilhas de
vocabulário já documentadas (que tratam de CANAIS diferentes cobrindo o mesmo
assunto sob nomes diferentes, ex. Vândalos/Reino Vândalo, Cátaros/Cruzada
Albigense): aqui é o MESMO canal, a MESMA season, dividida em lotes
sequenciais classificados em conversas separadas — o risco não é de fontes
diferentes, é de continuidade perdida entre lotes vizinhos do mesmo arco.
Lição: antes de propor um tema-raiz novo, checar não só a Lista C inteira,
mas especificamente o campo `observacoes` do canal/playlist em `canais.json`
— se o lote imediatamente anterior já tratou do mesmo arco narrativo, o tema
provavelmente já existe, mesmo que a Lista C ainda não tenha sido regenerada
para incluí-lo (ela só é regenerada na aprovação, não a cada lote).

**Vídeo que cruza vários períodos já cobertos pelo próprio catálogo através
de uma lente teórica, não narrativa, é `Extra`/método — não um falso
Panorama.** Achado na parada dos lotes 136-138 (podcast Revolutions): a
série de encerramento "Appendix 1-11" compara padrões comuns a TODAS as
revoluções que o podcast já cobriu em dez temporadas (Guerra Civil Inglesa,
Revolução Americana, Francesa, Haitiana, Hispano-Americana, 1830, 1848,
Comuna de Paris, Mexicana, Russa) — um arco de quase 300 anos (1640s-1920s),
bem perto do limiar de `Panorama` (`LIMIAR_PANORAMA = 300`, ver
`vocabulario-canonico.md`, Lista A). A tentação é tratar isso como mais um
caso do degrau `Panorama`: faixa larga, mas datável, então entra na linha do
tempo com um rótulo `Panorama (1640 - 1922)`. Mas o conteúdo não narra um
processo histórico contínuo — é uma teoria comparativa (por que regimes
caem, o que dispara uma revolução, por que a revolução "devora seus
filhos") ilustrada saltando entre processos já catalogados em linhas
próprias, sem ordem cronológica interna. Um leitor vendo "Panorama (1640 -
1922)" esperaria uma narrativa contínua desse intervalo, que não é o que o
vídeo entrega. Diferente do caso já registrado em "Extra virou balde" (onde
o problema era vídeos NARRATIVOS caindo em `Extra` por preguiça de calcular
o ponto médio de uma faixa larga): aqui o teste que decide é outro —
**o vídeo narra um processo histórico específico (mesmo que longo), ou usa
casos históricos como ilustração de uma tese que poderia ter escolhido
exemplos diferentes?** Só o primeiro caso é `Panorama`/linha do tempo; o
segundo é `Extra`, categoria "método" (mesmo grupo de `guia de estudo`,
já prevista no `protocolo.md`, "Decisões já tomadas"), com região `Global` e
anos vazios. Mesmo lote também teve o primeiro caso de ficção AUTORAL do
próprio canal (não resenha de obra alheia) — a mini-season "Martian
Revolution", publicada quase um ano após o encerramento da série regular,
como despedida especulativa do autor — tratada como `Aleatório` (tema novo
`Revolução Marciana (ficção)`), pelo mesmo princípio já usado para
ficção/cultura de internet no Thersites the Historian, mas registrado aqui
porque é a primeira vez que a ficção vem do próprio apresentador do canal de
história, não de terceiros.

**Reupload por recombinação: o mesmo conteúdo dividido de um jeito na série
antiga e de outro na série nova — não é o reupload 1:1 já documentado.**
Achado na adoção do canal Magistra Vitae (lotes 139-140). O padrão de
reupload já registrado (History of Byzantium, Shogunate, Revolutions) é
sempre 1:1: mesmo episódio, mesmo número, `video_id` diferente. Aqui o canal
refez a própria série do zero e, ao remontar, mudou o corte dos vídeos: a
série antiga contava o Reino de Roma em dois episódios (`Founding of Rome
[OLD] #1`, só o reinado de Rômulo, 753-716 a.C.; `Seven Kings of Rome #2`,
os outros seis reis, 716-509 a.C.), e a série nova compilou o mesmo conteúdo
em um vídeo só por corte diferente (`Founding of Rome - Start of the
Greatest Civilisation`, ainda só Rômulo; `Seven Legendary Kings of Rome`,
os sete reis inteiros num vídeo). A prova de que é o mesmo material, não
coincidência de assunto, veio da própria descrição do vídeo antigo: "We made
a remake of this video that you can watch here". As quatro linhas entraram
no catálogo normalmente (mesmo tratamento do reupload 1:1 — cada `video_id`
é uma linha própria, sem descartar nenhuma), com nota cruzando os pares.
Lição: ao encontrar um vídeo "[OLD]" ou uma descrição citando um remake, não
presumir que o corte cronológico bate 1:1 com o vídeo novo equivalente —
conferir capítulo a capítulo (ou, na ausência deles, frase a frase da
descrição) qual fatia de tempo cada versão cobre antes de copiar a faixa de
uma para a outra.

**"Nome de tema existente pode combinar com o assunto e ainda ser o tema
errado" reincide num canal completamente diferente — não é peculiaridade do
GatesOfKilikien.** Achado na parada dos lotes 141-144 (canal Ryan M Reeves,
sem nenhuma relação com o GatesOfKilikien): `ljBaVIp2pJQ` ("The Long History
of Notre Dame in Paris") foi classificado na hora em `Vida urbana > Paris`
— o tema existe, "vida numa cidade" bate com o assunto, Paris é uma cidade.
Mas, exatamente como no caso do Xi'an (protocolo.md, "Nome de tema existente
pode combinar com o ASSUNTO..."), os outros subtemas de `Vida urbana` (Roma,
Constantinopla, Alexandria, Atenas, Hattusa, Quioto) são recortes estreitos
de uma época específica, e este vídeo é um ensaio panorâmico de mais de 2000
anos ("From the Celtic tribes, to the conquest of Rome in Gaul, to the
cathedral we know today"). Corrigido na aprovação para `Geografia
Estratégica > Notre-Dame de Paris` — o mesmo tema que já resolveu o caso
original. Lição reforçada: esta armadilha não é sobre um canal específico
ter um formato "cidade através da história" — é sobre qualquer vídeo cujo
título nomeia um lugar que também é subtema de um tema de recorte estreito.
Antes de aceitar o encaixe, comparar a largura da própria faixa de anos do
vídeo com a largura típica dos outros membros do mesmo subtema/tema, não só
o nome do lugar.

**Copiar a faixa de um vídeo reupload para o par sem reavaliação
independente propaga qualquer erro que a faixa original já tivesse.**
Achado na parada dos lotes 145-148 (canal Ryan M Reeves): dois reuploads
confirmados no ciclo (`IXpX1Gy4vYA`/`Sjy23bJdLQg`, "Luther's Reformation
Breakthrough"; `7LDJiCtGuxA`/`JF3t3Xx4s5A`, "The Hobbit") tiveram a faixa do
vídeo novo copiada diretamente da linha irmã já catalogada, em vez de
reavaliada a partir da evidência do próprio vídeo novo (que também não
tinha nenhuma data própria, mas isso só reforça — não substitui — a
necessidade de checar). Diferente do caso já documentado ("Um canal pode
subir dois vídeos diferentes com o mesmo número e título" — onde cada
vídeo é classificado pela própria evidência, e às vezes uma versão tem mais
contexto que a outra): aqui a prática foi deliberadamente copiar a faixa
por eficiência, assumindo que "mesmo título, mesma faixa" é seguro. Nos dois
casos deste ciclo isso não gerou erro (a faixa original já estava correta,
confirmada por fact-check em pelo menos um deles), mas é uma prática de
risco: se a linha original tiver uma faixa `chute` errada, o reupload herda
o erro sem chance de ser pego por uma segunda leitura independente da
evidência. Lição: mesmo confirmando um reupload por título/duração idênticos,
vale reler a evidência do vídeo novo com os mesmos olhos de uma linha
qualquer — a cópia da faixa é um atalho aceitável só depois dessa
checagem, não no lugar dela.

**Uma frase na descrição que só reafirma o título não é "descrição narrando
o evento" — é o título com verbo, e sustenta no máximo `média`.** Achado nos
lotes 149-152 (canal HistoryMarche): boa parte das descrições do canal tem
uma frase de abertura do tipo "I'm happy to share the Battle of Salamis 480
BC with you" ou "Battle of Breitenfeld 1631 marked the emergence of Sweden
as a great power" — tecnicamente uma frase própria do vídeo, com um número
de ano dentro dela, diferente do caso já fechado "alta inflada por
título/tags" (onde não havia frase nenhuma, só o título nu). Mas essas
frases não narram o evento — elas só decoram o título com um verbo
("compartilhar", "marcar") sem acrescentar nenhum detalhe que um leitor não
já tivesse pelo título sozinho. Diferente de frases que genuinamente narram
("In August 1745, Nadir Shah faced a massive Ottoman army outside the
fortress of Kars" — que descreve quem, contra quem, onde), a frase-eco não
teria sentido fora do contexto do próprio título que acabou de repetir.
Tratado como `média`, não `alta`, em pelo menos 3 linhas do ciclo (Salamis
480 a.C., Breitenfeld 1631, Halidon Hill 1333) — critério aplicado consis-
tentemente, mas nunca antes registrado por escrito. Lição: ao decidir se uma
frase da descrição sustenta `alta`, o teste não é só "há um número de ano
dentro de uma frase própria do vídeo?", mas **"essa frase diz algo sobre o
evento que o título já não dissesse?"** — se a resposta for não, a frase é
eco de título, não narrativa, e o teto continua `média`.

**Faixa `chute` de uma compilação "ALL PARTS" sem nenhuma data pode ser
reconstruída cruzando com episódios individuais vizinhos já catalogados no
mesmo lote ou em lotes anteriores — mas é uma inferência em cadeia, não uma
leitura de evidência, e deve ficar registrada como tal.** Achado nos lotes
149-152 (canal HistoryMarche): `OtqFPmkBiqI` ("Hannibal PARTS 18-20") não
tinha nenhum ano no título nem na descrição, mas a Parte 20 (catalogada no
mesmo lote) descrevia seu próprio início como "continuamos de onde paramos
após a 2ª Batalha de Nola" — um evento datável por conhecimento geral (215
a.C.) — e terminava "spring of 212 BC" (data própria, já usada para a Parte
20). A faixa da compilação (216-212 a.C.) foi construída cruzando essas
pontas com a Parte 21 (Siracusa, 213-212 a.C., outro lote) e com o
conhecimento geral da campanha de Hannibal no sul da Itália pós-Canas.
Mesmo com o fact-check da parada confirmando a coerência (2ª Nola foi de
fato 215 a.C.), a linha continua `chute`: nenhuma das datas está na
evidência do próprio vídeo, todas vieram de outras linhas e de conhecimento
geral. Lição: cruzar dados de linhas vizinhas é uma técnica legítima para
escolher a faixa de uma compilação sem evidência própria — melhor do que
"nenhuma data, faixa arbitrária" —, mas não promove a confiança acima de
`chute`, e a nota da linha precisa deixar rastreável de onde cada ponta da
faixa veio (evita o problema já documentado de "nota promete o que a célula
não tem").

**`chute` tem um grau mais arriscado ainda: quando nem o assunto exato, só
a faixa, precisa ser inferido.** Achado na parada dos lotes 153-156 (canal
HistoryMarche): `_JPBPyMLvIA` ("Salt Trade and Rebellion in Medieval
China") não tinha nenhuma data nem o nome do evento na evidência — só as
tags "tang dynasty" e a palavra "rebellion" no título. Toda a maioria dos
casos `chute` documentados até aqui já sabiam do QUE o vídeo tratava (um
reinado, uma guerra nomeada) e só faltava a data; aqui faltava também
identificar QUAL revolta chinesa era essa. A classificação ("Rebelião de
Huang Chao, 874-884", ancorada em Huang Chao ter sido historicamente um
contrabandista de sal) foi uma inferência de segunda ordem, verificada só
depois, no fact-check da parada — e bateu. Lição: quando uma linha `chute`
exige adivinhar o próprio assunto (não só a data), isso é um risco
qualitativamente maior que o `chute` comum, mesmo que a confiança
registrada na planilha seja a mesma — vale registrar na nota o raciocínio
completo (não só "faixa por conhecimento geral", mas por que esse assunto
específico foi escolhido), porque se a parada não fizer o fact-check dessa
linha, o erro de identificação passa despercebido com a mesma aparência de
qualquer outro `chute` reforçado.

**Bloco "Related Videos:" da descrição carrega números reais que descrevem
OUTRO vídeo, não o assunto do vídeo atual.** Achado nos lotes 160-162 (canal
History with Cy), reincidente três vezes na mesma janela: `jvwiGj6e_X4`
(Pasargadae) tem, como único número na descrição, "History of the Achaemenid
Persian Empire, Part I (550-486 BC...)" — o título de um vídeo relacionado,
não a data da própria fundação de Pasárgada; `FYJ8lNl3mfY` (Peloponnesian
War Parte I) e `Y9iu34f2SQM` (Sparta and the Messenian Wars) têm, como único
número, "Ancient Greece during the Archaic Period (750-480 BC)" — de novo,
o título de um vídeo relacionado, não do assunto narrado no vídeo atual.
Diferente da armadilha já documentada "alta inflada por título/tags, sem
data própria" (que trata de título/tags do PRÓPRIO vídeo) e de "descrição
padrão da série engana" (que trata de um parágrafo de abertura reciclado
entre episódios da mesma minissérie): aqui o número está num campo de
metadado específico — a lista "Related Videos:"/"Contents: Related Videos:"
que o canal anexa ao fim de toda descrição — e o padrão do canal é linkar
vídeos cujo título já tem a própria faixa de datas embutida (formato comum
neste canal: "Title (XXX-YYY BC)"). É tentador contar esse número como
"data citada na descrição", mas ele descreve o vídeo linkado, não o vídeo
sendo classificado. Regra: ao aplicar a checagem de `alta` ("existe um
número que cai na faixa?"), ignorar por completo qualquer número que apareça
dentro de um item da lista de vídeos relacionados — só um número que
apareça no corpo narrativo da própria descrição (fora dessa lista) ou nos
capítulos sustenta `alta`. As três linhas deste canal já vinham `chute`
antes da checagem (nenhuma tinha sido inflada), mas o padrão é
suficientemente recorrente num canal só para merecer registro antes que
aconteça numa sessão que não preste atenção.

**Script de inserção manual de linha comparando só `ano_inicio`/`ano_fim`,
sem `Mês`/`Dias`, quebra a ordenação em empates.** Achado na gravação do
lote 171 (canal Epic History): sem `gravar.py` fixo no projeto, cada sessão
escreve um script `openpyxl` ad-hoc para achar a posição certa de cada linha
nova e usar `insert_rows()`. O script desse lote calculava a posição
percorrendo as linhas existentes e comparando só `(ano_inicio, ano_fim)` —
mas a ordenação real da planilha é por `(ano_inicio, ano_fim, Mês, Dias)`,
igual ao `chave()` do `verificar.py`. Resultado: `PbwH1ZBnYds` ("World War 1
- 1914", `Mês`/`Dias` = `*` → 0) ficou depois de uma linha existente com o
mesmo `ano_inicio`/`ano_fim` mas `Mês=11, Dias=1` — como 0 < 11, a linha
nova devia vir ANTES, não depois. `verificar.py --anterior` pegou o erro
("fora de ordem") antes de qualquer coisa ser salva — o portão funcionou
como devia — mas o backup teve que ser restaurado e o lote regravado depois
do conserto. Corrigido fazendo o `chave()` do script de inserção ler
`Mês`/`Dias` de cada linha candidata (com o mesmo parser `num()` de
`verificar.py`, que trata `*` como 0) em vez de usar um padrão fixo de
`0, 0`. Lição: qualquer script de inserção ad-hoc que decidir "onde a linha
nova entra" tem que usar a chave de ordenação **completa** de quatro campos,
nunca só os dois anos — testar contra `verificar.py --anterior` antes de
declarar a gravação pronta pega isso, mas sai mais barato acertar a chave
de uma vez.

**Tema-raiz novo proposto sem buscar sinônimo/tradução alternativa na Lista C
inteira, não só no ciclo em andamento.** Achado na parada dos lotes 172-175
(canal Invicta): duas propostas de tema-raiz eram duplicatas de termos já
existentes em canais *diferentes*, adotados muito antes — `Gladiadores
Romanos` (proposto) vs. `Gladiadores` (Kings and Generals, já existente,
mesma região e faixa quase idêntica) e `Besteiros Genoveses` (proposto) vs.
`Balestreiros Genoveses` (SandRhoman History, já existente, título do
vídeo em inglês literalmente idêntico — "Genoese Crossbowmen"). Em nenhum
dos dois casos houve busca por palavra-chave antes de propor o termo — o
raciocínio foi "não existe X" sem checar variações de tradução (besteiro/
balestreiro), de escopo ("Romanos" a mais/a menos) ou de nome curto vs.
composto. Diferente da lição já registrada sobre checar o vocabulário do
*próprio ciclo* em andamento (History with Cy, `Fenícia Antiga` vs.
`Civilização Fenícia`): aqui o duplicado estava em canais completamente
diferentes, adotados há dezenas de lotes — só aparece numa busca textual na
Lista C inteira do `vocabulario-canonico.md`, não na memória do que "parece
familiar". Lição: antes de propor qualquer tema-raiz novo, rodar ao menos
uma busca por palavra-chave (incluindo sinônimos plausíveis e traduções
alternativas do termo em português) contra a Lista C inteira — não confiar
só em não reconhecer o termo de memória. As duas linhas foram fundidas nos
temas já existentes na aprovação; uma delas ainda carregava um bug de sinal
(`ano_inicio` negativo por engano, 1000 a.C. em vez de 1000 d.C.) que só
apareceu ao investigar a duplicata.

**Vídeo se contradiz sozinho — título e descrição discordam do mesmo fato.**
Achado no lote 178 (canal Invicta): "Punic Sicilian Wars - The Battle of
Himera (480 BC)" tem o ano certo no título, mas a própria descrição escreve
"culminates in the climactic battle of Himera in 409 BC" — 71 anos de
diferença, mesmo evento. Diferente da armadilha "a fonte erra" (que compara
o vídeo contra o fato conhecido) e de "descrição padrão da série engana"
(parágrafo reciclado entre episódios): aqui as duas partes da evidência do
mesmo vídeo simplesmente não batem entre si. O desempate não veio só do
conhecimento geral — veio de checar o vídeo seguinte da mesma série
("Hannibal's Revenge"), que cita "at the Battle of Himera in 480 BC" no
próprio texto, confirmando o título como o lado certo. Lição: quando título
e descrição de um vídeo se contradizem numericamente, não escolher um dos
dois por padrão — checar contra o conhecimento geral do evento e, se
houver, contra a citação do mesmo fato em outro vídeo da série.

**Reaproveitar a faixa de um grupo adjacente sem checar se as pessoas citadas
pertencem mesmo a ele.** Achado no fact-check da parada dos lotes 184-187
(canal History of Philosophy Without Any Gaps): a linha "HoP 449 - Anna
Tropia on Jesuit Philosophy" recebeu a faixa 1483-1617, copiada dos
episódios vizinhos sobre a Escola de Salamanca — mas a ponta inicial vinha
de **Francisco de Vitoria, que era dominicano, não jesuíta**, e a Companhia
de Jesus só foi fundada em 1540. A faixa afirmava, na prática, que a
filosofia jesuíta existia 57 anos antes da existência dos jesuítas. O erro
passou pela classificação porque os episódios eram vizinhos na série, o
tema era o mesmo (`Segunda Escolástica`) e Molina e Suárez, de fato
jesuítas, apareciam nos dois blocos. Diferente da armadilha "descrição
padrão da série engana" (que trata de texto reciclado): aqui a contaminação
foi do **classificador**, não da fonte. Lição: ao herdar uma faixa de um
grupo/escola/dinastia vizinha, verificar se cada pessoa que ancora as pontas
da faixa pertence de fato ao grupo que a linha declara — sobretudo quando
uma das pontas vem de um nome que o próprio vídeo não cita. Sinal de alerta
prático: a nota da linha já dizia "o ponto é fraco" na hora de gravar; nota
que confessa fragilidade é candidata natural ao fact-check da parada.

**Mesmo nome de subtema criado em dois temas-raiz diferentes, quando o
assunto de fundo é o mesmo mas a época cai em lados opostos de uma fronteira
já fixada no catálogo.** Achado na parada dos lotes 188-191 (canal History of
Philosophy Without Any Gaps): `Tolerância Religiosa` foi criado sob
`Renascimento` (Sebastian Castellio, 1515-1563, lote 191) e, três lotes
depois na mesma sessão, sob `Filosofia Moderna` (Maria Rosa Antognazza sobre
tolerância em Locke/Leibniz, 1517-1716, também lote 191) — cada um checou a
Lista C antes de propor e não achou duplicata, porque tecnicamente não havia
nenhuma: são temas-raiz diferentes. O problema não é um erro de fato (cada
linha está no tema-raiz certo para a própria época, já que `Filosofia
Moderna` só começa com Descartes por convenção do catálogo), é que o mesmo
rótulo de subtema em dois lugares faz parecer que existe um nó só. Mesmo
padrão, mesma sessão: `Ceticismo Renascentista` (novo) ficou parecido demais
com `Ceticismo Francês` (já existente, era de Pascal). Lição: quando o
assunto de um subtema novo atravessa uma fronteira de época que já separa
dois temas-raiz do catálogo (ex.: Renascimento/Filosofia Moderna, medieval/
Segunda Escolástica), checar não só se o *nome* já existe em algum lugar, mas
se ele deveria ser o *mesmo* nome usado no tema-raiz vizinho — e, se for,
registrar a decisão consciente na nota (não deixar como coincidência muda).
Não corrigido retroativamente; registrado em `vocabulario-canonico.md`,
"Sobreposições ainda por resolver".

**Título de vídeo cita uma obra específica, mas a classificação usou "vida
inteira" no piloto automático.** Achado na parada dos lotes 192-195 (canal
History of Philosophy Without Any Gaps): `HAP 61 - When and Where I Enter -
Anna Julia Cooper` recebeu a faixa da vida inteira de Cooper (1858-1964),
seguindo a convenção padrão para conteúdo biográfico sem fase clara — mas a
própria descrição nomeia uma obra específica, "A Voice from the South"
(1892), como o assunto do episódio. A convenção já estava escrita no
protocolo ("Conteúdo biográfico/conceitual sem evento datável": obra
específica usa a faixa da obra, não a vida inteira) — o erro não foi não
saber a regra, foi aplicar o padrão "pensador → vida inteira" por reflexo
sem checar primeiro se a descrição já identificava uma obra pontual.
Corrigido na aprovação para `1892`. Lição: antes de aplicar a convenção de
vida inteira a um vídeo biográfico, checar se a descrição já nomeia uma obra
específica (título entre aspas, nome de livro/ensaio) — se sim, a faixa é da
obra, não da pessoa, mesmo que nada mais na evidência dê uma data.

**Frase evocativa da descrição ("crepúsculo do império", "no limiar de uma
nova era") não é uma data — é preciso achar o evento real por trás dela
antes de fechar a ponta da faixa.** Achado na parada dos lotes 196-199
(canal History of Philosophy Without Any Gaps): `HoP 324 - Latin Philosophy
in Byzantium` tinha a faixa `1330-1450`, com a ponta final ("1450")
justificada só pela frase da própria descrição, "at the twilight of
empire" — uma leitura minha de que "crepúsculo" significava "pouco antes da
queda de Constantinopla em 1453", sem nenhum evento real ancorando esse
número. A descrição também citava, de forma concreta, "the Hesychast
controversy" — um evento historicamente datável (os sínodos de
Constantinopla, 1341 a 1351) que eu não usei como âncora da faixa,
preferindo a frase vaga. Corrigido na aprovação para `1341-1351`. Diferente
da armadilha já documentada "moldura convencional do próprio vídeo pode
encurtar uma faixa chute" (que trata de aceitar um rótulo de período
genérico como se fosse a faixa real): aqui o problema foi o oposto —
inventei uma ponta de faixa a partir de uma frase impressionista quando a
própria evidência já continha um evento nomeado e verificável que deveria
ter sido a âncora. Lição: quando a descrição usa uma expressão evocativa de
tempo ("no auge de", "no ocaso de", "às vésperas de") ao lado de um evento
ou controvérsia nomeada, a âncora da faixa é o evento nomeado (buscável e
verificável), nunca a expressão evocativa (interpretação subjetiva de quem
classifica).

**Um canal grande com múltiplas séries numeradas paralelas pode esconder uma
série inteira por muitos lotes — vigie prefixos novos mesmo em canal já
`em andamento` há dezenas de lotes.** Achado no lote 200 (canal History of
Philosophy Without Any Gaps): até o lote 199, o `CLAUDE.md` e o
`vocabulario-canonico.md` só documentavam três séries intercaladas (HoP,
HPC, HAP). O lote 200 trouxe episódios com o prefixo `HPI` (*History of
Philosophy in India*) — uma quarta série inteira, com 62 episódios
próprios, que nunca tinha aparecido porque a coleta anda do mais recente ao
mais antigo e o HPI só começou a ser alcançado depois que as janelas
publicadas mais recentes de HoP/HAP foram esgotadas. Nenhum erro de
classificação aconteceu (o prefixo era óbvio no título assim que apareceu),
mas o registro de "quantas séries este canal tem" no `CLAUDE.md` estava
desatualizado havia 16 lotes sem que ninguém percebesse. Lição: num canal
com séries numeradas paralelas, não presumir que a lista de séries já
documentada está completa só porque muitos lotes já passaram sem novidade —
cada lote novo é uma chance de um prefixo nunca visto aparecer.

**Data explícita de século no título/descrição fixa a faixa exata do
século, não a faixa de vida dos pensadores citados.** Achado nos lotes
201-202 (canal History of Philosophy Without Any Gaps, arco "Fourteenth
Century Philosophy"): `HoP 280 - Fourteenth Century Physics` e `HoP 277 -
Fourteenth Century Logic` citam "Fourteenth Century" no próprio título, mas
os pensadores discutidos (Ockham, n. 1287; Buridan, n. c.1300; Oresme, n.
c.1320) têm datas de nascimento que começam antes de 1300. A tentação é
estender a faixa para cobrir a vida inteira do pensador mais velho citado
(1287-1382, por exemplo) — mas isso contradiz a própria evidência, que
narra "século XIV", não "vidas dos pensadores envolvidos". Faixa correta:
`1300-1400`, exatamente o que o título diz, confiança `alta`. Lição:
quando a evidência narra um século/período explícito, a faixa é esse
período, ponto — não amplie nem encolha para acomodar biografias
individuais que a própria evidência não está tentando descrever.

**Duas linhas sobre o mesmo pensador podem ter faixas diferentes,
legitimamente, se a evidência de cada uma aponta para coisas diferentes.**
Achado no lote 203 (mesmo canal): `HoP 257 - Henry of Ghent and Freedom`
usou a vida inteira de Henrique de Gand (1217-1293, convenção padrão para
conteúdo biográfico sem fase clara). `HoP 256 - Frequently Asked Questions
- Henry of Ghent`, sobre o mesmo pensador, tinha a própria descrição
dizendo "a leading scholastic in the **late 13th century**" — uma faixa
mais estreita (1270-1300) e com confiança `alta`, porque aponta para o
período de *atuação*, não para nascimento-morte. A tentação seria copiar a
faixa da linha companheira só porque é o mesmo subtema/pensador — errado:
cada linha usa a faixa que a *sua própria* evidência sustenta, mesmo que
outra linha do mesmo pensador, no mesmo lote, use uma faixa diferente.

**Texto religioso/filosófico antigo sem consenso de datação na própria
literatura acadêmica: faixa larga com `chute` é o resultado correto, não um
sinal de pesquisa malfeita.** Confirmado na parada dos lotes 200-204 (série
HPI, canal History of Philosophy Without Any Gaps): textos como o
Vaiśeṣika-Sūtra, o Mīmāṃsā-Sūtra e o Vedānta-Sūtra têm datações que a
própria literatura acadêmica dá como disputadas por séculos (ex.:
Bādarāyaṇa "variously dated from 500 BCE to 450 CE" — quase mil anos de
incerteza reconhecida pelos próprios especialistas). Fact-check da parada
confirmou 5 faixas assim, todas batendo com a literatura. Lição: para esse
tipo de texto, uma faixa larga com `chute` bem documentada em `notas` (com
a fonte da disputa) é a classificação correta — não tentar forçar precisão
que a própria academia não tem, nem rebaixar para Extra só porque a faixa é
larga (Extra é para quando não há nenhuma faixa fixável, não para quando a
faixa fixável é imprecisa).

**Episódio 1 (ou último) de uma série mistura "objetivos/despedida da
série" com conteúdo histórico real — decidir pelo peso do conteúdo, não
pela posição na numeração.** Achado no lote 214 (canal History of
Philosophy Without Any Gaps): `HoP 001 - Everything is Full of Gods -
Thales`, o primeiro episódio de todo o podcast, tem descrição "Peter
discusses the goals of the series and Thales, the first Greek
philosopher." Os episódios de puro lançamento de série já catalogados
(`HoP 196`, `HoP 120`, `HoP 101`, `HAP 01`, `HPI 01`) foram todos `Avisos
do canal` porque a descrição inteira era meta-discussão, sem substância
histórica própria. Este caso é diferente: mesmo citando "os objetivos da
série", a descrição nomeia um assunto histórico real e central (Tales, "o
primeiro filósofo grego"). Classificado como conteúdo histórico (subtema
`Tales de Mileto`), não `Avisos do canal`. Lição: não aplicar a convenção
"episódio de abertura/encerramento = Avisos do canal" no piloto automático
só pela posição na numeração — checar se a descrição tem substância
histórica própria pesando mais que a menção à série. Quando as duas coisas
aparecem juntas (comum em episódios-marco: 1º, 50º, 100º, 200º, 300º), o
critério é qual delas é o assunto central do vídeo, não qual é citada
primeiro.

**Esgotamento que se auto-confirma: a prova de que um canal acabou não vale
nada se o canal já estava marcado `encerrado`.** Achado na auditoria de
17/11/2026, ao reabrir os vinte canais encerrados. O `status: encerrado`
autoriza o `coletar.py` a ligar a parada antecipada, que interrompe a varredura
na primeira página inteiramente conhecida. Mas a prova de esgotamento que este
protocolo usa — "a coleta seguinte veio com 0 vídeos novos" — roda com essa
mesma parada ligada. Ou seja: **a parada antecipada produz o 0 que serve de
prova para o status que ligou a parada antecipada.** Circular, e silencioso.

O estrago: varrendo o `uploads` inteiro dos vinte canais com
`incremental=False` e comparando contra planilha ∪ `catalogados.txt` ∪
`descartados.txt`, apareceram **1216 vídeos catalogáveis que o projeto nunca
viu** — 1009 no Invicta (publicados de 2013 a 2019; a cobertura do catálogo
começa em 2019-11-27) e 204 no Kings and Generals (2017-2019; cobertura a
partir de 2019-12-01), mais 3 no Thersites. Conferido por título: **não são
reupload** — dos 204 do Kings and Generals, só 5 batem com título já na
planilha; dos 1009 do Invicta, nenhum. O `CLAUDE.md` tratava apenas o Invicta
como suspeito, por ter sido encerrado por decisão humana; o Kings and Generals
estava listado como esgotamento real e tinha o mesmo defeito.

Duas lições:

1. **Nunca aceite "0 vídeos novos" como esgotamento se o canal já estava
   `encerrado` na hora da coleta.** Para provar de verdade, varra o uploads
   inteiro com a parada antecipada desligada e compare contra os três arquivos
   de ids. É barato (1 unidade de cota por página de 50).
2. **Numa revisita, a parada antecipada esconde mais do que o acervo antigo.**
   Depois do primeiro lote de uma revisita, a primeira página fica toda
   conhecida (os 25 aprovados mais os descartes), e a varredura para ali — os
   vídeos novos das páginas seguintes ficam invisíveis. Foi o que aconteceu
   entre os lotes 232 e 233: 21 vídeos novos do Kings and Generals, publicados
   entre agosto e setembro de 2026, sumiram da coleta. Por isso existe o
   `coletar.py --desde AAAA-MM-DD`: desliga a parada antecipada e a troca por
   uma parada por data, que encerra a varredura quando aparece uma página só
   com vídeos anteriores ao corte. Assim a revisita pega tudo o que foi
   publicado desde a última coleta sem arrastar o acervo antigo — e os vídeos
   antigos ignorados **não** vão para `descartados.txt`, porque não foram
   recusados, só não foram pedidos.

**O dossiê da parada virou arquivo.** A partir da reabertura de 17/11/2026, a
parada de quatro lotes é escrita em `paradas/parada-NNN-NNN.md` em vez de só
aparecer na conversa: vocabulário novo, fact-check com fonte, as cinco linhas
sorteadas com a evidência ao lado, e as pendências abertas. Motivo prático: numa
rodada longa, o relato da parada 1 não sobrevive até a parada 5 se morar só no
chat, e as pendências se perdem entre sessões. O sorteio das cinco linhas usa
semente fixa derivada dos números de lote, para ser reproduzível e não
"escolhido" por quem apresenta.
