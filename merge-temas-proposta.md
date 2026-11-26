# Proposta de fusão de temas — para você aprovar linha por linha

Saiu do cruzamento da sua planilha ordenada à mão com a v2.

> **Estado em 26/11/2026.** Você aprovou tudo, em duas mensagens. Está
> aplicado: **A1**, **R**, **A3** inteira e **metade da A2**. Não está:
> **um item da A2, a camada B inteira** e a lista de trabalho **C**.
>
> | | linhas | temas-raiz | igual ao seu, nos 290 |
> |---|---|---|---|
> | antes | — | 525 | 146/290 (50%) |
> | A1 + R | 155 | 512 | 227/290 (78%) |
> | A2 (metade) + A3 | 97 | 485 | 256/290 (88%) |
> | `Roma antiga` | 69 | **482** | **254/290 (88%)** |
>
> Nenhuma linha foi criada ou removida; `trechos contíguos` caiu de 2657 para
> 2610. A Lista C do `vocabulario-canonico.md` foi regerada e registra o
> detalhe de cada fusão.
>
> **O que eu segurei, e por quê** — os três contradizem as linhas reais, e o
> motivo por extenso está em `merges/a2-a3.json`, campo `nao_aplicado`:
>
> - **`Vida urbana` → `Império Hitita`** (A2, 10 linhas). As 10 são Hattusa,
>   Roma (3), Constantinopla (2), Atenas, Alexandria, Antioquia e Quioto. É
>   tema transversal de verdade, e só uma linha é hitita — a fusão jogaria
>   Quioto e Alexandria dentro de um tema de 2 linhas sobre os hititas.
> - **`Cultura material samurai` e `Marinha samurai` → `Jogos de samurai`**
>   (B, 13 linhas). O destino são 41 resenhas de videogame. Armadura, espada,
>   castelo e guerra naval samurai são história.
> - **Os quatro aspectos romanos** — `Exército Romano`, `Sociedade Romana`,
>   `Religião Romana`, `Comércio Romano` (B, 69 linhas). Este é o achado que
>   importa, e ele explica a camada B inteira: **o padrão de aspecto só
>   funciona quando o destino é o nome da civilização.** Deu certo em
>   `Sociedade Mesopotâmica` → `Mesopotâmia Antiga` e `Sociedade Egípcia
>   Antiga` → `Egito antigo` porque esses destinos são a civilização. Roma não
>   tem esse tema: só `República Romana` (383) e `Império Romano` (112), que
>   são fases políticas, e os quatro aspectos atravessam as duas —
>   `Religião Romana` vai de 753 a.C. a 305 d.C., `Sociedade Romana` são 20
>   linhas sem data. Rotular isso `República Romana` seria mentira no dado,
>   não só na ordem. **Você autorizou o caminho: criar `Roma antiga` como
>   tema-raiz neutro**, na forma de `Egito antigo` e `Grécia antiga`. As 69
>   linhas entraram ali, cada aspecto virando subtema. Feito.
>
> Então a **camada B não foi aplicada como estava escrita**: dos seis itens,
> quatro foram resolvidos por um destino que a tabela não tinha, e dois — os
> samurai — seguem fora. Ela foi construída de padrão de nome mais massa de
> linhas na mesma região, que é o mesmo defeito que me fez abandonar a camada
> de família de nome; ele sobreviveu ali porque a massa de linhas também é um
> sinal ruim. **Acrescentei três itens por conta própria e tive que voltar
> atrás:** `Triunfo Romano`, `Pomério Romano` e `Colonização Romana` também
> atravessam as fases, então pus os três em `Roma antiga` — e a aderência aos
> seus 290 caiu de 256 para 252, porque na sua fatia você **manteve** esses
> temas. Restaurei o backup e rodei só o que você aprovou. Está em
> `merges/roma-antiga.json`.
>
> Sobra a lista de trabalho **C**, que nunca foi proposta — é inventário.

Fusão aplicada **não perde informação**: o tema antigo vira o `Subtema`
da linha. É o que você fez nos 290 — Tema é a civilização, Subtema é o
detalhe.

As camadas estão separadas por **força da evidência**, não por gosto meu.
Aprove por camada se quiser ir rápido: A1 e R são as seguras.

| se tudo for aprovado | |
|---|---|
| temas-raiz | 525 → 479 |
| trechos contíguos na v3 | 2657 → 2627 |
| linhas afetadas | 344 |
| tema igual ao seu, nos 290 | 146/290 (50%) → 257/290 (89%) |
| idem, só com A1 aprovada | → 221/290 (76%) |

