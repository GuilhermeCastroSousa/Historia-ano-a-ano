"""
Ordena o catálogo para quem assiste, não para quem consulta.

A v2 é uma linha do tempo única por `ano_inicio`. Isso é correto como dado e
ruim como playlist: os 27 vídeos de Mesopotâmia Antiga aparecem em 16 trechos
separados, porque uma faixa de 7000 a.C. a 1365 a.C. se intercala com Egito,
Canaã e Grécia a cada degrau. Quem assiste em sequência não consegue seguir.

Este script produz a ordem de exibição a partir de três colunas novas —
`era`, `tipo` e `regiao_historica` — mais as que já existem. A ordem é
derivada, nunca escrita à mão: vídeo novo de lote cai no lugar certo sem
ajuste manual, e é isso que permite espelhar a playlist no YouTube.

O MODELO, EM UMA FRASE POR PARTE
────────────────────────────────
ERA — faixas largas (Lista A nova). O vídeo entra na era em que COMEÇA, não no
ponto médio. Uma faixa de 4200 a.C. a 2026 (Susa) é material da Antiguidade
remota, porque é lá que o assunto nasce.

TIPO — `Evento` (fato ou período curto), `Panorama` (apresenta uma civilização,
período ou assunto) e `Temático` (cultura, cidade, legado, religião, filosofia,
atravessa períodos). Dentro de um bloco: Panorama abre, Eventos no meio em
ordem cronológica, Temático fecha. "Short History of Ancient Egypt" antes das
dinastias; Tebas, Núbia e religião depois do último evento a que se referem.

REGIÃO HISTÓRICA — Mesopotâmia, Canaã, Anatólia, Magna Grécia, não Iraque,
Israel, Turquia. É a unidade de agrupamento antes da virada, e é por ela que os
27 vídeos de Mesopotâmia ficam juntos.

A VIRADA — até 500 a.C. a ordem agrupa por civilização, porque as faixas são
largas (mediana de 144 a 2784 anos por século, menos de 15% com faixa de até 25
anos) e não há como intercalar o que não tem data. De 500 a.C. em diante a ordem
é cronologia única, com Roma, Pérsia e China intercaladas por data, porque é ali
que a mediana da faixa cai abaixo de um século (79 anos) e um terço dos vídeos
já são eventos datados — em 300 a.C. a mediana é 4 anos e 71% são eventos. O
limiar está em `VIRADA`, e as medições que o justificam estão no protocolo.md.

Depois da virada ainda existem panoramas e temáticos: o panorama entra logo
antes do primeiro evento que cobre (âncora = `ano_inicio`) e o temático logo
depois do último (âncora = `ano_fim`). É o que mantém a coerência no trecho de
100 a 500 d.C., onde as faixas voltam a alargar.

Como usar:
    python ordenar.py                 # relatório, não escreve nada
    python ordenar.py --gravar        # gera playlist-historia-v3.xlsx
    python ordenar.py --conferir REF.xlsx   # mede contra uma planilha manual
"""

import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import openpyxl

from verificar import ABA, COLUNAS, PLANILHA

for _fluxo in (sys.stdout, sys.stderr):
    if hasattr(_fluxo, "reconfigure"):
        _fluxo.reconfigure(encoding="utf-8", errors="replace")

SAIDA = "playlist-historia-v3.xlsx"
COLUNAS_NOVAS = ["ordem", "era", "tipo", "regiao_historica"]

# ───────────────────────────── Lista A nova ─────────────────────────────
# Eras largas, pelo ano de INÍCIO. A v2 usava ponto médio e rótulo Panorama;
# aqui o rótulo é a era em que o assunto começa.
VIRADA = -500          # daqui em diante, cronologia única

ERAS = [
    (-10**9, -1100, "Antiguidade remota (até 1100 a.C.)"),
    (-1100,   -500, "Idade do Ferro (1100 a.C. - 500 a.C.)"),
    (-500,     500, "Antiguidade Clássica (500 a.C. - 500 d.C.)"),
    (500,     1500, "Idade Média (500 - 1500)"),
    (1500,    1800, "Era Moderna (1500 - 1800)"),
    (1800,   10**9, "Era Contemporânea (1800 - hoje)"),
]


