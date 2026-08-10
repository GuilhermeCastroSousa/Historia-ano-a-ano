---
description: Trava as linhas aprovadas e incorpora os termos novos ao vocabulário
---

As linhas dos últimos quatro lotes estão aprovadas. Agora:

1. **Backup** antes de qualquer escrita.

2. **Corrija** o que a parada apontou como erro — confiança inflada, tema que
   contradiz os anos da própria linha, faixa fechada em cima de evidência
   truncada. Corrija antes de travar: linha travada com erro dentro fica errada
   para sempre.

3. **Trave**: `travado = sim` e `status = ok` nas linhas dos quatro lotes.
   Mantenha `confianca` como está — ela registra de onde a data veio, não se a
   linha foi aprovada. Humano pode aprovar um palpite; o palpite continua palpite.

4. **Vocabulário**: regenere a Lista C do `vocabulario-canonico.md` a partir da
   planilha, acrescente as regiões novas à Lista B, e atualize o "Estado atual"
   com as contagens reais.

5. **Protocolo**: se a parada revelou armadilha nova, acrescente ao
   `protocolo.md`, seção "Armadilhas conhecidas".

6. `python verificar.py --anterior <backup>`. Não salve se falhar.
