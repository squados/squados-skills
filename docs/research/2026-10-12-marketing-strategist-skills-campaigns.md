# Pesquisa de skills: campanhas, lançamentos e canais

Consulta: **12/10/2026**. Destino: futura Estrategista de Marketing interna, em PT-BR, para negócios variados. Entrega desta pesquisa: decisões sustentadas por fontes e lacunas; nenhuma skill foi criada, instalada ou executada. Catálogo e runtime não foram modificados.

## Método e alcance

Metodologia: `skills/skill-manager/references/research.md`. Descoberta no skills.sh; leitura primária por GitHub e HTTPS bruto. Foram lidos integralmente os seis SKILL.md abaixo e os recursos comportamentais especificados. Revisões novas foram confirmadas com `git ls-remote` somente leitura; revisões Anthropic e Digital Marketing Pro já haviam sido confirmadas nesta sessão. Datas de commit foram extraídas das páginas ou patches públicos. A API pública atingiu rate limit; não foi possível obter o histórico por arquivo de todas as fontes.

O diretório não foi tratado como fonte de eficácia: instalações, estrelas e badges não medem conversão, qualidade estratégica nem segurança. Forks que atribuem launch-strategy a Corey Haines foram evitados. A amostra resolve as dúvidas de planejamento; não pretende cobrir todas as skills existentes. Posicionamento, contexto de produto e banco de ideias pertencem à outra frente da pesquisa.

**Renomeações verificadas:** o nome launch-strategy descoberto no diretório corresponde agora a `skills/launch/SKILL.md`, `name: launch`. O nome campaign-planning da Anthropic corresponde a `marketing/skills/campaign-plan/SKILL.md`, `name: campaign-plan`. Os caminhos antigos retornaram 404; o README de marketing da Anthropic ainda lista campaign-planning. Uxcel usa `pm/deliverables/gtm-plan/`, fora de `skills/`.

## Proveniência

Datas desta tabela são da **revisão do repositório**, não da última alteração individual da skill nem de teste comercial. Autor de commit não é automaticamente autor editorial. Todos os links analíticos estão congelados na revisão consultada.

