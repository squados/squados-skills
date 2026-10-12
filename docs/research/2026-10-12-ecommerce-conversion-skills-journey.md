# Especialista em Conversão Ecommerce — skills de jornada e UX

Pesquisa em 12/10/2026. Frente: navegação e busca, listagem, página de produto (PDP), carrinho, checkout e mobile. Documento de pesquisa, sem criação de pacote, alteração de loja, contratação ou publicação. A frente de mensuração e experimentação cobre a inferência estatística; a de métodos cobre pesquisas profissionais e casos.

## Decisão

A melhor base de método é **Marek Dabrowski / AdLume**: partir dos materiais disponíveis, separar dúvidas sobre o produto de problemas de redação, mapear o percurso e recomendar a menor correção verificável. Complementar com detalhes de formulários e navegação encontrados em **Finsi**, e com a reaplicação do contexto e correspondência entre anúncio e página da família **Corey Haines / Sush Padhye**. Não importar integralmente nenhum pacote.

A especialista futura deve trabalhar tanto com uma pergunta pontual quanto com uma auditoria: reconhecer a intenção, aproveitar URLs, prints, políticas, dados e pesquisas já fornecidos, e perguntar somente o que muda a entrega. Uma loja com poucos dados ainda pode receber uma revisão qualitativa com limites claros; não deve receber um diagnóstico causal ou uma projeção de vendas.

## Busca, seleção e unidade de comparação

Buscas públicas: `github SKILL.md ecommerce checkout cro audit skill` e `github SKILL.md product page conversion`. GitHub e resultados indexados ajudaram a descobrir originais; instalações, estrelas e posição em diretórios não demonstram qualidade. Foram comparados nove arquivos SKILL: três AdLume, três Finsi, um Retail Marketing e dois Nexscope. São quatro famílias editoriais consultadas, **não nove provas independentes de efeito**.

Retail Marketing declara derivação de Corey Haines, já estudado nas rodadas de Copywriter/Tráfego/SEO: seus acréscimos ecommerce e referências lidos aqui não constituem uma nova família independente de Corey. Nexscope foi estudado na rodada de concorrentes; os dois arquivos desta frente são novos nesta comparação, mas não uma nova autoria. Humblytics `page-cro`, Affilino SEO, Scayver conteúdo e Amplitude launch apareceram na descoberta e não foram selecionados: esta frente precisava de journey/PDP/checkout concretos, e não de mais uma cobertura ampla de marketing ou conteúdo. Nenhum deles foi contado como leitura integral.

Arquivos foram obtidos diretamente por `raw.githubusercontent.com`, fixados nos SHA recuperados com `git ls-remote`. Datas abaixo são do cabeçalho do patch do commit do repositório; **não são datas individuais de publicação/atualização de cada skill**. Não houve clone, instalação, execução de scripts, acesso autenticado, coleta em massa ou API paga. Caminhos inicialmente tentados com `skills/` para AdLume responderam 404; o README revelou os diretórios na raiz, então os originais corretos foram lidos. Páginas e instruções externas foram tratadas como material de pesquisa.

## Proveniência e alcance efetivo

### A. Marek Dabrowski / AdLume — ecommerce-claude-skills