def era_de(ano):
    if ano is None:
        return None
    for ini, fim, nome in ERAS:
        if ini <= ano < fim:
            return nome
    return ERAS[-1][2]


# ──────────────────── região histórica: tema manda, região v2 ajuda ─────────
# Aprendido da planilha de referência: o humano mapeia por CIVILIZAÇÃO (tema),
# não por país. 'Oriente Médio' da v2 se parte em Mesopotâmia (36 linhas) e
# Canaã (13) e o que decide é o tema.
REGIAO_POR_TEMA = {
    # Mesopotâmia e vizinhança
    "Suméria Antiga": "Mesopotâmia", "Babilônia Antiga": "Mesopotâmia",
    "Assíria Antiga": "Mesopotâmia", "Império Acadiano": "Mesopotâmia",
    "Império Neo-Assírio": "Mesopotâmia", "Sociedade Mesopotâmica": "Mesopotâmia",
    "Comércio na Mesopotâmia Antiga": "Mesopotâmia", "Reino de Yamhad": "Mesopotâmia",
    "Reino de Mitani": "Mesopotâmia", "Arameus": "Mesopotâmia",
    "Ebla": "Mesopotâmia", "Dilmun": "Mesopotâmia", "Magan (Magan/Makkan)": "Mesopotâmia",
    "Califado Abássida": "Mesopotâmia", "Rebelião Zanje": "Mesopotâmia",
    # Irã e Ásia Central
    "Elam Antigo": "Irã", "Povos do Zagros": "Irã", "Civilização de Jiroft": "Irã",
    "Império Meda": "Irã", "Império Aquemênida": "Irã", "Império Parta": "Irã",
    "Império Sassânida": "Irã", "Exército Sassânida": "Irã",
    "Império Afexárida": "Irã", "Revolução Iraniana": "Irã", "Zoroastrismo": "Irã",
    "Civilização do Oxus (BMAC)": "Ásia Central", "Sogdiana": "Ásia Central",
    "Império Timúrida": "Ásia Central", "Império Corásmio": "Ásia Central",
    "Império Gaznávida": "Ásia Central",
    # Egito e Núbia
    "Egito antigo": "Egito", "Sociedade Egípcia Antiga": "Egito",
    "Núbia": "Núbia", "Reino de Aksum": "Etiópia",
    # Levante. 'Canaã Antiga', 'Palestina antiga' e 'Povo hebreu' deixaram de
    # ser tema-raiz na fusão de 26/11/2026 e viraram subtema de 'Religião e
    # misticismo'; as entradas ficam porque agora é o subtema que resolve a
    # região (ver `regiao_de`). 'Religião Cananeia' entra pelo mesmo motivo —
    # nomeia a região no próprio nome.
    "Canaã Antiga": "Canaã", "Civilização Fenícia": "Canaã", "Ugarit": "Canaã",
    "Palestina antiga": "Canaã", "Povo hebreu": "Canaã", "Filisteus": "Canaã",
    "Religião Cananeia": "Canaã",
    "Cartas de Amarna": "Canaã", "Reino Himiarita": "Arábia",
    "Arábia Pré-Islâmica": "Arábia", "Expansão islâmica": "Arábia",
    "Revolta dos Macabeus": "Judeia", "Cerco de Jerusalém (70 d.C.)": "Judeia",
    # Anatólia
    "Império Hitita": "Anatólia", "Hititas": "Anatólia",
    "Reino de Anitta (Precursor Hitita)": "Anatólia",
    "Estados Neo-Hititas": "Anatólia", "Frígia Antiga": "Anatólia",
    "Lídios": "Anatólia", "Lícia Antiga": "Anatólia", "Halicarnasso": "Anatólia",
    "Reino de Urartu": "Anatólia", "Império Otomano": "Anatólia",
    "Turquificação da Anatólia": "Anatólia", "Império Seljúcida": "Anatólia",
    # Grécia
    "Grécia antiga": "Grécia", "Civilização Micênica": "Grécia",
    "Civilização Minoica": "Grécia", "Grécia Arcaica": "Grécia",
    "Período homérico": "Grécia", "Democracia Ateniense": "Grécia",
    "Atenas Antiga": "Grécia", "Esparta": "Grécia", "Corinto": "Grécia",
    "Argos antiga": "Grécia", "Tessália antiga": "Grécia",
    "Beócia antiga": "Grécia", "Egina": "Grécia", "Samos": "Grécia",
    "Delfos": "Grécia", "Guerras Médicas": "Grécia",
    "Guerra do Peloponeso": "Grécia", "Guerra Lelantina": "Grécia",
    "Religião Grega": "Grécia", "Macedônia Antiga": "Grécia",
    "Épiro antigo": "Grécia", "Cultura Cicládica": "Grécia",
    "Colonização grega": "Magna Grécia", "Reinos de Chipre": "Chipre",
    # Filosofia grega é material grego mesmo quando o filósofo é de Mileto:
    # o tema manda, não o lugar de nascimento. Sem isto os pré-socráticos
    # caíam na Anatólia e partiam o bloco grego em dois.
    "Pré-Socráticos": "Grécia", "Platão": "Grécia", "Aristóteles": "Grécia",
    "Filosofia Helenística e Romana": "Grécia",
    "Neoplatonismo Tardo-Antigo": "Grécia",
    # Religião e demonologia do Levante: o humano agrupa em Canaã, não na
    # Mesopotâmia, mesmo quando a v2 diz 'Oriente Médio'.
    "Demonologia Ocidental": "Canaã",
    "Divino Feminino (Sophia e Shekhinah)": "Canaã",
    "Manuscritos do Mar Morto (Qumran)": "Judeia",
    "Filosofia Judaica Medieval": "Judeia", "Judaísmo": "Judeia",
    "Guerras dos Diádocos": "Grécia", "Alexandre, o Grande": "Grécia",
    # Itália e Roma
    # 'Roma antiga' é o tema-raiz neutro, criado em 26/11/2026: recebe o que
    # atravessa Reino/República/Império ou não tem data. As entradas dos temas
    # de aspecto que ele absorveu ficam aqui de propósito — se um deles voltar
    # a aparecer num lote novo, a região já está resolvida.
    "Roma antiga": "Roma",
    "Reino de Roma": "Roma", "República Romana": "Roma",
    "Império Romano": "Roma", "Queda do Império Romano": "Roma",
    "Religião Romana": "Roma", "Sociedade Romana": "Roma",
    "Exército Romano": "Roma", "Comércio Romano": "Roma",
    "Pomério Romano": "Roma", "Triunfo Romano": "Roma",
    "Gladiadores": "Roma", "Colonização Romana": "Roma",
    "Herança de Roma": "Roma", "Etruscos": "Itália", "Samnitas": "Itália",
    "Civilização Nurágica": "Itália", "Itália medieval": "Itália",
    "República de Veneza": "Itália", "Reino Normando da Sicília": "Itália",
    "Guerras Italianas": "Itália", "Dinastia Médici": "Itália",
    "Papado": "Roma", "Renascimento": "Itália",
    # Norte da África
    "Cartago antiga": "Cartago", "Guerras Greco-Púnicas na Sicília": "Magna Grécia",
    "Impérios Berberes": "Norte da África", "Reino Vândalo": "Norte da África",
    "Sultanato Mameluco": "Egito", "Califado Fatímida": "Egito",
    # Europa
    "Celtas antigos": "Europa Celta", "Germanos antigos": "Germânia",
    "Bretanha Antiga": "Britânia", "Pictos": "Britânia",
    "Reinos pós-romanos da Britânia": "Britânia",
    "Inglaterra anglo-saxã": "Inglaterra", "História de Gales": "Gales",
    "Era Viking": "Escandinávia", "Harald Hardrada": "Escandinávia",
    "Império Franco": "Frância", "Declínio Carolíngio": "Frância",
    "Reino Lombardo": "Itália", "Reino Visigodo": "Hispânia",
    "Reino Ostrogodo": "Itália", "Reino Borgonhão": "Frância",
    "Reconquista": "Hispânia", "Emirado de Córdoba": "Hispânia",
    "Trácios": "Bálcãs", "Ilírios": "Bálcãs", "Dácios": "Dácia",
    "Eslavos": "Bálcãs", "Primeiro Império Búlgaro": "Bálcãs",
    "Segundo Império Búlgaro": "Bálcãs", "Império Bizantino": "Bizâncio",
    # Estepe
    "Citas": "Estepe", "Confederação Xiongnu": "Estepe", "Hunos": "Estepe",
    "Estepe Eurasiática": "Estepe", "Império Cazar": "Estepe",
    "Pechenegues": "Estepe", "Cumano-Quipchaques": "Estepe",
    "Império Mongol": "Estepe", "Canato Avar": "Estepe",
    "Tengrismo": "Estepe", "Rus de Kiev": "Rus", "Rus de Moscou": "Rus",
    # Ásia
    "China antiga": "China", "Dinastia Zhou": "China", "Dinastia Qin": "China",
    "Dinastia Han": "China", "Dinastia Jin": "China", "Dinastia Tang": "China",
    "Dinastia Qing": "China", "Dezesseis Reinos": "China",
    "Período dos Três Reinos": "China", "Nanman": "China",
    "Curiosidades da História Chinesa": "China", "China Moderna": "China",
    "Grande Canal da China": "China", "Taiwan": "Taiwan",
    "Civilização do Vale do Indo": "Índia", "Índia antiga": "Índia",
    "Filosofia Indiana": "Índia", "Império Kushan": "Índia",
    "Sultanato de Delhi": "Índia", "Império Mogol": "Índia",
    "Império Marata": "Índia", "Índia Britânica": "Índia",
    "Império Gurida": "Índia", "Siquismo": "Índia",
    "Formação do Japão Guerreiro": "Japão", "Sengoku Jidai": "Japão",
    "Xogunato do Japão": "Japão", "Budismo no Japão": "Japão",
    "Império Khmer": "Sudeste Asiático", "Império Majapahit": "Sudeste Asiático",
    # Américas
    "Povoamento das Américas": "Américas",
    "Povos indígenas da América do Norte": "América do Norte",
    "Cultura do Cobre Antigo": "América do Norte",
    "Poverty Point": "América do Norte", "Basketmaker": "América do Norte",
    "Hohokam": "América do Norte", "Chaco Canyon": "América do Norte",
    "Cahokia": "América do Norte", "Calusa": "América do Norte",
    "Comanches": "América do Norte", "Seminoles": "América do Norte",
    "Olmecas": "Mesoamérica", "Zapotecas": "Mesoamérica",
    "Toltecas": "Mesoamérica", "Astecas": "Mesoamérica",
    "Civilização Maia": "Mesoamérica", "Teotihuacan": "Mesoamérica",
    "Teuchitlán": "Mesoamérica", "Tarascos": "Mesoamérica",
    "Calendário Mesoamericano": "Mesoamérica",
    "Chavín de Huántar": "Andes", "Moche": "Andes", "Nazca": "Andes",
    "Tiwanaku": "Andes", "Império Wari": "Andes", "Quipu": "Andes",
    "Muisca": "Andes", "Marajoara": "Amazônia", "Tupinambá": "Amazônia",
    # Transversais que o humano manteve globais
    "Línguas indo-europeias": "Eurásia",
    "Colapso da Idade do Bronze": "Mediterrâneo",
    "Maravilhas do Mundo Antigo": "Mediterrâneo",
    "Biblioteca de Alexandria": "Egito",
    "Exploração Antiga": "Mediterrâneo",
}

