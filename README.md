# História ano a ano

Um catálogo de vídeos de história do YouTube ordenados pelo período que o vídeo
**trata** — não pela data em que foi publicado.

O resultado é uma linha do tempo só, de 20000 a.C. até hoje, atravessando canais
diferentes. Um vídeo do Kings and Generals sobre a Batalha de Canas fica ao lado
de um do Magistra Vitae sobre a mesma guerra, mesmo tendo sido publicados com
seis anos de distância um do outro.

**Estado atual: 5.415 vídeos catalogados, de 20 canais, em 231 lotes.** Todos os
20 canais estão `encerrado` — ou seja, a coleta chegou ao fim do que cada um
tinha publicado.

---

## Por que isso existe

O YouTube ordena por data de publicação e recomenda por semelhança. Nenhuma das
duas coisas ajuda quem quer percorrer a história em ordem. Um canal bom de
história antiga publica um vídeo sobre a Suméria hoje e um sobre Napoleão na
semana que vem.

Este projeto resolve isso à mão, um vídeo por vez, com um protocolo escrito para
que a classificação seja repetível e auditável em vez de dependente do humor de
quem classificou.

## O que tem aqui

| Arquivo | O que é |
| --- | --- |
| `playlist-historia-v2.xlsx` | **O catálogo.** 5.567 linhas, 19 colunas. É o produto e a fonte de verdade. |
| `playlist-historia-v2.csv` | Espelho em texto do catálogo, para dar para ler e comparar aqui no GitHub. Derivado — gerado por `exportar_csv.py`, nunca editado à mão. |
| `protocolo.md` | O manual de operação: como datar, como classificar, como decidir confiança. Inclui a seção "Armadilhas conhecidas", que é o registro de todo erro já cometido e a lição tirada dele. |
| `vocabulario-canonico.md` | As listas fechadas de período, região, tema e subtema. Nada entra na planilha fora delas. |
| `canais.json` | Estado por canal: status, faixa de lotes, datas, e um campo `observacoes` longo com o histórico de cada um. |
| `coletar.py` | Puxa os vídeos novos de um canal pela YouTube Data API e monta o arquivo `lote-NN.md` para classificar. `--desde AAAA-MM-DD` restringe a coleta ao que foi publicado a partir de uma data. |
| `verificar.py` | O portão. Confere 10+ invariantes da planilha. Saiu diferente de 0, não se grava. |
| `playlist-historia-v3.xlsx` | **A ordem de exibição.** Derivada da v2 pelo `ordenar.py`, com as colunas `ordem`, `era`, `tipo` e `regiao_historica`. A v2 é o dado; esta é o produto para assistir. |
| `gravar.py` | Grava o lote classificado na v2: calcula os campos derivados, confere os ids contra o arquivo de lote e reordena a planilha pela chave completa. É o único script que escreve no catálogo. |
| `ordenar.py` | Deriva a v3. Agrupa por civilização enquanto as datas são largas e vira cronologia única em 500 a.C.; dentro de cada bloco o panorama abre, os eventos vêm por data e o temático fecha. Tem portão próprio: recusa gravar se a derivação sujar dado da v2. |
| `conferir_ordem.py` | Mede a ordem gerada contra uma planilha ordenada à mão — era, região, concordância de pares e sequência de blocos. |
| `auditar.py` | Auditoria de cobertura: varre a lista de uploads inteira de um canal e diz quantos vídeos o projeto nunca viu, separando o que é novo do que é buraco antigo. Somente leitura. |
| `consultar.py` | Procura um termo em Tema, Subtema e Título na planilha — o passo obrigatório antes de propor termo de vocabulário novo. |
| `amostra.py` | Sorteia as cinco linhas da parada de revisão, com semente fixa derivada dos lotes: o sorteio é reproduzível e não é escolha de quem apresenta. |
| `paradas/` | Os dossiês das paradas de revisão: vocabulário novo, fact-check com fonte, as cinco linhas sorteadas e as pendências abertas. |
| `Old_lote/` | Os lotes 0-230 já processados — a evidência bruta por trás de cada classificação. Os lotes 231-249 estão na raiz, ainda não arquivados aqui. |
| `CLAUDE.md` / `GUIA.md` | Instruções para o agente e para o humano, respectivamente. |
| `painel.html` | Visualização rápida do catálogo. |

## Como funciona o loop

```bash
python coletar.py @NomeDoCanal    # gera lote-NN.md com 25 vídeos
                                  # (classificar as 25 linhas)
python gravar.py classificacao.json lote-NN.md
python verificar.py --anterior backups/playlist-AAAA-MM-DD.xlsx
                                  # só grava se sair 0
python exportar_csv.py            # atualiza o espelho .csv antes do commit
```

A cada quatro lotes há uma **parada**: validação de vocabulário, fact-check por
amostra e cinco linhas sorteadas apresentadas a um humano com a evidência ao
lado. Essa última parte não é opcional — é o único ponto em que alguém de fora
olha o que foi produzido. Sem ela, quem classifica, valida e aprova é a mesma
parte.

## Regras de método

Três decisões definem o resto do projeto:

1. **A evidência é só o que a API oficial devolve** — título, capítulos,
   descrição e tags. Sem transcrição, sem raspagem, sem cookie de conta logada.
   Baixar legenda de terceiro exigiria OAuth do dono do vídeo; raspar o endpoint
   interno violaria os Termos de Serviço.
2. **Toda linha declara sua própria confiança** (`alta`, `média`, `chute`,
   `n/a`) e o que a sustenta. Uma data que veio de busca externa nunca é `alta`.
3. **Capítulos ganham de tags e de descrição** sempre que houver conflito.
   Canais reciclam blocos inteiros de descrição entre episódios — já apareceram
   tags de Vicksburg/1863 num vídeo sobre Atlanta/1864.

## Rodando por conta própria

Precisa de Python 3 e de uma chave da YouTube Data API v3.

```bash
pip install -r requirements.txt
```

A chave fica **fora da pasta do projeto**, num arquivo de texto com a chave e
nada mais:

- Padrão: `~/.chaves/youtube.txt` (no Windows, `%USERPROFILE%\.chaves\youtube.txt`)
- Ou aponte para outro lugar com a variável de ambiente `YOUTUBE_API_KEY_FILE`

Ela fica fora de propósito: assim não existe caminho pelo qual um commit
distraído a publique.

## Licença

O **código e a documentação** (`*.py`, `*.md`, `painel.html`) estão sob a
licença MIT — veja [LICENSE](LICENSE).

O **catálogo** (`playlist-historia-v2.xlsx` e os arquivos de lote) é
disponibilizado sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/):
use como quiser, inclusive comercialmente, desde que cite a fonte.

Títulos, descrições e demais metadados dos vídeos pertencem aos respectivos
canais e estão aqui apenas como referência e evidência de classificação. Este
projeto não é afiliado a nenhum dos canais catalogados nem ao YouTube.
