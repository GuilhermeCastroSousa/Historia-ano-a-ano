# Catálogo de história — instruções de sessão

Cataloga vídeos de história do YouTube numa planilha ordenada pelo período que o
vídeo **trata**, não pela data de publicação. Ordem: 3300 a.C. até hoje, numa
linha do tempo só.

**Leia antes de qualquer coisa:** `protocolo.md` (manual de operação) e
`vocabulario-canonico.md` (listas fechadas de período, região, tema e subtema).
Os dois são a fonte de verdade. Este arquivo não os repete — só cobre o que muda
por você estar rodando com acesso de escrita ao disco.

---

## Estado: vinte canais adotados, todos encerrados, nenhum em andamento

**Kings and Generals** (lotes 0-76), **Thersites the Historian** (lotes 40-75),
**Ancient Americas** (lotes 77-78), **Historia Civilis** (lotes 79-82),
**Cambrian Chronicles** (lotes 83-84), **The History of Rome (Mike Duncan)**
(lotes 85-86), **The History of Byzantium Podcast** (lotes 87-102),
**SandRhoman History** (lotes 103-109), **The Shogunate** (lotes 110-121),
**The Histories** (lote 122), **GatesOfKilikien** (lotes 123-124),
**Revolutions (Mike Duncan)** (lotes 125-138), **Magistra Vitae** (lotes
139-140 e 231, revisita pontual), **Ryan M Reeves** (lotes 141-148),
**HistoryMarche** (lotes 149-158), **History with Cy** (lotes 159-167),
**Epic History** (lotes 168-171), **Invicta** (lotes 172-183), **History of
Philosophy Without Any Gaps Podcast** (lotes 184-214) e **ESOTERICA** (lotes
215-230) estão todos `encerrado` em `canais.json` — **inclusive os dois
últimos, cuja decisão de fechar formalmente (em vez de manter em pausa
técnica) foi confirmada pelo humano em 10/08/2026.** `verificar.py` (sem
`--anterior`) confere limpo nesse estado: 5415 linhas, 0 `revisar`, checklist
ok. **Nenhum canal está `em andamento`** — a próxima sessão precisa adotar um
canal novo ou reabrir um dos vinte já encerrados antes de rodar `/lote` ou
`/rodada`.

**ESOTERICA encerrado em 10/08/2026** por esgotamento real confirmado — o
lote 230 veio como mini-lote de 8 vídeos e uma coleta seguinte confirmou 0
vídeos novos nos mesmos 505 percorridos, chegando ao início cronológico da
publicação do canal (março de 2020, `Introduction to Western
Esotericism`). Para reabrir quando o canal publicar episódios novos:
`python coletar.py "@TheEsotericaChannel"` (com aspas no PowerShell). Ver
a seção própria mais abaixo para o resumo completo do canal (383 linhas,
16 lotes, 22 temas-raiz novos).

