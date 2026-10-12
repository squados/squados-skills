# Analista de Logística: métodos profissionais, transporte e acompanhamento

Pesquisa em 12/10/2026 para uma futura skill de negócios, de uso interno. Este documento cobre transporte, cotação de frete, capacidade, janelas, expedição, comprovação de entrega, desempenho e retorno. A comparação de skills existentes e a redação do pacote pertencem às outras frentes da pesquisa.

## Conclusão para o desenho

O padrão recomendado é analisar um pedido concreto com os dados disponíveis, reconstruir os eventos e comparar alternativas viáveis. A entrega deve permitir que uma pessoa confira a conta e a decisão: unidades, origem do dado, fórmula, compromisso de prazo, restrição física, custo incluído, lacuna e responsável pela próxima providência. Uma planilha ou tabela simples pode bastar. Não há fundamento nesta pesquisa para exigir WMS, TMS, implantação de padrões GS1 ou transporte internacional em todo pedido.

Os indicadores precisam de uma definição acordada com a operação. Percentual de pedidos, de linhas e de unidades responde a perguntas diferentes. A entrega pode estar informada pela transportadora e ainda carecer de comprovação ou conferência de quantidade. Uma devolução pode estar fisicamente recebida e continuar sem inspeção, sem liberação para venda ou sem resolução financeira.

Essas são decisões de desenho autorais. As fontes abaixo informam os componentes; não demonstram a execução de uma skill.

## Alcance e acesso real

Foram selecionadas 12 referências nesta frente: nove fontes profissionais/documentais e três materiais de vídeo/webinar de 2025–2026. Houve leitura do texto de quatro páginas profissionais, leitura de trechos do PDF GS1 e consulta a extratos indexados de três páginas SCOR. APQC ficou em acesso parcial. Nos materiais audiovisuais, foi lida uma transcrição completa publicada junto ao vídeo GS1; dois ficaram limitados à página de apresentação. Nenhum audiovisual foi assistido, nenhuma conta foi acessada e nenhuma cobrança foi autorizada.

Consultas priorizaram GS1, ASCM/SCOR, transportadoras oficiais, ICC e APQC, em inglês, português e material primário em dinamarquês. Buscas de 2025–2026 trouxeram também temas amplos de automação e mercado internacional; eles foram usados para delimitar o escopo, sem transformar a função em especialista de todas as cadeias. Não se alegou cobertura de toda a internet.

Todas as URLs foram consultadas ou tentadas em 12/10/2026. Data de rastreamento do motor de busca e copyright de rodapé não são datas de publicação.

### Registro de fontes