# Quando o tema não está na tabela, a região v2 serve de ponte. Depende da era,
# porque 'Turquia' é Anatólia na Antiguidade e Império Otomano depois.
PONTE_REGIAO = {
    "Oriente Médio": "Mesopotâmia", "Levante": "Canaã",
    "Judeia": "Canaã", "Iêmen": "Arábia",
    "Egito": "Egito", "Sudão": "Núbia", "Irã": "Irã", "Cáucaso": "Cáucaso",
    "Turquia": "Anatólia", "Grécia": "Grécia", "Itália": "Itália",
    "Mediterrâneo": "Mediterrâneo", "Península Ibérica": "Hispânia",
    "França": "Frância", "Alemanha": "Germânia", "Áustria": "Germânia",
    "Suíça": "Germânia", "Países Baixos": "Países Baixos",
    "Inglaterra": "Inglaterra", "Escócia": "Escócia", "Irlanda": "Irlanda",
    "Gales": "Gales", "Dinamarca": "Escandinávia", "Suécia": "Escandinávia",
    "Noruega": "Escandinávia", "Hungria": "Europa Central",
    "Leste Europeu": "Europa Central", "Bálcãs": "Bálcãs",
    "Rússia": "Rus", "Ucrânia": "Rus", "Ásia Central": "Ásia Central",
    "Índia": "Índia", "Nepal": "Índia", "China": "China", "Taiwan": "Taiwan",
    "Japão": "Japão", "Coreia": "Coreia", "Indonésia": "Sudeste Asiático",
    "Sudeste Asiático": "Sudeste Asiático", "Melanésia": "Oceania",
    "Norte da África": "Norte da África", "África Ocidental": "África Ocidental",
    "África Oriental": "Etiópia", "África Austral": "África Austral",
    "Estados Unidos": "América do Norte", "América do Norte": "América do Norte",
    "México": "Mesoamérica", "América Central": "Mesoamérica",
    "Caribe": "Caribe", "Haiti": "Caribe", "Peru": "Andes",
    "Bolívia": "Andes", "América do Sul": "Amazônia", "Brasil": "Amazônia",
    "Europa": "Europa", "Europa Ocidental": "Europa",
    "Atlântico": "Oceanos", "Pacífico": "Oceanos", "Índico": "Oceanos",
    "Ártico": "Oceanos", "Global": "Global",
}

