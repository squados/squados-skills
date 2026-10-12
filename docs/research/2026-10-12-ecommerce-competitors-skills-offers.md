# Pesquisador de Concorrentes de Ecommerce — produtos e ofertas

Data da consulta: 12/10/2026. Frente da rodada 21/33: descobrir e comparar componentes de skills existentes para produtos, variantes, preços, promoções, frete, prazo, vendedor e condições. Pesquisa documental; nenhuma skill, coletor, conta, compra, publicação ou monitor recorrente foi executado ou instalado.

## Decisão principal

Adotar como referência de método a normalização de ofertas de **competitive-pricing-strategy**, do Nexscope, e a separação entre descoberta, leitura e observação de **ai-ecommerce-workflow**, de Ethan/mianbaofang. Usar a família de templates de sam6dvpte34 para conferir cobertura de campos, sem importar a dependência BrowserAct. Não aproveitar projeções de participação de mercado, elasticidade ou ROI de uma fotografia de preços, nem o runtime incompleto do ecommerce-competitor-analyzer de Buluslan.

O trabalho começa por “qual oferta realmente concorre com a nossa?”, e termina em diferença observada, consequência para o comprador e decisão sustentada. Uma faixa vazia de preço é um achado da amostra, não prova de demanda. Menor preço anunciado não garante melhor custo entregue nem maior conversão.

## Alcance, seleção e deduplicação

Busca pública por `github SKILL.md ecommerce competitor price comparison shopping skill` e `github agent skill product price comparison competitors variants shipping`. Resultados levaram aos repositórios originais. skills.sh foi apenas descoberta. Não se usaram instalações, estrelas ou texto promocional como validação.

Foram lidos integralmente dez SKILL.md de domínio: três Nexscope, seis sam6dvpte34 e um ai-ecommerce-workflow; mais o SKILL.md do Buluslan e o stub da dependência browser-act. Isso representa **quatro famílias de autoria de domínio**, não onze provas independentes. Os seis templates sam6dvpte34 repetem quase todo o método: os campos e pequenas diferenças são complementares, mas não demonstram seis abordagens distintas. Os três Nexscope têm autoria e repositório comuns. BrowserAct é dependência, não mais uma especialista de ecommerce.

Firecrawl competitor-analysis, habilidades gerais de Market Research, Procurement e SEO não foram contadas como novas. ecommerce-competitor-analysis do Nexscope ficou com a frente de posicionamento. Hermes price-monitor já pertence ao catálogo: possível reuso, sem nova contagem ou integração presumida. A frente de métodos cobre padrões profissionais e casos; este documento não duplica esse papel.

SHA foi obtido com `git ls-remote ... HEAD`; conteúdos decisivos foram consultados por raw fixado quando indicado abaixo. A API GitHub anônima retornou rate limit; a leitura continuou por raw e páginas HTML de diretório, sem novas tentativas da API, clones ou temporários. Não foram feitas chamadas às APIs de comércio anunciadas pelas skills.

## Registro de fontes e arquivos efetivamente lidos

### A. Nexscope AI — família ecommerce-skills

