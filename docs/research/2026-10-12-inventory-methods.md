# Analista de Estoque — métodos profissionais e casos de avaliação

Pesquisa de 12/10/2026, rodada 20/33. Frente de métodos, complementar à comparação de skills de saldo/controle e cobertura/reposição. Este documento não repete a descoberta de pacotes nem cria a skill. Nenhum ERP foi instalado ou operado; não houve compra, ajuste de saldo, envio, conta nova ou acesso pago. Os exemplos abaixo são autorais e fictícios, destinados à avaliação futura.

## Resultado da pesquisa

Recomenda-se começar por uma análise explicável de saldo, disponibilidade e prioridades, com os dados que a pessoa já trouxe. Reposição quantitativa entra quando existem período, demanda e prazo suficientemente definidos. Fórmulas sofisticadas não compensam saldo errado, vendas censuradas por ruptura ou recebimento sem data firme.

A entrega padrão deve ligar cada ação sugerida à evidência: item/local/unidade, data de corte, saldo utilizável, compromissos, recebimentos por data, demanda observada ou estimada, cálculo e limitação. “Comprar 36 unidades sob o cenário informado” é diferente de afirmar que 36 constitui uma compra ótima ou garante atendimento.

## Fontes primárias efetivamente consultadas

Links são de origem. A pesquisa lê conhecimento para produzir síntese própria; não copia recursos para um pacote. Acesso público não concede automaticamente direito de redistribuição. Não são prescritas obrigações de órgãos públicos nem normas estrangeiras a uma PME brasileira.