## A1 — você fez, com maioria clara  ·  ✔ APLICADA em 26/11/2026

Fusão aplicada por você em 2 ou mais linhas daquele tema, em 60% ou
mais das que revisou. É a camada com evidência direta e é a que eu
aplicaria sem hesitar.

| ok? | tema atual | passa a ser | linhas | você fez em |
|---|---|---|---|---|
|  | `Canaã Antiga` | `Religião e misticismo` | 22 | 10/13 |
|  | `Suméria Antiga` | `Mesopotâmia Antiga` | 19 | 8/10 |
|  | `Demonologia Ocidental` | `Religião e misticismo` | 19 | 8/8 |
|  | `Esparta` | `Grécia antiga` | 15 | 7/7 |
|  | `Assíria Antiga` | `Mesopotâmia Antiga` | 14 | 4/5 |
|  | `Sociedade Mesopotâmica` | `Mesopotâmia Antiga` | 9 | 4/4 |
|  | `Civilização Micênica` | `Grécia antiga` | 9 | 8/8 |
|  | `Democracia Ateniense` | `Grécia antiga` | 7 | 3/3 |
|  | `Colonização grega` | `Grécia antiga` | 6 | 5/6 |
|  | `Povos indígenas da América do Norte` | `Povos indígenas das Américas` | 5 | 3/3 |
|  | `Civilização Minoica` | `Grécia antiga` | 4 | 3/3 |
|  | `Índia antiga` | `Civilização do Vale do Indo` | 4 | 2/2 |
|  | `China antiga` | `China` | 4 | 4/4 |
|  | `Reino de Yamhad` | `Mesopotâmia Antiga` | 2 | 2/2 |
|  | `Comércio na Mesopotâmia Antiga` | `Mesopotâmia Antiga` | 2 | 2/2 |
|  | `Sociedade Egípcia Antiga` | `Egito antigo` | 2 | 2/2 |
|  | `Corinto` | `Grécia antiga` | 2 | 2/2 |

## A2 — você fez, por maioria simples  ·  ✔ `Babilônia Antiga` aplicada, `Vida urbana` segurada

Entre 50% e 60% das linhas revisadas. Vale conferir: pode ser que o
tema seja transversal e a decisão dependa do vídeo.

| ok? | tema atual | passa a ser | linhas | você fez em |
|---|---|---|---|---|
|  | `Babilônia Antiga` | `Mesopotâmia Antiga` | 24 | 6/11 |
|  | `Vida urbana` | `Império Hitita` | 10 | 1/2 |

## A3 — você fez, mas em uma linha só  ·  ✔ APLICADA em 26/11/2026

Evidência fraca por construção: havia um vídeo só daquele tema na sua
fatia. A maioria me parece certa — `Império Acadiano` em `Mesopotâmia
Antiga`, `Egina` e `Delfos` em `Grécia antiga` —, mas é palpite meu
sobre um caso único, não padrão medido.

| ok? | tema atual | passa a ser | linhas | você fez em |
|---|---|---|---|---|
|  | `Hermetismo` | `Religião e misticismo` | 37 | 1/1 |
|  | `Império Acadiano` | `Mesopotâmia Antiga` | 7 | 1/1 |
|  | `História dos Fantasmas` | `Religião e misticismo` | 5 | 1/1 |
|  | `Divino Feminino (Sophia e Shekhinah)` | `Religião e misticismo` | 2 | 1/1 |
|  | `Cultura do Cobre Antigo` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `Poverty Point` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `Basketmaker` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `História da Batata` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `História do Milho` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `História do Chocolate` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `Manejo do fogo indígena` | `Povos indígenas das Américas` | 1 | 1/1 |
|  | `Palestina antiga` | `Canaã Antiga` | 1 | 1/1 |
|  | `Povo hebreu` | `Religião e misticismo` | 1 | 1/1 |
|  | `Ugarit` | `Civilização Fenícia` | 1 | 1/1 |
|  | `Hititas` | `Império Hitita` | 1 | 1/1 |
|  | `Cultura Cicládica` | `Grécia antiga` | 1 | 1/1 |
|  | `Numismática Antiga` | `Grécia antiga` | 1 | 1/1 |
|  | `Curiosidades da História Chinesa` | `China` | 1 | 1/1 |
|  | `Tessália antiga` | `Grécia antiga` | 1 | 1/1 |
|  | `Atenas Antiga` | `Grécia antiga` | 1 | 1/1 |
|  | `Guerra Lelantina` | `Grécia antiga` | 1 | 1/1 |
|  | `Argos antiga` | `Grécia antiga` | 1 | 1/1 |
|  | `Egina` | `Grécia antiga` | 1 | 1/1 |
|  | `Samos` | `Grécia antiga` | 1 | 1/1 |
|  | `Halicarnasso` | `Grécia antiga` | 1 | 1/1 |
|  | `Delfos` | `Grécia antiga` | 1 | 1/1 |

