# Vocabulário canônico — playlist de história

A "constituição" do projeto: a IA só escolhe termos que estejam aqui. Quando nada
serve, propõe um termo novo em seção separada e o humano decide. Regenerado a
partir das 791 linhas de `playlist-historia-v2.xlsx` (lotes 0 a 29), na parada
dos lotes 26-29.

---

## Lista A — Período

**A Lista A vale para a v2, a camada de dado.** Para a ordem de exibição existe
agora a **Lista E — Eras**, mais abaixo: faixas largas, pelo ano de INÍCIO, sem
ponto médio. As duas coexistem de propósito — a v2 continua sendo a fonte de
verdade ordenada por `ano_inicio`, e a `playlist-historia-v3.xlsx` é derivada
dela pelo `ordenar.py`. Ver `protocolo.md`, "Duas camadas".

**Não é escolhida pela IA.** É calculada pelo Python a partir do **ponto médio**
entre `ano_inicio` e `ano_fim`. Testada contra as 155 linhas originais: reproduz
a classificação manual em 142 casos (92%).

| Faixa (ponto médio) | Rótulo |
|---|---|
| até 1100 a.C. | Antiguidade remota (até 1100 a.C.) |
| 1100 a.C. – 800 a.C. | Período homérico (1100 a.C. - 800 a.C.) |
| 800 a.C. – 500 a.C. | Época Arcaica (800 a.C. - 500 a.C.) |
| 500 a.C. – 250 a.C. | Apogeu Grego (500 a.C. - 250 a.C.) |
| 250 a.C. – 0 | Apogeu da República (250 a.C. - 0) |
| 0 – 250 | Apogeu Romano (0 - 250) |
| 250 – 500 | Antiguidade Tardia (250 - 500) |
| 500 – 1900 | séculos: `500 - 600`, `600 - 700`, … `1800 - 1900` |
| 1900 – 1925 | 1900 - 1925 |
| 1925 – 1950 | 1925 - 1950 |
| 1950 – 2000 | 1950 - 2000 |
| 2000 em diante | 2000+ |
| **faixa ≥ 300 anos** (não usa ponto médio) | **`Panorama (330 - 1453)`** |
| sem ano | Indefinido |
| é história, mas sem período fixável | Extra |
| **não é história** | **Aleatório** |

**A régua tem dois modos, e o gatilho é a largura da faixa** (parada dos lotes
30-33). A tabela acima vale para faixas de **menos de 300 anos** — 86% do
catálogo, 754 linhas. Faixa de 300 anos ou mais não passa pelo ponto médio:
mostra a própria faixa, no formato `Panorama (330 - 1453)`. O limiar está em
`LIMIAR_PANORAMA`, no `verificar.py`.

Motivo: o ponto médio de uma faixa larga não é um período, é aritmética. A
marinha bizantina (330–1453) caía em "800 - 900", como se fosse um vídeo sobre o
século IX; os Ilírios (1000 a.C.–600 d.C.) caíam em "Apogeu da República". O
rótulo apontava para um lugar que o vídeo mal encosta. Pior: como o rótulo saía
ruim, a saída fácil virou deixar os anos vazios — e a linha caía em `Extra`,
fora da linha do tempo. Era assim que 54 vídeos datáveis tinham ido parar lá.
Ver `protocolo.md`, "Extra virou balde".

**Por que os rótulos são grecorromanos — decisão consciente.** A Lista A é uma
**régua cronológica para o leitor se situar no tempo**, não uma descrição do
assunto do vídeo. Ela usa um único eixo de referência, e esse eixo é o
grecorromano. Por isso "What Tactics Did the Ancient Chinese Use?" (184–280)
aparece como "Apogeu Romano": o ponto médio cai ali, e a régua é a mesma para
todos, seja o assunto chinês, persa ou romano.

O que o vídeo **é** fica em `Tema` e `Região` — é lá que a interpretação
histórica acontece. Separar as duas coisas é o que permite ordenar o catálogo
inteiro numa linha do tempo só, de 3300 a.C. a hoje. Se cada região tivesse a sua
periodização, não haveria linha do tempo comum.

**Não "corrigir" isso em conversas futuras.** Rótulo que soa estranho para um
assunto não grecorromano é comportamento esperado, não bug. O degrau `Panorama`
**não** é exceção a isso: ele não existe para consertar incompatibilidade
cultural, e sim para faixa larga demais para ter ponto médio informativo. Um
assunto chinês de faixa estreita continua recebendo rótulo grecorromano, e está
certo assim.

**A ordenação não mudou.** A linha do tempo continua saindo de `ano_inicio`,
`ano_fim`, mês e dia — nunca do rótulo. `Panorama` altera o que se lê, não onde
a linha fica.

---

## Lista B — Região (60 termos)

Regra: a região que o vídeo cobre **por inteiro**. Se cobre várias, sobe um nível
(Inglaterra + França → Europa Ocidental). Se é global, `Global`.

**Europa**
Europa · Europa Ocidental · Leste Europeu · Bálcãs · Península Ibérica ·
Inglaterra · Escócia · Irlanda · Gales · França · Alemanha · Áustria · Itália · Rússia · Grécia ·
Turquia · Ucrânia · Suécia · Noruega · Países Baixos · Hungria · Suíça · Dinamarca

**Mediterrâneo e Oriente Médio**
Mediterrâneo · Oriente Médio · Judeia · Egito · Irã · Cáucaso · Iêmen

**Ásia**
Índia · China · Japão · Indonésia · Sudeste Asiático · Ásia Central · Taiwan ·
Coreia · Nepal

**Américas**
Estados Unidos · América do Norte · América do Sul · México · Peru ·
América Central · Brasil · Bolívia · Haiti · Caribe

**África**
Sudão · África Austral · África Ocidental · Norte da África · África Oriental

**Oceanos e Oceania**
Atlântico · Pacífico · Índico · Ártico · Melanésia

**Genérico**
Global

**Iêmen entrou na parada dos lotes 10-13** para o Reino Himiarita e a História do
Iêmen, que antes caíam em `Oriente Médio` por aproximação. `Iraque` (Califado
Abássida, Rebelião Zanje) e `Jordânia`/`Arábia` (Reino Nabateu, Anábase dos Dez
Mil) continuam em `Oriente Médio` por aproximação — só ganham termo próprio na
segunda ocorrência de cada um.

**Gales, Suécia e Noruega entraram na parada dos lotes 14-17** — três países que
nunca tinham aparecido. `Gales` para a História de Gales (antes não havia termo
para o País de Gales, só `Inglaterra`, que teria apagado o vídeo ser justamente
sobre a resistência galesa contra a Inglaterra). `Suécia` para a neutralidade
sueca na Segunda Guerra. `Noruega` para a sabotagem do programa nuclear alemão
(Operações Freshman/Gunnerside), que aconteceu lá, não na Alemanha.

**América do Sul, África Ocidental e Índico entraram na parada dos lotes 26-29.**
`América do Sul` para os conquistadores (espanhóis e alemães) na Venezuela —
antes só havia `Estados Unidos`/`América do Norte` nas Américas; pode precisar
virar `América Latina` se o canal cobrir também o México ou a América Central,
ainda sem termo próprio. `África Ocidental` para o Império do Mali/Mansa Musa —
antes só havia `Sudão` e `África Austral` na África. `Índico` (não "Oceano
Índico") para a incursão japonesa no Índico durante a Guerra do Pacífico —
nomeado assim para bater com o padrão enxuto das outras bacias oceânicas já na
lista (`Atlântico`, `Pacífico`, `Ártico`), corrigido do nome inicialmente
proposto ("Oceano Índico") na revisão humana da parada.

**Suíça entrou na parada dos lotes 141-144** (canal Ryan M Reeves) para o
ministério de João Calvino em Genebra e Heinrich Bullinger em Zurique — 6
vídeos caíam sem termo próprio (o mais próximo seria `Alemanha`, que teria
apagado o fato de a Reforma Suíça ser um ramo distinto da luterana alemã).

**Dinamarca entrou na aprovação dos lotes 149-152** (canal HistoryMarche).
Três vídeos sobre a Dinamarca medieval/moderna (`Visby 1361`, `Isefjord 986`,
`Lund 1676`) tinham caído em `Suécia` por aproximação — passou da terceira
ocorrência sem termo próprio (mesma regra usada para Iêmen, Gales e Norte da
África), e as três linhas foram corrigidas de `Suécia` para `Dinamarca` na
mesma aprovação.

**Caribe e África Oriental entraram na aprovação dos lotes 188-191** (canal
History of Philosophy Without Any Gaps Podcast, série HAP — Filosofia
Africana). `Caribe` para Sylvia Wynter, Édouard Glissant (×2) e Walter Rodney
(este último chamado de "Caribbean thinker" pela própria descrição do vídeo)
— antes só havia `Haiti`, país específico, sem termo que cobrisse a região
inteira (Jamaica, Martinica, Guiana). `África Oriental` para Ngũgĩ wa Thiong'o
(×2, Quênia) e Julius Nyerere (Tanzânia) — sem termo próprio para essa
sub-região da África até agora (só `Sudão`, `África Austral`, `África
Ocidental`, `Norte da África`).

**Norte da África entrou na parada dos lotes 30-33.** Gatilho: três vídeos
(`Impérios Berberes` × 2, `Beginning of Muslim Africa - Sufetula 647`) já
tinham caído em `Mediterrâneo` por aproximação — passou da segunda ocorrência
da mesma aproximação sem termo próprio (regra usada antes para Iêmen e
Iraque/Jordânia). Cobre Magrebe/Norte da África continental; não confundir com
`Egito`, que já tem termo próprio.

**Aproximações que seguem sem termo próprio, herdadas dos lotes 14-17:**
`Judaísmo` (judeus no califado islâmico primitivo, multi-regional) → `Oriente
Médio`; `Grupo Wagner` (Síria + vários países da África) → `Global`; `Colapso da
Idade do Bronze`/Povos do Mar (todo o Mediterrâneo oriental) → `Mediterrâneo`;
`Bretanha Antiga` (cobre também a Escócia nos capítulos) → `Inglaterra`;
`Guerra Civil Inglesa` (cobre também Irlanda — Drogheda — e Escócia — Dunbar,
Worcester) → `Inglaterra`.

**Aproximações novas dos lotes 18-21:** `Guerra Georgiano-Seljúcida` (Batalha de
Didgori, Geórgia) → `Cáucaso` (termo já existente, criado para os circassianos,
agora reaproveitado para a Geórgia — sem termo próprio ainda, ver "Sobreposições
ainda por resolver"); teatro China-Birmânia-Índia (CBI) da Guerra do Pacífico,
quando o vídeo cobre as três regiões sem detalhar → `Sudeste Asiático` (foco
birmanês dominante); Batalha das Ilhas Komandorski (geograficamente perto de
Kamchatka) → `Estados Unidos`, por extensão da convenção "Campanha das Aleutas
inteira usa Estados Unidos".

**Aproximações novas dos lotes 22-25:** `Reino da Armênia` e `Grande Guerra do
Norte` (teatro báltico) → `Cáucaso` e `Leste Europeu` respectivamente (sem
termos próprios); `Guerras Hussitas` (Boêmia) → `Leste Europeu`; bombardeio de
Darwin, ataque a Sydney (Austrália) e Raid em Makin Island (Ilhas Gilbert,
Micronésia) → `Pacífico`, três usos do mesmo aproximador para regiões sem
termo próprio na Lista B; "How the World Betrayed Ethiopia" → `Global` (o
vídeo foca na falha da Liga das Nações, não só na Etiópia).

**Escócia entrou na aprovação dos lotes 40-43.** Gatilho: a série "History of
Britain" do canal Thersites the Historian gerou dois vídeos seguidos sobre
reinos escoceses (`Reino de Strathclyde`, ep. XII, e `Reino da Escócia`, ep.
XI) — o primeiro tinha caído em `Inglaterra` por aproximação; passou da
segunda ocorrência sem termo próprio (mesma regra usada para Iêmen/Norte da
África) e a linha de Strathclyde foi corrigida para `Escócia` também.

**Aproximações que ganharam mais usos nos lotes 48-51, ainda sem termo
próprio:** `Bálcãs` para Macedônia/Ilírico (Gaius Antonius, lote 50; Marcus
Octavius, lote 48) chega a mais casos somados aos já registrados; `Norte da
África` para a campanha de Cúrio na Guerra Civil de César (Cornificius,
Lucius Julius Caesar, Quintus Marcius Rufus — lotes 48-49) — 3 usos só nesta
janela; `Oriente Médio` para a Síria (Sextus Julius Caesar) e o Mediterrâneo
oriental (Quintus Dellius) — 2 usos. Nenhum criado por conta própria; ver
"Sobreposições ainda por resolver" para a lista completa acumulada.

**`Turquia` cobre duas aproximações diferentes, achado nos lotes 48-51.** Um
uso é a costa da Anatólia na Guerra Romano-Selêucida (Lucius Aemilius
Regillus, Gaius Livius Salinator — batalhas navais no Egeu/Jônia, longe da
Grécia continental); o outro é a corte em Constantinopla nas bios bizantinas
(Zoe, Michael IV, Michael V, Romanus III — convenção já em uso desde Theodora
Porphyrogenita). Mesmo rótulo, duas épocas e dois motivos de aproximação sem
nenhuma relação entre si — registrado, não resolvido.

**México, Peru, América Central, Brasil e Bolívia entraram na aprovação dos
lotes 76-78**, na adoção do canal Ancient Americas (arqueologia
pré-colombiana). `México` e `Peru` pela recorrência imediata dentro do
próprio lote 77 (4 e 3 usos, muito acima do padrão de segunda ocorrência
já usado para Iêmen/Escócia/Norte da África). `América Central` para a
civilização Maia e temas mesoamericanos afins, que cobrem vários países
atuais sem termo próprio — o próprio vocabulário já previa essa
necessidade (ver nota da América do Sul, acima). `Brasil` pela segunda
ocorrência (`Tupinambá`, lote 77, corrigido retroativamente de `América do
Sul`; `Marajoara`, lote 78). `Bolívia` pela segunda ocorrência dentro do
próprio lote 78 (`Tiwanaku` Partes 1 e 2) — mantida separada do `Peru`
para não misturar dois países andinos distintos sob o mesmo rótulo.

**Teatros de guerra vão em `Subtema`, não em `Região`.** A batalha da Jutlândia
fica com `Região = Atlântico` (a bacia oceânica, pela lista grossa) e
`Subtema = Mar do Norte` (o teatro específico), sob o tema Primeira Guerra
Mundial. Mesmo padrão de `Frente do Oriente Médio` e `Guerra do Pacífico`.

**`Países Baixos` e `Hungria` entraram na aprovação dos lotes 103-106**, na
adoção do canal SandRhoman History. `Países Baixos` cobre o território
histórico dos Países Baixos Espanhóis (hoje dividido entre Holanda e Bélgica)
— criado de saída, não por segunda ocorrência, porque o canal trouxe 7 vídeos
sobre a Guerra dos Oitenta Anos (cercos de Haarlem, Leiden, Antuérpia,
Maastricht, Ostende, 's-Hertogenbosch) num único ciclo de quatro lotes. Um
oitavo vídeo do mesmo tema (captura da frota do tesouro espanhola por Piet
Hein, 1628) ficou de fora da convenção: o evento aconteceu na Baía de
Matanzas, Cuba, não nos Países Baixos, e a região registrada foi `América
Central` (o local do evento, não o lado da guerra) — inconsistência
deliberada, não corrigida, ver `protocolo.md`. `Hungria` fecha uma pendência
aberta desde o lote 19 (`Lenda Arturiana`, aproximada por `Leste Europeu` na
falta de termo próprio): o Exército Negro da Hungria (canal SandRhoman
History, lote 106) é a segunda ocorrência de conteúdo húngaro no catálogo.

**Nenhuma região nova no lote 122** (adoção do canal The Histories), mas 6
aproximações valem registro — nenhuma passou da segunda ocorrência ainda,
critério já usado para criar termo próprio: `Irã` para o deserto da Gedrósia
(Alexandre, o Grande — a área real cobre Irã e Paquistão modernos, sem termo
próprio) e para os Partos (uso legítimo, não aproximação); `Europa` para os
Hunos (cobre tanto os hunos europeus quanto os hunos brancos/heftalitas na
Ásia Central e Índia — aproximação pelo polo narrativo dominante do vídeo,
Átila); `Europa Ocidental` para Gauleses e para Godos (cobertura
multi-país); `Mediterrâneo` para os Fenícios (rede comercial marítima que
cobre o mar inteiro, não só o Levante). **A aproximação mais frágil da
lista: `Judeia` para os Filisteus** — os filisteus eram um povo rival dos
judeus, não o mesmo, e `Judeia` foi usado só por ser o termo mais próximo da
Lista B para o Levante bíblico-arcaico. Vale reconsiderar um termo tipo
`Levante`/`Canaã` se mais canais trouxerem povos da região que não sejam
israelitas.

**Nenhuma região nova nos lotes 123-124** (adoção do canal GatesOfKilikien,
primeiro do catálogo dedicado à China antiga/medieval). `China` já existia e
cobriu todo o núcleo do canal; `Turquia` (Bósforo/Istambul), `Grécia`
(Peloponeso) e `Península Ibérica` (Roma na Hispânia) já existiam e couberam
sem aproximação — são o uso exato, não o mais próximo disponível.

**`Haiti` entrou na aprovação dos lotes 129-132**, na playlist Revolutions
(Mike Duncan), para a Season 4 inteira do podcast (Revolução Haitiana,
episódios narrando Saint-Domingue de colônia francesa a nação independente).
Criada de saída, não por segunda ocorrência — mesmo padrão do México/Peru
(Ancient Americas) e Países Baixos/Hungria (SandRhoman History), quando um
canal traz uma leva grande e concentrada sobre um país sem termo próprio
ainda. Nome do país **moderno**, não o nome colonial do território (Saint-
Domingue) — mesma convenção já usada para Brasil/Bolívia/México/Peru em
conteúdo pré-colombiano ou colonial.

### Convenções por tema (valem para todos os lotes)

- Império Otomano → `Turquia`
- Império Franco → `França`
- Guerra Russo-Ucraniana → `Rússia`, com o mês no campo `Mês`
- Império Romano tratando de província específica → a província
  (Britânia → `Inglaterra`), não `Mediterrâneo`
- `Ucrânia` é para história nacional ucraniana ampla (ex.: tema `História da
  Ucrânia`), não para a guerra atual — essa continua em `Rússia`, pela
  convenção acima. As duas coisas coexistem de propósito.

---

## Lista C — Tema e Subtema (525 temas-raiz)

Regenerada na aprovação dos lotes 232-249 (reabertura dos vinte canais encerrados, só para o que publicaram desde a última coleta), a partir das 5567 linhas de `playlist-historia-v2.xlsx` (lotes 0 a 249). Introduziu 10 temas-raiz: `Guerra Civil Espanhola`, `Guerra Irã-Iraque`, `Guerras Iugoslavas`, `Povo Romani`, `Declínio do Budismo na Índia`, `Descolonização do Império Britânico`, `Guerras Civis do Sudão`, `Revolta dos Camponeses de 1381`, `História da Pimenta`, `Zoroastrismo`. As 152 linhas novas vieram de 16 canais; quatro não tinham nada catalogável. Nenhuma região nova — a Lista B segue com 60 termos em uso.

| n | Tema | Subtemas |
|---|---|---|
| 396 | Império Bizantino | Justiniano e Teodora (34) · Dinastia Comnena (22) · Dinastia Paleóloga (20) · Crise do Século XI (18) · Basílio II (14) · Focas e Tzimisces (14) · Dinastia Isáurica (10) · Filosofia Bizantina (Era Comnena) (9) · Heráclio (8) · O Império em 1025 (8) · O Império em 900 (8) · O Império em 500 (7) · Dinastia Amória (6) · Império de Niceia (6) · Nicéforo I e a Crise Sucessória (6) · Romanos I Lekapeno (6) · Ascensão Macedônia (5) · Dinastia Angelo (5) · Filosofia Bizantina Tardia (5) · O Império em 800 (5) · Sucessores de Justiniano (5) · Constans II e Constantino IV (4) · Justiniano II e a Anarquia (4) · Anastásio I (3) · Michael Psellos (3) · O Império em 600 (3) · O Império em 700 (3) · Perda da Anatólia (3) · Armas Incendiárias Bizantinas (2) · Bizâncio e o Islã (2) · Filosofia Bizantina (Era do Iconoclasmo) (2) · João Damasceno (2) · Panorama Bizantino (curso) (2) · Ana Comnena (1) · Controvérsia Iconoclasta (1) · Exército Temático (Themata) (1) · Filosofia Política Bizantina (1) · Fócio (Photius) (1) · Guarda Varegue (1) · Jorge Gemisto Pletão (1) · Panorama da Filosofia Grega Pós-Bizantina (1) · Peste de Justiniano (1) |
| 383 | República Romana | Segunda Guerra Púnica (68) · Guerra Civil de César (57) · Segundo Triunvirato (37) · Guerra da Gália (23) · Crise da República tardia (91-78 a.C.) (21) · Primeira Guerra Púnica (21) · Conquista da Grécia (13) · Idos de Março (11) · Guerra Jugurtina (7) · Guerra Social (7) · Terceira Guerra Púnica (7) · Conspiração de Catilina (5) · Guerra Mitridática (5) · Guerras Servis (5) · Guerra Cimbria (113-101 a.C.) (4) · Conflito das Ordens (3) · Reforma Agrária dos Gracos (3) · Sula (3) · Panorama Romano (curso) (2) · Saque Gaulês de Roma (2) · Terceira Guerra Samnita (2) · Guerra Latina (1) · Guerra Pírrica (1) · Guerra contra Veios (1) · Primeira Guerra Samnita (1) · Segunda Guerra Samnita (1) |
| 294 | Historiografia | H.G. Wells (22) · A Charge to Keep (12) · Edward Gibbon (7) · Historiadores latinos (6) · Early Rome (5) · Historiadores gregos (4) · Estado Atual do Ocultismo (Painel) (3) · HIS 2210 (3) · Hilaire Belloc (3) · Mitos de Wikipédia (3) · Colaboração entre Academia e Praticantes (RENSEP) (2) · Guia de Estudo do Esoterismo (2) · Idade das Trevas (2) · Pseudoarqueologia (2) · Taking Out the Trash (2) · Cabala no Mundo Contemporâneo (1) · Concepções Errôneas sobre a Alquimia (Debate) (1) · Epistemologia da Experiência Mística (Debate Filosófico) (1) · Guerra de Troia (1) · Hipótese de Tartária (1) · Hipótese do Tempo Fantasma (1) · Historiadores chineses (1) · Historiografia Moderna da Alquimia (Prof. Lawrence Principe) (1) · Historiografia da Alquimia Espiritual (Eliade e Jung) (1) · História do Conceito de 'Nada' (Palestra) (1) · Influência Indiana no Pensamento Grego (Debate) (1) · Lenda de Alexandre (1) · Lista Real Suméria (1) · Lógica Não-Clássica e Budismo (Debate Moderno) (1) · Mos Maiorum (1) · Mulan (1) · O Campo Acadêmico do Esoterismo Ocidental (Introdução) (1) · Recepção da Filosofia Indiana no Islã e na Europa (1) · Thucydides Trap (1) |
| 177 | Segunda Guerra Mundial | Guerra do Pacífico (107) · Prelúdio (20) · Frente Oriental (13) · Guerra de Inverno (6) · Campanha dos Bálcãs (5) · Potências Neutras (5) · Campanha do Norte da África (3) · Guerra Naval no Mediterrâneo (2) · Batalha do Castelo de Itter (1) · Campanha da França (1) · Campanha da Itália (1943-1945) (1) · Exército dos EUA (Organização) (1) · Força Aérea dos EUA (1) · Guerra Civil Espanhola (1) · Programa Nuclear Alemão (1) |
| 149 | Escolástica Medieval | Necromancia e Grimórios Medievais (15) · Sociedade Medieval (8) · Duns Scotus (7) · Tomás de Aquino (6) · Guilherme de Ockham (5) · Alberto Magno (4) · Anselmo de Cantuária (4) · Hildegard von Bingen (4) · Pedro Abelardo (4) · Bernardo de Claraval (3) · Hadewijch e Mechthild de Magdeburgo (Misticismo Beguino) (3) · Peter of Abano (Pietro d'Abano) (3) · Alberto Magno e Tomás de Aquino (2) · Dominicanos Alemães (Mística Renana) (2) · Eriúgena (2) · Henrique de Gand (2) · John Buridan (2) · Marguerite Porete (2) · Medicina Medieval (2) · Nicolau de Cusa (2) · Origens da Escolástica (Séc. XI) (2) · Animais na Filosofia Medieval (Debate Moderno) (1) · Anjos na Filosofia Medieval (1) · As Condenações de Paris (1270 e 1277) (1) · Ascensão das Universidades (Paris, Oxford, Bolonha) (1) · Averroísmo Latino (Siger de Brabant e Boécio da Dácia) (1) · Boaventura (1) · Calculadores de Oxford (1) · Ceticismo Medieval (Debate Moderno) (1) · Conflito Igreja-Estado (Egídio Romano e Dante) (1) · Dante Alighieri (1) · Debate sobre a Trindade (Abelardo, Ricardo de São Vítor e Bernardo de Claraval) (1) · Direito Romano e sua Recepção Medieval (Debate Moderno) (1) · Escola de Chartres (1) · Escolástica do Norte (Wegestreit) (1) · Escolástica na Europa Central (Viena e Praga) (1) · Estética Medieval (Debate Moderno) (1) · Eternidade do Mundo (Debate) (1) · Filosofia Irlandesa Medieval (1) · Filosofia Política Alto-Medieval (Querela das Investiduras e Policraticus) (1) · Filosofia da Natureza (Bernardo Silvestre e Alain de Lille) (1) · Filosofia e a Trindade (Debate Moderno) (1) · Física do Século XIII (1) · Física do Século XIV (Ockham, Buridan, Oresme, Marchia) (1) · Gilberto de Poitiers (1) · Graciano e Pedro Lombardo (1) · Gramática Especulativa (Modistas) (1) · Heloísa e Abelardo (1) · Instituições de Ensino Medievais (Debate Moderno) (1) · Introdução ao Século XIV (Nominalismo e Voluntarismo) (1) · Jean de Meun (Romance da Rosa) (1) · Lei Natural e Legitimidade Política (Séc. XIII) (1) · Lógica Medieval: Formalidade (Debate Moderno) (1) · Lógica das Obrigações (Debate Moderno) (1) · Lógica do Século XIII (1) · Lógica do Século XIV (Obrigações e Paradoxos) (1) · Magia na Filosofia Medieval (Debate Moderno) (1) · Manuscrito Voynich (1) · Marsílio de Pádua (1) · Mechthild de Magdeburgo (1) · Mereologia Medieval (Debate Moderno) (1) · Misticismo Inglês (Julian of Norwich) (1) · Movimento de Tradução para o Latim (1) · Nicolau de Autrecourt (Debate do Ceticismo) (1) · Os Transcendentais (Philip the Chancellor) (1) · Os Vitorinos (Hugo de São Vítor) (1) · Panorama da Escolástica (1) · Pedro Damião (1) · Peter Olivi (1) · Platonismo Medieval (Debate Moderno) (1) · Pobreza Franciscana (Debate) (1) · Poesia Inglesa Medieval (Chaucer e Langland) (1) · Presciência Divina e Livre-Arbítrio (1) · Problema dos Universais (Séc. XII) (1) · Psicologia do Século XIII (1) · Renascimento Carolíngio (Alcuíno) (1) · Robert Grosseteste (1) · Robert Kilwardby (1) · Roger Bacon (1) · Teoria Econômica Medieval (Preço Justo e Usura) (1) · Teorias Medievais da Vontade e da Ação (Debate Moderno) (1) · Teorias das Emoções (Aquino, Escoto, Wodeham) (1) · Trindade e Eucaristia (Filosofia e Teologia) (1) · Walter Burley (Resposta Realista a Ockham) (1) · Ângela de Foligno (1) · Ética do Século XIII (1) |
| 145 | Renascimento | Renascimento Italiano (31) · Cornélio Agripa (20) · Paracelso e a Alquimia (9) · Ciência na Inglaterra Renascentista (5) · Shakespeare (5) · A Monas Hieroglyphica de John Dee (1564) (3) · Ceticismo Renascentista (3) · John Winthrop, o Jovem (Ocultismo Colonial Americano) (3) · Nicolau Maquiavel (3) · Petrus Ramus (3) · A Qabalah Cristã (von Rosenroth e van Helmont) (2) · Jean Bodin (2) · Johannes Trithemius (Esteganografia) (2) · Justus Lipsius e o Neoestoicismo (2) · Literatura Espiritual Feminina (2) · Tolerância Religiosa (2) · A Imprensa e a Filosofia (1) · Arbatel de Magia Veterum (1575) (1) · Christine de Pizan (1) · Ciência e Maravilhas no Renascimento (1) · Defesa das Mulheres (Fonte e Marinella) (1) · Do Nominalismo ao Realismo Oculto (Séc. XIV-XV) (1) · Edward Kelley e a Alquimia (Além de John Dee) (1) · Filosofia Judaica no Renascimento Italiano (1) · Filosofia Política Huguenote (1) · François Rabelais (1) · Girolamo Savonarola (1) · Humanismo Francês Tardio (1) · Humanismo Francês: Budé e a Pléiade (1) · Humanismo do Norte (Agricola e Vives) (1) · Humanismo na Grã-Bretanha (1) · Humanistas Italianas (1) · Jean Gerson (1) · Jochanan Alemanno (Cabala Renascentista) (1) · Johannes Reuchlin e o De Verbo Mirifico (1492) (1) · Literatura Elisabetana (1) · Lorenzo Valla (1) · Lógica e Linguagem no Renascimento Francês (1) · Magiae Naturalis (Giambattista della Porta, 1558) (1) · Manuais de Exorcismo e Necromancia (pré-1614) (1) · Marguerite de Navarra (1) · Marie de Gournay (1) · Marsilio Ficino (1) · Medicina na França Renascentista (1) · Mutus Liber (1677) (1) · Nicolas Flamel (Vida e Lenda Alquímica) (1) · Os Rosacruzes e a Fama Fraternitatis (1614) (1) · Pensamento Político Inglês (1) · Pico della Mirandola (1) · Precursores do Humanismo (Llull e Petrarca) (1) · Teorias da Matéria (Atomismo Renascentista) (1) · Thomas More (1) |
| 131 | Filosofia Africana | Etnofilosofia e Debate sobre a Filosofia Africana (13) · Filosofia Etíope (4) · W.E.B. Du Bois (4) · Filosofia Africana Profissional (3) · Filosofia Islâmica na África Subsaariana (3) · Frantz Fanon (3) · Alain Locke (2) · Amílcar Cabral (2) · Anton Wilhelm Amo (2) · Claudia Jones (2) · Cornel West (2) · Frederick Douglass (2) · Marcus Garvey (2) · Martin Luther King Jr. (2) · Ngũgĩ wa Thiong'o (2) · Panorama da Filosofia Africana (Início do Séc. XX) (2) · Édouard Glissant (2) · Abdias do Nascimento (1) · Abolicionismo no Brasil (1) · Academia Negra Americana (ANA) (1) · Afrocentricidade (Molefi Asante) (1) · Afrofuturismo (1) · Aimé e Suzanne Césaire (1) · Alexander Crummell (1) · Angela Davis (1) · Anna Julia Cooper (1) · Anténor Firmin (1) · As Duas Amy Garvey (1) · Ativistas Negras (NACW) (1) · Audre Lorde (1) · Booker T. Washington (1) · C.L.R. James (1) · Carter G. Woodson (1) · Cedric Robinson (Marxismo Negro) (1) · Controvérsia da Colonização (1) · Cugoano e Equiano (Filhos da África) (1) · David Walker (1) · E. Franklin Frazier (1) · Edward Blyden (1) · Emigração para o Canadá (1) · Escrita Africana Primitiva em Inglês (1) · Estudos Culturais Negros Britânicos (Stuart Hall) (1) · Fela Kuti e Wole Soyinka (1) · Feminismo Negro (bell hooks e Patricia Hill Collins) (1) · Feminismo Negro dos Anos 1970 (Combahee River Collective) (1) · Henry Highland Garnet (1) · Henry McNeal Turner (1) · Hosea Easton (1) · Ida B. Wells (1) · Identidade Africana na Diáspora (1) · Ignatius Sancho e Benjamin Banneker (1) · Instituições Negras Primitivas nos EUA (1) · Intelectuais da África Ocidental (Início do Séc. XX) (1) · Introdução: Escravidão e Diáspora (1) · J.J. Thomas e F.A. Durham (1) · James Africanus Beale Horton (1) · James Baldwin (1) · Juan René Betancourt (1) · Julius Nyerere (1) · Kwame Nkrumah (1) · Lemuel Haynes (1) · Lorraine Hansberry (1) · Léopold Senghor (1) · Malcolm X (1) · Malcolm X e MLK: Últimos Anos (1) · Maria W. Stewart (1) · Martin Delany (1) · Marxismo e a Diáspora Africana (1) · Maulana Karenga e o Kwanzaa (1) · Movimento da Negritude (1) · Movimento das Artes Negras (1) · Nelson Mandela e o ANC (1) · Nnamdi Azikiwe e Obafemi Awolowo (1) · Oliver Cox e Eric Williams (1) · Origens da Humanidade (Pré-história) (1) · Panteras Negras (1) · Paul Robeson (1) · Phillis Wheatley (1) · Poder Negro (Black Power) (1) · Precursores da Afrocentricidade (1) · Ralph Ellison (1) · Raízes do Nacionalismo Negro (1) · Reggae e Rastafari (1) · Renascimento Literário das Mulheres Negras (1) · Renascimento do Harlem (1) · Richard Wright (1) · Socialismo Afro-Americano Primitivo (1) · Sojourner Truth e Frances Harper (1) · Steve Biko (1) · Sylvia Wynter (1) · T. Thomas Fortune (1) · Teologia Negra (1) · Teoria Racial Crítica (1) · Walker, Stewart e Easton (Pensamento Racial do Séc. XIX) (1) · Walter Rodney (1) · Zora Neale Hurston (1) |
| 119 | Sengoku Jidai | Clãs do Sengoku (24) · Batalha de Nagashino (4) · Cerco de Osaka (2) · Guerra Ōnin (2) · Castelos do Sengoku Jidai (1) · Exército do Sengoku Jidai (1) · Marinha do Sengoku Jidai (1) |
| 112 | Império Romano | Dinastia júlio-claudiana (31) · Ano dos Quatro Imperadores (11) · Crise do Século III (10) · Britânia romana (6) · Dinastia Constantiniana (6) · Limes Germânico (Fronteira do Reno) (4) · Invasão Romana da Escócia (Agrícola) (3) · Diocleciano e a Tetrarquia (2) · Dácia Romana (1) · Fronteiras do Império (1) · Hispania Romana (1) · Invasão Romana da Arábia (1) · Judeia Romana (1) · Peste Antonina (1) · Relações Roma-Índia (1) |
| 98 | Guerra Russo-Ucraniana | — |
| 90 | Avisos do canal | — |
| 90 | Cruzadas | Primeira Cruzada (37) · Segunda Cruzada (17) · Quarta Cruzada (16) · Terceira Cruzada (7) · Panorama das Cruzadas (3) · Cruzada Albigense (2) · Cruzada das Crianças (1) |
| 87 | História dos Estados Unidos | Candidatos Derrotados (43) · Política (24) · Bush 43 Still Sucks (6) · Presidência (5) · Fundação (2) · Guerras Índias (2) · Diplomacia (1) · Igreja Negra e Direitos Civis (1) · Marinha (1) |
| 83 | Reforma Protestante | Martinho Lutero (21) · João Calvino (14) · Reforma Católica (Contrarreforma) (6) · Puritanismo Inglês e Colonial (3) · A Bíblia em Inglês (2) · Assentamento Elisabetano (2) · Calvino e a Tradição Reformada (2) · Erasmo x Lutero: Livre-Arbítrio (2) · Henrique VIII e o Anglicanismo Primitivo (2) · Jan Hus e a Profecia da Reforma (2) · John Knox e a Reforma Escocesa (2) · John Wycliffe (2) · Luteranismo Posterior (2) · Panorama da Reforma (2) · Calvino e o Caso Sérveto (1) · Covenanters Escoceses (1) · Erasmo de Roterdã (1) · Guerra dos Camponeses e Reforma Radical (1) · Huguenotes e a Reforma Francesa (1) · Huldrych Zwínglio (1) · Indulgências (1) · Lutero e Calvino: Teologia Comparada (1) · Lutero e Melanchthon (1) · Menno Simons e os Menonitas (1) · Pano de Fundo Medieval da Reforma (1) · Panorama da Reforma Britânica (1) · Philip Melanchthon (1) · Protestantismo Espanhol (1) · Reino Anabatista de Münster (1) · Thomas Cranmer (1) · William Tyndale (1) |
| 82 | Império Otomano | Mehmed II (13) · Guerra Otomano-Portuguesa (4) · Cercos de Viena (3) · Bayezid II e Selim I (2) · Guerra de Chipre (2) · Janízaros (2) · Cem Sultan (1) · Guerra de Candia (1) · Guerras Otomano-Safávidas (1) · Islamização da Bósnia (1) · João Hunyadi (1) · Kapikulu (Exército Permanente) (1) · Skanderbeg (1) · Sultanato das Mulheres (1) |
| 77 | Filosofia Judaica Medieval | Misticismo Merkavah (Hekhalot) (25) · Cabala (Zohar e Abraham Abulafia) (7) · Cabala de Safed (Cordovero, Luria e Israel Sarug) (5) · Cabala Primitiva (Círculos de Provença e Castela) (4) · Maimônides (4) · Sabbatai Zevi e o Messianismo Cabalístico (Nathan de Gaza) (3) · Sefer Yetzirah e Sefer Bahir (Origens da Cabala) (2) · A Espada de Moisés (Harba de-Moshe) (1) · Ascensão do Apocalipticismo Judaico (Daniel e Enoque) (1) · Astrologia Médica Hebraica (Kelal Qatan) (1) · Astrologia no Judaísmo e Islã Antigos (1) · Cabala Cristã e Cabala Luriânica (1) · Cabala Moderna (R. Yosef Ergas) (1) · Cabala Tardia e o Surgimento do Hassidismo (1) · Controvérsia Maimonidiana (1) · Gersônides (1) · Gersônides e Hasdai Crescas (1) · Glória Divina e o Proto-Cabalismo dos Querubins (Akhatriel) (1) · Hasdai Crescas (1) · Ibn Gabirol (1) · Joseph Albo e Isaac Abravanel (1) · Judah Halevi (1) · Liberdade e Astrologia na Filosofia Judaica (Ibn Ezra, Ibn Daud e Maimônides) (1) · Magia Judaica Antiga e Medieval (1) · Neoplatonismo Judaico (Isaac Israeli, Ibn Gabirol e Maimônides) (1) · Panorama do Pensamento Judaico Andaluz (Debate Moderno) (1) · Profecia e Teofania Israelita (Fundamentos Pré-Cabalísticos) (1) · Raízes da Filosofia Judaica no Mundo Islâmico (Mishnah, Talmud e Isaac Israeli) (1) · Saadia Gaon (1) · Sar Torah e os Hasidei Ashkenaz (1) · Sefer HaMalbush e Sefer HaYashar (Magia do Manto) (1) · Sofrimento na Filosofia Judaica (Saadia a Gersônides) (1) · Zohar sobre Ester (Piada de 1º de Abril) (1) · Ética e Judaísmo (Baḥya Ibn Paquda e Maimônides) (1) |
| 69 | Cristianismo Primitivo | Gnosticismo (23) · Agostinho de Hipona (9) · Apologistas e Heresias Primitivas (3) · Atanásio e Niceia (3) · Boécio (3) · O Jesus Histórico (3) · Perseguições aos Cristãos (2) · Ambrósio de Milão (1) · Ambrósio e Jerônimo (1) · Ascetismo Cristão (Antão, Macrina e Evágrio) (1) · Concílio de Calcedônia (1) · Concílio de Constantinopla (1) · Formação da Doutrina da Trindade (1) · Magia Cristã Copta Primitiva (Proteção, Exorcismo e Amor) (1) · Monasticismo Primitivo (1) · Máximo o Confessor (1) · Nestório e o Concílio de Éfeso (1) · Orígenes (1) · Padres Apostólicos (1) · Padres Capadócios (1) · Padres Gregos e a Bíblia (Debate Moderno) (1) · Padres Latinos (Tertuliano a Jerônimo) (1) · Platonismo Latino (Apuleio a Calcídio) (1) · Pseudo-Dionísio Areopagita (1) · São Paulo (1) |
| 60 | Dinastia Zhou | Cem Escolas do Pensamento (53) · Estados Combatentes (5) · Zhou Ocidental e Primavera e Outono (1) |
| 58 | História na cultura popular | Literatura (33) · Cinema (17) · Televisão (4) · Jogos (2) · Luta livre profissional (1) |
| 57 | Filosofia Islâmica | Avicena (5) · Averróis (3) · Mulla Sadra (3) · al-Farabi (3) · al-Ghazali (3) · Sufismo Filosófico (Ibn 'Arabī e Rūmī) (2) · al-Kindī (2) · Abu Bakr al-Razi (Rhazes) (1) · Abu l-Barakat al-Baghdadi (1) · Cultura de Comentários na Filosofia Islâmica Tardia (Debate Moderno) (1) · Debate sobre a Metafísica de Avicena (Essência e Existência) (1) · Encontros com o Pensamento Europeu (Índia e Império Otomano, Séc. XVIII-XIX) (1) · Escola de Bagdá (1) · Escola de Shiraz (1) · Fakhr al-Din al-Razi (1) · Filosofia e Ciência na Era Mongol (1) · Filosofia na Era Buida (1) · Filosofia na Índia Islâmica (Dārā Shikūh) (1) · Filosofia sob os Otomanos (Kātib Çelebi) (1) · Filosofia sob os Safávidas (1) · Ibn 'Arabī (Misticismo) (1) · Ibn Bājja e Ibn Ṭufayl (1) · Ibn Khaldun (1) · Ibn Taymiyya (1) · Ibn al-Haytham (Teorias da Visão) (1) · Ibn Ḥazm e Teoria Jurídica Islâmica (1) · Literatura Ética Árabe (al-Kindī a Miskawayh) (1) · Medicina no Mundo Islâmico (Debate Moderno) (1) · Muhammad 'Abduh e Muhammad Iqbal (1) · Mulheres Estudiosas e o Islã (Fatema Mernissi e outras) (1) · Música e Filosofia na Tradição Árabe (1) · Naṣīr al-Dīn al-Ṭūsī (1) · Os Asharitas (al-Ash'arī) (1) · Os Ismaelitas (Painel/Entrevista) (1) · Os Mutazilitas (Abū l-Hudhayl e al-Naẓẓām) (1) · Panorama Pós-Suhrawardi (Iluminacionismo) (1) · Panorama da Filosofia em al-Andalus (1) · Pensamento Islâmico Contemporâneo (Debate Moderno) (1) · Pós-Mulla Sadra (Sabzawari a Nasr) (1) · Suhrawardi (1) · Tradição Lógica Pós-Avicena (Debate Moderno) (1) · Tradução do Grego para o Siríaco e o Árabe (1) · Traduções do Árabe para o Latim (1) |
| 57 | Revolução Francesa | Diretório (10) · O Terror (8) · Queda da Monarquia (4) · Reação Termidoriana (4) |
| 56 | Egito antigo | Reino Antigo (9) · Reino Novo (6) · Dinastia 0 (5) · Período Tardio (5) · Reino Médio (4) · Período Dinástico Arcaico (3) · Segundo Período Intermediário (3) · Terceiro Período Intermediário (3) · Egito e Núbia (2) · Período Pré-dinástico (2) · Primeiro Período Intermediário (1) |
| 56 | Filosofia Indiana | Nagarjuna (4) · Dignaga (3) · Patañjali e o Yoga-Sūtra (2) · Teorias Materialistas do Self (Payasi e Cārvāka) (2) · Upaniṣads (2) · Animais na Filosofia Indiana (1) · Bhagavad-Gītā (1) · Bhartṛhari (1) · Buddhaghosa (1) · Budismo: Teoria do Não-Self (Anattā) (1) · Ceticismo na Índia Antiga (Debate entre Escolas) (1) · Epistemologia Jainista (1) · Escola Nyāya (Gautama) (1) · Escola Nyāya (Painel) (1) · Escola Vaiśeṣika (Kaṇāda) (1) · Estética do Rasa (1) · Filosofia da Mente Indiana (Debate Budista-Hindu) (1) · Gramática de Pāṇini (1) · Hinduísmo e Filosofia (Painel/Entrevista) (1) · Introdução: A Era dos Sutras (1) · Lógica Jainista (Saptabhaṅgī) (1) · Mahābhārata: Dharma e Ética (1) · Medicina Ayurvédica Antiga (Caraka-Saṃhitā) (1) · Mulheres na Índia Antiga (1) · Mīmāṃsā (Painel/Entrevista) (1) · Mīmāṃsā-Sūtra (Jaimini) (1) · Mīmāṃsā: Conhecimento e Linguagem (1) · Nyāya: Lógica da Inferência (1) · Nyāya: Percepção (1) · Nyāya: Self e Mente (1) · Não-Violência (Ahimsā) (1) · O Buda e as Quatro Nobres Verdades (1) · Origens do Karma (Upaniṣads e Bhagavad-Gītā) (1) · Panorama Histórico: Escolas e Sistemas Indianos (1) · Panorama Pós-Dignaga (1) · Panorama: Budismo e Jainismo até Dignāga (1) · Pensamento Político Indiano Antigo (Kautilya e Aśoka) (1) · Período Védico (Panorama) (1) · Sāṃkhya-Kārikā (Īśvarakṛṣṇa) (1) · Tantra (Xivaísmo da Caxemira e Tantra Budista) (1) · Teoria dos Pontos de Vista Jainista (Anekāntavāda) (1) · Upaniṣads (Painel/Entrevista) (1) · Vaiśeṣika: Debate com o Ceticismo Budista (1) · Vaiśeṣika: Tempo e Espaço (1) · Vasubandhu (1) · Vedānta (Painel/Entrevista) (1) · Vedānta-Sūtra (Bādarāyaṇa) (1) · Śaṅkara e o Advaita Vedānta (1) |
| 51 | Guerras dos Diádocos | Segunda Guerra dos Sucessores (8) · Primeira Guerra dos Sucessores (3) |
| 50 | Jogos de estratégia | Lore de ficção (26) · Total War (12) |
| 50 | Revolução Russa de 1905 | Prelúdio (10) · Revolução de 1905 (9) · Pós-1905 (7) · Decembristas (3) |
| 48 | Filosofia Helenística e Romana | Epicuro e o Epicurismo (4) · O Renascimento Platônico (Eudoro, Alcínoo e Numênio) (4) · Os Primeiros Estoicos (Zenão, Cleantes e Crisipo) (4) · Cícero (2) · Fílon de Alexandria (2) · Platonismo Médio (Painel) (2) · A Academia Cética (1) · Alexandre de Afrodísias (1) · Antíoco de Ascalon (1) · Apuleio (1) · Aristotelismo Pós-Aristóteles (1) · As Origens Estoicas do Ocultismo Ocidental (1) · Diógenes e os Cínicos (1) · Epicteto (1) · Estoicismo Romano (Debate Moderno) (1) · Filosofia Helenística da Astrologia (Debate Moderno) (1) · Galeno (1) · Introdução: A Sombra de Platão (1) · Lucrécio (1) · Marco Aurélio (1) · Matemática Antiga e Filosofia (Debate Moderno) (1) · Medicina e Filosofia na Antiguidade (Herófilo a Galeno) (1) · Neopitagóricos (1) · O Estoicismo: Painel sobre a Escola (1) · O Self na Filosofia Helenística (Debate Moderno) (1) · O Submundo Platônico (1) · Os Cirenaicos (1) · Panorama: Filosofia no Império Romano (1) · Pirro e o Ceticismo Pirrônico (1) · Platonismo Médio e Cristianismo (1) · Plutarco (1) · Plutarco de Queroneia (1) · Ptolomeu: Astronomia, Astrologia e Filosofia (1) · Retórica e Filosofia Antiga (Temístio, Quintiliano e Luciano) (1) · Sexto Empírico (1) · Sêneca (1) |
| 44 | Império Mongol | Rabban Bar Sauma (1) |
| 44 | Revolução Americana | Campanha de Saratoga (2) · Cerco de Gibraltar (2) · Lealistas (2) · Igrejas na Revolução Americana (1) · Traição de Benedict Arnold (1) |
| 43 | Guerras Napoleônicas | Marechais de Napoleão (7) · Guerra Peninsular (5) · Grande Armée (Organização) (1) · Thomas Cochrane (1) · Velha Guarda (Old Guard) (1) |
| 43 | Resenhas de ficção | — |
| 42 | Filosofia Moderna | René Descartes (11) · Cartesianismo Francês (9) · Blaise Pascal (3) · Moralistas Franceses (3) · Pierre Bayle (3) · Elisabeth da Boêmia (2) · Gassendi e o Atomismo (2) · República Holandesa (2) · República das Letras (2) · Ceticismo Francês (1) · Teorias da Substância (Aquino a Locke e Leibniz) (1) · Tolerância Religiosa (1) |
| 42 | Primeira Guerra Mundial | Prelúdio (5) · Frente do Oriente Médio (3) · Frente Oriental (2) · Guerra Naval (2) · Frente do Cáucaso (1) · Igrejas na Primeira Guerra Mundial (1) · Mar do Norte (1) |
| 41 | Jogos de samurai | — |
| 38 | Alexandre, o Grande | — |
| 37 | Hermetismo | Datação e o Debate sobre a Autenticidade (Ficino a Casaubon) (3) · Panorama da Transmutação Alquímica (3) · A Edição de 1505 do Corpus Hermeticum e Lazzarelli (2) · O Deus Sem Cabeça (Akephalos) e os Papiros Mágicos Gregos (2) · Os Papiros Mágicos Gregos (PGM) (2) · A Fórmula do Caranguejo/Escorpião (Alquimia Greco-Egípcia) (1) · A Inquisição contra a Alquimia (Nicholas Eymerich, 1396) (1) · A Perseguição de Dioclesiano aos Alquimistas (296 d.C.) (1) · A Tábua de Esmeralda (Origens e Transmissão) (1) · Antologia Hermética Renascentista (1497) (1) · Cabala Química (Cabala e Alquimia) (1) · Cleópatra, a Alquimista (Crisopeia) (1) · Cosmologia e Teologia Hermética (Corpus Hermeticum) (1) · Fragmentos Herméticos Adicionais (Stobeu, Kore Kosmou) (1) · Hermetica Técnica (Kyranides) (1) · João de Rupescissa e a Alquimia Apocalíptica (1) · Magia do Tesouro (Lore e Feitiçaria) (1) · Magia e Doença (Panorama Histórico) (1) · Maria, a Judia (Alquimia Greco-Egípcia) (1) · O Livro da Composição da Alquimia (1144, Robert de Chester) (1) · O Livro de Tot Egípcio (Ritual de Iniciação Demótico) (1) · Os Alquimistas Empreendedores (Pós-Peste Negra) (1) · Os Magos (Mitologia e História) (1) · Petosíris, Sumo Sacerdote de Tot (Origens Egípcias) (1) · Summa Perfectionis (Pseudo-Geber, c. 1310) (1) · Símbolos Mágicos e Alfabetos Angélicos (Origens) (1) · Tot e a Origem de Hermes Trismegisto (1) · Tratado de Talismãs (De Imaginibus, Thabit ibn Qurra) (1) · Turba Philosophorum (Assembleia dos Filósofos) (1) · Zósimo de Panópolis (Origens Egípcias da Alquimia) (1) |
| 35 | Expansão islâmica | Al-Andalus (1) |
| 35 | Guerra Civil Americana | Prelúdio (4) · Campanha de Atlanta (2) · Teatro Ocidental (2) · Campanha Overland (1) · Campanha da Península (1) · Campanha de Chattanooga (1) · Campanha de Gettysburg (1) · Campanha de Vicksburg (1) · Marcha para o Mar (1) · Teatro naval (1) |
| 34 | Revoluções de 1848 | — |
| 33 | Guerra Civil Inglesa | Prelúdio (5) · Protetorado de Cromwell (4) · Coldstream Guards (1) · Puritanismo (1) |
| 32 | Exército Romano | — |
| 28 | Guerras de Independência Hispano-Americanas | — |
| 27 | Inglaterra anglo-saxã | Invasão Viking (16) · Reino de Kent (1) |
| 27 | Revolução Mexicana | — |
| 26 | Guerra dos Cem Anos | Ascensão dos Arqueiros Ingleses (3) · Joana d'Arc (3) |
| 26 | História do Cristianismo Moderno | Iluminismo e a Igreja (3) · John Wesley e George Whitefield (2) · Arminianismo e a Revolta Holandesa (1) · Catolicismo Imigrante nos EUA (1) · Evangelho Social e Liberalismo Teológico (1) · Fundamentalismo (1) · Inglaterra dos Stuart (1) · Jansenismo (1) · Jonathan Edwards (1) · Movimento de Oxford (1) · Movimentos de Santidade e Restauração (1) · Neoevangelicalismo (1) · Panorama do Século XIX (1) · Panorama do Século XVII (1) · Panorama do Século XVIII (1) · Pentecostalismo (1) · Peregrinos e Colônias Americanas (1) · Pietismo Luterano (1) · Primeiro Grande Despertar (1) · Puritanismo (panorama) (1) · Quietismo (1) · Segundo Grande Despertar (1) · Unitários, Batistas e Quacres (1) |
| 25 | História de Gales | Reino de Gwynedd (6) · Conquista de Gales (1) |
| 25 | Revolução Russa de 1917 | Prelúdio (7) · Revolução de Outubro (7) · Governo Provisório (6) · Revolução de Fevereiro (4) |
| 24 | Babilônia Antiga | Período Paleobabilônico (6) · Império Neo-Babilônico (3) · Astronomia Babilônica (1) · Babilônia Helenística (1) · Dinastia Cassita (1) · Dinastia do Sealand (1) · Jardins Suspensos (1) · Mari (1) · O Ritual Maqlû (Contra-Magia Babilônica) (1) · Panorama Babilônico (curso) (1) · Período Isin-Larsa (1) · Ritual do Rei Substituto (1) · Segunda Dinastia de Isin (1) · Sociedade e Leis Babilônicas (1) · Séculos Obscuros da Babilônia (1) |
| 24 | Grécia antiga | Idade das Trevas Grega (2) · Período Arcaico (2) · Demóstenes (1) · Filosofia Clássica (1) · Panorama Grego (curso) (1) · Panorama do Bronze Egeu (curso) (1) · Período Neolítico (1) · Safo de Lesbos (1) |
| 23 | Guerra dos Trinta Anos | Intervenção Sueca (9) · Fase Boêmia (3) · Fase Dinamarquesa (1) · Fase Francesa (1) · Guerra de Sucessão de Mântua (1) |
| 23 | Revolução Haitiana | — |
| 22 | Canaã Antiga | Religião Cananeia (7) · Reinos da Idade do Ferro (6) · Demonologia do Antigo Israel (Pré-Exílica) (1) · Domínio Egípcio (Bronze Final) (1) · Idade de Ouro Cananeia (Bronze Médio) (1) · Iom Kipur e o Ritual do Templo (1) · Jericó e o Bronze Antigo (1) · Possessão e Exorcismo no Judaísmo Antigo (Mil Anos) (1) |
| 21 | Aristóteles | Aristóteles (16) · Sucessores de Platão e Aristóteles (Academia Antiga e Teofrasto) (3) · Aristóteles e Platão: Recepção Crítica (1) · Meteorologica e as Origens da Alquimia (1) |
| 21 | Guerras Médicas | Invasão de Xerxes (12) · Primeira Invasão Persa (Maratona) (1) · Revolta da Jônia (1) |
| 21 | Platão | Platão (16) · Sócrates (3) · A Loucura Divina de Platão e sua Recepção Renascentista (Ficino, Agripa e Bruno) (1) · As Doutrinas Não-Escritas de Platão (Pitagorismo) (1) |
| 20 | Sociedade Romana | Literatura Romana (1) |
| 19 | Caça às Bruxas | Demonólogos Medievais (de Agostinho ao Malleus) (2) · As Bruxas e a Ascensão do Capitalismo (Silvia Federici) (1) · As Origens da Inquisição Medieval (1) · Daemonologie de Jaime VI/I e as Bruxas de North Berwick (1590-1597) (1) · Filosofia e a Bruxaria (Agrippa a Espinosa) (1) · Johann Weyer e o Ceticismo da Bruxaria (1563) (1) · Julgamentos de Bruxaria Coloniais Antes de Salém (1) · Julgamentos de Salém (Sobreviventes e o Manual Puritano) (1) · Manuais Inquisitoriais e a Heresia Mágica (Nicholas Eymerich) (1) · Martín Del Rio e a Disquisitionum Magicarum (1599) (1) · O Formicarius de Johannes Nider (Origem do Conceito de Bruxa) (1) · O Malleus Maleficarum (1486) (1) · O Voo das Bruxas ao Sabá (Mito e Unguento Alucinógeno) (1) · Panorama da Bruxaria no Início da Era Moderna (Palestra) (1) · Possessões de Loudun (Urbain Grandier) (1) · Transformação da Feitiçaria em Heresia (João XXII) (1) · Ulrich Molitor e a Iconografia da Bruxa (1489) (1) |
| 19 | Demonologia Ocidental | Anel e Selo de Salomão (7) · Lilith (5) · Demônios do Talmude (Daf Yomi) (2) · Baal (1) · Belial (1) · Moloch (1) · O Anjo da Morte (1) · Set (Seth) (1) |
| 19 | Evolução da guerra | — |
| 19 | Geografia Estratégica | Babilônia (1) · Estreito de Ormuz (1) · Grandes Muralhas (1) · Megido (1) · Naqsh-e Rustam (1) · Notre-Dame de Paris (1) · Susa (1) · Takht-e Soleyman (1) · Ur (1) |
| 19 | Guerra Civil Russa | Kronstadt e NEP (4) · Derrota dos Brancos (3) · Guerra Polaco-Soviética (2) · Terror Vermelho (2) · Alexander Kolchak (1) · Frente Ucraniana (1) |
| 19 | Jogos retrô | — |
| 19 | Queda do Império Romano | — |
| 19 | Suméria Antiga | Amorreus (2) · Cemitério Real de Ur (2) · Império Neo-Sumério (Ur III) (2) · Lagash e Umma (2) · Origens (2) · Panorama Sumério (curso) (2) · Bibliotecas Sumérias Primitivas (Shuruppak, Abu Salabikh e Ebla) (1) · Cidades do Período Dinástico Arcaico (1) · Cuneiforme (1) · Eridu (1) · Gudea de Lagash (1) · Kish (1) · Masterpieces de Mesopotâmia (1) |
| 19 | Xogunato do Japão | Período Edo (10) |
| 18 | Comentário Político Contemporâneo | — |
| 17 | Napoleão Bonaparte | Campanha da Itália (2) · Campanha do Egito (1) · Michel Ney (1) |
| 17 | Neoplatonismo Tardo-Antigo | Plotino (5) · Jâmblico (2) · Proclo (2) · Comentadores Antigos de Aristóteles (Debate Moderno) (1) · Estética Antiga (De Platão a Proclo) (1) · João Filópono (1) · Natureza no Neoplatonismo (Plotino e Porfírio) (1) · Neoplatonismo: Política e Matemática (Debate Moderno) (1) · Oráculos Caldeus e a Teurgia (1) · Os Últimos Filósofos Pagãos (Juliano e as Escolas de Atenas e Alexandria) (1) · Porfírio (1) |
| 17 | Pré-Socráticos | Heráclito (2) · Parmênides (2) · Anaximandro e Anaxímenes (1) · Anaxágoras (1) · Demócrito e Leucipo (Atomismo) (1) · Empédocles (1) · Hipócrates e a Medicina Grega Antiga (1) · Os Sofistas (Protágoras e Górgias) (1) · Painel sobre os Pré-Socráticos (Debate Moderno) (1) · Papiro de Derveni e os Mistérios Órficos (1) · Pitágoras (1) · Pitágoras e Parmênides (Esoterismo Filosófico) (1) · Tales de Mileto (1) · Xenófanes (1) · Zenão de Eleia e Melisso (1) |
| 16 | Cartago antiga | Conquista Bárcida da Ibéria (1) · Guerra dos Mercenários (1) |
| 16 | Império Aquemênida | Panorama Aquemênida (curso) (3) · Conquista Persa do Egito (1) · Expedição de Ciláx (1) · Pasárgada (1) · Persépolis (1) · Reino de Anshan (1) |
| 15 | Era Viking | Jomsvikings (1) |
| 15 | Esparta | Exército Espartano (1) · Guerras Messênias (1) |
| 15 | Guerra do Peloponeso | — |
| 14 | Assíria Antiga | Período Médio Assírio (3) · Reino Antigo Assírio (3) · Reino da Alta Mesopotâmia (3) · Panorama Assírio (curso) (2) · Biblioteca de Assurbanipal (1) · Exército Assírio (1) · Semíramis (Sammu-ramat) (1) |
| 14 | Império Franco | Carlos Magno (4) · Merovíngios (2) · Exército carolíngio (1) · Guerras Saxônicas (1) |
| 14 | Segunda Escolástica | Debate do Novo Mundo (3) · Escolástica Protestante (2) · Francisco Suárez (2) · Escolástica Britânica (1) · Luis de Molina (1) · Revival Tomista (1) |
| 13 | Religião Romana | — |
| 12 | Bretanha Antiga | — |
| 12 | Guerra Genpei | — |
| 12 | Guerra Medieval | — |
| 12 | Revoluções de 1830 | — |
| 11 | Cultura material samurai | — |
| 11 | Dinastia Han | Filosofia Han (4) · Han Ocidental (1) · Han Oriental (1) |
| 11 | Guerra Imjin | — |
| 11 | Guerra de Sucessão Espanhola | — |
| 11 | Guerras Germânicas de Roma | — |
| 11 | História dos Feriados | Halloween (2) · Advento (1) · Ação de Graças (1) · Dia das Mães (1) · Papai Noel (1) · Presentes de Natal (1) · Páscoa (1) · Silent Night (canção) (1) |
| 11 | Papado | Borgias (1) · Concílio Vaticano I (1) · Escavações do Túmulo de São Pedro (1) · Grande Cisma do Ocidente (1) · Leão Magno (1) · Papado de Avinhão (1) · Pio XII e a Segunda Guerra Mundial (1) |
| 11 | Teoria da Revolução | — |
| 10 | Comuna de Paris | — |
| 10 | Grande Guerra do Norte | — |
| 10 | Guerra dos Oitenta Anos | — |
| 10 | Guerras Greco-Púnicas na Sicília | — |
| 10 | História da Ucrânia | Euromaidan (1) · Holodomor (1) · Russificação (1) |
| 10 | Reconquista | — |
| 10 | Vida urbana | Roma (3) · Constantinopla (2) · Alexandria (1) · Antioquia (1) · Atenas (1) · Hattusa (1) · Quioto (1) |
| 9 | Civilização Micênica | Questão Ahhiyawa (1) |
| 9 | Fortalezas | Vauban (2) |
| 9 | Guerras Italianas | — |
| 9 | Sociedade Mesopotâmica | — |
| 8 | Civilização Fenícia | Biblos (1) · Sidon (1) · Tiro (1) |
| 8 | Colapso da Idade do Bronze | — |
| 8 | Feudalismo | — |
| 8 | Gladiadores | — |
| 8 | Império Afexárida | — |
| 8 | Macedônia Antiga | — |
| 8 | Reino de Roma | — |
| 8 | Rus de Kiev | — |
| 7 | Civilização Maia | Cidades Maias (2) · Período Clássico (2) · Colapso Maia (1) · Códice Maya de México (Almanaque de Vênus) (1) · Período Pré-Clássico (1) |
| 7 | Conquista normanda da Inglaterra | Hereward, o Vigilante (1) |
| 7 | Democracia Ateniense | — |
| 7 | Império Acadiano | Estela da Vitória de Naram-Sin (2) · Enheduanna (1) · Rimush e Manishtushu (1) |
| 7 | Período dos Três Reinos | Ascensão de Cao Cao (4) · Shu Han (1) |
| 7 | Revolução Científica | Johannes Kepler (1) · Nicolau Copérnico (1) · Tycho Brahe (1) |
| 7 | União Soviética | Luta pela Sucessão (4) · Fundação da URSS (3) |
| 6 | Califado Abássida | — |
| 6 | Colonização grega | Acragas (1) |
| 6 | Elam Antigo | Período Proto-Elamita e Elamita Antigo (3) · Período Médio e Neo-Elamita (2) · Período Neo-Elamita (1) |
| 6 | Formação do Japão Guerreiro | — |
| 6 | Guerra Israel-Hamas | — |
| 6 | Guerras Anglo-Escocesas | — |
| 6 | Guerras Indo-Paquistanesas | — |
| 6 | História alternativa | — |
| 6 | História da Rússia | — |
| 6 | John Dee e a Magia Enocheana | A Língua Enocheana e o Liber Loagaeth (2) · As Mulheres da Magia Enocheana (Jane Dee e Joan Kelley) (1) · Ferramentas e Rituais Enocheanos (Heptarchia Mystica) (1) · O Alfabeto Enocheano (Origens e Paleografia) (1) · O Livro de Soyga e as Tábuas Cifradas (1) |
| 6 | Manuscritos do Mar Morto (Qumran) | Calendário Astrológico Cifrado e o Tesouro (Manuscritos do Mar Morto) (1) · Literatura de Exorcismo Davídica (1) · O Pergaminho de Cobre (3Q15) e o Tesouro do Templo (1) · O Rolo da Guerra e a Batalha contra Belial (1) · Os Terapeutas (Filo de Alexandria) (1) · Painel sobre os Manuscritos do Mar Morto (Debate Moderno) (1) |
| 6 | Miguel, o Bravo | — |
| 6 | Reino Normando da Sicília | — |
| 6 | Sacro Império Romano-Germânico | — |
| 5 | Civilização do Vale do Indo | — |
| 5 | Condottieri | Companhias Livres (4) |
| 5 | Cátaros | Escrituras Cátaras (Visão de Isaías e Ceia Secreta de João) (1) · O Debate sobre a Existência Histórica dos Cátaros (1) · O Livro dos Dois Princípios (Liber de Duobus Principiis) (1) · Teologia Cátara (O Pai-Nosso Cátaro) (1) |
| 5 | Dinastia Qing | Koxinga (2) · Conquista de Xinjiang (1) |
| 5 | Guerra Anglo-Espanhola | — |
| 5 | Guerra Polaco-Sueca | Guerra da Lituânia (1) · Guerra da Livônia (1) · Guerra da Prússia Real (1) · Prelúdio (1) |
| 5 | Guerra de Independência da Grécia | — |
| 5 | Guerra dos Sete Anos | Guerra Franco-Indígena (3) |
| 5 | Guerras da Borgonha | — |
| 5 | Guerras Árabe-Israelenses | — |
| 5 | Harald Hardrada | — |
| 5 | História dos Fantasmas | De Spectris (Ludwig Lavater, 1569) (1) · Fantasmas Medievais (Thietmar de Merseburg) (1) · Os Primeiros Fantasmas (Suméria, Babilônia e Assíria) (1) · Plínio, o Jovem e a Casa Assombrada (1) |
| 5 | Hunos | — |
| 5 | Império Parta | — |
| 5 | Império Russo | Colonização Russa da América (1) · Conquista da Sibéria (1) · Gannibal (1) |
| 5 | Marinha Britânica | — |
| 5 | Núbia | Invasão Núbia do Egito (Piye) (1) · Invasão Romana da Núbia (1) |
| 5 | Origens da guerra | — |
| 5 | Povos indígenas da América do Norte | Grandes Planícies (2) |
| 5 | Ranking de samurais | — |
| 5 | Shinobi | — |
| 5 | Vida cortesã | Torneios (2) · Caça real (1) · Cortes Ocidentais (1) · Cortes Orientais (1) |
| 5 | Índia Britânica | Companhia das Índias Orientais (2) · Rebelião Indiana de 1857 (1) |
| 4 | Aleister Crowley | Absinthe e o Bairro Francês de Nova Orleans (1918) (2) · Boleskine House (2) |
| 4 | Casa de Habsburgo | — |
| 4 | Celtas antigos | — |
| 4 | China antiga | — |
| 4 | Civilização Minoica | — |
| 4 | Comércio Romano | — |
| 4 | Conflito Israel-Hezbollah | — |
| 4 | Conquistadores | Expedição de Narváez (1) |
| 4 | Etruscos | — |
| 4 | Formação das Monarquias Nacionais | Magna Carta (1) |
| 4 | Guerra Anglo-Americana de 1812 | Tecumseh (1) |
| 4 | Idade de Ouro Islâmica | — |
| 4 | Império Cazar | Guerras Árabe-Cazares (2) |
| 4 | Inklings (Lewis e Tolkien) | C.S. Lewis (2) · J.R.R. Tolkien (2) |
| 4 | Invasões Magiares | — |
| 4 | Lenda Arturiana | — |
| 4 | Marinha | — |
| 4 | Máfia | Máfia Americana (1) · Máfia Siciliana (1) · Tríades Chinesas (1) |
| 4 | Olmecas | La Venta (1) · San Lorenzo (1) |
| 4 | Período homérico | — |
| 4 | Programa Apollo | — |
| 4 | Revolução Marciana (ficção) | — |
| 4 | Taiwan | Povos indígenas (1) |
| 4 | Teologia Cristã | Doutrina em 90 segundos (3) · Sermões (1) |
| 4 | Vida do Soldado | — |
| 4 | Épiro antigo | — |
| 4 | Época Dourada da Pirataria | — |
| 4 | Índia antiga | Idade Védica (1) |
| 3 | Animais na história | — |
| 3 | Congresso de Viena | — |
| 3 | Cruzada de Marrocos (1578) | — |
| 3 | Declínio Carolíngio | — |
| 3 | Dinastia Jin | Jin Oriental (2) · Jin Ocidental (1) |
| 3 | Eslavos | Chegada aos Bálcãs (2) |
| 3 | Grécia Arcaica | — |
| 3 | Guerra Otomano-Valáquia | — |
| 3 | Guerra Romano-Seléucida | — |
| 3 | Guerra Russo-Japonesa | — |
| 3 | Guerra de Inverno (1939-1940) | — |
| 3 | Guerra de Pontiac | — |
| 3 | Guerra do Irã | — |
| 3 | Guerras Hussitas | — |
| 3 | História da Absinta | — |
| 3 | História da Arte | Giotto (1) · Rembrandt (1) |
| 3 | História da Prússia | — |
| 3 | Império Sassânida | — |
| 3 | Invasões Mongóis do Japão | — |
| 3 | Landsknechts | — |
| 3 | Línguas indo-europeias | — |
| 3 | Maravilhas do Mundo Antigo | — |
| 3 | Mercenários Suíços | — |
| 3 | Ordem Teutônica | — |
| 3 | Peste Negra | — |
| 3 | Povoamento das Américas | Caribe (1) |
| 3 | Rebelião de Shimabara | — |
| 3 | Reino Vândalo | — |
| 3 | Reinos pós-romanos da Britânia | Dumnónia (1) · Reino da Escócia (1) · Reino de Strathclyde (1) |
| 3 | Restauração Kenmu | — |
| 3 | Siquismo | — |
| 3 | Sultanato Mameluco | — |
| 2 | Arábia Pré-Islâmica | — |
| 2 | Balestreiros Genoveses | — |
| 2 | Biblioteca de Alexandria | — |
| 2 | Cisma do Oriente e Ocidente | — |
| 2 | Citas | — |
| 2 | Civilização Nurágica | — |
| 2 | Comércio na Mesopotâmia Antiga | — |
| 2 | Corinto | — |
| 2 | Credos e Confissões Cristãs | — |
| 2 | Crise medieval | — |
| 2 | Cultura de internet | — |
| 2 | Dezesseis Reinos | Antigo Qin (1) · Wei do Norte (1) |
| 2 | Divino Feminino (Sophia e Shekhinah) | Asherá (1) |
| 2 | Era Vitoriana | — |
| 2 | Esportes | — |
| 2 | Estepe Eurasiática | — |
| 2 | Exploração Antiga | Expedição Romana ao Nilo (Nero) (1) · Piteas de Massália (1) |
| 2 | Exército Sassânida | Cavalaria Sassânida (1) · Daylamitas (1) |
| 2 | Filisteus | — |
| 2 | Fraudes Financeiras | — |
| 2 | Germanos antigos | — |
| 2 | Guerra Civil Espanhola | — |
| 2 | Guerra Franco-Holandesa | — |
| 2 | Guerra Georgiano-Seljúcida | — |
| 2 | Guerra Irã-Iraque | — |
| 2 | Guerra Soviético-Afegã | — |
| 2 | Guerra das Rosas | — |
| 2 | Guerras Iugoslavas | — |
| 2 | Guerras de Independência Suíça | — |
| 2 | Guerras do Ópio | — |
| 2 | Herança de Roma | — |
| 2 | História da Alimentação | — |
| 2 | História do Iêmen | Insurgência Huthi (1) |
| 2 | Ilírios | Grande Revolta Ilíria (1) |
| 2 | Império Gurida | — |
| 2 | Império Hitita | — |
| 2 | Império Meda | — |
| 2 | Império Mogol | Akbar, o Grande (1) · Malik Ambar (1) |
| 2 | Império Neo-Assírio | — |
| 2 | Império Timúrida | — |
| 2 | Império Wari | — |
| 2 | Império do Mali | — |
| 2 | Impérios Berberes | — |
| 2 | Inquisição Espanhola | — |
| 2 | Jakob Böhme | A Alquimia Espiritual de Böhme (1) · A Teosofia de Böhme e O Caminho a Cristo (1) |
| 2 | Jogos de tabuleiro e cartas | — |
| 2 | Lendas samurai | — |
| 2 | Levante de Khmelnytsky | — |
| 2 | Lídios | — |
| 2 | Marinha samurai | — |
| 2 | Mercenários | — |
| 2 | Mitraísmo | A Liturgia de Mitras (Ascensão Mística) (1) |
| 2 | Mundo Medieval (Crusader Kings III) | — |
| 2 | Primeira Guerra dos Barões | — |
| 2 | Reino Ostrogodo | — |
| 2 | Reino da Boêmia | — |
| 2 | Reino de Mitani | Hurritas (povo) (1) |
| 2 | Reino de Yamhad | Idrimi de Alalakh (1) |
| 2 | Reinos de Chipre | — |
| 2 | Religião Grega | Xenia (Hospitalidade Sagrada) (1) |
| 2 | Revolta dos Camponeses de 1381 | — |
| 2 | Rus de Moscou | — |
| 2 | Sakoku | — |
| 2 | Samnitas | — |
| 2 | Sociedade Egípcia Antiga | — |
| 2 | Teotihuacan | — |
| 2 | Tiwanaku | — |
| 2 | Toltecas | — |
| 2 | Tércio Espanhol | — |
| 2 | Zapotecas | — |
| 2 | Últimas Resistências Samurai | — |
| 1 | Ainu | — |
| 1 | Albânia Caucasiana | — |
| 1 | Anne Conway | — |
| 1 | Anábase dos Dez Mil | — |
| 1 | Arameus | — |
| 1 | Argos antiga | — |
| 1 | Arthur Schopenhauer | — |
| 1 | As Origens do Gótico (Estética e Horror) | — |
| 1 | Astecas | Nezahualcoyotl (1) |
| 1 | Atenas Antiga | — |
| 1 | Austin Osman Spare | — |
| 1 | Baruch Spinoza | — |
| 1 | Basketmaker | — |
| 1 | Beócia antiga | — |
| 1 | Blackbeard | — |
| 1 | Budismo no Japão | — |
| 1 | Cahokia | — |
| 1 | Calendário Mesoamericano | — |
| 1 | Califado Fatímida | — |
| 1 | Calusa | — |
| 1 | Canato Avar | — |
| 1 | Carros de Guerra | — |
| 1 | Cartas de Amarna | — |
| 1 | Castelos Medievais | — |
| 1 | Catástrofe Climática de 536 | — |
| 1 | Cavaleiros Hospitalários | — |
| 1 | Cerco de Jerusalém (70 d.C.) | — |
| 1 | Chaco Canyon | — |
| 1 | Chavín de Huántar | — |
| 1 | China Moderna | — |
| 1 | Cisma Sunita-Xiita | — |
| 1 | Cisma entre Judaísmo e Cristianismo | — |
| 1 | Civilização de Jiroft | — |
| 1 | Civilização do Oxus (BMAC) | — |
| 1 | Colonização Romana | — |
| 1 | Colonização holandesa da Indonésia | — |
| 1 | Comanches | — |
| 1 | Comentários sobre criação de conteúdo | — |
| 1 | Commonwealth Polaco-Lituano | — |
| 1 | Comércio de escravos eslavos | — |
| 1 | Concílios Ecumênicos | — |
| 1 | Confederação Xiongnu | — |
| 1 | Conflitos na Irlanda do Norte | — |
| 1 | Conflitos no Oriente Médio | — |
| 1 | Contato Polinésio-Americano | — |
| 1 | Cossacos | — |
| 1 | Crise Geral do Século XVII | — |
| 1 | Crise de 1383-1385 | — |
| 1 | Cristianismo no Japão | — |
| 1 | Cultura Cicládica | — |
| 1 | Cultura do Cobre Antigo | — |
| 1 | Cumano-Quipchaques | — |
| 1 | Curiosidades da História Chinesa | — |
| 1 | Declínio do Budismo na Índia | — |
| 1 | Delfos | — |
| 1 | Descolonização do Império Britânico | — |
| 1 | Dilmun | — |
| 1 | Dinastia Médici | — |
| 1 | Dinastia Qin | — |
| 1 | Dinastia Tang | — |
| 1 | Ditmársia | — |
| 1 | Doutrina Monroe | — |
| 1 | Duelos | — |
| 1 | Dácios | — |
| 1 | Ebla | — |
| 1 | Egina | — |
| 1 | Emirado de Córdoba | — |
| 1 | Erupção do Vesúvio (79 d.C.) | — |
| 1 | Espadas militares japonesas | — |
| 1 | Espiritualismo Moderno | — |
| 1 | Estados Neo-Hititas | — |
| 1 | Exército Negro da Hungria | — |
| 1 | Família Imperial do Japão | — |
| 1 | Francis Drake | — |
| 1 | França Medieval | — |
| 1 | Frígia Antiga | — |
| 1 | Fugger | — |
| 1 | Galloglass | — |
| 1 | Gauleses | — |
| 1 | Gendarmes Franceses | — |
| 1 | Genocídio Circassiano | — |
| 1 | Georges Bataille | — |
| 1 | Godos | — |
| 1 | Grande Canal da China | — |
| 1 | Grande Jogo | — |
| 1 | Grupo Wagner | — |
| 1 | Guerra Anglo-Francesa | — |
| 1 | Guerra Bizantino-Sassânida | — |
| 1 | Guerra Civil Síria | — |
| 1 | Guerra Dano-Hanseática | — |
| 1 | Guerra Durrani-Marata | — |
| 1 | Guerra Escaniana | — |
| 1 | Guerra Escocesa-Norueguesa | — |
| 1 | Guerra Franco-Flamenga | — |
| 1 | Guerra Fria | Macarthismo (1) |
| 1 | Guerra Gótica | — |
| 1 | Guerra Jacobita na Irlanda | — |
| 1 | Guerra Lelantina | — |
| 1 | Guerra Polaco-Otomana | — |
| 1 | Guerra da Coreia | — |
| 1 | Guerra da Fronteira Sul-Africana | — |
| 1 | Guerra da Independência do Zimbábue | — |
| 1 | Guerra do Iraque (2003) | — |
| 1 | Guerra dos Nove Anos | — |
| 1 | Guerras Civis do Sudão | — |
| 1 | Guerras Galo-Romanas | — |
| 1 | Guerras Jacobitas | — |
| 1 | Guerras Sírias | — |
| 1 | Guerras da Chechênia | Primeira Guerra da Chechênia (1) |
| 1 | Guerras do Decão | — |
| 1 | Guerreiras Samurai | — |
| 1 | Gurkhas | — |
| 1 | Halicarnasso | — |
| 1 | Hashashins | — |
| 1 | História da Batata | — |
| 1 | História da Bíblia | — |
| 1 | História da Pimenta | — |
| 1 | História do Chocolate | — |
| 1 | História do Milho | — |
| 1 | História dos videogames | — |
| 1 | Hititas | — |
| 1 | Hohokam | — |
| 1 | Hussardos Alados | — |
| 1 | Ibn Fadlan | — |
| 1 | Icenos | — |
| 1 | Idade das Trevas Global | — |
| 1 | Immanuel Kant | Kant e o Misticismo (Swedenborg) (1) |
| 1 | Império Corásmio | — |
| 1 | Império Gaznávida | — |
| 1 | Império Khmer | — |
| 1 | Império Kushan | — |
| 1 | Império Majapahit | — |
| 1 | Império Marata | — |
| 1 | Império Seljúcida | — |
| 1 | Isaac Newton | — |
| 1 | Islamização da Indonésia | — |
| 1 | Itália medieval | — |
| 1 | Japoneses no exterior | — |
| 1 | Johannes Bureus e a Runologia Esotérica | — |
| 1 | Johannes Schiltberger | — |
| 1 | Judaísmo | — |
| 1 | Julgamentos de animais | — |
| 1 | Karl Marx | — |
| 1 | Legião Tchecoslovaca | — |
| 1 | Liga Hanseática | — |
| 1 | Lícia Antiga | — |
| 1 | Magan (Magan/Makkan) | — |
| 1 | Manejo do fogo indígena | — |
| 1 | Maniqueísmo | — |
| 1 | Mansa Musa | — |
| 1 | Marajoara | — |
| 1 | Meteoros na História | — |
| 1 | Moche | — |
| 1 | Moldávia de Estêvão, o Grande | — |
| 1 | Mormonismo | — |
| 1 | Mosqueteiros do Rei | — |
| 1 | Muisca | — |
| 1 | Nanman | — |
| 1 | Nazca | — |
| 1 | Ninjutsu | — |
| 1 | Numismática Antiga | — |
| 1 | Palestina antiga | — |
| 1 | Panorama de conflitos globais | — |
| 1 | Partições da Polônia | — |
| 1 | Pechenegues | — |
| 1 | Peregrinação Medieval | — |
| 1 | Pictos | — |
| 1 | Piratas Berberes | — |
| 1 | Política Chinesa Contemporânea | — |
| 1 | Polônia Piasta | — |
| 1 | Pomério Romano | — |
| 1 | Poverty Point | — |
| 1 | Povo Romani | — |
| 1 | Povo hebreu | — |
| 1 | Povos do Zagros | — |
| 1 | Primeira Guerra Civil Sudanesa | — |
| 1 | Primeiro Império Búlgaro | — |
| 1 | Protestantismo | — |
| 1 | Pseudociência e Conspirações | — |
| 1 | Puyi | — |
| 1 | Pânico Satânico | — |
| 1 | Querela das Investiduras | — |
| 1 | Quipu | — |
| 1 | Rebelião Percy (1403) | — |
| 1 | Rebelião Zanje | — |
| 1 | Rebeliões Huguenotes | — |
| 1 | Reforma Eleitoral de 1832 | — |
| 1 | Reino Borgonhão | — |
| 1 | Reino Himiarita | — |
| 1 | Reino Lombardo | — |
| 1 | Reino Nabateu | — |
| 1 | Reino Visigodo | — |
| 1 | Reino da Armênia | — |
| 1 | Reino de Aksum | — |
| 1 | Reino de Anitta (Precursor Hitita) | — |
| 1 | Reino de Ryukyu | — |
| 1 | Reino de Urartu | — |
| 1 | Reino do Bósporo | — |
| 1 | Reiters Negros | — |
| 1 | República de Veneza | — |
| 1 | Restauração Meiji | — |
| 1 | Retrospectiva Anual | — |
| 1 | Revolta dos Macabeus | — |
| 1 | Revolução Alemã | — |
| 1 | Revolução Iraniana | — |
| 1 | Risorgimento | — |
| 1 | Rússia Medieval | — |
| 1 | Samos | — |
| 1 | Segunda Guerra Civil Sudanesa | — |
| 1 | Segunda Guerra da Chechênia | — |
| 1 | Segundo Império Búlgaro | — |
| 1 | Seminoles | — |
| 1 | Sigmund Freud e a Psicanálise | A Pulsão de Morte e Georges Bataille (1) |
| 1 | Sogdiana | — |
| 1 | Sohei | — |
| 1 | Suevos | — |
| 1 | Sultanato de Delhi | — |
| 1 | Tarascos | — |
| 1 | Tempo das Perturbações | — |
| 1 | Tengrismo | — |
| 1 | Tessália antiga | — |
| 1 | Teuchitlán | — |
| 1 | Tratado de Tordesilhas | — |
| 1 | Tratados militares | — |
| 1 | Triunfo Romano | — |
| 1 | Trácios | — |
| 1 | Tráfico Transatlântico de Escravos | — |
| 1 | Tupinambá | — |
| 1 | Turquificação da Anatólia | — |
| 1 | Ugarit | — |
| 1 | Vampiros (Origens Históricas) | — |
| 1 | Vlad III, o Empalador | — |
| 1 | Vândalos | — |
| 1 | Wakō | — |
| 1 | War Plan Red | — |
| 1 | William Blake | — |
| 1 | Yukio Mishima | — |
| 1 | Zoroastrismo | — |
| 1 | Ártico | — |
| 1 | Çatalhöyük | — |

### Sobreposições ainda por resolver

Abertas na aprovação dos lotes 232-249 (reabertura dos vinte canais):

- **`Guerra Civil Espanhola` (tema-raiz novo, lotes 232-233, 2 linhas) ×
  `Segunda Guerra Mundial > Guerra Civil Espanhola` (subtema, 1 linha,
  1936-1939)** — a linha antiga é um episódio da série "Eastern Front
  Week-by-Week Prelude" do Kings and Generals, que trata a guerra como prelúdio
  da Segunda Guerra; as novas são de uma série dedicada do mesmo canal. O
  catálogo trata guerra civil como tema-raiz (Americana, Inglesa, Russa, Síria),
  daí o tema novo. **A linha antiga não foi migrada: está travada de um ciclo
  anterior.** Mesmo nome em dois lugares, com tratamentos diferentes — é a
  armadilha do "mesmo nome de subtema em dois temas-raiz" do `protocolo.md`.
- **`Guerras Civis do Sudão` (tema-raiz novo, lote 244, 1 linha) ×
  `Primeira Guerra Civil Sudanesa` (1955-1972) × `Segunda Guerra Civil
  Sudanesa` (1983-2005)** — o vídeo novo cobre as três guerras de uma vez e não
  cabia em nenhum dos dois temas existentes; a terceira guerra (2023-) não tem
  tema próprio. Três temas-raiz para o mesmo país, um deles panorâmico.
  Alternativa não aplicada: transformar os dois antigos em subtemas do novo, ou
  criar `Terceira Guerra Civil Sudanesa`.
- **`Império Otomano > Skanderbeg` (subtema novo, lote 232)** — a linha antiga
  do catálogo sobre o mesmo personagem ("Rise of Skanderbeg", 1443-1468) está
  sob `Império Otomano` **sem** subtema, e está travada de um ciclo anterior.
  O par ficou dividido; a correção exige autorização para sobrescrever célula
  travada.
- **`Espanha` como termo de região** — a aproximação `Península Ibérica` para a
  Espanha passou de longe do critério de segunda ocorrência (Guerra Civil
  Espanhola ×2, Villaviciosa, Reconquista, Inquisição Espanhola, Tércio,
  Guerra Anglo-Espanhola, Guerra de Sucessão Espanhola). Não criado: criar o
  termo implicaria reclassificar linhas antigas travadas.
- **`Historiografia > Historiadores gregos` com tratamentos opostos** — a linha
  "Herodotus - A Quick Look at his Life and Work" está como `Extra` (sem anos),
  e "HoP 500b Melissa Lane on Herotodus and Thucydides" (lote 248) entrou na
  linha do tempo com 484-400 a.C. Pelo teste das Decisões fechadas, a vida de
  dois historiadores é datável, logo não é `Extra`. A linha antiga está travada.
- **`Dinastia Zhou > Estados Combatentes`: Parte 1 engloba a Parte 2** — a linha
  "The Warring States Period Explained - Part 1" ficou com 400-221 a.C. e a
  Parte 2 (lote 242) com 338-221 a.C. Pelo título, a Parte 1 deveria terminar
  onde a Parte 2 começa. Linha antiga travada, não reaberta.
- **`Império Otomano > Mehmed II` recebendo episódios de um podcast cujo tema
  é `Império Bizantino`** — os episódios 339 e 341 do The History of Byzantium
  (lote 238) são posteriores a 1453 e tratam de política otomana, então foram
  para `Império Otomano`, enquanto as outras ~400 linhas do canal estão em
  `Império Bizantino` — inclusive "The Rise of the Ottomans, Part 1 e 2", que
  trata dos otomanos vistos de dentro do império que ainda existia. Decisão
  consciente, registrada aqui para não parecer descuido.

- **Cluster "Nicholas Eymerich" espalhado em 3 subtemas de 2 temas-raiz
  diferentes**: `A Inquisição contra a Alquimia (Nicholas Eymerich, 1396)`
  (Hermetismo, lote 220), `Manuais Inquisitoriais e a Heresia Mágica
  (Nicholas Eymerich)` (Caça às Bruxas, lote 221) e `As Origens da
  Inquisição Medieval` (Caça às Bruxas, lote 223) — mesmo inquisidor
  aragonês, três ângulos (o tratado sobre alquimia, o manual inquisitorial
  geral, as origens institucionais da Inquisição), sem termo guarda-chuva
  comum. Achado na parada do lote 215 + lotes 220-223. Não fundido.
- **`Manuais de Exorcismo e Necromancia (pré-1614)` (Renascimento, lote 217)
  × `Necromancia e Grimórios Medievais` (Escolástica Medieval, lote 216)**
  — mesma família de assunto (grimórios de necromancia/exorcismo), tratada
  em dois temas-raiz diferentes por corte de época (medieval vs. início da
  era moderna). Achado na parada dos lotes 216-219. Não fundido.
- **`Renascimento` como tema-raiz guarda-chuva do canal ESOTERICA já cobre
  a Europa continental inteira (Agripa, Paracelso, Trithemius, Del Rio, os
  Rosacruzes) mais as colônias americanas (John Winthrop, o Jovem, lote
  219)** — encaixe por continuidade temática (ocultismo europeu exportado
  para a Nova Inglaterra), não por época/lugar. Pode precisar de critério
  mais claro se o canal continuar trazendo conteúdo americano.
- **`Aristotelismo Pós-Aristóteles` (Filosofia Helenística e Romana, lote 211)
  × `Sucessores de Platão e Aristóteles` (Aristóteles, lote 212) — mesma
  pergunta ("o que aconteceu com o aristotelismo depois de Aristóteles"),
  faixas parcialmente sobrepostas, tratada em dois temas-raiz diferentes.**
  Achado na parada dos lotes 209-213. Não fundido.
- **`Platonismo Médio (Painel)` × `O Renascimento Platônico (Eudoro,
  Alcínoo e Numênio)`**, ambos sob `Filosofia Helenística e Romana` — mesmo
  movimento filosófico (Platonismo Médio) visto por um episódio-painel
  genérico e um episódio-conteúdo com os três nomes fundadores. Não é
  duplicata exata, mas família apertada.
- **`Estética Antiga (De Platão a Proclo)` ficou sob `Neoplatonismo
  Tardo-Antigo`** (ancorado pela ponta mais recente, Proclo), mas toca
  Platão diretamente e poderia caber em `Platão` também — decisão de
  fronteira, não erro.
- **Quatro temas-raiz novos cobrindo períodos adjacentes/contínuos**
  (`Platão` → `Aristóteles` → `Filosofia Helenística e Romana` →
  `Neoplatonismo Tardo-Antigo`, com `Cristianismo Primitivo` interpolado)
  formam uma cadeia cronológica só, sem um tema "guarda-chuva" que uniria a
  filosofia grega/romana antiga inteira. Não bloqueante, só um padrão
  notável desta parada.
- **`Traduções do Árabe para o Latim` (Filosofia Islâmica, lote 208) ×
  `Movimento de Tradução para o Latim` (Escolástica Medieval, lote 205) —
  mesmo evento histórico, mesma faixa (1085-1200).** Achado na parada dos
  lotes 205-208: o movimento de tradução de Toledo (fontes árabes/gregas
  vertidas para o latim) aparece em dois temas-raiz diferentes, cada um
  olhando o mesmo evento por um lado da fronteira cultural (o lado que
  produziu o texto x o lado que recebeu a tradução). Não fundido.
- **`Gersônides` (solo) × `Gersônides e Hasdai Crescas` (conjunto) ×
  `Hasdai Crescas` (solo)**, e **`Ibn 'Arabī (Misticismo)` (solo) ×
  `Sufismo Filosófico (Ibn 'Arabī e Rūmī)` (conjunto)** — mesmo padrão já
  visto com Alberto Magno/Tomás de Aquino e W.E.B. Du Bois: o mesmo
  pensador ganha subtema solo e subtema conjunto quando o canal trata dele
  sozinho num episódio e emparelhado com outro pensador em outro. Não
  bloqueante.
- **`Maimônides` é citado em 5 subtemas diferentes de `Filosofia Judaica
  Medieval`** (solo, mais coautor em `Neoplatonismo Judaico`, `Liberdade e
  Astrologia`, `Ética e Judaísmo` e `Controvérsia Maimonidiana`) — maior
  fragmentação de um único pensador no catálogo até agora. Não é erro (cada
  subtema reflete um episódio/ângulo diferente do canal), só registrado.
- **Cluster "(Debate Moderno)"/"(Painel/Entrevista)" chegou a 13 subtemas**
  entre `Escolástica Medieval` e `Filosofia Islâmica` (entrevistas sobre
  tópicos sem data própria, cada uma com subtema só seu). Pendência
  herdada da parada dos lotes 200-204, ainda sem decisão de consolidação.
- **Cluster "Século XII/XIII" somou-se ao cluster "Século XIV" já
  registrado**: `Escola de Chartres`, `Problema dos Universais (Séc. XII)`,
  `Física/Lógica/Psicologia/Ética do Século XIII` — mesma família de
  subtemas por corte de século que já preocupava na parada anterior, agora
  maior.
- **`Bhagavad-Gītā` × `Mahābhārata: Dharma e Ética` × `Origens do Karma
  (Upaniṣads e Bhagavad-Gītā)` — mesma obra em três subtemas.** Achado na
  parada dos lotes 200-204 (canal History of Philosophy Without Any Gaps,
  série HPI): a Bhagavad-Gītā é uma seção do próprio Mahābhārata, e o
  terceiro subtema volta a citá-la. Faixas quase idênticas (-400/-200 a
  200). Candidato a consolidar num subtema-guarda-chuva "Mahābhārata (incl.
  Bhagavad-Gītā)". Não resolvido.
- **Escolas indianas fragmentadas em muitos subtemas por escola.** Achado na
  mesma parada: `Nyāya` em 5 subtemas (`Escola Nyāya (Gautama)`, `Escola
  Nyāya (Painel)`, `Nyāya: Lógica da Inferência`, `Nyāya: Percepção`,
  `Nyāya: Self e Mente`), `Vaiśeṣika` em 3 e `Mīmāṃsā` em 3 — o padrão surge
  porque cada episódio do HPI vira um subtema próprio quando não há data
  para justificar consolidação por período. Não resolvido; vale reavaliar
  se compensa uma consolidação por escola.
- **Padrão "(Debate Moderno)"/"(Painel/Entrevista)" usado 8+ vezes** para
  entrevistas sem data em temas diferentes, cada uma com subtema próprio
  (`Ceticismo Medieval (Debate Moderno)`, `Estética Medieval (Debate
  Moderno)`, `Filosofia e a Trindade (Debate Moderno)`, etc., mais o lado
  indiano com "(Painel/Entrevista)"). Não ficou definido se deveriam
  convergir num subtema único por tema-raiz (ex. "Entrevistas e Debates
  Modernos"), como já existe `Avisos do canal` para o canal inteiro, ou se
  o subtema próprio por episódio (o que fiz) é preferível. Decisão de
  escopo em aberto.
- **Cluster "Século XIV" com 4 subtemas próximos em `Escolástica Medieval`**:
  `Introdução ao Século XIV (Nominalismo e Voluntarismo)`, `Física do
  Século XIV (Ockham, Buridan, Oresme, Marchia)`, `Lógica do Século XIV
  (Obrigações e Paradoxos)` e `Escolástica na Europa Central (Viena e
  Praga)` — não são duplicatas (cada um cobre um ângulo diferente do mesmo
  recorte de tempo, confirmado inclusive pela própria organização do site
  do podcast em uma seção "Fourteenth Century Philosophy"), mas formam uma
  família apertada que pode confundir numa leitura rápida da Lista C. Não
  resolvido.
- **`Alberto Magno` × `Alberto Magno e Tomás de Aquino` × `Tomás de
  Aquino`** — três subtemas para dois pensadores com vidas sobrepostas
  (1200-1274/1280), mesmo padrão já visto com W.E.B. Du Bois. Não
  bloqueante, só registrado.
- **`Império Bizantino` acumulou três subtemas de recorte cronológico que
  podem se sobrepor nas bordas.** Achado na parada dos lotes 196-199 (canal
  History of Philosophy Without Any Gaps): `Filosofia Bizantina (Era do
  Iconoclasmo)` (~330-900, lote 199), `Filosofia Bizantina (Era Comnena)`
  (~1000-1330, lote 198) e `Filosofia Bizantina Tardia` (~1296-1486, lote
  197) — as fronteiras entre os três foram decisões de julgamento na hora
  de classificar, não uma periodização historiográfica padronizada com
  limites fixos. Pode fazer sentido consolidar num só com sub-recortes
  nomeados, ou manter os três separados. Não resolvido.
- **`Etnofilosofia e Debate sobre a Filosofia Africana` é a maior
  consolidação de subtema num lote só até agora** (13 de 25 linhas do lote
  198, canal History of Philosophy Without Any Gaps) — 6 dessas 13 são
  `chute` puro, sem nenhuma pessoa ou país nomeado na evidência, usando a
  mesma faixa compartilhada `1945-2000` só por pertencerem ao mesmo arco
  temático (a fundação da etnofilosofia por Tempels, a crítica de
  Hountondji, etc.). Não é erro, mas é o caso mais fraco de consolidação
  por guarda-chuva registrado até agora — vale reavaliar se a técnica se
  repetir em outro cluster igualmente disperso.
- **`Renascimento Italiano` (12 vídeos, lotes 194-195) tem faixa interna
  muito variável, de 1370 a 1642, dependendo de quem é citado em cada
  episódio.** Guarda-chuva criado porque a própria descrição do canal chama
  a série de "nosso finale do Renascimento Italiano" (History of Philosophy
  Without Any Gaps) — melhor do que fragmentar em 9-12 subtemas de pessoa
  isolada, mas um leitor vendo `Ano` oscilar tanto sob o mesmo nome de
  subtema pode estranhar. Não é erro (cada faixa reflete a evidência do
  próprio vídeo), só registrado.
- **`W.E.B. Du Bois` acumulou 4 faixas diferentes em 3 lotes** (lotes
  193-194): vida inteira (1868-1963), o recorte do próprio título "1920-1963"
  (HAP 84), "virada do século" (1895-1905, HAP 68) e "os anos 1890" (1890-1899,
  HAP 66) — todas ancoradas na evidência de cada vídeo específico, mas o
  mesmo subtema com quatro janelas de tempo diferentes convida confusão.
- **Cluster de nomes pan-africanistas do séc. XIX com fronteiras temporais
  sobrepostas**: `Raízes do Nacionalismo Negro` (Douglass+Crummell,
  1818-1898), `Alexander Crummell` (sozinho, 1819-1898) e `Academia Negra
  Americana` (fundada por Crummell, 1897-1928) tocam a mesma pessoa em
  janelas que se cruzam. Achado na parada dos lotes 192-195; não
  consolidado.
- **`Tolerância Religiosa` existe duas vezes, em temas-raiz diferentes.**
  Achado na parada dos lotes 188-191 (canal History of Philosophy Without Any
  Gaps): `364n1Gb4aO0` (Sebastian Castellio, 1515-1563) ficou sob
  `Renascimento`, e `XnHo-FjrcJU` (Maria Rosa Antognazza sobre Locke/Leibniz,
  1517-1716) ficou sob `Filosofia Moderna` — mesmo nome de subtema, mesmo
  assunto de fundo (tolerância religiosa na Europa), só que em épocas que a
  periodização do próprio catálogo já trata como temas-raiz separados. Não
  fundido: cada um está corretamente encaixado na época do seu tema-raiz, mas
  o nome idêntico convida a pensar que é o mesmo nó. Decisão pendente:
  manter os dois, renomear um, ou criar um tema-raiz "Tolerância Religiosa"
  próprio que os absorva.
- **`Feminismo Negro` partido em dois subtemas por década, nomes quase
  idênticos.** Achado na mesma parada: `Feminismo Negro dos Anos 1970
  (Combahee River Collective)` (lote 190/191, 1970-1979) e `Feminismo Negro
  (bell hooks e Patricia Hill Collins)` (lote 189, 1981-2000) cobrem a mesma
  linhagem intelectual em gerações sequenciais — o próprio canal tratou os
  dois em episódios separados, o que justifica manter linhas distintas, mas
  os nomes convidam confusão numa sessão futura que não abrir os dois de
  uma vez. Não consolidado.
- **`Ceticismo Renascentista` (novo, lote 190) × `Ceticismo Francês` (já
  existente, sob `Filosofia Moderna`, era de Pascal ~1660)** — mesmo domínio
  conceitual (ceticismo francês), épocas diferentes por conta da própria
  periodização do catálogo (Montaigne é pré-`Filosofia Moderna`, que só
  começa com Descartes). Nomes parecidos o bastante para checar com cuidado
  antes de propor um terceiro.
- **`Filosofia Política Huguenote` (novo, lote 191) × `Rebeliões Huguenotes`
  (já existente, outro canal)** — mesma raiz de nome ("huguenote"), assuntos
  diferentes (teoria política monarcômaca vs. conflito militar). Mantidos
  separados de propósito; registrado para não confundir numa busca futura
  por "huguenote" na Lista C.
- **Região `Global` na linha de Frantz Fanon (3 vídeos, lote 191)** — Fanon
  nasceu na Martinica, psiquiatra na Argélia, escreveu e morreu associado à
  França; `Global` evita escolher errado, mas pode ser genérico demais.
  `Caribe` (origem) ou `Norte da África` (onde a obra mais influente,
  *Wretched of the Earth*, nasceu do contexto da Guerra da Argélia) são
  alternativas não avaliadas com o humano.
- **🔴 `Dinastia Zhou > Cem Escolas do Pensamento` está com 53 vídeos (era 46
  na aprovação dos lotes 184-187) e engloba cinco escolas filosóficas
  rivais** (canal History of Philosophy Without Any Gaps). O termo foi criado
  pelo Kings and Generals com 1 vídeo; o canal de filosofia já acrescentou 52
  em oito lotes, todos indistintos: confucionismo (Confúcio, Mêncio, Xunzi),
  moísmo (Mozi, moístas tardios), daoísmo (Laozi, Zhuangzi), legalismo (Shang
  Yang, Han Feizi) e Escola dos Nomes (Gongsun Long), mais Sunzi e Yang Zhu.
  Equivale a um subtema único "Filosofia Grega" cobrindo Platão, Aristóteles,
  estoicos, epicuristas e céticos juntos. **Como é subtema, não há
  granularidade possível abaixo dele** — a saída seria promovê-lo a tema-raiz
  com as cinco escolas como subtemas, mas isso mexeria na linha travada do
  Kings and Generals que criou o termo e **exige autorização escrita
  explícita do humano** (ver `protocolo.md`, "Linhas travadas"). Não feito na
  aprovação dos lotes 184-187 nem na dos lotes 188-191, pelo mesmo motivo — a
  pendência só cresce a cada ciclo que a série HPC continuar. A série ainda
  deve render
  ~10 episódios, então o custo da migração cresce a cada lote.
- **`Segunda Escolástica` (novo, lote 187) × `Escolástica Medieval` (já
  existente)** — criados como dois temas-raiz irmãos, cobrindo a fase dos
  séculos XI-XIV (medieval, europeia) e a dos séculos XVI-XVII (ibérica).
  Decisão deliberada, mas a alternativa (um tema só, com subtemas de fase)
  não foi avaliada com o humano.
- **`Dinastia Zhou` como tema-pai de conteúdo filosófico que extrapola a
  dinastia** — a Zhou terminou em 256 a.C., mas parte do pensamento clássico
  chinês discutido pelo canal se estende à Han. Uma linha (yin-yang, lote
  185) chegou a declarar faixa até 220 d.C. sob esse tema e foi estreitada na
  aprovação; o risco reaparece a cada episódio sobre conceitos que
  atravessam Zhou e Han.
- **`Dinastia Zhou > Cem Escolas do Pensamento` × `Tratados militares`** — a
  Arte da Guerra de Sunzi (lote 185) ficou em Cem Escolas porque o vídeo a
  enquadra como "daoísmo aplicado", mas `Tratados militares` já existe no
  catálogo (1 vídeo, manuais romanos/medievais europeus, 100-1000) e é o
  gênero literal da obra. Alternativa registrada na nota da linha.
- **Confúcio datado pela pessoa, Laozi datado pelo texto** — inconsistência
  aparente entre linhas do mesmo canal, com razão declarada nas notas: a
  historicidade de Confúcio é firme (551-479 a.C.), a de Laozi é disputada,
  então os episódios do Daodejing usam a datação do texto (c. 400-300 a.C.,
  manuscrito de Guodian) em vez da figura lendária.
- **Colisão de nome de subtema entre temas diferentes**: `Segunda Guerra
  Mundial > Campanha da Itália (1943-1945)` (novo, lote 183, canal Invicta)
  e `Napoleão Bonaparte > Campanha da Itália` (já existente, Epic History —
  a campanha napoleônica de 1796-1797) usam o mesmo nome-base "Campanha da
  Itália" para eventos de séculos diferentes. Não é duplicata (assuntos
  genuinamente distintos, temas-raiz diferentes), mas o nome sozinho não
  desambigua — só o parêntese "(1943-1945)" que acrescentei evita a
  confusão. Mesmo tipo de cluster de nomes parecidos já documentado para
  `Guerra Romano-Seléucida`/`Guerras Sírias`.
- **`Cerco de Jerusalém (70 d.C.)` (tema-raiz, lote 182, canal Invicta) tem
  1 vídeo só** — mesmo padrão já sinalizado para `Erupção do Vesúvio (79
  d.C.)` e `Harald Hardrada`. Poderia ter sido subtema sob `Império
  Romano`, mantido tema-raiz próprio por precedente.
- **Divergência entre dois vídeos da mesma série sobre a mesma data**: a
  compilação "Avenging Varus - The Germanic Wars [FULL DOCUMENTARY]" (lote
  180) descreve a Parte 6 ("Fate of Arminius and Germanicus") como
  ocorrendo em "16 AD" na própria descrição, mas o vídeo standalone dessa
  parte (lote 180 também) tem "(17 AD)" no próprio título. Cada linha do
  catálogo ficou fiel à sua própria evidência (a compilação com faixa até
  16, o standalone com 17) — as duas descrevem o desfecho da mesma guerra
  com anos diferentes, sem que uma tenha sido corrigida contra a outra.
- **`Harald Hardrada` (tema-raiz novo, lote 179, canal Invicta) vs. `Era
  Viking` (já existente, 11 vídeos, sem subtemas)** — criado um tema-raiz
  dedicado para as 5 linhas sobre a saga de Hardrada em vez de propor um
  subtema `Harald Hardrada` sob `Era Viking`. Mesmo tipo de decisão
  estrutural já aceita para `Napoleão Bonaparte` (separado de `Guerras
  Napoleônicas`), mas essa alternativa não foi checada antes de decidir.
  Aprovado no ciclo 176-179, mas vale revisão futura se `Era Viking`
  crescer muito com conteúdo adjacente.
- **`Erupção do Vesúvio (79 d.C.)` (tema-raiz, lote 176, canal Invicta) tem
  1 vídeo só** — poderia ter sido um subtema sob `Império Romano` em vez de
  tema-raiz próprio. Mantido como está, seguindo o precedente de `Guerra de
  Inverno (1939-1940)` (evento único vira tema-raiz quando é o tipo de
  assunto que pode ganhar mais vídeos depois).
- **`Guerra Romano-Seléucida` (novo, lote 172, canal Invicta) soa parecido mas
  é um conflito diferente de `Guerras Sírias` (já existente, HistoryMarche)**
  — a primeira é a guerra de Roma contra Antíoco III (192-188 a.C., inclui a
  Batalha das Termópilas de 191 a.C.), a segunda são as seis Guerras Sírias
  entre selêucidas e ptolomeus pela Cele-Síria (séc. III-II a.C.). Mesmo nome
  "selêucida/síria" no título, povos e datas diferentes — cluster de nomes
  parecidos, mesmo padrão de "Idade das Trevas" (vários assuntos, mesmo
  rótulo aproximado). Não fundir; só ficar atento na hora de classificar.
- **`Exército Sassânida` (novo, lote 174, canal Invicta) é adjacente a
  `Império Sassânida` (já existente, Thersites the Historian/HistoryMarche,
  mesma faixa 224-651 d.C., região Irã)** — verificado depois de criar o
  termo, não antes. Mantido separado por analogia ao par já aceito
  `Império Romano`/`Exército Romano` (o segundo é o ângulo institucional/
  militar de uma unidade específica — os Daylamitas —, não uma narrativa do
  império inteiro). Split defensável, mas vale revisar se `Exército
  Sassânida` crescer para além de uma unidade só.
- **`Fronteiras do Império` (novo subtema, lote 173, sob `Império Romano`)
  é genérico demais** — criado para um vídeo ('What Was Rome's Most Remote
  Outpost?') cuja evidência disponível não nomeia o posto avançado nem cita
  data; pode se sobrepor a `Britânia romana`, `Limes Germânico (Fronteira do
  Reno)` ou `Invasão Romana da Escócia (Agrícola)` dependendo do que o vídeo
  realmente trata. Revisar se o assunto real for identificado.
- **`Assíria Antiga > Exército Assírio` (lote 163, faixa 2000-609 a.C.) e
  `Assíria Antiga > Panorama Assírio (curso)` (lote 165, faixa 2025-609
  a.C.) cobrem quase a mesma janela inteira da história assíria** — um pela
  lente militar, outro pelo vídeo-resumo geral do canal. Não é erro (são
  vídeos genuinamente diferentes), mas as faixas quase idênticas merecem
  atenção numa sessão futura.
- **`Civilização de Jiroft` (novo, lote 164) é geograficamente adjacente a
  `Elam Antigo` (lote 161)** — ambas culturas do sudeste/sul do Irã na
  Idade do Bronze, mas distintas (Jiroft é anterior/à margem da civilização
  elamita propriamente dita). Registrado, sem fusão.
- **Família de temas "parceiros comerciais do Golfo com a Mesopotâmia":
  `Dilmun` (Barein, lote 165) e `Magan (Magan/Makkan)` (Omã/EAU, lote 164)**,
  criados em lotes consecutivos — cada um é um lugar genuinamente distinto,
  não duplicam, mas formam um cluster reconhecível.
- **`Suméria Antiga > Kish` e `Império Acadiano` (ambos novos, lotes 161-162,
  canal History with Cy) são adjacentes, não duplicados** — Sargão de Acádia
  começou a carreira em Kish antes de fundar o Império Acadiano, então os
  dois temas cobrem fases sequenciais do mesmo arco histórico. Registrado,
  sem fusão.
- **`Babilônia Antiga > Mari` (novo, lote 162) e `Babilônia Antiga > Período
  Paleobabilônico` (lote 159) são uma zona cinzenta.** Mari é um reino
  amorita distinto, com dinastia própria (Zimri-Lim), contemporâneo — não
  parte — da Babilônia da Primeira Dinastia, mas o vídeo do canal o enquadra
  como "Ancient Sumer / Akkad / Babylonia" e sua destruição por Hammurabi
  (c. 1760 a.C.) é o desfecho do enredo. Mantido como subtema próprio dentro
  de `Babilônia Antiga`, não fundido com `Período Paleobabilônico`.
- **Cluster de nomes parecidos em torno de "Idade das Trevas": `Idade das
  Trevas Grega` (novo, subtema de `Grécia antiga`, lote 161) / `Idade das
  Trevas` (subtema já existente de `Historiografia`, sobre a Hipótese do
  Tempo Fantasma/pseudo-história) / `Idade das Trevas Global` (tema-raiz já
  existente, mesmo campo pseudo-histórico).** Os três descrevem assuntos
  diferentes — um é o período histórico real da Grécia pós-micênica
  (1100-750 a.C.), os outros dois são sobre teorias pseudo-históricas
  modernas — nomeados deliberadamente distintos, mas é o mesmo tipo de
  armadilha de leitura já registrada para "Jogos retrô" vs "História dos
  videogames".
- **Família de temas Extra atemporais sobre a Mesopotâmia: `Sociedade
  Mesopotâmica` (novo, lote 160) e `Comércio na Mesopotâmia Antiga` (já
  existente).** Um é um bucket amplo (cultura, religião, língua, realeza);
  o outro é específico de comércio. Sem sobreposição direta, mas formam uma
  família de temas correlatos que pode merecer consolidação se crescer.
- **Cluster de três principados romenos/moldavos, todos região `Bálcãs`:
  `Guerra Otomano-Valáquia` (Vlad Țepeș, 1462, lote 152), `Moldávia de
  Estêvão, o Grande` (Vaslui 1475, lote 158) e `Miguel, o Bravo`
  (unificação Valáquia/Transilvânia/Moldávia, 1595-1601, lote 157).** Não
  é erro — são regentes e períodos genuinamente diferentes —, mas os três
  nomes parecidos (todos sobre principados romenos medievais/modernos)
  são uma armadilha de leitura à espreita numa sessão futura.
- **`Sultanato de Delhi` (novo, lote 154) e `Sultanato Mameluco` (existente,
  Egito) compartilham o nome "Mameluco"** — a dinastia de Razia Sultana em
  Delhi também é chamada de "Mamluk/Slave Dynasty" nas fontes, mas é uma
  linhagem inteiramente diferente da dos Mamelucos egípcios/levantinos
  (que enfrentaram os mongóis em Ain Jalut, lote 156). Não é erro de
  classificação — os temas estão corretamente separados —, mas o nome
  compartilhado é uma armadilha de leitura esperando para confundir uma
  sessão futura.
- **`Battle of Sekigahara, 1600` (lote 157) ficou em `Xogunato do Japão >
  Período Edo`, mas também caberia em `Sengoku Jidai`** — é literalmente a
  última grande batalha do período Sengoku e a que inaugura o xogunato
  Tokugawa ao mesmo tempo. Escolhi pelo lado que o título do próprio vídeo
  enfatiza ("Tokugawa Shogunate is Born"), não resolvido de forma geral.
- **`TbVfFq16gK8` (lote 152, já travada) classificada como Batalha de
  Kleidion (1014) por inferência, possivelmente errada.** O lote 153
  (canal HistoryMarche) trouxe `6QSf2sZgPuM`, confirmando que Kleidion é a
  **Parte 5** da série "Basil II, the Bulgar Slayer" do canal — mas
  `TbVfFq16gK8` se chama "Final battle of Basil II (**Part 7**)". Como a
  linha já está travada, a correção precisa de autorização explícita do
  humano antes de reabrir (ver protocolo.md, "Corrigir uma linha travada
  com aprovação humana explícita").
- **Compilação "Hannibal PARTS 18-20" (lote 151, já travada, faixa
  `216 a.C. - 212 a.C.`) pode ter o início errado.** O lote 154 trouxe
  `BHZ9xen25cY` ("Battle of Cumae, 215 BC ⚔️ Hannibal (Part 18)"),
  mostrando que a Parte 18 é 215 a.C., não 216 a.C. como eu tinha estimado
  para a compilação. Faixa correta provável: `215 a.C. - 212 a.C.`. Mesma
  ressalva: linha travada, precisa de autorização explícita antes de
  corrigir.
- **Subtema `Cercos de Viena` (Império Otomano) reaproveitado para Párkány,
  1683 (lote 149, canal HistoryMarche)**, uma batalha adjacente ao cerco em
  si, não o cerco. Se o canal trouxer mais episódios da mesma Grande Guerra
  Turca (1683-1699) — já há "related videos" para Buda 1686, Mohács 1687,
  Zenta 1697 nas descrições —, pode valer abrir um subtema-guarda-chuva mais
  largo (`Grande Guerra Turca`) e mover Párkány para ele. Não resolvido.
- **Região `Turquia` para os subtemas `Basílio II` e `Dinastia Comnena`
  (Império Bizantino) aplicada também a campanhas nos Bálcãs, não só a
  biografia de corte.** Achado no canal HistoryMarche (lotes 150 e 152):
  `Sirmium 1167` (Manuel I Komnenos marchando contra a Hungria) e `Setina
  1017`/`Final battle of Basil II` (campanhas de Basílio II contra a
  Bulgária) foram classificados como `Turquia` só por seguir a convenção já
  100% estabelecida nesses dois subtemas (corte em Constantinopla), mesmo as
  batalhas em si tendo sido travadas nos Bálcãs. A convenção foi pensada
  para biografia de corte, não para campanha militar — vale reconsiderar se
  os dois casos deveriam ter regras diferentes numa parada futura.
- **Granularidade de região inconsistente entre `Guerra Franco-Flamenga`
  (`Países Baixos`) e temas vizinhos da mesma geografia/época** (`Guerra de
  Sucessão Espanhola`, `Guerra dos Nove Anos`, ambos `Europa Ocidental`).
  Achado no canal HistoryMarche (lote 151). Não é erro — `Países Baixos` é
  um termo válido da Lista B —, mas o resto do "cluster" de guerras do
  noroeste europeu nos séculos XVII-XVIII usa o nível acima. Vale nivelar
  numa parada futura.
- **`Pano de Fundo Medieval da Reforma` (lote 146) e `Indulgências` (lote 142)
  têm faixa idêntica (1300-1517), ambos sob `Reforma Protestante`** (canal
  Ryan M Reeves). Distinção pretendida na nota da linha (Indulgências é mais
  estreito, só a prática; o outro é a vida católica tardo-medieval inteira),
  mas os dois cobrindo exatamente os mesmos 217 anos é sinal de possível
  redundância — não resolvido, aguardando decisão do humano.
- **`John Wycliffe` (novo, lote 148) e `Jan Hus e a Profecia da Reforma`
  (existente, lote 142) são dois precursores da Reforma tratados como
  subtemas separados sob `Reforma Protestante`**, apesar de o próprio vídeo
  de Hus (canal Ryan M Reeves) dizer que ele foi influenciado pelas ideias de
  Wycliffe. Não é erro de classificação, mas os dois poderiam virar um
  subtema-guarda-chuva "Precursores da Reforma" numa parada futura.
- **`Sociedade Medieval` (Escolástica Medieval) acumulou 5 vídeos com a faixa
  idêntica (Panorama 500-1500) em 3 lotes diferentes do canal Ryan M
  Reeves** (145-148) — o canal produz muitas aulas-panorama genéricas de
  "Idade Média" que colapsam todas na mesma linha. Não é erro, mas vale
  reconsiderar se esses vídeos deveriam se diferenciar por sub-período
  (alto/baixo medieval) numa parada futura.
- **`Puritanismo` está espalhado em três temas-raiz diferentes** (canal Ryan M
  Reeves, lotes 141-144): `Reforma Protestante > Puritanismo Inglês e
  Colonial` (3 vídeos — Shakespeare vs. Puritans, primeiro sermão na
  América, John Bunyan), `Guerra Civil Inglesa > Puritanismo` (1 vídeo — The
  English Civil War and Puritanism) e `História do Cristianismo Moderno >
  Puritanismo (panorama)` (1 vídeo — Puritanism, an overview). Nenhuma
  classificação individual parece errada (contextos diferentes: colonial,
  guerra civil, panorama do movimento inteiro), mas os três nomes de
  subtema quase idênticos convidam confusão numa sessão futura. Não
  consolidado — decisão do humano na parada dos lotes 141-144.
- **`Reforma Católica (Contrarreforma)` está aninhado dentro de `Reforma
  Protestante`** (canal Ryan M Reeves, lote 144, vídeo sobre Ignatius
  Loyola e os Jesuítas) — o nome do tema-pai não bate com o conteúdo (a
  Contrarreforma é a reação católica à Reforma protestante, não uma parte
  dela). `Concílio Vaticano I` (mesmo canal, lote 143), tratando de história
  católica institucional, foi para `Papado` em vez disso — os dois vídeos
  católicos ficaram em temas-raiz diferentes sem critério explícito. Não
  resolvido — considerar tema próprio para história católica pós-Reforma ou
  mover ambos para `Papado`.
- **`QjagO4aobpU` (All Souls' Day/Hallowtide) e `M9zWAAFiwV4` (History of
  Halloween) dividem o subtema `Halloween`** dentro de `História dos
  Feriados` (canal Ryan M Reeves, lote 141, classificado antes desta
  sessão), mesmo sendo vídeos de assunto nominalmente diferente (Dia de
  Finados vs. Halloween em si). Provavelmente intencional (as duas datas
  formam a mesma "temporada" de Hallowtide no calendário litúrgico), mas não
  confirmado com o humano.
- **`Interbellum - The Inevitable March Towards the Second Punic War #21`
  (canal Magistra Vitae, lote 139) ficou sem subtema, dentro de `República
  Romana > Segunda Guerra Púnica`, mesmo sendo sobre o período ENTRE a
  Primeira e a Segunda Guerra Púnica (241-219 a.C.).** Não criei um subtema
  "Prelúdio" para não multiplicar subtemas de baixíssimo uso (só essa linha)
  — mas o rótulo `Segunda Guerra Púnica` para um vídeo que é literalmente
  sobre o intervalo antes dela é uma aproximação, registrada aqui para não
  ser esquecida se mais vídeos do gênero aparecerem.
- **Cadeia de quatro temas-raiz cobrindo um único arco histórico contínuo
  (1905-1932), aprovada na parada dos lotes 136-138:** `Revolução Russa de
  1905` → `Revolução Russa de 1917` → `Guerra Civil Russa` → `União
  Soviética`. Estende o mesmo padrão já decidido para o par 1905/1917 ("dois
  eventos distintos, nomes próprios na historiografia, mantidos separados
  por desenho, não por dúvida de fusão") para mais dois elos. A fronteira
  entre `Guerra Civil Russa` e `União Soviética` (usei o fim da guerra
  propriamente dita, ~1921-1922, como corte) é decisão de quem classificou,
  não uma fronteira historiográfica de consenso único — vale revisitar se um
  lote futuro tornar a costura visivelmente errada.
- **`Frente Oriental` existe como subtema em dois temas-raiz diferentes**
  (`Segunda Guerra Mundial > Frente Oriental`, já existente, e `Primeira
  Guerra Mundial > Frente Oriental`, novo na parada dos lotes 136-138) — cada
  um correto para a guerra que descreve, mas o nome idêntico em dois temas
  pode confundir quem busca só pelo subtema, sem checar o tema-pai.
- **`Guerra Polaco-Soviética` (novo subtema de `Guerra Civil Russa`, parada
  136-138, 2 linhas) pode merecer tema-raiz próprio.** Historiograficamente é
  mais tratada como guerra interestatal (a Polônia já era Estado soberano
  reconhecido, não facção da guerra civil) do que como capítulo da guerra
  civil russa — mantida como subtema por ora porque as duas linhas do
  catálogo vieram do mesmo canal/série que também cobre a guerra civil
  propriamente dita.
- **Região `Leste Europeu` usada por aproximação para a Guerra
  Polaco-Soviética** (parada 136-138) — a Lista B não tem `Polônia` como
  região própria; primeira vez que o catálogo cobre território polonês como
  ator central, não só de passagem. Se mais canais tratarem de história
  polonesa, vale considerar adicionar `Polônia` à Lista B.
- **`rGxVvpsIRUk` ("Supplemental: The Streets of Paris", lote 136, canal
  Revolutions/Mike Duncan) é a linha de menor base do lote inteiro.** Sem
  numeração de episódio, descrição de uma linha só ("Au revoir Paris..."),
  nenhuma data ou capítulo. Classificada em `Comuna de Paris`, `1871 - 1880`,
  por palpite (provável epílogo sobre os comunardos exilados / anistia de
  1880) — aprovada pelo humano na parada mesmo assim, mas sinalizada aqui
  porque pode não pertencer nem à faixa nem ao tema se surgir evidência
  melhor no futuro.
- **`6pemEIq1KOo` ("100K Q&A: Better Late Than Never", lote 77, canal Ancient
  Americas, encerrado) tem `Século/Período = Extra` mas deveria ser
  `Aleatório`.** Mesmo bug encontrado e corrigido nesta parada (lotes
  125-128) em duas linhas próprias (`laM6N_ZnYxs`, `M6yv1ftGTj8`) — um vídeo
  de aviso de canal (`Tema = Avisos do canal`) não é história, então o rótulo
  certo é `Aleatório`, não `Extra`. Esta linha já está travada de um ciclo
  anterior (aprovação do lote 77-78); não corrigida agora por estar fora do
  escopo desta parada e exigir aprovação humana explícita célula a célula
  antes de tocar uma linha travada de outro ciclo. Ver `protocolo.md`,
  "Armadilhas conhecidas", para o bug em si.
- **`China antiga` (existente, 4 vídeos, outros canais) vs. `Dinastia Zhou` (novo,
  lotes 123-124, canal GatesOfKilikien).** Não comparei o conteúdo dos 4 vídeos
  já catalogados com os do canal novo — os dois podem cobrir o mesmo recorte
  cronológico (China pré-imperial) sob nomes diferentes. Registrado para
  checar antes do próximo canal de história chinesa; não resolvido.
- **`Dinastia Han` ganhou os subtemas `Han Ocidental`/`Han Oriental` nos lotes
  123-124, mas os 2 vídeos antigos do tema (de outro canal, sem subtema)
  continuam como estavam, travados.** Não retroagi sem aprovação explícita
  célula a célula — pendente se você quiser encaixá-los num dos dois.
- **`Geografia Estratégica` (novo, lotes 123-124) é o primeiro tema-raiz
  explicitamente cross-região do catálogo por desenho, não por aproximação.**
  Reúne o formato recorrente de ensaio "este lugar através da história" do
  canal GatesOfKilikien, aplicado tanto à China (Bósforo, Xiangyang, Xuzhou,
  geografia chinesa em geral, Grande Muralha, divisor Norte-Sul) quanto à
  Grécia (Peloponeso). Diferente de `Marinha`/`Fortalezas`/`Mercenários`
  (temas institucionais que também cruzam região), aqui o critério de
  agrupamento é o **formato** do vídeo (ensaio atemporal de lugar/estrutura),
  não o assunto ou a região. Registrado para acompanhar se isso confunde à
  medida que mais canais contribuírem.
- **`Vândalos` (novo, lote 122) vs. `Reino Vândalo` (já existente, 3 vídeos).**
  O canal The Histories trouxe uma etnografia completa do povo vândalo
  ("Who were the Vandals?"): origens na Polônia, migração pela Gália e
  Espanha, saque de Roma em 455, e só depois a fundação do reino no Norte da
  África — escopo mais amplo que `Reino Vândalo`, que cobre só o reino
  africano em si. Mesmo padrão do caso já registrado de `Reino Normando da
  Sicília` (tema que nasceu para um recorte e foi encolhendo por vídeos que
  cobrem o "antes"). Mantidos separados por ora; considerar fusão numa parada
  futura se o canal continuar produzindo sobre o mesmo povo.
- **`Cátaros` (novo, lote 122) vs. `Cruzadas > Cruzada Albigense` (já
  existente, 2 vídeos).** O mesmo canal trouxe uma etnografia do movimento
  cátaro em si (crença, organização, vida social, perseguição) que culmina na
  Cruzada Albigense mas não se resume a ela — o subtema existente é sobre a
  campanha militar. Mantidos separados; mesma lógica do par acima.
- **Classe "tema por era do mesmo conflito/país" — nova instância registrada na
  parada dos lotes 52-55.** `Guerra do Afeganistão` (novo, para a queda de Cabul
  de 2021) coexiste com `Guerra Soviético-Afegã` (1979-1989, já existente) do
  mesmo jeito que `Guerras Árabe-Israelenses`/`Guerra Israel-Hamas`/`Conflito
  Israel-Hezbollah` coexistem, e do jeito que `Guerras da Chechênia`/`Segunda
  Guerra da Chechênia` coexistem (ver entradas abaixo). São pelo menos três
  pares/trios do mesmo padrão — um tema-raiz por era do mesmo país/conflito, sem
  hierarquia comum. Decisão do humano: não fundir agora nenhum deles
  individualmente; reservar uma parada dedicada só a essa classe (Chechênia,
  Israel-Hamas/Hezbollah, Afeganistão) para decidir de uma vez se cada trio vira
  tema-pai com subtemas por era ou se a separação por era fica como está.
- **`Revolução Russa de 1905` e `Revolução Russa de 1917` (parada dos lotes
  133-135, playlist Revolutions/Mike Duncan) NÃO são a mesma classe "tema por
  era" do bullet acima.** Lá, cada par/trio cobre o MESMO conflito revisitado
  em datas diferentes — a dúvida pendente é só de hierarquia (fundir com
  subtema por era, ou manter separado). Aqui são **dois eventos históricos
  distintos**, com nomes próprios na historiografia e sem ambiguidade de
  fronteira: 1905 é a insurreição fracassada que arranca a Duma do czar sem
  derrubá-lo (Bloody Sunday, Manifesto de Outubro, reformas de Stolypin); 1917
  é o colapso do czarismo e a ascensão bolchevique — o evento que se chama "a
  Revolução Russa" sem qualificador quando alguém fala em geral. Decisão
  humana: manter os dois nomes como temas-raiz separados **por desenho**, não
  por dúvida de fusão pendente. `Revolução Russa de 1905` (46 linhas) fundiu
  nesta parada o tema que tinha sido criado sem essa distinção no lote 134
  (`Revolução Russa`, 21 linhas, episódios 10.1-10.21 — pano de fundo teórico e
  histórico anterior a 1905: Marx, Engels, Bakunin, doutrina da Terceira Roma,
  Decembristas de 1825, reformas de Alexandre II) com o tema já criado no lote
  135 (`Revolução Russa de 1905`, 25 linhas, episódios 10.22-10.46 — a
  revolução de 1905 em si e o pós-1905 até 1907-1911). `Revolução Russa de
  1917` fica **reservado, ainda sem nenhuma linha**: a playlist Revolutions só
  chegou até 1905-1911 no lote 135; quando os episódios sobre 1917 forem
  coletados, entram direto nesse tema, sem precisar de nova decisão de
  fronteira.
- **`Reino de Roma` (novo, parada dos lotes 52-55)** — criado para separar
  `Early Rome, Part IV: Plutarch's Life of Numa Pompilius` (que narra o reinado
  lendário de Numa Pompílio, 715-673 a.C., não só o método historiográfico de
  Plutarco) do resto da série `Early Rome` (que ficou em Historiografia, por
  método). Só 1 vídeo até agora; ainda não tem subtema. Pendente: se aparecerem
  mais vídeos sobre o período regal romano (Rômulo, os outros reis), decidir se
  ficam todos sob este tema-raiz.
- **Fragmentação do conteúdo sobre Atenas** entre três lugares: `Democracia
  Ateniense` (tema próprio, sobre a instituição), `Grécia antiga` (para "Late
  Classical Greece", lote 52) e agora `Vida urbana > Atenas` (lote 53, "Houses
  and Herms: Private Life in Classical Athens"). Mesmo padrão do "trio inglês
  fragmentado" já registrado — funciona por ora, mas vale considerar
  consolidação se o canal continuar produzindo sobre Atenas.
- **Historiografia ganhou 3 subtemas novos de "leitura comentada" na mesma
  janela (lotes 52-55): `Early Rome`, `H.G. Wells`, e antes deles já existiam
  `Edward Gibbon`/`Historiadores latinos`/`G.P. Baker`/`Taking Out the Trash`.**
  Nenhuma sobreposição de conteúdo entre elas (cada uma é um autor/formato
  diferente), só um alerta de que a lista de séries de leitura sob Historiografia
  está crescendo rápido e pode merecer uma seção própria na Lista C se continuar.
- **`Guerras Árabe-Israelenses` (novo, lote 39) vs. `Guerra Israel-Hamas` (6) e
  `Conflito Israel-Hezbollah` (4)**: três temas para o mesmo conflito
  árabe-israelense em eras diferentes — a Crise de Suez (1956) e a Guerra do
  Yom Kippur (1973) foram para o tema novo, cobrindo a série clássica de
  guerras 1948-1973; os outros dois cobrem os conflitos mais recentes.
  Pendente: unificar sob um tema-pai com subtemas por guerra, ou manter a
  separação por era (como já está).
- **`Exército Romano` (novo, lote 38) vs. `Império Romano`**: critério usado —
  reinado/evento específico (Cômodo, Marco Aurélio, Aureliano, Abritus) vai em
  `Império Romano`; tema institucional que atravessa vários reinados (evolução
  do centurião, reformas de Diocleciano, castra, cavalaria imperial) vai em
  `Exército Romano`, no mesmo padrão de `Religião Romana` (tema cross-era já
  existente). Critério criado na hora, não confirmado por revisão humana ainda.
- **`Reino Normando da Sicília` cobre cada vez mais o período pré-Reino.** O
  tema nasceu no lote 35 para o vídeo sobre o Reino multicultural de Rogério
  II (1130-1154), mas já acumulou 6 vídeos que remontam à conquista normanda
  do sul da Itália (Civitate 1053, Cerami 1063, Dirráquio 1081, saque de Roma
  1084) — quase 80 anos antes da fundação formal do Reino. O nome do tema
  descreve cada vez menos o conteúdo real; pode valer a pena renomear para
  algo como `Normandos no Mediterrâneo` ou dividir em conquista/reino.
- **`Império Timúrida` (novo, lote 37) vs. `Império Otomano`** — o saque de Delhi
  por Timur em 1398 (`issEot6c0d0`) recebeu tema-raiz novo, mas as duas linhas já
  existentes sobre a Batalha de Ancara de 1402 (Timur vs. Bayezid I —
  `sHH3lQ_O-xA`, lote 15, e `hIEIpQAz4PE`, lote 36) foram classificadas em
  `Império Otomano`, pelo ângulo otomano do mesmo conflito. É o mesmo
  personagem histórico (Timur) tratado em temas diferentes conforme o vídeo
  narra do lado timúrida ou do lado otomano. Não mexido retroativamente — linhas
  antigas travadas. Pendente: decidir se unifica tudo em `Império Timúrida` (com
  subtema para o confronto com os otomanos) ou mantém a divisão por ângulo.
- **Aproximações de região que já passaram da segunda ocorrência**: `Bálcãs`
  para Dirráquio/Albânia acumulou 3 usos nos lotes 35 e 37 (`9pDIeB3bVyU` 48
  a.C., `FFya9iLzvsM` e implicitamente `Q-2-JKF52cY` 1081-1084); `Oriente
  Médio` para Ctesifonte/Iraque (`o9jNvJFawlo`, lote 36) é a 2ª ocorrência
  depois de Califado Abássida/Rebelião Zanje. Pela regra já usada para Iêmen e
  Norte da África, ambas justificariam região própria (`Albânia`, `Iraque`) —
  registrado para decisão humana, não criado por conta própria.
- `Marinha` e `Marinha Britânica` — uma linha cada, intocadas desde o lote 0.
- `Período homérico` e `Ártico` aparecem como tema **e** como período/região em
  3 linhas: `lcfveYFnN7M` (Odysseus, lote 8), `C5rIbTq9txY` (Dark Ages, lote 0)
  e `XG0rqUOGrwc` (Arctic Matters, lote 0). O quarto caso (`k36ejxp4jNk`,
  Esparta) foi corrigido na parada dos lotes 10-13 — ver abaixo.
- `Xogunato do Japão` cobre dois assuntos distintos: governança/sucessão do
  xogunato (lote 12) e contato diplomático com o Ocidente (lote 13). Funciona
  como raiz guarda-chuva por ora; pode merecer subtema se o canal continuar
  produzindo sobre relações exteriores do Japão.
- **`Guerras da Chechênia` ficou parcialmente resolvido na parada dos lotes
  14-17.** O vídeo sobre a Primeira Guerra da Chechênia chegou no lote 14 e
  entrou como `Guerras da Chechênia > Primeira Guerra da Chechênia` (padrão
  `Cruzadas > Segunda Cruzada`, linha travada). Mas a linha da Segunda Guerra
  da Chechênia (`o7sHFtnR7qs`, lote 13) continua com `Tema =
  'Segunda Guerra da Chechênia'` solto, sem o pai nem subtema — é uma linha
  travada e não pode ser corrigida sem aprovação explícita célula a célula.
  Pendente: humano aprovar a correção dessa linha para
  `Guerras da Chechênia > Segunda Guerra da Chechênia`.
- **`Colapso da Idade do Bronze` vs `Egito antigo`** (novo, lote 16): "How did
  Ancient Egypt Survive the Bronze Age Collapse?" foi para o tema novo, não
  para `Egito antigo`, por ser sobre o colapso regional — mas o vídeo é 90%
  sobre o Egito. Pode fazer mais sentido como subtema `Colapso da Idade do
  Bronze` dentro de `Egito antigo`, em vez de tema-raiz próprio.
- **`Grupo Wagner` vs `Guerra Russo-Ucraniana`** (novo, lote 17): a história do
  grupo mercenário antes de 2022 (Síria, África) ficou em `Grupo Wagner`, mas
  o vídeo sobre o motim de Prigozhin (jun/2023) ficou em
  `Guerra Russo-Ucraniana`, não em `Grupo Wagner`. Divide o conteúdo sobre
  Wagner em dois temas dependendo da época — pode ser a linha certa (o motim
  está entrelaçado com a guerra) ou pode precisar virar um único tema com
  subtemas.
- **Trio inglês fragmentado**: `Bretanha Antiga` (novo, lote 17, pré-410),
  `Inglaterra anglo-saxã` (410-1066) e `Conquista normanda da Inglaterra`
  (1066+) são três temas-raiz separados cobrindo períodos consecutivos da
  história da Inglaterra. Funciona por ora; considerar tema-pai com subtemas
  se o canal continuar produzindo sobre isso.
- **Cluster judaico**: `Judaísmo` (novo, lote 14), `Cisma entre Judaísmo e
  Cristianismo` e `Povo hebreu` (ambos já existentes) são três temas
  adjacentes sem sobreposição direta de conteúdo até agora, mas com
  potencial de sobreposição futura.
- **Ensaios de opinião da série "Modern Affairs"** (`Is Russia Fascist?`,
  `Who is Going to Rule Russia After Putin?`, `Can the EU be a Superpower?`,
  `How do the Russian/Ukrainian Economies Cope?`, e mais `How Would Ukraine
  Liberate Crimea?`, `What is Prigozhin's Game?`, `Russia, China and Iran - a
  New Axis?`, `What is in the Pentagon Leaks?` dos lotes 18-19 — 10 linhas ao
  todo): continuam classificados como `Guerra Russo-Ucraniana`/`chute` (ou
  `média`, quando o título nomeia um evento inconfundível) por analogia às
  atualizações de campo de batalha, mas não narram um período — são ensaios
  analíticos atemporais, mais parecidos com o padrão `Extra` (historiografia,
  como `Napoleão Bonaparte`). Não foram reclassificados porque isso tocaria
  linhas já travadas — o cluster só cresceu nos lotes 18-21, ainda sem decisão.
- **`Guerra Imjin` (novo, lote 21) sobrepõe `Sengoku Jidai`** — mesmo padrão do
  antigo caso `Guerras Árabe-Cazares`/`Império Cazar` (resolvido na parada dos
  lotes 10-13, virou subtema). A invasão japonesa da Coreia (1592-1598) foi
  liderada por Toyotomi Hideyoshi durante o mesmo período que o canal cobre em
  `Sengoku Jidai` (10 linhas), mas envolve Coreia e China, não é conflito
  interno japonês — por isso ganhou tema-raiz próprio em vez de virar subtema
  de `Sengoku Jidai`. Registrado para decisão na próxima parada: manter
  separado ou virar `Sengoku Jidai` > `Guerra Imjin`.
- **`Lenda Arturiana` (novo, lote 19) usa `Região = Leste Europeu` por
  aproximação.** O vídeo (`Was an Arthurian Knight Inspired by a Hungarian
  King?`) é sobre o rei húngaro László I (r. 1077-1095), mas a Lista B não tem
  termo próprio para Hungria — `Leste Europeu` foi o mais próximo disponível.
  Registrado para a próxima parada avaliar se vale criar `Hungria` na Lista B
  (mesma regra de "segunda ocorrência" usada para Iraque/Jordânia).
- **Cluster japonês fragmentado (novo, lotes 24-25)**: `Wakō` (piratas,
  1200-1600), `Rebelião de Shimabara` (1637-38) e `Sakoku` (isolamento,
  1639-1854) são três temas-raiz separados cobrindo períodos consecutivos da
  história do Japão Edo/tardo-Sengoku — mesmo padrão do "trio inglês
  fragmentado" já registrado. Funciona por ora; considerar tema-pai com
  subtemas se o canal continuar produzindo sobre o período.
- **`Feudalismo` ganhou uma segunda linha (lote 25, `How European Kings
  Defeated their Nobles`)** que pode repetir o argumento da linha já
  catalogada (`What Everyone Gets Wrong About Feudalism`) — não confirmado,
  registrado para conferência futura.
- **Cluster de temas-raiz biográficos abaixo do piso de 3 vídeos** (novo, lotes
  26-29): `Ibn Fadlan`, `Mansa Musa` e `Johannes Schiltberger` (1 vídeo cada) e
  `Napoleão Bonaparte` (2 vídeos) violam a regra fechada nesta mesma parada
  ("pessoa só vira tema-raiz com 3+ vídeos"), mas não foram reclassificados
  retroativamente — ver "Decisões fechadas". Se o canal não produzir mais
  vídeos sobre essas pessoas, ficam como estão; se produzir, a próxima parada
  decide o tema-pai/subtema de cada um (provavelmente pelo contexto: Ibn Fadlan
  sob algo como `Expansão islâmica`/`Califado Abássida`, Mansa Musa sob um
  futuro tema de África Ocidental, etc.).
- **`Rise of the Cossacks` (lote 24, tema `História da Ucrânia`) tem faixa de
  quase 300 anos (1362-1657)**, cobrindo três processos distintos (fim do jugo
  mongol, tomada de poder pela Comunidade Polaco-Lituana, rebelião de
  Khmelnytsky) por não haver nenhuma data própria na evidência. Candidata a
  subdivisão ou a um marco mais preciso numa correção futura.
- **`Sula` sobrevive em 3 linhas travadas (`VbKMf3I0Vec` lote 8, `gQKMW_XLJgM`
  lote 4, `q5kleX6F-cM` lote 39), ao lado do subtema renomeado `Crise da
  República tardia (91-78 a.C.)` nas outras 15.** Na aprovação dos lotes
  40-43, o subtema `Sula` foi renomeado para descrever melhor o cluster de
  magistrados tardo-republicanos que cresceu nele — mas as 3 linhas acima já
  estavam travadas antes desta rodada, e renomear célula de linha travada sem
  passar pelo fluxo normal de correção dispara a checagem de "linha travada
  alterada" do `verificar.py`. Ficaram de fora de propósito. Pendente: humano
  aprovar a renomeação dessas 3 células especificamente (mesmo padrão do caso
  `Guerras da Chechênia` acima).
- **`Ano dos Quatro Imperadores` usado de forma elástica**: inclui bios cuja
  carreira vai bem além da crise de 68-69 (`Lucceius Albinus` 62-69,
  `Lucius Verginius Rufus` 63-97, lotes 41-42) — usado pela conexão do
  personagem com a crise, não pela contenção estrita da faixa de anos. Segue
  o mesmo raciocínio de "episódio de origem fica com o tema que origina" (ver
  "Decisões fechadas"), mas nunca foi confirmado explicitamente para este
  subtema. Registrado para decisão futura, não corrigido.
- **`Historiografia > Ancient Apocalypse (Graham Hancock)` (removido nesta
  parada, ver "Decisões fechadas") vs. `Historiografia > Datação da Esfinge`**
  (lote 43, reaproveitado no lote 48): mesmo cluster de catastrofismo do
  Dríade Recente/civilização perdida pré-histórica, mesmo entrevistado de
  referência (Robert Schneiker é citado dentro da própria resenha do vídeo do
  Hancock). Hoje as duas linhas do cluster de Schneiker estão sob `Datação da
  Esfinge` (2) e a resenha do Hancock ficou sem subtema (abaixo do piso de 3).
  Se aparecer uma terceira linha do mesmo assunto, decidir se unifica tudo
  num subtema-guarda-chuva (`Catastrofismo do Dríade Recente`, por exemplo)
  ou mantém `Datação da Esfinge` restrito ao método específico da Esfinge.

- **`Vida urbana` já soma 7 subtemas de 1 vídeo cada** (achado na parada dos
  lotes 56-59): Hattusa, Atenas, Quioto (anteriores) e Antioquia, Alexandria,
  Constantinopla, Roma (lotes 58-59). Nenhuma sobreposição de conteúdo — são
  cidades diferentes — só um alerta de que o padrão "uma cidade, um vídeo, um
  subtema" está crescendo rápido, no mesmo ritmo já registrado para os
  subtemas de leitura comentada em `Historiografia`.
- **Cluster de temas-raiz de uma única pólis/região grega** (achado na parada
  dos lotes 56-59): `Macedônia Antiga`, `Épiro antigo`, `Tessália antiga`,
  `Beócia antiga`, `Argos antiga` — todos com 1 vídeo, criados nos lotes
  58-59 — ao lado de `Esparta` (3, já existente, que abriu o precedente de
  "uma pólis, um tema-raiz"). Funciona por ora, mas a proliferação recente (5
  temas novos em 2 lotes) vale reconsiderar numa parada futura: talvez um
  tema-pai `Pólis e reinos gregos antigos` com subtema por região, se o canal
  continuar produzindo nesse formato.
- **`Guerras Napoleônicas` (7, rosters de comandantes) vs. `Napoleão
  Bonaparte` (8, incluindo a biografia em 5 partes do lote 59)** — temas
  adjacentes sobre o mesmo assunto geral (as Guerras Napoleônicas), um
  focado em listas/rankings de oficiais, o outro na vida do próprio Napoleão.
  Registrado na parada dos lotes 56-59, não fundido.
- **`Épiro antigo` usa `Região = Grécia` por aproximação** (lote 58): a
  Lista B não tem `Albânia`, e o Épiro histórico é dividido entre os dois
  países hoje. Mesma regra de "segunda ocorrência" já usada para Iêmen e
  Norte da África se aplicaria caso apareça um segundo vídeo sobre a região.
- **`Early Rome: Monarchy and Early Republic` (`6NxqOlQm7Mw`, lote 59)
  classificado em Historiografia > Early Rome por analogia de tom com o
  resto da subsérie, mas com ressalva registrada na parada dos lotes 56-59**:
  as tags citam eventos concretos (expulsão de Tarquínio, saque gaulês,
  Forcas Caudinas) que poderiam justificar tratá-lo como conteúdo de linha do
  tempo, no mesmo padrão que gerou `Reino de Roma` para a Parte IV (Numa
  Pompílio) na parada 52-55. Não reclassificado; pendente de revisão.
- **`Turquia` ganhou uma terceira aproximação distinta, achada na parada dos
  lotes 60-63.** Já cobria (a) litoral da Anatólia em batalhas navais
  greco-selêucidas e (b) corte de Constantinopla em bios bizantinas (ver acima,
  achado dos lotes 48-51). Agora cobre também `Halicarnasso` (lote 60, tema
  novo de pólis grega) — geograficamente Anatólia, mas nem batalha naval
  selêucida nem bio de corte bizantina. Três motivos de aproximação sem
  nenhuma relação entre si sob o mesmo rótulo — registrado, não resolvido.
- **`Marcha para o Mar` (novo, lote 60) e `Campanha de Atlanta` (já existente)
  cobrem trechos consecutivos da mesma campanha de Sherman** (Atlanta →
  Savannah → Carolinas), mesmo padrão do "trio inglês fragmentado" e do
  cluster japonês — funciona por ora como par relacionado, não fundido.
- **`Candidatos Derrotados` cresceu de poucos vídeos para 20 na parada dos
  lotes 60-63**, de uma vez só (perfis de Castro, Inslee, Williamson,
  Buttigieg, Bloomberg, Patrick, Bullock, Messam, Sestak, Delaney, Bennet,
  Swalwell, O'Rourke e o vídeo-resumo "Recent Democratic Dropouts"). Mesmo
  alerta de crescimento rápido já registrado para `Vida urbana` e o cluster de
  pólis gregas de 1 vídeo — funciona, mas é o maior salto de um subtema só até
  agora.
- **`A Charge to Keep` (Historiografia, 12 vídeos até o lote 63) mantido
  inteiramente como leitura comentada/Extra, sem separar capítulos que narram
  política real e datável do governo Bush no Texas** (ex.: Capítulo 13, debate
  de saúde de fins dos anos 1990; Capítulo 15, histórico de governo em
  educação). Achado e decidido na parada dos lotes 60-63: ao contrário de
  `Early Rome` Parte IV (que foi separada de Historiografia por narrar o
  reinado de Numa Pompílio sem comentário metalinguístico), os capítulos de
  "A Charge to Keep" não seguem a ordem cronológica da vida de Bush (é um
  livro de campanha organizado por tema, não por data) e o formato do canal é
  consistentemente crítico/interpretativo ("critique de como Bush se
  apresenta"), não narração neutra de um período. Mantido Extra em bloco —
  decisão registrada, não pendente.
- **`Guerras dos Diádocos` cresceu de 11 para 51 vídeos em quatro lotes (64-67)
  — o maior salto de um tema único já registrado no catálogo.** É uma
  "temporada" inteira de prosopografia dos Sucessores de Alexandre, mesmo
  formato de "Romans of Renown" e das bios bizantinas. Só 10 dos 51 têm
  subtema (`Primeira Guerra dos Sucessores` 3, `Segunda Guerra dos
  Sucessores` 7) — funciona, mas é um balde grande sem estrutura interna.
  Registrado, não resolvido.
- **`Bush 43 Still Sucks` (5, História dos Estados Unidos, entra na linha do
  tempo) vs. `A Charge to Keep` (12, Historiografia, Extra) — duas séries
  sobre o mesmo George W. Bush, tratamento oposto, achado na parada dos
  lotes 64-67.** Critério aplicado: `A Charge to Keep` é leitura comentada do
  livro-manifesto de campanha (o assunto é o texto e a retórica de Bush);
  `Bush 43 Still Sucks` é uma série crítica sobre o registro histórico real
  do governo dele (o assunto são os fatos, ainda que narrados com tom
  hostil). Inclui uma linha de fronteira (`7SuU8wtGW-w`, "Refutation of Bush
  Propaganda", lote 67) que é formalmente uma resposta a vídeo de terceiro
  (Simon Whistler/TopTenzNet) — mesmo formato de "Re: 10 Things About
  Hoplites" (lote 66, que foi para Extra) — mas ficou na linha do tempo
  porque o conteúdo real é sobre o mandato de Bush, não sobre método de
  vídeo. Registrado como decisão consciente, não pendente.
- **`Jogos retrô` (16, Aleatório) vs. `História dos videogames` (1, entra na
  linha do tempo) — nomes parecidos, tratamento oposto, achado na parada dos
  lotes 68-71.** Distinção: `Jogos retrô` é gameplay/let's-play (o assunto é
  jogar o jogo, entretenimento puro); `História dos videogames` é
  retrospectiva histórica real do console/era (o assunto é a história do
  hardware, mesmo critério já usado para tier-ranking de console real,
  parada 52-55). Risco registrado: escolher nome de tema novo parecido
  demais com um existente de tratamento oposto convida confusão futura —
  vale checar o vocabulário antes de nomear tema novo, não só o conteúdo
  dele.
- **`Formação das Monarquias Nacionais` (novo, 1066-1453) se sobrepõe
  cronologicamente com `Guerra dos Cem Anos`** (9, existente, 1337-1453) —
  a Guerra dos Cem Anos inteira está contida na faixa do tema novo. São
  níveis de zoom diferentes (panorama institucional vs. o conflito
  específico); registrado, não fundido.
- **`França Medieval` (novo, lote 72, 814-1328) se sobrepõe substancialmente
  com `Formação das Monarquias Nacionais` (lote 71, 1066-1453, França e
  Inglaterra) — achado na parada dos lotes 72-75.** Os dois cobrem
  1066-1328 do mesmo processo de formação do Estado francês, criados em
  janelas de aprovação diferentes sem que a checagem de "o tema já existe?"
  cruzasse as duas. Registrado, não fundido — mas é a mesma classe de
  problema do par "Guerra dos Cem Anos", só que desta vez entre dois temas
  novos, não um novo e um antigo. Lição: a checagem de sobreposição
  precisa olhar o vocabulário inteiro, não só o que a sessão atual já
  criou.
- **Cluster de 5 "reinos bárbaros pós-romanos"**: `Reino Vândalo`
  (existente), `Reino Ostrogodo`, `Reino Visigodo`, `Reino Borgonhão`,
  `Reino Lombardo` (todos novos, lotes 73-74) — mesmo padrão do "trio
  inglês fragmentado" e do "cluster japonês" já registrados. Funciona por
  ora; considerar tema-pai se o canal continuar produzindo sobre o
  assunto.
- **`Chavín de Huántar` quebra o padrão de nome usado no resto do lote 78:
  é nome de sítio, não de cultura, embora a cultura tenha nome próprio
  ("Chavín"), diferente de `Cahokia`/`Teotihuacan`/`Poverty Point`
  (sítios sem nome de povo preservado, onde o nome de sítio é mesmo a
  única opção).** Achado na parada dos lotes 76-78. Cogitar renomear
  para `Chavín`, para bater com `Nazca`/`Moche`/`Império Wari`. Não
  renomeado — decisão do humano, registrada como pendente.
- **Cluster institucional sem subtema sob `República Romana` chegou a 8
  vídeos numa janela só (achado na parada dos lotes 79-82):** Roman
  Elections (lote 80), Consuls, Families & Calendars, Praetors, Aediles,
  Quaestors (lote 81), The Roman Senate during the Republic, The Cursus
  Honorum (lote 82) — todos vídeos "civismo 101" do canal Historia Civilis
  sobre magistraturas/instituições da República, sem evento datável único,
  tratados com a mesma faixa cross-era (509-27 a.C.). Mesmo padrão de
  crescimento rápido já visto em `Vida urbana` e no cluster de pólis
  gregas. Considerar um subtema-guarda-chuva (ex.: `Instituições da
  República`) na próxima parada.
- **`Guerra Civil de César` usado de forma elástica para prelúdio político
  distante, achado na parada dos lotes 79-82.** Além dos eventos da
  própria guerra civil (49-45 a.C.), o subtema passou a incluir toda a
  série biográfica anual "His Year"/"Nobody's Year" do canal Historia
  Civilis — His Year: Julius Caesar (59 a.C.), His Year: Clodius (58
  a.C.), Nobody's Year: CHAOS (57 a.C.), Battle of Carrhae (53 a.C.),
  His Year(s): Pompey (56-52 a.C.) — sob o raciocínio de que cada um
  contribui para o rompimento entre César e Pompeu. Mesmo padrão já
  registrado para `Ano dos Quatro Imperadores` ("usado de forma
  elástica"), mas nunca confirmado por revisão humana. Pendente: manter
  como está ou separar um subtema `Prelúdio` (mesmo padrão já usado em
  Segunda Guerra Mundial/Primeira Guerra Mundial/Guerra Civil Americana).
- **`Reino de Roma` cresceu de 1 para 3 usos na janela 79-82**, incluindo
  um vídeo de escopo bem mais largo que o original: `The Roman Senate
  during the Monarchy` (lote 82, 753-509 a.C., o período regal inteiro)
  ao lado de `The City.` (lote 79, só o reinado de Rômulo, 753-716 a.C.)
  e a linha original de Numa Pompílio (715-673 a.C., parada 52-55). O
  tema estava pendente desde sua criação ("se aparecerem mais vídeos
  sobre o período regal, decidir se ficam sob este tema-raiz") — a
  pendência está ativa agora, não resolvida.
- **`Turquia` ganhou uma quarta aproximação, achada na parada dos lotes
  79-82.** Já cobria (a) litoral anatólio em batalhas navais
  greco-selêucidas, (b) corte de Constantinopla em bios bizantinas e (c)
  Halicarnasso (pólis grega). Agora cobre também Carras/Harran
  (sudeste da Turquia atual), pela Batalha de Carrhae (lote 80) —
  quarto motivo de aproximação sem relação com os outros três.
  Registrado, não resolvido.
- **`Reino de Gwynedd` (novo, sob `História de Gales`, parada dos lotes
  83-84) já nasce com 6 vídeos** — maior estreia de subtema desde a
  adoção do canal Cambrian Chronicles (lote 83). Cobre uma faixa muito
  larga (410-1283 d.C.: fundação pós-romana, Maelgwn Gwynedd, Llywelyn
  Fawr, Owain Gwynedd, até a conquista de Eduardo I), sem divisão
  interna — funciona por ora, mas é candidato a subdivisão por dinastia
  se o canal continuar produzindo sobre o assunto (mesmo alerta já dado
  para `Guerras dos Diádocos` e `Vida urbana`).
- **`Mitos de Wikipédia` (novo, sob `Historiografia`, parada dos lotes
  83-84) nasceu com 3 vídeos no mesmo lote (83)** — formato autoral do
  canal Cambrian Chronicles ("Wikipedia's ___", "The Internet's ___"),
  não uma teoria pseudo-histórica avulsa como os subtemas vizinhos
  (`Hipótese de Tartária`, `Hipótese do Tempo Fantasma`). Ainda não
  confirmado por revisão humana dedicada se a distinção "formato vs.
  teoria avulsa" deveria unificar os cinco num só grupo.
- **Duas decisões "Extra vs. linha do tempo" no limite, canal Cambrian
  Chronicles (parada dos lotes 83-84), registradas sem correção:**
  `The Medieval War Forgotten from History` (`Gc6azLydvlc`) foi para
  Extra/Historiografia porque os únicos números na evidência (`1700s`,
  `1800s`, `1900s`) descrevem a recepção antiquária do relato, não o
  evento original (~500-550 d.C., sem número próprio); `The Most
  Mysterious Name Ever Lost to History` (`Eq7pzp4EmiQ`) foi para a linha
  do tempo (chute, ~450-600 d.C.) apesar de também enfatizar propaganda
  genealógica (capítulo "Cunedda Wledig Propaganda"), por não ter
  nenhuma evidência de recepção equivalente à da linha anterior. As duas
  foram classificadas com o mesmo canal, o mesmo formato de "mistério
  medieval" e critérios ligeiramente diferentes — vale reconferir se o
  canal continuar produzindo esse tipo de vídeo híbrido.
- **`Crise do Século III` (novo, sob `Império Romano`, parada dos lotes
  85-86) nasce com 4 vídeos** e **`Dinastia Constantiniana` (novo, mesmo
  tema, mesma parada) nasce com 3** — os dois na playlist "The History of
  Rome" (Mike Duncan), primeiro canal coletado por playlist explícita em
  vez de canal inteiro (ver `coletar.py --playlist`, seção própria no
  `protocolo.md`). Nenhuma sobreposição achada com vocabulário existente,
  inclusive checado contra Kings and Generals (1042 vídeos, cobriria Roma
  tardia se tivesse esse recorte).
- **Fronteira `Império Romano` → `Queda do Império Romano` decidida sem
  regra fechada prévia (parada dos lotes 85-86).** A partir do episódio
  "Honorius And The Goths" (`iqHZK_Vumjk`, lote 86, 400-420 d.C. —
  primeiro da série com sinal explícito de colapso, tags citando "the
  goths"/"fall of the roman empire"), os episódios seguintes (34-36, até
  476 d.C.) entraram em `Queda do Império Romano` por continuidade
  narrativa, não por sinal individual de colapso em cada um. Os episódios
  30-32 (363-400 d.C., incluindo a derrota de Adrianópolis em 378, por
  conhecimento geral) ficaram em `Império Romano` sem subtema, por não
  terem esse sinal explícito. Linha de corte registrada, não testada por
  segunda opinião.
- **`King Arthur: What Everybody Gets Wrong` (`YUGcuqGczjs`, lote 84,
  canal Cambrian Chronicles) classificado com pouca base, sinalizado na
  amostra da parada e aprovado assim mesmo.** O vídeo rastreia a lenda
  arturiana por ~4 séculos (IX a XII, vários autores); a linha ancorou só
  no ponto de origem citado na descrição ("Wales in the 9th century
  developed... Arthur"), não no arco inteiro — mesmo critério de
  "episódio de origem fica com o tema que origina", mas aplicado a um
  vídeo que é mais sobre a evolução da lenda do que sobre um evento único.
  Se o canal continuar com esse formato de "história de uma lenda através
  dos séculos", vale reconsiderar se esse tipo de vídeo deveria virar
  `Extra` em vez de fixar um século.
- **`Roman History 18 - The Roman World` (`_TmxazjIZRM`, lote 85, chute,
  140 d.C.) não confirmado por busca externa na parada.** Não achei índice
  de episódios do podcast original que descesse a esse nível de detalhe
  para confirmar (nem desmentir) a posição cronológica exata do episódio.
  Chute mantido como estava, sem mudança.
- **`Dinastia Paleóloga` (novo, sob `Império Bizantino`, parada dos lotes
  87-90) nasce com 18 vídeos** — cobre a dinastia inteira (1258-1453), da
  restauração de Michael VIII à queda de Constantinopla, não só a fase
  final que os primeiros vídeos sugeriam.
- **`Império de Niceia` (novo, sob `Império Bizantino`, mesma parada)
  nasce com 6 vídeos** — o estado bizantino em exílio entre o saque de
  1204 e a retomada de Constantinopla em 1261.
- **`Quarta Cruzada` (existente, +8 vídeos na mesma parada) ganhou uma
  fronteira tardia bem mais larga que o evento nomeado.** Passou a cobrir
  não só a cruzada em si (1202-1204) mas também `Baldwin II with John
  Giebfried` (biografia do último Imperador Latino, até 1261) — 63 anos
  num subtema que nasceu para nomear uma campanha de ~6. Aprovado sem
  correção; registrado para reconsiderar se o canal continuar produzindo
  sobre o Império Latino tardio.
- **Estado de Epiro, canal The History of Byzantium Podcast (parada dos
  lotes 87-90): 2 vídeos sobre um terceiro sucessor bizantino rival de
  Niceia** (`Michael Doukas of Epirus`, `The Rise and Fall of Epirus`),
  abaixo do piso de 3 para nomear subtema. Registrado, não resolvido.
- **Região `Itália` escolhida com pouca base para `A Roman Comic Book
  with Marco Cappelli` (`EYlceZvHE3o`, lote 88)** — o cenário do
  quadrinho ficcional discutido é a Itália do século VI, mas o episódio
  em si é uma entrevista sobre a obra/autor, não narração desse período.
  Sinalizado na amostra da parada e aprovado assim mesmo.
- **`Dinastia Comnena` (novo, sob `Império Bizantino`, parada dos lotes
  91-94) nasce com 20 vídeos** — a maior estreia de subtema deste canal,
  cobrindo os três Comnenos (Alexios I, John II, Manuel I, 1081-1180).
  Cresceu em duas direções ao longo da janela: lote 92 cobria só John II
  e Manuel (1118-1180); o lote 93 estendeu para trás até as reformas de
  Alexios (1081-1096); o lote 94 fechou a fronteira exata no episódio de
  origem, o golpe de abril de 1081.
- **`Crise do Século XI` (novo, sob `Império Bizantino`, mesma parada)
  nasce com 12 vídeos** — segunda vez que esse padrão de nome é usado
  (depois de `Crise do Século III`, canal The History of Rome, lotes
  85-86) para o mesmo tipo de cluster: sucessão rápida de governantes
  fracos após o auge de uma dinastia, culminando num desastre militar
  (Manzikert, 1071) e abrindo caminho para uma nova dinastia forte
  (Comnena). Fronteira limpa com `Dinastia Comnena`: 1042-1081 vs.
  1081-1180, exatamente no golpe de Alexios.
- **`Dinastia Angelo` (novo, sob `Império Bizantino`, parada dos lotes
  91-94) nasce com 5 vídeos** — do usurpador Andronikos I Komnenos
  (episódio de origem) à queda de Alexios III Angelos, véspera da Quarta
  Cruzada (1180-1204). Duas linhas já travadas do lote 90
  (`Collapse of the Komnenian System`, `Provincial Separatism`) tratam do
  mesmo assunto/era mas ficaram sem o subtema, por terem sido
  classificadas antes dele existir — não alteradas por já estarem
  travadas. Pendência registrada, não resolvida.
- **`Justiniano e Teodora` (novo, sob `Império Bizantino`, mesma parada)
  nasce com 3 vídeos taggáveis** (`Theodora`, `Justinian`, `The Nika
  Revolt`), mas o assunto já é o 4º no canal — `Episode 22 - Justinian's
  Legacy` (lote 91) já está travado sem subtema. Pendência registrada,
  não resolvida.
- **`Perda da Anatólia` (novo, sob `Império Bizantino`, mesma parada)
  nasce com 3 vídeos** — o mesmo recorte (1070-1180, entre Manzikert e a
  Quarta Cruzada) contado de três ângulos: estratégia romana, vida
  bizantina e vida turca na Anatólia.
- **`Primeira Cruzada` ganhou 12 vídeos numa janela só** (18→30) — quase
  toda a série de episódios originais do canal sobre a Primeira Cruzada
  (2015-16), sem campo `Period:` (recurso que só apareceu em episódios
  posteriores do podcast), classificados inteiramente por conhecimento
  geral sobre a cronologia 1095-1099. Fact-checado na parada (Niceia,
  Dorileia, Antioch) — todas as datas bateram.
- **Cadeia cronológica sem lacuna nem sobreposição, achada na parada dos
  lotes 95-99**: os subtemas dinásticos do canal The History of Byzantium
  Podcast — `Dinastia Isáurica` (717-802) → `Nicéforo I e a Crise
  Sucessória` (802-820) → `Dinastia Amória` (820-856) → `Ascensão
  Macedônia` (866-912) → `Romanos I Lekapeno` (912-944) → `Focas e
  Tzimisces` (948-976) → `Basílio II` (976-1025) → `Crise do Século XI`
  (1025-1081) → `Dinastia Comnena` (1081-1180) → `Dinastia Angelo`
  (1180-1204) → `Império de Niceia` (1204-1261) → `Dinastia Paleóloga`
  (1261-1453) — cobrem 717-1453 d.C. inteiro sem se sobrepor. Não
  planejado; emergiu lote a lote conforme o canal foi revelando o
  próprio material. Os três `O Império em ___` (800/900/1025) são uma
  família à parte: episódios de interlúdio ("estado do império" num ano
  redondo), não narrativa dinástica.
- **6 pendências acumuladas de linhas já travadas sem subtema** (lotes
  90, 91, 94, 97), por terem sido classificadas antes dos termos que
  as cobririam existirem: 2 de `Dinastia Angelo`, 1 de `Justiniano e
  Teodora`, 1 de `Crise do Século XI`, 2 de `O Império em 900`.
  Nenhuma corrigida — reabrir linha travada exige decisão humana
  explícita, não uma inferência da própria classificação.
- **Duplicatas de episódio confirmadas, não é bug de dedup**: 4 pares de
  vídeos com o mesmo número/título de episódio mas `video_id` e
  descrição diferentes apareceram nos lotes 95-99 (`Episode 168 - A
  Guided Tour`, `Episode 125 - A Tsar is Born`, `Episode 109 - Leo the
  Wise?`, `John Chrysostom Part 1`) — o canal genuinamente subiu duas
  versões distintas do mesmo episódio numerado em momentos diferentes.
  Classificados separadamente, cada um pela própria evidência.
- **Cadeia dinástica estendida até 457 d.C. nos lotes 100-102**: 5 elos
  novos na ponta antiga — `Anastásio I` (491-518) → `Justiniano e
  Teodora` (estendido para trás, agora 518-565) → `Sucessores de
  Justiniano` (565-610) → `Heráclio` (610-641) → `Constans II e
  Constantino IV` (641-681) → `Justiniano II e a Anarquia` (685-717),
  emendando exatamente onde `Dinastia Isáurica` (717-802) já começava.
  Mais dois episódios de interlúdio (`O Império em 500`, `O Império em
  600`) — o `Episódio 12` revela que o formato inteiro descende do "tour
  do império" original do canal (episódios 6-13, o mais antigo do
  podcast).
- **8 duplicatas de episódio confirmadas no total** (4 novas nos lotes
  100-102: `Episode 69`, `Episode 46`, `Episode 22`, `Episode 20`, mais
  uma terceira versão de `Episode 16 - Theodora` e `Episode 1a`) — mesmo
  padrão já documentado no `protocolo.md`.
- **Lacuna de regex nova, achada no fact-check da parada dos lotes
  100-102**: `RE_DATA` não pegava data no formato "estação do ano + ano"
  quando uma palavra separava a preposição do número (`"By Spring 542"`
  — o "by" não fica colado no "542"). `"In the Summer of 533"` já
  funcionava (o "of" fica colado no número). Corrigido no `coletar.py`
  adicionando nomes de estação como palavra solta, mesmo mecanismo já
  usado para nomes de mês — testado contra as duas frases reais antes de
  aceitar. Ver `protocolo.md`, "Armadilhas conhecidas".
- **`Sakoku` (tema-raiz já existente, do Kings and Generals) vs. `Xogunato do
  Japão > Período Edo` (subtema novo, canal The Shogunate, lote 110).** O
  início do Sakoku (1639, `oCXVe3iYMlA`, lote 112) cai dentro do próprio
  intervalo do período Edo (1603-1868) que o subtema cobre — usei o tema mais
  específico (`Sakoku`) em vez do subtema, mas os dois convivem sem colisão de
  conteúdo por ora (nenhum dos 6 vídeos de `Período Edo` toca o fechamento do
  país). Pendente: se aparecer mais conteúdo de Sakoku, decidir se ele vira
  subtema de `Xogunato do Japão > Período Edo` em vez de tema-raiz próprio.
- **Três temas-raiz `Aleatório` para jogos no canal The Shogunate (lotes
  110-112): `Jogos de samurai` (12, específico do Japão/samurai), `Jogos de
  estratégia` (1, Age of Empires 3, genérico) e `Jogos de tabuleiro e cartas`
  (1, jogo de cartas "Time Rift").** Divididos por mídia/escopo, não por
  critério fechado — um jogo de tabuleiro sobre samurai, por exemplo, cairia
  em qual dos dois? Não testado ainda. Pendente: revisar se merecem virar um
  tema-pai (`Jogos`) com subtemas por mídia, mesmo padrão já discutido para
  outras famílias de temas-raiz irmãos.
- **`Formação do Japão Guerreiro` (novo, 300-1156) vs. `Guerra Genpei` (novo,
  1156-1192), ambos do canal The Shogunate, lote 110-111.** Fronteira na
  Rebelião Hōgen (1156). O Panorama `War in Japan (300-1392)` (`toPWGChbQm8`,
  lote 110) tecnicamente cruza os dois temas — comportamento esperado de
  Panorama (protocolo.md, "Rótulos grecorromanos na Lista A são
  intencionais"), não um erro, só registrado para quem for revisar o par.
- **`Clãs do Sengoku` (subtema novo, Sengoku Jidai, canal The Shogunate)
  mistura dois formatos: história multigeracional de família** (Mino-Saito,
  Tanegashima, Imagawa) **e biografia de uma única figura** (Hojo Soun,
  Uesugi Kenshin, Akechi Mitsuhide, este último nem fundador de clã, só
  general/traidor famoso). Funciona hoje como guarda-chuva de "figuras e
  famílias do Sengoku", não estritamente "clãs" — o nome pode ficar impreciso
  se o canal continuar. Considerar renomear para algo como `Daimyos e clãs
  do Sengoku` numa parada futura.
- **`Clãs do Sengoku` ficou ainda mais heterogêneo nos lotes 113-116 (16
  vídeos): passou a incluir biografia de pessoa sem clã fundado (Miyamoto
  Musashi), ensaios revisionistas ("In Defense of...", Takeda Katsuyori e
  Imagawa Yoshimoto) e um caso de dois clãs homônimos sem relação nenhuma**
  (`History of the Hojo Clan (Both Original and Later)`, que soma os
  regentes do Xogunato Kamakura, 1203-1333, com o Later Hojo do Sengoku
  Jidai, 1493-1590 — vira Panorama de 387 anos dentro do mesmo subtema). A
  pendência de renomear (ver item acima) fica mais urgente a cada lote.
- **`Ranking de samurais` (novo, Panorama 940-1877, lote 115) vs. `Últimas
  Resistências Samurai` (Panorama 1561-1877, lote 112), ambos do canal The
  Shogunate.** Dois temas-raiz para "ranking de figuras samurai reais
  através de toda a história" — um tier list geral, outro específico de
  última resistência/morte em combate. Mesmo domínio, critério de separação
  ainda não testado contra um terceiro caso (ex.: um ranking temático
  específico, tipo "melhores estrategistas", que já existe como linha solta
  dentro de `Sengoku Jidai` sem tema próprio — `Top 10 Greatest Samurai
  Strategists`, lote 116).
- **`Xogunato do Japão` (guarda-chuva de governança) e `Família Imperial do
  Japão` (novo, lote 116) cobrem domínios vizinhos sem sobreposição de
  conteúdo até agora, mas a linha entre os dois não está testada.** A
  distinção pretendida é xogunato/shogun (governo militar) vs. corte/
  imperador (autoridade simbólica), mas um vídeo sobre a relação entre os
  dois poderes (como `How the Samurai Relate to the Japanese Nobility and
  Imperial Court`, lote 113) já ficou em `Xogunato do Japão` antes de
  `Família Imperial do Japão` existir — se aparecer mais conteúdo assim,
  decidir qual dos dois recebe.
- **Vídeo de "discussão"/debate do canal The Shogunate pode estar ancorado
  a um evento datado específico (entra na linha do tempo) ou ser um debate
  metodológico amplo sem evento (Extra) — o formato "discussion video" não
  decide sozinho.** `Did Oda Nobunaga Really Influence Samurai Warfare at
  Nagashino?` (lote 116) foi para `Sengoku Jidai > Batalha de Nagashino`
  (linha do tempo) por debater um evento específico (1575); `When did the
  Sengoku Jidai REALLY Start (and End)?` (lote 115) e `The Problem With
  "Feudal" Japan` (lote 114) foram para `Historiografia`/Extra por serem
  debates metodológicos sem evento único. Critério não confirmado por
  revisão humana ainda — ver `protocolo.md`, "Armadilhas conhecidas".

### Resolvidas na aprovação do lote 214

Mini-lote de 16 linhas (não 25) — canal History of Philosophy Without Any
Gaps Podcast esgotou a série numerada principal (HoP) neste lote, chegando
ao próprio `HoP 001 - Thales`. Introduziu **1 tema-raiz novo**,
`Pré-Socráticos` (13 subtemas): os pré-socráticos jônios (Tales,
Anaximandro, Anaxímenes, Xenófanes, Heráclito), os da Magna Grécia
(Pitágoras, Parmênides, Zenão, Melisso, Empédocles), os pluralistas/
atomistas (Anaxágoras, Demócrito, Leucipo), os Sofistas e Hipócrates. Duas
linhas sobre Sócrates reaproveitaram o subtema já existente sob `Platão`
(lote 213). Nenhuma região nova; usadas por aproximação `Turquia` (jônios)
e `Itália` (Magna Grécia). Confiança: 15 `média` (vidas bem documentadas,
com faixas aproximadas onde a própria historiografia admite incerteza,
sem disputa a ponto de justificar `chute`), 1 `n/a` (Extra). Fact-check da
parada verificou 3 datações de risco (Leucipo, Melisso, Tales) — as 3
bateram, uma exatamente ("Thales of Miletus (624 to 546 BCE)"). **Zero
correções na aprovação.** Uma decisão de fronteira foi sinalizada na
amostra: `HoP 001` mistura "objetivos da série" com conteúdo real (Tales)
— classificado como conteúdo histórico, não `Avisos do canal`, porque a
substância sobre Tales é central, não incidental; lição registrada no
`protocolo.md`, "Armadilhas conhecidas". **Estado do canal:** esgotamento
real confirmado por duas coletas seguintes com 0 vídeos novos nos mesmos
768 percorridos — decisão sobre marcar `encerrado` formalmente ainda
pendente do humano (podcast ativo, não arquivo morto). Detalhes completos
em `canais.json`, campo `observacoes`.

### Resolvidas na aprovação dos lotes 209-213

Cinco lotes (não quatro — a parada só rodou depois do lote 213), canal
History of Philosophy Without Any Gaps Podcast. Marco do ciclo: **quatro
temas-raiz novos de uma vez** — `Platão`, `Aristóteles`, `Filosofia
Helenística e Romana` e `Neoplatonismo Tardo-Antigo` — a coleta reversa
finalmente alcançou o núcleo clássico grego (Sócrates via Platão, todos os
diálogos platônicos principais, o corpus aristotélico inteiro) e a
Antiguidade Tardia pagã (Plotino, Porfírio, Jâmblico, Proclo, os últimos
filósofos pagãos de Atenas/Alexandria), além do Estoicismo romano (Sêneca,
Epicteto, Marco Aurélio), Ceticismo (Pirro, a Academia Cética, Sexto
Empírico), Epicurismo (Epicuro, Lucrécio), Cirenaicos, Cínicos, Cícero,
Galeno e o Platonismo Médio. Introduziu **57 subtemas novos** ao todo.
Confiança: 108 `média`, 1 `alta` (só quando a própria descrição/página do
podcast narra o século explicitamente — "10th century Baghdad"), 1 `chute`
(Pseudo-Dionísio Areopagita, autor anônimo sem identidade resolvida). **A
maioria esmagadora das linhas datadas são pensadores centrais e
extremamente bem documentados** (Platão, Aristóteles, Sócrates, Galeno,
Cícero, Sêneca etc.), sem disputa acadêmica relevante de datação — perfil
de confiança mais "limpo" do canal até agora. Fact-check da parada
verificou 4 datações de maior risco (Pseudo-Dionísio, Escola de Bagdá, os
Cirenaicos, Platonismo Latino) — as 4 bateram, 2 delas exatamente. **Zero
correções na aprovação** — a amostra de 5 linhas sorteadas não revelou
erro (saiu repetitiva: 2 linhas do subtema `Aristóteles` reaproveitado sem
base própria além da vida inteira do filósofo, mas isso é a convenção
padrão já validada). Pendências de vocabulário deixadas em aberto, não
bloqueantes: `Aristotelismo Pós-Aristóteles` × `Sucessores de Platão e
Aristóteles` (mesmo assunto, dois temas); `Platonismo Médio (Painel)` × `O
Renascimento Platônico` (família apertada); `Estética Antiga (De Platão a
Proclo)` na fronteira entre dois temas-raiz; os quatro temas-raiz novos
formam uma cadeia cronológica contínua sem guarda-chuva comum — ver
"Sobreposições ainda por resolver", acima. Nenhuma região nova; 5
aproximações registradas (Ptolomeu/Ibn al-Haytham → Egito, Cirenaicos →
Norte da África, Alexandre de Afrodísias → Turquia, Sêneca → Itália,
Epicteto → Grécia). Detalhes completos em `canais.json`, campo
`observacoes`.

### Resolvidas na aprovação dos lotes 205-208

Quatro lotes, canal History of Philosophy Without Any Gaps Podcast. Marco do
ciclo: **dois temas-raiz novos de uma vez** — `Filosofia Islâmica`
(descoberta no lote 206, ao chegar à cauda/início da série *Philosophy in
the Islamic World* do canal) e `Filosofia Judaica Medieval` (descoberta no
lote 207, logo em seguida, cauda de um arco sobre pensamento judaico
andaluz). O catálogo já documentava HoP, HPC, HAP e HPI; com estes dois, o
podcast passou a ter **seis** domínios registrados. Cobriu o núcleo clássico
de ambas as tradições: Averróis, Avicena, al-Ghazali, Ibn Khaldun, Ibn
'Arabī do lado islâmico; Maimônides, Gersônides, Hasdai Crescas, Judah
Halevi, Ibn Gabirol do lado judaico — além de fechar o arco de Escolástica
Medieval do séc. XII-XIII (Abelardo, Anselmo, Eriúgena, Hildegard von
Bingen, a ascensão das universidades). Introduziu **57 subtemas novos** ao
todo. Confiança: 74 `média`, 8 `alta` (sempre com o século citado no próprio
título ou descrição do vídeo, nunca vida de pensador vinda de busca
externa), **zero `chute`** — diferença marcante do ciclo anterior (12
`chute`, todos textos indianos): aqui os pensadores são figuras centrais e
extremamente bem documentadas, sem disputa acadêmica relevante de datação.
Fact-check da parada verificou 5 datações de maior risco (Ibn Gabirol,
Baḥya Ibn Paquda, Controvérsia Maimonidiana, Hasdai Crescas, Era Mongol) —
as 5 bateram, uma com nuance registrada (o início da "Era Mongol" é uma
escolha de convenção — invasão de 1219-1221 vs. Ilcanato formal de
1256/1260/1265 — não um erro). **Zero correções na aprovação** — a amostra
de 5 linhas sorteadas não revelou erro; uma linha (`HoP 227 - Thirteenth
Century Psychology`) foi sinalizada na apresentação por ter o `alta`
baseado no título do próprio vídeo (não na descrição), mas isso é
consistente com o critério já validado nas paradas anteriores para esse
mesmo canal. Pendências de vocabulário deixadas em aberto, não bloqueantes:
sobreposição `Traduções do Árabe para o Latim` × `Movimento de Tradução
para o Latim`; `Gersônides`/`Hasdai Crescas`/`Ibn 'Arabī` solo × conjunto;
`Maimônides` fragmentado em 5 subtemas; cluster "(Debate Moderno)" (13
subtemas) e cluster "Século XII-XIV" (9 subtemas) — ver "Sobreposições
ainda por resolver", acima. Nenhuma região nova. Detalhes completos em
`canais.json`, campo `observacoes`.

### Resolvidas na aprovação dos lotes 200-204

Cinco lotes (não quatro — a parada só rodou depois do lote 204), canal
History of Philosophy Without Any Gaps Podcast. Marco do ciclo: descoberta
da série **HPI** (*History of Philosophy in India*), não documentada até
então — o catálogo tinha registrado só HoP, HPC e HAP. Introduziu o
tema-raiz `Filosofia Indiana` (49 subtemas) e mais 38 subtemas em
`Escolástica Medieval` (mergulho em Tomás de Aquino, Alberto Magno, Duns
Scotus e a "Filosofia do Século XIV" — seção com esse nome oficial no
próprio site do podcast, confirmada por busca externa). Confiança: 5
`alta` (só quando a própria descrição narra o século/período — "Fourteenth
Century Physics", "late 13th century" — nunca vida de pensador vinda de
busca externa), 67 `média`, 12 `chute` (todas HPI, textos indianos antigos
sem consenso de datação nem na própria literatura acadêmica), 41 `n/a`.
**Fact-check da parada verificou as 5 datações `chute` de maior risco**
(Cārvāka, Vaiśeṣika-Sūtra, Vedānta-Sūtra, Mīmāṃsā-Sūtra, Caraka-Saṃhitā) —
as 5 bateram com a literatura acadêmica, **nenhuma correção necessária**.
**Nenhuma linha corrigida na aprovação** — a amostra de 5 linhas sorteadas
para o humano (4 `Extra` + 1 `chute`) não revelou erro, só uma decisão de
base fraca já sinalizada na hora (`HPI 31`, faixa de 800 anos por disputa
acadêmica real). Pendências de vocabulário deixadas em aberto, não
bloqueantes: sobreposição `Bhagavad-Gītā`/`Mahābhārata`/`Karma`;
fragmentação de `Nyāya` (5 subtemas), `Vaiśeṣika` (3) e `Mīmāṃsā` (3);
convenção "(Debate Moderno)"/"(Painel/Entrevista)" usada 8+ vezes sem
critério fechado de consolidação; cluster "Século XIV" com 4 subtemas
próximos — ver "Sobreposições ainda por resolver", acima. Nenhuma região
nova; 3 aproximações registradas (Buddhaghosa → Índia, origens da
humanidade → África Oriental, Henrique de Gand → Países Baixos). Detalhes
completos em `canais.json`, campo `observacoes`.

### Resolvidas na aprovação dos lotes 184-187

Primeiro ciclo do canal **History of Philosophy Without Any Gaps Podcast**
(Peter Adamson), adotado no lote 184 — e o primeiro canal do catálogo em que
a evidência do vídeo quase nunca traz data: 24 de 25 vídeos por lote sem
nenhum número, descrições de 1-2 frases, zero capítulos. **88 das 100 linhas
foram datadas por busca externa** (`média`), com a fonte registrada em
`notas`; 6 tiveram data própria na descrição (`alta`) e 6 ficaram `chute`,
onde a busca não foi feita e isso está admitido na nota.

- **Faixa reprovada pelo fact-check da parada e corrigida**: `HoP 449 - Anna
  Tropia on Jesuit Philosophy` estava com 1483-1617, faixa reaproveitada da
  Escola de Salamanca — mas a ponta inicial vinha de **Francisco de Vitoria,
  que era dominicano, não jesuíta**. A Companhia de Jesus só foi fundada em
  1540. Corrigida para 1540-1640 ("primeiro século da Companhia"), conforme
  Routledge Encyclopedia of Philosophy e Portal to Jesuit Studies. Ver
  `protocolo.md`, "Armadilhas conhecidas", para a lição.
- **Tema que contradizia os anos da própria linha, corrigido**: `HPC 39.
  Robin Wang on Yin-Yang Thinking` declarava faixa 475 a.C.-220 d.C. sob o
  tema `Dinastia Zhou`, que terminou em 256 a.C. Estreitada para o período
  clássico pré-Qin (475-221 a.C.), que é o que a descrição chama de
  "classical Chinese thought".
- **Inconsistência entre lotes, unificada**: os dois episódios sobre Elisabeth
  da Boêmia estavam em subtemas diferentes — o da correspondência com
  Descartes (lote 185) em `René Descartes`, o biográfico (lote 186) em
  `Elisabeth da Boêmia`. O primeiro foi movido para `Elisabeth da Boêmia`;
  `René Descartes` fica com os episódios que são só sobre ele.
- **Fact-check da parada verificou 4 das 6 linhas `chute`** (jardim francês,
  yin-yang, introdução à filosofia moderna, filosofia jesuíta) — 3 bateram
  com busca externa, 1 foi reprovada e corrigida (acima).
- **Reuso forte de vocabulário existente, apesar de o canal ser de outro
  domínio**: `Revolução Científica` (já existia com a faixa 1610-1633,
  exatamente a janela de Galileu), `Renascimento`, `História da Arte`,
  `Reforma Protestante > Reforma Católica (Contrarreforma)`, `Historiografia`,
  `Dinastia Han`, `Dinastia Zhou > Estados Combatentes`.

### Resolvidas na aprovação dos lotes 180-183

- **Correção de região**: `How the Black Death Killed Rome - The Plague of
  Justinian` (lote 180) saiu de `Mediterrâneo` para `Egito` na aprovação —
  a evidência própria ancora o primeiro surto especificamente no Egito
  romano ("occurred around 540 AD in Roman Egypt... sprung up in the Roman
  fort of Pelusium"), mais específico que a região ampla do império
  inteiro que a peste depois alcançou.
- **Fact-check da parada verificou 4 datações** (galinhas sagradas/Batalha
  de Drépano 249 a.C., motim das legiões de César 47 a.C., Wojtek o urso
  em Monte Cassino 1944, invasão núbia do Egito por Piye ~720 a.C.) —
  3 bateram exatamente com busca externa; a de Piye ficou 7 anos abaixo do
  consenso (727 a.C.), dentro da margem normal de incerteza cronológica
  egípcia antiga e já sinalizada como `média` (hedge "around") na própria
  linha — nenhuma correção necessária.
- **Nenhuma duplicata de tema encontrada neste ciclo** — busquei
  explicitamente antes de propor `Guerras Germânicas de Roma` e `Cerco de
  Jerusalém (70 d.C.)` contra a Lista C inteira.

### Resolvidas na aprovação dos lotes 176-179

- **Correção de região**: `Ancient Greeks in the Arctic - The Voyage of
  Pytheas` (lote 178) saiu de `Atlântico` para `Ártico` na aprovação — o
  destino notável da viagem tem termo próprio já existente na Lista B, mais
  preciso que a rota inteira.
- **Nenhuma duplicata de tema encontrada neste ciclo** — busquei
  explicitamente antes de propor `Exploração Antiga`, `Meteoros na
  História` e `Harald Hardrada` contra a Lista C inteira; nenhum termo
  parecido já existia (puxando a lição registrada no `protocolo.md` depois
  do episódio `Gladiadores`/`Besteiros Genoveses` da aprovação anterior).
- **Fact-check da parada verificou 5 datações** (fundação dos Jomsvikings,
  nascimento de Olga de Kiev, viagem de Piteas, meteorito em campo de
  batalha romano, reinado hipotético de Sponsian) — todas bateram com busca
  externa dentro de margem normal de incerteza histórica (1-5 anos de
  divergência entre fontes antigas/modernas), nenhuma correção de fato
  necessária.

### Resolvidas na aprovação dos lotes 172-175

- **`Gladiadores Romanos` (proposto no lote 172, canal Invicta) era duplicata
  de `Gladiadores` (já existente, Kings and Generals)** — mesma região
  (Itália), faixa quase idêntica (264 a.C.-404 contra 264 a.C.-435). Fundido
  em `Gladiadores` na aprovação; a linha do Invicta migrou para o tema já
  existente.
- **`Besteiros Genoveses` (proposto no lote 173, canal Invicta) era duplicata
  de `Balestreiros Genoveses` (já existente, SandRhoman History)** — mesmo
  assunto (besteiros/arqueiros de virote genoveses), mesma região (Itália);
  o título em inglês do vídeo do SandRhoman era literalmente "Genoese
  Crossbowmen". Fundido em `Balestreiros Genoveses` na aprovação. Essa linha
  também tinha um bug de sinal (`ano_inicio = -1000`, ou seja 1000 a.C., em
  vez de 1000 d.C. — Genoa não existia em 1000 a.C.), corrigido junto.
- **Rebaixamento de confiança na aprovação**: `The Winter War (1939) - Last
  Stand of the Finns (Part 2 of 2)` (lote 175) saiu de `alta` para `média` —
  só o ano de início (1939) estava na evidência própria da linha; o fim
  (1940) vinha só da Parte 1 da mesma série, não citado nesta linha.
- **Faixa reconstruída em cima de evidência truncada corrigida**: `What Was
  Rome's Most Remote Outpost?` (lote 173) tinha uma faixa estreita
  (100-150) chutada sem base real, sobre uma descrição cortada que não
  nomeia o posto avançado. Alargada para o Principado inteiro (27 a.C.-284
  d.C., vira `Panorama`) para não fingir uma precisão que a evidência não
  sustenta — ver `protocolo.md`, "Armadilhas conhecidas", para a lição.

### Resolvidas na aprovação dos lotes 100-102

- **4 datações de risco confirmadas por fact-check na parada, nenhuma
  corrigida**: Batalha do Yarmuk (636), conquista persa de Alexandria
  (619), revolta de Vitaliano (513-515), Batalha de Dara (530) — todas
  bateram.
- **8 termos novos incorporados**, todos sob `Império Bizantino`:
  `Heráclio`, `Constans II e Constantino IV`, `Justiniano II e a
  Anarquia`, `O Império em 700`, `Sucessores de Justiniano`, `O Império
  em 600`, `O Império em 500`, `Anastásio I` — nenhum tema-raiz ou
  região nova.
- **1 bug de regex corrigido** (ver acima) — testado contra os dois
  casos reais que falharam antes de aceitar.
- **Canal esgotou a coleta no lote 102** (chegou ao Episódio 1, o
  primeiro do podcast inteiro, de 2007) — só vieram 19 vídeos, não 25.
  Decisão de `/encerrar` deixada para o humano.

### Resolvidas na aprovação dos lotes 95-99

- **5 datações de risco confirmadas por fact-check na parada, nenhuma
  corrigida**: Segundo Concílio de Niceia (787), Concílio de Hiéria
  (754), guerra civil de Constantino V contra Artabasdos (741-743),
  assassinatos de Bardas (866) e Miguel III (867) por Basílio I, morte
  do Tsar Simeão da Bulgária (927) — todas bateram.
- **10 termos novos incorporados**, todos sob `Império Bizantino`:
  `Dinastia Isáurica`, `Nicéforo I e a Crise Sucessória`, `Dinastia
  Amória`, `Ascensão Macedônia`, `Romanos I Lekapeno`, `Focas e
  Tzimisces`, `Basílio II`, `Crise do Século XI` (extensão), `O Império
  em 800`, `O Império em 900`, `O Império em 1025` — nenhum tema-raiz ou
  região nova.
- **Janela com a maior proporção de `chute` do canal até agora** (64 de
  125 linhas) — cinco lotes cobrindo seis dinastias em pouco mais de
  três séculos (717-1025), quase sem nenhuma data própria na
  descrição/tags da maioria dos episódios.

### Resolvidas na aprovação dos lotes 91-94

- **1 datação confirmada por fact-check pontual na aprovação** (fora da
  parada formal, resolvendo uma pendência que ela deixou aberta): cerco
  de Dirráquio por Boemundo (`7Sg-9_X1WSc`, lote 93) — busca externa
  confirmou 1107-1108 (out/1107 a set/1108, Tratado de Devol). Faixa
  mantida sem alteração.
- **Nenhuma outra correção de datação exigida** — o fact-check da parada
  verificou 4 datas de risco adicionais (Manzikert 1071, Grande Cisma
  1054, golpe de Alexios I 1081, cerco de Niceia/Dorileia/Antioquia
  1097-98) e todas bateram.
- **5 termos novos incorporados**: subtemas `Dinastia Comnena`, `Crise
  do Século XI`, `Dinastia Angelo`, `Justiniano e Teodora` e `Perda da
  Anatólia` (todos sob `Império Bizantino`); nenhum tema-raiz ou região
  nova — `Rússia`, `Itália`, `Oriente Médio` já existiam na Lista B.
- **3 pendências de subtema em linhas já travadas, não corrigidas**:
  2 linhas do lote 90 (`Dinastia Angelo`) e 1 linha do lote 91
  (`Justiniano e Teodora`) tratam do mesmo assunto que termos criados
  depois delas serem travadas — ficaram para trás por decisão de não
  reabrir linha travada sem correção humana explícita.

### Resolvidas na aprovação dos lotes 87-90

- **Nenhuma correção de datação exigida pela parada** — o fact-check
  verificou 4 datações de risco (usurpação de Michael VIII Palaiológos,
  1258-59; Quarta Cruzada Parte 1, 1198-1203; Balduíno I de Flandres,
  1204-05; cerco árabe a Constantinopla, 717-718) e todas bateram com as
  faixas já declaradas.
- **Convenção de canal registrada**: o campo `Period: XXXX-YY`, presente
  na descrição da maioria dos episódios narrativos deste canal, é tratado
  como confiança `alta` em toda a coleta — é metadado estruturado e
  deliberado do próprio podcaster sobre o escopo do episódio, não um
  número incidental em prosa. Primeira aplicação no lote 87
  (`RGuY5rqtIJI`); mantida em todos os lotes seguintes.
- **2 termos novos incorporados**: subtemas `Dinastia Paleóloga` e
  `Império de Niceia` (ambos sob `Império Bizantino`); nenhum tema-raiz
  ou região nova — todas as regiões usadas (`Turquia`, `Bálcãs`, `Itália`,
  `Grécia`, `Egito`, `Irã`, `Mediterrâneo`, `Global`) já existiam na
  Lista B.
- **Canal com proporção alta de `Extra`**: das 100 linhas dos quatro
  lotes, 56 ficaram `Extra`/`Historiografia` (entrevistas com autores,
  Q&A de ouvintes, retrospectivas "10 ___", e a série de vídeos "goes to
  Istanbul" sobre sítios que sobrevivem hoje) — o canal mistura narrativa
  cronológica com um volume grande de conteúdo de recepção/entrevista.
- **2 episódios antigos (nº 69 e nº 46) resurgiram fora de ordem no lote
  90**, republicados junto com uploads recentes — cerco árabe a
  Constantinopla (717) e a guerra de Heráclio contra a Pérsia (610-628).
  Classificados pelo conteúdo, sem campo `Period:`.

### Resolvidas na aprovação dos lotes 85-86

- **Nenhuma correção de datação exigida pela parada** — o fact-check
  verificou as datas de "conhecimento geral" usadas para justificar
  fronteiras (Batalha de Adrianópolis, 378 d.C.; assassinato de Aécio, 454
  d.C.; invasões de Átila, 451-453 d.C.) e todas bateram com as faixas já
  declaradas nas linhas. O único item de risco sem confirmação (`Roman
  History 18`, acima) ficou como estava, por falta de fonte, não por
  correção.
- **Nenhuma confiança `alta` nestes dois lotes** — 4 `alta` só no lote 85
  (`ItwGz43a_ak`, `plm9DvpInyY`, datas repetidas na própria descrição), 0
  no lote 86 (canal inteiro do lote é boilerplate de podcast sem número
  fora do título).
- **2 termos novos incorporados**: subtemas `Crise do Século III` e
  `Dinastia Constantiniana` (ambos sob `Império Romano`); nenhum
  tema-raiz ou região nova — `Itália` e `França` já existiam na Lista B.
- **Playlist explícita, não canal inteiro**: primeira coleta via
  `coletar.py --playlist ID --nome "..."` (ver `protocolo.md`). A
  playlist "History of Rome" (36 vídeos, 753 a.C.-476 d.C.) está esgotada
  — os dois lotes (85-86, 36 linhas) cobrem o total.
- **1 bug de processo achado e corrigido nesta janela** (fora do
  `coletar.py`, no processo de gravação manual): linhas novas anexadas ao
  fim da planilha quebram a ordenação cronológica da Lista A — corrigido
  reordenando a planilha inteira pela chave `(ano_inicio, ano_fim, Mês,
  Dias)` antes de gravar, em vez de só apensar. Documentado no
  `protocolo.md`, "Armadilhas conhecidas".

### Resolvidas na aprovação dos lotes 83-84

- **2 datações corrigidas por fact-check na aprovação** (substituindo a
  parada formal, que não rodou para este mini-ciclo de 2 lotes — o
  canal esgotou a coleta em 0 vídeos novos antes de completar quatro):
  `The Kingdom of Ceredigion` (`fXKG122NdbQ`, lote 84) alargada de
  `450-872` para `450-920` — a descrição do próprio vídeo diz que o
  arco termina na "unity with Dyfed", e busca externa mostra que esse
  evento é a formação de Deheubarth por Hywel Dda em 920 (não a morte
  de Rhodri Mawr em 878, confundida na classificação original com o
  contexto de Gwynedd de outras linhas do mesmo lote); `Dyfed - An Irish
  Kingdom In Wales` (`_oeUpbarWeo`, lote 84) ajustada de `400-900`
  (estimativa arredondada) para `400-920`, o mesmo evento real,
  registrado como correção-irmã.
- **Nenhuma confiança `alta` precisou ser rebaixada nesta janela** — só
  2 linhas `alta` nos dois lotes (`pZi13qIDIOM`, "100BC" citado
  diretamente na descrição; `6YpHJvl2A38`, "In 1157, Henry the II..."
  citado diretamente na descrição) — as duas com número real narrando o
  evento na própria descrição, não no título.
- **Mini-ciclo de 2 lotes, não os 4 de costume** (mesmo padrão já usado
  para os lotes 38-39 e para a revisão pontual do lote 76): o canal
  Cambrian Chronicles esgotou sua coleta (58 vídeos percorridos, 0
  novos) antes de fechar um quarto lote. Decisão do humano: aprovar os
  dois lotes existentes (83-84, 38 linhas) e deixar o canal `em
  andamento`, sem encerrar — pode ser revisitado depois com
  `python coletar.py @CambrianChronicles`.
- **1 subtema novo incorporado retroativamente a linhas não travadas**:
  `Reino de Gwynedd` foi adicionado a duas linhas do lote 83
  (`NTOPGwKlzzk`, Llywelyn Fawr; `nMA6SFyjO80`, Maelgwn Gwynedd) durante
  a classificação do lote 84, antes de qualquer trava — permitido porque
  nenhuma das duas ainda tinha passado por `/aprovar`.
- **2 termos novos incorporados**: subtemas `Reino de Gwynedd` (sob
  `História de Gales`) e `Mitos de Wikipédia` (sob `Historiografia`);
  nenhum tema-raiz ou região nova.
- **2 bugs de processo achados e corrigidos nesta janela, ambos
  documentados no `protocolo.md`**: lacuna de regex para duração por
  extenso ("for two centuries", "over 200 years") no `coletar.py`; e
  `UnicodeEncodeError` ao imprimir um título com caractere fora do
  cp1252 do console Windows, corrigido reconfigurando `stdout`/`stderr`
  para UTF-8.

### Resolvidas na aprovação dos lotes 79-82

- **2 datações corrigidas por fact-check na parada**: `Bureaucracy in
  Cleopatra's Egypt` (`DiG0LomEptE`, lote 81) alargada de `51 a.C. - 30
  a.C.` (reinado pessoal de Cleopatra) para `100 a.C. - 30 a.C.` — o
  resumo do próprio episódio descreve o vídeo como sendo sobre "first
  century BC Egypt" de forma geral, e "Cleopatra's Egypt" é metonímia
  popular para o sistema ptolomaico do último século, não um recorte
  estrito do reinado dela; nota da `Lupercalia` (`a_ZGSpQaw3A`, lote 82)
  corrigida para remover a alegação de que o festival foi "convertido" no
  Dia dos Namorados/Candelária — busca externa mostra que essa ligação é
  folclore moderno sem base documental contemporânea (o ano da abolição,
  494 d.C., estava correto).
- **1 ambiguidade documentada, não corrigida**: `The Pontifex Maximus`
  (`NcCtiX-VuWA`, lote 81) mantido em 383 d.C. para o abandono do título
  por Graciano — fontes divergem entre 382 (maioria) e 383 (ligado à
  embaixada de senadores pagãos); registrado na nota da linha.
- **Nenhuma confiança `alta` precisou ser rebaixada nesta janela** — 0
  linhas `alta` nos quatro lotes inteiros (53 `média`, 24 `chute`, 2
  `n/a`), porque o canal Historia Civilis não põe nenhuma data em
  descrição/tags (só boilerplate de Patreon/links) — toda data vem do
  título ou de conhecimento geral, então nada passou do teto certo.
- **5 temas novos incorporados**: `Pomério Romano`, `Triunfo Romano`,
  `Julgamentos de animais`, `Congresso de Viena`, `Reforma Eleitoral de
  1832` — todos do lote 79; nenhum subtema ou região nova em nenhum dos
  quatro lotes.
- **4 sobreposições registradas, não resolvidas**: cluster institucional
  de `República Romana` (8 vídeos), uso elástico de `Guerra Civil de
  César` para prelúdio político, crescimento de `Reino de Roma` (1→3) e
  quarta aproximação de `Turquia` (Carrhae/Harran). Ver "Sobreposições
  ainda por resolver", acima.
- **Amostra de 5 linhas apresentada ao humano e aprovada sem correção
  adicional** (Antony's Invasion of Parthia, Battle of the Teutoburg
  Forest, Battle of Pharsalus, Battle of Cannae, Bureaucracy in
  Cleopatra's Egypt) — a última sinalizada explicitamente na apresentação
  como a decisão de base mais fraca da amostra (corrigida depois, ver
  acima).
- **Achado durante a gravação do lote 81, não durante a parada**: o
  script de gravação ordenava só por `ano_inicio`/`ano_fim`, sem
  `Mês`/`Dias` — uma linha nova de Cannae (`Mês=*`) ficou fora de ordem
  contra uma linha já existente da mesma data com mês real (`Mês=8`,
  Kings and Generals). O `verificar.py` pegou o erro antes da gravação
  ser aceita; corrigido reordenando a planilha inteira pela mesma chave
  do portão, sem alterar nenhum valor de célula. Ver `protocolo.md`,
  "Armadilhas conhecidas".
- **Ciclo de quatro lotes fechado normalmente** (79, 80, 81, 82 — o
  último com só 4 linhas, não 25, porque o canal Historia Civilis está
  ficando sem vídeo novo para aprovar). Próxima coleta pode vir vazia;
  se vier, é sinal para considerar `/encerrar` o canal.

### Resolvidas na aprovação dos lotes 76-78

- **2 datações `chute` corrigidas por fact-check na parada**: fundação de
  Tiwanaku (`sybbruxeJu8`/`yXW1PU9xBRg`, ambas) de `300` para `200`
  (datação bayesiana por radiocarbono mais recente converge em ~150-180
  d.C.; 300 era o extremo mais antigo de uma faixa já incerta); início da
  Cultura do Cobre Antigo (`cpmMY_Rcbd8`) de `4000 a.C.` para `3000 a.C.`
  (faixa mais citada na literatura). 3 outras datações de risco
  verificadas por busca externa e confirmadas sem divergência: fundação
  dos toltecas em Tula (~900-1150/1168, consenso recente confirma 900s,
  não 750), Marajoara (400-1300 bate com o próprio título do artigo de
  referência de Denise Schaan na *Antiquity*), fundação de Tzintzuntzan
  pelos tarascos (~1325, múltiplas fontes convergem).
- **Nenhuma confiança `alta` precisou ser rebaixada nesta janela** — só 2
  linhas `alta` na janela inteira (Cyrus, lote 76; Colapso Maia, lote
  77), as duas com número real narrando o evento na própria descrição.
  Duas linhas que tinham só uma ponta da faixa ancorada em evidência
  (Tupinambá, lote 77; Tarascos, lote 78) já tinham entrado como `média`,
  não `alta` — critério aplicado corretamente desde a classificação, sem
  precisar de correção na parada.
- **1 correção retroativa numa linha não travada**: `Região` de
  `Tupinambá` (`Q1KcyEnFbzA`, lote 77) atualizada de `América do Sul`
  para `Brasil`, depois que `Brasil` foi criado como termo novo no lote
  78 (`Marajoara`). Só possível porque a linha ainda não estava travada.
- **31 temas, 9 subtemas e 5 regiões novos incorporados** — o maior
  volume de vocabulário novo de uma parada só até agora, por ser o
  primeiro ciclo de um canal num domínio (arqueologia pré-colombiana) sem
  nenhuma sobreposição com o vocabulário existente. Ver Lista B e Lista C,
  acima, e "Sobreposições ainda por resolver" para a questão de nome do
  `Chavín de Huántar`.
- **Amostra de 5 linhas apresentada ao humano e aprovada sem correção
  adicional** (Cyrus/Cilindro de Ciro, Rise of the Olmec, Muisca, Monte
  Albán/Zapotecas, 100K Q&A) — 3 das 5 eram faixas `chute` inteiramente
  construídas por pesquisa externa, sem nenhum número no próprio vídeo,
  sinalizado explicitamente na apresentação como a decisão de base mais
  fraca do lote.
- **Mini-ciclo de 3 lotes, não os 4 de costume** (mesmo padrão já usado
  para os lotes 38-39): a parada foi pedida com o lote 79 ainda não
  coletado. Próximo ciclo de quatro lotes recomeça a contagem em 79.

### Resolvidas na aprovação dos lotes 72-75

- **`Sweden's Role in WWII` (`V6KH4eaRhPs`, lote 71, linha travada) recebeu
  o subtema `Potências Neutras`**, com aprovação explícita do humano — a
  própria descrição de "Turkey's Role in WWII" (lote 75) confirma ser uma
  "five-part series" sobre potências neutras; Irlanda (lote 73), Turquia,
  Suíça e Portugal (lote 75) já tinham o subtema, só faltava a Suécia para
  fechar o grupo de 5.
- **4 datações de risco verificadas por busca externa**: Reino Ostrogodo
  (493-553, confirmado exato), Reino Borgonhão (411-534, confirmado
  exato), Guarda Varegue (988-1204, confirmado exato); Espanha Visigótica
  (507-711) confirmada como defensável, mas há moldura alternativa (uma
  fonte usa 409, a chegada inicial à Ibéria, em vez de 507, a Batalha de
  Vouillé) — não corrigido, ambas são leituras válidas.
- **12 temas novos incorporados**: `Rússia Medieval`, `Guerra Medieval`,
  `França Medieval`, `Canato Avar`, `Idade das Trevas Global`, `Guerra
  Bizantino-Sassânida`, `Império Sassânida`, `Reino Lombardo`, `Reino
  Visigodo`, `Reino Ostrogodo`, `Reino Borgonhão`, `Cristianismo
  Primitivo`. Nenhuma região nova (`Europa Ocidental` foi usada por
  aproximação para a Suíça, termo já existente na Lista B).
- **Nenhuma confiança `alta` precisou ser rebaixada nesta janela** (21
  linhas `alta`, todas com número real narrando um evento na própria
  descrição — inclusive duas com "about" na frente de um número especifico,
  tratadas como número real com ressalva epistêmica honesta, não como
  vaguidão).

### Resolvidas na aprovação dos lotes 68-71

- **"16-Bit Wars Rehashed" (`GPCYW0doc7Y`, lote 68) teve a faixa estendida
  de `1989-1996` para `1989-1997`**, depois de fact-check mostrar que o
  Sega Genesis foi descontinuado em 1997, não 1996 (fontes: Wikipedia,
  HisCoGa). Linha ainda não travada, corrigida antes de travar.
- **4 datações de risco verificadas por busca externa, todas confirmadas
  sem divergência**: civilização fenícia (Met Museum, "The Phoenicians
  1500-300 B.C." — o próprio título do ensaio bate com a faixa do
  catálogo); Três Augustos e Cinco Imperadores da China (2852-2070 a.C.,
  datação tradicional confirmada, embora lendária); civilização minóica
  (3000-1100 a.C., confirmado); escândalo Enron (2001, confirmado pela
  cronologia da FERC).
- **"Sweden's Role in WWII" (lote 71) menciona concluir uma "série sobre
  potências neutras" — checagem rápida no catálogo não encontrou episódios
  anteriores dessa série já catalogados** (Suíça, Irlanda, Espanha,
  Portugal na Segunda Guerra) sob nenhum título parecido. Não investigado a
  fundo; se aparecerem em lotes futuros, ligar pelas tags/descrição, não
  pelo título.
- **8 temas novos incorporados**: `Resenhas de ficção`, `História dos
  videogames` (recriado), `Esportes`, `Jogos retrô`, `Grécia Arcaica`,
  `Civilização Fenícia`, `Renascimento`, `Formação das Monarquias
  Nacionais`. Nenhum subtema ou região nova.
- **Nenhuma confiança `alta` precisou ser rebaixada nesta janela** — as 10
  linhas `alta` da janela (checadas na amostra e na resposta de cada lote)
  tinham todas número real narrando um evento na própria descrição.

### Resolvidas na aprovação dos lotes 64-67

- **`Sibyrtios` (`zOX04aIJm2g`, lote 64) recebeu o subtema `Segunda Guerra
  dos Sucessores`**, que já devia ter sido atribuído na classificação
  original — a própria nota da linha dizia que ela "fecha o trio" desse
  subtema junto com Teutamos e Eudamos, mas o campo `Subtema` ficou vazio
  por engano. Achado na parada, corrigido antes de travar (linha ainda não
  estava travada).
- **`Super Tuesday Predictions with Sean Chick` (`X0ROqOQxlFw`, lote 60,
  linha travada) teve a confiança rebaixada de `alta` para `média`**, com
  aprovação explícita do humano. A nota original apoiava `alta` em "2020"
  citado na descrição ("the various races and candidates in the 2020
  field") — mas isso é rótulo genérico do ciclo eleitoral, não a narração de
  um evento datado (como "1863" para Sherman ou "917" para Leo Phocas
  foram). Esse critério mais rigoroso só ficou explícito a partir do lote
  67; esta foi a única linha `alta` anterior a esse ponto que usava o mesmo
  padrão de rótulo genérico — as outras linhas com "2020" em descrição
  (Hickenlooper, Williamson, etc.) já tinham sido classificadas `média`
  desde o início.
- **5 linhas residuais de lotes anteriores (44, 52, 58×2, 59), já
  reclassificadas com nota detalhada em 30/07/2026 mas nunca travadas,
  foram travadas nesta aprovação**: `6NxqOlQm7Mw` (Early Rome: Monarchy and
  Early Republic), `7s50oTbp6-M` e `WN-vegx4RQ8` (H.G. Wells — Roman
  Republic/Fall of the Republic), `nYEtFFz86ls` (G.P. Baker/Teutoburg),
  `_9-5BjlOknU` (History of Britain X). Não precisaram de reclassificação —
  só faltava o `travado`/`status` final.
- **3 datações de risco verificadas por busca externa**: Antípatro Etesias
  (neto de Cassandro, deposto em 279 a.C., confirma a faixa `297-279 a.C.`
  de "The Last Antipatrids"); Neolítico chinês pré-Xia (Yangshao ~5000-3000
  a.C., Longshan ~3000-1900 a.C., confirma a faixa `5000-2000 a.C.`
  declarada); mandato de Bush como governador do Texas (real: 17/01/1995 a
  21/12/2000 — o "1995-2001" do título do canal inclui a transição até a
  posse presidencial; não corrigido, é a moldura do próprio canal). Uma
  parcialmente confirmada: Alexandre I do Épiro/Eácides ("Pyrrhus'
  Predecessors", faixa `350-313 a.C.`) — o fim bate exato (313 a.C.), o
  início real é 343 a.C., não 350 — chute impreciso, não corrigido.
- **3 termos novos incorporados**: subtemas `Primeira Guerra dos Sucessores`
  e `Segunda Guerra dos Sucessores` (Guerras dos Diádocos), `Bush 43 Still
  Sucks` (História dos Estados Unidos). Nenhum tema ou região nova.

### Resolvidas na aprovação dos lotes 60-63

- **Faixa de Egina (`5L6Ow0kgLw4`, lote 60) estendida de `800 a.C. - 480 a.C.`
  para `800 a.C. - 431 a.C.`**, depois de fact-check por busca externa mostrar
  que a rivalidade naval de Egina com Atenas só termina com a expulsão da
  população aeginetana em 431 a.C., não com a Batalha de Salamina (480 a.C.),
  que foi o corte usado originalmente por seguir de perto o enquadramento do
  próprio vídeo ("leading naval and trade power of the Archaic period").
  Continua `Panorama`, só os limites mudaram.
- **Metellus Numidicus (`-d2DITW2uCs`, lote 57, linha travada) recebeu o
  subtema `Guerra Jugurtina`** (criado no lote 60 para o mesmo assunto),
  correção de célula única autorizada explicitamente pelo humano na aprovação
  — mesmo padrão dos casos `Sula` e `Guerras da Chechênia`, mas desta vez a
  correção foi de fato aplicada, não só registrada como pendente.
- **4 datações confirmadas sem divergência por busca externa**: queda de
  Halicarnasso para Alexandre (334 a.C., Livius.org/Wikipedia), reinado de
  Frederico Guilherme I da Prússia (1713-1740, exato, Wikipedia/
  Encyclopedia.com), fundação/queda do Império Aquemênida (550-330 a.C., exato,
  Met Museum/Britannica), reinados de Romanus I Lecapenus (920-944, exato) e
  Constantine VII Porphyrogenitus (913-959, exato), ambos Wikipedia.
- **4 temas novos e 4 subtemas novos incorporados**: temas `Egina`, `Corinto`,
  `Halicarnasso` (cluster de pólis grega, mesmo padrão de Esparta/Épiro
  antigo/Tessália antiga), `História alternativa` (cenário eleitoral
  contrafactual, `Aleatório`); subtemas `Guerra Jugurtina` (República Romana),
  `Marcha para o Mar` (Guerra Civil Americana), `Guerras Índias` (História dos
  Estados Unidos), `A Charge to Keep` (Historiografia). Nenhuma região nova —
  as 100 linhas usaram só termos já existentes na Lista B.
- **Amostra de 5 linhas apresentada ao humano, tudo aprovado sem correção**:
  `SXW6SyCuptg` (GWB Charge to Keep Cap. 8), `LWMvy0Dsqb4` (Sherman Series
  Introduction), `mpdFz5onjMI` (Marcus Aurelius Cotta), `ony2-NPmJas` (Leo
  Phocas the Elder), `0i0Sk4pTtoM` (Iowa Caucus 2020). Duas decisões de base
  mais fraca foram sinalizadas na apresentação — a faixa estendida de Marcus
  Aurelius Cotta (74-71 a.C., mistura consulado com evento posterior) e o
  bloco inteiro de "A Charge to Keep" como Extra (ver acima) — e ambas foram
  aprovadas como estão.

### Resolvidas na aprovação dos lotes 56-59

- **Fundação de Bizâncio corrigida de 657 a.C. para 667 a.C.** (linha
  `2Dt0IKGyduc`, "Constantinople: The Capital of Eastern Rome") — fact-check
  por busca externa mostrou que 657 a.C. não bate com nenhuma fonte; o
  padrão mais citado (Heródoto) é 667 a.C., com uma variante antiga
  (Eusébio) em 656 a.C. Provável troca de dígito na classificação original.
  O rótulo continua `Panorama`, só o número mudou.
- **4 confianças `alta` rebaixadas para `média`**, mesma regra fechada na
  parada dos lotes 40-43 (título/tags sozinhos, sem número na descrição ou
  nos capítulos, sustentam no máximo `média`) — desta vez encontradas ao
  reauditar TODAS as linhas `alta` da janela de 4 lotes, não só as
  classificadas nesta sessão: `Es60Jsb5AhM` (Andronicus Ducas, 904-906 CE),
  `JuuJueRCr5Y` (Himerius, 906-912 CE) e `U66rqgMsbfU` (Samuel J. Tilden,
  1876) — todas do lote 57, de uma sessão anterior — e `-d2DITW2uCs`
  (Quintus Caecilius Metellus Numidicus), cuja descrição não tem nenhum
  número (a extração automática já dizia "nenhuma encontrada") e se apoiava
  numa década em prosa ("the 100's and 90's"), não um número que ancorasse
  109 ou 102. Lição: a checagem linha a linha de `alta` precisa ser reaplicada
  em toda parada sobre a janela inteira, não só sobre o que a sessão atual
  classificou — ver `protocolo.md`, "Armadilhas conhecidas".
- **3 linhas reclassificadas de `Aleatório` para `História dos Estados
  Unidos > Política`** (decisão do humano no `/aprovar`): `wIx4DcTwjGc`
  ("March 10 Predictions and Updates"), `u86QWORWGr4` ("Super Tuesday
  Breakdown") e `TGDy2Mw3kgA` ("Bernie vs. Biden: Ides of March Debate
  Analysis") tratam de um pleito real e datado (as primárias democratas de
  2020), mesmo critério já usado nas duas linhas irmãs do lote 57 (`2020
  Election Prediction Update`, `The 2020 Campaign...`). Resolve a
  contradição apontada na parada: o mesmo gênero de vídeo vinha recebendo
  tratamento oposto dentro da mesma janela de 4 lotes. Confiança `média`
  nas três (a data exata aparece só em tags/contexto, não como número na
  descrição); `Ano = 2020` com `Mês`/`Dias` do evento específico (10/3,
  3/3, 15/3).
- **Fact-check por amostra, 3 datações confirmadas sem divergência**:
  civilização etrusca (900 a.C.-264 a.C., cultura de Villanova e saque de
  Volsínios), reinado de João I Tzimisces (969-976, exato), revolta de
  Hampsícora na Sardenha (215 a.C., tag da linha de Titus Manlius Torquatus).
- **13 termos novos incorporados**: temas `Avisos do canal`, `Comentário
  Político Contemporâneo`, `Épiro antigo`, `Tessália antiga`, `Colonização
  Romana`, `Beócia antiga`, `Argos antiga`; subtemas `Candidatos Derrotados`
  (História dos Estados Unidos), `Hilaire Belloc` (Historiografia),
  `Antioquia`, `Alexandria`, `Constantinopla`, `Roma` (Vida urbana). Nenhuma
  região nova — as 91 linhas usaram só termos já existentes na Lista B.

### Resolvidas na aprovação dos lotes 52-55

- **`DvkWMoIYd7s` ("Tier-Ranking 100 NES Games!") corrigido de `Aleatório`/tema
  novo `NES` para `História dos videogames` (tema já existente), com período
  real (`1985-1995`, vida útil do console).** Achado na amostra de 5 linhas da
  parada: a planilha já tinha o padrão oposto — "SNES History and Games
  Tier-Ranking", "Sega Genesis Games Tier-Ranking" e "Xbox 360 Games
  Tier-Ranking" estão todos sob `História dos videogames`, com período real da
  era do console, não `Aleatório`. Regra confirmada nesta parada: tier-ranking
  de figuras/eventos históricos reais (reis, generais, jogos de um console real)
  entra na linha do tempo normalmente; só tier-ranking de **mídia de
  entretenimento como assunto em si** (filmes, música) é `Aleatório` (`John
  Carpenter`, `Steven Spielberg`, `Arnold Schwarzenegger`, `Música dos Anos
  1960`).
- **Subtema `John D. Hicks` (Historiografia, lote 54) revertido para sem
  subtema.** Violava a regra fechada na parada 48-51 (subtema em Historiografia
  só nasce nomeado com 3+ vídeos do mesmo assunto) — só havia 1 vídeo. Mesmo
  tratamento dado a `Money in Politics`/`Slavery, Ancient and Modern`/`F-Tier
  Tournament` na parada anterior: nota mantida, subtema revisitado se aparecer
  um segundo vídeo do mesmo autor.
- **`Early Rome, Part IV: Plutarch's Life of Numa Pompilius` (`IGWChQfeUSs`)
  separado do resto da série `Early Rome` e movido para `Reino de Roma`
  (tema novo), faixa `715 a.C. - 673 a.C.` (reinado tradicional de Numa
  Pompílio), confiança `média` (data lendária/tradicional, não evento
  documentado).** As outras 4 partes da série (I, II, III, V) continuam
  `Extra`/Historiografia — são sobre o método/tradição historiográfica de
  estudar a Roma primitiva, não sobre o conteúdo do reinado em si. Só a Parte
  IV narra efetivamente o reinado de um rei lendário com faixa própria.
- **Fact-check por amostra, 6 datações de risco verificadas por busca
  externa**: fundação/destruição de Cartago (814 a.C./146 a.C., confirmado),
  morte de Basílio II e Batalha de Kleidion (dez/1025 e 1014, confirmado),
  triunfo de Lucius Licinius Murena (81 a.C., confirmado), vida de W.T. Sherman
  (1820-1891, confirmado), premierato de Neville Chamberlain (1937-1940,
  confirmado). Uma ressalva sem correção: o Império Corásmio tem dois marcos de
  fundação na historiografia — 1077 (dinastia Anushtegin, vassala dos
  seljúcidas) e 1127 (reinado de Atsiz, independência efetiva) — o vídeo/título
  usa 1127, que foi mantido (não é erro, é a periodização escolhida pelo
  canal).
- **Classe "tema por era do mesmo conflito/país" ganhou uma 3ª instância**
  (`Guerra do Afeganistão` vs. `Guerra Soviético-Afegã`) — registrada, não
  fundida. Ver "Sobreposições ainda por resolver" acima: humano decidiu reservar
  uma parada dedicada só a essa classe (Chechênia, Israel-Hamas/Hezbollah,
  Afeganistão).
- **10 termos novos incorporados**: temas `Guerra do Afeganistão`, `Império
  Corásmio`, `Reino de Roma`; subtemas `Reforma Agrária dos Gracos` (República
  Romana), `Atenas` (Vida urbana), `HIS 2210` e `Early Rome` e `Military
  Blunders` e `H.G. Wells` (Historiografia). Nenhuma região nova — as 100
  linhas usaram só termos já existentes na Lista B.

### Resolvidas na aprovação dos lotes 48-51

- **3 datações `chute`/conhecimento geral corrigidas por fact-check**: faixa
  dos Reis Ágidas de Esparta (`uDzXASUqRUI`) estreitada de `930-222 a.C.` para
  `900-215 a.C.` — Cleômenes III (222 a.C.) não foi o último rei Ágida, foi
  Agesipolis III, deposto em 215 a.C. (fonte: Wikipedia, *Agiad dynasty*).
  Faixa dos Reis Eurepôntidas (`PpAtfVwCgww`) estendida de `930-331 a.C.` para
  `900-206 a.C.` — Ágis III (331 a.C.) não foi o último Eurepôntida, a linha
  seguiu até Pelops (r. 210-206 a.C.), último rei de qualquer uma das duas
  dinastias (fonte: Wikipedia). Faixa de Publius Popillius Laenas
  (`ygsc5aDwUL4`) estendida de `132-123 a.C.` para `132-120 a.C.` — o exílio
  começou por lei de 123 a.C., mas ele só retornou em 120 a.C., depois da
  morte de Gaio Graco (fonte: Oxford Classical Dictionary). As duas correções
  de Esparta mudaram a posição das linhas na ordenação; replanilha reordenada
  por inteiro e reconferida pelo `verificar.py`.
- **5 outras datações `chute`/conhecimento geral verificadas por busca
  externa, confirmadas sem divergência**: morte de Cornificius em 42 a.C.
  perto de Utica; morte de Gaius Antonius (irmão de Marco Antônio) em 42 a.C.
  por ordem de Bruto; campanha de Pomptinus contra os Alóbroges concluída até
  fins de 61 a.C.; Batalha de Kissos/Coricos em setembro de 191 a.C.; domínio
  de Dong Zhuo sobre a corte Han (189) e sua morte (22/05/192).
- **Bug do `verificar.py` corrigido**: o resumo impresso em `main()` quebrava
  com um `TypeError` não tratado (`sorted()` comparando `None` com `int`)
  sempre que alguma linha chegasse com `lote` vazio — foi o que aconteceu na
  gravação do lote 48 (corrigido na hora restaurando o backup, sem tocar no
  script). A checagem de `lote` vazio como falha já existia em "campos
  obrigatórios", mas o `print` do resumo rodava antes dela e não tinha
  proteção. Corrigido com uma chave de ordenação que trata `None` à parte
  (`key=lambda kv: (kv[0] is None, kv[0])`); testado numa planilha à parte com
  `lote=None` forçado — agora vira falha reportada normalmente, sem
  traceback. Ver `protocolo.md`, "Armadilhas conhecidas".

### Resolvidas na aprovação dos lotes 40-43

- **7 linhas com `alta` inflada por título/tags sem data própria na
  descrição, rebaixadas para `média`**: `Z24EDQJYzSM` (Ball's Bluff),
  `MIqSe95I_ZI` (Marcus Hordeonius Flaccus), `EPUO0UFquDI` (Lucius Salvius
  Otho Titianus), `SJ2xufBgxrQ` (Lucius Aurunculeius Cotta), `SaJ3udwTByc`
  (Gaius Fabius), `AzwjEsVGKfM` (Peninsula Campaign 1862), `Ky5w29lCPRs`
  (Seven Days Battles) — todas do lote 40. Achado na amostra de 5 linhas da
  parada, depois confirmado por auditoria de todas as `alta` do lote. Critério
  fechado: `alta` exige data numérica na **descrição ou capítulos** do próprio
  vídeo — título e tags não bastam, mesmo quando dão as duas pontas da faixa.
- **`Campanha do Vale` (lote 43) unificado em `Campanha do Vale do Shenandoah`
  (lote 40)** — mesmo teatro de guerra, nomes diferentes por eu não ter
  conferido o vocabulário já usado antes de propor um novo.
- **Região de `w5Z-RHyACec` (Strathclyde) corrigida de `Inglaterra` para
  `Escócia`**, o termo novo criado nesta mesma aprovação.
- **`Dumnónia`, `Reino de Strathclyde` e `Reino da Escócia` fundidos em
  `Reinos pós-romanos da Britânia`**, cada um como subtema — três episódios
  seguidos (XI, XII, XIII) da série "History of Britain" que tinham virado
  três temas-raiz de 1 vídeo cada.
- **`Presidência dos Estados Unidos`, `Diplomacia dos Estados Unidos`,
  `Marinha dos Estados Unidos` e `Política dos Estados Unidos` fundidos em
  `História dos Estados Unidos`**, com subtema por domínio (`Presidência`,
  `Diplomacia`, `Marinha`, `Política`) — quatro temas-raiz de 1 vídeo cada,
  todos biografias de figuras públicas americanas.
- **Subtema `Sula` renomeado para `Crise da República tardia (91-78 a.C.)`**
  nas 15 linhas não travadas do cluster. 4 linhas cujo ano não toca esse
  intervalo (`ftEcm59TlEU` 95 a.C., `wY-f-T_9AVc` 92 a.C., `qCo97YzH2L0` 118
  a.C., `j1pyw97miC4` 114 a.C.) foram tiradas do subtema — o nome com faixa
  numérica no meio ficaria contradizendo o próprio ano da linha. As 3 linhas
  travadas de antes desta rodada não puderam ser renomeadas — ver
  "Sobreposições ainda por resolver".
- **Critério fechado para `Aleatório` vs. histórico quando a descrição tem tom
  de humor/meme** — ver a seção `Aleatório`, acima. Aplicado a `Chuck Norris`
  (`AZtXSl0KoDY`) e `Herman Cain` (`nzEg909Ez4A`): os dois ficam como
  histórico, porque o assunto central de cada um é fato verificável.
- **Fact-check por amostra, 5 datações de risco confirmadas sem divergência**:
  unificação da Escócia por Kenneth MacAlpin (843), morte de Gan Ning
  (215-220, faixa cobre a incerteza das fontes), execução de Manius Aquillius
  (88 a.C., exata), suicídio de Quintus Lutatius Catulus (87 a.C., exata),
  existência do Reino de Strathclyde (séc. V a 1030, exata).

### Resolvidas na parada dos lotes 38-39

- **Cavaleiros Hospitalários (`VSnt1ATgYRo`, lote 38) teve o início corrigido
  de 1080 para 1048**, após fact-check mostrar que o hospício de mercadores de
  Amalfi em Jerusalém — origem da ordem — é de ~1048, não da época da Primeira
  Cruzada como eu tinha estimado (fonte: Wikipedia, "Pie postulatio
  voluntatis"). O reconhecimento papal formal de 1113 segue dentro da faixa.
- **5 de 6 datações `chute`/conhecimento geral verificadas por busca externa,
  confirmadas sem divergência** (Hashashins/Alamute 1090-1256, Malik Ambar
  1548-1626, Guerra das Rosas 1455-1487, Etruscos 900 a.C.-27 a.C.,
  Jardine-Matheson/Guerras do Ópio 1832-1860); a 6ª (Cavaleiros Hospitalários)
  foi corrigida, ver acima.
- **Confirmado que `Mercenários Suíços` (novo) não duplica `Mercenários`** (1
  vídeo já existente, `n7JYdhtR5Hg`): o vídeo antigo é sobre mercenários
  medievais em geral (1200-1300), não especificamente suíços — o tema novo
  estava correto.
- **Suspeita de anomalia no `coletar.py` descartada.** Na parada, registrei que
  a linha "Wars of Roses" (`Do7XBxUVJsE`, lote 39) parecia estar sem a linha
  `datas citadas` no `lote-39.md`. Reconferindo o arquivo diretamente, a linha
  estava lá desde o início (`datas citadas: (nenhuma encontrada — classificar
  pelo assunto)`) — foi erro de leitura, não um bug do script. Não há correção
  a fazer.
- **11 temas-raiz novos e 6 subtemas novos** propostos nos lotes 38-39,
  incorporados à Lista C acima.

### Resolvidas na parada dos lotes 34-37

- **Núbia (`jKIoLwKYpuY`, lote 34) teve o início corrigido de 2500 a.C. para
  2400 a.C.**, após fact-check mostrar que a cultura de Kerma começou por volta
  de 2400 a.C., não 2500 a.C. (fontes: Wikipedia, UEN Pressbooks World History).
  O fim (1500, queda dos reinos cristãos núbios) já estava correto — Alodia
  caiu em 1504, confirmado na mesma checagem.
- **6 datações `chute`/conhecimento geral verificadas por busca externa, 5
  confirmadas sem divergência** (Reino do Bósporo 438 a.C.-370, Império
  Gaznávida 977-1186, Cem Sultan 1481-1495, Koxinga 1624-1662, Tríades
  Chinesas/Tiandihui ~1644-1760) e 1 corrigida (Núbia, ver acima).
- **19 temas-raiz novos e 12 subtemas novos** propostos nos lotes 34-37,
  incorporados à Lista C acima. Destaque para `Rus de Kiev` (6 vídeos
  acumulados sem nenhum subtema — candidato a subdivisão numa parada futura) e
  `Máfia` (ganhou estrutura de subtemas — `Máfia Americana`, `Tríades
  Chinesas` — ao lado da linha original sem subtema, provavelmente a máfia
  siciliana).
- **`Reino Normando da Sicília` reaproveitado para eventos pré-Reino** —
  Dirráquio 1081 e o saque de Roma 1084 (lote 37), que antecedem a fundação
  formal do Reino (1130), foram classificados no mesmo tema pela regra
  "episódio de origem fica com o tema que origina" (mesmo precedente da queda
  de Edessa/Segunda Cruzada). Registrado aqui como aplicação nova da regra,
  não como sobreposição a resolver.

### Resolvidas na parada dos lotes 26-29

- **Manzikert (`JkyYjpYLORI`, lote 29) corrigido de `Cruzadas > Primeira
  Cruzada` / `Oriente Médio` para `Império Bizantino` (sem subtema) /
  `Turquia`.** O título do vídeo usa o nome da série do canal ("First Crusade:
  Battle of Manzikert 1071"), mas a Batalha de Manzikert (1071) antecede a
  Primeira Cruzada (1095) em 24 anos e é história bizantina, não das Cruzadas
  — o canal usa "First Crusade" como rótulo de temporada para todo o contexto
  bizantino/seljúcida que antecede a cruzada em si, não como classificação
  histórica. Mesmo padrão do Prelúdio nº1 da Frente Oriental (Segunda Guerra
  Mundial), que foi classificado pelo conteúdo (Revolução Russa), não pelo
  rótulo "Eastern Front Week-by-Week". As outras linhas do sub-arco "Cruzadas
  > Primeira Cruzada" catalogadas nos lotes 26-29 (ascensão de Aleixo Comneno,
  partilha do império seljúcida, apelo de Urbano II, Cruzada Popular/Civetot)
  não foram reabertas — tratam de fato do prelúdio direto da cruzada
  (1081-1096), diferente de Manzikert, que é 1071.
- **Região `Oceano Índico` renomeada para `Índico`** para bater com o padrão
  enxuto das outras bacias oceânicas da Lista B (`Atlântico`, `Pacífico`,
  `Ártico`). Afeta 1 linha (`E75hxwGbFHE`).
- **Duas regras de fronteira fechadas**: "episódio de origem fica com o tema
  que origina" e "pessoa só vira tema-raiz com 3+ vídeos" — ver "Decisões
  fechadas" acima.
- **8 datações `chute`/conhecimento geral verificadas por busca externa,
  8 confirmadas sem divergência** (Mansa Musa 1312-1337, Sultanato das
  Mulheres 1533-1656, Primeira Fitna/correção Uthman×Umar 656-661, queda do
  Ilcanato 1335-1353, fim do jugo tártaro-mongol na Rússia 1480, concessão
  Welser na Venezuela 1528-1546, queda da dinastia Yuan 1351-1368, partilha do
  império seljúcida 1092-1107).

### Resolvidas na parada dos lotes 22-25

- **Reino da Armênia (`faQsYjxtJRU`, lote 22) teve o início corrigido de 190
  a.C. para 321 a.C.**, após fact-check mostrar que 190 a.C. é só o começo da
  dinastia Artáxida (a fase "entre Roma e Pártia" que dá título ao vídeo), não
  do Reino da Armênia como um todo, que começa com os Orôntidas em 321 a.C.
  (fonte: Wikipedia, Artaxiad dynasty).
- **Wakō (`ptixgsjGxqg`, lote 24) teve o início corrigido de 1300 para 1200**,
  após fact-check confirmar que a pirataria Wakō foi ativa do século XIII ao
  XVI (dois picos, XIV e XVI), não só a partir do XIV.

### Resolvidas na parada dos lotes 18-21

- **Sobreposição de faixas entre dois vídeos sobre a Campanha de Guadalcanal.**
  `FI4eNk69E8Q` ("Guadalcanal Campaign FULL DOCUMENTARY", lote 18) tinha
  `Ano = '1942'` (ago-nov, por capítulos truncados no limite de 20 do
  `coletar.py`) apesar do título dizer "FULL". `D2Jw_AjaF94` ("End of the
  Guadalcanal Campaign", lote 20) cobre o desfecho real (Operação Ke, jan-fev
  de 1943) que ficou de fora do primeiro vídeo. As duas faixas não se
  sobrepõem numericamente (1942 x 1943), mas o título "FULL" do primeiro
  vídeo é enganoso sem a segunda linha — resolvido com notas cruzadas nos dois
  lados, deixando explícito que a causa foi o limite de captura de capítulos,
  não erro de leitura de evidência. Ver "Armadilhas conhecidas" no
  `protocolo.md`.
- **Reconquista Bizantina (`cpLicb2t7Mw`, lote 21) teve o início corrigido de
  950 para 960**, após fact-check na parada confirmar que as campanhas de
  Nikephoros II Phokas contra Creta começaram em 960-961, ainda como general
  (fonte: Wikipedia). O fim (1025, morte de Basílio II) já estava correto.
- **Genocídio Circassiano (`WFSDbHppDKg`, lote 19)** ganhou nota explicando
  que a faixa catalogada (1763-1864) cobre a guerra de conquista russa do
  Cáucaso (título do vídeo), não a limpeza étnica completa, que seguiu até
  1878 segundo o fact-check da parada.
- **Descrição reciclada nem sempre engana — contraexemplo confirmado.** Ao
  contrário da maioria dos casos documentados (Sherman/Vicksburg, "Bakhmut"),
  em pelo menos 2 vídeos dos lotes 20-21 (`bIO66-ZKNhQ` "Ottoman Expansion in
  Anatolia" e `qBA-jdWQGJs` "Maritsa 1371") a recapitulação da série batia
  exatamente com o conteúdo do próprio episódio, porque o título e a descrição
  descreviam o mesmo evento sem ambiguidade. A regra "capítulos/título ganham
  de descrição reciclada" continua valendo, mas o motivo é checar se a
  descrição descreve ESTE episódio ou anuncia episódios futuros/passados —
  não presumir que toda recapitulação é lixo.

### Resolvidas na parada dos lotes 14-17

- **Duas faixas fechadas sobre evidência truncada, corrigidas antes de travar.**
  `4bEGiozqiv8` (300k Russian Casualties) tinha `Ano = '2023 - 2024'`; a
  descrição diz explicitamente "we conclude the events of 2023" e nada no
  vídeo evidencia 2024 — só a data de publicação (14/01/2024). Estreitado para
  `2023`. `Jr8EGJwDCk8` (Full History of the Peloponnesian War) tinha
  `Ano = '431 a.C. - 404 a.C.'`; o vídeo tem quase 3h mas o `coletar.py` só
  captura até 20 capítulos, e os capturados param em 411 a.C. — os ~49 min
  finais (prováveis 411-404 a.C., o fim real da guerra) não têm evidência
  nenhuma. Estreitado para `431 a.C. - 411 a.C.`, o que os capítulos cobrem.
  Ver "Armadilhas conhecidas" no `protocolo.md`.
- **`Segunda Cruzada` nem sempre é a Segunda Cruzada histórica.** Confirmado
  ao classificar `Ager Sanguinis 1119` (lote 14): o subtema `Segunda Cruzada`
  já vinha sendo usado desde o lote 13 para vídeos de 1119-1149, cobrindo a
  "segunda temporada" da série de Cruzadas do canal (história dos Estados
  Cruzados após a Primeira Cruzada) — não a Segunda Cruzada histórica
  (1147-1149). O canal identifica isso na própria descrição de cada vídeo
  ("our series on the Second Crusade"). Mantido por ser o padrão já
  aprovado; documentado como armadilha de nomenclatura no `protocolo.md`.
- **`Guerras da Chechênia`** ganhou o padrão tema-pai/subtema (ver
  "Sobreposições ainda por resolver" acima — parcialmente resolvido, falta
  a linha travada do lote 13).

### Resolvidas na parada dos lotes 10-13

- **Trio romano (`Império Romano` / `República Romana` / `Queda do Império
  Romano`)** — aberto desde o lote 2, resolvido agora com uma fronteira fixa:
  ver "Decisões fechadas".
- **`Guerras Árabe-Cazares` virou subtema de `Império Cazar`** (3 linhas,
  lotes 10-12): duas raízes para o mesmo assunto (o Canato Cazar e as guerras
  árabe-cazares) viraram uma raiz com subtema.
- **`k36ejxp4jNk` (Was Sparta Really Different?, lote 4)** tinha `Tema =
  'Período homérico'` — um rótulo de Século/Período usado por engano como
  Tema. Corrigido para `Esparta`, unificando com a linha do lote 10 (Fall of
  Sparta). Correção humana, linha travada.
- **Região `Iêmen` criada** para o Reino Himiarita e a História do Iêmen, que
  antes caíam em `Oriente Médio` por aproximação. `Iraque` e `Jordânia`/
  `Arábia` continuam adiados até a segunda ocorrência de cada um.

### Resolvidas na parada dos lotes 4-7

- **`Segunda Guerra Mundial` ganhou `Prelúdio`** (9 linhas): separa contexto
  entreguerras dos episódios de combate. `Primeira Guerra Mundial` também usa,
  para o prelúdio nº1, que trata da Revolução Russa.
- **Teatros de guerra como subtema** virou padrão em quatro temas:
  2ª GM, 1ª GM, Guerra Civil Americana e Cruzadas.
- **`América do Norte`** entrou na Lista B. O gatilho foi um erro real: os povos
  do Noroeste do Pacífico estavam em `Estados Unidos`, mas a proibição do potlatch
  que o vídeo narra é lei canadense.
- **`Áustria`** entrou na Lista B, para os Habsburgos.

## Lista E — Eras (camada de exibição)

Usada pela `playlist-historia-v3.xlsx`. O vídeo entra na era em que **começa**,
não no ponto médio: Susa (4200 a.C. - 2026) é material da Antiguidade remota,
porque é lá que o assunto nasce. Definida em `ERAS`, no `ordenar.py`.

| Era | Faixa pelo ano de início |
|---|---|
| Antiguidade remota | até 1100 a.C. |
| Idade do Ferro | 1100 a.C. - 500 a.C. |
| Antiguidade Clássica | 500 a.C. - 500 d.C. |
| Idade Média | 500 - 1500 |
| Era Moderna | 1500 - 1800 |
| Era Contemporânea | 1800 - hoje |

**A virada está em 500 a.C.** Até ali a ordem agrupa por civilização; dali em
diante é cronologia única, com Roma, Pérsia e China intercaladas por data. O
corte saiu de medição, não de gosto: por século de início, a mediana da largura
de faixa é de 144 a 2.784 anos antes de 600 a.C., com menos de 15% dos vídeos
em faixa de até 25 anos; em 500 a.C. a mediana cai para 79 anos e 35% já são
eventos; em 300 a.C. a mediana é 4 anos e 71% são eventos. Antes da virada não
há o que intercalar, porque não há data. Limiar em `VIRADA`.

## Lista F — Tipo (camada de exibição)

Três valores, que decidem a posição do vídeo DENTRO do bloco:

| Tipo | O que é | Onde entra |
|---|---|---|
| `Panorama` | apresenta uma civilização, um período ou um assunto | abre o bloco, antes do primeiro evento que cobre |
| `Evento` | um fato ou período curto (faixa de até 60 anos) | no meio, em ordem cronológica |
| `Temático` | cultura, cidade, legado, religião, filosofia — atravessa períodos | fecha o bloco, depois do último evento que cobre |

Exemplo: "Short History of Ancient Egypt" antes das dinastias; as dinastias em
ordem; Tebas, Núbia, cotidiano e religião depois. Derivado por regra em
`tipo_de()`, não escrito à mão — e **é a coluna de maior risco do modelo**,
porque as 5.567 linhas nunca foram classificadas por tipo por ninguém.

## Lista G — Regiões históricas (camada de exibição)

Região **histórica**, não país atual: `Mesopotâmia`, `Canaã`, `Anatólia`,
`Magna Grécia`, `Frância`, `Britânia`, `Rus`, `Estepe`, `Mesoamérica` — não
Iraque, Israel, Turquia, França. É a unidade de agrupamento antes da virada: é
por ela que os 27 vídeos de Mesopotâmia Antiga ficam juntos, em vez de
aparecerem nos 16 trechos separados que a ordem por `ano_inicio` produzia.

A região sai do **tema** (a civilização manda), com a região da v2 como ponte
quando o tema não está na tabela. Tabelas em `REGIAO_POR_TEMA` e
`PONTE_REGIAO`, no `ordenar.py`.

**A sequência das regiões dentro de cada era é dado, não dedução.** Nada nas
colunas da planilha diz que Mesopotâmia vem antes de Irã, que vem antes de
Egito — é uma escolha editorial de passeio geográfico, e está em `SEQUENCIA`.
Sem ela a ordem não é reproduzível por script. Vale só antes da virada; depois,
quem ordena é a data.

Decisões de vocabulário tomadas ao montar a Lista G, resolvendo inconsistências
da planilha manual:

- `Turquia` → **Anatólia** na Antiguidade (a planilha manual tinha as duas).
- `América Central`/`Américas` → **Mesoamérica** para olmecas, zapotecas,
  maias, astecas (os olmecas estavam em duas regiões diferentes).
- Filosofia grega → **Grécia**, mesmo com o filósofo nascido em Mileto: o tema
  manda, não o lugar de nascimento. Sem isso os pré-socráticos caíam na
  Anatólia e partiam o bloco grego em dois.
- Religião e demonologia do Levante → **Canaã**, não Mesopotâmia.

## Regras de normalização (Python, sem IA)

1. Remover espaços no início e no fim de todo campo.
2. `1942.0` → `1942` (resíduo do Excel).
3. Unificar travessões: `–` e `—` viram `-`.
4. Aceitar `a.C`, `a.C.`, `BC`, `d.C`, `AD` como marcadores de era.
5. `*` significa "não se aplica" e deixa `ano_inicio`/`ano_fim` vazios.
6. `1480s` → 1480–1489 (década).

O parser foi testado nos 93 formatos de data da planilha original e converteu
148 de 155 sem falha. Os 7 restantes eram linhas com `*`.

---

## Decisões fechadas

**Fronteira `Revolução Francesa` / `Napoleão Bonaparte` (parada dos lotes
125-128).** O Golpe de Brumário (nov/1799) marca o fim convencional da
Revolução Francesa na historiografia padrão. Episódios sobre o Consulado e o
Império (1799 em diante) vão para o tema já existente `Napoleão Bonaparte`,
não para `Revolução Francesa` — mesmo quando vêm da mesma série/canal que
cobriu a Revolução inteira. Mesmo princípio da "Fronteira do trio romano"
abaixo: um corte cronológico fixo definido por convenção historiográfica, não
pela série do canal.

**Fronteira do trio romano (parada dos lotes 10-13).** `República Romana` vale
até 27 a.C.; `Império Romano` vale de 27 a.C. em diante; `Queda do Império
Romano` é só para vídeos sobre o colapso em si (não qualquer vídeo tardio sobre
Roma). Fecha a sobreposição aberta desde o lote 2. Regra vale para classificação
futura — linhas antigas não foram reclassificadas retroativamente.

**Episódio de origem fica com o tema que origina (parada dos lotes 26-29).**
Quando um vídeo narra o evento fundador/gatilho de um subtema, ele entra nesse
subtema mesmo que cronologicamente venha antes do nome do subtema "começar" no
sentido estrito. Precedente original: a queda de Edessa (1144) abre o subtema
`Segunda Cruzada`, mesmo sendo o estopim que antecede a cruzada propriamente
dita. Confirmado de novo com `jfBsb_-h-_M` ("What Happened In Rome After
Caesar's Assassination", 44 a.C.): fica em `Segundo Triunvirato` (sob
`República Romana`), mesmo o triunvirato só se formando em nov/43 a.C. — o
vídeo é o episódio de abertura dessa mesma série narrativa ("Post-Caesar Civil
Wars"), não um evento solto. Regra geral: o critério é a série/arco narrativo
do canal, não um corte cronológico rígido no nome do subtema.

**Pessoa só vira tema-raiz com 3 ou mais vídeos no catálogo (parada dos lotes
26-29).** Abaixo disso, entra como subtema do contexto histórico em que a
pessoa atua (ex.: um viajante medieval isolado vira subtema de `Expansão
islâmica`/`Império Mongol`/etc., não tema-raiz próprio). Motivo: o cluster de
temas-raiz biográficos de 1 vídeo só (`Ibn Fadlan`, `Mansa Musa`, `Johannes
Schiltberger`) estava crescendo sem necessidade — um tema-raiz para uma única
linha é ruído na Lista C. `Napoleão Bonaparte` (2 vídeos) também fica abaixo do
piso por enquanto. **Não reclassificar os temas biográficos já existentes
retroativamente** — a regra vale só para classificação futura; ver
"Sobreposições ainda por resolver" abaixo.

**Subtema em `Historiografia` só nasce nomeado com 3 ou mais vídeos do mesmo
assunto (parada dos lotes 48-51).** Abaixo disso, a linha entra sem subtema
(célula vazia), com uma nota explicando do que se trata — para ficar
reconhecível se aparecer uma segunda ou terceira ocorrência do mesmo assunto
no futuro. Mesmo raciocínio da regra acima (pessoa só vira tema-raiz com 3+
vídeos): `Historiografia` estava acumulando um subtema novo por resenha ou
ensaio atemporal — `Datação da Esfinge`, `Hipótese de Tartária`, `Hipótese do
Tempo Fantasma`, `Mulan`, `Taking Out the Trash`, `Guerra de Troia`, `Mos
Maiorum`, `Idade das Trevas`, `Lenda de Alexandre`, `Historiadores gregos`,
`Carreira acadêmica` — a maioria com 1 vídeo só, ruído crescente na Lista C.
**Não reclassificar esses subtemas já existentes e aprovados em paradas
anteriores** — a regra vale só para classificação futura. Aplicada nesta
mesma parada a 5 subtemas novos que caíam abaixo do piso: `Ancient Apocalypse
(Graham Hancock)`, `Dinheiro na Política`, `Escravidão: Antiga e Moderna`,
`F-Tier Tournament` e `G.P. Baker` — todos as 5 linhas voltaram para sem
subtema. `Edward Gibbon` (5 vídeos) e `Datação da Esfinge` (2, abaixo do piso
mas já existente antes da regra) não foram tocados.

**Idades Médias → séculos.** De 500 d.C. em diante a escada usa só séculos.
`Early / High / Late Middle Ages` foram aposentados.

**Vídeos sem ano.** A IA escolhe o período da Lista A; a linha recebe
`confianca = chute` e `status = revisar`.

**`NN00s`.** Década por padrão (`800s` → 800–809), sempre com `revisar`.

**Shorts não entram.** Mínimo de 181 segundos.

**Exclusivos de membros não entram.** Filtrados pelo título no `coletar.py`.

**Extras — teste apertado a partir da parada dos lotes 30-33.** Entra com
`Século/Período = Extra`, anos vazios, `confianca = n/a`, `travado = sim`. Vale
por tema e subtema. Mas **"panorama" não é mais motivo para Extra**: faixa larga
tem lugar na linha do tempo, com o rótulo `Panorama (X - Y)`. Só há dois casos
legítimos:

- **Recepção** — o assunto é o artefato moderno ou o método, não o passado:
  precisão histórica de filme/série/jogo, teoria conspiratória, guia de como
  estudar história. Ex.: `Is Ridley Scott's Napoleon Historically Accurate?`,
  `What is the Truth about Tartaria`.
- **Atemporal** — atravessa milênios sem recorte datável: família linguística,
  miscelânea de exemplos soltos. Ex.: `Evolution of the Indo-European
  Languages`, `The Whale Which Annoyed Justinian and Other Historical Animals`.

O teste prático: **o vídeo tem começo e fim no tempo, mesmo que distantes?** Se
tem, não é Extra — é `Panorama`. Se o vídeo é sobre como falamos do passado
hoje, aí sim é Extra.

**`Aleatório` — não é história (lote 40, canal Thersites the Historian).** Mesma
forma do Extra: anos vazios, `confianca = n/a`, `status = ok`, `travado = sim`,
ordena no fim. A diferença é de assunto, não de datação:

- **`Extra`** — *é* história, mas sem período fixável.
- **`Aleatório`** — **não é história.** Mundo ficcional inventado, cultura de
  internet, assunto que o canal publicou e que o catálogo registra por
  completude. Ex.: `Targaryen Rulers of Westeros` (Game of Thrones),
  `Kenneth D. Pinyan a.k.a. Mr. Hands`.

**Aleatório não recebe anos nem quando existe uma data.** O vídeo do Mr. Hands
traz "1960-2005" no título e mesmo assim fica sem faixa: a linha do tempo do
catálogo significa "o período que o vídeo trata", e esse vídeo não trata de
período histórico. Deixar a data entrar colocaria na linha do tempo algo que
não é história.

Cuidado para não confundir com dois vizinhos que **não** são `Aleatório`:
análise de artefato pop como documento do seu tempo (`G.I. Joe: 1980's American
Jingoism` → `História na cultura popular > Televisão`, anos 1980) e história de
domínios não militares (`History of Video Games` → tema próprio, 1997-1998).
Os dois têm contexto histórico datável e entram na linha do tempo normalmente.

**Tom de humor/meme na descrição não decide sozinho — o teste é o assunto
central (parada dos lotes 40-43).** Vídeos biográficos do canal às vezes
narram uma vida real com tom de piada (`Chuck Norris, Martial Arts Champion
and "Actor", 1940-2026` referencia "Chuck Norris Facts"; `Herman Cain, Pizza
Executive and Presidential Candidate, 1945-2020` diz que o vídeo vai "relive
the memes"). Isso não basta para virar `Aleatório`. O critério:

- **Histórico** se o assunto central é fato verificável — carreira, atuação
  pública, evento real — ainda que contado com humor. Chuck Norris (ator,
  lutador, ativista político real) e Herman Cain (candidato presidencial real
  em 2011, influência real sobre a estratégia de Trump) ficam aqui, mesmo com
  a descrição de tom cômico.
- **Aleatório** só quando o assunto em si é ficção (`Targaryen Rulers of
  Westeros`) ou puro humor sem fato de fundo (o meme, não a pessoa/evento por
  trás dele — nenhum caso do catálogo até agora se encaixa só nisso; `Mr.
  Hands` é `Aleatório` porque o assunto é um caso de crime tratado como meme,
  não porque tenha piada).

Não reabrir Chuck Norris (`AZtXSl0KoDY`) nem Herman Cain (`nzEg909Ez4A`) por
causa do tom da descrição — já decidido por este critério.

**Sem transcrições.** Só a API oficial. Evidência = título, capítulos, descrição
e tags.

**Tags não valem mais que capítulos.** Canais reciclam o bloco de tags entre
episódios da mesma série. Quando tags e capítulos discordam, valem os capítulos.

**`Comentário Político Contemporâneo` (Aleatório) vs. `História dos Estados
Unidos > Política` (histórico) — critério fechado na aprovação dos lotes
60-63, documentando uma distinção que já vinha sendo aplicada desde o lote 59
sem estar escrita aqui.** Os dois tratam de conteúdo político dos EUA
contemporâneo ao canal, mas a linha do tempo só aceita o segundo:

- **`Política`** (histórico, entra na linha do tempo) — o vídeo trata de um
  **pleito real e datado**: debate, caucus, previsão de resultado de eleição,
  ou perfil de um candidato dentro do ciclo eleitoral (`Candidatos
  Derrotados`). Mesmo quando o vídeo é especulativo ("Predictions and
  Updates"), o pleito em si é um evento com data no calendário.
- **`Comentário Político Contemporâneo`** (Aleatório, não é história) — ensaio
  ou especulação política **sem estar ancorado a um evento datado
  específico**: análise de estratégia partidária de longo prazo, comparação
  histórica usada como argumento retórico sobre a corrida atual (ex.: "The
  McGovern Myth", comparando 1972 a 2020), ou "musings" gerais sobre o estado
  da política americana.

O teste prático: **o vídeo é sobre um pleito específico com data, ou é um
argumento/opinião que usa a política como pano de fundo?** Se tem uma data de
votação ou debate por trás, é `Política`; se é ensaio/especulação atemporal
dentro do ciclo, é `Comentário Político Contemporâneo`.

---

## Estado atual (17/11/2026)

5567 linhas, ordenadas de 20000 a.C. a 2026.

| | |
|---|---|
| canais | `Kings and Generals` 1042 (lotes 0-76, encerrado) · `Thersites the Historian` 689 (lotes 40-75, encerrado) · `Ancient Americas` 48 (lotes 77-78, encerrado) · `Historia Civilis` 79 (lotes 79-82, encerrado) · `Cambrian Chronicles` 38 (lotes 83-84, encerrado) · `The History of Rome (Mike Duncan)` 36 (lotes 85-86, encerrado — playlist explícita, não canal) · `The History of Byzantium Podcast` 394 (lotes 87-102, encerrado — esgotou a coleta no lote 102) · `SandRhoman History` 153 (lotes 103-109, encerrado — esgotou a coleta no lote 109) · `The Shogunate` 285 (lotes 110-121, encerrado — esgotou a coleta no lote 121, confirmado por uma coleta seguinte com 0 vídeos novos em 304 percorridos) · `The Histories` 21 (lote 122, encerrado — canal só tem 21 vídeos longos publicados, todos já coletados; uma segunda coleta confirmou 0 novos) · `GatesOfKilikien` 29 (lotes 123-124, encerrado — canal esgotado, confirmado por uma coleta seguinte com 0 vídeos novos nos mesmos 29 percorridos) · `Revolutions (Mike Duncan)` 350 (lotes 125-138, encerrado — playlist explícita, não canal, mesmo padrão do History of Rome; canal esgotado, confirmado por duas coletas seguidas com 0 vídeos novos nos mesmos 350 percorridos) · `Magistra Vitae` 41 (lotes 139-140 e 231, encerrado — canal só tinha 46 vídeos no total, esgotado; história romana/grega/cartaginesa pré-imperial; lote 231 é uma revisita de 1 vídeo, publicado em 10/08/2026, aprovada e travada no mesmo dia) · `Ryan M Reeves` 195 (lotes 141-148, encerrado — canal esgotado, confirmado por uma coleta seguinte com 0 vídeos novos em 210 percorridos) · `HistoryMarche` 245 (lotes 149-158, encerrado — esgotou a coleta, confirmado por uma coleta seguinte com 0 vídeos novos em 373 percorridos; o lote 158 já tinha vindo como mini-lote de 20, sinal de esgotamento próximo) · `History with Cy` 225 (lotes 159-167, encerrado — esgotou a coleta, 0 vídeos novos em 255 percorridos após o lote 167; primeiro canal do catálogo dedicado ao Antigo Oriente Próximo/Egito pré-clássico em profundidade) · `Epic History` 96 (lotes 168-171, encerrado — 0 vídeos novos em 353 percorridos após o lote 171; canal generalista de documentários narrados sobre Guerras Napoleônicas, Alexandre o Grande, Belisário/Justiniano, Cruzadas, Primeira Guerra Mundial, História da Rússia, Programa Apollo e diversos temas avulsos) · `Invicta` 300 (lotes 172-183, encerrado em 08/08/2026 por decisão humana, NÃO por esgotamento — ver `canais.json` — canal de documentários em 3D/reconstruções ("True Size of..."), séries "Units of History" e "How They Did It", Warhammer 40k/Star Wars/Duna/LOTR como ruído de ficção recorrente, Terceira Guerra Púnica, Guerras Greco-Púnicas na Sicília, Guerra Jugurtina, Guerras Germânicas de Roma (Avenging Varus), Harald Hardrada, Cruzadas, Império do Mali, Guerra de Inverno finlandesa e diversos temas avulsos; três ciclos aprovados, 172-175, 176-179 e 180-183, todos em 08/08/2026) · `History of Philosophy Without Any Gaps Podcast` 766 (lotes 184-214, `encerrado` em 09/08/2026 — podcast de Peter Adamson, primeiro canal de filosofia do catálogo. **A série numerada principal, HoP, está esgotada**: o lote 214 (mini-lote de 16 vídeos) terminou no próprio `HoP 001 - Thales`, o primeiro episódio do podcast inteiro, e duas coletas seguintes confirmaram 0 vídeos novos nos mesmos 768 percorridos. A coleta reversa cobriu o núcleo clássico grego inteiro (pré-socráticos, Sócrates, Platão, Aristóteles) e a Antiguidade Tardia pagã (Neoplatonismo, de Plotino a Proclo) antes de esgotar. Nove domínios/séries documentados ao todo: HoP (esgotado), Pré-Socráticos, Platão, Aristóteles, Filosofia Helenística e Romana, Neoplatonismo Tardo-Antigo, Cristianismo Primitivo, Filosofia Islâmica, Filosofia Judaica Medieval, HPI (indiana, coberta por inteiro), HAP (africana, ainda não esgotada) e HPC (chinesa clássica, sem aparecer desde o lote 199 — pode ter conteúdo restante não alcançado). **Decisão do humano em 10/08/2026: encerrado formalmente**, não mantido em pausa — mesmo sendo podcast ativo, "esgotado" aqui significava só "em dia com tudo que existe até agora"; reabrir quando publicar episódio novo é `python coletar.py "@HistoryofPhilosophywithoutGaps"`. Evidência excepcionalmente magra: descrições de 1-2 frases, zero capítulos, a maioria dos vídeos sem nenhuma data própria — a maioria das linhas datadas por busca externa)  · `ESOTERICA` 383 (lotes 215-230, `encerrado` em 10/08/2026 — primeiro canal de esoterismo/ocultismo do catálogo, Dr. Justin Sledge. Cobre magia ritual, hermetismo, gnosticismo, cabala, demonologia, alquimia e a vida de ocultistas/filósofos-limítrofes históricos (Agripa, Paracelso, Trithemius, John Dee, Crowley, Bureus, Newton, Spinoza, Bataille). **Esgotamento real confirmado** no lote 230 (mini-lote de 8), por uma coleta seguinte com 0 vídeos novos em 505 percorridos — **decisão do humano em 10/08/2026: encerrado formalmente** (mesma decisão do HoP), não mantido em pausa. Todos os lotes 215-230 travados, 0 `revisar`) |
| lotes 0-39 | 25 cada, salvo 0 (85) · 1 (7) · 6 (24) |
| lotes 40-75 | 40 (10) · 41 (8) · 42 (15) · 43 (16) · 44 (17) · 45 (13) · 46 (17) · 47 (11) · 48 (13) · 49 (19) · 50 (6) · 51 (10) · 52 (15) · 53 (14) · 54 (10) · 55 (13) · 56 (16) · 57 (25) · 58 (25) · 59 (25) · 60 (25) · 61 (25) · 62 (25) · 63 (25) · 64 (25) · 65 (25) · 66 (25) · 67 (25) · 68 (25) · 69 (25) · 70 (25) · 71 (25) · 72 (25) · 73 (25) · 74 (25) · 75 (16) |
| lotes 76-78 | 76 (1) · 77 (25) · 78 (23) |
| lotes 79-82 | 79 (25) · 80 (25) · 81 (25) · 82 (4) |
| lotes 83-86 | 83 (25) · 84 (13) · 85 (25) · 86 (11) |
| lotes 87-102 | 87 (25) · 88 (25) · 89 (25) · 90 (25) · 91 (25) · 92 (25) · 93 (25) · 94 (25) · 95 (25) · 96 (25) · 97 (25) · 98 (25) · 99 (25) · 100 (25) · 101 (25) · 102 (19) |
| lotes 103-109 | 103 (25) · 104 (25) · 105 (25) · 106 (25) · 107 (25) · 108 (25) · 109 (3) |
| lotes 110-121 | 110 (25) · 111 (25) · 112 (25) · 113 (25) · 114 (25) · 115 (25) · 116 (25) · 117 (25) · 118 (25) · 119 (25) · 120 (25) · 121 (10) |
| lote 122 | 122 (21) |
| lotes 123-124 | 123 (25) · 124 (4) |
| lotes 125-128 | 125 (25) · 126 (25) · 127 (25) · 128 (25) |
| lotes 129-132 | 129 (25) · 130 (25) · 131 (25) · 132 (25) |
| lotes 133-135 | 133 (25) · 134 (25) · 135 (25) |
| lotes 136-138 | 136 (25) · 137 (25) · 138 (25) |
| lotes 139-140 | 139 (25) · 140 (15) |
| lotes 141-144 | 141 (25) · 142 (25) · 143 (25) · 144 (25) |
| lotes 145-148 | 145 (25) · 146 (25) · 147 (25) · 148 (20) |
| lotes 149-152 | 149 (25) · 150 (25) · 151 (25) · 152 (25) |
| lotes 153-156 | 153 (25) · 154 (25) · 155 (25) · 156 (25) |
| lotes 157-158 | 157 (25) · 158 (20) — ciclo fechado por esgotamento, não por 4 lotes |
| lotes 159-162 | 159 (25) · 160 (25) · 161 (25) · 162 (25) — ciclo completo, parada e aprovação em 07/08/2026 |
| lotes 163-166 | 163 (25) · 164 (25) · 165 (25) · 166 (25) — ciclo completo, parada e aprovação em 07/08/2026 |
| lote 167 | 167 (25) — canal esgotado no meio do ciclo (167-170), parada sobre a janela parcial e aprovação em 07/08/2026 |
| lotes 168-171 | 168 (25) · 169 (25) · 170 (25) · 171 (21) — ciclo completo (mini-lote no 171), parada e aprovação em 07/08/2026 |
| lotes 172-175 | 172 (25) · 173 (25) · 174 (25) · 175 (25) — ciclo completo, parada e aprovação em 08/08/2026 |
| lotes 176-179 | 176 (25) · 177 (25) · 178 (25) · 179 (25) — ciclo completo, parada e aprovação em 08/08/2026 |
| lotes 180-183 | 180 (25) · 181 (25) · 182 (25) · 183 (25) — ciclo completo, parada e aprovação em 08/08/2026 |
| lotes 184-187 | 184 (25) · 185 (25) · 186 (25) · 187 (25) — ciclo completo, parada e aprovação em 08/08/2026 |
| lotes 188-191 | 188 (25) · 189 (25) · 190 (25) · 191 (25) — ciclo completo, parada e aprovação em 09/08/2026 |
| lotes 192-195 | 192 (25) · 193 (25) · 194 (25) · 195 (25) — ciclo completo, parada e aprovação em 09/08/2026 |
| lotes 196-199 | 196 (25) · 197 (25) · 198 (25) · 199 (25) — ciclo completo, parada e aprovação em 09/08/2026 |
| lotes 200-204 | 200 (25) · 201 (25) · 202 (25) · 203 (25) · 204 (25) — cinco lotes (não quatro: a parada só rodou depois do 204), parada e aprovação em 09/08/2026 |
| lotes 205-208 | 205 (25) · 206 (25) · 207 (25) · 208 (25) — ciclo completo, parada e aprovação em 09/08/2026 |
| lotes 209-213 | 209 (25) · 210 (25) · 211 (25) · 212 (25) · 213 (25) — cinco lotes (não quatro: a parada só rodou depois do 213), parada e aprovação em 09/08/2026 |
| lote 214 | 214 (16) — mini-lote de esgotamento (chegou ao HoP 001, o primeiro episódio do podcast), parada e aprovação em 09/08/2026 |
| lote 215 | 215 (25) — primeiro lote do canal ESOTERICA; travado na aprovação de 10/08/2026 junto com o ciclo 220-223 |
| lotes 216-219 | 216 (25) · 217 (25) · 218 (25) · 219 (25) — ciclo completo via `/rodada` (primeira vez que o comando rodou), parada e aprovação em 10/08/2026 |
| lotes 220-223 | 220 (25) · 221 (25) · 222 (25) · 223 (25) — segundo ciclo via `/rodada`, parada conjunta com o lote 215 e aprovação em 10/08/2026 |
| lotes 224-227 | 224 (25) · 225 (25) · 226 (25) · 227 (25) — terceiro ciclo via `/rodada`, parada e aprovação em 10/08/2026 |
| lotes 228-230 | 228 (25) · 229 (25) · 230 (8) — quarto ciclo via `/rodada`, encerrado por esgotamento real (mini-lote de 8 + coleta seguinte confirmando 0 novos), parada e aprovação em 10/08/2026 |
\1
| lotes 232-235 | 232 (25) · 233 (21) · 234 (25) · 235 (5) — reabertura dos canais encerrados (Kings and Generals e Thersites), parada e aprovação em 17/11/2026 |
| lotes 236-239 | 236 (1) · 237 (1) · 238 (3) · 239 (5) — Ancient Americas, Cambrian Chronicles, Byzantium Podcast e SandRhoman — quatro canais em 10 linhas, parada e aprovação em 17/11/2026 |
| lotes 240-243 | 240 (7) · 241 (2) · 242 (1) · 243 (3) — The Shogunate, The Histories, GatesOfKilikien e Magistra Vitae, parada e aprovação em 17/11/2026 |
| lotes 244-247 | 244 (5) · 245 (7) · 246 (9) · 247 (3) — Ryan M Reeves, HistoryMarche, History with Cy e Invicta, parada e aprovação em 17/11/2026 |
| lotes 248-249 | 248 (15) · 249 (14) — History of Philosophy Without Any Gaps e ESOTERICA — encerra a reabertura, parada e aprovação em 17/11/2026 |
| status | 5567 `ok` · 0 `revisar` |
| confiança | 1210 alta · 1713 média · 1792 chute · 852 n/a |
| travadas | 5495 |
| temas-raiz | 525 · regiões: 60 |
| rótulos | 635 `Extra` · 217 `Aleatório` · 633 `Panorama` · 4082 na escada do ponto médio |
| `descartados.txt` | 1540 ids |

**Lotes 216-219 (100 linhas) travados na aprovação de 10/08/2026 — primeiro
ciclo rodado pelo comando `/rodada`, canal ESOTERICA segue `em andamento`,
sem sinal de esgotamento.** Primeira execução do novo comando (criado nesta
mesma sessão): 4 lotes de 25 rodados em sequência sem pausa entre eles,
cada um com seu próprio backup e `verificar.py`, fechando com a parada de
revisão de uma vez só. Conteúdo dominado por três séries em curso do canal
— "Introduction to Merkavah Mysticism" (15 episódios, misticismo judaico
pré-cabalístico), "The Occult Philosophy of Cornelius Agrippa" (8 episódios
cobertos, de 14) e uma sequência avulsa sobre demônios/entidades
(Lilith, Belial, Baal, Moloch, os demônios do Talmud) — mais biografias de
ocultistas e filósofos-limítrofes (Peter of Abano, Aleister Crowley, John
Dee, Immanuel Kant, Arthur Schopenhauer, John Winthrop o Jovem). Introduziu
**9 temas-raiz** (`Vlad III, o Empalador`, `História dos Fantasmas`,
`Aleister Crowley`, `John Dee e a Magia Enocheana`, `Immanuel Kant`,
`Manuscritos do Mar Morto (Qumran)`, `Arthur Schopenhauer`, `Espiritualismo
Moderno`, `As Origens do Gótico (Estética e Horror)`) e cerca de 30
subtemas, a maioria reaproveitando os quatro temas-raiz que o lote 215 já
tinha aberto (`Demonologia Ocidental`, `Hermetismo`, `Filosofia Judaica
Medieval > Misticismo Merkavah`, `Renascimento > Cornélio Agripa`/`Paracelso
e a Alquimia`). Nenhuma região nova. Fact-check da parada verificou 4
datações de maior risco (morte de Peter of Abano, ano do Malleus
Maleficarum usado para calcular a data do Formicarius de Nider, datação do
Códice Maya de México, período de Zósimo de Panópolis) — as 4 bateram.
**1 correção na aprovação**: a linha "Agrippa's Afterlife" (lote 219) tinha
a ponta final da faixa (1700) baseada numa extensão especulativa minha
sobre a recepção rosacruz do século seguinte, sem nenhuma palavra da
evidência sustentando — estreitada para `1535`, a morte de Agripa, o único
ano que a série realmente ancora; lição registrada no `protocolo.md`,
"Armadilhas conhecidas". Pendências de vocabulário deixadas em aberto, não
bloqueantes: `Manuais de Exorcismo e Necromancia (pré-1614)` (Renascimento)
× `Necromancia e Grimórios Medievais` (Escolástica Medieval), mesma família
de assunto em dois temas-raiz diferentes; `Renascimento` como tema-raiz
guarda-chuva já cobre a Europa continental inteira mais as colônias
americanas (Winthrop) — ver `vocabulario-canonico.md`, "Sobreposições ainda
por resolver". Detalhes completos em `canais.json`. O lote 215 (25 linhas)
ficou de fora deste ciclo porque foi classificado antes do `/rodada`
existir — travado na parada seguinte, junto com 220-223 (ver abaixo).

**Lote 215 (25 linhas) + lotes 220-223 (100 linhas) travados na aprovação
de 10/08/2026 — segundo ciclo rodado pelo comando `/rodada`, canal
ESOTERICA segue `em andamento`, sem sinal de esgotamento.** Primeira parada
a reunir um lote "órfão" (215, pendente da rodada anterior) com um ciclo
novo inteiro. Mesmo padrão de conteúdo do ciclo anterior — a série
"Introduction to Merkavah Mysticism" terminou de ser coberta (chegando ao
próprio anúncio do seminário, lote 222), "The Occult Philosophy of
Cornelius Agrippa" foi concluída (14 de 14 episódios, do fim ao início),
mais uma leva grande de textos/figuras avulsas de história da magia,
alquimia e demonologia (Lilith em três episódios diferentes, o Deus Sem
Cabeça/Akephalos, a Chave Menor de Salomão, o Manual Necromântico de
Munique). Introduziu **6 temas-raiz** (`Karl Marx`, `Johannes Bureus e a
Runologia Esotérica`, `Vampiros (Origens Históricas)`, `Yukio Mishima`,
`William Blake`, `Sigmund Freud e a Psicanálise`) e cerca de 35 subtemas,
a maioria reaproveitando temas-raiz já abertos (`Caça às Bruxas` e
`Hermetismo` viraram os maiores ímãs do ciclo, 6 subtemas novos cada).
Nenhuma região nova. Fact-check da parada verificou 4 datações de maior
risco (execução de Cecco d'Ascoli, publicação de "Beyond the Pleasure
Principle" de Freud, De Lamiis et Pythonicis Mulieribus de Molitor, datas
de vida de Plotino) — as 4 bateram (a data exata do dia de Cecco d'Ascoli
tem divergência na própria historiografia acadêmica entre 16/09 e
26/09/1327, mas o ano bate e a evidência do canal usa 26/09). **Nenhuma
correção na aprovação** — a amostra de 5 linhas sorteadas não revelou
erro, só sinalizou uma decisão de base ampla já marcada como frágil na
hora ("A Loucura Divina de Platão e sua Recepção Renascentista", faixa de
quase 2000 anos reconstruída a partir de quatro nomes citados, sem nenhuma
data própria na evidência). Pendências de vocabulário deixadas em aberto,
não bloqueantes: cluster "Nicholas Eymerich" espalhado em 3 subtemas de 2
temas-raiz diferentes (`A Inquisição contra a Alquimia` e `Manuais
Inquisitoriais e a Heresia Mágica`, Hermetismo/Caça às Bruxas, mais `As
Origens da Inquisição Medieval`) — ver `vocabulario-canonico.md`,
"Sobreposições ainda por resolver". Detalhes completos em `canais.json`.

**Lotes 224-227 (100 linhas) travados na aprovação de 10/08/2026 — terceiro
ciclo rodado pelo comando `/rodada`, canal ESOTERICA segue `em andamento`,
sem sinal de esgotamento.** A coleta reversa chegou ao **vídeo de
lançamento do canal** (`Welcome to ESOTERICA`, maio de 2021) no lote 227 —
o canal ainda não esgotou, mas a linha do tempo de publicação já foi
percorrida quase por inteiro. A série "Introduction to Kabbalah and Jewish
Mysticism" (14 episódios) foi coberta do fim ao início nestes quatro
lotes, gerando a maior concentração de subtemas novos sob `Filosofia
Judaica Medieval` de qualquer ciclo do canal até agora (13 subtemas, do
Sabbateanismo à profecia israelita pré-cabalística). `Hermetismo` também
cresceu bastante (7 subtemas: Tábua de Esmeralda, Turba Philosophorum,
Cleópatra a Alquimista, Maria a Judia, Perseguição de Dioclesiano aos
Alquimistas). Introduziu **6 temas-raiz** (`Pânico Satânico`, `Austin
Osman Spare`, `Georges Bataille`, `Anne Conway`, `Isaac Newton`, `Baruch
Spinoza`) e cerca de 40 subtemas. Nenhuma região nova. **Primeiro
`Aleatório` do canal**: uma "descoberta arqueológica" de um fragmento do
Zohar sobre Ester, explicitamente identificada na própria descrição como
piada de 1º de abril de 2022 — não é história, o canal publicou e o
catálogo registra, mas o vídeo não trata de nenhum período real. Fact-check
da parada verificou 4 datações de maior risco (perseguição de Dioclesiano
aos alquimistas, datação de Cleópatra a Alquimista, datação de Maria a
Judia, datas de Isaac o Cego/Azriel de Gerona) — as 4 bateram. **Zero
correções na aprovação** — a amostra de 5 linhas não revelou erro, só
confirmou uma decisão já sinalizada como frágil na hora (faixa de quase
2300 anos da linha sobre o Anjo da Morte, reconstruída a partir de pontos
nomeados sem nenhuma âncora numérica própria). Reaproveitou pela primeira
vez dois temas-raiz herdados de outros canais do catálogo (`Pré-Socráticos`
e `Mitraísmo`), sinal de que o vocabulário acumulado do catálogo inteiro
segue útil mesmo para um canal de assunto bem diferente. Canal com 325
linhas totais (lotes 215-227). Detalhes completos em `canais.json`.

**Lotes 228-230 (58 linhas) travados na aprovação de 10/08/2026 — quarto
ciclo rodado pelo comando `/rodada`, encerrado por esgotamento real, não
por completar 4 lotes.** O lote 230 chegou como mini-lote de 8 vídeos
(sinal clássico de esgotamento) e uma coleta seguinte confirmou 0 vídeos
novos nos mesmos 505 percorridos — o canal está de fato esgotado, chegando
ao início cronológico da própria publicação (março de 2020, incluindo o
vídeo `Introduction to Western Esotericism`). `Hermetismo` foi de longe o
maior ímã do ciclo (12 subtemas novos: Turba Philosophorum, Summa
Perfectionis, Fórmula do Caranguejo/Escorpião, Magia e Doença, Papiros
Mágicos Gregos, O Livro da Composição da Alquimia de 1144, entre outros) —
a série "John Dee - The Monas Hieroglyphica" (3 partes) e a trilogia sobre
absinta também foram fechadas neste ciclo. Introduziu **1 tema-raiz**
(`História da Absinta`) e cerca de 35 subtemas. Nenhuma região nova.
Fact-check verificou 4 datações de maior risco (Summa Perfectionis c.
1310, tradução de Robert de Chester em 1144, Sefer HaRazim séc. III-IV
d.C., Ritual Maqlû) — 3 bateram exatamente; a 4ª (Maqlû, "3000 anos" na
descrição -> c. 1000-900 a.C.) ficou no fim da janela de uso do ritual
segundo a bibliografia mais recente (composição c. 1300-1100 a.C., em uso
"throughout the 1st millennium BC") — divergência normal de datação de um
ritual usado por mais de mil anos, não um erro de classificação. **Zero
correções na aprovação**. Pendência de vocabulário: a linha sobre a
história da absinta (tema-raiz novo) foi montada sem nenhuma âncora
numérica própria — a data explícita do banimento francês (1915) veio de
uma linha-irmã do mesmo lote, não da própria evidência dessa linha. Canal
com 383 linhas totais (lotes 215-230), 0 `revisar`. **Esgotamento real
confirmado, decisão sobre marcar `encerrado` pendente do humano.**
Detalhes completos em `canais.json`.

**Lotes 196-199 (100 linhas) travados na aprovação de 09/08/2026 — quarto
ciclo do canal `History of Philosophy Without Any Gaps Podcast`, sem sinal
de esgotamento.** Duas mudanças de conteúdo grandes neste ciclo. HAP recuou
até perto do **início da própria série**: filosofia no Egito e na
Mesopotâmia antigos, os filósofos etíopes Zera Yacob e Walda Heywat, a
Etiópia antiga (Kebra Nagast), Islã na África Subsaariana (Songhay, Sokoto),
e — no lote 198 — treze episódios seguidos sobre o debate do séc. XX de
como fazer filosofia africana (etnofilosofia de Tempels, crítica de
Hountondji, Filosofia dos Sábios de Odera Oruka), consolidados num único
subtema guarda-chuva. HoP percorreu o Renascimento italiano completo
(Maquiavel, Ficino, Pico, Savonarola, humanistas) até a filosofia bizantina,
que ganhou **três subtemas de recorte cronológico** sob o mesmo tema-raiz
`Império Bizantino`: era do Iconoclasmo (séc. VII-IX), era Comnena (séc.
XI-XIII) e Tardia (séc. XIV-XV, já criada no lote 197). Dois vídeos foram
movidos para temas-raiz já existentes em vez de gerar conteúdo paralelo —
Egito/Mesopotâmia Antiga (`Egito antigo`, `Babilônia Antiga`) e a Revolução
Haitiana (`Revolução Haitiana`) — achado da checagem obrigatória da Lista C
inteira antes de propor termo novo. Nenhum tema-raiz novo, nenhuma região
nova, **42 subtemas novos**. Confiança: **62 `média`**, **26 `chute`** (o
maior número de qualquer lote do canal até agora, concentrado nos episódios
de conceito bizantino/etnofilosófico sem pessoa nomeada), **9 `alta`** e
**3 `n/a`** (dois episódios-marco/meta do HoP e um "Bonus Episode" fora de
história). Fact-check da parada verificou 2 datações de risco (vida de John
Ítalos, morte de Bar Hebraeus) — as 2 bateram. **1 correção na aprovação**:
`HoP 324 - Latin Philosophy in Byzantium` tinha a ponta final da faixa
("1450") baseada numa leitura minha da frase vaga "twilight of empire", não
numa data real — estreitada para `1341-1351`, os sínodos reais da
controvérsia hesicasta citada na própria descrição. Pendências de
vocabulário deixadas em aberto, não bloqueantes: os três recortes
cronológicos de `Filosofia Bizantina` podem se sobrepor nas bordas;
`Etnofilosofia e Debate sobre a Filosofia Africana` é a maior consolidação
de subtema por guarda-chuva até agora, com 6 de 13 linhas `chute` sem
nenhuma âncora própria — ver acima, "Sobreposições ainda por resolver".
Detalhes completos em `canais.json`, campo `observacoes`.

**Lotes 192-195 (100 linhas) travados na aprovação de 09/08/2026 — terceiro
ciclo do canal `History of Philosophy Without Any Gaps Podcast`, sem sinal de
esgotamento.** HoP fechou o finale da série "Renascimento Italiano" (12
vídeos consolidados num único subtema guarda-chuva, em vez de fragmentar por
pessoa — Cardano, Telesio/Campanella, magia e astrologia, Bruno, Galileu,
medicina, Roma, mais o cluster próprio de Maquiavel com 3 episódios) e entrou
na Reforma alemã/suíça (Lutero, Melanchthon, Zwínglio, Calvino, Erasmo, a
Guerra dos Camponeses). HAP consolidou o núcleo de pensadores negros do
final do séc. XIX/virada do XX — Du Bois, Alain Locke, Booker T. Washington,
Marcus Garvey (+ as duas esposas Amy), a Academia Negra Americana, e uma
dúzia de intelectuais pan-africanistas menos conhecidos (Crummell, Blyden,
Horton, Fortune, Firmin, Turner, Cooper, Wells) — mais um desvio geográfico
único, o abolicionismo no Brasil (Luiz Gama, Machado de Assis, Joaquim
Nabuco). Nenhum tema-raiz novo, nenhuma região nova — só reaproveitamento
(`Caribe`, `África Oriental`, `Haiti`) e **61 subtemas novos**, a grande
maioria (43) sob `Filosofia Africana`, que já passa de 90 subtemas desde sua
criação no lote 188. Confiança: **72 `média`** (busca externa), **17
`alta`** (época narrada no corpo da descrição, nunca em título — inclusive
um caso em que a faixa veio do **próprio título** do episódio, "W.E.B. Du
Bois, 1920-1963") e **10 `chute`** (episódios de conceito amplo da série do
Renascimento Italiano sem pensador nomeado). Fact-check da parada verificou
3 datações de risco (invenção da imprensa/Reforma, nascimento de Leonardo
Bruni, fundação/dissolução da Academia Negra Americana) — as 3 bateram.
**1 correção na aprovação**: `HAP 61 - Anna Julia Cooper` tinha a faixa da
vida inteira (1858-1964), mas a evidência aponta para uma obra específica
("A Voice from the South") — estreitada para `1892`, o ano do livro,
seguindo a convenção do `protocolo.md` sobre conteúdo biográfico com obra
identificável. Pendências de vocabulário deixadas em aberto, não
bloqueantes: faixa interna muito variável (1370-1642) dentro do mesmo
subtema `Renascimento Italiano`; `W.E.B. Du Bois` com 4 faixas diferentes em
3 lotes; cluster pan-africanista do séc. XIX com fronteiras temporais
sobrepostas (`Raízes do Nacionalismo Negro` / `Alexander Crummell` /
`Academia Negra Americana`) — ver acima, "Sobreposições ainda por
resolver". Detalhes completos em `canais.json`, campo `observacoes`.

**Lotes 188-191 (100 linhas) travados na aprovação de 09/08/2026 — segundo
ciclo do canal `History of Philosophy Without Any Gaps Podcast`, sem sinal
de esgotamento.** Marco do ciclo: chegada da terceira série do canal, **HAP**
(*History of Africana Philosophy*), que abriu o tema-raiz `Filosofia
Africana` no fim do lote 188 e o encheu de **32 subtemas** em três lotes —
quase um por pessoa ou movimento (Cornel West, Angela Davis, Frantz Fanon,
Nelson Mandela, Amílcar Cabral, Kwame Nkrumah, Steve Biko, Walter Rodney,
Édouard Glissant, Sylvia Wynter, Ngũgĩ wa Thiong'o, Panteras Negras, Poder
Negro, Teoria Racial Crítica, Afrofuturismo, Reggae e Rastafari, entre
outros). As outras duas séries (HoP, humanismo/reforma franco-inglês; HPC,
filosofia chinesa clássica) continuaram no ritmo normal, com destaque para um
arco fechado de 5 episódios sobre Shakespeare e outro sobre ciência inglesa
renascentista (Dee, Gilbert, Fludd). Introduziu **2 regiões novas** (`Caribe`,
`África Oriental`) e **1 tema-raiz novo** (`Filosofia Africana`), além dos 54
subtemas (32 em Filosofia Africana, 17 em Renascimento, 3 em Segunda
Escolástica, 1 em Escolástica Medieval, 1 em Filosofia Moderna — mais 2 em
Reforma Protestante). Confiança seguiu o padrão do primeiro ciclo do canal:
**93% `média`** (datas de vida/evento confirmadas por busca externa, nunca
`alta` — convenção fixada na adoção do canal), só 5 `alta` (todas com
século/década narrado no corpo da própria descrição, nunca em título ou
bloco de relacionados) e 2 `chute`. Fact-check da parada verificou 3 datações
de maior risco (início da carreira de Sun Ra/Afrofuturismo, início da
Escolástica ~1100, declínio do Black Power ~1975) — as 3 bateram, nenhuma
correção necessária. **Nenhuma correção na aprovação** — a parada não achou
erro de fato, só sobreposições de nomenclatura registradas em "Sobreposições
ainda por resolver": `Tolerância Religiosa` duplicado em dois temas-raiz por
época (`Renascimento` × `Filosofia Moderna`); `Feminismo Negro` partido em
dois subtemas por década (anos 1970 × bell hooks/Collins); `Ceticismo
Renascentista` × `Ceticismo Francês` (nomes parecidos, épocas diferentes);
`Filosofia Política Huguenote` × `Rebeliões Huguenotes` (nomes parecidos,
assuntos diferentes); região `Global` na linha de Frantz Fanon, talvez
`Caribe` ou `Norte da África` fosse mais preciso. `Dinastia Zhou > Cem
Escolas do Pensamento` cresceu de 46 para 53 vídeos neste ciclo — pendência
antiga (promover a tema-raiz exige autorização sobre linha travada do Kings
and Generals) que só piora a cada lote da série HPC.

**Lotes 184-187 (100 linhas) travados na aprovação de 08/08/2026 — primeiro
ciclo do canal `History of Philosophy Without Any Gaps Podcast`
(@HistoryofPhilosophywithoutGaps), adotado no lote 184 e o vigésimo primeiro
do catálogo.** Primeiro canal de filosofia, e o de evidência mais magra até
hoje: descrições de 1-2 frases, **zero capítulos em 100 vídeos**, e 24 de 25
vídeos por lote sem nenhum número — contra ~330 palavras por vídeo do
Invicta. Duas séries numeradas intercaladas semana a semana: **HoP** (série
principal, percorrida de trás para frente porque a coleta vai do mais
recente ao mais antigo — chegou na França do século XVII e recuou até o
Renascimento tardio) e **HPC** (filosofia chinesa clássica: daoísmo,
moísmo, confucionismo, legalismo). Perfil de confiança inédito no catálogo:
**zero linhas `Extra`/`Aleatório`** (todo episódio é história de alguma
coisa) e **88 de 100 linhas `média`** — datadas por busca externa, com a
fonte registrada em `notas`, não por evidência do próprio vídeo. Introduziu
**3 temas-raiz novos** (`Filosofia Moderna`, `Segunda Escolástica`,
`Dinastia Qin`) e **14 subtemas**, nenhuma região nova. Duas convenções
foram fixadas com o humano antes do primeiro lote e valem para todo conteúdo
biográfico/conceitual — ver `protocolo.md`, "Conteúdo biográfico/conceitual
sem evento datável": vídeo sobre um pensador usa a **vida inteira** dele
como faixa padrão; vídeo sobre conceito que atravessa séculos fica na
**linha do tempo com faixa ampla**, não vira `Extra`. **3 correções na
aprovação**: faixa da filosofia jesuíta (reprovada no fact-check — Vitoria
era dominicano), faixa do yin-yang (o tema `Dinastia Zhou` contradizia os
anos da linha) e unificação dos dois episódios sobre Elisabeth da Boêmia num
subtema só. Pendência principal, **não resolvida por exigir autorização
sobre linha travada**: `Dinastia Zhou > Cem Escolas do Pensamento` chegou a
46 vídeos misturando cinco escolas filosóficas rivais — ver acima,
"Sobreposições ainda por resolver".

**Lotes 180-183 (100 linhas) travados na aprovação de 08/08/2026 — terceiro
ciclo do canal `Invicta`, sem sinal de esgotamento.** Continuação do mesmo
padrão dos ciclos anteriores, com a maior proporção de conteúdo
`Extra`/`Aleatório` até agora (71% do ciclo `n/a`) — Roma cotidiana (leis,
tribunais, exército, gladiadores, Cartago) sem recorte de evento único, e
levantamentos comparativos cross-era (`Evolução da guerra` ganhou 4 linhas
Extra num ciclo só: PTSD antigo, discursos de batalha, torres de cerco,
táticas antielefante). Conteúdo histórico real cobriu a sequência completa
da campanha de vingança contra Armínio pós-Teutoburgo (9-17 d.C., novo tema
`Guerras Germânicas de Roma`), a Guarda Varegue e a Peste de Justiniano no
Império Bizantino, e episódios avulsos bem documentados historicamente sem
data própria na evidência (galinhas sagradas/Drépano 249 a.C., motim das
legiões de César 47 a.C., Wojtek o urso em Monte Cassino 1944). Introduziu
**2 temas-raiz novos** (`Guerras Germânicas de Roma`, `Cerco de Jerusalém
(70 d.C.)`) e **9 subtemas novos**, nenhuma região nova — busquei cada
termo na Lista C inteira antes de propor, nenhuma duplicata encontrada.
Confiança com a maior proporção `n/a` de qualquer ciclo do canal até agora
(71%), refletindo o volume de `Extra`/`Aleatório`, não datação fraca — das
20 linhas com data para estimar, 17 foram `alta`. Fact-check da parada
verificou 4 datações de risco (Drépano, motim de César, Wojtek, invasão de
Piye) — 3 bateram exatamente, 1 (Piye) ficou 7 anos abaixo do consenso,
dentro de margem normal e já sinalizada `média` na própria linha. **1
correção na aprovação**: região da linha da Peste de Justiniano trocada de
`Mediterrâneo` para `Egito` (mais específica, ancorada na evidência
própria). Pendências de vocabulário deixadas em aberto, não bloqueantes:
colisão de nome "Campanha da Itália" entre `Segunda Guerra Mundial` e
`Napoleão Bonaparte` (assuntos diferentes, mesmo nome-base); `Cerco de
Jerusalém (70 d.C.)` como tema-raiz de 1 vídeo só; divergência entre dois
vídeos da série Avenging Varus sobre se o desfecho foi 16 ou 17 d.C. — ver
acima, "Sobreposições ainda por resolver". Detalhes completos em
`canais.json`, campo `observacoes`.

**Lotes 176-179 (100 linhas) travados na aprovação de 08/08/2026 — segundo
ciclo do canal `Invicta`, sem sinal de esgotamento.** Continuação do mesmo
padrão do primeiro ciclo (documentários "True Size"/"Units of History"/"How
They Did It"), com uma fração grande de conteúdo `Extra`/`Aleatório` — Roma
cotidiana (exército, gladiadores, sociedade, direito) sem recorte de evento
único, e ficção recorrente (Warhammer 40k, Star Wars, Duna, O Senhor dos
Anéis). Conteúdo histórico real cobriu principalmente a série completa das 7
Guerras Greco-Púnicas na Sicília (reaproveitando um tema-raiz de só 1 vídeo do
Kings and Generals, que virou o maior consumidor desse termo), a série da
Guerra Jugurtina (reaproveitando subtema do Thersites the Historian), o
Império Bizantino, o Império Sassânida, a Rus de Kiev e a saga completa de
Harald Hardrada. Introduziu **4 temas-raiz novos**: `Erupção do Vesúvio (79
d.C.)`, `Exploração Antiga`, `Harald Hardrada`, `Meteoros na História` — mais
**10 subtemas novos**, com destaque para dois pares que formam famílias
institucionais dentro de temas já existentes (`Guerras Napoleônicas` ganhou
`Velha Guarda`/`Grande Armée`; `Exploração Antiga`, recém-criado, já nasceu
com 2 subtemas). Nenhuma região nova — antes de propor cada tema-raiz,
busquei o termo (e sinônimos plausíveis) na Lista C inteira, não só no ciclo
em andamento, puxando a lição registrada no `protocolo.md` depois do episódio
`Gladiadores`/`Besteiros Genoveses` do ciclo anterior; a busca não encontrou
nenhuma duplicata desta vez. Confiança mais alta que o ciclo anterior do
mesmo canal (31% alta, 6% média, 8% chute, 55% n/a — o n/a alto reflete o
volume grande de `Extra`/`Aleatório`, não datação fraca: das linhas que
tinham data pra estimar, a maioria foi `alta`, o canal costuma pôr o ano
certo no próprio título quando o vídeo narra um evento). Fact-check da
parada verificou 5 datações de risco (fundação dos Jomsvikings, nascimento
de Olga de Kiev, viagem de Piteas, meteorito em campo de batalha romano na
Terceira Guerra Mitridática, reinado hipotético do "imperador" Sponsian) —
todas bateram com busca externa dentro de margem normal de incerteza
histórica, nenhuma correção de fato necessária. **1 correção na aprovação**:
região da linha de Piteas trocada de `Atlântico` para `Ártico` (termo mais
preciso já existente na Lista B para o destino notável da viagem). Um caso
de "a fonte erra" tratado durante a classificação, não na aprovação:
`Punic Sicilian Wars - The Battle of Himera` (lote 178) tem o título correto
("480 BC") mas a própria descrição escreve "409 BC" para o mesmo evento —
mantida a data do título/fato histórico (480 a.C.), confirmada também pelo
texto do vídeo seguinte da mesma série. Pendências de vocabulário deixadas
em aberto, não bloqueantes: `Harald Hardrada` (tema-raiz) vs. `Era Viking`
(subtema não avaliado como alternativa); `Erupção do Vesúvio (79 d.C.)` como
tema-raiz de 1 vídeo só — ver acima, "Sobreposições ainda por resolver".
Detalhes completos em `canais.json`, campo `observacoes`.

**Lotes 172-175 (100 linhas) travados na aprovação de 08/08/2026 — primeiro
ciclo do canal `Invicta` (@invictahistory), adotado no lote 172.** Canal de
reconstruções militares em 3D ("True Size of...", Unreal Engine 5) e da série
"Units of History", cobrindo majoritariamente história romana (Terceira
Guerra Púnica em série de 5 partes, Segunda Guerra Púnica/Cannae, Exército
Romano — medicina, inteligência, carreira do soldado —, Invasão Romana da
Escócia, relações Roma-Índia), Guerras Médicas (Batalha de Platéia),
Sengoku Jidai (exército, marinha, castelos), Império do Mali, Guerra de
Inverno finlandesa (1939-1940) e Império Sassânida/Daylamitas — com um ruído
recorrente grande de conteúdo não histórico (lore de ficção de Warhammer
40.000, LOTR, Duna; gameplay de Total War/Manor Lords/Tlatoani/Empire of the
Ants) e uma família de resenhas de mídia/entrevistas sobre acurácia histórica
em filmes e séries. Propôs 10 temas-raiz ao longo da classificação, dos
quais **8 sobreviveram** à aprovação (2 eram duplicatas fundidas em temas
já existentes — ver as correções abaixo): `Guerra Romano-Seléucida`,
`Exército Sassânida`, `Império do Mali`, `Guerra de Inverno (1939-1940)`,
`Guerra do Iraque (2003)`, `Sociedade Romana`, `Comércio Romano`,
`Biblioteca de Alexandria` — mais **11 subtemas novos**, com destaque para
uma família de três subtemas institucionais sob `Sengoku Jidai` (`Castelos
do Sengoku Jidai`, `Marinha do Sengoku Jidai`, `Exército do Sengoku Jidai`).
Nenhuma região nova — `Norte da África` (já existente) usada pela primeira
vez para este canal; `Rússia` usada por aproximação para a Finlândia, que
ainda não tem termo próprio na Lista B. Confiança abaixo da média histórica
do catálogo (24% alta, 26% média, 36% chute, 14% n/a — o "n/a" alto reflete
o volume grande de conteúdo `Extra`/`Aleatório` do canal): quando o canal
narra um evento específico, quase sempre põe o ano no próprio título; boa
parte do resto é explicador atemporal (institucional/"how it works") sem
nenhuma data. Fact-check da parada verificou 4 datações de maior risco
(Batalha de Mons Graupius, fundação do Império do Mali/Batalha de Kirina,
fundação e queda do Império Sassânida, cronologia dos 5 episódios da
Terceira Guerra Púnica) — todas bateram com busca externa, nenhuma correção
de fato necessária. **3 correções na aprovação**: (1) `Gladiadores Romanos`
fundido em `Gladiadores`, já existente (Kings and Generals); (2) `Besteiros
Genoveses` fundido em `Balestreiros Genoveses`, já existente (SandRhoman
History) — essa linha também tinha um bug de sinal no `ano_inicio` (-1000
em vez de 1000), corrigido junto; (3) rebaixamento de `alta` para `média`
em `The Winter War... (Part 2 of 2)`, cujo ano final (1940) só estava
evidenciado na Parte 1 da série, não na própria linha. Pendências de
vocabulário deixadas em aberto, não bloqueantes: adjacência `Guerra
Romano-Seléucida`/`Guerras Sírias` (nomes parecidos, conflitos diferentes);
adjacência `Exército Sassânida`/`Império Sassânida` (verificada só depois
de criar o termo, mantida separada por analogia a `Império Romano`/
`Exército Romano`); subtema `Fronteiras do Império`, genérico demais, criado
para um vídeo com evidência truncada — ver acima, "Sobreposições ainda por
resolver". Detalhes completos em `canais.json`, campo `observacoes`.

**Lotes 168-171 (96 linhas) travados na aprovação de 07/08/2026 — primeiro
ciclo do canal `Epic History` (@EpichistoryTv), adotado no lote 168.** Canal
generalista de documentários narrados em inglês, sem série única amarrando
os quatro lotes: Guerras Napoleônicas (o maior bloco, cobrindo praticamente
toda a linha do tempo 1793-1815 batalha a batalha), Napoleão Bonaparte
(campanhas pré-Império), Império Bizantino (série completa de 6 partes
sobre Belisário sob Justiniano), Alexandre o Grande (série de 4 partes mais
extras), Cruzadas, Primeira Guerra Mundial (série ano-a-ano 1914-1918) e
Guerra Civil Russa/Revolução Russa. Introduziu **7 temas-raiz novos**:
`China Moderna`, `Programa Apollo`, `Castelos Medievais`, `República de
Veneza`, `Francis Drake`, `História da Rússia` e `Blackbeard` — mais **5
subtemas novos**: `Campanha do Egito` e `Campanha da Itália` (sob `Napoleão
Bonaparte`), `Alexander Kolchak` (sob `Guerra Civil Russa`), `Marechais de
Napoleão` (sob `Guerras Napoleônicas`) e `Decembristas` (sob `Revolução
Russa de 1905`, reaproveitando o precedente já aberto pelo canal Revolutions
de tratar os Decembristas como pano de fundo pré-1905 dentro desse tema).
Nenhuma região nova — todas as regiões usadas (inclusive `Áustria` e
`Alemanha`, primeira vez em `Guerras Napoleônicas`; `Atlântico`, por
aproximação, para `Blackbeard`, que não tem termo próprio de "Caribe" na
Lista B) já existiam. Confiança mais baixa que a média histórica do
catálogo (24% alta, 27% média, 46% chute, 2% n/a): o canal tem duas faces
opostas — os documentários mais recentes e mais bem financiados (Guerras
Napoleônicas 2018-2025, Suez Crisis, Waterloo) narram data explícita em
prosa própria quase sempre, enquanto o material institucional/atemporal
(guias 3D de navio e castelo, explicadores de tática) e as séries mais
antigas sem parágrafo narrativo próprio (Marechais de Napoleão pré-2024,
Belisário, Alexandre) não têm nenhum número na descrição, forçando `chute`
apoiado em conhecimento geral. Fact-check da parada confirmou a cronologia
inteira dos 6 episódios do Belisário (100% chute, reconstruída da numeração
da série) contra fontes externas, mais as datas-âncora de `República de
Veneza`, `Francis Drake` e as duas pontas de `História da Rússia` — todas
bateram, nenhuma correção necessária (uma pequena divergência não corrigida:
o próprio vídeo do Blackbeard diz "career probably began in 1717", enquanto
o consenso externo é final de 1716 — mantida a leitura do vídeo). **7
rebaixamentos de `alta` para `média` feitos antes da gravação**, todos pelo
mesmo padrão (número só no título ou em citação bibliográfica, não narrando
o evento na descrição/capítulos do próprio vídeo): `Battle of the Wabash
1791`, `Battle of Wagram 1809`, `The Peninsular War 1809-11`, `Battle of
Friedland 1807`, `Siege of Toulon 1793`, `Salamis 480 BC` e os dois vídeos
dos Abássidas (que tinham "século VIII" + "cinco séculos" na descrição, mas
nenhum ano numérico literal). Pendência de vocabulário deixada em aberto,
não bloqueante: `História da Rússia` (novo) se sobrepõe em conteúdo — não em
formato — com `Revolução Russa de 1905`/`Revolução Russa de 1917`, já
existentes (a Parte 5 da série, "The Last Romanov", narra o mesmo arco
1881-1917 que os dois temas de revolução já cobrem em profundidade); e
`China Moderna` (novo) é adjacente a `Dinastia Qing`/`Guerras do Ópio`, já
existentes — ver `protocolo.md`, "Armadilhas conhecidas", e detalhes
completos em `canais.json`, campo `observacoes`.

**O lote 167 (25 linhas) fechou o canal `History with Cy` por esgotamento
real, no meio do terceiro ciclo (167-170) — não por completar 4 lotes.**
Uma coleta seguinte confirmou 0 vídeos novos em 255 percorridos. Parada
rodou sobre a janela parcial real (25 linhas), mesmo procedimento já usado
para Cambrian Chronicles/GatesOfKilikien/The Histories. Cobriu o material
mais antigo do canal (2018-2019): biografias curtas de reis acadianos
(Sargão, filhos, Naram-Sin), a primeira série "History of Assyria" do
canal (distinta de "Concise History" e "Epic of Ancient Assyria Podcast",
já catalogadas em ciclos anteriores) e uma leva de civilizações/reinos que
ainda não tinham termo no catálogo. Introduziu **4 temas-raiz novos**:
`Ebla`, `Império Hitita` (lacuna importante do catálogo, agora coberta),
`Reino de Mitani` (com subtema `Hurritas (povo)`) e `Çatalhöyük`. Mais 4
subtemas novos em temas já canônicos: `Império Acadiano` → `Rimush e
Manishtushu`; `Suméria Antiga` → `Cidades do Período Dinástico Arcaico`;
`Babilônia Antiga` → `Dinastia Cassita`; `Geografia Estratégica` →
`Babilônia` (panorama da cidade através de vários impérios, distinto de
`Babilônia Antiga`, que cobre a civilização/dinastias — mesmo padrão de
Susa/Delfos/Corinto/Ur). Nenhuma região nova. **Nenhuma linha `alta`** neste
lote — o material mais antigo do canal (2018-2019) tem a evidência mais
fraca do canal inteiro (22 de 25 linhas `chute`, 23 sem nenhuma data no
bloco de evidência). Fact-check de 5 datações de maior risco: 3 confirmadas
sem correção (Dinastia Cassita, Império Hitita, Reino de Mitani) e 2
corrigidas na aprovação — Ebla (fim de 2300 para 2240 a.C., destruição por
Naram-Sin) e Çatalhöyük (fim de 5700 para 5500 a.C., ocupação completa do
sítio incluindo o monte oeste calcolítico), ambas por ficarem um pouco
curtas na ponta final da faixa, dentro da margem normal de incerteza de
datação pré-histórica/protohistórica — nenhuma correção grave. Pendências
de vocabulário deixadas em aberto, não bloqueantes: subtema `Panorama
Assírio (curso)` reaproveitado entre duas séries diferentes do canal
("Concise History of Ancient Assyria" e "History of Assyria"); subtema
`Estela da Vitória de Naram-Sin` usado para uma biografia geral do rei, não
especificamente sobre o artefato. Detalhes completos em `canais.json`,
campo `observacoes`.

**Os lotes 163-166 (100 linhas) fecharam o segundo ciclo do canal `History
with Cy`, aprovado em 07/08/2026 — canal segue `em andamento`, sem sinal de
esgotamento (lote 166 ainda veio cheio, 250 vídeos percorridos).** Ciclo
cobriu majoritariamente o material mais antigo do canal (2019-2022):
biografias curtas de reis/dinastias mesopotâmicas, a série em partes "The
Epic of Ancient Assyria Podcast", "Ancient Egypt Dynasty by Dynasty" e
"History of Ancient Canaan", além de povos/reinos periféricos do Antigo
Oriente Próximo (licênios, arameus, medas, hititas neo, cipriotas, urarteus)
e incursões na Grécia arcaica (colonização, Guerra Lelantina, Atenas) e na
Índia védica. Introduziu **19 temas-raiz novos**: `Lícia Antiga`,
`Numismática Antiga` (Extra), `Reino de Yamhad`, `Civilização do Oxus
(BMAC)`, `Ugarit`, `Guerra Lelantina`, `Atenas Antiga`, `Dilmun`, `Estados
Neo-Hititas`, `Império Meda`, `Arameus`, `Cartas de Amarna`, `Reino de
Urartu`, `Reino de Aksum`, `Reinos de Chipre`, `Reino de Anitta (Precursor
Hitita)`, `Civilização de Jiroft`, `Confederação Xiongnu` — mais 1 tema
proposto na classificação (`Reinos de Israel e Judá`) que a parada
identificou como duplicata de `Canaã Antiga > Reinos da Idade do Ferro`
(mesmo assunto, duas séries diferentes do canal) e fundiu na aprovação, com
as 2 linhas migradas para o subtema já existente. Mais **25 subtemas
novos**, com destaque para a cadeia cronológica completa da série "History
of Ancient Canaan" do canal dentro de `Canaã Antiga` (Jericó e o Bronze
Antigo → Idade de Ouro Cananeia/Bronze Médio → Domínio Egípcio/Bronze Final
→ Reinos da Idade do Ferro) e mais 4 subtemas em `Assíria Antiga` (Exército
Assírio, Biblioteca de Assurbanipal, Panorama Assírio (curso), Semíramis).
Confiança bem mais baixa que os ciclos anteriores do mesmo canal (12% alta,
6% média, 71% chute, 11% n/a): o material mais antigo do canal raramente
tem data na descrição ou nos capítulos. Fact-check de 6 datações `chute`/
inferidas de maior risco (Shulgi de Ur, Ur-Nammu, Anitta de Kussara, Idrimi
de Alalakh, Reino de Aksum, civilização Tolteca) confirmou todas as 6, sem
nenhuma correção. Pendências de vocabulário deixadas em aberto, não
bloqueantes — ver "Sobreposições ainda por resolver": par de subtemas com
faixas quase idênticas (`Exército Assírio`/`Panorama Assírio (curso)`);
adjacência `Civilização de Jiroft`/`Elam Antigo`; cluster `Dilmun`/`Magan`
(parceiros comerciais do Golfo com a Mesopotâmia); aproximações de região
(`Mediterrâneo` para Chipre e Sardenha, `Sudão` para Aksum, `Cáucaso` para
Urartu). Detalhes completos em `canais.json`, campo `observacoes`.

**Os lotes 159-162 (100 linhas) fecharam o primeiro ciclo do canal `History
with Cy`, aprovado em 07/08/2026 — canal segue `em andamento`.** Primeiro
canal do catálogo dedicado ao Antigo Oriente Próximo em profundidade
(Suméria, Acádia, Assíria, Babilônia, Elam) e ao Egito pré-clássico dinastia
por dinastia (do Período Pré-dinástico ao Período Tardio), com incursões em
Pérsia aquemênida, Grécia pré-helenística (Neolítico, Cíclades, Micênicos,
Guerras Médicas, Guerra do Peloponeso) e nos fenícios/cananeus do Levante.
Introduziu **13 temas-raiz novos** (`Suméria Antiga`, `Assíria Antiga`,
`Babilônia Antiga`, `Elam Antigo`, `Império Acadiano`, `Canaã Antiga`,
`Delfos`, `Cultura Cicládica`, `Povos do Zagros`, `Sociedade Mesopotâmica` e
`Sociedade Egípcia Antiga` — os dois últimos, Extra — mais um que **fundiu**
com um tema já existente: `Fenícia Antiga`, proposto na classificação,
identificado na parada como duplicata de `Civilização Fenícia` (já existente,
canal The Histories) e corrigido na aprovação, com as 3 linhas — Biblos, Tiro,
Sidon — migradas para o tema existente como subtemas novos). Mais **28
subtemas novos**, a maioria formando a periodização completa da egiptologia
dentro de `Egito antigo` (10 subtemas: Período Pré-dinástico → Dinastia 0 →
Período Dinástico Arcaico → Reino Antigo → Primeiro Período Intermediário →
Reino Médio → Segundo Período Intermediário → Reino Novo → Terceiro Período
Intermediário → Período Tardio) e a cadeia da Segunda Guerra Médica dentro
de `Guerras Médicas` (Revolta da Jônia → Primeira Invasão Persa/Maratona →
Invasão de Xerxes). Nenhuma região nova — todo o conteúdo mesopotâmico coube
em `Oriente Médio` por aproximação (sem termo próprio de "Mesopotâmia" na
Lista B ainda). Confiança mais baixa que a média histórica do catálogo (20%
`alta`, 26% `média`, 43% `chute`, 11% `n/a`): o canal raramente escreve datas
numéricas na descrição/capítulos dos vídeos mais antigos (2022-2023, formato
"Dynasty by Dynasty" e cidades mesopotâmicas avulsas), forçando faixas de
conhecimento geral. Fact-check de 6 datações `chute` de maior risco (Gudea de
Lagash, destruição de Mari, destruição de Hasanlu, fundação de Pasárgada,
período Cicládico Antigo, os dois candidatos aos Jardins Suspensos) confirmou
todas as 6, incluindo o caso mais arriscado (a própria historicidade dos
Jardins Suspensos é debatida). **Nenhuma correção de confiança na aprovação**
— diferente de ciclos anteriores, a checagem "todo `alta` tem número na
própria descrição/capítulos, não em título nem em vídeo relacionado" não
achou nenhuma linha inflada desta vez, embora a armadilha "número real mas de
vídeo relacionado" (ver `protocolo.md`, "Armadilhas conhecidas") tenha
aparecido 3 vezes (Pasárgada, Peloponnesian War Parte I, Esparta/Guerras
Messênias) — todas já classificadas `chute` corretamente antes da parada.
Pendências de vocabulário deixadas em aberto, não bloqueantes — ver
"Sobreposições ainda por resolver": adjacência `Suméria Antiga > Kish` /
`Império Acadiano` (Sargão começou a carreira em Kish); zona cinzenta
`Babilônia Antiga > Mari` / `Período Paleobabilônico` (Mari é um reino
amorita distinto, contemporâneo de Hammurabi); cluster de nomes parecidos
`Idade das Trevas Grega` (novo, Grécia antiga) / `Idade das Trevas`
(Historiografia) / `Idade das Trevas Global` (tema-raiz) — três assuntos
diferentes, risco de confusão numa sessão futura; família de temas Extra
atemporais sobre a Mesopotâmia (`Sociedade Mesopotâmica` novo vs `Comércio
na Mesopotâmia Antiga` já existente). Detalhes completos em `canais.json`,
campo `observacoes`.

**Os lotes 157-158 (45 linhas) fecharam o ciclo do canal `HistoryMarche` por
esgotamento — não por completar 4 lotes.** O lote 158 já tinha vindo como
mini-lote de 20 vídeos (sinal de esgotamento próximo, mesmo padrão já visto
em Cambrian Chronicles/SandRhoman/The Shogunate), e a coleta seguinte
confirmou 0 vídeos novos em 373 percorridos. Parada rodou sobre a janela
parcial real (45 linhas), não sobre 4 lotes completos — mesmo procedimento
já usado para Cambrian Chronicles e GatesOfKilikien. Introduziu **4
temas-raiz novos**: `Segundo Império Búlgaro` (distinto do `Primeiro
Império Búlgaro`, lote 154), `Miguel, o Bravo` (unificação da Valáquia/
Transilvânia/Moldávia, 1595-1601), `Ditmársia` (Hemmingstedt 1500) e
`Moldávia de Estêvão, o Grande` (Vaslui 1475) — nenhum subtema novo,
nenhuma região nova. Fact-check de 3 datações de maior risco confirmou
todas as 3 (cronologia da unificação de Miguel, o Bravo; afundamento do
SMS Emden em 9 de novembro de 1914; Batalha de Adrianópolis em 14 de abril
de 1205). Nenhuma correção na aprovação. Achado de vocabulário: os temas
`Guerra Otomano-Valáquia` (lote 152), `Moldávia de Estêvão, o Grande` e
`Miguel, o Bravo` (ambos deste ciclo) formam um cluster de três principados
romenos/moldavos distintos, todos região `Bálcãs` — corretamente separados
(regentes e períodos diferentes), mas visualmente parecidos na Lista C.
Praticamente toda a série numerada "Hannibal" do canal (Partes 1 a 23)
ficou coberta entre os lotes 149-158, todas sob `República Romana > Segunda
Guerra Púnica`. Pendências cross-ciclo da parada 149-152/153-156 seguem
sem correção (`TbVfFq16gK8`; faixa de "Hannibal PARTS 18-20"). **Canal
`encerrado` em 03/08/2026** — total de 245 linhas em 10 lotes (149-158).
Detalhes completos em `canais.json`, campo `observacoes`.

**Os lotes 153-156 (100 linhas) continuaram o canal `HistoryMarche`**,
aprovados em 03/08/2026 com parada completa — canal segue `em andamento`.
Introduziu **8 temas-raiz novos**: `Guerra Jacobita na Irlanda`, `Querela
das Investiduras`, `Primeiro Império Búlgaro`, `Sultanato de Delhi`,
`Dinastia Tang`, `Guerras do Decão`, `Império Marata` e `Império Gurida`
— nenhum subtema novo. **Primeiras 2 linhas `Extra` do canal**: um debate
historiográfico sobre como interpretar as invasões bárbaras (`eRUAvjL3uMU`)
e a história de transmissão do tratado agrícola cartaginês de Mago
(`cAXf1_dcdDE`) — ambos "assunto atemporal/método", não narrativa de
evento. Dois lotes (154 e 155) vieram da fase mais antiga do canal
(2019-2022), com formato "explicador"/minissérie sem data própria na
descrição — isso derrubou a confiança média do ciclo (20% `alta`, 61%
`média`, 17% `chute`, a maior proporção de `chute` de qualquer ciclo do
canal), mas o fact-check compensou: **5 datações `chute` de maior risco
verificadas, 5 confirmadas** (reinado de Simeão da Bulgária, 893-927;
reinado de Razia Sultana, 1236-1240; campanha de Ungern-Sternberg na
Mongólia, 1920-1921; Terceira Guerra Samnita, 298-290 a.C.; e a mais
arriscada — não só a faixa, mas o **assunto em si** — Rebelião de Huang
Chao, 874-884, identificada só pela combinação "contrabandista de
sal + revolta + Dinastia Tang" nas tags, sem nome próprio na evidência).
Nenhuma correção na aprovação — as 5 linhas da amostra da parada foram
julgamentos defensáveis, não erros. **2 lições novas no `protocolo.md`,
"Armadilhas conhecidas"**: capítulos de compilações "Hannibal PARTS X-Y"
podem ser cruzados para reconstruir a cronologia de partes vizinhas sem
capítulo próprio, mas isso não eleva a confiança acima de `chute`; e
compilações multi-região (Guerra Civil de César, Hannibal) sobem a região
um nível (`Mediterrâneo`) em vez de escolher arbitrariamente um dos países
cobertos. Pendências deixadas em aberto, não bloqueantes — ver
`vocabulario-canonico.md`, "Sobreposições ainda por resolver": nome
"Mameluco" compartilhado por `Sultanato de Delhi` (novo) e `Sultanato
Mameluco` (Egito, já existente) — dinastias diferentes, nome parecido;
`Battle of Sekigahara 1600` na fronteira exata entre `Sengoku Jidai` e
`Xogunato do Japão > Período Edo`. **2 pendências cross-ciclo, sobre linhas
já travadas de lotes anteriores, não corrigidas**: `TbVfFq16gK8` (lote 152)
foi classificada como a Batalha de Kleidion (1014) por inferência, mas o
lote 153 revelou que Kleidion é a Parte 5 da série do canal sobre Basílio
II, não a Parte 7 como a linha sugere — a identificação pode estar errada;
e a compilação "Hannibal PARTS 18-20" (lote 151, faixa `216-212 a.C.`) pode
precisar da faixa ajustada para `215-212 a.C.`, já que o lote 154 revelou
que a Parte 18 (Cumae) é 215 a.C., não 216 a.C. Detalhes completos em
`canais.json`, campo `observacoes`.

**Os lotes 149-152 (100 linhas) adotaram o canal `HistoryMarche`**, primeiro
canal do catálogo sem foco regional/temporal único: cada vídeo é uma batalha
isolada, de qualquer época (547 a.C. a 1745) e qualquer região (Pérsia,
Escócia, Bizâncio, Roma republicana, Alemanha, Ucrânia...), sem série
narrativa contínua amarrando um lote ao outro — o oposto do padrão usual
(canais de podcast/curso com um fio condutor único). Introduziu **15
temas-raiz novos**, o maior número desde a adoção do Ancient Americas:
`Guerra dos Nove Anos`, `Guerra Escocesa-Norueguesa`, `Polônia Piasta`,
`Guerra Dano-Hanseática`, `Guerra Franco-Holandesa`, `Levante de
Khmelnytsky`, `Guerra Franco-Flamenga`, `Invasões Magiares`, `Rebelião Percy
(1403)`, `Guerra Otomano-Valáquia`, `Guerras Sírias`, `Cruzada de Marrocos
(1578)`, `Guerras de Independência Suíça`, `Crise de 1383-1385` e `Guerra
Escaniana`. **1 subtema novo**: `Guerra Cimbria (113-101 a.C.)` sob
`República Romana` (a guerra ainda não tinha subtema próprio, distinto da
`Crise da República tardia`, posterior). **1 região nova**: `Dinamarca`
(3 vídeos que caíam em `Suécia` por aproximação — Visby, Isefjord, Lund —
corrigidos na mesma aprovação). Confiança mais baixa que a média histórica
do catálogo: **28% `alta`, 68% `média`, 4% `chute`** nas 100 linhas — o
canal escreve títulos com data exata quase sempre, mas a descrição raramente
narra o evento em si (mais comumente listas de vídeos relacionados e
bibliografia), então a maioria das linhas não passa no teste "capítulos ou
descrição narram o evento com número próprio" para `alta`. Fact-check de 4
datações de maior risco (as `chute`, mais uma `média` obscura): todas as 4
confirmadas por busca externa (reinado de Basílio II 976-1025; Batalha de
Kleidion 1014 como a "batalha final" de Basílio contra a Bulgária; janela
216-212 a.C. para a compilação Hannibal Partes 18-20, refinada pela 2ª
Batalha de Nola, 215 a.C.; Batalha de Merv/Herat 484 d.C.). **1 correção na
aprovação**: `_mIb1TOgmD0` (Tolbiac 496) rebaixado de `alta` para `média` —
a própria fonte hedgeia entre 496 e 506, o que enfraquece a ancoragem num
único ano mesmo havendo frase narrativa própria (ver `protocolo.md`,
"Armadilhas conhecidas"). Muitas linhas cobrem batalhas **já catalogadas por
outros canais** (Termópilas, Salamina, Las Navas de Tolosa, Blenheim,
Poltava, Abritus, Covadonga) — cobertura duplicada esperada e não é erro.
Pendências deixadas em aberto (ver "Sobreposições ainda por resolver"):
subtema `Cercos de Viena` reaproveitado para uma batalha adjacente (Párkány
1683) que pode merecer um subtema mais amplo; região `Turquia` para os
subtemas `Basílio II`/`Dinastia Comnena` aplicada também a campanhas nos
Bálcãs (Sirmium, Setina), não só a biografia de corte; granularidade de
região inconsistente entre `Guerra Franco-Flamenga` (`Países Baixos`) e
temas vizinhos da mesma geografia (`Europa Ocidental`). Canal `em
andamento`, sem sinal de esgotamento ainda.

**Os lotes 145-148 (95 linhas) fecharam a coleta do canal `Ryan M Reeves`** —
esgotamento real confirmado com uma coleta seguinte retornando 0 vídeos
novos em 210 percorridos (o lote 148 já tinha vindo como mini-lote de 20,
sinal de esgotamento próximo). Cobriu o restante do curso "Church History:
Early and Medieval/Reformation to Modern" e do curso "Lewis and Tolkien":
Padres da Igreja e concílios cristológicos (Constantinopla 381, Éfeso 431,
Calcedônia 451, Trindade pré-Niceia, gnosticismo, apologistas, perseguições,
monasticismo), o restante da carreira de Lutero e Calvino (quase 20 vídeos
novos cada, todos sob os subtemas já criados), precursores da Reforma (Jan
Hus, John Wycliffe), Cisma do Oriente e Ocidente (1054) e Grande Cisma do
Ocidente (1378-1417), Idade Média inglesa/franca/ibérica (Alfredo o Grande,
Merovíngios, Carlos Magno, Al-Andalus, Cruzadas, Magna Carta), e uma extensa
série sobre C.S. Lewis/J.R.R. Tolkien e os Inklings — 15 vídeos de análise
literária de ficção deles foram `Extra` (recepção, tema `História na
cultura popular > Literatura`, de outro canal), e só as 4 linhas biográficas
reais (vida de Lewis e Tolkien como pessoas históricas) foram para a linha
do tempo, sob o único **tema-raiz novo do ciclo**: `Inklings (Lewis e
Tolkien)`. Todos os outros temas usados já existiam (a maioria de outros
canais, reaproveitados pela primeira vez neste canal: `Império Bizantino`,
`Império Romano`, `Império Franco`, `Grécia antiga`, `República Romana`,
`Religião Romana`, `Inglaterra anglo-saxã`, `Era Viking`, `Expansão
islâmica`, `Formação das Monarquias Nacionais`, `Cruzadas`, `Guerra dos Cem
Anos`, `Peste Negra`, `Renascimento`, `Cisma do Oriente e Ocidente`).
Fact-check de 6 datações `chute` de vida/reinado (nenhuma com número na
evidência do próprio vídeo): todas as 6 confirmadas por busca externa, sem
correção. **2 reuploads confirmados** neste ciclo (mesmo título/faixa,
`video_id` diferente): `IXpX1Gy4vYA`/`Sjy23bJdLQg` ("Luther's Reformation
Breakthrough") e `7LDJiCtGuxA`/`JF3t3Xx4s5A` ("The Hobbit") — ver
`protocolo.md`, "Armadilhas conhecidas", para o risco de copiar a faixa do
par sem reavaliação independente. Nenhum erro de confiança inflada, tema
contradizendo os anos da própria linha, ou faixa fechada sobre evidência
truncada foi encontrado na parada — travado direto na aprovação de
03/08/2026. Pendências de vocabulário deixadas em aberto (ver
"Sobreposições ainda por resolver"): `Pano de Fundo Medieval da Reforma` e
`Indulgências` com faixa idêntica (1300-1517); `John Wycliffe` e `Jan Hus e
a Profecia da Reforma` como precursores da Reforma tratados separadamente;
`Sociedade Medieval` acumulando 5 vídeos com a faixa idêntica (Panorama
500-1500). Canal `Ryan M Reeves` aguardando `/encerrar`.

**Os lotes 141-144 (100 linhas) adotaram o canal `Ryan M Reeves`**, primeiro
do catálogo dedicado à história do cristianismo e teologia histórica —
professor de teologia histórica que cobre desde os Padres da Igreja
(Ambrósio, Atanásio, Boécio) até a Reforma (Lutero, Calvino, Zwínglio/
Bullinger, Anabatistas, Puritanos), a Escolástica medieval (Anselmo,
Abelardo, Bernardo de Claraval, Tomás de Aquino, Duns Scotus, Guilherme de
Ockham) e o cristianismo americano moderno (Grandes Despertares,
Fundamentalismo, Pentecostalismo). Introduziu **11 temas-raiz novos**:
`Reforma Protestante` (já existia com 1 vídeo de outro canal; ganhou massa
aqui, 32 vídeos), `História do Cristianismo Moderno` (criado no lote 142
como "Cristianismo Americano Moderno", renomeado no lote 143 por já cobrir
conteúdo não-americano), `Escolástica Medieval`, `História dos Feriados`,
`História da Arte`, `História da Bíblia`, `Credos e Confissões Cristãs`,
`Caça às Bruxas`, `Revolução Científica`, `Pseudociência e Conspirações` e
`Teologia Cristã` (bucket para explicadores doutrinários atemporais,
tratados como `Aleatório` por não narrarem período histórico algum). Mais
de 60 subtemas novos, a maioria sob os dois temas grandes acima — ver Lista
C para a lista completa. **1 região nova**: `Suíça` (ministério de Calvino
em Genebra e Bullinger em Zurique, 6 vídeos). Fact-check externo sobre 8
datações `chute` de maior risco (vidas/fundações inteiramente de
conhecimento geral, sem nenhum número na evidência do vídeo) **confirmou
todas as 8**, sem correção — ver `protocolo.md`, "Armadilhas conhecidas".
**1 correção na aprovação**: `ljBaVIp2pJQ` (Notre Dame de Paris) saiu de
`Vida urbana > Paris` para `Geografia Estratégica > Notre-Dame de Paris` —
mesmo padrão já documentado do Xi'an (GatesOfKilikien): o vídeo é um
panorama de mais de 2000 anos, e `Vida urbana` é sempre um recorte estreito
de época. Pendências de vocabulário deixadas em aberto (ver "Sobreposições
ainda por resolver"): `Puritanismo` espalhado em três temas-raiz diferentes;
`Reforma Católica (Contrarreforma)` aninhado dentro de `Reforma Protestante`
apesar de ser a reação católica, não parte dela; `Concílio Vaticano I` (em
`Papado`) e a Contrarreforma (em `Reforma Protestante`) tratando do mesmo
domínio católico em temas-raiz diferentes; subtema `Halloween` compartilhado
por dois vídeos de assunto nominalmente distinto (Dia de Finados vs.
Halloween em si).

**Os lotes 139-140 (40 linhas) adotaram o canal `Magistra Vitae`**, primeiro
do catálogo dedicado à Roma pré-imperial (Reino de Roma, início da
República, Guerras Samnitas/Latina, Guerras Púnicas) com incursões em
Grécia arcaica/clássica e Egito antigo em formato de panorama. Nenhum
tema-raiz novo — tudo coube em `Reino de Roma` e `República Romana`, já
existentes, mais `Cartago antiga` para dois vídeos sobre a expansão
cartaginesa pré-guerra. **8 subtemas novos**, todos sob temas já
existentes: `Conflito das Ordens`, `Guerra contra Veios`, `Saque Gaulês de
Roma`, `Primeira/Segunda/Terceira Guerra Samnita`, `Guerra Latina` e
`Guerra Pírrica` (sob `República Romana`); `Guerra dos Mercenários` e
`Conquista Bárcida da Ibéria` (sob `Cartago antiga`). Nenhuma região nova —
`Itália`, `Grécia`, `Egito`, `Mediterrâneo`, `Península Ibérica` e `Norte da
África` já existiam. Travados na aprovação de 03/08/2026, sem correções
(revisão própria da sessão, sem parada formal de quatro lotes completa — só
2 lotes desde a adoção do canal — não encontrou confiança inflada, tema
contradizendo os anos da própria linha, nem faixa fechada sobre evidência
truncada além do já registrado nas notas individuais). Confirmado **um
padrão de reupload**: `Founding of Rome [OLD]` e `Seven Kings of Rome`
(lote 140) são a série antiga do canal, mesmo conteúdo de `Founding of Rome
- Start of the Greatest Civilisation` e `Seven Legendary Kings of Rome`
(lote 139) — a diferença é que a série antiga dividia o Reino de Roma em
dois vídeos (fundação + os seis reis seguintes) e a nova compila tudo em um
só por vídeo equivalente; a própria descrição do vídeo antigo linka o
remake. Ver `protocolo.md`, "Armadilhas conhecidas", para o registro desse
padrão de reupload por recombinação (distinto do reupload 1:1 já
documentado em outros canais).

**Os lotes 136-138 (75 linhas) fecharam a coleta inteira da playlist
`Revolutions (Mike Duncan)`** — não quatro lotes, três, porque o canal
esgotou no meio do ciclo (confirmado com duas coletas seguidas retornando 0
vídeos novos nos mesmos 350 percorridos). Cobriu o resto da Season 10 (do
pós-1905/Stolypin, 1917 do prelúdio ao Caso Kornilov, Revolução de Outubro,
Guerra Civil Russa até a fundação da URSS e a luta pela sucessão de Lenin,
1922-1932) e o encerramento inteiro do podcast: a série de apêndices
teóricos comparando as revoluções cobertas nas dez temporadas, o episódio de
despedida da série regular, e uma mini-season fictícia posterior de quase um
ano ("Martian Revolution", ficção científica, publicada em 2024 como
retorno do autor). Introduziu **5 temas-raiz novos** (`Revolução Russa de
1917`, já reservado desde a parada 133-135; `União Soviética`; `Revolução
Alemã`; `Teoria da Revolução`, Extra; `Revolução Marciana (ficção)`,
Aleatório) e **7 subtemas novos**, nenhuma região nova. Fact-check externo
sobre as 6 datações de maior risco (todas `chute`, nenhuma com data própria
na evidência) **confirmou todas as 6** sem nenhuma correção — ver
`protocolo.md`, "Armadilhas conhecidas", para o caso da série de apêndices
teóricos (`Extra`/método) e o teste que a distingue de um falso Panorama.
Travado direto na aprovação de 03/08/2026, sem correções (nenhum erro
encontrado na parada). Pendências de vocabulário deixadas em aberto: a
cadeia de quatro temas-raiz para o mesmo arco 1905-1932; `Frente Oriental`
como nome de subtema repetido em dois temas (Primeira e Segunda Guerra
Mundial); `Guerra Polaco-Soviética` como subtema vs. tema-raiz próprio;
região `Leste Europeu` usada por aproximação por falta de `Polônia` na Lista
B; e a linha `rGxVvpsIRUk` ("Streets of Paris"), classificada por palpite
quase sem evidência nenhuma. Ver "Sobreposições ainda por resolver", acima,
para os detalhes de cada uma. Canal `Revolutions (Mike Duncan)` aguardando
`/encerrar`.

**Os lotes 133-135 (75 linhas) fecharam um ciclo parcial de três lotes da
playlist `Revolutions (Mike Duncan)`** — não quatro, porque a parada anterior
já tinha fechado nos lotes 129-132; esta parada rodou sobre a janela real
acumulada desde então, mesmo padrão já usado com Cambrian Chronicles,
GatesOfKilikien e The Histories. Cobriu o fim da Comuna de Paris (8.8, semana
sangrenta de maio/1871, tema já aprovado), a Season 9 inteira (Revolução
Mexicana, Nova Espanha colonial 1521 até o Maximato/Cárdenas 1940) e o início
da Season 10 (a Revolução Russa propriamente dita, do pano de fundo
ideológico — Primeira Internacional, Marx, Bakunin — até o pós-1905, reformas
Stolypin e golpe de 1907). Travados na aprovação de 03/08/2026, depois da
parada: **5 correções aplicadas antes de travar.** Fact-check externo
corrigiu duas datações: início da doutrina da Terceira Roma (1547→1523,
epístola de Filofei de Pskov em vez da coroação de Ivan IV) e fim da Union of
Struggle for the Emancipation of the Working Class (1897→1900, dissolução
real da organização, fusão no RSDLP); confiança rebaixada de alta para média
em uma linha por só uma ponta da faixa ter data própria (The Socialist
Revolutionaries, faixa 1881-1901 com só o início — "didn't die after 1881" —
evidenciado); início corrigido de 1893 para 1894 em outra (Vladimir and
Nadya, Lenin conheceu Krupskaya em fevereiro de 1894). Uma linha
reclassificada por conteúdo: `10.7 - The Paris Commune Revisited` saiu de
`Revolução Russa de 1905` para `Comuna de Paris` (tema já existente) — o
episódio revisita o evento de 1871 pela lente do debate Marx-Bakunin, mas o
conteúdo é sobre a Comuna, não sobre a Rússia (vale o conteúdo, não o rótulo
da temporada, mesmo princípio do achado Manzikert já registrado em
`protocolo.md`). **Achado de vocabulário mais importante da parada:** o tema
`Revolução Russa` (criado sem qualificador no lote 134, 21 linhas, episódios
10.1-10.21) e o tema `Revolução Russa de 1905` (criado separadamente no lote
135, 25 linhas, episódios 10.22-10.46) cobriam o mesmo arco narrativo
contínuo sem que a classificação do lote 135 checasse o que o lote 134 já
tinha criado — fundidos em `Revolução Russa de 1905` (45 linhas após a
reclassificação acima). `Revolução Russa de 1917` fica reservado, ainda sem
nenhuma linha, para quando a playlist chegar lá de fato — ver "Sobreposições
ainda por resolver" para o registro completo da distinção entre os dois
eventos. Nenhum tema-raiz novo além da fusão, nenhuma região nova (as 56
regiões usadas nos três lotes já existiam todas na Lista B).

**Os lotes 129-132 (100 linhas) fecharam o segundo ciclo completo de quatro
lotes da playlist `Revolutions (Mike Duncan)`.** Cobriu a Revolução Haitiana
inteira (Season 4, Saint-Domingue de colônia francesa a nação independente,
1697-2016), as Guerras de Independência Hispano-Americanas (Season 5,
1492-1830, de Bolívar a San Martín, terminando com a morte de Bolívar e a
dissolução da Gran Colômbia), as Revoluções de 1830 (Season 6, França e
Bélgica) e a maior parte das Revoluções de 1848 e o início da Comuna de
Paris (Seasons 7-8, até o nascimento da Comuna em março de 1871). Travados
na aprovação de 03/08/2026, depois da parada: **1 correção aplicada antes de
travar** — a faixa de `_qxcm5y-FuE` ("5.09 - God's Divine Wrath") foi
estreitada de `1810-1812` para `1811-1812`: fact-check externo confirmou que
a Primeira República Venezuelana foi formalmente proclamada em 5/jul/1811,
não em 1810 (data da Junta de Caracas que iniciou o processo político, mas
não da própria "Primeira República"). Outros 5 fact-checks bateram sem
correção: cessão de Saint-Domingue à França (Tratado de Ryswick, 1697),
retorno de Bolívar à Venezuela (1807), vida de Gregor MacGregor (1786-1845),
recusa da coroa por Frederico Guilherme IV ("crown from the gutter", 3 de
abril de 1849). A amostra de 5 linhas sorteada teve 3 de 5 sinalizadas como
decisão de base fraca (`mp4d4GPhuT4` Metternich, `GSGWlAezl3M` The Sea Wolf,
`qZ80T9JpFos` Assembly of the Damned — todos episódios de contexto/transição
sem nenhuma data na evidência, faixa inteiramente por conhecimento geral) —
aprovada sem pedido de correção adicional. Canal introduziu **5 temas-raiz
novos e 1 região nova**: `Revolução Haitiana` (região `Haiti`, nova — nome
do país moderno, não "Saint-Domingue"), `Guerras de Independência
Hispano-Americanas`, `Revoluções de 1830`, `Revoluções de 1848` e `Comuna de
Paris` (regiões já existentes nos quatro últimos) — nenhum subtema novo,
mesma decisão de segurar propostas até a densidade se confirmar já usada com
a Revolução Francesa. Ver `canais.json`, campo `observacoes`, para o
detalhamento completo dos quatro lotes.

**Os lotes 125-128 (100 linhas) fecharam o primeiro ciclo completo de quatro
lotes da playlist `Revolutions (Mike Duncan)`** (adotada no lote 125 — mesmo
padrão do History of Rome: playlist específica hospedada num canal sem
relação com história, `@Seaquences`, resolvida via `--nome` na adoção).
Cobriu o fim da Guerra Civil Inglesa e o Interregno (1625-1660), a Revolução
Americana inteira (1607/1763-1791) e a Revolução Francesa até o limiar do
Consulado (1789-1799), mais Consulado e Império de Napoleão (1799-1815).
Travados na aprovação de 03/08/2026, depois da parada: **1 correção
aplicada antes de travar** — 2 linhas (`laM6N_ZnYxs`, introdução do podcast;
`M6yv1ftGTj8`, especial de perguntas e respostas do 250º episódio) tinham
`Século/Período = Extra` em vez de `Aleatório`, porque o script de gravação
usa a função `periodo()` compartilhada com o `verificar.py`, que devolve
`"Extra"` sempre que os anos vêm vazios — sem saber que essas duas linhas são
avisos de canal, não história sem período fixável. Corrigido para
`Aleatório` nas duas (só essa célula, confirmado por diff célula a célula
contra o backup pré-correção). **A mesma inconsistência já existia antes
desta sessão**, sem relação com o canal Revolutions: `6pemEIq1KOo` ("100K
Q&A: Better Late Than Never", lote 77, canal Ancient Americas, já encerrado
e travado) tem o mesmo padrão (`Tema = Avisos do canal`, `Século/Período =
Extra`) e **não foi corrigida** — está fora do escopo desta parada e exigiria
aprovação humana explícita célula a célula por já estar travada de um ciclo
anterior. Ver `protocolo.md`, "Armadilhas conhecidas", para o registro
completo do bug. 8 fact-checks por busca externa nesta parada (Diggers
1649-50, Philippe Égalité 1747-1793, Golpe de Prairial 18/jun/1799, slogan
"Bread and the Constitution of 1793" → revolta de Prairial de 1795, Guns of
Ticonderoga 1775-76) bateram sem divergência — inclusive as duas linhas que
eu mesmo tinha rebaixado de `alta` para `média` na hora de classificar (Coup
of Prairial, Thermidor), confirmando que o rebaixamento foi o julgamento
certo. A amostra de 5 linhas sorteada para o humano foi apresentada com uma
ressalva própria (`3.37 The Republic of Virtude`, data 1794 ancorada de
memória não verificada na hora — confirmada só agora, na aprovação, pela
busca do discurso de Robespierre de 5/fev/1794). Canal introduziu **1
tema-raiz novo e 6 subtemas novos**: `Revolução Francesa` (57 linhas, região
`França` já existente); subtemas `Protetorado de Cromwell` (em `Guerra Civil
Inglesa`), `Queda da Monarquia`, `O Terror`, `Reação Termidoriana` e
`Diretório` (todos em `Revolução Francesa`) — nenhuma região nova. Decisão de
fronteira: os episódios sobre o Consulado e o Império de Napoleão (3.53,
3.54) **não** entraram em `Revolução Francesa` — foram para o tema já
existente `Napoleão Bonaparte` (região `Europa`), porque o Golpe de Brumário
marca o fim convencional da Revolução na historiografia padrão, e as faixas
bateram exatamente com linhas já catalogadas desse tema por outro canal.
Canal segue `em andamento`. Ver `canais.json`, campo `observacoes`, para o
detalhamento completo dos quatro lotes.

**Os lotes 123-124 (29 linhas) fecharam o canal `GatesOfKilikien` — primeiro
do catálogo dedicado à China antiga/medieval —, num ciclo de 2 lotes em vez
de 4.** O canal esgotou de fato: 29 vídeos percorridos ao todo (25 no lote
123, mais 4 no lote 124), e uma terceira coleta confirmou 0 vídeos novos nos
mesmos 29. Sem os quatro lotes de praxe, a parada rodou sobre a janela real
disponível — mesmo padrão já usado com Cambrian Chronicles e The Histories.
Travado na aprovação de 02/08/2026, depois da parada: **2 correções
aplicadas antes de travar.** `Xi'an (Chang'an)` Partes 1 e 2 (`Ypprp25DKK8`,
`F_wjEVfVIfQ`) saíram de `Vida urbana > Chang'an` para `Geografia
Estratégica` — os dois são ensaios panorâmicos de mais de 800 anos sobre a
cidade-capital através dos séculos, o mesmo formato dos outros ensaios de
"lugar estratégico" do canal, não a fatia estreita de vida urbana que o
resto do tema usa. E 2 linhas (`GZ_lSXv4Psg`, `1ivVDnSyM7Q`) tiveram a
confiança rebaixada de `alta` para `média`: em ambas, só uma ponta da faixa
tinha um ano exato narrando o evento — a outra vinha de formato de década
(`400s`/`400s-410s`) ou do `~` de aproximação da própria fonte. 4
fact-checks por busca externa (Batalha de Jinyang/Partição de Jin em 453/403
a.C., fundação da Dinastia Liu Song em 420, conquista romana da Hispânia
218 a.C.-476, uso do Grande Canal até o Song do Norte) bateram sem
divergência de datação. Achado à parte, sem impacto na planilha: a
descrição de "Ancient Greece - The Peloponnese" cita "300 (2006)", que é o
ano do filme *300*, não uma data histórica — descartado como evidência na
hora de classificar. A amostra de 5 linhas sorteada para o humano foi
aprovada sem pedido de correção adicional; as duas linhas sinalizadas na
apresentação como decisão de base mais fraca (`GZ_lSXv4Psg`, `1ivVDnSyM7Q`)
foram justamente as que caíram na correção de confiança acima. Canal
introduziu **6 temas-raiz novos e 5 subtemas novos em temas já existentes**
(`Dinastia Zhou`, `Dinastia Jin`, `Dezesseis Reinos`, `Grande Canal da
China`, `Geografia Estratégica`, `Curiosidades da História Chinesa`;
subtemas `Período dos Três Reinos > Ascensão de Cao Cao`, `Dinastia Han >
Han Ocidental`/`Han Oriental`, `Império Romano > Hispania Romana`), nenhuma
região nova. `Geografia Estratégica` é o primeiro tema do catálogo
explicitamente cross-região por desenho de formato, não por aproximação de
conteúdo (ver Lista C, "Sobreposições ainda por resolver"). Pendências
abertas, não resolvidas: `China antiga` (existente, outro canal) vs.
`Dinastia Zhou` (novo); os 2 vídeos antigos de `Dinastia Han` continuam sem
subtema, travados, sem retroagir sem aprovação explícita. Canal segue `em
andamento` no `canais.json` — esgotado, aguardando `/encerrar`.

**O lote 122 (21 linhas) fechou sozinho, como um ciclo de um lote só, na
adoção do canal `The Histories`** — o canal só tem 21 vídeos longos
publicados, todos coletados de uma vez; uma segunda coleta confirmou 0
vídeos novos. Sem os quatro lotes de praxe, a parada rodou sobre a janela
real disponível. Travado na aprovação de 02/08/2026, depois da parada: **4
datações `chute` corrigidas por fact-check externo** — Minoicos (início
2700→3000 a.C., padrão Britannica), Fenícios (início 1200→1500 a.C., padrão
Met Museum), Pechenegues (fim 1100→1122, Batalha de Beroia é o
desaparecimento real, não Levounion 1091) e Pictos (início 300→297,
primeira menção romana documentada). Outras 4 datações `chute`/`alta`
verificadas bateram sem correção (Filisteus, Etruscos, Vândalos, Hunos). A
amostra de 5 linhas sorteada para o humano incluiu duas das corrigidas
(Pechenegues, Minoicos) e foi aprovada sem pedido de mudança adicional.
Canal introduziu **12 temas-raiz novos e 2 subtemas novos** (Icenos,
Gauleses, Hunos, Godos, Lídios, Hititas, Vândalos, Filisteus, Cátaros,
Pictos, Suevos, Pechenegues; subtemas `Expedição de Narváez` sob
`Conquistadores` e `Hereward, o Vigilante` sob `Conquista normanda da
Inglaterra`), nenhuma região nova — canal é inteiramente formato "Who were
the X?", uma etnografia de povo antigo por vídeo, o que produziu o maior
número de temas-raiz de um lote só (não ciclo de quatro) desde a adoção de
qualquer canal novo. 2 sobreposições de vocabulário registradas, não
resolvidas: `Vândalos` vs. `Reino Vândalo`; `Cátaros` vs. `Cruzadas >
Cruzada Albigense` (ver "Sobreposições ainda por resolver"). Região `Judeia`
usada por aproximação para os Filisteus é a mais frágil já registrada —
filisteus e judeus eram povos rivais, não o mesmo (ver Lista B, acima).
Canal continua `em andamento` — decisão do humano de não encerrar um canal
já esgotado, para deixar a porta aberta a upload futuro.

**Os lotes 117-121 (110 linhas) fecharam o terceiro ciclo pós-adoção do canal
`The Shogunate`** — estendido a 5 lotes (em vez de 4) porque o lote 121 veio
como mini-lote de só 10 vídeos (304 percorridos, quase todos já conhecidos),
sinal forte de que a coleta está perto de esgotar o arquivo do canal.
Travados na aprovação de 02/08/2026, depois da parada — nenhuma correção
aplicada às 110 linhas: os 9 fact-checks por busca externa (Anegawa, Monte
Hiei, Mikatagahara, Otate no Ran, Konodai, Un no Kuchi, Cerco de Odawara,
Yasuke, Kizugawaguchi) bateram sem divergência, e a amostra de 5 linhas
sorteada foi aprovada sem correção — duas foram sinalizadas na apresentação
como decisões de base mais fraca (`J5PAt9YMqtc`, resenha pré-lançamento de
Ghost of Tsushima classificada como Aleatório em vez de possivelmente Extra;
`aIrPeV8Lg_Y`, recap+discussão que herdou a faixa Panorama do recap irmão por
analogia). **Primeiro ciclo do canal sem nenhum termo novo** — os 110 vídeos
usaram só vocabulário já existente (`Sengoku Jidai` sozinho recebeu 48
linhas, o maior uso de um tema num ciclo só do canal). A proporção de linhas
na linha do tempo subiu para 64% (contra 48-49% dos dois ciclos anteriores) —
esperado, já que estes lotes cobriram o miolo da série numerada "Sengoku
Jidai" (que agora está catalogada do Episódio 1 ao 64, FINALE) e menos
conteúdo de resenha/jogo proporcionalmente. O lote 121 trouxe também 8
vídeos "(OUTDATED)" da série original "Setting the Stage", substituída pela
"Setting the Stage (UPDATED)" já catalogada nos lotes 110-111 — mapeados 1:1
para o tema/faixa da versão nova (3 confirmados porque o vídeo UPDATED cita o
título antigo na própria descrição). Nenhuma pendência de vocabulário nova;
as 8 já registradas nas duas paradas anteriores continuam abertas (ver
"Sobreposições ainda por resolver").

**Os lotes 113-116 (100 linhas) fecharam o segundo ciclo completo de quatro
lotes pós-adoção do canal `The Shogunate`.** Travados na aprovação de
02/08/2026, depois da parada — nenhuma correção aplicada às 100 linhas: os
11 fact-checks por busca externa (Sekigahara, morte de Toyotomi Hideyoshi,
invasão de Ryukyu, Batalha de Minatogawa, Cerco de Akasaka, regência Hōjō do
Xogunato Kamakura, Xogunato Ashikaga, chegada de Francisco Xavier, édito de
expulsão cristã de 1614, Miyamoto Musashi, rebelião de Taira Masakado)
bateram sem divergência, e a amostra de 5 linhas sorteada para o humano
(2 linha do tempo, 2 Extra, 1 Aleatório) foi aprovada sem correção — duas
delas (`np-NKhtwQ_4`, "The Cursed Blades of Muramasa", e `jx4zXF_nD-4`, "How
Peace Changed the Samurai") foram sinalizadas na apresentação como decisões
de base mais fraca (Extra vs. um tema mais específico), mas nenhuma correção
foi pedida. Canal introduziu **5 temas-raiz novos e 2 subtemas novos**
(`Lendas samurai`, `Cultura material samurai`, `Ranking de samurais`,
`Cristianismo no Japão`, `Família Imperial do Japão`; subtemas `Batalha de
Nagashino` e `Cerco de Osaka`, ambos sob `Sengoku Jidai`), nenhuma região
nova — ritmo de vocabulário bem mais lento que o primeiro ciclo (12 temas em
3 lotes), esperado à medida que o vocabulário do canal satura. Também ficou
mais historiográfico: só 49% das 100 linhas ficaram na linha do tempo
(contra 48% no ciclo anterior), estável. Pendências novas registradas, não
resolvidas (ver "Sobreposições ainda por resolver"): `Clãs do Sengoku` cada
vez mais heterogêneo (16 vídeos, incluindo dois clãs Hojo homônimos somados
num Panorama de 387 anos); `Ranking de samurais` vs. `Últimas Resistências
Samurai` (dois temas para tier-ranking histórico através de toda a
história); `Xogunato do Japão` vs. `Família Imperial do Japão`; critério de
"vídeo de discussão ancorado a evento vs. debate metodológico amplo" ainda
não confirmado por revisão humana (ver `protocolo.md`, "Armadilhas
conhecidas").

**Os lotes 110-112 (75 linhas) fecharam o primeiro ciclo pós-adoção do canal
`The Shogunate`** (adotado no lote 110, primeiro canal novo desde o
encerramento do SandRhoman History — nenhum canal ficou `em andamento` entre
os dois). Ciclo de 3 lotes, não 4: a adoção em si já consumiu o primeiro lote
da janela, então a parada rodou sobre os únicos 3 lotes acumulados desde então,
sem esperar um lote 113. Travados na aprovação de 02/08/2026, depois da
parada — nenhuma correção aplicada às 75 linhas: os 14 fact-checks por busca
externa (Guerra Genpei, Rebeliões Hōgen/Heiji, Guerra Ōnin, invasões mongóis,
Grande Incêndio de Meireki, início do Sakoku, Hōjō Sōun, Batalha de
Shizugatake, Uesugi Kenshin, Incidente de Honnōji, morte de Imagawa Yoshimoto,
era Tenshō, Kawanakajima, Shiroyama) bateram sem divergência, e a amostra de 5
linhas sorteada para o humano (enviesada para `Aleatório`/`Extra` por sorteio
honesto, não por escolha) foi aprovada como estava. Canal introduziu **12
temas-raiz novos e 3 subtemas novos** (`Guerra Genpei`, `Formação do Japão
Guerreiro`, `Jogos de samurai`, `Últimas Resistências Samurai`, `Restauração
Kenmu`, `Comentários sobre criação de conteúdo`, `Jogos de tabuleiro e
cartas`, `Jogos de estratégia`, `Marinha samurai`, `Espadas militares
japonesas`, `Shinobi`, `Japoneses no exterior`; subtemas `Período Edo` sob
`Xogunato do Japão`, `Clãs do Sengoku` e `Guerra Ōnin` sob `Sengoku Jidai`),
nenhuma região nova, e foi o primeiro canal a reaproveitar um tema criado por
outro canal (`Resenhas de ficção`, do Thersites the Historian, cresceu de 5
para 20 linhas com as resenhas de "Shogun" 2024/FX) — confirma que a Lista C é
mesmo compartilhada entre canais, não um vocabulário por canal. Canal também
introduziu o padrão de amostra crua mista: das 75 linhas, só 36 (48%) ficaram
na linha do tempo — as outras 39 são resenha de jogo/filme/TV, entrevista
sobre livro/produto ou aviso de canal, o maior desvio para fora de história
de um canal só desde o Thersites the Historian. Pendências registradas, não
resolvidas (ver "Sobreposições ainda por resolver"): `Sakoku` vs. `Período
Edo`; três temas `Jogos de X`; `Formação do Japão Guerreiro` vs. `Guerra
Genpei`; nome de `Clãs do Sengoku`. Uma linha (`JqkG_hxQLhQ`, "Top 5 Greatest
Samurai Last Stands", lote 112) recebeu faixa por suposição — copiada do
vídeo seguinte do mesmo lote, que é uma continuação explícita e cita batalhas
reais, mas a própria linha não tem nenhuma data nem batalha nomeada na
evidência. Aprovada mesmo assim (a suposição é razoável dado o formato de
dupla do canal), mas registrada aqui para quem revisitar.

**Os lotes 107-109 (53 linhas) fecharam o canal `SandRhoman History` e foram
travados sem ter passado por uma parada de quatro lotes completa** — só
havia 3 lotes desde a última parada (feita sobre 103-106) quando a coleta do
canal esgotou (lote 109 fechou com 3 linhas; a coleta seguinte devolveu 0
vídeos novos em 153 percorridos). O canal foi encerrado com fact-check
pontual no lugar da parada formal (mesmo padrão do Cambrian Chronicles), e
esta aprovação rodou uma parada retroativa sobre os 3 lotes pendentes antes
de travar. Fact-check confirmou 2 datações sem correção necessária (cerco de
Candia 1648-1669; fundação dos Mosqueteiros do Rei em 1622, dentro da faixa
1600-1700 usada). Canal fechou com **26 temas-raiz novos e 2 regiões novas**
ao longo dos 7 lotes inteiros — o maior salto de vocabulário de um canal só
desde o Ancient Americas. A Guerra dos Trinta Anos ganhou a periodização
historiográfica padrão completa (Fase Boêmia, Fase Dinamarquesa, Intervenção
Sueca, Fase Francesa, Guerra de Sucessão de Mântua). Pendências registradas,
não resolvidas: região `Polônia` candidata (7+ usos de `Leste Europeu` só
nos lotes 107-109, somando-se à `Suíça` já candidata dos lotes 103-106);
`Cercos de Viena` (subtema novo do lote 108) tem um irmão natural já travado
(cerco de 1529, lote 106) que precisaria de aprovação humana explícita
célula a célula para juntar; sobreposição parcial entre `Guerra
Polaco-Sueca` e `Hussardos Alados` (mesmo período, atores parcialmente
sobrepostos). Ver `canais.json`, campo `observacoes`, para o detalhamento
completo dos 7 lotes.

**Os lotes 103-106 (100 linhas) fecharam o primeiro ciclo completo de quatro
lotes do canal `SandRhoman History`** (adotado no lote 103, após o
encerramento do The History of Byzantium Podcast). Travados na aprovação de
02/08/2026, depois da parada: 2 datações corrigidas por fact-check externo —
faixa da Guarda Varegue (`7BlRu7lkVpM`) estendida de 988-1204 para 988-1453
(a fonte mais consistente aponta continuidade até a queda de Constantinopla,
não até a Quarta Cruzada) e faixa da Companhia Alemã de Werner de Urslingen
(`_cdWg7biGxo`) estreitada de 1338-1354 para 1342-1347 (a companhia foi
fundada e dissolvida no mesmo ano, 1342; Werner só voltou à Itália em 1347).
Uma terceira correção menor: início da White Company (`D8-KzkExE-s`) de 1360
para 1361 (a companhia entrou na Itália em 1361; 1360 é o ano do Tratado de
Brétigny, que liberou os mercenários, não o ano da travessia). Canal muito
institucional/granular: 16 temas-raiz novos, 2 regiões novas (`Países
Baixos`, `Hungria`) e 14 subtemas novos numa janela só — o maior número de
temas-raiz de um único ciclo desde a adoção do Ancient Americas (lotes
77-78). Ver `protocolo.md`, "Armadilhas conhecidas", para a lição sobre
faixas de instituição montadas de memória sem nenhuma busca no momento da
classificação.

**Os lotes 100-102 (69 linhas) fecharam a cadeia dinástica do canal até
o início do próprio podcast.** O lote 102 esgotou a coleta em 19 vídeos
(não 25) — chegou ao Episódio 1 ("An Introduction", 2007), o primeiro
do podcast inteiro; não há como coletar mais para trás. Travados na
aprovação de 01/08/2026, depois da parada: 4 datações de risco
confirmadas (Yarmuk 636, conquista persa de Alexandria 619, revolta de
Vitaliano 513-515, Batalha de Dara 530) — todas bateram. 8 subtemas
novos incorporados, todos sob `Império Bizantino`: `Heráclio`, `Constans
II e Constantino IV`, `Justiniano II e a Anarquia`, `Sucessores de
Justiniano`, `Anastásio I`, e os interlúdios `O Império em 500/600/700`
— nenhum tema-raiz ou região nova. `Justiniano e Teodora` chegou a 20
vídeos. 1 bug de regex corrigido no `coletar.py` (estação do ano + ano
não capturada quando uma palavra separa a preposição do número — "By
**Spring** 542"), testado contra os casos reais antes de aceitar.
Decisão de `/encerrar` o canal deixada para o humano. Ver "Resolvidas
na aprovação dos lotes 100-102", acima.

**Os lotes 95-99 (125 linhas) formaram um ciclo esticado de cinco
lotes, não quatro** — a parada só rodou depois do 5º por decisão do
humano (continuar coletando antes de parar). Travados na aprovação de
01/08/2026: 5 datações de risco confirmadas por fact-check na parada
(Segundo Concílio de Niceia 787, Concílio de Hiéria 754, guerra civil
de Constantino V 741-743, assassinatos de Bardas/Miguel III por
Basílio I 866-867, morte do Tsar Simeão 927) — todas bateram. 10
subtemas novos incorporados, todos sob `Império Bizantino`: `Dinastia
Isáurica` (8), `Nicéforo I e a Crise Sucessória` (6), `Dinastia Amória`
(6), `Ascensão Macedônia` (4), `Romanos I Lekapeno` (6), `Focas e
Tzimisces` (14 no total), `Basílio II` (8) e os três episódios de
interlúdio `O Império em 800/900/1025` (5/8/8) — nenhum tema-raiz ou
região nova. Achado da parada: os subtemas dinásticos do canal formam
uma cadeia cronológica contínua e sem sobreposição, 717-1453 d.C.
inteiro. 6 pendências acumuladas de linhas já travadas sem subtema (não
corrigidas). Canal continua `em andamento`. Ver "Resolvidas na aprovação
dos lotes 95-99", acima.

**Os lotes 91-94 (100 linhas) fecharam o segundo ciclo completo de
quatro lotes do canal `The History of Byzantium Podcast`.** Travados na
aprovação de 01/08/2026, depois da parada: 1 datação confirmada por
fact-check pontual na aprovação (cerco de Dirráquio, 1107-1108); mais 4
datas de risco verificadas na parada (Manzikert 1071, Grande Cisma 1054,
golpe de Alexios I 1081, Niceia/Dorileia/Antioquia 1097-98) — todas
bateram. 5 subtemas novos incorporados, todos sob `Império Bizantino`:
`Dinastia Comnena` (20 vídeos, a maior estreia do canal), `Crise do
Século XI` (12), `Dinastia Angelo` (5), `Justiniano e Teodora` (3) e
`Perda da Anatólia` (3) — nenhum tema-raiz ou região nova. `Primeira
Cruzada` ganhou 12 vídeos numa janela só (18→30), quase toda a série
original do canal sobre a Primeira Cruzada, de uma época do podcast sem
o campo `Period:`, classificada inteiramente por conhecimento geral. 3
pendências: linhas já travadas dos lotes 90-91 que ficaram sem subtema
por terem sido classificadas antes dos termos existirem (2 de `Dinastia
Angelo`, 1 de `Justiniano e Teodora`). Canal continua `em andamento`. Ver
"Resolvidas na aprovação dos lotes 91-94", acima.

**Os lotes 87-90 (100 linhas) fecharam o primeiro ciclo completo de
quatro lotes do canal `The History of Byzantium Podcast`, adotado no
lote 87.** Travados na aprovação de 01/08/2026, depois da parada:
nenhuma datação corrigida — o fact-check verificou 4 datas de risco
(usurpação de Michael VIII Palaiológos, Quarta Cruzada, Balduíno I de
Flandres, cerco árabe a Constantinopla) e todas bateram. 2 subtemas
novos incorporados (`Dinastia Paleóloga`, 18 vídeos, e `Império de
Niceia`, 6 vídeos, ambos sob `Império Bizantino`), nenhum tema-raiz ou
região nova. Convenção de canal registrada: campo `Period: XXXX-YY` na
descrição tratado como confiança `alta` em toda a coleta. Canal com
proporção alta de `Extra` (56 de 100 linhas — entrevistas, Q&A,
retrospectivas e a série "goes to Istanbul" sobre sítios que sobrevivem
hoje). 2 pendências registradas: fronteira larga do subtema `Quarta
Cruzada` (1198-1261, bem além da cruzada em si) e o "Estado de Epiro" (2
vídeos, abaixo do piso de 3 para subtema). Canal continua `em andamento`.
Ver "Resolvidas na aprovação dos lotes 87-90", acima.

**Os lotes 85-86 (36 linhas) são o primeiro canal coletado por playlist
explícita, não por canal inteiro.** `coletar.py` ganhou o modo
`--playlist ID --nome "..."` porque a playlist "The History of Rome"
(Mike Duncan) está hospedada num canal do YouTube (`- Timaeus -`) com 225
vídeos sem nenhuma relação com história — coletar o canal inteiro traria
189 vídeos de ruído. A playlist tem 36 vídeos (753 a.C.-476 d.C.) e foi
esgotada nos dois lotes (85 com 25, 86 com os 11 finais); mini-ciclo de 2
lotes, mesmo padrão do Cambrian Chronicles. Parada formal rodou desta vez
(diferença do ciclo anterior): fact-check confirmou as datas de
"conhecimento geral" usadas para justificar fronteiras de tema (Batalha
de Adrianópolis 378 d.C., morte de Aécio 454 d.C., invasões de Átila
451-453 d.C.), sem exigir nenhuma correção de datação. 2 subtemas novos
incorporados (`Crise do Século III` e `Dinastia Constantiniana`, ambos
sob `Império Romano`), nenhum tema-raiz ou região nova. 1 bug de processo
achado no fluxo de gravação manual (linhas novas apensadas quebravam a
ordenação cronológica) — ver `protocolo.md`. Canal deixado `em andamento`
por decisão do humano ainda pendente de `/encerrar`; playlist já esgotada
(36/36), sem vídeo novo esperado a menos que o curador da playlist
adicione algum. Ver "Resolvidas na aprovação dos lotes 85-86", acima.

**Os lotes 83-84 (38 linhas) são um mini-ciclo de 2 lotes, não os 4 de
costume — o canal `Cambrian Chronicles` (adotado no lote 83, após o
encerramento do Historia Civilis) esgotou sua coleta (58 vídeos
percorridos, 0 novos) antes de fechar um quarto lote.** Travados na
aprovação de 31/07/2026, com fact-check substituindo a parada formal (que
não chegou a rodar): 2 datações corrigidas (`Kingdom of Ceredigion` e
`Dyfed`, ambas ajustadas para `920` — formação real do Reino de
Deheubarth, confundida na classificação original com outro evento).
Nenhuma confiança `alta` precisou ser rebaixada — as 2 linhas `alta` da
janela tinham número real narrando o evento na própria descrição. 2
subtemas novos incorporados (`Reino de Gwynedd`, sob `História de Gales`,
já com 6 vídeos; `Mitos de Wikipédia`, sob `Historiografia`, já com 3),
nenhum tema-raiz ou região nova. Achados e corrigidos dois bugs de
processo do `coletar.py` (lacuna de regex para duração por extenso;
`UnicodeEncodeError` ao imprimir título fora do cp1252 do console
Windows) — ver `protocolo.md`. Canal mantido `em andamento` por decisão
do humano, não encerrado, apesar de esgotado nesta coleta — pode ser
revisitado com `python coletar.py @CambrianChronicles`. Ver "Resolvidas na
aprovação dos lotes 83-84", acima.

**Os lotes 79-82 (79 linhas) fecharam o oitavo ciclo completo de quatro
lotes, o primeiro do canal `Historia Civilis`** (adotado no lote 79, após
o encerramento do Ancient Americas). Travados na aprovação de 31/07/2026,
depois da parada: 2 datações corrigidas por fact-check (`Bureaucracy in
Cleopatra's Egypt` alargada de 51-30 a.C. para 100-30 a.C.; nota da
`Lupercalia` corrigida, removendo uma alegação de folclore moderno sem
base documental) e 1 ambiguidade documentada sem correção (`Pontifex
Maximus`, 382 vs. 383 d.C., mantido 383). Nenhuma confiança `alta`
precisou ser rebaixada — **0 linhas `alta` na janela inteira**, porque o
canal não põe nenhuma data em descrição/tags (só boilerplate de
Patreon/links); todas as 79 linhas ficaram `média` (data só no título) ou
`chute` (sem nenhuma data). 5 temas novos incorporados, nenhum subtema ou
região nova. 4 sobreposições registradas, não resolvidas (cluster
institucional de `República Romana`, uso elástico de `Guerra Civil de
César`, crescimento de `Reino de Roma`, quarta aproximação de `Turquia`).
O lote 82 fechou com só 4 linhas — sinal de que o canal está perto do fim
do próprio arquivo, não um buraco de filtro; a próxima coleta pode vir
vazia. Ver "Resolvidas na aprovação dos lotes 79-82", acima.

**O lote 76 tem só 1 linha** — revisita pontual e incremental ao canal
Kings and Generals depois de encerrado (protocolo diz para não rodar
`coletar.py` nesse canal; a exceção não foi investigada a fundo, só
registrada aqui). **O lote 78 tem 23 linhas, não 25** — o canal Ancient
Americas só tinha 23 vídeos aprovados nessa varredura (63 percorridos, 0
Shorts/lives/exclusivos descartados nessa passada).

**Ancient Americas (lotes 77-78) foi o primeiro canal adotado cujo
domínio (arqueologia pré-colombiana) não tem nenhuma sobreposição com o
vocabulário existente — daí o salto de 31 temas novos em só 2 lotes**,
muito acima de qualquer ciclo anterior. 22 das 25 linhas do lote 77 e 22
das 23 do lote 78 não tinham nenhuma data na evidência
(título/capítulos/descrição/tags) — a maior concentração de `chute` já
vista num par de lotes — porque o formato do canal (documentário sobre
cultura/sítio arqueológico) narra civilizações inteiras, não eventos
datados. Ver "Resolvidas na aprovação dos lotes 76-78", acima.

**O lote 75 tem só 16 linhas** — o canal ficou sem vídeos novos para
aprovar nessa coleta (900 vídeos percorridos, só 16 aprovados). Não é um
buraco por filtro incorreto como os das lives; é o próprio canal
desacelerando conforme o `coletar.py` se aproxima do início do arquivo do
canal (vídeos de 2016-2017). **`0 revisar` no catálogo inteiro, mantido.**

**Os lotes 40-56 têm menos de 25 linhas porque as lives saíram.** Em 29/07/2026,
por observação do humano, descobriu-se que o `coletar.py` nunca filtrou
transmissão ao vivo — lacuna que não incomodava no Kings and Generals e que no
Thersites the Historian deixou passar **46% do coletado**: 202 linhas (15 do
lote 40, 187 dos lotes 41-56). Todas removidas, ids em `descartados.txt`, filtro
acrescentado ao `coletar.py` via `liveStreamingDetails`. **Os buracos nos lotes
são permanentes por decisão do humano — não recoletar para completá-los.** Ver
`protocolo.md`, "Lives entraram por 17 lotes sem ninguém notar".

O expurgo custou vocabulário: 14 temas desapareceram do catálogo inteiro
(`História dos videogames`, com 8 linhas, era o maior; também `Bad Movies`,
`Dinastia Plantageneta`, `Dinastia Valois`, `Game of Thrones`, `Titanic`,
`Steven Spielberg`, `John Carpenter`, `Arnold Schwarzenegger`,
`Teenage Mutant Ninja Turtles`, `Música dos Anos 1960`, `História da Líbia`,
`Guerra Mexicano-Americana`, `Guerra do Afeganistão`). Outros encolheram muito:
`Retrospectiva Anual` 16→1, `Cultura de internet` 13→1, `Guerra Civil Americana`
46→22, `Historiografia` 69→45. O rótulo `Aleatório`, criado no lote 40, ficou
com **1 linha** (`Mr. Hands`) — quase todo o material que o motivou era live.
As entradas da Lista C acima já foram regeneradas — na parada dos lotes 72-75 (ver Lista C, no topo do arquivo).

Os lotes 72-75 (91 linhas) fecharam o sétimo ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 01/08/2026,
depois da parada: subtema `Potências Neutras` adicionado à linha da Suécia
(lote 71, travada), fechando o grupo de 5 potências neutras da Segunda
Guerra (Suécia, Irlanda, Turquia, Suíça, Portugal). Fact-check por amostra
confirmou 3 datações sem divergência (Reino Ostrogodo, Reino Borgonhão,
Guarda Varegue) e uma quarta defensável com moldura alternativa (Espanha
Visigótica, 507 vs. 409 como marco inicial). Nenhuma confiança `alta`
precisou ser rebaixada nesta janela (21 linhas `alta`, todas com número
real narrando um evento na própria descrição). 12 temas novos incorporados
(`Rússia Medieval`, `Guerra Medieval`, `França Medieval`, `Canato Avar`,
`Idade das Trevas Global`, `Guerra Bizantino-Sassânida`, `Império
Sassânida`, `Reino Lombardo`, `Reino Visigodo`, `Reino Ostrogodo`, `Reino
Borgonhão`, `Cristianismo Primitivo`); nenhuma região nova. Duas
sobreposições registradas, não resolvidas: `França Medieval`/`Formação das
Monarquias Nacionais` (mesmo processo histórico, temas criados em janelas
de aprovação diferentes) e o cluster de 5 "reinos bárbaros pós-romanos".
Ver "Resolvidas na aprovação dos lotes 72-75", acima.

Os lotes 68-71 (100 linhas) fecharam o sexto ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 31/07/2026,
depois da parada: faixa de "16-Bit Wars Rehashed" estendida (1989-1996 →
1989-1997, descontinuação real do Sega Genesis). Fact-check por amostra
confirmou 4 datações sem divergência (civilização fenícia, Três Augustos e
Cinco Imperadores da China, civilização minóica, escândalo Enron). Nenhuma
confiança `alta` precisou ser rebaixada nesta janela (10 linhas `alta`,
todas com número real narrando um evento na própria descrição) — inclusive
as ~15 linhas "2020 genérico" de `Candidatos Derrotados` desta janela foram
conferidas e mantidas corretamente em `média`. 8 temas novos incorporados
(`Resenhas de ficção`, `História dos videogames` recriado, `Esportes`,
`Jogos retrô`, `Grécia Arcaica`, `Civilização Fenícia`, `Renascimento`,
`Formação das Monarquias Nacionais`); nenhum subtema ou região nova. Ver
"Resolvidas na aprovação dos lotes 68-71", acima.

Os lotes 64-67 (100 linhas) fecharam o quinto ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 31/07/2026,
depois da parada: subtema de `Sibyrtios` corrigido (`Segunda Guerra dos
Sucessores`, célula que tinha ficado vazia por engano na classificação
original), confiança de `Super Tuesday Predictions` (lote 60, linha travada)
rebaixada de `alta` para `média` com aprovação explícita do humano — "2020"
na descrição era rótulo genérico do ciclo eleitoral, não narração de evento
datado. Fact-check por amostra confirmou 2 datações sem divergência
(Antípatro Etesias/Últimos Antipátridas, Neolítico chinês pré-Xia) e achou
1 imprecisão pequena não corrigida (Alexandre I do Épiro, início real 343
a.C. vs. 350 a.C. usado). Nenhuma confiança `alta` precisou ser rebaixada
nesta janela (14 linhas `alta`, todas com número real na descrição). 3
subtemas novos incorporados (`Primeira Guerra dos Sucessores`, `Segunda
Guerra dos Sucessores`, `Bush 43 Still Sucks`); nenhum tema ou região nova.
Também travadas as 5 linhas residuais achadas na aprovação anterior
(lotes 44, 52, 58×2, 59) — catálogo volta a `0 revisar`. Ver "Resolvidas na
aprovação dos lotes 64-67", acima.

Os lotes 60-63 (100 linhas) fecharam o quarto ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 30/07/2026,
depois da parada: faixa de Egina estendida (800-480 a.C. → 800-431 a.C., ver
"Resolvidas na aprovação dos lotes 60-63"), correção de célula única
autorizada no Metellus Numidicus (lote 57, subtema `Guerra Jugurtina`
adicionado). Fact-check por amostra confirmou 4 datações sem divergência
(Halicarnasso, Frederico Guilherme I da Prússia, Império Aquemênida, Romanus
I Lecapenus/Constantine VII Porphyrogenitus). Nenhuma confiança `alta`
precisou ser rebaixada — a checagem linha a linha (9 linhas `alta` na
janela) não encontrou nenhuma inflada por título/tags. 4 temas novos e 4
subtemas novos incorporados; nenhuma região nova. Amostra de 5 linhas
apresentada ao humano e aprovada sem correção, com duas decisões de base
mais fraca sinalizadas explicitamente na apresentação (faixa de Marcus
Aurelius Cotta, bloco "A Charge to Keep" como Extra) — ambas mantidas como
estavam. Ver "Resolvidas na aprovação dos lotes 60-63", acima.

Os lotes 56-59 (91 linhas) fecharam o terceiro ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 30/07/2026,
depois da parada: fundação de Bizâncio corrigida (657 a.C. → 667 a.C., ver
"Resolvidas na aprovação dos lotes 56-59"), 4 confianças `alta` rebaixadas
para `média` por título/tags sem número na descrição — 3 delas de uma sessão
anterior (lote 57), achadas só porque esta parada reauditou toda linha `alta`
da janela, não só as classificadas na sessão atual — e 3 linhas reclassificadas
de `Aleatório` para `História dos Estados Unidos > Política` (previsões e
análises de um pleito real e datado, mesma regra das duas linhas irmãs do
lote 57). Fact-check por amostra confirmou 3 datações sem divergência
(Etruscos, João I Tzimisces, revolta de Hampsícora na Sardenha). 13 termos
novos incorporados: 7 temas e 6 subtemas, nenhuma região nova. Ver
"Resolvidas na aprovação dos lotes 56-59", acima.

Os lotes 52-55 (100 linhas) fecharam o segundo ciclo completo de quatro lotes
pós-adoção do Thersites the Historian. Travados na aprovação de 29/07/2026,
depois da parada: 3 correções — `DvkWMoIYd7s` (NES) reclassificado de
`Aleatório` para `História dos videogames` com período real, subtema `John D.
Hicks` revertido por violar o piso de 3+ vídeos em Historiografia, e
`Early Rome, Part IV` separado do resto da série para o tema novo `Reino de
Roma` (faixa lendária de Numa Pompílio, confiança `média`). Fact-check por
amostra confirmou 6 datações de risco sem divergência (Cartago, Basílio II,
Murena, Sherman, Chamberlain), com uma ressalva sem correção sobre o marco de
fundação do Império Corásmio (1077 vs. 1127 — mantido 1127, pela periodização
do próprio vídeo). Nenhuma confiança `alta` precisou ser rebaixada — a
checagem linha a linha não encontrou nenhuma inflada por título/tags/data
irrelevante neste ciclo, embora duas armadilhas novas desse tipo tenham sido
evitadas (ver `protocolo.md`, "Armadilhas conhecidas"). Ver "Resolvidas na
aprovação dos lotes 52-55", acima. A sobreposição `Guerra do Afeganistão`/
`Guerra Soviético-Afegã` foi registrada, não resolvida — mais uma instância da
classe "tema por era do mesmo conflito/país", que ganhará uma parada dedicada
própria (junto com Chechênia e Israel-Hamas/Hezbollah).

Os lotes 48-51 (100 linhas) fecharam o primeiro ciclo completo de quatro
lotes pós-adoção do Thersites the Historian. Travados na aprovação de
29/07/2026, depois da parada: 3 datações `chute` corrigidas por fact-check
(Reis Ágidas e Eurepôntidas de Esparta, Publius Popillius Laenas — ver
"Resolvidas na aprovação dos lotes 48-51"), 5 subtemas de `Historiografia`
com 1 vídeo só voltaram para sem subtema por um critério novo (3+ vídeos do
mesmo assunto para nomear subtema em `Historiografia`, mesmo raciocínio da
regra de tema-raiz biográfico), e um bug do `verificar.py` (traceback não
tratado quando `lote` vinha vazio) foi corrigido e testado. Nenhuma
confiança `alta` precisou ser rebaixada nesta rodada — a checagem linha a
linha (feita antes de cada resposta do `/lote`, desde a lição dos lotes
40-43) não encontrou nenhuma inflada por título/tags neste ciclo.

Os lotes 40-43 (100 linhas) são do canal **Thersites the Historian**, adotado
no lote 40 após o encerramento do Kings and Generals (ver `CLAUDE.md`).
Travados na aprovação de 28/07/2026, depois da parada de quatro lotes: 7
confianças `alta` infladas por título/tags foram rebaixadas para `média`, 2
subtemas duplicados foram unificados, 2 grupos de temas-raiz de 1 vídeo cada
foram fundidos (`Reinos pós-romanos da Britânia`, `História dos Estados
Unidos`), 1 subtema foi renomeado e 4 linhas saíram dele por contradizer a
própria faixa de anos, e um critério novo (`Aleatório` vs. histórico com tom
de humor) foi fechado e registrado. Ver "Resolvidas na aprovação dos lotes
40-43", acima.

Ordenação: `ano_inicio`, `ano_fim`, mês, dia. As duas últimas chaves entraram na
parada dos lotes 4-7, para desembaralhar os 12 episódios semanais da Frente
Oriental de 1941 e as 19 linhas da Guerra Russo-Ucraniana.

O lote 6 tem 24 linhas: `Zi8Fioe0YKU` era teaser de vídeo exclusivo e foi para
`descartados.txt`.

As linhas dos lotes 8 a 39 entraram travadas (`travado = sim`, `status = ok`)
após correção humana de confiança e conteúdo. Isso deixou de exigir `status =
revisar` para toda linha `média`/`chute`: o `verificar.py` aceita `status =
ok` quando `travado = sim` — confiança registra a origem da data, status
registra o fluxo, e um humano pode aprovar um palpite.

Os lotes 38-39 (50 linhas) foram travados na parada de 28/07/2026 — um
mini-ciclo de 2 lotes, não os 4 de costume, a pedido do humano — depois de
checagem de confiança `alta` linha a linha (nenhuma inflada), fact-check por
amostra (1 correção — ver "Resolvidas na parada dos lotes 38-39") e amostra de
5 linhas apresentada ao humano. As 37 linhas que chegaram `chute`/`média`
mantiveram a confiança como estava — só o `status` virou `ok` e o `travado`
virou `sim`.

**Nenhuma linha em `revisar`.** As 109 que estavam pendentes — 65 de antes do
lote 8, nunca vistas em parada nenhuma, e 44 vindas da reclassificação dos
Extras — foram revisadas numa passada avulsa em 28/07/2026, fora do ciclo de
lotes, porque o canal foi encerrado no lote 39 e a parada seguinte (lote 43)
nunca ia acontecer. Com o ciclo interrompido, o mecanismo de revisão morre
junto: **pendência amarrada a um loop que parou é pendência permanente.**

O que a passada encontrou:

- **66 divergências entre o texto `Ano` e `ano_inicio`/`ano_fim`** — defeito
  sistêmico que o portão não olhava, 54 delas criadas pela própria
  reclassificação dos Extras. Todas corrigidas; `verificar.py` ganhou a
  checagem. Ver `protocolo.md`, "`Ano` e `ano_inicio`/`ano_fim` discordando".
- **Clóvis** (`sQ728X06zhs`): `ano_fim` 509 → 511, o fim real do reinado.
- **Mani** (`J6XumIkJpcE`): tema `Império Bizantino` → `Império Otomano`, faixa
  1000..1834 → 1460..1834. O título e a nota da própria linha diziam que o foco
  era otomano; a faixa começava antes de os otomanos existirem.
- **Taiwan** (`AhwB0lMoPKQ`): `ano_fim` 1900 → 1895 (Shimonoseki), trocando um
  número redondo por um marco real. Segue sendo a faixa mais larga do catálogo,
  4895 anos, e segue `chute`.
- **Kupiansk** (`PV7iDgpcOaw`): `Mês` 9 → 10, aplicando a regra de que capítulos
  ganham de descrição.

As 109 foram travadas depois da amostra de 5 linhas ao humano, com `confianca`
intacta — 362 linhas seguem `chute` e continuam dizendo que são palpite.

**Ressalva registrada, não resolvida:** cinco linhas bizantinas compartilham a
faixa genérica 330..1453 (marinha, exército/etnias, diplomacia, guerras civis,
herança grega). É defensável, mas é um balde mais fraco que os demais Panoramas.
Estreitar exige recoletar a evidência dos vídeos.

**Segunda ressalva:** 34 linhas caem na banda de 200-299 anos, logo abaixo do
limiar do `Panorama`, e recebem rótulo de ponto médio enganoso — "The Entire
History of Prussia" (1618-1871) aparece como "1700 - 1800". Baixar
`LIMIAR_PANORAMA` para 200 pegaria essas 34. Não feito: 300 foi decisão do
humano.

Os `Extra` (67 no total) seguem a regra fechada na parada dos lotes 30-33
(recepção ou atemporal). Os lotes 30-43 somavam 18 (10 de recepção, 8
atemporais — línguas indo-europeias × 2, miscelânea de animais históricos,
sete maravilhas alternativas, "Is Mulan historical?", "Taking Out the Trash
8" sobre a Prússia, "The Great Sphinx, Erosion, and Dating", e o comparativo
"Loathsome Lickspittles"). Os lotes 52-55 sozinhos acrescentaram 22 (líquido,
após a correção de Early Rome Parte IV): séries de leitura comentada
inteiras ou parciais (`Early Rome` ×4, `H.G. Wells`, cujos episódios que
narram um período real ficaram com data — ver acima), o cluster `Taking Out
the Trash` (agora 6 vídeos no total), comparações atemporais cross-era
(`The Great Captains`, `Ides of March Special`, `Minor Historical Figures`,
`Military Blunders` ×3, `More Blood in the Snow`) e recepção pontual (`G.P.
Baker` ×2, `My Review of Graham Hancock's America Before`, `9/11, 20 Years
Hence`, `John D. Hicks`). Os lotes 60-63 acrescentaram mais 23: o cluster
`A Charge to Keep` inteiro (12 vídeos, tema novo, ver "Sobreposições ainda
por resolver" acima), 5 episódios adicionais de `H.G. Wells` (Rome and
Carthage, Early Thought, History of Japan, Napoleon Bonaparte, First and
Second Punic Wars), e 6 sem subtema — as duas introduções de série
(Napoleão, Sherman), duas leituras de Robert O. Paxton sobre a França de
Vichy (abaixo do piso de 3 para nomear subtema) e os dois primers
conceituais de causas da Primeira e Segunda Guerras Mundiais — todos
recepção/método, nenhum atemporal novo. Os lotes 64-67 acrescentaram mais 4:
a introdução da série sobre os Sucessores de Alexandre, uma resposta a
artigo de terceiro sobre hoplitas gregos (método, ver "Sobreposições ainda
por resolver"), um primer conceitual sobre a Era Neoliberal e a introdução
da série `Bush 43 Still Sucks` — todos recepção/método, nenhum atemporal. Os
lotes 68-71 acrescentaram mais 1: o segundo vídeo de `China antiga` não
conta aqui (tem data real); o único Extra da janela foi a introdução da
série "History of China". Os lotes 72-75 acrescentaram mais 4, todas
Historiografia: "HIS 2202 The Legacy of Rome" (aula conceitual), "The
Politics of Framing History" (método), "Dialogue between a Priest and a
Dying Man" (leitura de texto filosófico do Marquês de Sade) e "The Dark
Ages" (subtema já existente, 2º vídeo).

Os `Aleatório` (52 no total) são todos do canal Thersites the Historian. Os
lotes 40-43 somavam 4 (`Mr. Hands`, as duas partes de `Targaryen Rulers of
Westeros`, `John Carpenter Movies Tier-Ranking`). Os lotes 52-55 acrescentaram
17: tier-rankings de mídia (`Steven Spielberg`, `Arnold Schwarzenegger`,
`Música dos Anos 1960` — `NES` saiu dessa lista na correção da parada, ver
acima) e uma leva de streams/call-in shows de formato variado, inclusive um
(`Hq6d1PA9ZJ8`, "World War I: A General Overview") cujo título nomeia um
assunto histórico mas cuja descrição/tags batem, palavra por palavra, com as
de outro call-in show do mesmo lote — classificado pelo formato real, não
pelo título. **A contagem líquida caiu para 11** porque o expurgo de lives
(ver acima) removeu a maior parte desse material antes do lote 57. Os lotes
57-59 acrescentaram `Avisos do canal` (tema novo, 1 linha, lote 57) e
`Comentário Político Contemporâneo` (tema novo, 5 linhas: 2 no lote 58, 3 no
lote 59). Os lotes 60-63 acrescentaram mais 4: uma linha de `Comentário
Político Contemporâneo` ("The McGovern Myth", lote 60), duas de `Avisos do
canal` ("Channel Update", lote 61; "Summer 2019 Update", lote 63) e `Feel the
Chafe!` (tema novo `História alternativa`, lote 61, cenário eleitoral
contrafactual). Os lotes 64-67 acrescentaram mais 6: um ensaio de resposta a
editorial ("Response to Bolden Editorial", lote 64), uma atualização geral
de cobertura eleitoral (lote 65), duas de `Avisos do canal` (lote 65, lote
67), uma resposta a ranking da CNN e uma crítica a Warren Buffett (ambas
lote 67) — todas `Comentário Político Contemporâneo` ou `Avisos do canal`,
nenhum tema novo. Os lotes 68-71 acrescentaram um salto grande, 30 linhas:
16 de `Jogos retrô` (tema novo, playthroughs de Sega/SNES), 5 de `Resenhas
de ficção` (tema novo, livros e um filme), 6 de `Comentário Político
Contemporâneo`, 2 de `Avisos do canal`, 1 de `Esportes` (tema novo). Os
lotes 72-75 acrescentaram mais 5: 3 de `Jogos retrô` (mais playthroughs de
Sega Genesis), 1 de `Comentário Político Contemporâneo` (crítica ao livro
de Hillary Clinton) e 1 de `História alternativa` (cenário contrafactual de
D-Day, 2º vídeo do tema).

**Lotes 76-78 (49 linhas) travados na aprovação de 31/07/2026, depois da
parada — um mini-ciclo de 3 lotes, não os 4 de costume** (mesmo padrão
já usado para os lotes 38-39): a parada foi pedida com o lote 79 ainda
não coletado. Ver "Resolvidas na aprovação dos lotes 76-78", acima.

**Lotes 79-82 travados na aprovação de 31/07/2026** (ver "Resolvidas na
aprovação dos lotes 79-82", acima). Canal Historia Civilis encerrado em
seguida (79 linhas, lotes 79-82) — ver `canais.json`. **Lotes 83-84
travados na aprovação de 31/07/2026** (mini-ciclo de 2, ver "Resolvidas na
aprovação dos lotes 83-84", acima). **Próxima parada: após o quarto lote
do canal Cambrian Chronicles** (`em andamento`, esgotado na última coleta
— pode encerrar antes disso, se a próxima coleta vier vazia de novo).

Todos os `video_id` são únicos e estão preenchidos.