**ESOTERICA fechou o primeiro ciclo de quatro lotes (216-219, 100 linhas)
via o novo comando `/rodada`, aprovado em 10/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** Canal do Dr. Justin Sledge, primeiro
de esoterismo/ocultismo do catálogo (adotado no lote 215, ver
`.claude/commands/rodada.md` para o comando criado nesta sessão que roda até
4 lotes sem pausa e fecha com a parada sozinho). Mesma convenção do canal de
filosofia: conteúdo biográfico/conceitual sem evento datável vai para a
linha do tempo (vida inteira do pensador, ou faixa ampla do conceito
cross-era), nunca `Extra`/`Aleatório` por padrão — só administrivia real do
canal (avisos, sorteios, divulgação de excursão/curso) vira `Extra > Avisos
do canal`. Conteúdo dominado por três séries em curso do canal:
"Introduction to Merkavah Mysticism" (15 episódios sobre misticismo judaico
pré-cabalístico, c. 100-1000 d.C.), "The Occult Philosophy of Cornelius
Agrippa" (8 de 14 episódios cobertos até agora) e uma sequência avulsa sobre
demônios/entidades (Lilith, Belial, Baal, Moloch, os demônios do Talmude).
Introduziu **9 temas-raiz** neste ciclo (`Vlad III, o Empalador`, `História
dos Fantasmas`, `Aleister Crowley`, `John Dee e a Magia Enocheana`,
`Immanuel Kant`, `Manuscritos do Mar Morto (Qumran)`, `Arthur Schopenhauer`,
`Espiritualismo Moderno`, `As Origens do Gótico`) e ~30 subtemas, a maioria
reaproveitando os quatro temas-raiz que o lote 215 já tinha aberto
(`Demonologia Ocidental`, `Hermetismo`, `Filosofia Judaica Medieval >
Misticismo Merkavah`, `Renascimento > Cornélio Agripa`/`Paracelso e a
Alquimia`). Nenhuma região nova. Fact-check da parada verificou 4 datações
de maior risco (morte de Peter of Abano, ano do Malleus Maleficarum usado
para calcular a data do Formicarius de Nider, datação do Códice Maya de
México, período de Zósimo de Panópolis) — as 4 bateram. **1 correção na
aprovação**: a linha "Agrippa's Afterlife" (lote 219) teve a ponta final da
faixa estreitada de 1700 (extensão especulativa minha sobre a recepção
rosacruz do século seguinte, sem base na evidência) para 1535, a morte de
Agripa — lição registrada no `protocolo.md`, "Armadilhas conhecidas"
("Estender a ponta de uma faixa por inferência de gênero/formato do
episódio"). Pendências de vocabulário deixadas em aberto, não bloqueantes:
`Manuais de Exorcismo e Necromancia (pré-1614)` (Renascimento) vs
`Necromancia e Grimórios Medievais` (Escolástica Medieval), mesma família de
assunto em dois temas-raiz diferentes; `Renascimento` como tema-raiz
guarda-chuva já cobrindo tanto a Europa continental quanto as colônias
americanas (John Winthrop, o Jovem) — ver `vocabulario-canonico.md`,
"Sobreposições ainda por resolver". Detalhes completos em `canais.json`,
campo `observacoes`.

**ESOTERICA fechou o segundo ciclo via `/rodada` — lote 215 (órfão da
rodada anterior) + lotes 220-223 (125 linhas), aprovados em 10/08/2026 na
mesma parada — canal segue `em andamento`, sem sinal de esgotamento.**
Primeira parada do projeto a reunir um lote solto com um ciclo novo
inteiro numa só rodada de revisão. Fechou duas séries longas do canal por
completo: "Introduction to Merkavah Mysticism" (15 de 15 episódios) e "The
Occult Philosophy of Cornelius Agrippa" (14 de 14 episódios). Introduziu
**6 temas-raiz** (`Karl Marx`, `Johannes Bureus e a Runologia Esotérica`,
`Vampiros (Origens Históricas)`, `Yukio Mishima`, `William Blake`, `Sigmund
Freud e a Psicanálise`) e ~35 subtemas — `Caça às Bruxas` e `Hermetismo`
foram os maiores ímãs do ciclo, 6 subtemas novos cada. Nenhuma região
nova. Fact-check verificou 4 datações de maior risco (execução de Cecco
d'Ascoli, publicação de "Beyond the Pleasure Principle" de Freud, De
Lamiis et Pythonicis Mulieribus de Molitor, datas de vida de Plotino) — as
4 bateram. **Zero correções na aprovação** — a amostra de 5 linhas não
revelou erro, só confirmou uma decisão já sinalizada como frágil na hora
(faixa de quase 2000 anos da linha sobre a loucura divina de Platão,
reconstruída a partir de quatro nomes citados sem data própria). Pendência
nova: cluster `Nicholas Eymerich` espalhado em 3 subtemas de 2 temas-raiz
diferentes (`Hermetismo` e `Caça às Bruxas`) — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Canal
agora com 225 linhas totais (lotes 215-223). Detalhes completos em
`canais.json`, campo `observacoes`.

**ESOTERICA fechou o terceiro ciclo via `/rodada` — lotes 224-227 (100
linhas), aprovados em 10/08/2026 — canal segue `em andamento`, sem sinal
de esgotamento formal, mas a coleta reversa chegou ao próprio vídeo de
lançamento do canal** (`Welcome to ESOTERICA`, maio de 2021, lote 227) —
a linha do tempo de publicação está quase inteiramente percorrida; a
próxima rodada pode vir como mini-lote. Fechou a série "Introduction to
Kabbalah and Jewish Mysticism" (14 de 14 episódios), gerando a maior
concentração de subtemas novos sob `Filosofia Judaica Medieval` de
qualquer ciclo do canal (13 subtemas). Introduziu **6 temas-raiz**
(`Pânico Satânico`, `Austin Osman Spare`, `Georges Bataille`, `Anne
Conway`, `Isaac Newton`, `Baruch Spinoza`) e ~40 subtemas. Nenhuma região
nova. **Primeiro `Aleatório` do canal**: uma "descoberta arqueológica"
fictícia do Zohar sobre Ester, identificada na própria descrição como
piada de 1º de abril de 2022. Fact-check verificou 4 datações de maior
risco (Perseguição de Dioclesiano aos alquimistas, Cleópatra a Alquimista,
Maria a Judia, Isaac o Cego/Azriel de Gerona) — as 4 bateram. **Zero
correções na aprovação**. Reaproveitou pela primeira vez dois temas-raiz
herdados de outros canais do catálogo (`Pré-Socráticos`, `Mitraísmo`).
Canal agora com 325 linhas totais (lotes 215-227), 0 `revisar`. Detalhes
completos em `canais.json`, campo `observacoes`.

**ESOTERICA fechou o quarto ciclo via `/rodada` — lotes 228-230 (58
linhas), aprovados em 10/08/2026 — encerrado por ESGOTAMENTO REAL
CONFIRMADO, não por completar 4 lotes.** O lote 230 veio como mini-lote de
8 vídeos e uma coleta seguinte confirmou 0 vídeos novos nos mesmos 505
percorridos — o canal chegou ao início cronológico da própria publicação
(março de 2020, `Introduction to Western Esotericism`). `Hermetismo` foi
o maior ímã (12 subtemas novos), com a série "John Dee - The Monas
Hieroglyphica" (3 partes) e a trilogia sobre absinta fechadas neste ciclo.
Introduziu **1 tema-raiz** (`História da Absinta`) e ~35 subtemas. Nenhuma
região nova. Fact-check verificou 4 datações de maior risco — 3 bateram
exatamente (Summa Perfectionis c. 1310, tradução de Robert de Chester em
1144, Sefer HaRazim séc. III-IV d.C.); a 4ª (Ritual Maqlû, "3000 anos" na
evidência) ficou no fim da janela de uso do ritual segundo a bibliografia
mais recente — divergência normal, não erro. **Zero correções na
aprovação**. Canal com **383 linhas totais (lotes 215-230), 0 `revisar`**.
**Decisão confirmada pelo humano em 10/08/2026: encerrado formalmente**, não
mantido em pausa — `canais.json` já reflete `status: "encerrado"`,
`encerrado_em: "2026-08-10"`. Reabertura futura é o mesmo comando de sempre:
`python coletar.py "@TheEsotericaChannel"` (com aspas no PowerShell) quando o
canal publicar episódios novos. Detalhes completos em `canais.json`, campo
`observacoes`.

**History of Philosophy Without Any Gaps Podcast encerrado em 09/08/2026**
por esgotamento real da série principal (HoP) — confirmado por duas coletas
seguidas com 0 vídeos novos, depois que o lote 214 (mini-lote de 16)
terminou no próprio `HoP 001 - Thales`, o primeiro episódio do podcast
inteiro. Para reabrir quando o podcast publicar episódios novos: `python
coletar.py "@HistoryofPhilosophywithoutGaps"` (com aspas no PowerShell —
sem elas, `@` é interpretado como operador de splatting e o argumento some,
caindo no `CANAL` hardcoded do script). Ver a seção própria mais abaixo
para o resumo completo do canal (766 linhas, 31 lotes, 11 temas-raiz
novos, e a pendência aberta sobre a linha `HPI 60`).

Para adotar um canal novo, `python coletar.py @Handle` (que registra o
canal em `canais.json` sozinho na primeira coleta) ou reabra um
dos vinte encerrados apontando o `coletar.py` para ele (revisita
incremental — lote parcial, às vezes de 1 vídeo só, é o esperado; para o
Revolutions especificamente, é `python coletar.py --playlist
PLIjP3HEQ0F-8B6x_9l4bJef2q4hFvb9s0`, sem precisar de `--nome` de novo, já
salvo; para o Magistra Vitae, `python coletar.py @MagistraVitae`; para o
Ryan M Reeves, `python coletar.py @ryanreevesm`; para o HistoryMarche,
`python coletar.py @historymarche`; para o History with Cy, `python
coletar.py @historywithcy`; para o Epic History, `python coletar.py
@EpichistoryTv`; para o Invicta, `python coletar.py @invictahistory`).

**History of Philosophy Without Any Gaps (Peter Adamson) fechou o primeiro
ciclo com 100 linhas em 4 lotes (184-187), aprovado em 08/08/2026 — canal
segue `em andamento`.** Primeiro canal de filosofia do catálogo, e o de
**evidência mais magra até hoje**: descrições de 1-2 frases, **zero
capítulos em 100 vídeos**, 24 de 25 vídeos por lote sem nenhum número. São
**duas séries numeradas intercaladas semana a semana** — HoP (principal) e
HPC (filosofia chinesa) — então cada lote mexe em duas famílias de
vocabulário separadas por 1.800 anos. Como a coleta vai do mais recente ao
mais antigo e a série é cronológica progressiva (ep. 1 = Tales, ep. 498 =
Bayle), **o catálogo percorre a história da filosofia de trás para frente**:
os lotes 184-187 cobriram a França do século XVII recuando até o
Renascimento tardio; os gregos só devem aparecer daqui a ~15 lotes.
Perfil de confiança inédito — **zero linhas `Extra`/`Aleatório`** e **88 de
100 linhas `média`**, datadas por busca externa com a fonte em `notas`.
Introduziu **3 temas-raiz** (`Filosofia Moderna`, `Segunda Escolástica`,
`Dinastia Qin`) e 14 subtemas, nenhuma região nova. **Duas convenções
fixadas com o humano antes do primeiro lote**, válidas para todo conteúdo
biográfico/conceitual (ver `protocolo.md`): vídeo sobre um pensador usa a
**vida inteira** dele; vídeo sobre conceito cross-era fica na **linha do
tempo com faixa ampla**, não vira `Extra`. Também ficou fixado que **data
confirmada por busca externa entra como `média`**, não `chute` — sem isso,
88 linhas deste ciclo teriam colapsado num balde só. 3 correções na
aprovação (faixa da filosofia jesuíta reprovada no fact-check, faixa do
yin-yang que contradizia o tema, unificação dos dois episódios sobre
Elisabeth da Boêmia). **Pendência principal, não resolvida por exigir
autorização sobre linha travada:** `Dinastia Zhou > Cem Escolas do
Pensamento` chegou a **46 vídeos** misturando cinco escolas filosóficas
rivais (confucionismo, moísmo, daoísmo, legalismo, Escola dos Nomes) — a
saída seria promovê-lo a tema-raiz, mas isso mexeria na linha travada do
Kings and Generals que criou o termo. Detalhes em `canais.json`.

**History of Philosophy Without Any Gaps fechou o segundo ciclo com 100
linhas em 4 lotes (188-191), aprovado em 09/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** Marco do ciclo: chegada da
**terceira série** do canal, **HAP** (*History of Africana Philosophy*),
que abriu o tema-raiz `Filosofia Africana` no fim do lote 188 e o encheu de
**32 subtemas em três lotes** — quase um por pessoa ou movimento (Cornel
West, Angela Davis, Frantz Fanon, Nelson Mandela, Amílcar Cabral, Kwame
Nkrumah, Steve Biko, Walter Rodney, Édouard Glissant, Sylvia Wynter, Ngũgĩ
wa Thiong'o, Panteras Negras, Poder Negro, Teoria Racial Crítica,
Afrofuturismo, Reggae e Rastafari, entre outros). HoP fechou um arco de 5
episódios sobre Shakespeare e outro sobre ciência inglesa renascentista
(Dee, Gilbert, Fludd), avançando até o humanismo/reforma franco-inglês de
fins do séc. XVI/início do XVII; HPC seguiu no período clássico chinês.
Introduziu **2 regiões novas** (`Caribe`, `África Oriental`) e **1 tema-raiz
novo** (`Filosofia Africana`), mais **54 subtemas** ao todo. Confiança no
mesmo padrão do primeiro ciclo — **93 linhas `média`** (busca externa, nunca
`alta` por convenção já fixada), **5 `alta`** (século/década narrado no
corpo da própria descrição, nunca em título) e **2 `chute`**. Fact-check da
parada verificou 3 datações de risco (início da carreira de Sun Ra/
Afrofuturismo, início da Escolástica, declínio do Black Power) — as 3
bateram, **zero correções na aprovação**. Pendências de vocabulário
deixadas em aberto, não bloqueantes: subtema `Tolerância Religiosa`
duplicado em dois temas-raiz por época (`Renascimento` × `Filosofia
Moderna`); `Feminismo Negro` partido em dois subtemas por década; `Ceticismo
Renascentista` × `Ceticismo Francês` (nomes parecidos); `Filosofia Política
Huguenote` × `Rebeliões Huguenotes` (nomes parecidos, assuntos diferentes);
região `Global` na linha de Frantz Fanon, talvez `Caribe`/`Norte da África`
fosse mais preciso — ver `vocabulario-canonico.md`, "Sobreposições ainda por
resolver". **Pendência principal segue crescendo:** `Dinastia Zhou > Cem
Escolas do Pensamento` foi de 46 para **53 vídeos** neste ciclo, ainda sem
autorização para promover a tema-raiz. Detalhes completos em `canais.json`.

**History of Philosophy Without Any Gaps fechou o terceiro ciclo com 100
linhas em 4 lotes (192-195), aprovado em 09/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** HoP fechou o finale da série
"Renascimento Italiano" (**12 vídeos consolidados num único subtema
guarda-chuva** — Cardano, Telesio/Campanella, magia e astrologia, Bruno,
Galileu, medicina, Roma — em vez de fragmentar por pessoa, mais um cluster
próprio de 3 episódios sobre Maquiavel) e entrou na Reforma alemã/suíça
(Lutero, Melanchthon, Zwínglio, Calvino, Erasmo, Guerra dos Camponeses). HAP
consolidou o núcleo de pensadores negros do final do séc. XIX/virada do
XX — Du Bois, Alain Locke, Booker T. Washington, Marcus Garvey (+ as duas
esposas Amy), a Academia Negra Americana, e uma dúzia de intelectuais
pan-africanistas menos conhecidos (Crummell, Blyden, Horton, Fortune,
Firmin, Turner, Cooper, Wells) — mais um desvio geográfico único, o
abolicionismo no Brasil (Luiz Gama, Machado de Assis, Joaquim Nabuco).
Nenhum tema-raiz novo, nenhuma região nova — só reaproveitamento (`Caribe`,
`África Oriental`, `Haiti`) e **61 subtemas novos**, a maioria (43) sob
`Filosofia Africana`, que já passa de 90 subtemas desde sua criação no lote
188. Confiança: **72 `média`**, **17 `alta`** (época narrada no corpo da
descrição — inclusive um caso em que a faixa veio do **próprio título** do
episódio, "W.E.B. Du Bois, 1920-1963") e **10 `chute`**. Fact-check da
parada verificou 3 datações de risco (invenção da imprensa/Reforma,
nascimento de Leonardo Bruni, fundação/dissolução da Academia Negra
Americana) — as 3 bateram. **1 correção na aprovação**: `HAP 61 - Anna Julia
Cooper` tinha a faixa da vida inteira (1858-1964), mas a evidência aponta
para uma obra específica ("A Voice from the South") — estreitada para
`1892`, o ano do livro; lição registrada no `protocolo.md`, "Armadilhas
conhecidas" (aplicar "vida inteira" no piloto automático sem checar se a
descrição já nomeia uma obra pontual). Pendências de vocabulário deixadas em
aberto, não bloqueantes: faixa interna muito variável (1370-1642) dentro do
mesmo subtema `Renascimento Italiano`; `W.E.B. Du Bois` com 4 faixas
diferentes em 3 lotes; cluster pan-africanista do séc. XIX com fronteiras
temporais sobrepostas (`Raízes do Nacionalismo Negro` / `Alexander
Crummell` / `Academia Negra Americana`) — ver `vocabulario-canonico.md`,
"Sobreposições ainda por resolver". Detalhes completos em `canais.json`.

**History of Philosophy Without Any Gaps fechou o quarto ciclo com 100
linhas em 4 lotes (196-199), aprovado em 09/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** Duas mudanças de conteúdo grandes.
HAP recuou até perto do **início da própria série**: filosofia no Egito e
na Mesopotâmia antigos, os filósofos etíopes Zera Yacob e Walda Heywat, a
Etiópia antiga (Kebra Nagast), Islã na África Subsaariana (Songhay, Sokoto)
— e, no lote 198, **treze episódios seguidos** sobre o debate do séc. XX de
como fazer filosofia africana (etnofilosofia de Tempels, crítica de
Hountondji, Filosofia dos Sábios de Odera Oruka), consolidados num único
subtema guarda-chuva. HoP percorreu o Renascimento italiano completo
(Maquiavel, Ficino, Pico, Savonarola, humanistas) até a filosofia bizantina,
que ganhou **três subtemas de recorte cronológico** sob o mesmo tema-raiz
`Império Bizantino`: era do Iconoclasmo (séc. VII-IX), era Comnena (séc.
XI-XIII) e Tardia (séc. XIV-XV, já criada no lote 197). **Dois vídeos foram
movidos para temas-raiz já existentes** em vez de gerar conteúdo paralelo —
Egito/Mesopotâmia Antiga (`Egito antigo`, `Babilônia Antiga`) e a Revolução
Haitiana (`Revolução Haitiana`). Nenhum tema-raiz novo, nenhuma região
nova, **42 subtemas novos**. Confiança: **62 `média`**, **26 `chute`** (o
maior número de qualquer lote do canal até agora), **9 `alta`** e **3
`n/a`**. Fact-check da parada verificou 2 datações de risco (vida de John
Ítalos, morte de Bar Hebraeus) — as 2 bateram. **1 correção na aprovação**:
`HoP 324 - Latin Philosophy in Byzantium` tinha a ponta final da faixa
("1450") baseada numa leitura minha da frase vaga "twilight of empire", não
numa data real — estreitada para `1341-1351`, os sínodos reais da
controvérsia hesicasta citada na própria descrição; lição registrada no
`protocolo.md`, "Armadilhas conhecidas" (frase evocativa não é data — achar
o evento real por trás dela). Pendências de vocabulário deixadas em aberto,
não bloqueantes: os três recortes cronológicos de `Filosofia Bizantina`
podem se sobrepor nas bordas; `Etnofilosofia e Debate sobre a Filosofia
Africana` é a maior consolidação de subtema por guarda-chuva até agora, com
6 de 13 linhas `chute` sem nenhuma âncora própria — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`.

**History of Philosophy Without Any Gaps fechou o quinto ciclo com 125
linhas em 5 lotes (200-204 — cinco, não quatro, porque a parada só rodou
depois do lote 204), aprovado em 09/08/2026 — canal segue `em andamento`,
sem sinal de esgotamento.** Marco do ciclo: descoberta da **quarta série**
do canal, **HPI** (*History of Philosophy in India*), não documentada até
então — até o lote 199 o catálogo só registrava HoP, HPC e HAP. A série
inteira (62 episódios) coube neste ciclo só: o lote 200 trouxe o **último**
episódio da série (HPI 62, encerramento) e o lote 204 já alcançou o
**primeiro** (HPI 03, Período Védico) — a coleta reversa finalmente atingiu
a janela de publicação em bloco da série (2024-04-27/2024-05-05). HoP
percorreu o século XIV inteiro (Ockham, Buridan, Oresme, os "Calculadores
de Oxford", a seção oficial "Fourteenth Century Philosophy" do próprio
site do podcast, confirmada por busca externa) até Tomás de Aquino, Alberto
Magno e Duns Scotus no século XIII. Introduziu **1 tema-raiz novo**
(`Filosofia Indiana`, 49 subtemas — o maior tema-raiz introduzido de uma
vez neste catálogo) e mais **38 subtemas em `Escolástica Medieval`**.
Nenhuma região nova; 3 aproximações registradas (Buddhaghosa → Índia,
origens da humanidade → África Oriental, Henrique de Gand → Países Baixos).
Confiança: 67 `média`, 12 `chute` (todas HPI, textos indianos antigos sem
consenso de datação nem na própria literatura acadêmica), 5 `alta` (só
quando a própria descrição narra o século/período explicitamente — nunca
vida de pensador vinda de busca externa) e 41 `n/a`. Fact-check da parada
verificou as 5 datações `chute` de maior risco (Cārvāka, Vaiśeṣika-Sūtra,
Vedānta-Sūtra, Mīmāṃsā-Sūtra, Caraka-Saṃhitā) — as 5 bateram com a
literatura acadêmica. **Zero correções na aprovação** — a amostra de 5
linhas sorteadas para o humano não revelou erro, só uma decisão de base
fraca já sinalizada na hora (`HPI 31`, faixa de 800 anos por disputa
acadêmica real). **Duas lições novas registradas no `protocolo.md`,
"Armadilhas conhecidas"**: data explícita de século no título/descrição
fixa a faixa exata do século, não a faixa de vida dos pensadores citados
(ex.: "Fourteenth Century Physics" = 1300-1400, não 1287-1382 só porque
Ockham nasceu em 1287); e duas linhas sobre o mesmo pensador podem ter
faixas diferentes legitimamente, se a evidência de cada uma aponta para
coisas diferentes (Henrique de Gand: uma linha usa vida inteira, outra usa
"late 13th century" porque a própria descrição diz isso). Pendências de
vocabulário deixadas em aberto, não bloqueantes: `Bhagavad-Gītā` ×
`Mahābhārata: Dharma e Ética` × `Origens do Karma` (mesma obra em três
subtemas); `Nyāya` fragmentado em 5 subtemas, `Vaiśeṣika` em 3, `Mīmāṃsā`
em 3; convenção "(Debate Moderno)"/"(Painel/Entrevista)" usada 8+ vezes sem
critério fechado de consolidação; cluster "Século XIV" com 4 subtemas
próximos — ver `vocabulario-canonico.md`, "Sobreposições ainda por
resolver". Detalhes completos em `canais.json`.

**History of Philosophy Without Any Gaps fechou o sexto ciclo com 100
linhas em 4 lotes (205-208), aprovado em 09/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** Marco do ciclo: **dois temas-raiz
novos de uma vez** — `Filosofia Islâmica` (descoberta no lote 206, cauda/
início da série *Philosophy in the Islamic World* do canal) e `Filosofia
Judaica Medieval` (descoberta no lote 207, logo em seguida, cauda de um
arco sobre pensamento judaico andaluz). O catálogo já documentava HoP,
HPC, HAP e HPI; com estes dois, o podcast passou a ter **seis** domínios
registrados. HoP fechou o arco do século XII-XIII (Abelardo, Heloísa,
Anselmo, Eriúgena, Hildegard von Bingen, carolíngios, ascensão das
universidades) e entrou no núcleo clássico da filosofia islâmica e
judaica: Averróis, Avicena, al-Ghazali, Ibn Khaldun, Ibn 'Arabī de um
lado; Maimônides, Gersônides, Hasdai Crescas, Judah Halevi, Ibn Gabirol do
outro. Introduziu **57 subtemas novos**. Nenhuma região nova. Confiança:
74 `média`, 8 `alta` (sempre com o século citado no próprio título/
descrição, nunca vida de pensador vinda de busca externa), **zero
`chute`** — diferença marcante do ciclo anterior (12 `chute`, todos textos
indianos): aqui os pensadores são figuras centrais extremamente bem
documentadas, sem disputa acadêmica relevante de datação. Fact-check da
parada verificou 5 datações de maior risco (Ibn Gabirol, Baḥya Ibn
Paquda, Controvérsia Maimonidiana, Hasdai Crescas, Era Mongol) — as 5
bateram. **Zero correções na aprovação.** Pendências de vocabulário
deixadas em aberto, não bloqueantes: sobreposição `Traduções do Árabe
para o Latim` × `Movimento de Tradução para o Latim` (mesmo evento
histórico); `Gersônides`/`Hasdai Crescas`/`Ibn 'Arabī` solo × conjunto;
`Maimônides` fragmentado em 5 subtemas; cluster "(Debate Moderno)" (13
subtemas) e cluster "Século XII-XIV" (9 subtemas) — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`.

**History of Philosophy Without Any Gaps fechou o sétimo ciclo com 125
linhas em 5 lotes (209-213), aprovado em 09/08/2026 — canal segue `em
andamento`, sem sinal de esgotamento.** Marco do ciclo: **quatro
temas-raiz novos de uma vez** — `Platão`, `Aristóteles`, `Filosofia
Helenística e Romana` e `Neoplatonismo Tardo-Antigo` — a coleta reversa
finalmente alcançou o núcleo clássico grego (Sócrates via Platão, todos os
diálogos platônicos principais, o corpus aristotélico inteiro) e a
Antiguidade Tardia pagã (Plotino, Porfírio, Jâmblico, Proclo), além do
Estoicismo romano, Ceticismo, Epicurismo, Cirenaicos, Cínicos, Cícero,
Galeno e o Platonismo Médio. Introduziu **57 subtemas novos**. Nenhuma
região nova. Confiança: 108 `média`, 1 `alta` (só quando a própria
descrição/página do podcast narra o século explicitamente), 1 `chute`
(Pseudo-Dionísio Areopagita) — a maioria esmagadora das linhas datadas são
pensadores centrais extremamente bem documentados, sem disputa acadêmica
relevante de datação. Fact-check da parada verificou 4 datações de maior
risco — as 4 bateram. **Zero correções na aprovação.** Pendências de
vocabulário deixadas em aberto, não bloqueantes: `Aristotelismo
Pós-Aristóteles` × `Sucessores de Platão e Aristóteles` (mesmo assunto,
dois temas); `Platonismo Médio (Painel)` × `O Renascimento Platônico`; os
quatro temas-raiz novos formam uma cadeia cronológica contínua sem
guarda-chuva comum — ver `vocabulario-canonico.md`, "Sobreposições ainda
por resolver". Detalhes completos em `canais.json`.

**History of Philosophy Without Any Gaps: a série HoP esgotou no lote 214
(mini-lote de 16, chegando ao próprio `HoP 001 - Thales`), aprovado em
09/08/2026.** Duas coletas seguintes confirmaram 0 vídeos novos nos mesmos
768 percorridos — esgotamento real. Introduziu o tema-raiz `Pré-Socráticos`
(13 subtemas: os jônios — Tales, Anaximandro, Anaxímenes, Xenófanes,
Heráclito —, os da Magna Grécia — Pitágoras, Parmênides, Zenão, Melisso,
Empédocles —, os pluralistas/atomistas — Anaxágoras, Demócrito, Leucipo —,
os Sofistas e Hipócrates). Confiança: 15 `média`, 1 `n/a`, zero `alta` e
zero `chute`. Fact-check verificou 3 datações de risco — as 3 bateram, uma
exatamente (Tales, 624-546 a.C.). **Zero correções na aprovação.** Uma
decisão de fronteira foi registrada no `protocolo.md`, "Armadilhas
conhecidas": `HoP 001` mistura "objetivos da série" com conteúdo histórico
real (Tales) — classificado como conteúdo, não `Avisos do canal`, porque a
substância é central, diferente dos demais episódios de lançamento de
série já catalogados. Detalhes completos em `canais.json`.

**History of Philosophy Without Any Gaps Podcast encerrado em 09/08/2026 —
esgotamento real confirmado.** Maior canal de filosofia do catálogo: **766
linhas em 31 lotes (184-214)**. A revisão pedida pelo humano antes do
encerramento (todas as 81 linhas `Extra` do canal, nenhuma `Aleatório`)
encontrou **1 classificação provavelmente errada, não corrigida**: `HPI 60
- The Buddha and I - Indian Influence on Islamic and European Thought`
(`xDV0UEgmEbQ`, lote 200) nomeia quatro pensadores com datas conhecidas
(al-Bīrūnī 973-1048, Hume, Hegel, Schopenhauer) na própria descrição — pelo
padrão já fixado neste canal ("conceito que atravessa vários pensadores e
séculos vai para a linha do tempo, não vira Extra"), deveria ser `Panorama
(973-1860)`, `média`, em vez de `Extra`/`n/a`. A linha está travada
(aprovada numa parada anterior) e segue **sem correção**, aguardando
autorização explícita para sobrescrever célula travada — nenhuma das
outras 80 linhas `Extra` teve problema encontrado. Canal cobriu a história
da filosofia **de trás para frente** (coleta reversa): começou na
filosofia contemporânea (pontas mais recentes de HPC/HAP/HPI) e terminou
nos pré-socráticos gregos do séc. VI a.C. Introduziu **11 temas-raiz
novos** ao todo: `Filosofia Moderna`, `Segunda Escolástica`, `Dinastia Qin`
(primeiro ciclo) e depois `Filosofia Indiana`, `Filosofia Islâmica`,
`Filosofia Judaica Medieval`, `Neoplatonismo Tardo-Antigo`, `Filosofia
Helenística e Romana`, `Aristóteles`, `Platão`, `Pré-Socráticos` — nove
domínios/séries do próprio podcast documentados (HoP, HPC, HAP, HPI,
Filosofia Islâmica, Filosofia Judaica Medieval, Cristianismo Primitivo,
Neoplatonismo Tardo-Antigo, Filosofia Helenística/Romana + Aristóteles +
Platão + Pré-Socráticos como a "espinha dorsal" clássica). HPC não aparece
desde o lote 199 e HAP não estava esgotada quando a série principal
terminou — ambas podem ter conteúdo mais antigo não alcançado pela coleta
reversa. Pendências de vocabulário não bloqueantes acumuladas ao longo do
canal (cluster "(Debate Moderno)" com 13+ subtemas, cluster de cortes de
século XII-XIV, `Bhagavad-Gītā`/`Mahābhārata`/`Origens do Karma`,
fragmentação de escolas indianas, `Maimônides` em 5 subtemas,
`Aristotelismo Pós-Aristóteles`/`Sucessores de Platão e Aristóteles`,
`Traduções do Árabe para o Latim`/`Movimento de Tradução para o Latim`)
seguem documentadas em `vocabulario-canonico.md`, "Sobreposições ainda por
resolver". Reabertura: `python coletar.py "@HistoryofPhilosophywithoutGaps"`
quando o podcast publicar episódios novos. Detalhes completos em
`canais.json`.

**Invicta encerrado em 08/08/2026 por decisão humana explícita — ATENÇÃO:
diferente de todos os outros dezenove canais fechados neste catálogo, sem
esgotamento real confirmado.** O lote 183 (o último antes do encerramento)
percorreu 450 vídeos e ainda trouxe 25 aprovados cheios, sem sinal de
mini-lote nem uma coleta seguinte confirmando 0 vídeos novos. Se este canal
for reaberto, a paginação antecipada que `status: encerrado` habilita no
`coletar.py` pode pular vídeos antigos ainda não coletados — vale conferir
o total de vídeos do canal contra as 300 linhas já coletadas antes de
confiar na paginação rápida. Total: **300 linhas em 12 lotes (172-183)**,
três ciclos de parada completos (172-175, 176-179, 180-183), todos
aprovados e travados, 0 em `revisar`. Vídeo mais antigo: 2019-12-04; mais
recente: 2026-08-02. Canal de reconstruções militares em 3D ("True Size
of...", Unreal Engine 5) e das séries "Units of History" e "How They Did
It", cobrindo majoritariamente história romana (Terceira Guerra Púnica,
Segunda Guerra Púnica/Cannae, Exército Romano, Guerras Germânicas de Roma/
Avenging Varus), Guerras Greco-Púnicas na Sicília, Guerra Jugurtina, Sengoku
Jidai, Império do Mali, Guerra de Inverno finlandesa, Império Sassânida e
Harald Hardrada — com ruído recorrente grande de lore de ficção (Warhammer
40k, Star Wars, Duna, O Senhor dos Anéis) e resenhas de acurácia histórica
em mídia. Introduziu **18 temas-raiz novos** ao longo dos três ciclos e
dezenas de subtemas — ver `canais.json`, campo `observacoes`, para o
detalhamento por ciclo. Pendências de vocabulário deixadas em aberto, não
bloqueantes: ver `vocabulario-canonico.md`, "Sobreposições ainda por
resolver", pelos itens introduzidos por este canal (adjacências
`Guerra Romano-Seléucida`/`Guerras Sírias`, `Exército Sassânida`/`Império
Sassânida`, `Harald Hardrada`/`Era Viking`; colisão de nome "Campanha da
Itália"; divergência de datas 16×17 d.C. na série Avenging Varus).

**Invicta fechou o terceiro ciclo com 100 linhas em 4 lotes (180-183),
aprovado em 08/08/2026 com parada completa — canal segue `em andamento`,
sem sinal de esgotamento.** Maior proporção de conteúdo `Extra`/`Aleatório`
de qualquer ciclo do canal até agora (71% `n/a`): Roma cotidiana (leis,
tribunais, exército, gladiadores, Cartago) sem recorte de evento único, e
levantamentos comparativos cross-era sob o tema `Evolução da guerra` (PTSD
antigo, discursos de batalha, torres de cerco, táticas antielefante — 4
linhas Extra num ciclo só). Conteúdo histórico real cobriu a sequência
completa da campanha de vingança contra Armínio pós-Teutoburgo (9-17 d.C.,
novo tema `Guerras Germânicas de Roma`), a Guarda Varegue e a Peste de
Justiniano no Império Bizantino, e episódios avulsos bem documentados
historicamente sem data própria na evidência (galinhas sagradas/Drépano
249 a.C., motim das legiões de César 47 a.C., Wojtek o urso em Monte
Cassino 1944). Introduziu **2 temas-raiz novos** (`Guerras Germânicas de
Roma`, `Cerco de Jerusalém (70 d.C.)`) e **9 subtemas novos**, nenhuma
região nova — busquei cada termo na Lista C inteira antes de propor,
nenhuma duplicata encontrada. Fact-check da parada verificou 4 datações de
risco (Drépano, motim de César, Wojtek, invasão de Piye) — 3 bateram
exatamente, 1 (Piye) ficou 7 anos abaixo do consenso, dentro de margem
normal e já sinalizada `média` na própria linha. **1 correção na
aprovação**: região da linha da Peste de Justiniano trocada de
`Mediterrâneo` para `Egito` (mais específica, ancorada na evidência
própria). Pendências de vocabulário deixadas em aberto, não bloqueantes:
colisão de nome "Campanha da Itália" entre `Segunda Guerra Mundial` e
`Napoleão Bonaparte` (assuntos diferentes, mesmo nome-base); `Cerco de
Jerusalém (70 d.C.)` como tema-raiz de 1 vídeo só; divergência entre dois
vídeos da série Avenging Varus sobre se o desfecho foi 16 ou 17 d.C. — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`, campo `observacoes`.

**Invicta fechou o segundo ciclo com 100 linhas em 4 lotes (176-179),
aprovado em 08/08/2026 com parada completa — canal segue `em andamento`,
sem sinal de esgotamento (lote 179 veio cheio).** Mesmo padrão de
documentários "True Size"/"Units of History"/"How They Did It" do primeiro
ciclo, com fração grande de conteúdo `Extra`/`Aleatório`: Roma cotidiana
(exército, gladiadores, sociedade, direito) sem recorte de evento único, e
ficção recorrente (Warhammer 40k, Star Wars, Duna, O Senhor dos Anéis).
Conteúdo histórico real cobriu principalmente a série completa das 7
Guerras Greco-Púnicas na Sicília (reaproveitando um tema-raiz de só 1 vídeo
do Kings and Generals, que virou o maior consumidor do termo), a série da
Guerra Jugurtina (reaproveitando subtema do Thersites the Historian),
Império Bizantino, Império Sassânida, Rus de Kiev e a saga completa de
Harald Hardrada. Introduziu **4 temas-raiz novos** (`Erupção do Vesúvio (79
d.C.)`, `Exploração Antiga`, `Harald Hardrada`, `Meteoros na História`) e
**10 subtemas novos**, nenhuma região nova — busquei cada termo (e
sinônimos plausíveis) na Lista C inteira antes de propor, puxando a lição
do ciclo anterior; nenhuma duplicata encontrada desta vez. Confiança mais
alta que o ciclo anterior do mesmo canal (31% alta, 6% média, 8% chute, 55%
n/a — o n/a alto reflete o volume de `Extra`/`Aleatório`, não datação
fraca). Fact-check da parada verificou 5 datações de risco (fundação dos
Jomsvikings, nascimento de Olga de Kiev, viagem de Piteas, meteorito em
campo de batalha romano na Terceira Guerra Mitridática, reinado hipotético
do "imperador" Sponsian) — todas bateram com busca externa dentro de
margem normal de incerteza histórica, nenhuma correção de fato necessária.
**1 correção na aprovação**: região da linha de Piteas trocada de
`Atlântico` para `Ártico` (termo mais preciso já existente na Lista B).
**Nova lição registrada no `protocolo.md`, "Armadilhas conhecidas"**: um
vídeo cujo título e descrição discordam numericamente do mesmo fato
("Battle of Himera" com "480 BC" no título e "409 BC" na descrição) —
resolvido a favor do título/fato histórico, confirmado pelo texto de outro
vídeo da mesma série. Pendências de vocabulário deixadas em aberto, não
bloqueantes: `Harald Hardrada` (tema-raiz) vs. `Era Viking` (alternativa de
subtema não avaliada); `Erupção do Vesúvio (79 d.C.)` como tema-raiz de 1
vídeo só — ver `vocabulario-canonico.md`, "Sobreposições ainda por
resolver". Detalhes completos em `canais.json`, campo `observacoes`.

**Invicta fechou o primeiro ciclo com 100 linhas em 4 lotes (172-175),
aprovado em 08/08/2026 com parada completa — canal segue `em andamento`,
sem sinal de esgotamento.** Canal de reconstruções militares em 3D (série
"True Size of...", Unreal Engine 5) e da série "Units of History", com
ruído não-histórico grande: lore de ficção de Warhammer 40.000, O Senhor
dos Anéis (Rohan) e Duna (Fremen) — tudo `Extra`/`Aleatório` —, gameplay de
Total War/Manor Lords/Tlatoani/Empire of the Ants (`Aleatório`), e uma
família de resenhas de mídia/entrevistas sobre acurácia histórica em filmes
e séries (`Extra > História na cultura popular > Cinema`). Conteúdo
histórico real cobriu majoritariamente a Terceira Guerra Púnica (série de 5
partes), Segunda Guerra Púnica/Batalha de Cannae, Exército Romano
(medicina militar, inteligência/Frumentarii, carreira do soldado — tudo
`Extra` atemporal), Guerras Médicas (Batalha de Platéia), Sengoku Jidai
(exército, marinha, castelos), Império do Mali, Guerra de Inverno
finlandesa (1939-1940) e Exército Sassânida/Daylamitas. Introduziu **8
temas-raiz novos** sobreviventes à aprovação (`Guerra Romano-Seléucida`,
`Exército Sassânida`, `Império do Mali`, `Guerra de Inverno (1939-1940)`,
`Guerra do Iraque (2003)`, `Sociedade Romana`, `Comércio Romano`,
`Biblioteca de Alexandria`) e **11 subtemas novos**, nenhuma região nova
(`Norte da África`, já existente, usada pela primeira vez para este canal;
`Rússia` por aproximação para a Finlândia, sem termo próprio na Lista B).
Confiança abaixo da média histórica do catálogo (24% alta, 26% média, 36%
chute, 14% n/a). Fact-check da parada verificou 4 datações de maior risco
(Mons Graupius, fundação do Mali/Batalha de Kirina, Império Sassânida,
cronologia da Terceira Guerra Púnica) — todas bateram, nenhuma correção de
fato necessária. **3 correções na aprovação**: dois temas-raiz propostos
eram duplicatas não detectadas antes de propor o termo — `Gladiadores
Romanos` fundido em `Gladiadores` (Kings and Generals) e `Besteiros
Genoveses` fundido em `Balestreiros Genoveses` (SandRhoman History, mesmo
vídeo em essência — título em inglês idêntico "Genoese Crossbowmen"), essa
última linha também com um bug de sinal no `ano_inicio` (-1000 em vez de
1000 d.C.) corrigido junto; mais um rebaixamento de `alta` para `média` (fim
de faixa não evidenciado na própria linha, só na Parte 1 da série). **Nova
lição registrada no `protocolo.md`, "Armadilhas conhecidas":** buscar
sinônimos/traduções alternativas na Lista C inteira do vocabulário — não só
no ciclo em andamento — antes de propor qualquer tema-raiz novo. Pendências
de vocabulário deixadas em aberto, não bloqueantes: adjacência `Guerra
Romano-Seléucida`/`Guerras Sírias` (nomes parecidos, conflitos diferentes);
adjacência `Exército Sassânida`/`Império Sassânida` (mantida separada por
analogia a `Império Romano`/`Exército Romano`); subtema `Fronteiras do
Império`, genérico demais, criado para um vídeo com evidência truncada —
ver `vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`, campo `observacoes`.

**Epic History encerrado em 07/08/2026, esgotamento real confirmado por uma
coleta seguinte com 0 vídeos novos em 353 percorridos** (o lote 171 já
tinha vindo como mini-lote de 21, sinal de esgotamento próximo). Total:
**96 linhas em 4 lotes (168-171)**, todas aprovadas e travadas em ciclo
único (parada e aprovação em 07/08/2026, sem pendência cross-ciclo). Canal
generalista de documentários narrados em inglês, sem série/curso contínuo
amarrando os lotes (mesmo padrão do HistoryMarche): Guerras Napoleônicas (o
maior bloco, praticamente toda a linha do tempo 1793-1815 batalha a
batalha), Napoleão Bonaparte, Império Bizantino (série completa de 6 partes
sobre Belisário sob Justiniano), Alexandre o Grande, Cruzadas, Primeira
Guerra Mundial (série ano-a-ano 1914-1918), Guerra Civil Russa/Revolução
Russa, e tópicos avulsos (Programa Apollo, Francis Drake, Blackbeard,
República de Veneza, Castelos Medievais, China Moderna). Introduziu **7
temas-raiz novos** (`China Moderna`, `Programa Apollo`, `Castelos
Medievais`, `República de Veneza`, `Francis Drake`, `História da Rússia`,
`Blackbeard`) e **5 subtemas novos** (`Campanha do Egito` e `Campanha da
Itália` sob `Napoleão Bonaparte`; `Alexander Kolchak` sob `Guerra Civil
Russa`; `Marechais de Napoleão` sob `Guerras Napoleônicas`; `Decembristas`
sob `Revolução Russa de 1905`), nenhuma região nova. Confiança mais baixa
que a média histórica do catálogo (36% alta, 36% média, 25% chute, 2%
n/a) — documentários recentes (2018-2025) quase sempre narram data
explícita em prosa própria, mas material institucional/atemporal e séries
mais antigas sem parágrafo narrativo próprio não têm nenhum número na
descrição. Fact-check da parada confirmou a cronologia inteira dos 6
episódios do Belisário (100% chute, reconstruída da numeração da série) e
as datas-âncora de `República de Veneza`, `Francis Drake` e `História da
Rússia` contra fontes externas — nenhuma correção necessária. 7
rebaixamentos de `alta` para `média` feitos antes da gravação (número só em
título ou citação bibliográfica, não narrando o evento no corpo do texto).
Pendências de vocabulário deixadas em aberto, não bloqueantes: `História da
Rússia` (novo) se sobrepõe em conteúdo — não em formato — com `Revolução
Russa de 1905`/`Revolução Russa de 1917`, já existentes; `China Moderna`
(novo) é adjacente a `Dinastia Qing`/`Guerras do Ópio`, já existentes — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`, campo `observacoes`.

**History with Cy encerrado em 07/08/2026, esgotamento real confirmado por
uma coleta seguinte com 0 vídeos novos em 255 percorridos.** Total: **225
linhas em 9 lotes (159-167)**, todas aprovadas e travadas. Primeiro canal
do catálogo dedicado ao Antigo Oriente Próximo em profundidade (Suméria,
Acádia, Assíria, Babilônia, Elam, Mitani, Hititas) e ao Egito pré-clássico
dinastia por dinastia (Período Pré-dinástico ao Período Tardio), com
incursões em Pérsia aquemênida, Grécia pré-helenística, Levante/Canaã,
fenícios, e periferias do Oriente Próximo (lícios, arameus, medas, hititas
neo, cipriotas, urarteus, Ebla, Çatalhöyük). Três ciclos de parada
completos (159-162, 163-166) mais um ciclo parcial fechado por esgotamento
no meio (167, único lote do ciclo 167-170). Introduziu dezenas de
temas-raiz novos ao longo do canal — ver `vocabulario-canonico.md`, "Estado
atual", para o detalhamento por ciclo. **Dois casos de fusão de tema
notáveis**: na aprovação dos lotes 159-162, `Fenícia Antiga` (proposto) foi
identificado como duplicata de `Civilização Fenícia` (já existente, canal
The Histories) e fundido; na aprovação dos lotes 163-166, `Reinos de
Israel e Judá` (proposto) foi identificado como duplicata de `Canaã Antiga
> Reinos da Idade do Ferro` (duas séries diferentes do mesmo canal sobre o
mesmo assunto) e fundido — ambos reforçam a lição de checar o vocabulário
do próprio ciclo em andamento, não só a Lista C já consolidada, antes de
propor tema novo. Confiança mais baixa que a média histórica do catálogo
(61% `chute`), concentrada no material mais antigo do canal (2018-2022),
que raramente tem data na descrição/capítulos; a evidência melhora nos
vídeos mais recentes (2023-2026). Fact-check cobriu pelo menos 17 datações
de risco ao longo dos três ciclos, com apenas 2 pequenas correções de faixa
(Ebla, Çatalhöyük — ambas na ponta final, dentro da margem normal de
incerteza pré-histórica) — nenhum erro grave de classificação encontrado.
Pendências de vocabulário deixadas em aberto, não bloqueantes: adjacência
`Kish`/`Império Acadiano` e `Jiroft`/`Elam Antigo`; zona cinzenta
`Mari`/`Período Paleobabilônico`; par `Exército Assírio`/`Panorama Assírio
(curso)` com faixas quase idênticas; cluster de nomes parecidos em torno de
"Idade das Trevas"; família de temas Extra atemporais sobre a
Mesopotâmia/Egito; cluster `Dilmun`/`Magan` — ver `vocabulario-canonico.md`,
"Sobreposições ainda por resolver". Detalhes completos em `canais.json`,
campo `observacoes`.

**History with Cy fechou o segundo ciclo com 100 linhas em 4 lotes
(163-166), aprovado em 07/08/2026 com parada completa — canal segue `em
andamento`, sem sinal de esgotamento (lote 166 veio cheio, 250 vídeos
percorridos).** Ciclo cobriu majoritariamente o material mais antigo do
canal (2019-2022): biografias curtas de reis/dinastias mesopotâmicas, a
série em partes "The Epic of Ancient Assyria Podcast", "Ancient Egypt
Dynasty by Dynasty" e "History of Ancient Canaan", além de povos/reinos
periféricos do Antigo Oriente Próximo (lícios, arameus, medas, hititas neo,
cipriotas, urarteus) e incursões na Grécia arcaica e na Índia védica.
Introduziu **19 temas-raiz novos**: `Lícia Antiga`, `Numismática Antiga`
(Extra), `Reino de Yamhad`, `Civilização do Oxus (BMAC)`, `Ugarit`, `Guerra
Lelantina`, `Atenas Antiga`, `Dilmun`, `Estados Neo-Hititas`, `Império
Meda`, `Arameus`, `Cartas de Amarna`, `Reino de Urartu`, `Reino de Aksum`,
`Reinos de Chipre`, `Reino de Anitta (Precursor Hitita)`, `Civilização de
Jiroft`, `Confederação Xiongnu` — mais 1 tema proposto na classificação
(`Reinos de Israel e Judá`) que a parada identificou como duplicata de
`Canaã Antiga > Reinos da Idade do Ferro` (mesmo assunto, duas séries
diferentes do canal) e fundiu na aprovação. Mais **25 subtemas novos**, com
destaque para a cadeia cronológica completa da série "History of Ancient
Canaan" dentro de `Canaã Antiga` (Jericó e o Bronze Antigo → Idade de Ouro
Cananeia → Domínio Egípcio → Reinos da Idade do Ferro). Nenhuma região
nova. Confiança bem mais baixa que os ciclos anteriores do canal (12%
`alta`, 6% `média`, 71% `chute`, 11% `n/a`): o material mais antigo do
canal raramente tem data na descrição/capítulos. Fact-check de 6 datações
`chute`/inferidas de maior risco confirmou todas as 6 (Shulgi de Ur,
Ur-Nammu, Anitta de Kussara, Idrimi de Alalakh, Reino de Aksum, civilização
Tolteca) — nenhuma correção necessária. Pendências de vocabulário deixadas
em aberto, não bloqueantes: par `Exército Assírio`/`Panorama Assírio
(curso)` com faixas quase idênticas; adjacência `Civilização de
Jiroft`/`Elam Antigo`; cluster `Dilmun`/`Magan` — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`, campo `observacoes`.

**History with Cy fechou o primeiro ciclo com 100 linhas em 4 lotes
(159-162), aprovado em 07/08/2026 com parada completa — canal segue `em
andamento`, sem sinal de esgotamento.** Primeiro canal do catálogo dedicado
ao Antigo Oriente Próximo em profundidade (Suméria, Acádia, Assíria,
Babilônia, Elam) e ao Egito pré-clássico dinastia por dinastia (do Período
Pré-dinástico ao Período Tardio), com incursões em Pérsia aquemênida, Grécia
pré-helenística (Neolítico, Cíclades, Micênicos, Guerras Médicas, Guerra do
Peloponeso) e fenícios/cananeus do Levante. Introduziu **13 temas-raiz
novos**: `Suméria Antiga`, `Assíria Antiga`, `Babilônia Antiga`, `Elam
Antigo`, `Império Acadiano`, `Canaã Antiga`, `Delfos`, `Cultura Cicládica`,
`Povos do Zagros`, `Sociedade Mesopotâmica` e `Sociedade Egípcia Antiga`
(os dois últimos, `Extra`) — mais 1 tema proposto na classificação
(`Fenícia Antiga`) que a parada identificou como duplicata de `Civilização
Fenícia` (já existente, canal The Histories) e fundiu na aprovação, com as
3 linhas migradas como subtemas novos (Biblos/Tiro/Sidon). Mais **28
subtemas novos**, a maioria formando a periodização completa da egiptologia
dentro de `Egito antigo` (10 subtemas: Pré-dinástico → Dinastia 0 →
Dinástico Arcaico → Reino Antigo → Primeiro Período Intermediário → Reino
Médio → Segundo Período Intermediário → Reino Novo → Terceiro Período
Intermediário → Período Tardio) e a cadeia da Segunda Guerra Médica dentro
de `Guerras Médicas` (Revolta da Jônia → Primeira Invasão Persa/Maratona →
Invasão de Xerxes). Nenhuma região nova — todo o conteúdo mesopotâmico coube
em `Oriente Médio` por aproximação, sem termo próprio de "Mesopotâmia" na
Lista B ainda. Confiança mais baixa que a média histórica do catálogo (20%
`alta`, 26% `média`, 43% `chute`, 11% `n/a`): os vídeos mais antigos do canal
(2022-2023, formato "Dynasty by Dynasty" e cidades mesopotâmicas avulsas)
raramente citam data numérica na descrição ou nos capítulos. Fact-check de 6
datações `chute` de maior risco confirmou todas as 6 (Gudea de Lagash,
destruição de Mari, destruição de Hasanlu, fundação de Pasárgada, período
Cicládico Antigo, os dois candidatos aos Jardins Suspensos). **Nenhuma
correção de confiança `alta` na aprovação**, mas a armadilha "número real
citado no bloco 'Related Videos:' da descrição, mas descrevendo outro
vídeo" apareceu 3 vezes (Pasárgada, Peloponnesian War Parte I, Esparta/
Guerras Messênias) — nova lição registrada no `protocolo.md`, "Armadilhas
conhecidas". Pendências de vocabulário deixadas em aberto, não bloqueantes:
adjacência `Suméria Antiga > Kish`/`Império Acadiano`; zona cinzenta
`Babilônia Antiga > Mari`/`Período Paleobabilônico`; cluster de nomes
parecidos em torno de "Idade das Trevas" (três assuntos diferentes); família
de temas Extra atemporais sobre a Mesopotâmia (`Sociedade Mesopotâmica` vs
`Comércio na Mesopotâmia Antiga`) — ver `vocabulario-canonico.md`,
"Sobreposições ainda por resolver". Detalhes completos em `canais.json`,
campo `observacoes`.