## R — renomeação, não fusão  ·  ✔ APLICADA em 26/11/2026

Aqui o destino **não existe** como tema no catálogo: você não juntou
dois temas, deu outro nome ao mesmo assunto. Barato e seguro de
aplicar, e um deles corrige grafia (`Nurágica`, não `Nuráguica` — a
sua planilha tem o erro, a v2 está certa; confirme qual você quer).

| ok? | tema atual | passa a ser | linhas | você fez em |
|---|---|---|---|---|
|  | `Línguas indo-europeias` | `Línguas` | 3 | 2/2 |
|  | `Civilização Nurágica` | `Cultura Nuráguica` | 2 | 1/1 |
|  | `Impérios Berberes` | `Berberes` | 2 | 1/1 |
|  | `Povos do Zagros` | `Zagros` | 1 | 1/1 |
|  | `Civilização de Jiroft` | `Jiroft` | 1 | 1/1 |
|  | `Civilização do Oxus (BMAC)` | `Oxus` | 1 | 1/1 |

## B — padrão de aspecto  ·  ✖ NÃO APLICADA como estava; os 4 romanos foram resolvidos de outro jeito

> Os quatro aspectos romanos (69 linhas) não foram para `Império Romano` nem
> para `República Romana`, como esta tabela propunha. Em 26/11/2026 você
> autorizou criar **`Roma antiga`** como tema-raiz neutro, e eles entraram
> ali, cada um virando subtema: `Roma antiga > Exército Romano`, `> Sociedade
> Romana`, `> Religião Romana`, `> Comércio Romano`. Ver
> `merges/roma-antiga.json` e a regra de uso no `vocabulario-canonico.md`.
> Os dois itens samurai seguem sem aplicar.

`Sociedade X`, `Exército X`, `Comércio X` absorvidos por `X`, na mesma
região. Não é palpite sobre o assunto: o nome do tema já diz que ele é
um aspecto de outro, e é o que você fez com `Sociedade Mesopotâmica` e
`Sociedade Egípcia Antiga`. **Confira a direção**: pus `Exército
Romano` em `Império Romano` e `Religião Romana` em `República
Romana` porque é onde está a massa de linhas de cada um, mas os dois
atravessam República e Império.

| ok? | tema atual | passa a ser | linhas |
|---|---|---|---|
|  | `Exército Romano` | `Império Romano` | 32 |
|  | `Sociedade Romana` | `República Romana` | 20 |
|  | `Religião Romana` | `República Romana` | 13 |
|  | `Cultura material samurai` | `Jogos de samurai` | 11 |
|  | `Comércio Romano` | `Império Romano` | 4 |
|  | `Marinha samurai` | `Jogos de samurai` | 2 |

## C — Onde eu não arrisco palpite

Regiões com muitos temas de 1 ou 2 linhas. Fundir aqui é decisão
editorial sua: não tenho como saber se `Samos` deve virar subtema de
`Grécia antiga` ou seguir tema próprio. Listo para você decidir.

**Europa** — 18 temas de 1-2 linhas. Núcleo possível: `Escolástica Medieval` (149 linhas).  
  `Castelos Medievais`, `Cisma do Oriente e Ocidente`, `Crise Geral do Século XVII`, `Crise medieval`, `Duelos`, `Gauleses`, `Godos`, `Guerra Anglo-Francesa`, `Guerra dos Nove Anos`, `História da Bíblia`, `Julgamentos de animais`, `Liga Hanseática`, `Mercenários`, `Peregrinação Medieval` ...

**Anatólia** — 11 temas de 1-2 linhas. Núcleo possível: `Historiografia` (294 linhas).  
  `Credos e Confissões Cristãs`, `Estados Neo-Hititas`, `Frígia Antiga`, `Império Hitita`, `Império Seljúcida`, `Lícia Antiga`, `Lídios`, `Reino de Anitta (Precursor Hitita)`, `Reino de Urartu`, `Turquificação da Anatólia`, `Çatalhöyük`

