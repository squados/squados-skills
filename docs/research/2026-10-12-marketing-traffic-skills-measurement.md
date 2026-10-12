# Analista de Marketing e Tráfego — mensuração, análise e comunicação

Pesquisa consultada em **12/10/2026**, para a sétima profissão do catálogo de 33 especialidades. Este arquivo cobre qualidade dos dados, GA4, funil, atribuição, experimentos e relatórios executivos. A frente de operação de mídia paga é tratada em outra pesquisa. **Só pesquisa:** não cria a skill, instala pacotes, acessa contas, executa as skills estudadas ou altera a galeria.

## Decisão recomendada

Construir depois uma skill própria que reconheça a intenção pelo pedido e comece pela decisão de negócio: diagnosticar uma mudança, explicar o funil, reconciliar fontes, avaliar um teste ou apresentar resultados. A melhor composição encontrada é **método de instrumentação e reconciliação do Corey Haines + organização de relatórios da Anthropic + contexto por modelo de negócio do Digital Marketing Pro + diagnóstico por composição de tráfego do Clamp**, com correções estatísticas e de atualidade explicitadas abaixo.

Não juntar os pacotes inteiros. GA4/GTM, fórmulas de testes, MMM e formatos extensos ficam em referências carregadas conforme a necessidade. A análise deve funcionar com arquivos exportados e números fornecidos; conectores são uma capacidade opcional a conferir no ambiente, não um pré-requisito inventado. O resultado precisa ser compreensível por quem administra uma empresa sem conhecer desenvolvimento de software.

## Alcance e método

- Descoberta por buscas em PT/EN para analytics, GA4, marketing measurement, attribution, performance reporting, funnel, experiment e sample ratio mismatch, usando resultados para localizar repositórios originais.
- **10 SKILL.md lidos integralmente, em 5 repositórios**, mais **9 arquivos de apoio lidos integralmente**. Alguns resultados chegaram truncados; as partes faltantes foram recuperadas em leituras separadas. O inventário abaixo distingue leitura da skill de auditoria do pacote.
- **5 candidatas adicionais descobertas**, sem leitura integral: a busca registra 15 candidatas em 10 repositórios, não uma cobertura exaustiva do ecossistema. Elas não recebem o mesmo peso das dez analisadas.
- Seleção por diversidade de trabalho: instrumentação, experimentação, atribuição, diagnóstico e narrativa. As várias skills do mesmo repositório não contam como fontes independentes. Não foi identificada cópia literal entre as cinco famílias analisadas; isto não é uma auditoria completa de genealogia ou forks.
- Revisões fixadas por SHA. Data do commit do repositório não é data de atualização de cada arquivo. Conteúdo foi obtido por GitHub público/API/raw; após limite da API pública, foram usados raw e `git ls-remote`, sem autenticação.
- Documentação profissional primária foi consultada para resolver conflitos. Não houve conta de cliente, ferramenta paga, instalação, execução de scripts externos, teste de segurança ou demonstração de resultado real.

## Fontes e escopo efetivamente lido

### A. Corey Haines — instrumentação, testes e reconciliação

Repositório [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), SHA `1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff`, commit **08/10/2026, 21:51:37 UTC**. Autoria indicada na [licença MIT](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/LICENSE): Corey Haines, copyright 2025.

| Skill integral | Versão declarada | Recursos integrais consultados | Contribuição |
|---|---|---|---|
| [analytics](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/analytics/SKILL.md) | 2.0.3 | [ga4-implementation.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/analytics/references/ga4-implementation.md) | Instrumentar apenas o que informa decisões; plano de eventos; propriedades; UTMs; depuração; duplicações |
| [ab-testing](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/ab-testing/SKILL.md) | 2.0.1 | [sample-size-guide.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/ab-testing/references/sample-size-guide.md) | Hipótese, métrica principal, limites de dano, amostra e decisão previamente definida |
| [attribution](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/attribution/SKILL.md) | 1.1.4 | [measurement-paradigms.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/attribution/references/measurement-paradigms.md) | Resultado financeiro separado de crédito por canal; deduplicação; comparação de abordagens; lacunas e confiança |

