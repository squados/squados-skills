# Especialista em Catálogo de Produtos Ecommerce — métodos e casos

Pesquisa profissional da rodada 22/33, consultada em 12/10/2026. Escopo: identidade, variantes, títulos, descrições, atributos, categorização e qualidade. Descoberta e comparação de pacotes de skills estão nas frentes irmãs. Este documento propõe critérios para uma futura skill; não comprova execução dessa skill, aprovação de feed, publicação ou melhoria de vendas.

## Decisão central

A especialista deve transformar materiais existentes em um catálogo revisável e adequado ao destino, com dados rastreáveis por produto e variante. O ponto de partida é o pedido: melhorar cinco descrições, organizar atributos de centenas de itens e corrigir um feed são trabalhos diferentes. Não exigir planilha, título, bullets, descrição longa e feed em toda resposta.

A recomendação é um núcleo curto que reconheça a intenção, recupere evidências, resolva a identidade do item, faça o trabalho e confira o resultado. Regras de plataforma, taxonomias e validação em lote entram sob demanda. As fontes abaixo ajudam a tomar decisões; seus exemplos e textos não devem ser redistribuídos como templates próprios.

## Fontes profissionais: contribuição e decisão

Datas ausentes significam não exibidas no conteúdo consultado. Data de rastreamento não foi tratada como publicação. Acesso aberto para leitura não significa licença aberta para redistribuir. Todos os links foram consultados nesta data; o escopo exato consta na tabela.

