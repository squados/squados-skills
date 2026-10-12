# Pesquisador de Concorrentes Ecommerce — métodos e casos de avaliação

Pesquisa em 12/10/2026. Autoria da síntese e dos casos: SquadOS. Frente de métodos profissionais, documentação original e avaliações; a seleção de pacotes e a análise estratégica ficam nas outras frentes da rodada. Este documento não implementa nem instala uma skill e não comprova sua execução.

## Decisão de método

O trabalho começa pela decisão comercial: comparar ofertas de um produto, explicar uma diferença de preço ou avaliar uma oportunidade de posicionamento. Aproveitar o contexto já fornecido e reconhecer a intenção sem apresentar um menu técnico. Pedir somente informações cuja ausência mude a conclusão: produto/variante, quantidade, destino quando houver comparação de frete, restrições de pagamento ou decisão pretendida. Uma pesquisa de posicionamento não precisa de CEP; um ranking de custo entregue precisa.

A recomendação é uma matriz curta de ofertas comparáveis acompanhada de evidências datadas. Antes de recomendar uma reação, verificar se a diferença vem do produto, da condição comercial, da disponibilidade ou da data. Uma loja pode disputar a mesma compra e oferecer outro produto; isso permite comparação de alternativas, mas não prova diferença de preço do mesmo item.

## Fontes, alcance e contribuição

Todas as páginas abaixo foram consultadas nesta pesquisa, com os limites indicados. A data de acesso não é a data de publicação. Documentação viva sem data editorial visível está identificada assim. A pesquisa utilizou fontes abertas, sem contas novas, compra, instalação, contato com fornecedores ou varredura em massa.