| ID | Fonte, autoria e URL | Data/versão verificável | Acesso efetivo e licença | Contribuição e decisão |
|---|---|---|---|---|
| M01 | GS1 AISBL, [GS1 Logistic Label Guideline](https://ref.gs1.org/guidelines/logistic-label/) | O endereço de referência retornou release 1.3, ratificado em jul/2019, 58 páginas. Não tratá-lo como edição de 2026. | Texto extraído do PDF: capa, histórico, escopo e identificação. Expedição/recebimento: extrato indexado da versão HTML da mesma obra; abertura direta retornou 403. Tentativa posterior de trechos do PDF retornou timeout. Não foi feita inspeção visual de todas as páginas. Copyright GS1 e política de propriedade intelectual no documento; nenhuma licença aberta de redistribuição verificada. | Identificar unidade logística separadamente do produto; conectar carga física e aviso de expedição. Adaptar a operações que já usam GS1. Não copiar exemplos de etiquetas nem impor adesão. |
| M02 | ASCM, [SCOR RL.1.1 Perfect Customer Order Fulfillment](https://scor.ascm.org/performance/reliability/RL.1.1) | Página sem data de revisão verificada. Código atual observado no extrato indexado. | Extrato indexado extenso da fonte primária consultado; abertura direta devolveu HTML de iframe sem corpo útil. Não houve leitura integral do padrão. Licença aberta não verificada. | Pedido perfeito considera os componentes de cada linha, inclusive documentação e condição. Aproveitar a distinção conceitual; evitar chamar OTIF de pedido perfeito. |
| M03 | ASCM, [SCOR RL Level-3 Metrics](https://scor.ascm.org/performance/reliability/RL.3.1) | Sem data de revisão verificada. | Extrato indexado da fonte primária; corpo direto não capturado. Licença aberta não verificada. | Acurácia de item e quantidade e definições dependentes da data solicitada/comprometida ajudam a especificar denominadores e tolerâncias. Adaptar, identificando a convenção local. |
| M04 | ASCM, [SCOR RS Level-3 Metrics](https://scor.ascm.org/performance/responsiveness/RS.3.111) | Sem data de revisão verificada. | Extrato indexado extenso; página direta sem corpo útil. Licença aberta não verificada. | Separa ciclos de separação, embalagem, carregamento, transporte, recebimento e retorno. Aproveitar decomposição; não reproduzir catálogo ou prometer conformidade SCOR integral. |
| M05 | DHL Global Forwarding, [Calculating Chargeable Weight by Air, Ocean, Road and Rail](https://www.dhl.com/gb-en/home/global-forwarding/freight-forwarding-education-center/calculating-chargeable-weights.html) | Sem data de publicação/revisão visível verificada. Região da página: Reino Unido. | Texto do artigo consultado. Licença aberta não verificada. | A regra de peso tarifável varia por modalidade e serviço; no rodoviário, consultar transportadora e região. Aproveitar método de conferir a cotação. Descartar divisor universal. |
| M06 | FedEx, [Can I get a proof of delivery?](https://www.fedex.com/en-es/customer-support/faq/receiving/tracking-questions/fedex-proof-of-delivery.html) | Sem data de revisão visível. Página para Espanha, em inglês. | Texto da FAQ consultado; nenhum rastreio de cliente consultado. Copyright FedEx; licença aberta não verificada. | A prova disponível pode conter assinatura, imagem ou dados limitados; detalhes dependem de conta/serviço. Adaptar a distinção entre status e evidência. Não exportar requisitos dessa região para o Brasil. |
| M07 | Correios, [Logística Reversa](https://www.correios.com.br/enviar/encomendas/logistica-reversa) | Sem data de revisão visível; página corrente consultada. | Corpo da página lido. Não foi acessado o sistema de emissão. Licença aberta de redistribuição não verificada. | O serviço depende de contrato do vendedor e autorização; custo e validade são condições do serviço. Referência sob demanda para retorno por Correios no Brasil; não confundir com prazo jurídico do consumidor. |
| M08 | International Chamber of Commerce, [Incoterms and Commercial Contracts: Incoterms 2020 Q&A](https://library.iccwbo.org/clp/clp-incoterms-qa-2020.htm?AGENT=ICC_UK) | Referência explícita a Incoterms 2020; sem revisão datada visível. | Texto público de orientação consultado. Não houve acesso ao livro integral/licenciado. Material protegido da ICC; não incorporar tabelas ou redação das regras. | Incoterms alocam obrigações, risco e custos quando incorporados ao contrato; não definem transferência de propriedade e não substituem contratos de venda/transporte. Usar somente quando o pedido trouxer esses termos. |
| M09 | APQC, [Percentage of orders delivered complete and on time (OTIF)](https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/percentage-orders-delivered-complete) | Sem data/revisão verificada. | Título e referência pública localizados; uma abertura retornou página, tentativas de recuperar o corpo útil falharam por timeout. Definição integral, benchmarks e permissões não foram verificados. | Corrobora a existência do indicador nomeado, sem sustentar uma fórmula específica ou meta. Não copiar benchmark, nem alegar que o método APQC foi integralmente lido. |
| V01 | GS1 Denmark, [Bliv klog på GS1-128 pallelabels og SSCC](https://live.gs1.dk/bliv-klog-pa-gs1-128-pallelabels-og/) | 12/03/2026 visível na página. Idioma: dinamarquês. | Página e transcrição completa publicada consultadas. Sem timestamps na transcrição. Audiovisual não assistido. Licença aberta não verificada. | Exemplo didático do fabricante de geleia: identificação do produto, unidade logística e aviso digital que é confrontado no recebimento. Adaptar o raciocínio, sem reutilizar personagem, vídeo ou roteiro. |
| V02 | ASCM, [ASCM's 2025 Top 10 Trends](https://mylearning.ascm.org/course/info.php?id=394) | Tema/ano 2025; data de publicação não verificada. Página informa duração de 3.570 segundos. Autores: Matt Talbert, Armand van Oostrom, Amy Augustine e Ulf Suerig. | Página de catálogo e biografias lidas. Conteúdo assinalado como reservado a membros; nenhuma transcrição ou audiovisual acessado. Todos os direitos reservados na página. | Mostra profissionais e escopo de tendências, mas não prova um método operacional. Manter como descoberta/lacuna; não recomendar blockchain, IA ou sistema por conta da ementa. |
| V03 | DHL Global Forwarding, [Air & Ocean Freight Market Updates, H1 2026](https://go.freightforwarding.dhl.com/market-update-webinars-h1-2026) | Sessões de air freight anunciadas para 18/03/2026. | Página pública de inscrição/ementa lida. Sem inscrição, gravação, transcrição ou audiovisual. Licença aberta não verificada. | Exemplo de atualização contextual de mercado, útil somente se modal/rota forem pertinentes. Página promocional não é prova de taxa, capacidade real ou desempenho de transportadora. |

Falha adicional de acesso: o [PDF ASCM de introdução de 2025](https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf) apareceu na busca, mas a abertura retornou 403. Não se utilizou esse PDF como documento integralmente lido nem se contou como uma décima terceira fonte selecionada. O [guia GS1 antigo em HTML](https://www.gs1.org/standards/gs1-logistic-label-guideline/1-3) foi descoberta da mesma obra M01, sem contagem independente.

## Decisões aplicáveis à futura skill

| Componente profissional | Contribuição | Aproveitar, adaptar ou descartar | Decisão para negócios em geral |
|---|---|---|---|
| Identificação GS1, M01/V01 | Liga unidade física a documentos/eventos. | Adaptar. | Usar identificadores existentes de pedido, linha, remessa, volume e lote. Explicar SSCC apenas quando a operação já usar ou pedir compatibilidade. |
| Expedição confirmada, M01 | Aviso precisa corresponder ao que realmente carregou. | Aproveitar. | Separar planejado, separado, embalado, carregado e expedido. Conferir faltas/volumes no evento efetivo, preservando evidência. |
| Pedido perfeito, M02 | Condição e documentação somam requisitos ao prazo/quantidade. | Adaptar. | OTIF e pedido perfeito aparecem como medidas diferentes. Uma entrega no prazo pode falhar em avaria ou documento. |
| Ciclos por etapa, M04 | Permite localizar espera e processamento. | Aproveitar. | Definir início/fim de cada tempo e separar preparação, espera da coleta, trânsito e recebimento. Não atribuir todo atraso à transportadora. |
| Peso tarifável, M05 | Compara massa, volume e regra contratada. | Aproveitar. | Conferir unidade, conversão, fator, arredondamento, mínimo e base de adicionais por cotação; capacidade física continua usando grandezas físicas. |
| POD regional, M06 | Evidência muda por serviço/conta. | Adaptar. | Registrar qual comprovante existe, o que confirma e qual lacuna permanece. Não inventar assinatura ou disponibilidade. |
| Retorno pelos Correios, M07 | Emissão/autorização e postagem são eventos distintos. | Sob demanda. | Aplicar só ao contrato pertinente; análise e minuta não emitem autorização nem garantem coleta. |
| Incoterms, M08 | Responsabilidade contratual e risco não são sinônimos de posse ou propriedade. | Sob demanda. | Se houver termo, conferir versão, lugar nomeado e contrato; não encaixar automaticamente uma venda doméstica em FOB/CIF. |
| Benchmark/OTIF APQC, M09 | Nomenclatura profissional. | Descartar benchmark não acessado. | Calcular com definição local explícita, sem metas automáticas ou comparação entre populações diferentes. |
| Tendências e webinars, V02/V03 | Atualização potencial de cenário. | Manter como lacuna. | Só acrescentar inteligência de mercado quando ajudar a escolha do pedido atual e a informação puder ser efetivamente consultada. |

## Método autoral para transporte e frete

1. Identificar a decisão: escolher uma cotação, explicar custo, viabilizar uma entrega, priorizar expedição ou investigar atraso. Aproveitar dados já enviados e perguntar apenas o que muda o resultado.
2. Fixar a unidade de trabalho: pedido, carga, remessa ou viagem; origem/destino; quantidade de volumes; dimensões externas com unidade; peso bruto; unidades por caixa; restrições de empilhamento ou manuseio quando relevantes.
3. Reconstruir a disponibilidade: quando a mercadoria fica pronta, tempo de carregamento, horário limite da coleta, janela no destino, calendário explicitamente fornecido e prazo realmente prometido. Distinguir previsão de compromisso confirmado.
4. Normalizar cada cotação: moeda, validade, modalidade/serviço, base de cobrança, fator volumétrico, arredondamento, frete mínimo, adicionais, tributos incluídos/excluídos e condições de nova tentativa. Não comparar preço por kg com preço por viagem antes de calcular o total do mesmo pedido.
5. Verificar viabilidade antes de ordenar por preço: peso bruto, cubagem, posições de pallet quando aplicáveis, não empilhamento, dimensões de acesso, janela, coleta disponível e documentação efetivamente exigida. Uma capacidade declarada apenas em kg não prova que a carga cabe em volume.
6. Comparar alternativas viáveis e mostrar custos conhecidos e condicionais separadamente. Custo esperado de falha só entra com probabilidade/evidência fornecida, identificado como cenário. Não somar um custo máximo hipotético como se fosse cobrado.
7. Entregar recomendação verificável, alternativa e lacunas que poderiam mudar a escolha. A pessoa responsável confirma disponibilidade/contrato antes de contratar ou despachar.

Inferência operacional de M05: usar o maior entre massa e peso volumétrico é pertinente quando a cotação determina essa regra. O artigo DHL distingue exemplos por modalidade e cálculo por contêiner em FCL. Portanto, a fórmula não deve ser aplicada a qualquer transporte; os coeficientes ilustrativos do artigo não substituem a cotação brasileira.

## Expedição, evidência e acompanhamento

O mínimo útil para reconstruir uma ocorrência é: identificador de pedido/linha/remessa, quantidade pedida, quantidade expedida, quantidade recebida quando conhecida, compromisso original e eventuais revisões com motivo, horário de coleta/carregamento/saída/entrega, fonte de cada evento e referência do comprovante. O dado bruto fica preservado; correções e deduplicações são explicadas.

A contribuição GS1 é ligar unidade logística ao conteúdo e ao aviso de expedição. A orientação menciona registrar unidades efetivamente carregadas e confrontar o aviso com o recebimento. Isso informa a conferência, sem fazer de uma leitura de código prova automática da quantidade interna ou da condição da mercadoria. [M01](https://ref.gs1.org/guidelines/logistic-label/)

Na análise, apresentar a condição confirmada: entregue com comprovante, entregue informado pela transportadora, entregue com divergência, em trânsito, pendente ou sem informação suficiente. Fotos, assinaturas e eventos de rastreio têm alcances diferentes; uma referência ao documento e a ressalva de quantidade/avaria podem ser mais importantes que o rótulo “entregue”. A FAQ FedEx mostra que podem existir comprovações sem assinatura e que detalhes podem ser limitados. [M06](https://www.fedex.com/en-es/customer-support/faq/receiving/tracking-questions/fedex-proof-of-delivery.html)

O mapa de exceções deve ligar fato → impacto → hipótese → evidência necessária → ação proposta → responsável → prazo. Exemplos: coleta perdida, documento divergente, janela fechada, falta na carga e entrega parcial. Não culpar uma parte apenas pelo último status, não editar compromisso original para melhorar um indicador e não enviar reclamações a terceiros sem autorização.

## Indicadores: definir antes de calcular

As fórmulas abaixo são convenções analíticas propostas para um relatório concreto, não um score universal nem uma reprodução de todo o SCOR/APQC. Cada medida precisa declarar período, população, unidade, regra de elegibilidade, fonte, corte, exceções e tratamento de desconhecidos.

| Medida | Definição contextual proposta | O que precisa estar explícito |
|---|---|---|
| OTIF por pedido | Pedidos com todas as linhas recebidas na quantidade acordada dentro da janela acordada / pedidos elegíveis × 100. | Janela/data original ou revisada; recebimento vs saída; tolerância; entregas parciais; cancelamentos; pendentes; unidade de análise. |
| OTIF por linha | Linhas que atendem simultaneamente prazo e quantidade / linhas elegíveis × 100. | Uma linha de pedido não é um pedido; diferentes datas de linha exigem política própria. Não comparar diretamente com OTIF por pedido. |
| Atendimento de quantidade | Quantidade recebida ou expedida / quantidade pedida, com unidades compatíveis. | Não mede prazo. Misturar itens de unidades distintas exige justificativa; excesso e falta devem aparecer separadamente. |
| Comprovação de entrega | Remessas com comprovante válido no corte / remessas que deveriam ter comprovante no mesmo corte × 100. | Validade do comprovante para o serviço, atraso de disponibilização, duplicações e tipo de evidência. Não é automaticamente OTIF. |
| Tempo até entrega | Horário de recebimento menos marco inicial definido. | Pedido recebido, liberado ou coleta são inícios distintos; horas corridas vs úteis; fuso; pedido ainda aberto não tem duração final conhecida. |
| Tempo por etapa | Fim menos início da separação, embalagem, espera, trânsito ou conferência. | Eventos faltantes e sobreposição entre etapas; uma média exige mesmos marcos. Distribuição/percentis só com amostra e método declarados. |
| Custo por remessa/unidade | Custos atribuídos às mesmas remessas / remessas ou unidades pertinentes. | Frete, adicionais e custos internos efetivamente incluídos; rateio; retornos; período de competência; cotado vs faturado. |
| Ocupação | Carga física usada / capacidade física disponível, para kg, m³ ou posições. | Exibir restrições separadas. Peso tarifável não é carga física; 80% em kg não significa 80% em m³. Não juntar denominadores incompatíveis. |
| Taxa de retorno | Pedidos ou unidades retornadas de uma coorte / pedidos ou unidades vendidos da mesma coorte. | Defasagem de retorno, devoluções parciais e motivo; retorno recebido vs solicitado. Não dividir tudo recebido no mês por tudo vendido no mês sem explicar. |
| Tempo de retorno | Marco final definido menos solicitação ou autorização. | Mostrar subtempos de coleta, trânsito, inspeção, decisão e resolução financeira; retorno logístico e resolução financeira podem fechar em momentos diferentes. |

M02 acrescenta documentação e condição ao conceito de pedido perfeito: não basta inferir esse resultado de OTIF. M03 apresenta convenções específicas sobre pedido/linha/data; por isso, a escolha de uma fórmula deve ser declarada. M04 fornece a decomposição de ciclos, inclusive retorno. A evidência consultada dessas três páginas é indexada, com o limite registrado na bibliografia.

Não calcular OTIF multiplicando percentuais agregados de prazo e quantidade: é necessário contar a interseção dos mesmos pedidos/linhas. Não remover desconhecidos silenciosamente. Um relatório pode trazer “confirmado no corte” e um intervalo condicionado às pendências, sem transformar ausência de evidência em entrega boa ou falha operacional provada.

## Retorno: separar fluxo físico e resolução financeira

A entrega deve distinguir solicitação, autorização, coleta/postagem, recebimento físico, identificação, inspeção, disposição e resolução financeira. A disposição pode ser venda, reparo, devolução ao fornecedor ou descarte, segundo política e condição comprovada. Uma caixa recebida não está automaticamente vendável; crédito ao cliente não prova entrada física.

Para um retorno concreto, comparar despesas de coleta/postagem, recebimento, inspeção, reparo e destino, com dados fornecidos. Registrar motivo informado e motivo verificado separadamente. Custo original do produto, crédito comercial, recuperação econômica e desembolso logístico são grandezas distintas; a avaliação de custo não autoriza lançamento contábil.

Se a operação brasileira usar Correios, consultar seu contrato e serviço. A página oficial informa autorização pelo vendedor, dependência de contrato e validade de uso definida pelo vendedor, até o limite indicado pelo serviço. Esse prazo operacional não é prazo legal de arrependimento nem prazo universal de retorno. Não foi emitida autorização. [M07](https://www.correios.com.br/enviar/encomendas/logistica-reversa)

## Três casos fictícios autorais com gabarito

Todos os dados, transportadoras fictícias e regras comerciais abaixo são inventados para avaliar o raciocínio. Não representam preços, SLA, calendário de transportadora ou obrigação legal real. Os casos não reutilizam templates protegidos.

### Caso 1 — Frete: custo, unidades, capacidade e data

**Pedido.** Escolher transporte para 20 caixas de 50 × 40 × 30 cm, peso bruto de 8 kg por caixa, 12 unidades de produto por caixa. Carga pronta em 13/10/2026 às 09h. Destino aceita entrega em 14 ou 15/10, das 09h às 17h; compromisso máximo 15/10 às 17h. Caixas podem ser empilhadas. Custos são BRL; cotações válidas para esse pedido; valores não mencionados estão incluídos. Não há arredondamentos adicionais. Prazos são datas expressamente cotadas, sem calendário inferido.

| Alternativa | Regra de custo fornecida | Capacidade física confirmada | Coleta/entrega fornecida |
|---|---|---|---|
| A — expresso | Peso tarifável = maior entre bruto e cm³/5.000 por caixa; R$ 2/kg + R$ 40; adicional de 10% sobre essa soma; taxa fixa de R$ 80 depois do adicional. | 300 kg e 1,5 m³. | Coleta 13/10; carga precisa estar pronta até 11h. Entrega 15/10 às 14h. |
| B — fracionado | Peso tarifável = maior entre bruto e 300 kg/m³; R$ 1,30/kg + R$ 30; adicional de 8% sobre essa soma; taxa fixa de R$ 20 depois do adicional. | 300 kg e 1,5 m³. | Coleta 13/10 exige carga pronta até 08h; após corte, coleta 14/10 e entrega 16/10 às 10h. |
| C — viagem pequena | R$ 500 por viagem, total. | 1.000 kg e 1,0 m³. | Coleta 13/10 às 12h e entrega 14/10 às 14h. |
| D — dedicada | R$ 700 por viagem, total. | 200 kg e 1,5 m³. | Coleta 13/10 às 12h e entrega 14/10 às 14h. |

**Gabarito verificável.**

- Volume por caixa = 50 × 40 × 30 = 60.000 cm³ = 0,06 m³. Total = 1,20 m³; peso bruto total = 160 kg; produtos = 240 unidades.
- A: peso volumétrico = 12 kg/caixa × 20 = 240 kg; tarifável = 240 kg. Custo = (240 × 2 + 40) × 1,10 + 80 = **R$ 652,00**. Custo por caixa = R$ 32,60; por produto = R$ 2,7167, exibível como R$ 2,72 com nota de arredondamento.
- B: peso volumétrico = 1,20 × 300 = 360 kg; tarifável = 360 kg. Custo = (360 × 1,30 + 30) × 1,08 + 20 = **R$ 557,84**. A carga física é 160 kg, portanto os 360 kg tarifáveis não violam a capacidade física de 300 kg. Porém a disponibilidade às 09h perde o corte das 08h; a entrega em 16/10 viola o compromisso.
- C é inviável: 1,20 m³ supera 1,0 m³, apesar de caber em kg. Não criar uma segunda viagem e manter R$ 500 como total.
- D é viável e custa R$ 700. A também é viável e é R$ 48 mais barata. **Recomendação: A**, com confirmação comercial antes de contratar. Se o compromisso mudar para 14/10 às 17h, D será a única opção viável entre as cotações dadas.
- Para A, ocupação em kg = 160/300 = 53,33%; em volume = 1,20/1,50 = 80%. São restrições separadas; não usar 240 kg tarifáveis na ocupação.

**Erros que o caso detecta.** Confundir cm³/m³, caixas/produtos, peso bruto/tarifável; aplicar divisor único a todas as opções; ignorar a base do adicional; escolher a menor cotação antes de conferir corte e capacidade; prometer que o carregamento foi contratado.

### Caso 2 — Expedição, POD e OTIF: pedidos, linhas e corte

**Pedido.** Analisar a coorte de quatro pedidos prometidos para 15/10/2026, janela de recebimento das 09h às 15h, fuso America/Sao_Paulo. Corte do relatório: 15/10 às 16h. Cada linha pede dez unidades; não há tolerância, cancelamento ou revisão da promessa. A política local exige comprovação do recebimento e quantidade para confirmar OTIF. Todas as linhas do pedido precisam passar para ele passar. O denominador inclui todos os quatro pedidos prometidos, inclusive pendências. Dados fornecidos:

| Pedido/linha | Expedição informada | Recebimento comprovado | Evidência no corte |
|---|---|---|---|
| P01/L1 | 10 unidades; saída 14/10 às 17h. | 10 unidades em 15/10 às 14h. | POD e conferência presentes. |
| P01/L2 | 10 unidades; mesma remessa. | 10 unidades no mesmo horário. | POD e conferência presentes. |
| P02/L1 | 10 unidades; saída 14/10 às 18h. | 10 unidades em 15/10 às 14h30. | POD e conferência presentes. |
| P02/L2 | 10 unidades; mesma remessa. | 6 unidades no mesmo horário. | POD com ressalva de falta; transportadora investiga. |
| P03/L1 | 10 unidades; saída 15/10 às 08h. | 10 unidades em 15/10 às 15h10. | POD e conferência presentes. |
| P04/L1 | 10 unidades; saída 14/10 às 18h. | Status da transportadora diz entregue às 14h55; quantidade recebida não confirmada. | POD/conferência ausentes às 16h. |

**Gabarito verificável.**

- Total: quatro pedidos, seis linhas, sessenta unidades pedidas. Expedição informada: sessenta unidades. Isso não prova sessenta recebidas.
- P01 passa; P02 falha em quantidade; P03 falha em prazo por dez minutos; P04 fica **pendente de evidência**, com status de entrega informado. Não fabricar horário comprovado ou quantidade.
- **OTIF confirmado por pedido = 1/4 = 25%** no corte. Há duas falhas comprovadas e uma pendência. Se P04 for posteriormente comprovado integral e pontual, o resultado será 2/4 = 50%; se falhar, permanece 25%. Esse intervalo não presume probabilidade.
- **OTIF confirmado por linha = 3/6 = 50%**: duas linhas P01 e P02/L1. Limite condicionado à pendência: 4/6 = 66,67%. As duas taxas não devem ser publicadas com o mesmo nome sem unidade.
- Taxa apenas entre pedidos com classificação resolvida = 1/3 = 33,33%; não é a taxa principal solicitada. Se exibida, nomear a população e mostrar a exclusão de P04.
- Recebimento quantitativo confirmado = 10 + 10 + 10 + 6 + 10 = **46 unidades**. São 46/60 = 76,67% confirmadas frente ao pedido; P04 continua desconhecido e quatro unidades de P02 estão comprovadamente faltantes. O número não mede prazo e não prova que as catorze restantes foram perdidas.
- Documentos presentes por pedido/remessa: 3/4 = 75%, somente se cada pedido corresponder a uma remessa como declarado no caso. Não converter isso em OTIF de 75%.
- Saídas informadas em dia não eliminam divergência no recebimento. Ação proposta: solicitar comprovação de P04 e apurar falta de P02 com dados de carga/POD. Não autoriza envio da solicitação.

**Erros que o caso detecta.** Usar saída como entrega, eliminar pendência do denominador, contar linhas como pedidos, multiplicar percentuais marginais, igualar status a POD, alterar corte para esconder atraso ou contar toda falta de evidência como perda.

### Caso 3 — Reversa: custo, condição física e crédito comercial

**Pedido.** Um cliente retorna dez unidades. Identificador R01. Preço de venda fornecido: R$ 150/unidade; crédito comercial aprovado pelo responsável: R$ 1.500, ainda não pago/lançado. Custo histórico fornecido: R$ 80/unidade. As dez unidades chegaram e foram identificadas em 16/10. Inspeção no mesmo dia: seis aptas à revenda e liberadas; três reparáveis em quarentena, sem teste final; uma sem recuperação, segregada para destinação ainda não executada. Política comercial autoriza crédito integral independentemente da inspeção. Não há instrução sobre lançamentos, tributos ou reconhecimento contábil.

Custos efetivamente incorridos no retorno: coleta R$ 120; recebimento R$ 20; inspeção R$ 30. Para as três reparáveis, proposta de reparo de R$ 25/unidade. A política de avaliação econômica do caso estabelece recuperação bruta de R$ 70/unidade **se** o reparo e o teste passarem; essa recuperação não é valor contábil validado nem receita realizada. Destinação da unidade irrecuperável orçada em R$ 10, ainda não executada. Todas as grandezas em BRL.

**Gabarito verificável.**

- Físico: dez recebidas; seis disponíveis para venda; três em quarentena/reparo proposto; uma segregada. Não somar dez ao saldo vendável.
- Financeiro/comercial: R$ 1.500 de crédito aprovado, sem evidência de pagamento/lançamento. A política fornecida permite aprovação antes de concluir destino físico; nenhum débito/crédito contábil deve ser inventado.
- Custo logístico incorrido = 120 + 20 + 30 = **R$ 170**; por unidade recebida = R$ 17. Reparo proposto = 3 × 25 = R$ 75; destinação orçada = R$ 10. Total de cenário = **R$ 255**, dos quais R$ 85 ainda condicionais. Não apresentar R$ 255 como gasto já realizado.
- Recuperação bruta hipotética das três = 3 × 70 = R$ 210; recuperação líquida incremental após reparo = 210 − 75 = **R$ 135**, antes de quaisquer custos não fornecidos. O cenário favorece avaliar reparo; não comprova sucesso técnico, venda ou autorização para executar.
- Custos incorridos de coleta/recebimento/inspeção são comuns às alternativas de destino já analisadas. Não contar novamente esses R$ 170 como custo incremental exclusivo do reparo.
- Custo histórico das dez = R$ 800; custo histórico das seis aptas = R$ 480. Nenhum desses valores é automaticamente receita, crédito ao cliente, saldo contábil final ou perda reconhecida. Para os lançamentos, encaminhar os fatos e pendências ao responsável contábil, conforme política e jurisdição.
- Fechamento logístico parcial: recebimento/inspeção feitos, disposição ainda pendente para quatro unidades. Fechamento financeiro pendente: aprovação comercial não prova pagamento ou registro. O relatório precisa apresentar ambos.

**Erros que o caso detecta.** Devolver ao estoque vendável tudo que chegou, supor crédito pago, tratar orçamento como gasto, confundir preço de venda com custo, somar crédito ao cliente e perda de estoque como se fossem um único custo operacional, ou criar lançamento contábil.

## Limites e organização recomendada

No núcleo da skill devem ficar: identificar o pedido, reaproveitar dados, explicitar unidades e corte, calcular com rastreabilidade, conferir viabilidade e separar fato/hipótese/pendência. As referências sob demanda podem cobrir cotação de frete, indicadores de entrega e retorno. A bibliografia extensa e o registro de acesso devem permanecer no dossiê de pesquisa.

Regras fiscais, aduaneiras, transporte regulado, direitos de devolução e descarte dependem de produto, operação e jurisdição. Esta frente não investigou um caso jurídico concreto e não recomenda checklist legal genérico. Se o pedido exigir esses assuntos, buscar fonte oficial atual do local pertinente, declarar alcance e encaminhar decisão especializada quando necessária. ICC é padrão contratual profissional, não legislação aduaneira. Correios descreve seu serviço, não todos os direitos de devolução.

Não foi demonstrada execução real de logística, contratação, emissão de autorização, prova de entrega autenticada, integração ou instalação. Não foram copiados recursos protegidos. Os três casos verificam coerência de raciocínio e aritmética, sem comprovar desempenho da futura skill em operação real.