Revisão: `ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e`. Autoria declarada: Nexscope; [LICENSE MIT](https://github.com/nexscope-ai/ecommerce-skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/LICENSE), copyright 2026 Nexscope AI, lido. O frontmatter destas três skills não repete a licença; a base é a licença do repositório nessa revisão.

- [competitive-pricing-strategy/SKILL.md](https://github.com/nexscope-ai/ecommerce-skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitive-pricing-strategy/SKILL.md), integral; `agents/openai.yaml`, integral, só identidade e prompt de descoberta.
- [competitor-price-analysis/SKILL.md](https://github.com/nexscope-ai/ecommerce-skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitor-price-analysis/SKILL.md), integral.
- [competitor-price-tracker/SKILL.md](https://github.com/nexscope-ai/ecommerce-skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitor-price-tracker/SKILL.md), integral.

Páginas HTML das três pastas foram usadas para conferir recursos locais: price-analysis e price-tracker listam apenas SKILL.md; competitive-pricing-strategy também lista `agents/`. Não há coletor ou motor de repricing demonstrado nos arquivos lidos. O README foi consultado pela descoberta pública para identificar as candidatas; sua classificação “production-ready” não serve como evidência de execução.

**competitive-pricing-strategy** é a candidata mais consistente: usa materiais fornecidos primeiro, distingue confirmado/hipótese/desconhecido, registra instante e origem, compara quantidade, condição, acessórios, vendedor e logística. Separa cupom, crédito de fidelidade, impostos e benefícios de associação quando o tratamento não está confirmado. Para estratégia de preços, exige custos do vendedor e reconhece limites causais. Estas capacidades estão descritas em instruções, sem execução nesta pesquisa.

Seu conceito de preço entregue deve ser adaptado ao Brasil: pagamento, imposto obrigatório, região/CEP, benefício condicionado e moeda fazem parte da comparação. A fórmula da fonte não basta para toda situação. Custos internos, contribuição e preço mínimo só são relevantes quando o pedido incluir decisão de preço e houver dados autorizados; não devem travar uma simples comparação concorrencial.

**competitor-price-analysis** tem formato amplo, mas inclui estimativas de market share, elasticidade, projeções de receita e margem sem método suficiente no arquivo. A seção final reconhece parte desses limites, mas não elimina o risco de o template pedir números inexistentes. Não tratar como versão equivalente da skill acima.

**competitor-price-tracker** é uma orientação curta, sem framework detalhado, coletor, armazenamento ou alerta implementado. Suporta um resumo e ações priorizadas; suas promessas de tracking não demonstram monitoramento funcionando.

### B. sam6dvpte34 — Ecommerce Skill e dependência BrowserAct

Revisão: `68b33a5aa8520d10d82479a8fd57d540fd0f9b8c`. Autoria declarada no frontmatter: sam6dvpte34, versão 0.1.0; README descreve manutenção independente, não autoria BrowserAct. README integral e os seis arquivos abaixo foram lidos integralmente:

- [ecommerce-price-comparison-research](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/ecommerce-price-comparison-research/SKILL.md).
- [ecommerce-product-variant-scraper](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/ecommerce-product-variant-scraper/SKILL.md).
- [ecommerce-shipping-fee-scraper](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/ecommerce-shipping-fee-scraper/SKILL.md).
- [marketplace-shipping-promise-monitor](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/marketplace-shipping-promise-monitor/SKILL.md).
- [ecommerce-promotion-deal-scraper](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/ecommerce-promotion-deal-scraper/SKILL.md).
- [ecommerce-seller-profile-scraper](https://github.com/sam6dvpte34/ecommerce-skill/blob/68b33a5aa8520d10d82479a8fd57d540fd0f9b8c/skills/ecommerce-seller-profile-scraper/SKILL.md).

Todos declaram `license: MIT`; não foi encontrado LICENSE raiz na URL testada (404), portanto não presumir inventário completo de avisos ou liberação de outros recursos. A declaração permite identificar intenção de licença; qualquer redistribuição de texto exige resolver o aviso completo e preservar autoria. Nesta entrega há síntese própria, sem cópia do pacote. A página HTML da pasta price-comparison lista somente SKILL.md. Não se verificou todo o acervo de 185 itens e 49 plataformas anunciado no README.

Contribuição útil: campos de oferta e contexto; referências de origem; IDs/URLs estáveis para deduplicar; resultado direto; declarar falha em vez de inventar registros. Promoções incluem elegibilidade e prazo; shipping-promise inclui região, retirada, fulfillment e snapshot anterior fornecido. Limites: os templates não detalham equivalência de variante, CEP obrigatório para custo entregue, empilhamento de cupom ou histórico independente. Rating e seguidores são informações visíveis de reputação, não prova de vendas ou participação.

Dependência determinante: [browser-act/SKILL.md](https://github.com/browser-act/skills/blob/11c057b03f92101642cadc9f840564574120d184/browser-act/SKILL.md), revisão `11c057b03f92101642cadc9f840564574120d184`, integral; LICENSE MIT copyright 2026 BrowserAct integral; README consultado com saída parcial, sem base para avaliação integral do runtime. O stub declara Python 3.12+, uv, CLI externo, acesso de rede, perfis e logs locais; exige confirmação de instalação inicial e operações sensíveis. As seis skills de ecommerce mandam instalar automaticamente sem confirmação: divergência concreta entre wrapper e dependência. Nenhuma dessas instruções externas foi executada.

O verdadeiro fluxo é fornecido por `browser-act get-skills core`, não pelo stub. Não foi obtido: exigiria runtime/execução fora do escopo. Assim, dependência funcional, privacidade operacional, custo e compatibilidade com Studio permanecem **não demonstrados**. O método de pesquisa pode usar ferramentas disponíveis; não precisa incorporar BrowserAct, proxy, CAPTCHA ou outra instalação para existir.

### C. Ethan/mianbaofang — AI Ecommerce Workflow

Revisão: `679b3b67f01ab52be6998f7cdc3fd714dcfafd26`. [LICENSE MIT](https://github.com/mianbaofang/ai-ecommerce-workflow/blob/679b3b67f01ab52be6998f7cdc3fd714dcfafd26/LICENSE) integral, copyright 2026 Ethan. Arquivos integrais:

- [skills/ai-ecommerce-workflow/SKILL.md](https://github.com/mianbaofang/ai-ecommerce-workflow/blob/679b3b67f01ab52be6998f7cdc3fd714dcfafd26/skills/ai-ecommerce-workflow/SKILL.md).
- [references/public-search-policy.md](https://github.com/mianbaofang/ai-ecommerce-workflow/blob/679b3b67f01ab52be6998f7cdc3fd714dcfafd26/skills/ai-ecommerce-workflow/references/public-search-policy.md).
- [references/research-evidence-ledger.md](https://github.com/mianbaofang/ai-ecommerce-workflow/blob/679b3b67f01ab52be6998f7cdc3fd714dcfafd26/skills/ai-ecommerce-workflow/references/research-evidence-ledger.md).

Referências de copy, imagens e compliance de listing não foram lidas: não determinam a comparação de ofertas desta frente e nenhum componente delas está sendo aprovado. A fonte tem escopo maior, mas a contribuição selecionada limita-se a pesquisa pública e evidência.

Aceita nome, URL ou imagem sem ficha longa; pesquisa primeiro, pergunta quando material; entrega uma página de conclusão antes de expandir. A referência de evidência registra status de leitura, URL, query, observação com fuso, mercado, moeda, valor observado, lacuna e uso. Distingue preço observado de transação e resultado de busca de ranking orgânico estável. Não atribui material, eficácia ou certificação a uma imagem sozinha.

Adaptar para abandonar perguntas de setup por rotina na primeira interação: a intenção do usuário e ferramentas disponíveis já orientam o caminho. Ler corpo público selecionado quando necessário; guardar só evidência pertinente. O limite “5–8 concorrentes/3–6 consultas” é orientação da fonte, não quota universal nem critério de parada.

### D. Buluslan — ecommerce-competitor-analyzer

Revisão: `853c7102b76940be78422ac765fb98a22e76f206`. Autoria: Buluslan@新西楼.AI; SKILL versão 1.0.1. [SKILL.md](https://github.com/buluslan/ecommerce-competitor-analyzer/blob/853c7102b76940be78422ac765fb98a22e76f206/SKILL.md) integral; LICENSE MIT copyright 2026 Buluslan@新西楼Newest AI lido inicialmente por HEAD correspondente ao SHA observado; sem data individual de commit verificada. Recursos integrais fixados:

- [platforms.yaml](https://github.com/buluslan/ecommerce-competitor-analyzer/blob/853c7102b76940be78422ac765fb98a22e76f206/platforms.yaml).
- [prompts/analysis-prompt-base.md](https://github.com/buluslan/ecommerce-competitor-analyzer/blob/853c7102b76940be78422ac765fb98a22e76f206/prompts/analysis-prompt-base.md).
- [scripts/scrape-amazon.js](https://github.com/buluslan/ecommerce-competitor-analyzer/blob/853c7102b76940be78422ac765fb98a22e76f206/scripts/scrape-amazon.js).
- [scripts/batch-processor.js](https://github.com/buluslan/ecommerce-competitor-analyzer/blob/853c7102b76940be78422ac765fb98a22e76f206/scripts/batch-processor.js).

É um contraponto implementado, não só texto, porém o conteúdo consultado não comprova funcionamento completo. O runtime pede Olostep, Gemini e Google Sheets/credenciais. A descrição cita Amazon/Temu/Shopee; configuração mantém Temu/Shopee desabilitados e SKILL esclarece MVP Amazon US. Preços de serviços e tempos do README/SKILL são alegações da fonte, não valores atuais validados.

Achados estáticos que desaconselham copiar:

- `getAnalysisPrompt()` devolve placeholder em vez de ler o prompt prometido.
- `formatForGoogleSheets()` produz linhas; arquivo lido não executa gravação Sheets.
- `processBatch()` é sequencial, apesar da orientação geral de paralelismo; passa `item` diretamente ao scraper e não chama `extractASIN()` nesse caminho.
- O domínio default é amazon.com; ASIN extraído de outra região não preserva automaticamente mercado original.
- Timeout declarado no scraper não é aplicado ao fetch no código consultado.
- Preço e rating são extraídos por regex de **texto gerado pelo modelo**, com perda de moeda/contexto; isto não deve substituir fato coletado da página.
- Prompt pede oscilações de preço e ranking sem obrigar snapshots; o caminho lido só busca a página atual.
- A promessa de imagens não comprova leitura visual: pipeline observado passa conteúdo Markdown ao modelo; não há envio de imagem nessa chamada.

Aproveitar apenas isolamento de falha por produto e resumo de sucessos/lacunas como ideia; reescrever no método simples, sem dependências. `references/n8n-workflow-analysis.md` e origem n8n v81 não foram auditadas. Nenhum benchmark anunciado foi reproduzido.

## Matriz fonte → componente → decisão

| Fonte/arquivo | Componente | Decisão | Motivo e adaptação |
|---|---|---|---|
| A / competitive-pricing-strategy | Normalização por variante, pack, condição e itens incluídos | Aproveitar método | Evita comparar outro produto como concorrente de preço; confirmar identidade antes de calcular |
| A / competitive-pricing-strategy | Preço entregue e unitário | Adaptar | Incluir CEP/região, pagamento, impostos obrigatórios confirmados e unidade de comparação; sem frete observado, total desconhecido |
| A / competitive-pricing-strategy | Separação de descontos do vendedor/plataforma e associação | Aproveitar método | Oferta universal e condicionada aparecem separadas; não subtrair cashback como desconto imediato |
| A / competitive-pricing-strategy | Custos, contribuição e piso | Sob demanda | Depende de dados internos; não impor à comparação pública nem estimar margem do rival |
| A / competitive-pricing-strategy | Respostas a desconto/ruptura/entrante | Adaptar | Diagnosticar equivalência, duração e estoque primeiro; recomendação não muda preço vivo |
| A / competitor-price-analysis | Faixas e clusters de preço | Adaptar | Descrever a amostra comparável e seus limites; sem converter frequência de anúncio em share |
| A / competitor-price-analysis | Elasticidade, market share, ROI projetado | Descartar padrão | Não há estimador nem dados necessários; fotografia pública não sustenta causalidade |
| A / competitor-price-tracker | Resumo e ações priorizadas | Aproveitar ideia | Curto e utilizável; recorrência depende de pedido/autorização e execução separada |
| A / três skills | Handoff comercial Nexscope obrigatório | Descartar | Divulgação do fornecedor não melhora comparação; APIs não usadas nem validadas |
| B / price-comparison | Referência, timestamp e dedup por IDs/URL | Adaptar | Chave precisa conter variante/oferta/vendedor/mercado; URL da página pai sozinha perde diferenças |
| B / variant | Lista de opções e disponibilidade | Adaptar | Registrar variante selecionada; “a partir de” não vale como preço de todas as opções |
| B / shipping e promise | Frete, promessa, retirada e fulfillment | Adaptar | Informar destino e instante; promessa observada não é entrega real garantida |
| B / promotion | Elegibilidade, prazo, preço de e preço atual | Adaptar | Preservar condições e não validar “de” como histórico real sem evidência |
| B / seller-profile | Vendedor, reputação, políticas | Adaptar | Distinguir marca, plataforma e merchant; métricas visíveis não comprovam performance econômica |
| B / runtime + browser-act | Autoinstalação e dependência de CLI | Descartar | Conflito entre arquivos e custo de instalação; só considerar necessidade concreta posterior |
| C / SKILL | Entrada natural e conclusão de uma página | Aproveitar método | A pessoa não escolhe modo nem preenche inventário; aprofundar conforme decisão |
| C / ledger e policy | Descoberta/leitura/falha e preço observado | Aproveitar método | Impede transformar snippet, imagem ou memória em fato confirmado |
| C / setup e quotas | Pergunta inicial de provider e contagem fixa | Descartar padrão | Atrito sem necessidade; parar quando dúvidas materiais resolvidas |
| D / scripts | Falha isolada e lista de incompletos | Aproveitar ideia | Uma página bloqueada não elimina restantes; lacunas permanecem no relatório |
| D / scripts e prompt | APIs obrigatórias, regex após IA, histórico implícito | Descartar | Custo, dependências e fragilidade; código incompleto não serve como runtime pronto |

## Proposta mínima de execução para a futura skill

Reconhecer pelo pedido se a pessoa quer uma comparação pontual, mapear concorrentes de uma categoria ou compreender uma diferença observada. Começar por URLs, SKU, nome, planilha ou captura fornecidos; pesquisar sem exigir a escolha de abordagem. Fazer uma pergunta curta se destino, variante ou condição alterar a resposta. Sem esse detalhe, avançar com o que pode ser comparado e declarar o que fica bloqueado.

1. Fixar objeto e decisão: produto/variante, canal/região, concorrentes indicados e o que a comparação deve apoiar.
2. Identificar ofertas equivalentes, substitutas e excluídas, com motivo. Modelo/GTIN ajudam; SKU é frequentemente interno ao vendedor e não prova equivalência entre lojas. ASIN de produto pai não dispensa variante. Tamanho, cor relevante, capacidade, pack, condição, garantia e acessórios mudam equivalência.
3. Ler fontes selecionadas e preservar vendedor, preço, disponibilidade, promoção, frete/prazo e contexto. A publicidade pode ajudar a descobrir, mas afirmações finais devem apontar à página ou material efetivamente lido.
4. Calcular apenas grandezas com insumos compatíveis. Custo entregue = preço aplicável à condição analisada + cobranças obrigatórias conhecidas − desconto imediato confirmado. Cashback, parcelamento e benefício dependente de conta permanecem campos separados. Comparar preço unitário só dentro de unidade e configuração equivalentes.
5. Entregar conclusão curta, tabela de ofertas e diferenças decisivas; listar incertezas que mudam a decisão. Disponibilidade vencida, sold out ou frete desconhecido impedem chamar uma oferta de melhor compra entregue.

Campos mínimos devem aparecer conforme relevância, sem impor formulário: fonte/data; produto/GTIN/modelo/SKU observado; variante/tamanho/capacidade/pack/condição; merchant e plataforma; preço atual/moeda/preço de; pagamento; desconto/cupom e elegibilidade; disponibilidade; região/CEP; frete, retirada, fulfillment e prazo; total conhecido; comparabilidade e lacuna. Identificadores ausentes permanecem ausentes. Não inferir garantia, estoque, imposto ou reputação a partir do título.

**Núcleo conciso:** equivalência, condições completas, origem/instante, desconhecidos, conclusão proporcional e capacidade de oferecer melhoria da própria skill. **Referências sob demanda:** comparação de variantes/packs; promoções e pagamento; destino/logística; marketplaces/vendedores; reobservação/histórico; decisão de preço com dados internos. Bibliografia e histórico desta pesquisa ficam no dossiê, fora do núcleo executável.

Não criar scripts de scraping, conta, API ou cron por padrão. Um script pequeno de cálculo/deduplicação pode ser útil em CSV grande e repetido, mas só quando houver ganho mecânico real e insumos seguros. Se faltar ferramenta necessária a uma entrega concreta, explicar benefício e oferecer cuidar da instalação em linguagem de trabalho; usar autorização anterior se existir. A alternativa sem instalação deve manter explícita a limitação, sem prometer execução.

Se a pessoa repetir a preferência “sempre comparar o custo entregue para nosso CEP e pagamento à vista”, oferecer ajustar sua versão da skill, com aceite antes de mudar: reduz repetição e erros concretos. Essa preferência local não vira regra publicada para toda a galeria. Recorrência de pesquisa deve ser oferecida quando houver demanda, e só configurada após autorização; esta pesquisa não criou monitor.

## Casos para futura avaliação — não executados

| Pedido/cenário | Comportamento esperado | Falha que deve ser detectada |
|---|---|---|
| “Qual rival vende este modelo mais barato?”; 128 GB vs 256 GB | Separar variantes e comparar equivalentes | Usar preço de entrada da página como preço do 256 GB |
| Pacote de 6 × 500 ml vs 1 × 3 l | Calcular por litro e explicar embalagem/uso | Concluir que packs são substitutos perfeitos sem contexto |
| Desconto Pix vs cartão parcelado e cupom de primeira compra | Colunas de condições e duas conclusões se relevante | Subtrair cupom indisponível ou cashback do total imediato |
| R$ 150 + frete versus R$ 165 com frete anunciado grátis | Pedir/aproveitar CEP; total indeterminado se não há destino | Inventar frete ou eleger vencedor entregue |
| Mesmo marketplace, sellers diferentes; novo vs recondicionado | Merchant, condição, garantia e fulfillment visíveis | Misturar marca/plataforma/vendedor |
| “De R$ 299 por R$ 199”, sold out | Registrar referência exibida e indisponibilidade | Chamar referência de preço histórico ou promoção comprável |
| Duas capturas com data/região iguais, variante diferente | Não classificar como queda de preço do mesmo item | Produzir alerta com falso comparável |
| Uma página bloqueada, três legíveis | Entregar comparação parcial e identificar impacto | Omitir página sem dizer ou inventar registro |
| Imagem reconhecida sem modelo verificável | Tratar como candidato semelhante, com dúvida | Afirmar GTIN, material, certificação ou preço sem fonte |
| Categoria com muitos anúncios baratos e ratings elevados | Descrever distribuição observada | Inferir share, conversão, margem ou elasticidade |

## Estado e dúvidas residuais

As dúvidas de método desta frente estão resolvidas para orientar uma proposta: equivalência, condição comercial, evidência e saída progressiva. Ampliar diretórios não agregaria outra decisão material agora. Faltam criação da futura skill, avaliação dos casos, validação de pacote, integração com ferramentas disponíveis, proposta nativa revisável, contratação e execução real — etapas distintas, não cumpridas pela leitura documental.

Nenhum conteúdo externo foi copiado para `skills/`, nenhum item de galeria foi alterado. Para redistribuir texto de qualquer fonte, confirmar licença/avisos na revisão pretendida e manter atribuição; no acervo sam6dvpte34 a ausência de LICENSE raiz continua uma lacuna de empacotamento. Não afirmar compatibilidade Studio dos runtimes externos ou custo atual de APIs com base no material lido.
