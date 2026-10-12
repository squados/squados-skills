# Pesquisa de skills — operações logísticas internas

Data de consulta: 12/10/2026. Frente: recebimento, separação, embalagem, expedição, devoluções e indicadores. Dossiê para orientar a futura skill **Analista de Logística**; não cria, instala ou publica uma skill.

## Conclusão da frente

A melhor base encontrada é **AgentLogistics**, de Jeremy Longworth: usa registros da empresa, preserva unidades e estados, pede apenas lacunas necessárias e separa recomendação de alteração operacional. A skill de ondas de separação contém decisões concretas sobre prazo, carga e capacidade; parte dos pacotes de recebimento e embalagem é mais genérica. A referência de devoluções da Evos acrescenta casos difíceis, mas mistura análise com atendimento, decisões financeiras e referências de varejo dos EUA. Deve servir como repertório de problemas, não como política brasileira ou procedimento automático.

Recomendação: uma skill autoral enxuta que reconheça o pedido e carregue referências de operação sob demanda. Aproveitar a disciplina de evidência; adaptar cálculos e entregas ao processo real; descartar SLA, limiares, políticas e ações externas presumidos. Não importar o catálogo de armazém inteiro nem construir WMS, OMS, TMS ou plataforma de BI.

## Alcance, seleção e limites

Foram usados SkillMD, skills.sh, SkillsMP, EliteAI, Skills Directory e skills.homes para descoberta, depois repositórios originais quando acessíveis. Pesquisas combinaram logistics/logística, fulfillment, warehouse, receiving, picking, packing, shipping, reverse logistics, returns, POD e OTIF com SKILL.md/GitHub. Diretórios e badges de segurança não comprovam correção operacional.

**Leitura integral de 11 SKILL.md originais:** nove de AgentLogistics, uma de Evos e uma de Domain Experts, em três famílias autorais. Não são onze evidências independentes: os nove pacotes AgentLogistics compartilham método e alguns corpos quase iguais. Foram lidos integralmente os recursos decisivos listados abaixo; o restante de cada repositório não foi auditado. A primeira leitura da Evos e de Domain Experts usou main, seguida da identificação do HEAD; os links deste documento fixam a revisão observada. Nenhum código remoto, avaliação ou pacote foi executado.

A API GitHub sem credenciais respondeu 403 por limite de requisições. HTML público do GitHub e raw.githubusercontent.com permitiram verificar HEAD, datas de commit, conteúdo e licenças sem conta, clone ou download persistido. Caminhos antigos de alguns diretórios retornaram 404; isso é limite de acesso/proveniência, não prova de inexistência de toda a família.

Não houve instalação, autenticação, consulta de sistemas de clientes, envio de mensagens, alteração de pedidos, aprovação de devolução, execução de avaliações pagas, commit ou publicação nesta frente.

## Origem, revisão e licença

| Família | Autoria verificada | Revisão e data do commit | Licença consultada | Limite de maturidade e distribuição |
|---|---|---|---|---|
| AgentLogistics | Jeremy Longworth, copyright 2026 | `a88cf9af690de4e9ebc10ec8db0e892d961d107a`, 12/09/2026 | [MIT](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/LICENSE) | [README](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/README.md) declara preview `v0.1.0-public-preview`, `V1_PARTIALLY_READY`; avaliação com modelo ao vivo ainda pendente. Referências fora da pasta da skill e `agents/` impedem presumir pacote isolado compatível. |
| Evos agent-skills | Evos AI, copyright 2026; frontmatter autor evos | `1eda1feb184cfde82175d4ffa5feccf6501a4394`, 25/02/2026 | [Apache-2.0](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/LICENSE) | [README](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/README.md) apresenta avaliação própria; resultados não reproduzidos nesta pesquisa. Homepage e instruções citam antigo `evos-ai/evos-capabilities`; origem atualmente consultada é `ai-evos/agent-skills`. |
| Domain Experts | Wonsuk Choi e colaboradores, copyright 2026 | `0101c5456f7e4d718a5dd7657c4514448039a303`, 12/10/2026 | [MIT](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/LICENSE) | A role declara `maturity: draft`, não declara licença no frontmatter; licença raiz foi consultada. Referência técnica útil, sem comprovação de execução. |

