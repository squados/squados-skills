# Fórmulas e conferência

Use ao criar ou corrigir cálculos, modelos e resumos.

Escolha fórmulas compatíveis com o aplicativo e o motor disponíveis. Na escrita por openpyxl, funções e separadores seguem a representação interna em inglês e vírgula; a interface pode exibir português. Não reescreva fórmulas existentes apenas por aparência. Deixe premissas de negócio em células reconhecíveis e mantenha referências coerentes ao copiar linhas.

Trate erros pelo significado: chave ausente pode pedir pendência; taxa zero informada é diferente de taxa em branco. `IFERROR(...,0)` é adequado apenas quando zero corresponde à regra. Não trunque saldo negativo nem converta toda ausência em zero. Fórmulas editáveis devem responder às entradas, sem totais congelados como valores quando atualização é necessária.

Exemplos de invariantes: caixa final = inicial + entradas − saídas, com abertura seguinte igual ao fechamento anterior; estoque = inicial + entradas − saídas + ajustes; cada transação conciliada usada uma vez. Comissões requerem base, situação elegível, vigência, faixa progressiva ou retroativa e arredondamento definidos. Teste abaixo/no/acima dos limites e cancelamento, ausência e zero. Em orçamento, explique sinal da variação e não trate aumento de despesa como favorável automaticamente.

Recálculo requer motor apropriado. openpyxl grava fórmulas, sem avaliá-las; resultados em cache podem faltar ou estar antigos. Existência do arquivo e exit code zero não comprovam novos valores. Quando possível, recalcule no aplicativo compatível, reabra resultados e compare células materiais com contas independentes. Altere uma entrada e confira a propagação esperada. Não destrua fórmulas para mostrar resultados.

Verifique totais por linha/grupo, referências, sinais, percentuais, datas e recursos afetados. Informe separadamente fórmula inspecionada, cálculo realizado, preservação e renderização; marque pendências concretas. A quantidade de conferências deve acompanhar o impacto do arquivo.