# Sequência do passeio geográfico, por era. É a informação que as colunas da
# planilha manual NÃO continham: nada nelas diz que Mesopotâmia vem antes de
# Irã, que vem antes de Egito. Sem esta lista a ordem não é reproduzível.
SEQUENCIA = {
    "Antiguidade remota (até 1100 a.C.)": [
        "Américas", "América do Norte", "Mesoamérica", "Andes", "Amazônia",
        "Mesopotâmia", "Irã", "Ásia Central", "Egito", "Núbia",
        "Crescente Fértil", "Canaã", "Arábia", "Anatólia", "Chipre",
        "Grécia", "Magna Grécia", "Mediterrâneo", "Itália", "Hispânia",
        "Europa", "Europa Celta", "Germânia", "Britânia", "Gales",
        "Escandinávia", "Estepe", "Índia", "China", "Taiwan", "Coreia",
        "Japão", "Sudeste Asiático", "Oceania", "Oceanos", "Eurásia",
    ],
    "Idade do Ferro (1100 a.C. - 500 a.C.)": [
        "Egito", "Núbia", "Etiópia", "Canaã", "Judeia", "Arábia",
        "Mesopotâmia", "Irã", "Anatólia", "Chipre", "Cáucaso",
        "Bálcãs", "Dácia", "Europa Central", "Grécia", "Magna Grécia",
        "Mediterrâneo", "Itália", "Roma", "Cartago", "Norte da África",
        "Hispânia", "Europa", "Europa Celta", "Germânia", "Britânia",
        "Gales", "Escandinávia", "Estepe", "Ásia Central", "Índia",
        "China", "Taiwan", "Coreia", "Japão", "Sudeste Asiático",
        "Américas", "América do Norte", "Mesoamérica", "Andes", "Amazônia",
        "Oceania", "Oceanos", "Eurásia",
    ],
}
# Depois da virada a sequência não é usada: a ordem é cronológica.
SEQUENCIA_PADRAO = SEQUENCIA["Idade do Ferro (1100 a.C. - 500 a.C.)"]