| ID | Origem e autoria verificável | Revisão | Data visível / versão | Licença |
|---|---|---|---|---|
| A | Anthropic, pacote marketing de knowledge-work-plugins | `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06` | [Commit](https://github.com/anthropics/knowledge-work-plugins/commit/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06): 11/10/2026 | [Apache-2.0 do pacote](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/marketing/LICENSE), lida |
| B/C | Corey Haines, copyright nominal na licença | `1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff` | [Commit](https://github.com/coreyhaines31/marketingskills/commit/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff): 08/10/2026; launch 2.2.0, marketing-plan 1.2.1 | [MIT](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/LICENSE), lida |
| D | indranilbanerjee / Digital Marketing Pro; copyright Digital Marketing Pro | `dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8` | [Commit](https://github.com/indranilbanerjee/digital-marketing-pro/commit/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8): 12/10/2026 | [MIT](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/LICENSE), lida |
| E | Uxcel Lab; frontmatter autor uxcel | `5007cd0241ccaa51ae2e4681f9618912dc10e239` | [Commit](https://github.com/uxcel-lab/product-skills/commit/5007cd0241ccaa51ae2e4681f9618912dc10e239): 02/07/2026; skill 1.0.0 | [MIT](https://github.com/uxcel-lab/product-skills/blob/5007cd0241ccaa51ae2e4681f9618912dc10e239/LICENSE), lida |
| F | Ömer Metin / skills-for-antigravity | `e8dcf4e8737921a10088bd5c9eb65e81f74c051f` | [Commit](https://github.com/omer-metin/skills-for-antigravity/commit/e8dcf4e8737921a10088bd5c9eb65e81f74c051f): 22/01/2026 | [Apache-2.0](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/LICENSE), lida |

Essas origens não estão na allowlist github atual da galeria, inclusive o repositório Anthropic consultado, distinto de anthropics/skills. Pesquisa não autoriza empacotamento; eventual adaptação material deve preservar licenças, autoria e avisos pertinentes.

## Comparação de comportamento

| Fonte principal | Contexto e método | Entrega e dependências | Flexibilidade / limite |
|---|---|---|---|
| A — [campaign-plan](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/marketing/skills/campaign-plan/SKILL.md) | Objetivo, público, prazo e orçamento; organiza mensagem, canais e medição. | Brief, calendário retroativo às dependências, lista de peças e métricas; dados conectados opcionais. | Orçamento ausente permite plano sem alocação. Defaults de frequência, produção e porcentagem de investimento não trazem evidência específica do cliente. Classifica perfis sociais como owned, diferente de B. |
| B — [launch](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/launch/SKILL.md) | Oferta lançada, canais existentes, prazo e histórico; distingue canais próprios, alugados e emprestados. | Fases de lançamento e sustentação; refs de site e novidades publicadas. | Forte default SaaS: alpha/beta, self-service e Product Hunt. Exemplos de empresas são alegações da fonte, não resultados desta skill. |
| C — [marketing-plan](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/marketing-plan/SKILL.md) | Planejamento amplo com equipe, orçamento, estágio e histórico; organiza aquisição até receita. | Treze seções, roadmap e responsabilidades; numerosas referências e integrações opcionais. | Foco fCMO/VC/SaaS, documento extenso e aprovação seção a seção. Afirma produtividade de equipe sem evidência experimental. Dados desconhecidos devem ficar explícitos. |
| D — [campaign-plan](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/campaign-plan/SKILL.md) | Objetivo, produto, audiência, restrições; seleciona canais e organiza orçamento/prazo. | Plano com hipóteses de alcance, dependências e medição; contexto de marca e referências do plugin. | SKILL lista orçamento entre entradas requeridas; brief de apoio o torna opcional. Dispatch por canal depende de aprovação e subagentes. Benchmarks não são automaticamente locais ou atuais. |
| E — [pm-gtm-plan](https://github.com/uxcel-lab/product-skills/blob/5007cd0241ccaa51ae2e4681f9618912dc10e239/pm/deliverables/gtm-plan/SKILL.md) | Demanda, maturidade, modelo de negócio e timing; trata canal como custo e relação. | Plano e trade-offs de entrada; sugere auditorias vizinhas. | Ajusta estágios por contexto, não só clientes; respeita jornada não linear. Sem skills adjacentes instaladas, prossegue. Obrigar validação prévia pode impedir justamente o plano de teste de demanda solicitado. |
| F — [growth-strategy](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/growth-strategy/SKILL.md) | Sistemas de crescimento, retenção e loops; obriga três referências como base. | Não fixa um contrato claro de entrega; prescreve diagnóstico/revisão com padrões e validações. | Persona inventa experiência pessoal em empresas. Direciona corrigir usuário quando diverge das referências; não é postura adequada para uma colaboradora contextual. |

## Fonte → componente → decisão

Cada recurso abaixo foi lido integralmente, exceto a política Uxcel explicitamente indisponível.

| Fonte / arquivo exato | Componente aproveitável | Decisão e motivo |
|---|---|---|
| A, SKILL acima | Objetivo → público → mensagem → canais → medida; cronograma com pré-requisitos | **Aproveitar** como raciocínio e saída proporcional. **Adaptar** métricas ao objetivo. **Descartar** cadência, reserva e número de KPIs obrigatórios. |
| B — [site-launch-qa.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/launch/references/site-launch-qa.md) | Confirmar destino e conversão antes da divulgação | **Adaptar** para pré-requisitos e responsáveis; a estrategista não precisa executar crawler, DNS ou deployment. |
| B — [shipped-changes.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/launch/references/shipped-changes.md) | Anunciar apenas capacidades realmente disponíveis, com fonte | **Aproveitar** fidelidade à oferta. **Adaptar** de mudanças de código para mudanças reais do curso, produto ou serviço; redação final é handoff ao Copywriter. |
| C — [methodology.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/marketing-plan/references/methodology.md) | Aproveitar materiais, registrar premissas e reconhecer trabalho anterior | **Aproveitar** pesquisa e continuidade. **Descartar** treze aprovações, diretório obrigatório fora do projeto e publicação como extensão padrão do pedido. |
| C — [budget-planning.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/marketing-plan/references/budget-planning.md) | Orçamento viável e custos completos; projeção com premissas | **Adaptar** ao modelo de receita. O recurso distingue retenção da base/coorte nova; resumo do SKILL tem fórmula simplificada diferente. **Descartar** ARR, funding e baseline de CAC assumido como universais. |
| D — [brief-structure.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/campaign-plan/brief-structure.md) | Brief transferível e dependências entre peças | **Adaptar** tamanho ao pedido; sem obrigar menu de continuação, aprovação por canal ou delegação. |
| D — [campaign-planning.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/campaign-orchestrator/campaign-planning.md) | Meta realizável baseada em histórico ou benchmark registrado | **Aproveitar** rastreabilidade; **descartar** tabela de horas, quantidades de peças e reservas como compromissos sem estimativa local. |
| D — [channel-strategy.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/campaign-orchestrator/channel-strategy.md) | Tempo para aprender, orçamento mínimo do teste, custo de oportunidade e critério de decisão | **Aproveitar** perguntas. **Descartar** estrelas por segmento, limites de frequência e sequência fixa de semanas como recomendação comprovada. |
| D — [budget-allocation.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/campaign-orchestrator/budget-allocation.md) | Separar iniciativas comprovadas de testes e considerar CAC marginal | **Adaptar** com dados reais. **Descartar** CPC/CPM/ROAS em dólares, rankings fixos de eficiência e percentuais de pausa/escala como regra PT-BR. |
| E, SKILL acima | Maturidade contextual, sazonalidade e compras não lineares | **Aproveitar** trade-offs. **Adaptar** prontidão: quando demanda não está provada, entregar plano de validação. **Descartar** regra direta-primeiro quando o negócio já depende legitimamente de marketplace/distribuidor. |
| F — [patterns.md](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/growth-strategy/references/patterns.md) | Evitar dispersão e mapear mecanismo de crescimento | **Aproveitar** foco e mecanismo. **Descartar** retenção semanal mínima e três meses obrigatórios de canal como regra de negócios variados. |
| F — [sharp_edges.md](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/growth-strategy/references/sharp_edges.md) | Qualidade da aquisição e risco de concentração | **Adaptar** dependência à fase. Contrasta foco de 100% em um canal de patterns com teto de 40% aqui; números não solucionam a decisão contextual. |
| F — [validations.md](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/growth-strategy/references/validations.md) | Pedir hipótese, critério e prazo de experimento | **Aproveitar** perguntas; **descartar** regex como validação objetiva: presença de palavras como `and` aciona excesso de canais sem compreender conteúdo. |

## Adaptação para negócios variados

Inferências para SquadOS, a validar em pedidos representativos:

| Negócio / pedido | O que altera o planejamento | Evidência e entrega úteis |
|---|---|---|
| Curso com turma datada | Calendário de matrícula, capacidade de atendimento, objeções e condição real de oferta | Histórico de vendas, comparecimento e pagamentos; campanha de captação/matrícula com peças e prazo real. Não exigir beta SaaS nem Product Hunt. |
| Serviço local | Área atendida, agenda disponível, deslocamento, contato e conversão offline | Agendamentos e serviços realizados; teste de canal com rastreio até atendimento, sem assumir cadastro de usuário como sucesso. |
| E-commerce | Margem por produto, estoque, frete, devoluções, sazonalidade e recompra | Pedidos aprovados e margem; calendário condicionado a disponibilidade e teto de aquisição. ROAS bruto isolado não decide orçamento. |
| B2B consultivo | Comitê comprador, ciclo comercial, oportunidades e capacidade de entrega | Leads qualificados, reuniões úteis e negócios; plano de relacionamento compatível com timing do comprador, sem forçar sequência diária. |

Canais são opções condicionadas ao público, material disponível e recursos. Para uma equipe pequena, escolher poucas apostas sustentáveis; ampliar quando houver capacidade e informação. Perfis sociais permitem relacionamento direto, mas distribuição depende da plataforma: evitar confundir controle do perfil com controle do alcance.

## Limite entre especialistas

A Estrategista conecta objetivo, público, oferta, recursos, calendário e hipóteses. Seu experimento explicita o que aprender, indicador, fonte, prazo e decisão possível; reconhece incerteza e define o encaminhamento adequado quando exige cálculo estatístico ou análise aprofundada.

O Analista de Marketing e Tráfego assume investigação de performance, atribuição, coortes e eficiência com dados operacionais. Execução e alterações em anúncios pertencem ao especialista responsável e ao escopo autorizado. O Copywriter produz e refina as peças; a estrategista entrega briefing e mantém coerência da campanha. Nenhum handoff implica instalar ferramenta, publicar conteúdo ou iniciar despesa.

## Lacunas e avaliação futura

Não houve execução dos pacotes, prova de compatibilidade Hermes ou comparação controlada de resultados. Alguns materiais são prescritivos e ingleses; não demonstram funcionamento em PT-BR ou no mercado brasileiro. Limites numéricos e benchmarks aqui identificados não foram validados como aconselhamento financeiro/comercial corrente.

Não foram auditados todos os recursos de C: template completo, rubric de estado atual, mapa de operações e demais módulos. D teve os quatro recursos decisivos de planejamento lidos, mas não UTM, ABM, compliance, perfis ou agentes completos. [docs/orchestration-policy.md de Uxcel](https://github.com/uxcel-lab/product-skills/blob/5007cd0241ccaa51ae2e4681f9618912dc10e239/docs/orchestration-policy.md), citado pela skill, retornou 404; auditorias vizinhas e lições externas não foram lidas. Essas lacunas impedem aprovar os pacotes completos; não impedem comparar os componentes observados.

Aceitação futura: testar os quatro pedidos da tabela, incluindo caso com poucos dados e revisão de plano existente. Verificar adequação de escopo, decisões justificadas, oferta fiel, esforço exequível, fontes dos números, responsáveis e dependências, hipótese com decisão explícita e ausência de aprovação burocrática ou execução não pedida. Pesquisa, plano útil, skill validada e desempenho de campanha são estados separados.
