# Demanda, serviço e custos

Leia para previsão, estoque de segurança ou EOQ. Preserve vendas, disponibilidade e registros faltantes. Quarenta vendidos em dez dias dão quatro por dia observado; se só cinco dias tinham disponibilidade, oito por dia disponível é proxy/cenário, sem provar demanda perdida exata. Promoção e sazonalidade mudam comparabilidade; demanda intermitente não recebe normalidade automática.

Previsão deve declarar horizonte, origem, dados conhecidos naquele instante e baseline. Compare nas mesmas datas e condições. Atualização diária não equivale a previsão de origem fixa de trinta dias. Erro de previsão positiva em dia de demanda zero continua erro; WMAPE soma erros absolutos e divide pela demanda total, ficando indefinido quando esse total é zero. Não exclua zeros para melhorar a métrica.

Estoque de segurança requer objetivo de serviço e variabilidade pertinentes. Probabilidade de não romper por ciclo e fração da demanda atendida são medidas distintas; meta de fill rate não vira diretamente quantil normal. Sob demanda independente por período e lead time fixo, desvio no prazo pode escalar com raiz do número de períodos; variabilidade do prazo exige outro modelo e hipóteses. Não aplique fórmula sem verificar unidade e validade.

EOQ = raiz de `2 × demanda anual × custo por pedido / custo anual de manutenção por unidade`, sob hipóteses de demanda estável, custo e reposição pertinentes. Não invente custos nem use doze períodos quando a base não é mensal. Custos zero/ausentes podem tornar cálculo indefinido. MOQ, desconto por faixa, validade e caixa exigem comparar lotes factíveis e custo total, não apenas arredondar o EOQ. Avaliação aritmética não demonstra política operacional ideal.