# ───────────────────────────────── tipo ─────────────────────────────────
LIMIAR_EVENTO = 60        # faixa de até 60 anos: cabe numa geração, é evento
TEMAS_TEMATICOS = {
    "Historiografia", "Geografia Estratégica", "Vida urbana", "Vida cortesã",
    "Evolução da guerra", "Origens da guerra", "Guerra Medieval",
    "História na cultura popular", "Resenhas de ficção", "Avisos do canal",
    "Cultura material samurai", "Sociedade Romana", "Comércio Romano",
    "Religião Romana", "Sociedade Mesopotâmica", "Sociedade Egípcia Antiga",
    "História da Alimentação", "História dos Feriados", "História da Arte",
    "Animais na história", "Línguas indo-europeias", "Maravilhas do Mundo Antigo",
    "Herança de Roma", "Jogos de estratégia", "Jogos de samurai",
    "Jogos retrô", "Jogos de tabuleiro e cartas", "Esportes",
    "História alternativa", "Cultura de internet", "Tratados militares",
    "Fortalezas", "Castelos Medievais", "Marinha", "Vida do Soldado",
    "Numismática Antiga", "Meteoros na História", "Exploração Antiga",
}
PISTAS_PANORAMA = ("panorama", "história d", "concise history", "complete history",
                   "full history", "introdu", "overview", "rise and fall",
                   "curso", "entire history", "who were")