Os nomes históricos pedidos, `analytics-tracking` e `ab-test-setup`, não são os caminhos da revisão atual: os arquivos usam `analytics` e `ab-testing`. As referências de primeira parte, demais guias de eventos/GTM, templates, avaliações e integrações ligadas externamente **não foram auditados integralmente**. A alegação de exemplos de produção no texto de atribuição não foi validada externamente.

### B. Anthropic — relatório que pode ser encaminhado à liderança

Repositório [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins), SHA `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06`, commit **11/10/2026, 07:46:12 UTC**. Autoria do plugin: Anthropic. [Licença do pacote marketing: Apache-2.0](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/marketing/LICENSE).

Lidos integralmente [marketing/skills/performance-report/SKILL.md](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/marketing/skills/performance-report/SKILL.md) e [CONNECTORS.md](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/marketing/CONNECTORS.md). O caminho atual é `performance-report`, não `performance-reporting`.

Forças: aceita dados colados, arquivos e conectores; adapta campanha, canal e visão geral; separa resumo, comparação, tendências, hipóteses e prioridades; prevê relatório semanal, mensal e trimestral. Limites: algumas definições são anteriores ao GA4; tabelas de benchmark não têm proveniência suficiente no próprio arquivo; comparar modelos não torna uma atribuição causal. Nenhum conector do plugin foi acessado ou considerado disponível no Studio por simples menção.

### C. Digital Marketing Pro — contexto de negócio e divisão entre coleta e narrativa