**América do Norte** — 17 temas de 1-2 linhas. Núcleo possível: `Filosofia Africana` (131 linhas).  
  `Cahokia`, `Calusa`, `Chaco Canyon`, `Comanches`, `Doutrina Monroe`, `Espiritualismo Moderno`, `Esportes`, `Fraudes Financeiras`, `Guerra Fria`, `História dos videogames`, `Hohokam`, `Mormonismo`, `Pânico Satânico`, `Retrospectiva Anual` ...

**Japão** — 16 temas de 1-2 linhas. Núcleo possível: `Sengoku Jidai` (119 linhas).  
  `Ainu`, `Budismo no Japão`, `Cristianismo no Japão`, `Espadas militares japonesas`, `Família Imperial do Japão`, `Guerreiras Samurai`, `Jogos de tabuleiro e cartas`, `Lendas samurai`, `Ninjutsu`, `Reino de Ryukyu`, `Restauração Meiji`, `Sakoku`, `Sohei`, `Wakō` ...

**Mesopotâmia** — 17 temas de 1-2 linhas. Núcleo possível: `Cruzadas` (90 linhas).  
  `Anábase dos Dez Mil`, `Arameus`, `Cavaleiros Hospitalários`, `Cisma Sunita-Xiita`, `Conflitos no Oriente Médio`, `Dilmun`, `Ebla`, `Guerra Bizantino-Sassânida`, `Guerra Civil Síria`, `Guerra Irã-Iraque`, `Guerra do Iraque (2003)`, `História da Alimentação`, `Império Neo-Assírio`, `Magan (Magan/Makkan)` ...

**Rus** — 7 temas de 1-2 linhas. Núcleo possível: `Guerra Russo-Ucraniana` (98 linhas).  
  `Cossacos`, `Ibn Fadlan`, `Legião Tchecoslovaca`, `Levante de Khmelnytsky`, `Rus de Moscou`, `Rússia Medieval`, `Tempo das Perturbações`

**Global** — 12 temas de 1-2 linhas. Núcleo possível: `Avisos do canal` (90 linhas).  
  `Carros de Guerra`, `Catástrofe Climática de 536`, `Comentários sobre criação de conteúdo`, `Cultura de internet`, `Descolonização do Império Britânico`, `Era Vitoriana`, `Francis Drake`, `Grupo Wagner`, `Idade das Trevas Global`, `Meteoros na História`, `Mundo Medieval (Crusader Kings III)`, `Panorama de conflitos globais`

**Itália** — 11 temas de 1-2 linhas. Núcleo possível: `Renascimento` (145 linhas).  
  `Balestreiros Genoveses`, `Dinastia Médici`, `Erupção do Vesúvio (79 d.C.)`, `Guerras Galo-Romanas`, `Itália medieval`, `Querela das Investiduras`, `Reino Lombardo`, `Reino Ostrogodo`, `República de Veneza`, `Risorgimento`, `Samnitas`

**Germânia** — 13 temas de 1-2 linhas. Núcleo possível: `Reforma Protestante` (83 linhas).  
  `Arthur Schopenhauer`, `Ditmársia`, `Fugger`, `Germanos antigos`, `Guerra Franco-Holandesa`, `Guerras de Independência Suíça`, `Immanuel Kant`, `Jakob Böhme`, `Karl Marx`, `Reiters Negros`, `Revolução Alemã`, `Sigmund Freud e a Psicanálise`, `Suevos`

**Inglaterra** — 13 temas de 1-2 linhas. Núcleo possível: `História na cultura popular` (58 linhas).  
  `Anne Conway`, `As Origens do Gótico (Estética e Horror)`, `Austin Osman Spare`, `Guerra das Rosas`, `Icenos`, `Isaac Newton`, `Japoneses no exterior`, `Primeira Guerra dos Barões`, `Pseudociência e Conspirações`, `Rebelião Percy (1403)`, `Reforma Eleitoral de 1832`, `Revolta dos Camponeses de 1381`, `William Blake`

**Frância** — 6 temas de 1-2 linhas. Núcleo possível: `Revolução Francesa` (57 linhas).  
  `França Medieval`, `Gendarmes Franceses`, `Georges Bataille`, `Mosqueteiros do Rei`, `Rebeliões Huguenotes`, `Reino Borgonhão`

