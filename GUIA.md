# Guia de uso — catálogo de história

Este arquivo é para **você**, não para o Claude Code. O `CLAUDE.md` diz o que o
agente deve fazer; aqui está o que você digita e o que você olha.

Regra geral: você aprova, ele executa. Você não precisa entender de Python nem
abrir a planilha, exceto quando este guia disser para abrir.

---

## Rodar um lote

Abra o CMD, entre na pasta, abra o agente:

```
cd caminho\para\Historia-ano-a-ano
claude
```

Cole:

> Rode o próximo lote seguindo o CLAUDE.md. Backup antes de gravar, e não salve
> se o `verificar.py` falhar. No fim, me diga: quantas linhas entraram, quantas
> ficaram `revisar`, quais termos novos você propôs, e se alguma linha `alta`
> tem data citada fora da faixa que ela declara.

A última frase é a que mais importa. É o erro que já apareceu uma vez: marcar
confiança `alta` usando datas que estavam na descrição mas eram de **outro**
episódio — títulos de vídeos linkados, ou o bloco fixo que o canal repete em
toda a série.

### Os 30 segundos de conferência

Na resposta dele, olhe três coisas:

1. **"checklist passou"** com 0 falhas. Se falhou e ele salvou mesmo assim, veja
   *Desfazer* abaixo.
2. **A contagem fecha.** Linhas antes + 25 = linhas agora. Se o lote veio com
   menos de 25, ele deve explicar por quê.
3. **Confiança.** Se mais da metade das 25 vier como `alta`, desconfie e pergunte:

   > Para cada linha `alta` do lote, me mostre qual data da evidência caiu dentro
   > da faixa de anos que a linha declara.

Se as três estiverem bem, acabou. Não precisa abrir a planilha.

---

## A parada, a cada quatro lotes

Os lotes 9 e 10 correm normalmente. **No lote 11**, depois de rodar, cole:

> Agora faça a parada dos lotes 8 a 11: validação de vocabulário, fact-check por
> amostra das datações de maior risco, e sorteie 5 linhas dos quatro lotes com a
> evidência ao lado para eu conferir.

**As 5 linhas são a sua parte.** Leia a evidência ao lado da classificação e diga
"ok" ou aponte o erro. Cinco linhas a cada cem é o único momento em que alguém
de fora olha o resultado — sem isso, quem classifica, valida e aprova é a mesma
parte.

Depois de conferir, se estiver tudo bem:

> Aprovado. Trave as linhas dos quatro lotes, incorpore os termos novos ao
> vocabulario-canonico.md e atualize o Estado atual.

Aí começa o ciclo seguinte, e o próximo parada é no lote 15.

---

## Quando parar e perguntar

Chame ajuda se aparecer:

- **`verificar.py` falhando e ele insistindo em salvar.** É o único caso grave.
- **"linhas TRAVADAS alteradas"** no relatório. Significa que ele mexeu em
  trabalho já aprovado. Já aconteceu uma vez, por um bug de escrita do
  `openpyxl` — restaure do backup e não deixe passar.
- **Contagem que não fecha** sem explicação.
- **Termo novo que muda a estrutura**, não só acrescenta: fundir temas, renomear
  região existente, mexer na escada da Lista A.

O resto acumula até a parada. Termo novo estranho, faixa de anos larga demais,
subtema duplicado — nada disso justifica interromper.

---

## Desfazer

Toda gravação gera um backup em `backups\`. Para voltar:

```
dir backups
copy backups\playlist-2026-07-27-1636.xlsx playlist-historia-v2.xlsx
python verificar.py
```

Use o backup **anterior** à rodada que deu errado — o nome tem data e hora. Se o
`verificar.py` passar depois de restaurar, você está de volta ao estado bom.

Os ids do lote perdido continuam em `catalogados.txt`, então eles **não** voltam
na próxima coleta. Se quiser recatalogá-los, é preciso tirar as linhas
correspondentes desse arquivo primeiro.

---

## Situações normais que parecem erro

**"Nenhum video longo novo."** Você está em dia com o canal. Não é falha.

**"cota diária da API esgotada."** Reseta à meia-noite no horário do Pacífico
(4h ou 5h da manhã no Brasil). Só esperar.

**Muitos descartados numa rodada.** O lote 8 descartou 149 contra os ~25
habituais. São Shorts e exclusivos de membros acumulados naquele trecho do
catálogo. Vale conferir se o número disparar de novo:

> Dos descartados desta rodada, quantos foram Shorts e quantos foram
> exclusivos/teasers? Algum tinha mais de 10 minutos?

Vídeo longo descartado é o sinal de alarme — pode ser filtro pegando demais, e
id descartado não volta sozinho.

**Rótulo de período que soa errado.** Um vídeo sobre a Sardenha aparecer como
"Período homérico" é esperado, não bug. A Lista A é régua cronológica, não
descrição do assunto. Está explicado no `vocabulario-canonico.md` e não deve ser
"corrigido".

---

## Manutenção

**Backups.** Crescem uns 50 KB por rodada. Apague os antigos quando quiser, mas
guarde sempre pelo menos os dois últimos.

**A chave da API.** Vive em `%USERPROFILE%\.chaves\youtube.txt`, fora da pasta
do projeto, de propósito — assim ela nunca entra num commit. Dá para apontar
para outro lugar com a variável de ambiente `YOUTUBE_API_KEY_FILE`. Se a chave
algum dia aparecer no terminal ou numa resposta, troque a chave.

**Os `lote-NN.md`.** Não apague. O `coletar.py` usa a numeração deles para saber
qual é o próximo lote. Sem eles, a próxima coleta vira `lote-01.md` e sobrescreve.

**Quando o canal acabar.** Em algum momento o `coletar.py` vai parar de achar
vídeos novos. Aí é trocar `CANAL` no topo do arquivo por outro `@handle` e
recomeçar. O vocabulário e a planilha continuam os mesmos.

---

## Onde cada coisa mora

| Arquivo | Para que serve |
|---|---|
| `playlist-historia-v2.xlsx` | O catálogo. Fonte de verdade. |
| `CLAUDE.md` | Instruções para o agente. |
| `GUIA.md` | Este arquivo. Instruções para você. |
| `protocolo.md` | Manual detalhado: regras, decisões, armadilhas. |
| `vocabulario-canonico.md` | Listas fechadas de período, região, tema, subtema. |
| `verificar.py` | O portão. Reprova gravação com defeito. |
| `coletar.py` | Busca os vídeos novos e gera o `lote-NN.md`. |
| `catalogados.txt` | Ids já enviados. Evita recoleta. Não editar à mão. |
| `descartados.txt` | Shorts, exclusivos e teasers recusados. Cresce sozinho. |
| `backups\` | Cópias datadas. Sua rede de segurança. |