**HistoryMarche fechou o primeiro ciclo com 100 linhas em 4 lotes
(149-152), aprovado em 03/08/2026 com parada completa — canal segue `em
andamento`, sem sinal de esgotamento.** Primeiro canal do catálogo sem
série/curso contínuo amarrando os lotes: cada vídeo é uma batalha isolada,
de qualquer época (547 a.C. a 1745 até agora) e qualquer região (Pérsia,
Escócia, Bizâncio, Roma republicana, Alemanha, Ucrânia...). Introduziu **15
temas-raiz novos** — o maior número desde a adoção do Ancient Americas:
`Guerra dos Nove Anos`, `Guerra Escocesa-Norueguesa`, `Polônia Piasta`,
`Guerra Dano-Hanseática`, `Guerra Franco-Holandesa`, `Levante de
Khmelnytsky`, `Guerra Franco-Flamenga`, `Invasões Magiares`, `Rebelião
Percy (1403)`, `Guerra Otomano-Valáquia`, `Guerras Sírias`, `Cruzada de
Marrocos (1578)`, `Guerras de Independência Suíça`, `Crise de 1383-1385` e
`Guerra Escaniana`; mais 1 subtema novo (`Guerra Cimbria`, 113-101 a.C.,
sob `República Romana`) e 1 região nova (`Dinamarca`, promovida de
aproximação `Suécia` depois do 3º uso). Confiança bem mais baixa que a
média histórica do catálogo (28% `alta`, 68% `média`, 4% `chute`): o canal
quase sempre põe o ano exato no título, mas raramente narra o evento na
própria descrição (mais comum: lista de vídeos relacionados e
bibliografia) — não passa no teste "capítulos ou descrição narram o
evento com número próprio" para `alta`. Fact-check de 4 datações `chute`
confirmou todas as 4. **1 correção na aprovação**: `Battle of Tolbiac, 496`
rebaixado de `alta` para `média` — a própria fonte hedgeia entre 496 e 506.
**2 lições novas no `protocolo.md`, "Armadilhas conhecidas"**: uma frase da
descrição que só reafirma o título (ex.: "I'm happy to share the Battle of
X with you") não sustenta `alta`, mesmo tendo um ano dentro dela; e a faixa
de uma compilação "ALL PARTS" sem nenhuma data pode ser reconstruída
cruzando com episódios vizinhos já catalogados, mas continua `chute`, não
sobe para `média`. Pendências de vocabulário deixadas em aberto, não
bloqueantes — ver `vocabulario-canonico.md`, "Sobreposições ainda por
resolver": subtema `Cercos de Viena` reaproveitado para uma batalha
adjacente (Párkány, 1683); região `Turquia` para `Basílio II`/`Dinastia
Comnena` aplicada também a campanhas nos Bálcãs, não só à biografia de
corte; granularidade de região inconsistente entre `Guerra
Franco-Flamenga` (`Países Baixos`) e temas vizinhos da mesma geografia
(`Europa Ocidental`). Detalhes completos em `canais.json`, campo
`observacoes`.

**HistoryMarche continuou com mais 100 linhas em 4 lotes (153-156),
aprovados em 03/08/2026 — canal segue `em andamento`, lote 157 já coletado
e classificado, aguardando a próxima parada.** Introduziu **8 temas-raiz
novos** (`Guerra Jacobita na Irlanda`, `Querela das Investiduras`,
`Primeiro Império Búlgaro`, `Sultanato de Delhi`, `Dinastia Tang`,
`Guerras do Decão`, `Império Marata`, `Império Gurida`) e as **primeiras 2
linhas `Extra` do canal**. Confiança mais baixa que a média do canal (20%
`alta`, 61% `média`, 17% `chute`) por causa de dois lotes (154-155) da fase
mais antiga (2019-2022), formato "explicador" sem data própria na
descrição — mas o fact-check de 5 datações `chute` de maior risco confirmou
todas as 5, incluindo um caso em que até o **assunto** do vídeo (não só a
data) teve que ser inferido das tags (ver `protocolo.md`, "Armadilhas
conhecidas"). Nenhuma correção na aprovação. **2 pendências cross-ciclo**,
sobre linhas já travadas de lotes anteriores, aguardando autorização
explícita antes de corrigir: `TbVfFq16gK8` (lote 152) pode ter identificado
a batalha errada dentro da série "Basil II" do canal; a compilação
"Hannibal PARTS 18-20" (lote 151) pode ter o início da faixa um ano
adiantado. Detalhes completos em `canais.json`, campo `observacoes`.

**HistoryMarche fechou o ciclo 157-158 (45 linhas) por esgotamento real,
não por completar 4 lotes** — o lote 158 já tinha vindo como mini-lote de
20 vídeos, e uma coleta seguinte confirmou 0 vídeos novos em 373
percorridos. Total do canal: **245 linhas em 10 lotes (149-158)**, todas
aprovadas e travadas. Introduziu mais **4 temas-raiz** neste ciclo final:
`Segundo Império Búlgaro`, `Miguel, o Bravo`, `Ditmársia` e `Moldávia de
Estêvão, o Grande` — os três últimos formam, junto com `Guerra
Otomano-Valáquia` (já existente), um cluster de principados romenos/
moldavos distintos mas com nomes parecidos, região `Bálcãs` nos quatro.
Fact-check de 3 datações de maior risco confirmou todas as 3. Praticamente
toda a série numerada "Hannibal" do canal (Partes 1-23) ficou coberta.
**Canal `encerrado` em 03/08/2026** — as 2 pendências cross-ciclo já
registradas (`TbVfFq16gK8`; faixa de "Hannibal PARTS 18-20") seguem sem
correção, aguardando autorização explícita do humano. Detalhes completos
em `canais.json`, campo `observacoes`.

**Ryan M Reeves fechou com 195 linhas em 8 lotes (141-148)** — esgotamento
real, confirmado com uma coleta seguinte retornando 0 vídeos novos nos
mesmos 210 percorridos (o lote 148 já tinha vindo como mini-lote de 20,
sinal de esgotamento próximo). Professor de teologia histórica
(Gordon-Conwell), cobrindo Padres da Igreja, concílios cristológicos,
Escolástica medieval, a Reforma protestante e católica, o cristianismo
americano moderno (Grandes Despertares a Pentecostalismo), e uma extensa
série sobre C.S. Lewis/J.R.R. Tolkien e os Inklings. Introduziu **12
temas-raiz novos** ao longo de dois ciclos de parada completos (141-144,
145-148): `Reforma Protestante` (ganhou massa, mais de 50 vídeos),
`História do Cristianismo Moderno` (criado como "Cristianismo Americano
Moderno" no lote 142, renomeado no lote 143), `Escolástica Medieval`,
`História dos Feriados`, `História da Arte`, `História da Bíblia`, `Credos
e Confissões Cristãs`, `Caça às Bruxas`, `Revolução Científica`,
`Pseudociência e Conspirações`, `Teologia Cristã` (bucket `Aleatório` para
explicadores doutrinários sem período histórico) e `Inklings (Lewis e
Tolkien)` (só biografia real de Lewis/Tolkien — as 15 análises literárias
de ficção deles foram `Extra`, tema `História na cultura popular` de outro
canal). Mais de 100 subtemas novos ao todo — detalhes em
`vocabulario-canonico.md`, "Estado atual". Fact-check de 14 datações `chute`
de maior risco ao longo dos dois ciclos: todas confirmadas por busca
externa, nenhuma correção necessária. **2 reuploads confirmados** no
segundo ciclo (`IXpX1Gy4vYA`/`Sjy23bJdLQg`, `7LDJiCtGuxA`/`JF3t3Xx4s5A`) —
ver `protocolo.md`, "Armadilhas conhecidas", para o risco de copiar a faixa
do par sem reavaliação independente. 1 correção na aprovação do primeiro
ciclo: Notre Dame de Paris saiu de `Vida urbana > Paris` para `Geografia
Estratégica > Notre-Dame de Paris` (mesma armadilha do Xi'an/
GatesOfKilikien). Pendências de vocabulário deixadas em aberto, não
bloqueantes: `Puritanismo` espalhado em três temas-raiz diferentes; `Reforma
Católica (Contrarreforma)` aninhado dentro de `Reforma Protestante`;
catolicismo institucional dividido entre `Papado` e `Reforma Protestante`;
`Pano de Fundo Medieval da Reforma`/`Indulgências` com faixa idêntica;
`John Wycliffe`/`Jan Hus` como precursores tratados separadamente;
`Sociedade Medieval` com 5 vídeos de faixa idêntica — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver".

**Magistra Vitae fechou com 40 linhas em 2 lotes (139-140)** — esgotamento
real, confirmado com uma coleta seguinte retornando 0 vídeos novos nos
mesmos 46 percorridos. Primeiro canal do catálogo dedicado a Roma
pré-imperial (Reino de Roma, início da República — Conflito das Ordens,
Guerra contra Veios, Guerras Samnitas/Latina, Guerra Pírrica — e as duas
Guerras Púnicas), com incursões em Grécia arcaica/clássica e Egito antigo
em formato de panorama de longa duração. Nenhum tema-raiz novo — tudo coube
em `Reino de Roma`, `República Romana` e `Cartago antiga`, já existentes.
Introduziu **8 subtemas novos**, nenhuma região nova. Sem parada formal de
quatro lotes (só 2 lotes ao todo); revisão rodou sobre a janela real na
aprovação de 03/08/2026, sem correções — 40/40 linhas `ok`, nenhuma
`revisar` ao encerrar. Confirmado um **padrão de reupload por
recombinação** (variante nova do reupload já visto em outros canais): a
série antiga do canal divide o Reino de Roma em dois vídeos (`Founding of
Rome [OLD] #1` + `Seven Kings of Rome #2`), a série nova compila o mesmo
conteúdo em corte diferente (`Founding of Rome` + `Seven Legendary Kings of
Rome`) — ver `protocolo.md`, "Armadilhas conhecidas". Pendência de
vocabulário deixada em aberto, não bloqueante: linha `Interbellum` (lote
139) sem subtema próprio dentro de `Segunda Guerra Púnica`, sendo na
verdade sobre o intervalo ENTRE a Primeira e a Segunda Guerra Púnica — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver". Detalhes
completos em `canais.json`, campo `observacoes`.

**Revolutions (Mike Duncan) fechou com 350 linhas em 14 lotes (125-138)** —
esgotamento real, confirmado com duas coletas seguidas retornando 0 vídeos
novos nos mesmos 350 percorridos. Mesmo padrão do History of Rome: não é um
canal do YouTube, é uma playlist específica (`--playlist
PLIjP3HEQ0F-8B6x_9l4bJef2q4hFvb9s0`), hospedada num canal sem relação com
história (`@Seaquences`) — resolvida via `--nome "Revolutions (Mike Duncan)"`
na adoção, seguindo `resolver_playlist_explicita()` do `coletar.py`. É o
podcast sequência de The History of Rome, mesmo autor. Quatro ciclos
aprovados: **125-128** (fim da Guerra Civil Inglesa/Interregno, Revolução
Americana inteira, Revolução Francesa até o Diretório/Napoleão — introduziu
`Revolução Francesa` e os subtemas de sua periodização padrão de livro-texto:
`Queda da Monarquia`, `O Terror`, `Reação Termidoriana`, `Diretório`);
**129-132** (Revolução Haitiana inteira, Guerras de Independência
Hispano-Americanas, Revoluções de 1830 e 1848, início da Comuna de Paris —
introduziu região `Haiti` e os temas-raiz de cada uma dessas revoluções);
**133-135** (fim da Comuna de Paris, Season 9 inteira — Revolução Mexicana,
Nova Espanha 1521 até o Maximato 1940 — e início da Season 10 — a Revolução
Russa propriamente dita, do pano de fundo ideológico ao pós-1905); e
**136-138**, o ciclo final, de 3 lotes só porque o canal esgotou no meio
(mesmo padrão de Cambrian Chronicles/SandRhoman/The Histories/GatesOfKilikien)
— o resto da Season 10 (1917 inteiro, do prelúdio ao Caso Kornilov, Revolução
de Outubro, Guerra Civil Russa, fundação da URSS e luta pela sucessão de
Lenin até ~1930) e o encerramento inteiro do podcast (série de apêndices
teóricos comparando as dez temporadas, episódio de despedida, e uma
mini-season fictícia posterior de quase um ano, "Martian Revolution",
publicada em nov/2024). Introduziu **5 temas-raiz novos** (`Revolução Russa
de 1917`, `União Soviética`, `Revolução Alemã`, `Teoria da Revolução`/Extra,
`Revolução Marciana (ficção)`/Aleatório) e 7 subtemas novos, nenhuma região
nova. Fact-check de 6 datações `chute` de maior risco: todas as 6
confirmadas por busca externa, nenhuma correção necessária. Todos os quatro
ciclos passaram por parada + fact-check + aprovação; nenhum termo pendente
no momento — mas 3 pontos de vocabulário ficaram registrados como
pendência aberta (não bloqueante) no `vocabulario-canonico.md`, "Sobreposições
ainda por resolver": a cadeia de quatro temas-raiz sequenciais para o mesmo
arco 1905-1932, o subtema `Frente Oriental` repetido em dois temas
diferentes (1ª e 2ª Guerra Mundial), e `Guerra Polaco-Soviética` como
subtema vs. tema-raiz próprio. **Achado da parada 133-135, vale para
qualquer canal em múltiplos lotes:** o lote 134 criou o tema `Revolução
Russa` e o lote 135, numa conversa separada, criou por engano um segundo
tema `Revolução Russa de 1905` para o mesmo arco contínuo (10.1-10.46, sem
checar o `canais.json` do lote anterior) — fundidos na aprovação.
**Padrão de reupload confirmado** (mesmo já visto no History of Byzantium
Podcast): pelo menos 2 pares de episódios com o mesmo número/título mas
`video_id` diferente (`2.9 Valley Forge`, `3.10 Tennis Court Oath`), com
nota do próprio uploader explicando o reupload — não é bug de dedup.
Detalhes completos em `canais.json`, campo `observacoes`.

**GatesOfKilikien fechou com 29 linhas em 2 lotes (123-124)** — o canal
esgotou a própria coleta: o lote 124 já tinha vindo com só 4 vídeos novos (29
percorridos, a maioria já conhecida), e uma terceira coleta confirmou 0
vídeos novos nos mesmos 29, fechando por esgotamento real. **Primeiro canal
do catálogo dedicado à China antiga/medieval** (dinastias Zhou, Han, Jin,
Dezesseis Reinos, Três Reinos) — trouxe também um formato recorrente de
ensaio atemporal "este lugar através da história" (Bósforo, Xiangyang,
Xuzhou, geografia chinesa em geral, Grande Muralha, divisor Norte-Sul),
aplicado uma vez também à Grécia (Peloponeso). Introduziu **6 temas-raiz
novos e 5 subtemas novos** (`Dinastia Zhou`, `Dinastia Jin`, `Dezesseis
Reinos`, `Grande Canal da China`, `Geografia Estratégica`, `Curiosidades da
História Chinesa`; subtemas `Período dos Três Reinos > Ascensão de Cao Cao`,
`Dinastia Han > Han Ocidental`/`Han Oriental`, `Império Romano > Hispania
Romana`), nenhuma região nova. Sem parada de quatro lotes completa (só havia
2 lotes desde a última parada, que fechou The Histories) — a parada rodou
sobre a janela real de 29 linhas. 2 correções na aprovação: `Xi'an
(Chang'an)` Partes 1 e 2 saíram de `Vida urbana > Chang'an` para `Geografia
Estratégica` (formato de ensaio panorâmico de 800+ anos, não a fatia estreita
de época que o resto de `Vida urbana` usa — ver `protocolo.md`, "Armadilhas
conhecidas"); confiança rebaixada de `alta` para `média` em 2 linhas (só uma
ponta da faixa tinha número exato). Achado à parte: a descrição de "Ancient
Greece - The Peloponnese" citava "300 (2006)", o ano do filme, não uma data
histórica. Pendências de vocabulário deixadas em aberto: `China antiga`
(existente, outro canal) vs. `Dinastia Zhou` (novo, ainda não comparados); 2
vídeos antigos de `Dinastia Han` continuam sem subtema, travados. Detalhes
completos em `canais.json`, campo `observacoes`.

**The Histories fechou com 21 linhas em 1 lote só (122)** — o canal só tem
21 vídeos longos publicados no total; a primeira coleta já trouxe tudo, e
uma segunda coleta confirmou 0 vídeos novos nos mesmos 21, fechando por
esgotamento real. Canal inteiramente no formato "Who were the X?" — uma
etnografia de povo antigo por vídeo (Micênicos, Minoicos, Gauleses, Partos,
Etruscos, Hunos, Godos, Lídios, Hititas, Vândalos, Filisteus, Cátaros,
Fenícios, Pictos, Suevos, Pechenegues, Icenos), mais uma mini-série "Lost
Expeditions" (Alexandre na Gedrósia; expedição espanhola de Pánfilo de
Narváez) e dois vídeos avulsos (evolução de Constantinopla; Hereward the
Wake). Introduziu **12 temas-raiz novos e 2 subtemas novos** num lote só —
o maior número de temas-raiz de um lote único (não ciclo de quatro) desde a
adoção de qualquer canal novo neste catálogo — e nenhuma região nova. Único
canal até agora sem nenhuma linha `Extra`/`Aleatório`: as 21 linhas ficaram
todas na linha do tempo, esperado pelo formato uniforme do canal (sem
resenha, aviso de canal ou vídeo de reação). Sem parada de quatro lotes
completa (só havia 1 lote desde a última parada, que fechou o Shogunate) —
a parada rodou sobre a janela real de 21 linhas. 4 datações `chute`
corrigidas por fact-check na aprovação (Minoicos, Fenícios, Pechenegues,
Pictos — todas no ano de **início**, nenhuma no fim; ver `protocolo.md`,
"Armadilhas conhecidas", para a lição sobre esse padrão). Pendências de
vocabulário deixadas em aberto: `Vândalos` vs. `Reino Vândalo` (já
existente); `Cátaros` vs. `Cruzadas > Cruzada Albigense` (já existente);
região `Judeia` usada por aproximação para os Filisteus é a mais frágil já
registrada (filisteus e judeus eram povos rivais, não o mesmo). Detalhes
completos em `canais.json`, campo `observacoes`.

**The Shogunate fechou com 285 linhas em 12 lotes (110-121)** — o lote 121
já tinha vindo como mini-lote de 10 vídeos (304 percorridos), e a coleta
seguinte confirmou 0 vídeos novos nos mesmos 304, fechando o canal por
esgotamento real da coleta, não abandono no meio. Canal de história
pré-moderna do Japão (samurai/xogunato): introduziu **17 temas-raiz novos e
5 subtemas novos** ao longo de três ciclos de parada completos (110-112,
113-116, 117-121), nenhuma região nova, e foi o primeiro canal a
reaproveitar um tema criado por outro canal (`Resenhas de ficção`, do
Thersites the Historian). Achado central: o canal tem uma série numerada
própria chamada "Sengoku Jidai" (mesmo nome do tema já existente na Lista C)
cobrindo o período inteiro episódio a episódio, catalogada do Episódio 1
(2019) ao Episódio 64 (FINALE) — mais a sub-série "Guerra Imjin" (5 partes)
e 8 vídeos "(OUTDATED)" da série antiga "Setting the Stage", mapeados 1:1
para a versão "UPDATED" já catalogada (mesmo padrão de reupload/refação já
visto no History of Byzantium Podcast). Cerca de metade do canal não é
história — cultura material samurai, resenha de jogo/filme/livro,
entrevista, aviso de canal e ranking cross-era ficaram `Aleatório`/`Extra`
o canal inteiro (48%, 49% e 64% das linhas na linha do tempo em cada
ciclo). Pendências de vocabulário deixadas em aberto, sem correção
retroativa: `Sakoku` (tema-raiz já existente, Kings and Generals) vs.
subtema `Período Edo`; três temas `Jogos de X` sem critério fechado de
fronteira; `Clãs do Sengoku` heterogêneo demais (24 vídeos, nome pode
precisar virar "Daimyos e clãs do Sengoku"); `Ranking de samurais` vs.
`Últimas Resistências Samurai` (mesmo formato de clipshow cross-era em dois
temas); `Xogunato do Japão` vs. `Família Imperial do Japão`. Detalhes
completos em `canais.json`, campo `observacoes`.

**SandRhoman History fechou com 153 linhas em 7 lotes (103-109)** — mini-lote
final de 3 vídeos no lote 109, seguido de uma coleta que retornou 0 vídeos
novos em 153 percorridos, confirmando o esgotamento. Canal de história
militar pré-moderna muito institucional/granular: introduziu **26 temas-raiz
novos e 2 regiões novas** (`Países Baixos`, `Hungria`) em sete lotes — o maior
salto de vocabulário de um canal só desde o Ancient Americas. A Guerra dos
Trinta Anos ganhou a periodização historiográfica padrão completa (Fase
Boêmia, Fase Dinamarquesa, Intervenção Sueca, Fase Francesa, Guerra de
Sucessão de Mântua). Encerrado **sem parada formal** sobre os lotes 107-109
(só havia 3 lotes desde a última parada, feita nos 103-106) — fact-check
pontual no encerramento corrigiu uma faixa errada (Guerras Hussitas, ver
`protocolo.md`). **A Lista C do `vocabulario-canonico.md` só reflete até o
lote 106** — os temas/subtemas dos lotes 107-109 ainda não foram
incorporados; confira o campo `observacoes` do canal em `canais.json` antes
de propor um tema que pode já existir. Detalhes completos em `canais.json`.

**The History of Byzantium Podcast é o segundo maior canal do catálogo**
(394 linhas, 16 lotes) — fechou porque esgotou a própria coleta, chegando ao
Episódio 1 (2007), o primeiro do podcast inteiro. Introduziu 24 subtemas
formando uma cadeia dinástica cronológica sem lacuna de 457 a 1453 d.C., mais
uma família de 6 episódios de interlúdio ("O Império em 500/600/.../1025").
Achado recorrente que vale saber antes de revisitar: o canal reupou pelo
menos 8 pares de episódios com o mesmo número/título mas `video_id`
diferente — não é bug de dedup, são uploads reais distintos (ver
`protocolo.md`, "Armadilhas conhecidas"). Detalhes completos em
`canais.json`, campo `observacoes`.

**Cambrian Chronicles fechou com só 2 lotes (83-84, 38 linhas), não 4:** o
canal esgotou a coleta (58 vídeos percorridos, 0 novos) antes de completar um
quarto lote, e o humano decidiu aprovar o mini-ciclo em vez de esperar. A
parada formal não rodou — fact-check substituiu na aprovação. Detalhes em
`canais.json`, campo `observacoes`.

**The History of Rome (Mike Duncan) não é um canal do YouTube — é uma
playlist específica** (`coletar.py --playlist ID --nome "..."`, modo novo
desde este canal). Os 36 vídeos estão hospedados num canal (`- Timaeus -`)
com 225 vídeos sem relação nenhuma com história; coletar por playlist evita
esse ruído. A chave em `canais.json` é `playlist:<ID>`, não um `@handle` — ao
revisitar, use o mesmo comando com `--playlist`, sem precisar de `--nome` de
novo (o nome já está salvo). Fechou em mini-ciclo de 2 lotes (85-86, 36
linhas) porque a playlist inteira (36 itens) coube nisso — parada formal
rodou normalmente desta vez. Detalhes em `canais.json`, campo `observacoes`.

**Cuidado ao rodar `coletar.py` sem argumento:** a constante `CANAL` no topo
do script fica hardcoded e **não é atualizada automaticamente** a cada canal
adotado — hoje ainda aponta para `@AncientAmericas` (lote 77), bem atrás do
canal mais recente. Ela não segue sozinha o campo `em andamento` do
`canais.json`. Rodar sem `@Handle` explícito coleta do canal errado. Sempre
passe o handle (ou `--playlist ID`) na linha de comando ao adotar ou reabrir
um canal.

`catalogados.txt` e `descartados.txt` continuam compartilhados de propósito —
indexados por `video_id`, único no YouTube inteiro — e a numeração de lote
segue única entre todos os canais, para o catálogo continuar sendo uma linha
do tempo só. A coluna `Canal` da planilha é a chave de agrupamento; o nome
tem que bater exatamente com a chave `nome` de `canais.json`.

**Duas lições valem para qualquer canal novo, não só os três já encerrados:**

- **Live não entra**, mesma regra dos Shorts. O `coletar.py` filtra pela parte
  `liveStreamingDetails` da API — nunca usar `snippet.liveBroadcastContent`
  nem heurística de duração/título. Descoberto tarde no Thersites the
  Historian (202 linhas de live entraram nos lotes 40-56 antes do filtro
  existir; os buracos que isso deixou são permanentes, não recoletados).
- **Olhe uma amostra crua antes de classificar 25 linhas de um canal novo.**
  Os filtros que bastam para um canal podem deixar passar metade de outro.

Detalhes de cada canal encerrado (buracos em lotes, rótulos que ele
introduziu, séries longas, decisões de escopo) estão no campo `observacoes`
de cada um em `canais.json`, e no histórico de `protocolo.md`
("Armadilhas conhecidas") e `vocabulario-canonico.md` ("Estado atual").

## O loop (para um canal novo)

```
python coletar.py                      # gera lote-NN.md
                                       # classificar as 25 linhas
python verificar.py --anterior backups/playlist-AAAA-MM-DD.xlsx
                                       # só salvar se sair 0
```

A cada quatro lotes, uma parada: validação de vocabulário, fact-check por amostra
e **cinco linhas sorteadas apresentadas ao humano** com a evidência ao lado.
Essa amostra não é opcional. É o único ponto em que alguém de fora olha o que foi
produzido — sem ela, quem classifica, valida e aprova é a mesma parte.

`coletar.py` já suporta múltiplos canais (aceita `@Handle` na linha de
comando, registra e atualiza `canais.json` sozinho) desde a adoção do
Thersites the Historian no lote 40 — nenhum ajuste extra é necessário para
adotar um canal novo.

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
completa sai na parada do quarto lote — não pare a rodada por causa disso.

**Só erro crítico interrompe.** A lista está no `protocolo.md`, seção "Rotina de
quatro lotes". Fora dela, acumula.

---

## Armadilhas com histórico neste projeto

Estão detalhadas no `protocolo.md`. As que mais reincidiram:

- **Descrição e tags recicladas entre episódios.** Canais repetem o mesmo bloco.
  Já apareceram tags de Vicksburg/1863 num vídeo de Atlanta/1864. **Capítulos
  ganham de tags e de descrição sempre que houver conflito.**
- **Desalinhamento de tupla ao montar linhas em lote.** Já custou 14 linhas sem
  `publicado`/`Título`, e mais 3 linhas apagadas durante a correção. Conte os
  campos de cada linha **antes** de montar a planilha, e confira o conjunto de
  ids contra o `lote-NN.md`.
- **Regex de data míope.** Já ignorou anos de três dígitos e `centuries` no
  plural. Todo padrão novo de data se testa contra a faixa inteira do catálogo,
  de 20000 a.C. a hoje (o limite mudou de 3300 a.C. na adoção do canal Ancient
  Americas, lote 77 — povoamento das Américas).
- **A fonte erra.** Quando o vídeo contradiz o fato conhecido, vale o fato, e a
  divergência vai para `notas`.

---

## Sem transcrições, sem contornos

Só a YouTube Data API oficial. Evidência = título, capítulos, descrição e tags.
Baixar legendas de terceiros exige OAuth do dono do vídeo; raspar o endpoint
interno viola os Termos de Serviço. Nunca usar cookies de conta logada nem proxy
para contornar bloqueio — troca um bloqueio de IP temporário por risco de
suspensão da conta.