| Fonte original e autoria | Data/versão e acesso real | Contribuição → decisão |
|---|---|---|
| [GS1, GTIN Management Standard](https://ref.gs1.org/standards/gtin-management/) | Release 1.1, ratificado em setembro/2023; PDF de 18 páginas, extração textual consultada, com foco nas seções 2.3 e 2.8 | Identidade comercial e conteúdo da embalagem → adaptar: mudança de conteúdo líquido declarado ou configuração de caixa exige atenção à identidade. Conferir quantidade e embalagem mesmo com nomes semelhantes; o identificador não dispensa ler a oferta. |
| [Google Merchant Center, Product data specification](https://support.google.com/merchants/answer/7052112?hl=en) | Documento vivo, sem data editorial visível; leitura seletiva de variantes, `item_group_id` e `multipack` | Grupo de variantes não equivale a item idêntico; pacote montado pelo vendedor difere de pacote do fabricante → aproveitar na matriz, sem transformar pesquisa em implementação de feed. |
| [Google Merchant Center, Price](https://support.google.com/merchants/answer/6324371?hl=en) | Documento vivo; requisitos e orientações de preço, quantidade mínima e pacotes consultados | Separação entre preço do produto, frete e benefícios condicionados → adaptar: registrar preço, condições e total entregue. Não transportar regras de envio de feed como política universal de todos os sites. |
| [Google Merchant Center, Set up estimated delivery time](https://support.google.com/merchants/answer/14949917?hl=en) | Documento vivo; extração textual da página consultada | Prazo envolve corte do pedido, processamento e trânsito em dias úteis → adaptar: comparar a estimativa exibida para o destino e o momento, sem prometer entrega real. |
| [Mercado Livre Developers, Busca de itens](https://developers.mercadolivre.com.br/pt_br/itens-e-buscas) e [versão inglesa](https://developers.mercadolivre.com.br/en_us/api-docs/items-and-searches) | Sem data/versão confirmada. Busca retornou trecho oficial; ambas as aberturas diretas falharam | Trecho informa que `available_quantity` público é referencial por faixas → aproveitar apenas como alerta para não chamar quantidade pública de estoque exato. A documentação completa permanece uma lacuna; nenhuma API foi executada. |
| [Michael Keenan, Competitive Analysis: Guide and Free Template, Shopify](https://www.shopify.com/blog/competitive-analysis) | Página traz título “2026”, autoria de Keenan, atualização por Kaleigh Moore e Brinda Gulati e data editorial 18/09/2025; extração textual consultada | Definir pergunta, selecionar concorrentes e comparar dimensões ligadas à decisão → adaptar: uma matriz com recomendação e evidências, sem exigir SWOT ou um número fixo de rivais. O título não prova revisão em 2026. |
| [Shopify Staff, Competitive Intelligence: A Practical Guide](https://www.shopify.com/blog/what-is-competitive-intelligence) | Atualizado em 09/06/2025; texto retornado pela pesquisa consultado | Sites e comunicação pública sustentam observações sobre oferta e mensagem → aproveitar pesquisa focada; descartar expansão automática para monitoramento e ferramentas pagas. |

Os métodos foram estudados para produzir síntese autoral. Nenhum template, PDF, vídeo ou código de terceiros foi redistribuído. Consulta pública não implica licença de redistribuição; esses materiais permanecem em suas origens. Não foi feita auditoria de licença de um pacote de terceiros nesta frente.

### Vídeos recentes e limite de acesso

Foram buscados vídeos de 2025–2026 ligados à pesquisa competitiva e à comparação de condições comerciais. Os candidatos mais concretos encontrados nesta frente tratam do prazo e frete no Merchant Center. Eles acrescentam contexto profissional, mas não substituem a documentação atual.

| Material | Autor e data verificável | O que foi realmente consultado | Aproveitamento e limite |
|---|---|---|---|
| [Important Shipping Policy Update For March 2025 In Google Merchant Center](https://www.youtube.com/watch?v=Nw2UkoTORE4) | FeedArmy, 24/03/2025; descrição apresenta Emanuel | Metadados e descrição retornados na busca. Abertura direta falhou. Sem transcrição nem audiovisual | A descrição chama atenção à diferença entre processamento no mesmo dia e prazo de entrega. Conferir regras atuais no documento Google. Nenhum timestamp foi verificado. |
| [How to Add Shipping Rates in Google Merchant Center](https://support.google.com/merchants/community-video/367611915/how-to-add-shipping-rates-in-google-merchant-center-step-by-step-guide?hl=en-au) | Emmanuel Flossie, fundador FeedArmy e Diamond Product Expert; publicação 25/08/2025; última edição da postagem 23/07/2026 | Página da comunidade Google e descrição da apresentação. Sem transcrição nem reprodução audiovisual | Descrição diferencia configuração de frete na interface e no feed. Usar como referência profissional secundária para contexto. A própria comunidade alerta que conteúdo pode não estar verificado/atualizado; a edição da postagem não prova edição do vídeo. |
| [How to Set Up Google Merchant Center in 2025: A Complete Guide](https://www.youtube.com/watch?v=OPhsJfgi0is) | AA-Creation, 01/08/2025 | Metadados e descrição da busca; abertura direta falhou | Descrição publica capítulos 08:13 frete e 12:59 devoluções. São marcadores do autor, não trechos assistidos; não sustentam conclusão sobre o conteúdo audiovisual. Menor contribuição para a decisão de método, sem adoção operacional. |

Não foi encontrada nesta frente uma transcrição acessível ou análise audiovisual que justificasse atribuir uma técnica específica a um trecho assistido. A lacuna está declarada; os princípios decisivos têm suporte documental. Número de seguidores, visualizações e curtidas não foi usado como prova de competência ou resultado comercial.

## Matriz de comparação proposta

A tabela final mostra só o que importa ao pedido. Estes campos orientam a coleta quando relevantes, sem impor ao usuário um formulário completo:

| Dimensão | Registro necessário | Tratamento da lacuna |
|---|---|---|
| Identidade | Marca, modelo/MPN, GTIN quando publicado, variante, cor, tamanho/capacidade, conteúdo, unidades por pack, composição do kit | Nome ou imagem semelhantes não confirmam equivalência. Identificador ausente não exclui automaticamente: conferir atributos e registrar confiança. Não inventar GTIN. |
| Oferta | URL, marketplace/loja, vendedor efetivo, responsável pelo envio quando indicado, condição novo/usado/recondicionado | Marketplace não é o vendedor. Vendedor ou condição diferente impede agregar como uma única oferta. |
| Cenário | Data/hora e fuso da observação, moeda, país, CEP/região quando necessário, quantidade pretendida e contexto de acesso | Sem destino, frete e prazo ficam desconhecidos; a pesquisa pode entregar comparação de preço do produto e deixar total pendente. |
| Preço | Preço aberto, promocional, unidade de venda, forma de pagamento, valor total parcelado, cupom, validade, limite e elegibilidade | “A partir de” e parcela isolada não são preço total. Não somar descontos sem comprovar cumulatividade. Não aplicar cupom de primeira compra ao cliente recorrente. |
| Disponibilidade | Texto/estado da variante, disponibilidade para destino/quantidade e nível observado: página, simulador ou etapa anterior à compra | Ausência de aviso não prova estoque. “Disponível” não prova unidades exatas nem entrega efetiva. Uma oferta indisponível não lidera um ranking de compra viável. |
| Entrega | Frete, mínimo para benefício, modalidade, estimativa exibida, dias úteis/corridos, processamento separado quando declarado | Frete grátis exige conferir requisitos e destino. Prazo anunciado é promessa observada; não prova histórico de pontualidade. |
| Posicionamento | Público, proposta, atributos, políticas/serviços e linguagem da página | “Melhor”, “líder” ou “mais rápido” permanece alegação da empresa até haver verificação independente compatível. |
| Evidência | URL e localização do dado, momento, acesso realizado, trecho curto ou descrição autoral, contradição e limite | Snippet orienta descoberta. Evidência decisiva exige leitura da origem quando possível; bloqueio permanece limitação. |

A identidade é necessária para dizer “mesmo produto”; contexto comercial é necessário para dizer “melhor oferta para este cenário”. Essas são duas decisões diferentes. Caso o pedido envolva substitutos, declarar a função e os requisitos que eles atendem, sem misturar seus preços ao índice do mesmo SKU.

### Cálculo e linguagem da conclusão

Procedimento autoral: custo entregue do cenário = total dos produtos após descontos elegíveis + frete + cobranças obrigatórias conhecidas. Mostrar incógnitas em vez de assumir zero. Preço por unidade = custo correspondente dividido pela quantidade daquela unidade; declarar se inclui frete. Kits heterogêneos não permitem rateio neutro entre produtos sem uma premissa explícita. Cashback futuro não reduz desembolso imediato; financiamento exige comparar o total pago e suas condições.

Para diferenças percentuais, declarar a base: `(oferta concorrente − nossa oferta) / nossa oferta × 100`. Isso não é margem, lucratividade ou recomendação automática de desconto. A habilidade pode sugerir conferir margem e testar uma hipótese, mas só pode calcular rentabilidade com custos fornecidos e pertinentes.

Uma mudança exige duas observações comparáveis: mesma identidade, vendedor, condição e cenário, com datas distintas. Troca de variante, promoção vencida, CEP diferente ou seleção de vendedor distinta pode explicar a diferença. Se falta observação histórica, dizer “preço observado hoje”; não “baixou”, “subiu” ou “faz isso toda semana”.

Reviews informam relatos de clientes e temas observados, com período e seleção declarados. Quantidade de avaliações, seguidores, tráfego estimado e anúncios visíveis não mede vendas, conversão ou participação de mercado. Uma hipótese estratégica liga evidência a uma ação testável; o relatório não transforma presença digital em resultado comercial.

## Entrega e organização da futura skill

Núcleo sugerido: reconhecer a decisão, aproveitar contexto, esclarecer lacuna material, selecionar rivais pertinentes, conferir comparabilidade, calcular quando há dados, separar observação/alegação/hipótese e entregar recomendação com evidência e limites. Texto principal curto, usando palavras do trabalho.

Referências sob demanda: identidade/variante/pack, condições comerciais e cálculo, leitura de posicionamento, formato de relatório e estes casos. Bibliografia extensa e histórico de pesquisa ficam no dossiê, fora do núcleo executável. A skill não deve abrir todas as referências para uma pergunta simples.

Formato mínimo útil: conclusão em um parágrafo, matriz comparável, ação sugerida e motivo, fontes datadas e pendências que podem mudar a decisão. Para um pedido estratégico, acrescentar evidência → hipótese → teste proposto, sem criar uma campanha ou fazer mudanças externas.

Scripts entram somente se um pedido real demonstrar ganho, por exemplo validar cálculos repetidos em um arquivo fornecido; não precisam de scraping para comparar poucas ofertas. Dependências ausentes não são presumidas instaladas. Quando necessárias e autorizadas, explicar em linguagem simples o benefício, conferir o ambiente e oferecer instalação simples executada pelo agente quando autorizada, aproveitando autorização existente e sem pedir comandos ao usuário. A pesquisa atual não instala nada.

Melhoria da própria skill: após uso real, detectar preferência recorrente ou atrito concreto e oferecer adaptar a própria versão da skill. Aplicar uma alteração pequena com aceite ou pedido direto, com critério de aceitação pertinente. Não criar infraestrutura de feedback. Agendamento só entra em um pedido explícito de acompanhamento: uma comparação pontual não arma monitoramento.

## Três casos autorais com gabarito

Dados abaixo são fictícios, escritos para avaliação futura. Nomes de lojas e identificadores simbólicos não representam empresas ou GTINs reais. Os gabaritos foram recalculados nesta pesquisa; não são testes executados no agente final.

### Caso 1 — mesmo nome, outra variante e condição

Pedido: “Nossa garrafa Aurora 750 ml nova está cara? Compare as ofertas para uma unidade, pagamento à vista, CEP 13010-000, 12/10/2026 às 10h BRT.” Nossa oferta: modelo A750, preta, 750 ml, R$ 90 + R$ 15 de frete, disponível, entrega estimada 3–5 dias úteis.

| Oferta fictícia | Atributos e condição | Produto + frete | Disponibilidade |
|---|---|---|---|
| Loja Cedro | A750 preta 750 ml, nova, uma unidade | R$ 88 + R$ 20 | Disponível; 4–6 dias úteis |
| Loja Lume | A500 preta 500 ml, nova | R$ 70 + R$ 10 | Disponível |
| Loja Vale | A750 preta 750 ml, usada | R$ 65 + R$ 15 | Disponível |
| Loja Nexo | A750 preta 750 ml, nova | R$ 80 + R$ 0 | Indisponível na variante preta |

Gabarito: nossa oferta comparável entregue custa R$ 105; Cedro custa R$ 108. Cedro tem preço do produto R$ 2 inferior, mas total entregue R$ 3 superior: `3 / 105 × 100 = 2,86%`. Nossa oferta é a menor entre as duas ofertas novas idênticas disponíveis no cenário. A500 é outra capacidade; usada é outra condição; Nexo é indisponível. Não concluir que somos os mais baratos do mercado ou que entregamos efetivamente mais rápido. Fonte do prazo é estimativa.

Aceitação: preservar atributos, excluir os três falsos vencedores do ranking viável, comparar total com base explícita e limitar a conclusão ao conjunto. Reprova se recomendar baixar para R$ 65 ou declarar liderança geral.

### Caso 2 — cupom, quantidade e frete

Pedido: “Para cliente recorrente, qual loja custa menos para seis frascos idênticos de 500 ml, no CEP informado, hoje?” A documentação fictícia confirma mesmo modelo, fórmula, condição nova e disponibilidade de seis unidades.

| Oferta fictícia | Condições observadas |
|---|---|
| Nossa loja | Seis unidades a R$ 25 cada; frete R$ 12; sem cupom |
| Loja Cedro | Pack fechado de seis a R$ 138; frete R$ 18; cupom 10% somente primeira compra, desconto apenas no produto |
| Loja Lume | Unidade a R$ 24; frete grátis a partir de R$ 150 em produtos; abaixo disso, R$ 20; comprador pode levar seis ou sete |

Gabarito: nossa loja `6 × 25 + 12 = R$ 162`; Cedro recorrente `138 + 18 = R$ 156`; Lume seis `6 × 24 + 20 = R$ 164`. Cedro vence o cenário de seis. Total por frasco entregue: R$ 27; R$ 26; R$ 27,33, respectivamente. Cupom não é elegível para este cliente. Para primeiro comprador, se as condições forem as fornecidas, Cedro seria `138 × 0,90 + 18 = R$ 142,20`, ou R$ 23,70 por frasco.

Levar sete na Lume custa `7 × 24 = R$ 168` com frete grátis: R$ 24 por frasco, mas R$ 12 a mais de desembolso que Cedro para atender a necessidade original. É alternativa de maior quantidade, não vencedora de seis. Não completar o mínimo com produto fictício nem presumir estoque adicional sem os dados do caso.

Aceitação: manter cenário recorrente, distinguir desconto condicional, unidade/pack e total, explicar o custo incremental de sete. Reprova se aplicar cupom universal, dar frete grátis a R$ 144 ou chamar R$ 168 de menor desembolso.

### Caso 3 — falsa queda de preço e hipótese estratégica

Pedido: “O concorrente está baixando preços e vendendo mais? Devemos copiar seu posicionamento?” Conjunto fictício:

- Em 05/10 às 10h BRT, Loja Cedro exibia tênis Passo, modelo P1, tamanho 40, novo, por R$ 200, cartão à vista, sem promoção; disponível.
- Em 12/10 às 10h BRT, uma página do mesmo grupo exibia R$ 180 para tamanho 38; tamanho 40 permanecia R$ 200. Ambos novos, mesmo vendedor. Não há observação histórica do 38.
- Loja Lume, rival direta da mesma categoria/público, comunica “entrega em 24h” na página inicial. O simulador público para o CEP do pedido apresenta 3–5 dias úteis. Loja Cedro comunica troca de tamanho; a política publicada detalha as condições. Uma sapataria de reparos resolve conservar um calçado existente, sendo substituto funcional e não oferta do mesmo tênis.
- Cedro tem 20 mil seguidores e 120 reviews públicos. O conjunto não inclui vendas, sessões, conversões, mercado total, amostra representativa de clientes ou motivos de compra.

Gabarito: não há queda comprovada no tamanho 40; comparar R$ 200 do 40 a R$ 180 do 38 é misturar variante. Sem histórico do 38, não concluir tendência. Não é possível afirmar crescimento de vendas, conversão ou participação. “Entrega em 24h” é alegação; para este destino, a estimativa observada é 3–5 dias úteis, e a divergência merece destaque antes de copiar a promessa.

Evidência estratégica utilizável: troca de tamanho é comunicada e tem condições publicadas. Hipótese autoral: esclarecer as condições de troca pode reduzir incerteza de tamanho no público atendido. Próximo teste proposto: comparar a compreensão e as dúvidas de clientes sobre a mensagem atual e uma versão mais clara, com critério previamente definido; medir resultado comercial exige dados próprios adequados e autorização. Não declarar que Cedro vende mais por causa da troca, nem copiar textos. O reparo entra como alternativa à compra para outro pedido, fora do índice de preço do P1.

Aceitação: conservar a série por variante, reconhecer contradição, distinguir rival direta/substituto e produzir hipótese verificável com limites. Reprova se chamar a diferença de R$ 20 de desconto temporal, inventar vendas a partir de reviews ou recomendar reproduzir promessa não confirmada.

## Estado de validação

Fontes decisivas, contribuições e limites foram registrados; os três gabaritos são avaliação autoral para futura execução. Não houve compra, checkout concluído, consulta autenticada de estoque, teste de entrega ou execução de um pedido real pela skill. Acesso completo à documentação Mercado Livre e ao conteúdo dos vídeos permanece limitado. Não foi alterado o catálogo nem verificada compatibilidade de um pacote nesta frente.