| Fonte, autoria e data/versão | Alcance real da consulta | Contribuição → decisão |
|---|---|---|
| [Inventory on-hand list](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list), Microsoft Learn, Dynamics 365 Supply Chain Management; data editorial não visível na extração, consultado em 12/10/2026 | Texto da página e tabela de saldos; sem execução do ERP | Físico, reservado físico e disponível físico são distintos; pedidos recebíveis ainda não permitem separação física → adaptar o vocabulário ao sistema da pessoa e evitar somar trânsito ao disponível de hoje. Filtros/dimensões mudam agregações → manter SKU/local/lote pertinentes. |
| [Reserve inventory quantities](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities), Microsoft Learn; versão do produto acima, data não verificada | Texto de reservas e políticas; sem configuração do produto | Reserva pode atingir saldo físico ou recebimento futuro → conferir se a coluna já foi abatida antes de subtrair novamente. Aproveitar distinção; descartar instruções de configuração como requisito da skill. |
| [Inventory Management: Fundamental Concepts & EOQ](https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/120bf3cdc3e9b1947ae2a8d0a264d901_lect7.pdf), Chris Caplice/MIT, outubro de 2006 | PDF de 28 páginas acessível; leitura seletiva do texto, sobretudo páginas 5–20; metadado do buscador traz título incorreto, título interno confirmado | Distingue custos relevantes e pressupostos do EOQ → adaptar como referência sob demanda, conferir unidades e hipóteses. Não converter custos de exemplo em parâmetros padrão. |
| [Inventory Management: Probabilistic Demand](https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf), Chris Caplice/MIT, outubro de 2006 | PDF de 30 páginas acessível; texto seletivo das páginas 1–16; sem revisão integral de exercícios/figuras | Posição de estoque, revisão contínua/periódica, objetivos de custo/serviço e classes ABC → aproveitar escolha condicionada da política; não transformar regras práticas de classe em lei. |
| [Calculate Inventory with Precision — Even Amid Variability](https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/), Peter L. King, CSCP, e Courtney Bigler/ASCM, 21/09/2025 | Texto extenso retornado pela busca, incluindo variabilidade, serviço, sazonalidade e prazo; abertura direta falhou. Equações em imagens não foram lidas | Buffer depende de variabilidade e decisão de serviço; sazonalidade não deve virar apenas margem extra → aproveitar o raciocínio e usar MIT para equações. Não declarar artigo/figuras integralmente revisados. |
| [Forecasting: Principles and Practice, 3ª edição, §13.2](https://otexts.com/fpp3/practical.html#time-series-of-counts), Rob J. Hyndman e George Athanasopoulos, edição online; data pontual da seção não visível | Texto seletivo da seção de contagens/Croston e referências; sem execução de R/fable | Croston separa tamanho e intervalo entre demandas, mas tem viés conhecido e não fornece distribuição preditiva pelo modelo apresentado → adaptar a identificação da demanda intermitente; descartar uso automático do método como garantia de estoque de segurança. |
| [A Non-Parametric Approach to Stochastic Inventory Planning with Lost Sales and Censored Demand](https://www.columbia.edu/~th2113/files/DataLostSales_gg_submit.pdf), Woonghee Tim Huh e Paat Rusmevichientong, manuscrito de 06/01/2006 | PDF autoral público de 49 páginas; resumo e introdução, páginas 1–3, consultados. Provas/algoritmos não revisados integralmente | Vendas são limitadas pelo que estava disponível quando há perda de vendas → aproveitar cautela com censura. Não transpor convergência teórica, reposição instantânea ou algoritmo do artigo para uma operação real. |
| [Controle de estoques ABC](https://www.sebraeplay.com.br/content/controle-de-estoques-abc), Sebrae Minas/Sebrae Play, autoria individual não indicada, 14/02/2025 | Texto do artigo consultado, incluindo ranking e exemplo; não é um vídeo | Ranking depende do critério escolhido e o próprio texto rejeita corte rígido em 80/20 → adaptar para priorização brasileira em linguagem acessível; registrar base e fronteira de classe. |
| [Configure reordering rules — Odoo 18.0](https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/purchase/products/reordering.html?highlight=product+type), documentação oficial Odoo, versão 18.0; data editorial não visível | Texto retornado pela busca: mínimo/máximo, unidade e múltiplos; abertura direta falhou. Tentativa da versão 19.0 também falhou | Múltiplo pode ultrapassar máximo → aproveitar como exemplo de restrição comercial. Não afirmar que telas/campos de 18 existem em 19 nem recomendar ERP. |
| [Sebrae orienta sobre gestão de estoque para lucratividade empresarial](https://ba.agenciasebrae.com.br/cultura-empreendedora/sebrae-orienta-sobre-gestao-de-estoque-para-lucratividade-empresarial/), Milka Morais para ML Comunicação/ASN Bahia, 31/01/2025 | Texto completo da notícia; curso/ebook/vídeo mencionados não foram cursados/lidos/assistidos | Confirma foco em micro/pequenas empresas, organização, codificação, giro e inventário → referência de contexto, não evidência de eficácia nem validação do material indicado. |
| [FreshRetailNet-50K](https://arxiv.org/html/2505.16319v5), Wang e colaboradores, preprint iniciado em maio de 2025, versão 5 revisada em 18/06/2026 | Coordenação desta rodada consultou resumo e seletivamente introdução, §3.1, §4.1 e §6 do HTML; sem código, dataset inteiro ou experimentos executados | Dados de perecíveis chineses em março–junho de 2024, com anotações horárias de ruptura → separar venda observada, disponibilidade e estimativa de demanda. Período/contexto limitam generalização; não impor aprendizado de máquina nem transpor ganhos publicados para esta skill ou PME. CC BY 4.0 declarada para o dataset, sem redistribuição nesta pesquisa. |

### Materiais recentes e lacunas audiovisuais

As buscas cobriram fontes originais de ASCM, MIT, documentação de ERP, OTexts e Sebrae, com tentativas específicas de vídeos de estoque publicados em 2025–2026. Não se alega cobertura exaustiva.

O [Vídeo — Controle de Estoque](https://www.sebraeplay.com.br/content/video-controle-de-estoque), Sebrae Minas, com Cristiano Andrade, publicado em 22/01/2025, foi encontrado. Consultados apenas título, descrição, autoria e data na página; o conteúdo pede cadastro/login. Não houve transcrição nem audiovisual, e não há timestamps consultados. A descrição reforça adequação ao setor; não permite extrair um procedimento operacional. Horário difere entre busca e abertura; apenas a data é usada.

O [vídeo de planejamento para 2026](https://sebraepr.com.br/videos/como-revisar-2025-e-planejar-um-2026-de-crescimento-passo-a-passo-completo/), Sebrae/PR, tem duração declarada de 8:08 e menciona problemas de estoque na descrição. Foi consultada apenas a página/descrição, sem data de publicação confirmada, transcrição ou audiovisual. É periférico; descartar como base quantitativa. Não tratar o número 2026 no título como prova de publicação em 2026. Não foi encontrada nesta frente uma transcrição pública recente decisiva de estoque; a lacuna permanece explícita e é compensada por textos primários acessíveis, sem criar conta.

Tentativas de acesso ao antigo artigo Sebrae de giro e ao ebook de compras/estoque redirecionaram para uma página geral. Não foram contados como leitura atual. Certificações pagas ASCM/CPIM não foram acessadas e não constituem fundamentação integral deste dossiê.

## Decisões de método para a futura skill

### 1. Período, unidade e significado do saldo antes da métrica

Confirmar apenas lacunas que mudam a decisão: data/hora do saldo; período de movimentos e demanda; dias corridos ou dias de operação; unidade de compra e de controle; SKU/local; alcance de reservas, bloqueios e trânsito. Se o dado já está no arquivo, aproveitá-lo. Uma pergunta útil substitui um formulário fixo.

Definir físico como quantidade presente, disponível como parte utilizável ainda livre, reserva como compromisso identificado, e recebimento firme como entrada com quantidade/data suficientemente confirmadas. Mercadoria bloqueada ou em inspeção continua fisicamente presente, mas pode não estar disponível. A nomenclatura final depende do sistema da empresa. Não chamar recebido o que apenas foi pedido; não usar promessa sem data como cobertura firme.

Uma posição para reposição pode ser `físico utilizável + entradas firmes − compromissos pendentes`. Explicitar cada termo e impedir dupla subtração de reservas/backorders que representam a mesma demanda. A posição agregada precisa de uma projeção por datas quando um recebimento chega depois da ruptura. Saldo negativo é evidência a investigar, não quantidade que a skill corrige por conta própria. Referências: Microsoft e MIT probabilístico.

### 2. Giro, cobertura e ruptura medem coisas diferentes

Giro no período usa saída/consumo dividido pelo estoque médio compatível. Para visão financeira, CMV/estoque médio ao custo; não misturar faturamento a preço de venda com estoque ao custo. Para visão por SKU, unidades consumidas/unidades médias. Se só há saldos inicial/final, chamar a média de aproximação; amostras diárias ponderadas podem representar melhor sazonalidade e picos. Zero no denominador produz indicador indefinido, não infinito útil.

Cobertura de hoje usa saldo livre utilizável e taxa de demanda explicitamente definida; entradas futuras aparecem em projeção separada. Informar o horizonte observado e a base diária; não misturar média semanal com prazo em dias. Com demanda zero ou intermitente, “dias de cobertura” pode não ser interpretável. Dias sem vendas por indisponibilidade não demonstram ausência de procura. Referências: MIT, OTexts e manuscrito Columbia; fórmulas de relatório constituem síntese autoral dimensional.

Ruptura pode ser tempo sem disponibilidade, linhas não atendidas, unidades faltantes ou ciclos com falta. Cada indicador precisa de denominador e janela. Não inferir vendas perdidas exatas sem pedidos recusados, disponibilidade histórica ou modelo identificado. Separar observado, limite inferior e cenário estimado.

### 3. Política de reposição proporcional aos dados

Com prazo constante e demanda estável, um cenário determinístico permite necessidade durante prazo/revisão. Na revisão periódica, considerar o período de proteção `prazo de entrega + intervalo até a próxima revisão`; na contínua, o gatilho considera prazo. Com histórico curto, zeros intermitentes, promoções ou ruptura, apresentar cenários e lacunas em vez de ajustar silenciosamente um modelo.

Estoque de segurança depende de objetivo de serviço, erro de previsão durante o período de proteção, variação do prazo e pressupostos estatísticos. `z × desvio durante o prazo` não é a mesma coisa que `z × desvio diário`; multiplicar pela raiz do tempo exige condições de independência/estabilidade. Correlação, prazo dependente da procura, tendência e sazonalidade exigem tratamento próprio. Se faltam dados ou objetivo, buffer pode ser parâmetro de cenário informado, jamais “95% de serviço”, “30 dias” ou “20%” fabricados.

CSL é probabilidade de ciclo sem falta; fill rate é fração de volume atendida. Não usar o mesmo percentual/fator normal para ambos sem método apropriado. Médias de prazos precisam de origem e quantidade de observações, além de atrasos reais. Item crítico barato pode exigir mais atenção que item caro substituível. Referências: MIT probabilístico, ASCM e OTexts.

### 4. EOQ e custos: referência opcional

EOQ `sqrt(2 × D × K / H)` requer D e H no mesmo período, K por pedido e H por unidade por período, com hipóteses de demanda estável e custos relevantes. Não basta conhecer preço de compra para estimar H. Se faltam custo de pedir/manter, não calcular lote “econômico” preenchendo valores padrão. Descontos, mínimo de fornecedor, validade, caixa, capacidade e preço variável podem mudar a decisão. Usar EOQ como comparação, não mandato. Base: MIT aula 7.

### 5. Excesso, obsolescência e ABC contextual

Excesso é relativo ao alvo e horizonte escolhidos, considerando compras abertas e compromissos. Dias sem movimento são um alerta com período definido, não prova automática de obsolescência. Verificar validade, coleção/ciclo de vida, peça de reposição crítica, demanda sazonal, contrato, substituição e prazo. Valor de estoque parado é quantidade vezes custo informado; não é perda contábil reconhecida nem economia garantida.

ABC precisa declarar se o ranking é consumo anual a custo, receita, margem ou valor imobilizado. Um item que cruza a fronteira pode entrar em A ou B conforme política explicitada; não há necessidade de encaixar exatamente 80/15/5. Cruzar com criticidade e variabilidade sem criar uma matriz obrigatória para toda análise. Bases: Sebrae ABC e MIT probabilístico.

## Três casos autorais para avaliação futura

Os gabaritos foram recalculados com expressões próprias em PowerShell em 12/10/2026; nenhum script de terceiro foi executado. Esta é validação aritmética dos exemplos, não execução nem eficácia demonstrada de uma skill.

### Caso 1 — físico, reserva, bloqueio e trânsito por data

Pedido: “Posso prometer 100 unidades hoje? Quanto fica livre na próxima semana?” SKU único, unidade peça, corte D0 após movimentos. Físico 144; bloqueado por inspeção 12; reservado físico 36. Não há sobreposição entre bloqueio e reserva; as reservas não voltarão a ficar livres nesta projeção. Recebimento firme de 48 peças no começo de D4, outro pedido de 24 sem data confirmada. Demanda adicional livre do cenário: 8 peças/dia em D1–D7, excluindo as 36 já reservadas. Não há outro movimento.

Gabarito: físico utilizável 132; disponível livre hoje `144−12−36=96`. Faltam 4 para prometer 100 hoje. As 48 futuras não corrigem a falta imediata. Ao fim de D3, livre `96−3×8=72`; no começo de D4 após recebimento `72+48=120`; ao fim de D7 `120−4×8=88`. Pedido sem data firme fica fora da projeção confirmada. Posição livre incluindo somente entrada firme em D0 é 144, mas não se chama disponível físico. Se a pessoa quiser acrescentar a promessa de 100 ao cenário de saídas, deve ser incluída como compromisso adicional; os 88 calculados não contemplam essa nova promessa.

Avaliação futura: rejeitar promessa imediata de 100; não somar entrada atrasada; não retirar 36 duas vezes; informar datas/unidades; manter o pedido incerto visível. Falha crítica: afirmar 168 disponíveis hoje por somar todo trânsito, ou aprovar promessa com base na posição agregada.

### Caso 2 — janela curta e vendas censuradas

Pedido: “Essa média justifica repor só 8 peças?” Dez dias corridos de operação, vendas `[8,9,7,8,8,0,0,0,0,0]`; houve disponibilidade plena nos cinco primeiros e ruptura total nos cinco últimos. Saldo livre após recebimento emergencial no corte: 20. Fornecedor entrega no começo do quinto dia após a decisão, isto é, após quatro dias de consumo; revisão a cada três dias; lote múltiplo de 12, sem mínimo adicional. Sem pedidos pendentes. Custos e objetivo de serviço não informados.

Gabarito: 40 vendidos; média observada na janela 4/dia; média nos dias disponíveis 8/dia. A primeira descreve vendas realizadas; a segunda é apenas cenário condicionado aos dias disponíveis, não demanda verdadeira comprovada. Não estimar “40 vendas perdidas” como fato. Sob cenário constante explícito de 8/dia, proteção `4+3=7` dias, alvo sem buffer `7×8=56`, necessidade `56−20=36`, múltiplo de 12 mantém 36. Isso não garante atendimento: antes de a nova compra chegar, consumo de quatro dias é 32 e faltariam 12; saldo 20 cobre 2,5 dias. Ação proposta inclui tratar a janela de falta com recebimento antecipado/substituição/transferência a investigar; uma compra ordinária de 36 não resolve o intervalo.

Ao final dos sete dias, `20+36−56=0` apenas em uma conta agregada que supõe todo consumo atendido. Apresentá-la como controle aritmético, não trajetória viável: houve falta antes do recebimento. Recomendar 8 a partir de média censurada ou afirmar serviço garantido são falhas críticas. Variar cenário para 6/dia dá necessidade 22, arredondada a 24; ainda faltam 4 antes do recebimento. Não calcular desvio/serviço normal a partir dessa janela como política validada.

### Caso 3 — mínimo comercial, excesso e ABC sem dogma

Pedido: “Compro o lote do fornecedor? O que merece atenção primeiro?” Quatro SKUs; consumo dos últimos 12 meses com custo unitário constante informado, em reais. Item X: 240×20=4.800; Y: 60×20=1.200; Z: 30×20=600; W: 20×20=400. Total 7.000. X tem 18 livres, alvo operacional informado de 40, demanda de cenário de 2/dia, mínimo comercial de 120 por pedido e múltiplo de 12. Não há trânsito/compromissos. Validade restante de 30 dias. W é peça crítica sem substituta, usada em falha de máquina; essa criticidade foi informada pela empresa.

Gabarito: ranking financeiro X/Y/Z/W; participações 68,57%, 17,14%, 8,57%, 5,71%; acumuladas 68,57%, 85,71%, 94,29%, 100%. Se política de A incluir o item que cruza 80%, X e Y ficam A; se política exigir abaixo de 80%, apenas X fica A. Declarar escolha em vez de fingir classe universal. W segue prioridade técnica apesar de 5,71% do consumo financeiro.

Para X, necessidade ao alvo `40−18=22`; restrição comercial eleva pedido a 120 e saldo agregado pós-entrada a 138. São 98 acima do alvo, R$1.960 a custo informado; cobertura de cenário 69 dias. Se o lote entra imediatamente e todos os 138 têm a mesma validade restante de 30 dias, demanda constante consome 60 e sobram 78 no vencimento. Se lotes têm validades distintas, refazer por lote e ordem de saída; o enunciado não autoriza supor esse dado em uma planilha real. A recomendação é negociar fracionamento, outro prazo/fornecedor ou revisar o alvo com a pessoa. Não emitir compra nem declarar perda de R$1.960.

Subquestão independente de EOQ: para item não perecível, D=600 unidades/ano, K=R$45/pedido, H=R$3/unidade/ano, sem descontos/capacidade ou ruptura no modelo. EOQ `sqrt(18.000)=134,164...`; custo relevante no ótimo ≈ R$402,49/ano. Com mínimo de 240, custo `600×45/240 + 3×240/2 = 112,50+360 = R$472,50/ano`; aumento ≈ R$70,01/ano. Este mínimo é 240 nessa subquestão e não 120 do SKU X. Não extrapolar o cenário anual para o perecível nem chamar 134 viável se o mínimo é 240.

## Organização proporcional proposta

Núcleo conciso: reconhecer intenção de saldo, reposição ou priorização; usar dados existentes; esclarecer unidade/período/significado materialmente ausentes; selecionar abordagem; entregar decisão rastreável, cálculos e limites. Referências sob demanda: reconciliação/dimensões; reposição e serviço; demanda intermitente/censura; custos/EOQ; ABC/validade. Bibliografia e histórico permanecem neste dossiê.

Tabela pequena admite cálculo transparente sem script. Arquivo grande ou rotina recorrente pode justificar script próprio que valide colunas, unidades e cálculos; o benefício precisa superar custo de instalação/manutenção. Não pressupor Python, R ou biblioteca já instalada. Quando uma dependência for necessária, explicar finalidade e oferecer instalação simples assistida a quem não desenvolve, conforme autorização de execução do ambiente; manter alternativa utilizável quando possível.

Personalização do procedimento nasce de repetição observada e aceite da pessoa: dias úteis, critério de classe, unidades, fornecedores e formato de entrega. Quando recorrência ou atrito justificar, oferecer explicitamente adaptar a própria skill para esses pedidos, mostrando a mudança proposta e aguardando o aceite antes de incorporá-la. Não registrar uma hipótese de hoje como regra permanente. Não criar infraestrutura, monitoramento, compra automática ou integração de ERP como consequência da pesquisa.

## Evidência e pendências

- Fundamentação consultada e exemplos autorais recalculados: presentes neste documento.
- Vídeos recentes: páginas/metadata somente; nenhum audiovisual/transcrição validado nesta frente.
- Pacote executável, licença de recursos que eventualmente sejam copiados, compatibilidade no Studio e contratação: não avaliados aqui.
- Avaliação futura: executar os três casos com a skill criada, conferir cada saída contra os gabaritos e erros críticos, depois testar pedido real autorizado com dados da empresa. Medir se as ações propostas são utilizáveis e corrigir a skill com aceite; não usar acerto aritmético isolado como prova de desempenho operacional.