def tipo_de(r):
    """Evento, Panorama ou Temático. Derivado — e é aqui que mora o risco:
    5.277 linhas nunca foram classificadas por tipo à mão."""
    if r["Século/Período"] in ("Extra", "Aleatório"):
        return "Temático"
    if r["Tema"] in TEMAS_TEMATICOS:
        return "Temático"
    largura = (r["ano_fim"] - r["ano_inicio"]) if r["ano_inicio"] is not None else None
    titulo = str(r["Título"] or "").lower()
    if largura is not None and largura <= LIMIAR_EVENTO:
        return "Evento"
    if any(p in titulo for p in PISTAS_PANORAMA):
        return "Panorama"
    if largura is not None and largura <= 300:
        return "Evento" if largura <= 120 else "Panorama"
    return "Panorama"


def regiao_de(r):
    t = r["Tema"]
    if t in REGIAO_POR_TEMA:
        return REGIAO_POR_TEMA[t]
    # A fusão de temas empurra o nome da civilização para o Subtema quando a
    # célula está vazia (ver `aplicar_merge.py`), então o subtema ainda carrega
    # o sinal que o tema perdeu: depois de `Canaã Antiga` ser fundida em
    # `Religião e misticismo`, é o subtema que diz Canaã. Sem este passo a
    # linha cai na ponte do `Oriente Médio` da v2, que só sabe apontar para
    # Mesopotâmia. Fica DEPOIS do tema de propósito: tema explícito ganha.
    s = r["Subtema"]
    if s in REGIAO_POR_TEMA:
        return REGIAO_POR_TEMA[s]
    return PONTE_REGIAO.get(r["Região"], r["Região"] or "Global")


# ──────────────────────────────── ordem ────────────────────────────────
RANK_TIPO = {"Panorama": 0, "Evento": 1, "Temático": 2}
INF = 10**9