| Fonte exata, autoria, data/versão | Acesso efetivo | Contribuição → decisão |
|---|---|---|
| [GS1 GTIN Management Standard](https://ref.gs1.org/standards/gtin-management/), GS1 AISBL, versão 1.1 ratificada, setembro/2023 | PDF textual de 18 páginas, metadados e regras consultados; sem copiar o PDF | Identidade comercial e mudanças de conteúdo líquido/embalagem → aproveitar os princípios e adaptar à auditoria de identidade; a skill não atribui GTIN por conta própria. |
| [Declared net content](https://www.gs1.org/1/gtinrules/en/rule/266/declared-net-content), GS1, data ausente | Página da regra lida | Quantidade declarada é parte da identidade → conferir unidade e apresentação; não fundir 500 mL e 750 mL por semelhança de nome. |
| [What is the GS1 Data Quality Framework?](https://support.gs1.org/support/solutions/articles/43000734211-what-is-the-gs1-data-quality-framework-), GS1 GO, atualização 30/08/2024 | Artigo introdutório integral; não houve leitura integral do pacote DQF | Qualidade combina processo e inspeção física → adaptar a distinção entre consistência digital e prova física. Um CSV coerente não confirma medidas reais. |
| [Title and structured title](https://support.google.com/merchants/answer/6324415?hl=en), Google Merchant Center, data/versão ausentes | Página textual: formato, requisitos, recomendações e exemplos | Título identifica a oferta e distingue variantes → aproveitar; adaptar limites e origem de IA ao feed deste canal. Descartar uso de 150 caracteres como meta universal. |
| [Description and structured description](https://support.google.com/merchants/answer/6324468?hl=en), Google Merchant Center, data/versão ausentes | Página textual: formato e requisitos; exemplos acessíveis | Descrição coerente com título e página de destino → aproveitar; separar informação do produto de promoção e políticas comerciais quando o destino for o feed. |
| [Google product category](https://support.google.com/merchants/answer/6324436?hl=en), Google Merchant Center, data/versão ausentes | Seções de uso, valores, requisitos, recomendações e exemplos lidas | Categoria de Google e classificação própria têm funções diferentes → adaptar; escolher por função principal e consultar taxonomia atual, sem converter departamento interno em código Google inventado. |
| [Category metafields](https://help.shopify.com/en/manual/custom-data/metafields/category-metafields), Shopify, data/versão ausentes | Artigo integral de 21 linhas | Categoria determina atributos pertinentes e pode ligar opções de variantes → aproveitar o modelo de atributo dependente da categoria; previsão de IA é sugestão, não prova do atributo. |
| [New product title requirements](https://sellercentral.amazon.com/seller-forums/discussions/t/b2b15728-0d43-453e-974f-59eb63f73059), News_Amazon, vigência declarada 21/01/2025; publicação exibida apenas relativamente | Anúncio oficial e link de orientação; comentários não usados como política | Mudanças limitam caracteres e repetição para a maioria das categorias → adaptar após verificar loja/categoria; não declarar 200 como limite universal. |
| [Amazon SEO](https://sell.amazon.com/blog/amazon-seo?mons_sel_locale=en_US), Daisy Quaker / Amazon, 03/09/2025 | Artigo textual, especialmente títulos/descrições | Marca, tipo e detalhes ajudam identificação; recomenda título curto → adaptar à relevância; não adotar densidade fixa de palavras-chave nem prometer ranking. |
| [How to create Amazon product listings](https://sell.amazon.com/blog/amazon-product-listings), Amazon, 29/04/2026, autoria individual não exibida no trecho | Artigo textual de identidade, descrição, detalhes e oferta | Produto e oferta do vendedor são entidades distintas → aproveitar para não tratar preço/estoque como fato eterno do modelo. Conteúdo exigido varia pelo produto. |
| [How to boost Amazon listings](https://sell.amazon.com/blog/how-to-boost-amazon-listings?lang=en-US), Amazon, 29/04/2026 | Resultado de busca com trechos; leitura integral não realizada | Recomenda até 80 caracteres; artigo de 2025 recomenda até 60 → descartar ambos como regra fixa. São orientações editoriais divergentes, não evidência de conversão deste catálogo. |
| [Atributos Mercado Livre](https://developers.mercadolivre.com.br/pt_br/atributos), Mercado Livre Developers, data/versão ausentes | Trechos indexados; acesso direto retornou 403. URL alternativa também falhou | Indica dependência da categoria e valores numéricos com unidades → pista útil, mas não contrato validado. Não afirmar limites, obrigatoriedade ou payload atual sem schema aplicável acessível. |

| [Adding variants](https://help.shopify.com/en/manual/products/variants/add-variants), Shopify, data/versão ausentes | Introdução e considerações, incluindo mais de 100 variantes, lidas | Limite atual e compatibilidade de integrações divergem → adaptar por canal, tema e app; descartar teto universal antigo de 100. |

### Leitura das políticas atuais

As páginas Merchant consultadas exigem `structured_title`/`structured_description` para texto gerado por IA, com `digital_source_type=trained_algorithmic_media`. Os limites ali exibidos são 150 e 5.000 caracteres, respectivamente. Isso pertence à submissão Merchant; não determina o layout nem o limite editorial de toda página de produto. A presença simultânea dos campos simples faz o Google priorizar os simples; a futura referência de feed deve explicar esse conflito. [Título](https://support.google.com/merchants/answer/6324415?hl=en), [descrição](https://support.google.com/merchants/answer/6324468?hl=en).

No anúncio Amazon de 2025, o teto de 200 inclui espaços para a maioria das categorias; há restrições de caracteres e repetição com exceções. Registrar loja, categoria e versão consultada antes de verificar um lote. Validação de byte para termos de busca não pode ser substituída por contagem de caracteres, nem inferida de um checker comunitário. A regra vigente desse campo específico não foi confirmada nesta frente. [Anúncio oficial](https://sellercentral.amazon.com/seller-forums/discussions/t/b2b15728-0d43-453e-974f-59eb63f73059).

Google recomenda marca quando ela diferencia o produto. Isso não prova que todo título deve começar por marca nem que inserir marca sempre melhora CTR. Campos obrigatórios, dimensões, garantia, disponibilidade e certificações dependem do canal, mercado, produto e fonte disponível. Não inventar garantia para preencher uma estrutura.

A documentação Shopify consultada permite até 2.048 variantes e três opções por produto, mas ressalva temas, apps, canais e integrações REST legadas com limitações acima de 100. Não gerar automaticamente todas as combinações cartesianas: uma combinação possível não prova que o SKU existe, tem estoque ou está publicado. Novas combinações propostas devem permanecer candidatas até confirmação; não preencher `published=true`, estoque zero ou SKU fictício como dado comercial confirmado. [Adding variants](https://help.shopify.com/en/manual/products/variants/add-variants).

A página específica de `google_product_category` consultada marca o atributo como opcional, com classificação automática e condições para sobrescrever. Não tornar a coluna obrigatória para toda exportação com base em snippets ou referências genéricas que divergem; documentar a regra específica e o contexto do feed. Isso não elimina requisitos próprios de categorias especiais. [Página específica](https://support.google.com/merchants/answer/6324436?hl=en).

## Vídeos e limites de acesso

| Material 2025–2026 | O que foi consultado | Contribuição → decisão |
|---|---|---|
| [Google Merchant Center Title Policy Update – Add Brand Names to Product Titles!](https://www.youtube.com/watch?v=ZtUiots4oT0), FeedArmy / Emmanuel, 15/05/2025 | Metadados e descrição indexada. Página direta falhou; sem transcrição, áudio ou vídeo assistido; timestamps indisponíveis | Profissional apresenta a marca como diferenciador, mas descrição oscila entre recomendação e possível obrigação → usar somente como pista verificada contra a documentação oficial; descartar promessa de CTR/conversão como prova. |
| [What makes a new product launch good?](https://sell.amazon.com/blog/ask/new-product-launch), Amazon Selling Insights, Mickey Toogood, Sr. Content Marketing Manager, 27/06/2025 | Página e transcrição textual integral, parágrafos publicados entre linhas 200–208 da extração; audiovisual não consultado; transcrição sem timestamps | Mostra que A+ Content/experimentos dependem de contexto e programas da Amazon → adaptar apenas a separação entre trabalho editorial e recursos autenticados; descartar logística, Vine, anúncios e repricing do núcleo da especialista de catálogo. |
| [How to Optimize Your Product Feed & Data in Google Merchant Center — 2025 Full Guide](https://www.youtube.com/watch?v=DpX6KjOVTUk), Learn With Liam, 18/04/2025 | Metadados e descrição indexada; sem transcrição/audiovisual | Descrição enumera palavras-chave, sem procedimento demonstrável → descartar como fundamento metodológico. |

Não houve consulta ao vidIQ, criação de conta, curso pago ou inferência sobre conteúdo inacessível. A busca recente encontrou material datado de 2025 e documentos de 2026; não encontrou vídeo de 2026 suficientemente acessível e pertinente para fundamentar uma nova decisão. Não atribuir timestamps que não foram observados.

## Método autoral proposto

1. **Reconhecer a entrega.** Usar arquivos e conversa para inferir destino, idioma, mercado, volume e intenção. Perguntar apenas quando uma decisão material mudar o resultado: qual variante está sendo vendida, se é unidade ou kit, qual canal exige o arquivo. Uma melhoria de descrição pode continuar como rascunho enquanto faltam regras de importação.
2. **Resolver identidade.** Separar produto/família, variante, SKU, GTIN e oferta do vendedor. SKU não é GTIN; checksum válido não demonstra cadastro GS1 legítimo. Identificar mudança de conteúdo, composição, modelo ou pacote antes de mesclar registros. [GS1](https://ref.gs1.org/standards/gtin-management/).
3. **Construir a base factual mínima.** Cada afirmação usada deve ter origem e escopo: arquivo/página/data, SKU ou família, observação direta ou declaração do fornecedor. Pode ser uma coluna ou anotação curta; não exige banco ou novo sistema. Imagem confirma aspectos visuais observáveis, não composição, resistência, certificação ou compatibilidade técnica.
4. **Ajustar categoria e atributos.** Selecionar atributos que ajudam a identificar e escolher aquele produto. Categoria própria, Shopify e Google podem exigir mapeamentos separados. Usar taxonomia consultada; quando não houver correspondência demonstrada, propor candidata com motivo e pendência. [Shopify](https://help.shopify.com/en/manual/custom-data/metafields/category-metafields), [Google](https://support.google.com/merchants/answer/6324436?hl=en).
5. **Escrever para a decisão de compra.** Identificar tipo, modelo e diferenças relevantes no título. Na descrição, organizar o uso, características e limitações confirmados. Adaptar ordem e extensão ao pedido; vocabulário de busca só entra quando representa o produto. Característica não autoriza deduzir desempenho: aço inox não prova grau, ausência de níquel ou duração térmica.
6. **Revisar no nível certo.** Conferir cada SKU contra suas fontes e o contrato do destino. Conteúdo comum da família só pode ser herdado se a evidência abranger as variantes; peso, material ou acessórios podem divergir. Uma divergência impede a afirmação afetada, sem inutilizar todo o restante.
7. **Entregar resultado utilizável.** Mostrar o texto ou arquivo pedido, mudanças importantes e lacunas que ainda impedem uso específico. Separar rascunho editorial revisado, exportação validada, aprovação do canal e desempenho real. Oferecer adaptar a rotina aos nomes, regras e arquivos que a empresa já usa quando isso reduzir retrabalho recorrente.

Fato, promessa e estimativa não são sinônimos. “Contém 750 mL” pode vir do rótulo; “mantém quente por 12 h” requer ensaio ou declaração claramente atribuída; “deve reduzir dúvidas” é hipótese de benefício do trabalho, não resultado medido. Uma medição de CTR exige período, população e comparação adequados; não inferir ganho de tráfego a partir de título mais claro.

## Três casos autorais com gabarito

Dados, marcas e documentos abaixo são fictícios e criados para esta pesquisa. São exercícios de revisão manual, não testes já executados de uma skill futura.

### Caso 1 — herança errada entre variantes

**Pedido:** “Arrume o cadastro das garrafas Linha Campo.”

**Entradas fictícias:** tabela do fornecedor v3 identifica família Campo. SKU `CP-500-AZ`: 500 mL, azul, corpo aço inox 304. SKU `CP-750-PR`: 750 mL, preto, corpo aço inox, grau não informado. Importação antiga atribui 500 mL e grau 304 a ambos. Foto do segundo mostra cor preta. GTIN do segundo está ausente.

**Gabarito:** manter dois SKUs; corrigir capacidade e cor do segundo. Material do primeiro: “aço inox 304”; do segundo: “aço inox”, sem herdar grau. Títulos: “Garrafa Linha Campo 500 mL — Azul” e “Garrafa Linha Campo 750 mL — Preta”. GTIN ausente permanece pendente, não é derivado do primeiro. Fonte do grau é específica ao primeiro SKU; a foto não confirma grau.

**Aceitação:** nenhum SKU absorve quantidade ou grau do outro; grupo comum não autoriza afirmar propriedades não comprovadas. Se o destino exigir identificador, a exportação final depende da informação ou exceção legítima aplicável. A distinção de conteúdo líquido acompanha a regra GS1; nenhum número GTIN foi criado. [GS1, conteúdo líquido](https://www.gs1.org/1/gtinrules/en/rule/266/declared-net-content).

### Caso 2 — título e descrição com promessa sem prova

**Pedido:** “Deixe este anúncio convincente, sem mudar o produto.”

**Entradas fictícias:** SKU `GT-750-VD`, Garrafa Trilha, verde, 750 mL, tampa rosqueável, parede dupla, corpo aço inox. Folheto do distribuidor diz “até 12 horas quente”, sem condições de teste. Texto atual: “Garrafa antibacteriana certificada, 100% antivazamento, mantém qualquer bebida quente por 24 h e serve em todo porta-copos”. Não há fonte para certificação, propriedade antibacteriana, vedação absoluta ou dimensões.

**Gabarito principal:** título “Garrafa Trilha de aço inox 750 mL — Verde”. Descrição “Garrafa Trilha verde, com capacidade de 750 mL, corpo de aço inox, parede dupla e tampa rosqueável.” As quatro promessas sem suporte saem. Se a empresa quiser manter duração térmica, oferecer redação atribuída — “O distribuidor informa conservação de bebidas quentes por até 12 horas; condições de teste não fornecidas” — para revisão, sem transformá-la em garantia verificada. Para a versão final, solicitar ficha ou ensaio apenas se a promessa for material ao pedido.

**Aceitação:** afirmar somente especificações documentadas; não inferir segurança sanitária ou performance. Se o destino for Merchant e o texto tiver sido gerado por IA, preparar os campos estruturados aplicáveis. Uma descrição para a loja pode ter organização diferente do feed; não incluir promoção no campo Merchant. [Descrição Merchant](https://support.google.com/merchants/answer/6324468?hl=en).

### Caso 3 — categoria, unidades, pacote e locale

**Pedido:** “Prepare estes itens para cadastrar no canal, com medidas corretas.”

**Entradas fictícias:** ERP pt-BR lista SKU `CAN-2`, “kit com 2 canecas”, capacidade de cada peça `0,35 L`, peso bruto do kit `0,84 kg`, campo `altura=12` sem unidade nem indicação de produto/embalagem; departamento interno “Presentes”. Marca e material desconhecidos. Destino informado inicialmente como “canal de vendas”, sem plataforma/país.

**Gabarito:** kit contém 2 peças de 350 mL cada (`0,35 × 1.000`), total aritmético de capacidade 700 mL, que não deve ser apresentado como capacidade de uma caneca. Peso bruto de embalagem é 840 g (`0,84 × 1.000`), distinto de peso líquido. Não converter altura 12 em centímetros, não preencher material e não usar “Presentes” como categoria oficial. Pergunta material: qual canal/mercado e qual significado/unidade da altura? Enquanto isso, título de rascunho “Kit com 2 canecas de 350 mL” e tabela factual já podem ser entregues.

**Aceitação:** preservar números como dados numéricos e formatar decimal conforme arquivo/destino; distinguir pacote e unidade; não inventar códigos de categoria. Categoria candidata é caneca segundo função principal, sujeita à taxonomia do canal. Importação só se declara validada depois de verificar regras aplicáveis e dados faltantes. No Mercado Livre, os trechos indexados sugerem unidades e atributos por categoria, mas o 403 impediu confirmação contratual; isso permanece uma pendência explícita, sem execução autenticada. [Google categoria](https://support.google.com/merchants/answer/6324436?hl=en), [Mercado Livre, acesso limitado](https://developers.mercadolivre.com.br/pt_br/atributos).

## Núcleo, referências e scripts

**Núcleo:** intenção, entrega, identidade, evidência, escrita e revisão. **Referências sob demanda:** variantes e identidade; vocabulário de atributos por categoria; regras de cada feed e mercado; tratamento de unidades e locale. Histórico extenso e bibliografia ficam neste dossiê, fora do pacote executável.

Um script só compensa quando houver lote e ganho concreto: verificar duplicatas de SKU, presença de colunas exigidas pelo perfil já confirmado, conversões explícitas e conflitos variante/fonte. Não usar pontuação SEO opaca, densidade fixa, remoção automática de avisos, scraping atrás de captcha ou envio para loja. Script valida consistência; não conhece a verdade física do produto nem certifica elegibilidade comercial. Esta frente não criou scripts nem instalou dependências.

Na execução futura, aproveitar bibliotecas e autenticação existentes quando necessárias. Se faltar capacidade para gerar o arquivo solicitado, explicar o que falta e oferecer a instalação simples possível no ambiente, em linguagem de trabalho; não exigir que a pessoa opere terminal, nem prometer que o Studio já inclui a biblioteca. Para poucas linhas, entregar tabela ou texto utilizável pode resolver o pedido sem qualquer instalação.

Quando o uso recorrente ou o atrito justificar, oferecer uma skill própria adaptada ao dicionário de cores, nomes de família e formato de entrega da empresa. Criar ou alterar essa skill somente após aceite da oferta ou pedido direto; observar recorrência não autoriza incorporação automática. Aceitação sugerida: pedido cumprido; informação suportada; diferenças de variantes preservadas; lacunas explícitas; contrato do canal conferido quando aplicável; formato utilizável. Não criar novos cadastros, publicar anúncios, executar APIs, enviar mensagens ou comprar serviços a partir desta pesquisa.

## Limites desta frente

As decisões materiais de método estão resolvidas para orientar a criação posterior. Mercado Livre tem acesso documental incompleto; regras específicas Amazon de termos de busca e imagens não foram verificadas nesta frente; vídeos têm os alcances discriminados acima. Não afirmar cobertura exaustiva nem compatibilidade integral com marketplaces. A validação deste documento cobre estrutura, rastreabilidade e gabaritos autorais revisados; execução real da futura skill e aceitação dos canais permanecem etapas posteriores.