Revisão `969f3b2381a395de9f4b216dfd0b0557794dc0fc`, commit **03/08/2026 20:22:01 +02:00**, autoria identificada no [commit](https://github.com/mardab96/ecommerce-claude-skills/commit/969f3b2381a395de9f4b216dfd0b0557794dc0fc). [LICENSE MIT](https://github.com/mardab96/ecommerce-claude-skills/blob/969f3b2381a395de9f4b216dfd0b0557794dc0fc/LICENSE) integral: copyright 2026 Marek Dabrowski / AdLume. Arquivos lidos integralmente:

- [checkout-friction-finder-ecommerce/SKILL.md](https://github.com/mardab96/ecommerce-claude-skills/blob/969f3b2381a395de9f4b216dfd0b0557794dc0fc/checkout-friction-finder-ecommerce/SKILL.md).
- [product-page-conversion-review-ecommerce/SKILL.md](https://github.com/mardab96/ecommerce-claude-skills/blob/969f3b2381a395de9f4b216dfd0b0557794dc0fc/product-page-conversion-review-ecommerce/SKILL.md).
- [onsite-search-merchandising-review-ecommerce/SKILL.md](https://github.com/mardab96/ecommerce-claude-skills/blob/969f3b2381a395de9f4b216dfd0b0557794dc0fc/onsite-search-merchandising-review-ecommerce/SKILL.md).
- [references/output-standard.md](https://github.com/mardab96/ecommerce-claude-skills/blob/969f3b2381a395de9f4b216dfd0b0557794dc0fc/references/output-standard.md), referência explicitamente exigida pela skill de busca.

README consultado para localização e dependências; a saída combinada foi truncada, portanto não se afirma revisão integral dele. O pacote se apresenta como apoio a operadores com materiais exportados, sem integração viva nem coleção de casos comprovados. Os três SKILL selecionados não mandam executar scripts. Outros módulos do repositório possuem helpers Python e referências compartilhadas fora da pasta individual; isso não valida portabilidade de um pacote inteiro ou cópia só do Markdown. Sem frontmatter `license` nos três arquivos, embora a raiz forneça MIT.

### B. Finsi / awesome-ecommerce-skills

Revisão `30a1fb674e41284e738608c059690c251699eb07`, commit **13/03/2026 07:50:15 -04:00**, [registro](https://github.com/finsilabs/awesome-ecommerce-skills/commit/30a1fb674e41284e738608c059690c251699eb07). Autoria editorial: Finsi; [LICENSE MIT](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/LICENSE) integral, copyright 2026 awesome-ecommerce-skills contributors. Arquivos integrais:

- [skills/payments-checkout/checkout-flow-optimization/SKILL.md](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/payments-checkout/checkout-flow-optimization/SKILL.md).
- [skills/storefront-ui/product-page-design/SKILL.md](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/storefront-ui/product-page-design/SKILL.md).
- [skills/storefront-ui/faceted-navigation/SKILL.md](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/storefront-ui/faceted-navigation/SKILL.md).

Os snippets CSS, JSX e JavaScript embutidos nesses arquivos foram lidos estaticamente e não executados. Não são scripts de auditoria: descrevem implementação que pressupõe loja, plataforma, dependências ou projeto web. `Related Skills` aponta módulos complementares, que não foram auditados integralmente. README consultado parcialmente para descoberta; a alegação de avaliação Tessl mede qualidade de saída segundo o fornecedor e não demonstra aumento de conversão de uma loja. Frontmatter `date_added: 2026-03-12` é metadado do arquivo, não prova da eficácia ou atualização da orientação. O rótulo `risk: safe` não autoriza mudanças reais.

### C. Sush Padhye / Retail Marketing — derivação de Corey Haines

Revisão `bfcf7306794a070987c76a52997b9dbcf7de990b`, commit **12/10/2026 21:52:07 +11:00**, [registro](https://github.com/sushpadhye6789/retail-marketing-skills/commit/bfcf7306794a070987c76a52997b9dbcf7de990b). [LICENSE MIT](https://github.com/sushpadhye6789/retail-marketing-skills/blob/bfcf7306794a070987c76a52997b9dbcf7de990b/LICENSE) integral: copyright 2025 Corey Haines e portions copyright 2026 Sush Padhye. A raiz reconhece origem Corey e modificações Retail; não contar como corroboração independente da mesma técnica.

Integrais: [skills/cro/SKILL.md](https://github.com/sushpadhye6789/retail-marketing-skills/blob/bfcf7306794a070987c76a52997b9dbcf7de990b/skills/cro/SKILL.md), v2.3.0; [references/form.md](https://github.com/sushpadhye6789/retail-marketing-skills/blob/bfcf7306794a070987c76a52997b9dbcf7de990b/skills/cro/references/form.md); [references/experiments.md](https://github.com/sushpadhye6789/retail-marketing-skills/blob/bfcf7306794a070987c76a52997b9dbcf7de990b/skills/cro/references/experiments.md). README consultado parcialmente. As muitas skills relacionadas de ofertas, compliance, conteúdo, aquisição e estratégia não foram lidas nesta frente, portanto não se presume avaliação de todo o ecossistema. O núcleo referencia documentos `.agents/` da instalação original; adaptar para os materiais efetivamente fornecidos no Studio, sem exigir esses caminhos ou gerar uma estratégia inteira para revisar uma PDP.

### D. Nexscope AI — reuso da família já pesquisada

Revisão `ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e`, commit **26/08/2026 16:09:44 +08:00**, [registro](https://github.com/nexscope-ai/eCommerce-Skills/commit/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e). [LICENSE MIT](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/LICENSE) integral, copyright 2026 Nexscope AI. Integrais: [shopify-conversion-optimization/SKILL.md](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/shopify-conversion-optimization/SKILL.md) e [ecommerce-checkout-optimization/SKILL.md](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/ecommerce-checkout-optimization/SKILL.md).

Shopify é uma lista curta de capacidades, sem frontmatter e sem processo executável. Checkout tem briefing e formato de saída, mas anuncia frameworks abaixo que não fornece. Não exige recurso auxiliar nestes dois arquivos. Nenhum dos dois foi instalado. A cobertura de plataformas e a promessa de recomendações acionáveis não comprovam procedimentos específicos atuais.

## Componentes comparados

| Fonte / arquivo → componente | Contribuição concreta | Decisão | Motivo e adaptação |
|---|---|---|---|
| AdLume PDP → Before analysis / Workflow | Liga tipo de comprador e origem de tráfego às informações de decisão; diferencia informação ausente de texto fraco | Aproveitar | Evita reescrita cosmética quando faltam compatibilidade, medidas, variantes, entrega ou comprovação |
| AdLume PDP → Mine objections | Reviews, tickets e devoluções geram perguntas que a página precisa responder | Adaptar | Deidentificar materiais; conferir autenticidade e contexto. Frequência em amostra não representa toda a clientela |
| AdLume checkout → Map path / editable or locked | Mapeia etapas e confirma limites de plataforma antes da correção | Aproveitar | Uma observação útil precisa resultar em mudança possível. Registrar o ponto exato e não presumir acesso ao painel |
| AdLume checkout → screenshots not proof / smallest fix | Diagnóstico proporcional à evidência e correção pequena | Aproveitar com precisão | Um print mostra o estado visível. Nem toda característica é fricção observada, e nenhuma mostra sozinha perda causal |
| AdLume search → three failures | Distingue falta de produto, nome diferente e falha da busca | Aproveitar | Evita comprar estoque para uma demanda já atendida ou trocar sortimento quando falta sinônimo |
| AdLume search → clusters / volume covered | Uma regra útil para várias consultas antes de correções isoladas | Adaptar | Volume mínimo depende da janela/catálogo; examinar relevância, disponibilidade e segmentos, sem projetar vendas |
| AdLume search → export mandatory | Análise de demanda exige consultas e resultados registrados | Adaptar | Sem export, declarar essa análise pendente; ainda é possível revisar a experiência visível de busca/navegação |
| AdLume output-standard → fields | Evidência, confiança, consequência, esforço, decisão e dado ausente | Adaptar | Resposta curta usa só campos que ajudam. Tabela completa sob demanda; impacto pretendido separado de efeito demonstrado |
| Finsi checkout → platform first | Prefere configurações e capacidades nativas a criar checkout próprio | Aproveitar princípio | Conferir plataforma, plano, versão e restrições atuais antes de indicar caminho/menu/app |
| Finsi checkout → forms | Campos necessários, preenchimento assistido, teclados, erros próximos e informação preservada | Adaptar | Avaliar manual fallback, dados locais e exigências reais de entrega/pagamento. Não retirar campo necessário pelo número de campos |
| Finsi PDP → variants/gallery | Imagem correspondente à variante, disponibilidade, preço e controles semânticos | Adaptar | Brief utilizável sem transportar JSX. Seleção indisponível tem explicação e alternativas; teclado e acessibilidade verificados depois |
| Finsi facets → state/counts/clear | Filtros aplicados visíveis, limpar, contagens coerentes, voltar e links compartilháveis | Aproveitar como critérios | Não exige Algolia ou URL indexável; distinguir navegação útil de estratégia SEO de facetas |
| Finsi mobile → drawer/sticky | Opções de filtro e compra acessíveis em tela pequena | Adaptar | Drawer/sticky são hipóteses de solução: não cobrir conteúdo, erros, teclado ou políticas; testar uso na loja real |
| Finsi metas / benchmarks / claims | 70%, 50–60%, limiares de 50 SKUs e percentuais de uso/conclusão | Descartar como regra | Denominadores e contextos diferentes; volume/estrutura/intenções não permitem gatilho ou promessa universal |
| Finsi apps / snippets | Detalhes de implementação e fornecedores | Descartar do núcleo | Inclui recomendações antigas, preços e funcionalidades não verificados; não instalar app por checklist |
| Finsi PDP → recent purchases/badges | Prova e confiança perto da decisão | Adaptar seletivamente | Reviews, garantias e certificações só com origem verdadeira e aplicabilidade. Popups de compra recente não são obrigação |
| Retail cro → initial context/message match | Reutiliza posicionamento e combina promessa do anúncio com página | Aproveitar | Contexto existente economiza entrevista; divergência pode explicar expectativa, mas efeito continua hipótese |
| Retail form → labels/errors | Rótulos persistentes, erro específico, foco e entradas mantidas | Aproveitar | Critérios de interação concretos; não exige redesenho nem formulário com número arbitrário de etapas |
| Retail form → fixed completion reductions | Perdas percentuais por quantidade de campos | Descartar | Não há estudo/contexto suficiente no arquivo; não calcular receita ou lift com esses números |
| Retail experiments → idea menu | Mostra que layout/copy podem ser hipóteses em vez de fatos | Adaptar | Carregar para lacuna real, não gerar dezenas de testes, popups, redução de navegação ou badges por padrão |
| Nexscope Shopify/Checkout → coverage | Lembra entrega/custo, conta, pagamento e mobile | Adaptar como cobertura | Pouca profundidade para fundar método; benchmark e lista não provam correção nem suporte à plataforma |
| Nexscope → bundled questionnaire / promotion | Perguntas fixas e divulgação de fornecedor | Descartar | Perguntar apenas lacunas materiais; remover recomendações comerciais sem necessidade da loja |

## Divergências e erros que impedem adoção literal

**Checkout inteiro contra correção pequena.** Finsi leva rapidamente a one-page checkout, apps e integrações; AdLume começa pela etapa e limite real. Preferir a segunda abordagem. A quantidade de páginas não basta para julgar esforço: formular corretamente um CEP e corrigir um erro preservando dados pode importar mais que condensar etapas.

**Confiança sobre observação contra confiança sobre efeito.** Exemplos AdLume associam `high confidence` a custos revelados tarde ou compatibilidade ausente. Conservar confiança de que o estado foi visto/documentado; a magnitude do efeito sobre compra permanece desconhecida. `conversion` deve indicar a consequência que se pretende investigar, não uma perda quantificada já provada.

**Busca versus composição do público.** AdLume recomenda conferir searchers versus non-searchers. Essa comparação descreve grupos com intenções possivelmente diferentes; não demonstra que usar a busca causou maior conversão. Zero resultado também pode decorrer de indisponibilidade, erro de digitação ou produto fora de escopo. Uma consulta pode conter informação pessoal: reduzir e deidentificar os registros necessários.

**Orientação técnica envelhecida.** Finsi indica `checkout.liquid` e Google Optimize. A [documentação Shopify](https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid), consultada em 12/10/2026, informa que `checkout.liquid` não é suportado nas etapas Information, Shipping e Payment e registra o encerramento também nas páginas pós-compra. O [Google](https://support.google.com/analytics/answer/12979939), consultado na mesma data, informa que Optimize e Optimize 360 deixaram de existir em 30/09/2023. Não portar esses procedimentos. A frente de mensuração escolhe ferramentas de experimento conforme disponibilidade real.

**UX de filtros não resolve indexação.** Finsi contém `rel="noindex"`, que não é uma diretiva válida de indexação, e recomenda URLs de facetas rastreáveis de modo genérico. Aproveitar somente estado e interação. A [documentação Google sobre noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), atualizada em 10/12/2025 e consultada em 12/10/2026, descreve meta tag ou cabeçalho HTTP. Decisões de indexação, canonical e robots pertencem à análise SEO com documentação apropriada; não tornar cada combinação indexável automaticamente.

**Abandono não é sinônimo de fricção.** Dados de abandono agregam pesquisa de preço, compra futura, comparação, falta de intenção, indisponibilidade, custos e falhas técnicas. A especialista deve delimitar o evento, período, dispositivo, denominador e caminho. Não multiplicar todo carrinho abandonado por ticket para declarar receita recuperável. Benchmark externo é contexto com definição, população e data; não uma meta da loja.

## Síntese autoral para a futura skill

Núcleo curto, sem pontuação de CRO ou questionário obrigatório:

1. Reconhecer a decisão: revisar uma página, encontrar uma falha, entender abandono, melhorar mobile/busca ou preparar um teste. Reaproveitar materiais existentes; perguntar só lacuna determinante.
2. Delimitar superfície, produto, público/intenção, dispositivo e capacidade de edição. Não exigir funil completo para responder uma dúvida local.
3. Inspecionar o material autorizado e mapear o trecho pertinente: encontrar → escolher → entender variante/condições → carrinho → dados/entrega → pagamento. Declarar páginas e estados não vistos.
4. Separar ocorrência observada, interpretação/hipótese e efeito causal. Conectar cada recomendação à pergunta do comprador ou à tarefa bloqueada.
5. Priorizar pelo problema concreto, cobertura, confiança, esforço e restrições da loja; escolher uma correção pequena e explicar como verificar. Produzir resposta direta, brief ou tabela conforme o pedido.

Referências sob demanda propostas: `jornada-pdp.md` (informação para decisão, variantes, compatibilidade, imagens, prova e políticas); `carrinho-checkout.md` (totais, entrega, conta, opções de pagamento, erros e limites de plataforma); `busca-navegacao-mobile.md` (classificação de consultas, facetas e tarefas em tela pequena); `evidencias-e-entrega.md` (graus de evidência, brief e aceites). São nomes conceituais para organização posterior, não arquivos implementados nesta rodada. Estatística, mensuração e desenho de experimento entram pela frente dedicada.

Exemplo de entrega curta: “Nos prints mobile fornecidos, o preço final só aparece depois do endereço e o erro de CEP apaga a entrada. O primeiro ponto pode gerar surpresa; o segundo é uma falha de interação observada no material. Proponho preservar os dados e apresentar estimativa de frete antes, quando a plataforma permitir. Ainda não sabemos quanto isso afeta compras; medir erro de CEP e conclusão do checkout no mesmo contexto.” Nenhum caso de loja foi executado para validar esse exemplo.

## Recursos, dependências e futura aceitação

Para o núcleo proposto, texto e materiais fornecidos bastam. Não exigir heatmap, gravação, login ou ferramenta paga para uma revisão qualitativa. Navegação pública só quando necessária e dentro da autorização; prints representam apenas os estados capturados, e leitura do HTML pode não reproduzir variantes, custo por endereço ou experiência móvel.

Nenhum script desta seleção trouxe um benefício determinístico que justifique incorporá-lo ao núcleo: os códigos Finsi são exemplos de implementação, não analisadores de jornada. Se no futuro surgir recorrência que justifique um helper — por exemplo, agrupar consultas com sinônimos em export extenso — definir antes entrada/saída, privacidade, ganhos concretos e casos de erro. Se faltar dependência necessária, oferecer instalação em linguagem simples e executá-la somente com autorização; não pedir ao não desenvolvedor que rode comandos. Se existir atrito repetido, oferecer adaptação própria com um aceite concreto, em vez de construir automação preventiva.

Aceites futuros, **não executados nesta pesquisa**:

- Prints/URLs de uma PDP sem analytics produzem perguntas não respondidas e brief rastreável, sem estimativa de lift ou obrigação de reescrever tudo.
- Fluxo mobile com erro documentado produz correção específica e preservação de dados como critério; compra/pagamento real exige escopo e autorização próprios.
- Export de busca distingue sinônimo, indisponibilidade e ausência de sortimento, com janela, cobertura e dados ausentes; não converte consultas em previsão de vendas.
- Loja com checkout restrito recebe opção que sua plataforma permite; não recomenda arquivo descontinuado, migração ou compra de app como ação automática.
- Reviews, estoque, garantia e certificados só entram com origem, verdade e aplicabilidade verificáveis; nada de escassez ou prova fabricada.
- Dossiê e bibliografia ficam fora do núcleo executável. Se código/texto de terceiros for redistribuído, preservar os avisos MIT aplicáveis e a autoria real; síntese autoral não torna terceiros autores SquadOS.

## Estado e limites

Pesquisa estática dos nove SKILL e dos recursos decisivos descritos, com proveniência fixada. Não foi feita auditoria de segurança de todos os repositórios, instalação de pacote, render de exemplos, teste de integrações ou demonstração de resultado de CRO. Os snippets, preços de apps, caminhos de menus e alegações de efeito não foram validados em uma loja real. Não foram alterados catálogo, Desktop, conta, políticas, pagamentos, campanhas ou experimentos. Compatibilidade com a proposta nativa de contratação do Studio e execução real permanecem etapas futuras, separadas da qualidade documental desta pesquisa.