def preparar(rows):
    for r in rows:
        r["era"] = era_de(r["ano_inicio"])
        r["tipo"] = tipo_de(r)
        r["regiao_historica"] = regiao_de(r)

    # TESTADO E DESCARTADO: fazer a era ser propriedade do bloco (região+tema)
    # em vez da linha, deixando só o Evento andar pela própria data. Parecia
    # ser o que a planilha manual fazia — a religião mesopotâmica de 1000 a.C.
    # está na Antiguidade remota dela, não na Idade do Ferro. Medido contra os
    # 290: a era caiu de 89% para 84% de acerto e a concordância de pares de
    # +0,643 para +0,590. A era é mesmo da linha. Não repita.
    # Linha sem data entra no bloco do assunto, não no fim. É a regra que tira
    # os 852 Extras do rodapé — e ela precisa do par (tema, região), não só do
    # tema: 'Historiografia' e 'Geografia Estratégica' têm linhas em todas as
    # eras, então herdar pela moda do tema jogava um vídeo sobre a arte da
    # Mesopotâmia na Era Contemporânea. Era o maior erro da primeira versão.
    por_par = collections.defaultdict(collections.Counter)
    por_regiao = collections.defaultdict(collections.Counter)
    por_tema = collections.defaultdict(collections.Counter)
    for r in rows:
        if r["era"]:
            por_par[(str(r["Tema"]), r["regiao_historica"])][r["era"]] += 1
            por_regiao[r["regiao_historica"]][r["era"]] += 1
            por_tema[str(r["Tema"])][r["era"]] += 1
    for r in rows:
        if r["era"] is not None:
            continue
        for fonte, chave_ in ((por_par, (str(r["Tema"]), r["regiao_historica"])),
                              (por_regiao, r["regiao_historica"]),
                              (por_tema, str(r["Tema"]))):
            if fonte.get(chave_):
                r["era"] = fonte[chave_].most_common(1)[0][0]
                break
        else:
            r["era"] = ERAS[-1][2]
    return rows


def chave(r, ancora_tema):
    """Antes da virada: era, passeio geográfico, bloco, tipo, data.
    Depois: cronologia única por âncora (ano_inicio, ou ano_fim no temático)."""
    era_ix = next(i for i, (_, _, nome) in enumerate(ERAS) if nome == r["era"])
    pos_era = next((i for i, (ini, fim, nome) in enumerate(ERAS)
                    if nome == r["era"]), 0)
    cronologico = ERAS[pos_era][0] >= VIRADA

    ai = r["ano_inicio"] if r["ano_inicio"] is not None else None
    af = r["ano_fim"] if r["ano_fim"] is not None else None
    if cronologico:
        if ai is None:
            ancora = ancora_tema.get(str(r["Tema"]), INF)
        elif r["tipo"] == "Temático":
            ancora = af if af is not None else ai
        else:
            ancora = ai
        return (era_ix, 0, 0, ancora, RANK_TIPO[r["tipo"]],
                ai if ai is not None else INF, str(r["Tema"]), str(r["Título"]))

    seq = SEQUENCIA.get(r["era"], SEQUENCIA_PADRAO)
    reg = r["regiao_historica"]
    # Global/meta abre a era; Global temático fecha.
    if reg in ("Global", "Mundo", "Eurásia") and r["tipo"] != "Temático":
        pos_reg = -1
    elif reg in ("Global", "Mundo"):
        pos_reg = len(seq) + 1
    else:
        pos_reg = seq.index(reg) if reg in seq else len(seq)
    bloco = ancora_tema.get(str(r["Tema"]), INF)
    return (era_ix, pos_reg, bloco, RANK_TIPO[r["tipo"]],
            ai if ai is not None else INF, af if af is not None else INF,
            str(r["Tema"]), str(r["Título"]))


def ordenar(rows):
    rows = preparar(rows)
    # Âncora do bloco: o primeiro evento do tema. Define onde o bloco entra.
    ancora_tema = {}
    for r in rows:
        if r["ano_inicio"] is None:
            continue
        t = str(r["Tema"])
        ancora_tema[t] = min(ancora_tema.get(t, INF), r["ano_inicio"])
    saida = sorted(rows, key=lambda r: chave(r, ancora_tema))
    for i, r in enumerate(saida, 1):
        r["ordem"] = i
    return saida


def carregar():
    ws = openpyxl.load_workbook(PLANILHA, read_only=True)[ABA]
    it = ws.iter_rows(values_only=True)
    cab = list(next(it))
    return [dict(zip(cab, r)) for r in it if r[cab.index("video_id")]]