**China** — 9 temas de 1-2 linhas. Núcleo possível: `Dinastia Zhou` (60 linhas).  
  `China Moderna`, `Dezesseis Reinos`, `Dinastia Qin`, `Dinastia Tang`, `Grande Canal da China`, `Guerras do Ópio`, `Nanman`, `Política Chinesa Contemporânea`, `Puyi`

**Índia** — 9 temas de 1-2 linhas. Núcleo possível: `Filosofia Indiana` (56 linhas).  
  `Declínio do Budismo na Índia`, `Guerra Durrani-Marata`, `Guerras do Decão`, `Gurkhas`, `Império Gurida`, `Império Kushan`, `Império Marata`, `Império Mogol`, `Sultanato de Delhi`

**Estepe** — 7 temas de 1-2 linhas. Núcleo possível: `Império Mongol` (44 linhas).  
  `Canato Avar`, `Citas`, `Confederação Xiongnu`, `Cumano-Quipchaques`, `Estepe Eurasiática`, `Pechenegues`, `Tengrismo`

**Irã** — 6 temas de 1-2 linhas. Núcleo possível: `Império Aquemênida` (16 linhas).  
  `Exército Sassânida`, `Hashashins`, `Império Meda`, `Maniqueísmo`, `Revolução Iraniana`, `Zoroastrismo`

**Mesoamérica** — 8 temas de 1-2 linhas. Núcleo possível: `Revolução Mexicana` (27 linhas).  
  `Astecas`, `Calendário Mesoamericano`, `História da Pimenta`, `Tarascos`, `Teotihuacan`, `Teuchitlán`, `Toltecas`, `Zapotecas`

**Hispânia** — 7 temas de 1-2 linhas. Núcleo possível: `Segunda Escolástica` (14 linhas).  
  `Crise de 1383-1385`, `Emirado de Córdoba`, `Guerra Civil Espanhola`, `Inquisição Espanhola`, `Reino Visigodo`, `Tratado de Tordesilhas`, `Tércio Espanhol`

**Europa Central** — 9 temas de 1-2 linhas. Núcleo possível: `Grande Guerra do Norte` (10 linhas).  
  `Commonwealth Polaco-Lituano`, `Comércio de escravos eslavos`, `Exército Negro da Hungria`, `Guerra Polaco-Otomana`, `Hussardos Alados`, `Partições da Polônia`, `Polônia Piasta`, `Reino da Boêmia`, `Vampiros (Origens Históricas)`

**Bálcãs** — 7 temas de 1-2 linhas. Núcleo possível: `Miguel, o Bravo` (6 linhas).  
  `Guerra Gótica`, `Guerras Iugoslavas`, `Ilírios`, `Moldávia de Estêvão, o Grande`, `Primeiro Império Búlgaro`, `Segundo Império Búlgaro`, `Trácios`

**Andes** — 7 temas de 1-2 linhas. Núcleo possível: `Tiwanaku` (2 linhas).  
  `Chavín de Huántar`, `Império Wari`, `Moche`, `Muisca`, `Nazca`, `Quipu`, `Tiwanaku`

**Ásia Central** — 7 temas de 1-2 linhas. Núcleo possível: `Império Timúrida` (2 linhas).  
  `Grande Jogo`, `Guerra Soviético-Afegã`, `Império Corásmio`, `Império Gaznávida`, `Império Timúrida`, `Johannes Schiltberger`, `Sogdiana`

**Cáucaso** — 7 temas de 1-2 linhas. Núcleo possível: `Guerra Georgiano-Seljúcida` (2 linhas).  
  `Albânia Caucasiana`, `Genocídio Circassiano`, `Guerra Georgiano-Seljúcida`, `Guerras da Chechênia`, `Reino da Armênia`, `Reino do Bósporo`, `Segunda Guerra da Chechênia`


## O que eu tentei e descartei

**Casar temas por palavra em comum na mesma região.** Produziu lixo:
`Primeira Guerra Mundial ← Guerra de Sucessão Espanhola`,
`Dinastia Zhou ← Dinastia Han`, `Guerra Civil Americana ← Guerra
Fria`. 'Guerra' e 'dinastia' não dizem nada sobre o assunto. Método
abandonado — e é por isso que não existe uma camada cobrindo os 460
temas que você não revisou: para eles não há evidência, só analogia.

**Temas transversais sem destino único** — você dividiu caso a
caso, e quem decide é a região ou o subtema, não o tema:

- `Geografia Estratégica`: 3 de 7 revisadas iriam para `China`, o resto para outros destinos