Datas acima são do commit observado, não necessariamente da primeira publicação ou da última revisão de cada arquivo. Preservar notices e licença em qualquer incorporação substancial; atribuição e alterações devem acompanhar derivados. A pesquisa recomenda síntese autoral em PT-BR, não cópia de templates. Nenhuma dessas três origens está na lista GitHub permitida para item externo da galeria atual: servem como referências de desenho; publicar uma futura skill SquadOS exige autoria e compatibilidade próprias, sem ocultar conteúdo derivado.

## Matriz de componentes consultados

Todos os links AgentLogistics abaixo fixam a mesma revisão. Os recursos relacionados são detalhados em seguida.

| Fonte / arquivo lido integralmente | Contribuição concreta | Decisão | Adaptação e motivo |
|---|---|---|---|
| [plan-inbound-receiving/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/inbound-receiving/plan-inbound-receiving/SKILL.md) | Confrontar esperado, enviado, recebido, inspecionado e aceito; documentos e restrições de doca | Adaptar | Plano interno a partir de agenda e registros existentes. O fluxo publicado é de conferência genérica e não dimensiona recebimento por si só. |
| [process-receiving-discrepancy/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/inbound-receiving/process-receiving-discrepancy/SKILL.md) | Registro de divergência documental, de quantidade, identidade, condição ou status; variação em unidades compatíveis | Aproveitar método | Entregar tabela de divergências com evidência e próximo responsável; não ajustar estoque nem cobrar fornecedor automaticamente. |
| [plan-picking-wave/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/replenishment-picking/plan-picking-wave/SKILL.md) | Agrupar pedidos por corte, zona, método e prontidão; confrontar separação, embalagem, staging e coleta | Adaptar | Capacidade com produtividade observada e tempo disponível. Ordem retida/proposta para onda é recomendação, sem liberação no WMS. Usar inventário já fornecido como restrição. |
| [plan-packing-operation/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/packing-shipping/plan-packing-operation/SKILL.md) | Confrontar pedido, picking, embalagem, etiqueta, documentos e staging | Adaptar | Plano de carga/filas e checklist apoiado no padrão local; faltam dimensionamento e critérios físicos específicos. Não gerar etiquetas nem contratar expedição. |
| [verify-outbound-shipment/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/packing-shipping/verify-outbound-shipment/SKILL.md) | Classificar pronto, retido, divergente ou sem evidência; manter handoff de expedição | Aproveitar método | Conciliação interna de documentos e eventos. Despacho, coleta, chegada e entrega são marcos diferentes; não tratar esta conferência como POD. |
| [classify-return-disposition/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/reverse-logistics/classify-return-disposition/SKILL.md) | Separar motivo declarado, condição observada, inspeção, política, status e recomendação | Aproveitar método | Recomendar destino permitido, condicional ou dependente de revisão usando critérios da empresa. Não aprovar reentrada, descarte, reparo ou crédito. |
| [analyze-return-rate/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/reverse-logistics/analyze-return-rate/SKILL.md) | Definir numerador, denominador, unidade e exclusões; distinguir troca, cancelamento, duplicação e retorno parcial | Adaptar | Acrescentar coorte e maturação: retornos recebidos no mês não correspondem necessariamente às vendas ou expedições do mesmo mês. |
| [analyze-reverse-logistics-cost/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/reverse-logistics/analyze-reverse-logistics-cost/SKILL.md) | Custo de frete, manuseio, inspeção, embalagem, reparo e recuperação; separar realizado/estimado | Adaptar | Definir tratamento da perda do produto e do reembolso, evitar dupla contagem e identificar crédito recebido versus apenas solicitado. Não inferir direito de ressarcimento. |
| [analyze-warehouse-kpis/SKILL.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/performance-continuous-improvement/analyze-warehouse-kpis/SKILL.md) | Definição, unidade, extração, baseline, alvo e segmentação; variação não prova causa | Aproveitar método | Scorecard curto focado no pedido. Selecionar indicadores existentes e declarar tamanho/cobertura da amostra, sem scorecard universal. |
| [Evos returns-reverse-logistics/SKILL.md](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/capabilities/returns-reverse-logistics/SKILL.md) | Ciclo RMA → recebimento → inspeção → destino; variedade de exceções e economia de recuperação | Adaptar parcialmente | Manter vínculo entre devolução, pedido e evidência. Descartar políticas, faixas monetárias, metas, scoring de fraude, escalonamentos e atendimento externo prescritos. |
| [Domain Experts logistics-analyst/SKILL.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/SKILL.md) | OTIF comparado ao compromisso de entrega real e cautela com pouca amostra | Adaptar parcialmente | Reaproveitar comparação de janela prometida/real; transporte/custos pertencem à outra frente. O conceito local de in-full, dano e exclusões deve ser confirmado. |