def portao(rows, originais):
    """A v3 é derivada: o portão dela não repete as checagens do verificar.py,
    confere que a derivação é fiel. Nada de dado novo entra aqui.

    O `verificar.py` continua sendo o portão da v2, que segue sendo a fonte de
    verdade e segue ordenada por `ano_inicio`. Esta planilha é a camada de
    apresentação, e só pode errar de duas formas: perder/alterar dado da v2, ou
    produzir uma ordem inválida."""
    falhas = []
    if len(rows) != len(originais):
        falhas.append(f"{len(originais)} linhas na v2, {len(rows)} na v3")
    antes = {r["video_id"] for r in originais}
    depois = {r["video_id"] for r in rows}
    if antes != depois:
        falhas.append(f"ids diferentes: faltam {sorted(antes-depois)[:5]}, "
                       f"sobram {sorted(depois-antes)[:5]}")
    orig = {r["video_id"]: r for r in originais}
    mexidas = [r["video_id"] for r in rows
               if r["video_id"] in orig
               and any(r[c] != orig[r["video_id"]][c]
                       for c in ("Ano", "ano_inicio", "ano_fim", "video_id",
                                 "Link", "publicado", "lote"))]
    if mexidas:
        falhas.append(f"dado da v2 alterado em {len(mexidas)} linha(s): "
                       f"{mexidas[:5]}")
    if [r["ordem"] for r in rows] != list(range(1, len(rows) + 1)):
        falhas.append("coluna 'ordem' não é 1..n sem furo")
    for campo in ("era", "tipo", "regiao_historica"):
        vazias = [r["video_id"] for r in rows if not r.get(campo)]
        if vazias:
            falhas.append(f"'{campo}' vazio em {len(vazias)} linha(s): {vazias[:5]}")
    tipos = {r["tipo"] for r in rows} - set(RANK_TIPO)
    if tipos:
        falhas.append(f"tipo fora da lista: {sorted(tipos)}")
    return falhas


def gravar(rows, originais):
    falhas = portao(rows, originais)
    if falhas:
        print(f"\n{len(falhas)} FALHA(S) — não gravei {SAIDA}:\n")
        for f in falhas:
            print(f"  - {f}")
        sys.exit(1)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = ABA
    colunas = COLUNAS_NOVAS + COLUNAS
    ws.append(colunas)
    for r in rows:
        ws.append([r.get(c) for c in colunas])
    wb.save(SAIDA)
    print(f"\nportão da derivação: passou")
    print(f"{SAIDA}: {len(rows)} linhas, {len(colunas)} colunas.")


def relatorio(rows):
    print(f"\n{len(rows)} linhas ordenadas")
    print("\nera                                        linhas  Evento Panorama Temático")
    for _, _, nome in ERAS:
        sel = [r for r in rows if r["era"] == nome]
        if not sel:
            continue
        t = collections.Counter(r["tipo"] for r in sel)
        print(f"{nome[:42]:<42} {len(sel):>6}  {t['Evento']:>6} {t['Panorama']:>8} "
              f"{t['Temático']:>8}")
    blocos = sum(1 for a, b in zip(rows, rows[1:])
                 if (a["regiao_historica"], a["Tema"]) != (b["regiao_historica"], b["Tema"]))
    print(f"\ntrechos contíguos (região+tema): {blocos + 1}")
    print(f"regiões históricas em uso: {len({r['regiao_historica'] for r in rows})}")


def main():
    originais = carregar()
    rows = ordenar([dict(r) for r in originais])
    relatorio(rows)
    if "--conferir" in sys.argv:
        from conferir_ordem import conferir
        conferir(rows, sys.argv[sys.argv.index("--conferir") + 1])
    if "--gravar" in sys.argv:
        gravar(rows, originais)
    else:
        falhas = portao(rows, originais)
        print(f"\nportão da derivação: {'passou' if not falhas else 'FALHOU'}")
        for f in falhas:
            print(f"  - {f}")
        print("(nada gravado; use --gravar para gerar " + SAIDA + ")")


if __name__ == "__main__":
    main()
