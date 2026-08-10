---
description: Restaura a planilha a partir de um backup e confirma a integridade
---

Algo deu errado na última gravação. Restaure.

1. Liste os backups em `backups\` com data e hora
2. Me diga qual você vai usar e por quê — deve ser o **anterior** à rodada que
   falhou, não o mais recente
3. Copie por cima de `playlist-historia-v2.xlsx`
4. `python verificar.py` para confirmar que o estado restaurado está íntegro
5. Me diga quantas linhas voltaram e quais lotes existem agora

**Depois de restaurar, avise sobre isto:** os ids das linhas perdidas continuam
em `catalogados.txt`, então esses vídeos não voltam na próxima coleta. Se a
intenção é recatalogá-los, me pergunte antes — é preciso tirá-los desse arquivo
primeiro, e isso não deve ser feito por engano.