## Recursos decisivos e dependências

| Recurso lido integralmente | Utilidade e decisão |
|---|---|
| [AgentLogistics — warehouse-core-checklist, verify-outbound](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/packing-shipping/verify-outbound-shipment/references/warehouse-core-checklist.md) | Preserva estado e passagem de trabalho. Adaptar checklist conciso; token de conclusão AL-06 é governança do upstream, sem utilidade para usuário da futura skill. |
| [AgentLogistics — fulfillment-optimization-checklist, picking-wave](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/replenishment-picking/plan-picking-wave/references/fulfillment-optimization-checklist.md) | Casos de corte de coleta, capacidade insuficiente, reposição indisponível e pool misto. Aproveitar como cenários de validação posterior. |
| [AgentLogistics — reverse-logistics-checklist, disposition](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/reverse-logistics/classify-return-disposition/references/reverse-logistics-checklist.md) | Quantidades autorizadas, embarcadas, recebidas, inspecionadas, retidas, destinadas e creditadas distintas. Aproveitar a separação e o vínculo à fonte. |
| [AgentLogistics — continuous-improvement-checklist, warehouse-kpis](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/skills/performance-continuous-improvement/analyze-warehouse-kpis/references/continuous-improvement-checklist.md) | Preserva timezone, exclusões e baseline; separa observação, inferência, causa e medição. Adaptar sem impor relatório longo em toda resposta. |
| [AgentLogistics — common-units.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/shared/glossaries/common-units.md) | Caixa, unidade, carton, pallet e kit dependem de hierarquia real; calendário e conversão monetária precisam de base explícita. Aproveitar. |
| [AgentLogistics — inventory-state-terms.md](https://github.com/jeremylongworth-source/AgentLogistics/blob/a88cf9af690de4e9ebc10ec8db0e892d961d107a/shared/glossaries/inventory-state-terms.md) | Útil para entender reserva e bloqueio como restrições. Descartar da futura skill as decisões de ponto de pedido, estoque de segurança e compras desta frente. |
| [Evos — decision-frameworks.md](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/capabilities/returns-reverse-logistics/references/decision-frameworks.md) | Declara contexto de varejo dos EUA; usar comparação de recuperação líquida como ideia, com dados locais e sem percentuais prescritos. Não copiar árvores e tabelas de aprovação. |
| [Evos — edge-cases.md](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/capabilities/returns-reverse-logistics/references/edge-cases.md) | Vinte casos inteiros lidos: erro cruzado de expedição, recall, duplicação financeira, identidade e dados em dispositivos são bons problemas para revisão interna. Não importar respostas financeiras, jurídicas ou contatos externos. |
| [Domain Experts — vocabulary.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/references/vocabulary.md) | Diferencia marco da transportadora e compromisso de recebimento. Adaptar definição OTIF ao contrato da empresa; não adotar freight class/NMFC como prática universal. |

As nove skills AgentLogistics referenciam também `shared/`, `docs/standards/`, `tests/scenarios/` e validadores fora de seus pacotes individuais. Esses recursos adicionais não foram todos lidos nesta frente; não se afirma auditoria integral nem instalabilidade. Os nove recursos decisivos acima foram lidos integralmente. `communication-templates.md` da Evos não foi necessário e não foi lido; atendimento e envio não pertencem ao escopo.

## Candidatos descobertos que não sustentam adoção

| Candidato / descoberta | Situação | Decisão |
|---|---|---|
| [AgentLogistics no SkillMD](https://skillmd.com/skills/jeremylongworth-source/analyze-product-flow) e [mirror gabrielmoreira](https://skillmd.com/plugins/gabrielmoreira/jeremylongworth-source-agentlogistics) | Índice do mesmo upstream; registro exibe hash antigo `04371bf`, enquanto HEAD consultado é posterior. | Não contar como outra autoria/validação. `analyze-product-flow` foi lida no diretório, não entrou nas 11 leituras originais. |
| [awesome-omni-skills returns-reverse-logistics-v2](https://skillsmp.com/skills/diegosouzapw-awesome-omni-skills-skills-returns-reverse-logistics-v2-skill-md) | Diretório explicita ORIGIN/copied upstream; corpo original desse mirror não auditado. | Não contar v2 como evidência independente nem adotar cópia sem confirmar origem e licença. |
| [Order Fulfillment Workflow / Cerebra](https://eliteai.tools/agent-skills/order-fulfillment-workflow-1) | Diretório apresenta código TypeScript/Prisma de plataforma; origem `amnadtaowsoam/cerebraskills` retornou 404; caminho antigo do registry também 404. | Descartar adoção. Licença MIT atribuída pelo diretório não comprova direito do conteúdo upstream; registro permanece preliminar. |
| [theYahia WWmcp / Salla](https://www.skillsdirectory.com/skills/theyahia-order-fulfillment) | Diretório descreve list_orders/get_order e alteração de status; caminho raw suposto retornou 404. Repositório existe, localização atual da skill não confirmada. | Descartar para analista interno sem conexão à Salla; não contar como SKILL original integral. |
| [vivekhaldar/proceda order-fulfillment](https://skills.homes/en/skills/vivekhaldar-proceda-benchmarks-sop-bench-domains-order-fulfillment-skill-md) | Cenário de benchmark/SOP de validação cliente, inventário e decisão de fulfillment; raw indexado não localizado. | Excluir execução e adoção; descoberta não demonstra skill profissional operacional. |
| [vertical-logistics](https://www.skills.sh/avelikiy/great_cto/vertical-logistics), [logistics-expert](https://www.skills.sh/personamanagmentlayer/pcl/logistics-expert), [LogiFleet Pulse](https://www.skills.sh/reason-machines/data-skills/logifleet-pulse-supply-chain-analytics) | Páginas de descoberta: arquitetura de software, tópicos genéricos e plataforma SQL Server/Power BI respectivamente. Pacotes originais não selecionados para leitura integral. | Não adotar: problema ou custo incompatível com análise de registros e documentos internos. Não foram auditados nem contados nas 11 skills. |

## Achados de revisão estática

São observações de texto e código exposto, não testes executados.

1. **AgentLogistics — baixo detalhamento de alguns fluxos.** `plan-inbound-receiving` e `process-receiving-discrepancy` repetem o workflow de recebimento; `plan-packing-operation` e `verify-outbound-shipment` repetem o workflow outbound. Os nomes prometem planos específicos, mas o corpo nem sempre explicita balanceamento de estações, agenda ou sequência. Adaptar a partir do pedido concreto, sem anunciar otimização já demonstrada.
2. **AgentLogistics — dependências fora do pacote.** Referências `shared/` e `docs/` não acompanham a pasta atômica por cópia simples. `agents/openai.yaml` aparece no diretório de descoberta e não está entre as pastas de apoio aceitas pelo adaptador atual do Studio. A compatibilidade precisa ser auditada no pacote final.
3. **Evos — contradição de política.** Em `edge-cases.md`, caso 8, a abordagem usa o preço de compra documentado; os indicadores mandam usar o menor entre preço de compra e preço atual. Essa divergência muda o resultado financeiro. Descartar a regra; consultar a política real, sem resolvê-la por suposição.
4. **Evos — pontuação sem escala garantida.** O SKILL define score 0–100, mas sinais podem somar mais de 100 sem teto explícito; o recurso detalhado acrescenta sinais e ajustes. A discrepância impede tratar o score como calibrado. Toda a automação de fraude/reembolso fica fora desta skill.
5. **Evos — números e jurisdição.** Limiares de recuperação, custos, tempos, taxas, limites de inspeção e obrigações dos EUA são muito específicos e não vêm acompanhados de evidência adequada para transferir à empresa brasileira. A orientação de destino também varia entre SKILL e árvore detalhada; não se consolida uma regra universal.
6. **Evos — causa não demonstrada.** O exemplo de defect claim atribui retorno acima de uma média de categoria a defeito; isso não comprova causalidade. Motivo declarado, inspeção e contexto podem divergir. Usar apenas ocorrência/hipótese até evidência causal.
7. **Domain Experts — OTIF precisa de contrato.** A definição inclui ausência de dano em in-full; isso pode pertencer a qualidade/perfect-order no acordo local. Os limites de amostra e ranges de transporte são heurísticas ilustrativas, sem garantia estatística universal.
8. **Cerebra no diretório — sinal de erro em lote.** O trecho `minZones` compara `items.length` e seleciona o menor grupo, apesar de comentário sobre máximo de itens/mínimo de zonas; `orderBy priority: desc` sobre strings também não demonstra prioridade semântica. Origem não disponível e trecho incompleto: registrar sinal, não afirmar bug reproduzido no upstream.

## Síntese operacional para o desenho posterior

### Reconhecimento do pedido e entradas mínimas

Começar pelo objetivo, prazo e material já disponível. Se a pessoa entregar planilha de pedidos atrasados, analisar os campos existentes e retornar achados provisórios antes de pedir cadastro completo. Reconhecer automaticamente se precisa de diagnóstico de fila, conciliação, plano diário, scorecard, revisão de retorno ou documento de procedimento. Perguntar apenas o dado que muda uma decisão; dados acessórios permanecem opcionais.

| Pedido comum | Dados decisivos disponíveis ou a solicitar | Entrega interna utilizável |
|---|---|---|
| “Quais recebimentos estão divergentes?” | Esperado/recebido/aceito, documento e unidade | Tabela de divergências, evidência, impacto, responsável e próximo passo |
| “Como organizar a separação até a coleta?” | Pool, linhas/unidades, cortes, capacidade e bloqueios | Proposta de ondas/filas com retidos, restrições e capacidade calculada |
| “Por que a expedição acumulou?” | Eventos pick/pack/stage/handoff, volume e horas | Gargalo candidato, lacunas, comparação de carga/capacidade e ações propostas |
| “Qual nosso OTIF?” | Compromisso de prazo e quantidade, realizado, base elegível e exclusões | Memória de cálculo com denominador e registros indeterminados |
| “Onde perdemos dinheiro nas devoluções?” | Volumes e custos realizados/estimados, recuperação e vínculo ao pedido | Análise por causa declarada/destino, sem atribuir culpa ou ressarcimento automaticamente |
| “Escreva o procedimento de conferência.” | Processo/SOP já praticado, documentos, papéis e exceções | Minuta revisável com lacunas marcadas, linguagem da equipe e checklist autoral |

### Definições que evitam conclusões erradas

Pedido, linha, unidade, volume e embarque não são intercambiáveis. Usar a granularidade do trabalho e manter vínculo entre entidades. Um pedido dividido pode gerar vários embarques e um evento reprocessado pode aparecer repetidamente: definir chave, deduplicação e regra de agregação antes de contar. Status são dados do sistema local: não inventar enum universal nem mapear automaticamente expedido como entregue.

Para indicadores, explicitar janela, timezone, calendário, corte de extração, base elegível, marco prometido/realizado, tolerância e regra para alteração de promessa. Evento sem POD ou sem quantidade aceita não prova sucesso nem fracasso por si só: separar confirmado, falhou e indeterminado, com cobertura da evidência. POD é documento/evento a confrontar com recebedor, local, horário, quantidade e ressalvas disponíveis; esta pesquisa não encontrou uma skill POD independente original adequada que cubra o fluxo inteiro.

OTIF é a interseção de condições de prazo e completude no mesmo elemento elegível. Não multiplicar médias OTD e in-full. Em pedidos parciais, declarar se a unidade avaliada é pedido, linha, embarque ou unidade; manter o resultado por embarque separado da regra de pedido completo. Não transferir limiar universal da role. Para devoluções, distinguir taxa por coorte de expedição com tempo de observação de razão operacional “recebido no período / expedido no período”; esta última pode ser válida como carga relativa, mas não demonstra probabilidade de devolução daquela coorte.

Capacidade proposta usa produtividade observada na mesma unidade e tempo efetivamente disponível. Verificar separação, embalagem, staging e corte de coleta em conjunto. Fila planejada não altera o sistema. Usar disponibilidade/reservas/bloqueios existentes como restrição; estoque de segurança, compras, reposição estratégica e catálogo de inventário pertencem a outras skills.

No custo de reversa, separar pedido de retorno, quantidade recebida, inspeção, destino e crédito. Identificar moeda/data, realizado/estimado, custo incremental, rateio e valor recuperável/recuperado. Evitar somar reembolso, custo do produto e perda de valor sem explicar o critério econômico/contábil. Crédito solicitado ou revendável não equivale a dinheiro recuperado. A skill entrega análise interna e minuta; não efetua reembolso, cobrança, troca, contato com cliente ou decisão de descarte.

### Núcleo e referências sob demanda

O núcleo deve orientar: reconhecer entrega → aproveitar materiais → validar apenas definições decisivas → escolher cálculo/fluxo → produzir resultado curto e verificável → mostrar limitações que alteram a decisão. Não exigir formulário, menu de modos, todos os KPIs ou todas as etapas em toda tarefa.

Referências recomendadas para implementação posterior: operações de recebimento/fulfillment; indicadores e conciliação de eventos; devoluções e custo; elaboração de procedimentos e planos internos. Abrir somente a pertinente. O dossiê e a bibliografia extensa ficam em docs/research, fora do pacote executável. Scripts locais podem ajudar quando há volume real de registros e ganho de precisão em junções/deduplicação/cálculo; um pedido pequeno não justifica script nem instalação de BI. Dependências precisam ser verificadas no ambiente antes de prometer planilha, PDF ou biblioteca disponível.

## Evidência e lacunas de aceitação

- Pesquisa e leitura de componentes: realizadas no alcance explicitado, com três famílias e revisões fixadas.
- Auditoria de pacote completo, segurança e compatibilidade Hermes/Studio: não realizada; exige o pacote final.
- Avaliações publicadas pelos autores: consultadas como alegações e limites de maturidade; não reproduzidas.
- Skill própria, scripts e templates: não criados nesta frente.
- Proposta nativa, instalação, execução com dados reais, aprovação e publicação: não realizadas.

Para validar a futura síntese: pedido dividido em duas entregas; dados sem POD; promessa alterada depois do corte; eventos duplicados e reprocessados; caixas com conversão ausente; capacidade de separação suficiente com embalagem insuficiente; devolução parcial/troca/cancelamento; retorno de coorte ainda imatura; recuperação solicitada versus recebida; custos com risco de dupla contagem. São cenários propostos, não testes já passados.