Repositório [indranilbanerjee/digital-marketing-pro](https://github.com/indranilbanerjee/digital-marketing-pro), SHA `dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8`, commit **11/10/2026, 21:41:30 UTC**. Mantenedor/origem: Indranil Banerjee; [licença MIT](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/LICENSE), copyright 2026 Digital Marketing Pro.

| Skill integral | Recursos integrais consultados | Contribuição |
|---|---|---|
| [analytics-insights](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/analytics-insights/SKILL.md) | [kpi-frameworks.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/analytics-insights/kpi-frameworks.md), [dashboard-design.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/analytics-insights/dashboard-design.md), [incrementality-testing.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/analytics-insights/incrementality-testing.md) | Métricas por negócio, dados antes de causas, visualização por audiência, escolha de experimento |
| [attribution-report](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/attribution-report/SKILL.md) | Nenhum guia específico adicional integral | Comparação explícita de janelas/modelos, cobertura de jornadas, tempo até conversão |
| [performance-report](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/performance-report/SKILL.md) | [deliverable-layout.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/skills/performance-report/deliverable-layout.md) | Relatório como camada narrativa sobre dados já coletados; causas apresentadas como hipóteses |

Também foi lido integralmente [agents/analytics-analyst.md](https://github.com/indranilbanerjee/digital-marketing-pro/blob/dd65250cfe4ed98ab46b84f40b6b57eae87cf0e8/agents/analytics-analyst.md), pois determina delegação, ferramentas e critérios de análise. As três skills acima não declaram versão no frontmatter; a referência é o SHA.

Não foram lidos os scripts associados, todos os perfis de setor/compliance, a configuração de conectores, o agente `marketing-scientist`, todos os guias de MMM/privacidade ou o pacote completo. Portanto, a pesquisa não atesta as rotinas automáticas, memória de marca, otimização ou modelagem desse ecossistema. `~/.claude-marketing`, hooks e divisão em agentes são dependências daquele produto, não conteúdo para copiar ao núcleo do SquadOS.

### D. Clamp — diagnóstico que separa composição de desempenho

Repositório [clamp-sh/analytics-skills](https://github.com/clamp-sh/analytics-skills), SHA `b9e06c5131a6060114e68893bc34fc77b65a9552`, commit **11/06/2026, 10:10:50 UTC**. [Licença MIT](https://github.com/clamp-sh/analytics-skills/blob/b9e06c5131a6060114e68893bc34fc77b65a9552/LICENSE), copyright 2026 Clamp contributors.

Lidos integralmente [analytics-diagnostic-method/SKILL.md](https://github.com/clamp-sh/analytics-skills/blob/b9e06c5131a6060114e68893bc34fc77b65a9552/skills/analytics-diagnostic-method/SKILL.md) e [experiment-result-reader/SKILL.md](https://github.com/clamp-sh/analytics-skills/blob/b9e06c5131a6060114e68893bc34fc77b65a9552/skills/experiment-result-reader/SKILL.md). Sem versão no frontmatter. Não foram lidos os tool maps, esquema de eventos ou skills Bayesian/sequential referenciadas.

Forças: pergunta precisa antes do painel; árvore de diagnóstico; triangulação; diferenças entre taxa agregada e composição de canais; resposta primeiro, números e ressalvas depois; exposição antes de conversão. Limite material: há simplificações estatísticas erradas nos dois arquivos, descritas com localização adiante. O bom formato da análise não valida suas fórmulas.

### E. Amin Borghei — alternativa de análise offline, com restrição de licença

Repositório [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills), SHA `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`; [commit de 07/10/2026](https://github.com/borghei/Claude-Skills/commit/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0) confirmado pelo cabeçalho público do patch. Lido integralmente [marketing/campaign-analytics/SKILL.md](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/marketing/campaign-analytics/SKILL.md): versão 1.0.0, author `borghei`, updated **21/09/2026**.

A [licença completa do repositório](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/LICENSE), também lida, é **MIT + Commons Clause**, não MIT puro. Autoria: Amin Borghei. A condição restringe vender/reempacotar e determinados serviços cujo valor deriva substancialmente do software. **Não recomendar redistribuir seus scripts, templates ou texto como componente comercial do catálogo.** O método profissional pode ser descrito independentemente, apoiado por fontes abertas e primárias; esta decisão evita depender da interpretação de uma licença restritiva.

O arquivo descreve três scripts Python offline com biblioteca padrão, contratos de entrada JSON e saída texto/JSON. Isso é uma alegação documental, **não execução comprovada**: os scripts, templates e demais referências não foram lidos. Há benchmarks universais e afirmações de GA4 sem fonte adequada; ficam fora da recomendação.

### Candidatas adicionais, somente descoberta

| Origem independente | Candidata | Por que a busca parou antes de aprofundar |
|---|---|---|
| [rampstackco/claude-skills](https://github.com/rampstackco/claude-skills/blob/main/skills/experimentation-analytics/SKILL.md) | experimentation-analytics | Escopo promissor para leitura de testes; principais dúvidas estatísticas resolvidas com fontes primárias |
| [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/main/social/observe/dark-social-attributor/SKILL.md) | dark-social-attributor | Especialização de atribuição; núcleo já pode explicitar lacunas sem inventar fontes ocultas |
| [SpillwaveSolutions/running-marketing-campaigns-agent-skill](https://github.com/SpillwaveSolutions/running-marketing-campaigns-agent-skill/blob/main/references/analytics-measurement.md) | running-marketing-campaigns, referência analytics-measurement | Mais ampla e sobrepõe operação de campanhas; não contada como SKILL.md integral |
| [he8um/marketing-maestro](https://github.com/he8um/marketing-maestro/blob/main/marketing-maestro/SKILL.md) | marketing-maestro | Bom sinal de separação entre observado/financeiro/modelado; não necessário ampliar pacote para resolver esta frente |
| [openai/plugins](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/build-report/SKILL.md) | build-report | Relatório geral; fontes já cobrem narrativa executiva e dados fornecidos |

Licenças, recursos completos e revisões dessas cinco candidatas não foram verificados. Não são recomendações de instalação, redistribuição ou compatibilidade.

## Matriz de componentes

| Fonte / componente | Contribuição | Decisão | Motivo e destino |
|---|---|---|---|
| Corey analytics — Initial Assessment/Core Principles | Decisão antes da coleta; reutiliza contexto | **Aproveitar** | Núcleo: perguntar apenas o que muda a entrega |
| Corey analytics — Tracking Plan/Validation | Evento, gatilho, propriedades, duplicação | **Adaptar** | Referência de mensuração: incluir unidade, responsável e prova observável; implementação só quando solicitada |
| Corey ga4-implementation — Recommended Events | Nomes nativos e receita com moeda/transação | **Adaptar** | Referência GA4; conferir contrato atual, evitando instruções de UI envelhecidas |
| Corey ab-testing — métricas e análise | Hipótese, efeito, incerteza, limite de dano | **Aproveitar** | Núcleo resumido; estatística detalhada sob demanda |
| Corey sample-size-guide — tabelas fixas | Atalho de dimensionamento | **Descartar como cálculo final** | Divergem da tabela do SKILL.md e omitem condições suficientes para confiar em qualquer linha |
| Corey attribution — fonte de verdade/deduplicação | Conversões reais separadas do crédito | **Aproveitar** | Núcleo: uma venda não vira duas porque duas plataformas a reivindicam |
| Corey measurement-paradigms — escolha MTA/MMM/testes | Rigor proporcional ao problema | **Adaptar** | Referência: suposições e viabilidade substituem escolha automática por orçamento |
| Corey measurement-paradigms — synthetic touchpoints | Ajustar crédito em lacunas | **Descartar** | Não criar toques individuais sintéticos em jornadas; estimativas ficam separadas do dado observado |
| Anthropic performance-report — audiência/cadência | Resumo encaminhável e apêndice | **Aproveitar** | Template opcional; relatório curto não deve preencher oito seções por obrigação |
| Anthropic — fórmulas/benchmarks/atribuição | Referência rápida | **Adaptar/descartar** | Corrigir GA4 e ROI; retirar hierarquia universal entre modelos e benchmarks sem origem |
| DMP analytics-insights — dados antes de causas | Checa tracking, atraso, segmento e mudanças | **Aproveitar** | Núcleo e referência de diagnóstico |
| DMP kpi-frameworks — árvore de métricas | Receita, aquisição, retenção, margem | **Adaptar** | Só métricas necessárias à pergunta; nenhum North Star garante saúde sozinho |
| DMP dashboard-design — três audiências | Detalhe adequado a liderança/gestão/operação | **Adaptar** | Modelo de profundidade, sem criar três dashboards nem impor quotas de métricas |
| DMP incrementality-testing — desenhos e riscos | Holdout, geo, contaminação, extrapolação | **Adaptar** | Referência causal; recalcular potência e usar margem própria, sem iROAS universal |
| DMP attribution-report — matriz e cobertura | Janela, caminhos, créditos lado a lado | **Aproveitar** | Descrição de jornadas; a diferença entre modelos é sensibilidade, não efeito incremental |
| DMP attribution-report — orçamento a partir de modelos | Projeta aumento de receita | **Descartar** | Crédito reatribuído não sustenta projeção causal ou otimização automática |
| DMP performance-report — coleta separada da narrativa | Usa exportação/snapshot existente | **Aproveitar** | Evita recapturar dados sem motivo; registrar origem e atualização |
| DMP analytics-analyst — perfis, scripts e delegação | Ecossistema persistente de marketing | **Descartar do núcleo** | Não transplantar instalação, diretórios globais, hooks ou agentes obrigatórios |
| Clamp diagnostic — triangulação e mix shift | Explica por que taxa total pode cair com canais melhores | **Aproveitar** | Referência diagnóstica; separar composição de deterioração real |
| Clamp experiment reader — exposição, denominador e SRM | Valida quem entrou no experimento | **Adaptar** | Comparar com alocação planejada e teste adequado, não expectativa universal de 50/50 |
| Clamp — IC/peeking/certeza por volume | Heurísticas estatísticas | **Descartar** | Fórmulas e conclusões inadequadas; substituição por método documentado |
| Borghei campaign-analytics — offline e contratos | Cálculo repetível com dados explícitos | **Referência, sem cópia** | Redigir método próprio; a licença condicionada e falta de auditoria impedem recomendar recursos |

## Conflitos materiais e como resolvê-los

### 1. Atribuição, incrementalidade e MMM

Na seção **Purpose** e no **Process, passos 3–6** de DMP `attribution-report`, crédito entre caminhos aparece como contribuição real e base para projetar conversões incrementais após aumento de orçamento. O agente DMP `analytics-analyst`, **Behavior Rules 1**, exige distinguir associação de causa. **Manter a disciplina do agente; corrigir o fluxo de orçamento.**

Comparar first-touch/last-touch/linear mostra quanto uma conclusão depende da regra de crédito. Não identifica sozinho o que ocorreria sem a campanha. No GA4 atual, há DDA e duas variantes de último clique; first click, linear, time decay e position-based foram retirados dos relatórios em novembro de 2023. Esses modelos podem continuar como cálculo próprio sobre caminhos suficientemente completos, sem prometer que aparecem no painel. [Google, attribution](https://support.google.com/analytics/answer/10596866).

Corey `measurement-paradigms`, **MMM** e **How to read a test**, reduz MMM a correlação e diz que um intervalo atravessando zero significa não aprender nada. Corrigir ambos: MMM pode sustentar inferência causal sob hipóteses explícitas, e intervalo inconclusivo ainda informa quais efeitos são compatíveis com os dados. Ajuste preditivo alto não basta para justificar uma conclusão causal. [Google Meridian, causal inference](https://developers.google.com/meridian/docs/causal-inference/about-mmm-causal-inference-methodology).

Não usar uma regra rígida de dois anos, valor de orçamento ou quantidade de canais como prova de viabilidade. Conferir variação dos investimentos, granularidade, confundidores, estabilidade, horizonte e objetivo; se necessário, entregar avaliação de viabilidade em vez de um modelo ajustado. Não aumentar o escopo para MMM quando um diagnóstico ou comparação simples resolve o pedido.

### 2. Estatística do Clamp: boa comunicação, atalhos errados

Localizações na revisão fixada de [experiment-result-reader](https://github.com/clamp-sh/analytics-skills/blob/b9e06c5131a6060114e68893bc34fc77b65a9552/skills/experiment-result-reader/SKILL.md):

- **Phase 3, item 1**, usa margem de proporção calculada no pior caso para concluir que diferença menor é ruído; **Phase 5, NUMBERS** rotula essa margem como IC do lift. São quantidades distintas. **Worked example** afirma ±5,7 pontos para o lift de 15/302 versus 22/297. Conferência matemática simples do revisor, sob Bernoulli independente e aproximação normal: diferença ≈ **2,44 pp**, meia largura `1,96 × sqrt(pA(1-pA)/nA + pB(1-pB)/nB)` ≈ **3,86 pp**, intervalo ≈ **[−1,42; 6,30] pp**. É ilustração do problema, não execução da skill nem recomendação universal de usar Wald em amostras pequenas.
- **Phase 3, item 3**, propõe nominal 1% como aproximação para olhares semanais; **Traps to avoid, Stopping a test**, propõe estender uma semana para ver se persiste. Nenhuma dessas regras define controle válido do erro com repetidas consultas. Usar horizonte fixo previamente definido ou metodologia sequencial documentada com regra de parada. [GrowthBook, sequential testing](https://www.growthbook.io/insights/sequential-testing).
- **Phase 1/Phase 4**, usa equilíbrio visual como sinal de configuração limpa. Desequilíbrio deve ser avaliado contra a proporção configurada e o tamanho da amostra; 60/40 não é defeito se era o desenho planejado. [Microsoft Research, SRM, 14/09/2020](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/).

Em `analytics-diagnostic-method`, **Separate signal from noise**, o exemplo 5%→4% com 5.000 sessões é chamado de real sem cálculo suficiente. **Worked example** usa volume acima de mil como comprovação. Retirar esses limiares como veredito. Efeito absoluto, denominadores e modelo de incerteza precisam acompanhar a conclusão. Significância estatística não mede importância econômica. [ASA, declaração de 2016](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).

### 3. Tabelas e benchmarks não são decisões universais

Corey `ab-testing`, **Sample Size**, cita 150 mil por variante para baseline 1% e lift relativo 10%; `sample-size-guide`, tabela **Conversion Rate: 1%**, cita 380 mil para os mesmos rótulos. Divergência observada, sem execução externa. Recalcular com hipótese, teste, poder, efeito e alocação explícitos; não copiar uma das tabelas como autoridade.

DMP `incrementality-testing`, **Interpreting Results**, usa faixas de iROAS como orientação para escalar/manter/reduzir. Receita incremental por gasto não incorpora automaticamente margem, devoluções, custos variáveis ou horizonte. Usar a economia do negócio. Seus valores de elegibilidade de estudos de plataforma também são estimativas documentais, não elegibilidade verificada de uma conta.

As metas universais do Borghei (CPA em dólares, ROAS por canal, melhoria de 29% por UTMs) e parte das tabelas Anthropic/DMP não trazem fontes suficientes para emprego corrente. Preferir histórico comparável e metas da empresa. Benchmark externo exige fonte, período, mercado, moeda, definição, população e método compatíveis; não confundir rótulo de confiabilidade com proveniência.

### 4. Definições e superfícies GA4 precisam ser atuais

Anthropic `performance-report`, **Content Marketing**, e DMP `kpi-frameworks`, **eCommerce**, definem bounce rate como sessões de página única. No GA4, é proporção de sessões sem engajamento. Uma visita de uma página pode ser engajada. [Google, engagement and bounce rate](https://support.google.com/analytics/answer/12195621).

Anthropic chama receita atribuída/custo de produção de “Content ROI”; esse quociente descreve uma relação receita/custo, não lucro incremental sobre investimento. Na própria entrega, explicitar fórmula e custos incluídos em vez de reutilizar rótulo incorreto.

Comparações GA4/UI/API/BigQuery não devem ser forçadas a coincidir: revisar datas, filtros, escopo, identidade, atualização, amostragem, supressão e agregação. O guia corrente da Data API recomenda conferir metadados `samplingMetadatas`, `subjectToThresholding` e `dataLossFromOtherRow`; não confundir valor suprimido ou linha agregada com zero. [Google, Reporting data expectations, atualizado em 09/10/2026](https://developers.google.com/analytics/devguides/reporting/data/v1/reporting-data-expectations), [data thresholds](https://support.google.com/analytics/answer/9383630).

O canal **AI Assistant** citado por DMP existe na documentação atual; exclui AI Overviews e AI Mode do Google. Incluir quando relevante, preservando a origem. Não chamar esse canal de todo o tráfego de IA, somar sessões com impressões/citações nem inferir tráfego oculto de IA em Direct. [Google, default channel group](https://support.google.com/analytics/answer/9756891).

### 5. Observado, financeiro, atribuído, modelado e hipótese

Corey `measurement-paradigms`, **Triangulated overrides**, sugere inserir touchpoints sintéticos em parte das jornadas. Descartar no caminho padrão: o que foi observado deve continuar identificável. Pode-se apresentar um cenário agregado baseado em teste ou pesquisa, com método e intervalo próprios, sem reescrever o caminho observado de cada pessoa.

Receita real vem da fonte financeira escolhida para o pedido, com definição de pagamento, aprovação, cancelamento e estorno. Receita atribuída é outra medida. Conversões modeladas, estimativas por ticket e pesquisas de origem também são outras medidas. Uma ausência de rastreamento não demonstra ausência de impacto; uma pesquisa de origem não autoriza repartir automaticamente todas as vendas por seus percentuais.

## Organização posterior: núcleo curto e referências sob demanda

### Núcleo

1. Reconhecer intenção pelo pedido e reutilizar arquivos/contexto existentes. Definir decisão, período, comparador, audiência e dado indispensável. Perguntas apenas para lacunas que mudam o resultado; explicitar suposições quando uma primeira versão for útil.
2. Conferir qualidade antes de interpretar: origem, definição da conversão, unidade, janela, denominador, fuso, moeda, duplicação, cobertura, atraso e evidência disponível. Não transformar isto num questionário obrigatório para pedidos simples.
3. Escolher o menor método suficiente. Diagnóstico começa por integridade e composição; atribuição começa por resultado e regra de crédito; experimento começa por desenho/exposição; relatório começa pela decisão da audiência.
4. Mostrar conclusão ou limite da conclusão, evidência principal e próxima ação. Separar fato, hipótese, estimativa e resultado experimental. Traduzir consequência em receita, margem, aquisição, retenção ou risco pertinente ao negócio.
5. Entregar formato utilizável solicitado: resposta curta, relatório, tabela/planilha, diagnóstico, plano de teste ou especificação de dashboard. Não produzir deck, instalação e automação como complementos obrigatórios.

### Referências sugeridas

| Referência futura | Carregar quando | Conteúdo que vale guardar |
|---|---|---|
| `measurement-and-ga4.md` | “Os números não batem”, medir evento, plano GA4 | Escopos, nomes nativos, UTMs, deduplicação, limites das superfícies e evidência de implementação |
| `funnel-and-diagnostics.md` | Queda de resultado ou gargalo | Unidade/coorte/janela; perdas absolutas e relativas; mix shift; observações que confirmam/refutam hipóteses |
| `attribution-and-incrementality.md` | Origem de receita, contribuição de canais | Resultado versus crédito, cobertura, sensibilidade, desenho causal, elegibilidade, hipóteses de MMM |
| `experiments.md` | Planejar/ler A/B, holdout ou geo | Unidade, exposição, métrica, MDE, poder, SRM, multiplicidade, parada, atraso de conversão, incerteza e economia |
| `executive-reporting.md` | Relatório para gestão/cliente | Resumo, comparação comparável, métricas relevantes, recomendação vinculada à evidência, apêndice quando necessário |

Nomes propostos apenas para organização; nenhum desses arquivos foi criado. Evitar repetir princípios nas referências. Bibliografia extensa e histórico desta comparação permanecem neste dossiê, fora do núcleo executável.

### Scripts e dependências

Scripts só entram se resolverem uma necessidade concreta: validar exportações grandes, reconciliar IDs de transação, agregar períodos/coortes, recalcular muitos cenários ou dimensionar um teste com método verificável. Um relatório com dez números não exige um programa.

Nenhum script externo estudado foi executado ou aprovado para reutilização. Se uma tarefa futura precisar de biblioteca ausente, conferir primeiro o ambiente e oferecer instalar a dependência explicando utilidade, alternativa e custo; não assumir que o Studio já a traz. Se um padrão recorrente justificar melhorar a própria skill, oferecer uma adaptação pequena e explícita. Essas ofertas são pertinentes ao pedido, não um menu repetido ao fim de toda resposta.

## Exemplos de entregas e critérios de qualidade

**“O tráfego subiu, mas as vendas caíram.”** Entregar definição/periodização, validação de receita e tracking, decomposição `volume × taxa × valor`, comparação por canal/coorte/dispositivo relevante, evidência de mix shift e hipóteses concorrentes. Maior perda percentual em uma etapa não é automaticamente a maior oportunidade econômica.

**“Meta e GA4 não batem.”** Entregar tabela com população, janela, clique/visualização, contagem, fuso, cobertura e atualização de cada fonte; contar vendas aprovadas uma vez; explicar créditos separadamente. Não inferir uma correção multiplicativa só pela diferença entre painéis.

**“Qual variante ganhou?”** Entregar exposição e conversões por grupo, efeito absoluto/relativo, regra de análise/parada, checagem da alocação, intervalo e limites de dano. Conclusão possível: inconclusivo para a decisão atual. Não chamar não significância de equivalência ou de teste fracassado.

**“Monte o relatório mensal para a diretoria.”** Entregar resumo curto com resultado e implicação, tabela com poucas métricas pertinentes e comparador, ações vinculadas aos achados e apêndice suficiente para auditoria. Metas ausentes não devem virar metas inventadas; previsões precisam estar marcadas como cenários e mostrar premissas.

Critérios transversais: números rastreáveis ao material recebido; taxas calculadas de totais compatíveis em vez de média simples de percentuais; moeda/fuso/unidade declarados quando afetam o cálculo; receita e gasto reconciliados ao mesmo escopo; separação entre novos clientes e recompra quando necessária; confiança proporcional ao dado, sem rótulos automáticos; nenhuma alegação de execução real baseada em leitura de Markdown.

## Limites e fechamento da frente

Esta comparação resolve as escolhas materiais de método, profundidade, organização e fontes para mensuração. **Não comprova segurança ou compatibilidade dos pacotes completos, disponibilidade de conectores, instalações, acesso a contas, cálculo correto dos scripts ou sucesso em um trabalho real.** Não há teste de pacote, proposta nativa, aprovação, instalação ou publicação nesta frente.

Corey, DMP e Clamp não são fontes diretamente permitidas pelo `github` atual da galeria; o pacote Anthropic estudado está em `knowledge-work-plugins`, não `anthropics/skills`. Portanto, nenhuma escolha desta pesquisa implica adicionar esses caminhos ao índice. A criação posterior precisa sintetizar método próprio, preservar origem/licenças quando houver reprodução permitida e verificar compatibilidade do pacote final no consumidor atual.

Encerrar descoberta aqui é deliberado: as dúvidas de atribuição versus causalidade, dados versus narrativa, qualidade estatística, limites de dependências e licença foram resolvidas o bastante para a consolidação. Permanecem para depois da conclusão das pesquisas do catálogo: autoria da skill própria, textos finais, recursos estritamente necessários e validação em pedidos representativos.
