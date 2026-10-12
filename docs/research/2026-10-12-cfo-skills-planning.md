# CFO — planejamento financeiro, orçamento e decisões

Pesquisa de 12/10/2026, rodada 17/33. Frente de planejamento: FP&A, orçamento, forecast, análise de variações, cenários e decisão empresarial. Complementa a frente de caixa/demonstrações e a frente de métodos/vídeos; não substitui suas leituras. Entrega documental, sem criar ou instalar a skill, executar código remoto, abrir contas ou realizar transações.

## Recomendação

Construir posteriormente uma síntese própria, curta e orientada ao pedido. Aproveitar a investigação de variações do `budget-vs-actual`, a separação entre dados preliminares/finais e ações do Oracle, os modelos de drivers e templates do `financial-analyst` com licença MIT verificada na revisão Alireza, e a ponte plano → realizado → forecast do prompt FP&A. Adaptar tudo ao negócio e retirar valores financeiros automáticos, benchmarks universais, probabilidades fictícias e ritual obrigatório de todas as ferramentas.

Nenhuma candidata deve ser adotada inteira como CFO genérico. A qualidade da aritmética, a qualidade das premissas e o acerto da previsão são evidências diferentes. Cenários condicionais apoiam decisões; não são probabilidades nem intervalos estatísticos apenas por terem três colunas.

## Alcance, leitura e contagens

A descoberta combinou pesquisa web por `SKILL.md`, FP&A, financial planning, variance analysis, rolling forecast e budget; inspeção dos repositórios originais por raw URLs; `git ls-remote` para fixar HEAD; API GitHub somente de leitura para árvores e datas. A API anônima inicialmente atingiu limite de requisições; a consulta autenticada disponível com `gh api` resolveu a leitura, sem instalação, clone ou scratch. Os SHAs abaixo são o estado observado nesta consulta, não versões imutáveis de branches chamadas `main`.

Foram lidos integralmente **cinco SKILL.md**: as duas revisões de `financial-analyst`, `budget-vs-actual`, `fpa-model` e `netsuite-finance-analyst`. Correspondem a **quatro definições distintas em três famílias de pacotes**: financial-analyst; SkillMedev (duas skills complementares); Oracle. Há **um prompt de papel FP&A lido integralmente**, de Agency Agents, contado separadamente. O prompt não é um pacote `SKILL.md`, e suas conversões Hermes/forks não geram novas evidências independentes.

Leituras de recursos decisivos: scripts de forecast e variância nas duas revisões financial-analyst; referência de forecasting nas duas revisões; templates de forecast e variância da revisão Alireza; playbook de análise e referência de saída executiva Oracle; licenças de todos os cinco repositórios. A comparação dos scripts mostrou código compartilhado e os acréscimos de entrada da revisão Alireza; a referência de forecasting é idêntica entre elas. Não foi auditado todo recurso de valuation, toda integração NetSuite ou toda dependência. As contagens de arquivos abaixo são da árvore, não uma alegação de leitura integral do pacote.

Pesquisa anterior de Planilhas/Dados pode orientar execução de artefatos e séries temporais na consolidação, mas não é contada aqui como nova leitura. Hermes/Anthropic finance core ficou com a frente de caixa. Descoberta não equivale a levantamento de toda a internet, instalação, aprovação do guard ou execução demonstrada.

## Registro de fontes e revisões

| Código | Fonte original e arquivo principal | Revisão observada / data do HEAD | Autoria e licença consultadas | Alcance e compatibilidade |
|---|---|---|---|---|
| A | [Alireza financial-analyst](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/SKILL.md) | `19392f7a08264ed00486a251f5b2098321771f94`; 26/08/2026 13:53:02 UTC | Mantenedor Alireza Rezvani; [MIT raiz, copyright 2025](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/LICENSE). Frontmatter não traz licença específica | 14 arquivos: core, 4 scripts, 4 referências, 5 assets. Scripts desta frente usam biblioteca padrão Python; Python continua sendo runtime necessário. Não assumido instalado |
| B | [Borghei financial-analyst](https://github.com/borghei/claude-skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/finance/financial-analyst/SKILL.md) | `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0`; 07/10/2026 10:46:46 UTC; metadata da skill: 31/03/2026 | Amin Borghei; [MIT + Commons Clause](https://github.com/borghei/claude-skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/LICENSE), também no frontmatter | 13 arquivos; falta `industry-adaptations.md` separado presente em A. Consulta interna não autoriza presumir redistribuição comercial no Studio |
| C | [SkillMedev budget-vs-actual](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/budget-vs-actual/SKILL.md) | `6b3044d569595b481a3677da8f68af7aa239dc09`; 05/10/2026 05:02:28 UTC; última alteração consultada no arquivo: 05/10/2026 03:07:49 UTC | Alexander Ouellet, autoria do commit e [MIT raiz](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/LICENSE), copyright 2026. Core sem campo license | 1 arquivo. Referências a outras skills são roteamento textual; não se presume que estejam disponíveis no destino |
| D | [SkillMedev fpa-model](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/fpa-model/SKILL.md) | Mesmo HEAD de C; última alteração consultada no arquivo: 05/10/2026 03:07:49 UTC | Mesma autoria e MIT de C | 1 arquivo. Descreve modelo de planilha, sem script próprio ou prova de recálculo |
| E | [Oracle NetSuite finance analyst](https://github.com/oracle/netsuite-suitecloud-sdk/blob/a142c29c4ddf599a07f3a02c0016ee83c509b94e/packages/agent-skills/netsuite-finance-analyst/SKILL.md) | `a142c29c4ddf599a07f3a02c0016ee83c509b94e`; 09/10/2026 13:20:33 UTC; última alteração consultada do core: 15/06/2026 15:15:07 UTC | Frontmatter Oracle NetSuite; commit consultado Viktor Nikulin; [UPL 1.0](https://github.com/oracle/netsuite-suitecloud-sdk/blob/a142c29c4ddf599a07f3a02c0016ee83c509b94e/LICENSE.txt), copyright Oracle 2019/2023 | 6 arquivos: core + 5 referências. Integração nativa depende de NetSuite/MCP ou fonte equivalente. Sem conectar conta ou provar runtime aqui |
| F | [Agency Agents FP&A](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/finance/finance-fpa-analyst.md) | `f99f6aa910a442b0197b768ce0ea7751e35e2060`; 07/10/2026 16:45:46 UTC; última alteração consultada do arquivo: 11/04/2026 05:44:11 UTC | Michael Sitarzewski no commit consultado; [MIT, copyright AgentLand Contributors 2025](https://github.com/msitarzewski/agency-agents/blob/f99f6aa910a442b0197b768ce0ea7751e35e2060/LICENSE) | Um prompt de especialista, sem pacote executável, scripts ou evidência de currículo real da persona |

### Linhagem e licença: o caso financial-analyst

A e B compartilham organização dos quatro calculadores, referências e templates; a referência de forecasting comparada é idêntica. Nos dois scripts comparados, A acrescenta resolver o objeto JSON aninhado e rejeitar entrada vazia. Os cálculos centrais observados coincidem. Isso basta para tratá-los como uma família de implementação, mas **não prova a direção histórica da cópia nem autoriza transferir a licença de A para B**. A API identifica B como `fork: false`; essa propriedade não prova autoria independente.

A licença MIT verificada refere-se à revisão A e aos arquivos nela presentes. A versão B declara Commons Clause: permite uso interno no resumo da própria licença, mas restringe venda/reempacotamento de serviço cujo valor derive substancialmente do software. Para eventual incorporação no produto comercial, preferir conceitos profissionais reescritos e, se houver reutilização textual/código, avaliar especificamente A, com avisos preservados. Não trocar apenas o cabeçalho de B por MIT. A pesquisa não é um parecer jurídico nem uma aprovação geral para distribuir.

Discovery também encontrou `bestagentkits/agency-skills/.../financial-analyst`, registries e conversões de Agency Agents. Não foram somados como skills originais lidas. Outros resultados — finance-operator, business-analysis genérico, finanças pessoais e análise de investimentos — permaneceram fora da seleção aprofundada por repetição ou menor aderência ao pedido; não há julgamento de qualidade do pacote inteiro sem leitura.

## Fonte → componente → decisão

| Fonte/arquivo | Contribuição observada | Decisão | Motivo concreto |
|---|---|---|---|
| A/B `SKILL.md` | Escopo, validação dos dados, análise, síntese executiva e comparação futura com realizado | Adaptar | Reconhecer intenção e usar dados já recebidos; não obrigar ratios/DCF/forecast juntos ou escolha de ferramenta pelo usuário |
| A/B `references/forecasting-best-practices.md` | Drivers por negócio; impacto versus incerteza; forecast móvel; ponte entre versões; viés | Adaptar | Bom repertório, mas remover metas MAPE universais, probabilidades base/bull/bear e benchmarks SaaS fixos |
| A `assets/variance_report_template.md` | Desvio, causa, impacto, ação; comparações identificadas; responsável/prazo | Aproveitar estrutura, adaptar extensão | Relatório pode ser curto; causa não comprovada deve aparecer como hipótese, responsável como papel quando pessoa não informada |
| A `assets/forecast_report_template.md` | Histórico, drivers, premissas, cenários, riscos e acompanhamento | Adaptar | Retirar caixa de 13 semanas quando não pedido, probabilidade obrigatória e leitura de R² como confiança futura |
| A/B `scripts/budget_variance_analyzer.py` | Aritmética repetível e saída estruturada por categoria/departamento | Não copiar sem correção; script opcional posterior | Base zero, ausência de dado, tipo de linha e agregação exigem tratamento explícito; cálculo não descobre causa |
| A/B `scripts/forecast_builder.py` | Exemplo simples de parâmetros e cenários | Descartar como motor padrão | Defaults financeiros inventam premissas; drivers de clientes não entram no cálculo; não modela capacidade, custos em degraus ou sazonalidade real |
| C `SKILL.md` | Receita por preço/volume, classificação temporal/volume/estrutural, efeito no forecast | Adaptar | Forte para diagnóstico; precisa correções de mix, materialidade e preservação do orçamento aprovado |
| D `SKILL.md` | Separar premissas, receita, despesas e outputs; folha derivada de quadro/start date | Adaptar arquitetura, descartar números e regras universais | A simplificação de receita/ARR, encargos e resposta de custo não se generaliza a empresas brasileiras |
| E `SKILL.md` + `references/finance-analysis-playbook.md` | Fonte mínima suficiente, período aberto/final, exceções abaixo materialidade e drivers específicos | Adaptar | Aplicável também a arquivos recebidos. Não exigir NetSuite, onboarding ou consolidação por default |
| E `references/executive-output.md` | Conclusão com número, escopo, riscos, ação/dono/prazo | Aproveitar | Ajuda a entregar decisão utilizável; identidade do dono e data não devem ser fabricadas |
| F `finance/finance-fpa-analyst.md` | Reconciliar alvo top-down com capacidade bottom-up; ligar variação ao efeito futuro; trade-offs | Adaptar | Funciona em orçamento e expansão; não importar persona fictícia, calendário corporativo rígido ou metas de sucesso como prova |

## Divergências e falhas decisivas

**Materialidade:** B usa 10% ou US$50 mil; Oracle usa vários limites contextualizados à escala de empresas e permite escalada qualitativa; C escreve “greater of” uma porcentagem e valor absoluto, sem converter bases, enquanto seu exemplo comenta COGS com 4,5% e US$28 mil. Esse exemplo ultrapassa o valor absoluto e não a porcentagem, em tensão com uma leitura de “ambos os limites”. A skill futura precisa declarar claramente a regra escolhida, a moeda, a base e a finalidade. Preferir política já recebida; quando faltar e afetar a decisão, perguntar. Não transformar materialidade gerencial em norma de auditoria. Desvios pequenos recorrentes ou concentração de risco podem merecer comentário mesmo abaixo do limite.

**Mix:** as fórmulas de C por segmento, `volume = (Qa − Qb) × Pb` e `preço = (Pa − Pb) × Qa`, já reconciliam a variação de receita daquele segmento. Um resíduo agregado não deve ser batizado automaticamente de mix: pode conter mudança de escopo, unidade, período ou erro. Se mix for separado, escolher e documentar uma ponte consistente com a quantidade total e a composição, sem dupla contagem. Sem unidades/preço por segmento, explicar a limitação e usar drivers verificáveis; nunca completar decomposição com números inventados.

**Orçamento e previsão:** C chama para atualizar número da linha estruturalmente desviada. Interpretação recomendada: preservar o orçamento aprovado como baseline e atualizar uma coluna de forecast identificada, com data e ponte de alterações. Reescrever a meta para eliminar o desvio impede avaliar o plano original. Forecast é melhor estimativa com informação atual; orçamento também pode representar meta/compromisso. Um não substitui silenciosamente o outro.

**Receita SaaS não é regra empresarial:** D propõe receita mensal = ARR final/12. Isso pode servir como aproximação de run-rate sob condições explícitas, mas não é uma regra de receita reconhecida para contratos que começam ao longo do mês, serviços, descontos ou reconhecimento diferente. D também toma encargos de 1,2–1,3 salários, faixas de hosting/comissão e prazo de fundraising como padrões. Descartar esses valores: não há data, jurisdição ou contexto suficiente. Comércio/serviços/indústria não devem receber ARR, CAC ou runway como métricas padrão.

**Cenários:** exigir cenário para uma decisão material é útil; exigir sempre três variantes, mesma quantidade de parâmetros e probabilidades é ritual. Em D, bull com custos fixos e bear com redução de custos mistura ambiente com reação gerencial. Separar primeiro o choque, depois a resposta e suas restrições/prazos. Reação não é instantânea; receita maior pode exigir capacidade, estoque ou pessoas. Uma faixa entre cenários não mede probabilidade nem constitui intervalo preditivo. Remover probabilidades de 50–60%/15–25% sugeridas na referência A/B quando não houver base.

**Auditoria estática dos scripts A/B, sem execução:**

- `forecast_builder.py` fornece crescimento anual de 5%, margem de 40%, opex de 25%, unidades/preço e aumento anual quando ausentes. A matemática determinística sobre esses valores não transforma defaults em premissas aprovadas. `customer_drivers` é carregado mas não usado; descrever suporte a clientes/conversão sem conferir o caminho efetivo superestima o motor.
- O chamado índice sazonal divide as últimas quatro observações pela média do histórico; não estima um ciclo sazonal e não é aplicado ao forecast de receita observado. R² de ajuste não prova previsão fora da amostra. Dividir crescimento anual de unidades por 12 difere de converter taxa efetiva por composição; ambas só devem entrar com convenção e períodos explícitos.
- `budget_variance_analyzer.py` usa zero como fallback para dados ausentes e percentual 0 quando orçamento é zero. Uma despesa não orçada pode assim aparecer sem percentual de desvio. Reportar “não aplicável — base zero” e evidenciar valor absoluto; ausência deve continuar ausente.
- Valor exatamente igual ao orçamento cai como desfavorável tanto em receita quanto em despesa; precisa estado “sem desvio”. Tudo que não é `revenue/income/sales` recebe lógica de despesa: EBITDA, margem e indicadores físicos não cabem nisso automaticamente.
- Resumos de departamento somam linhas indiscriminadamente. Receitas, despesas, totais/subtotais ou sinais contábeis podem tornar a soma enganosa. Validar plano de contas e não misturar métricas diferentes. Nenhum script consultado produz causalidade preço-volume-mix ou evidência operacional por si só.
- A melhoria de A rejeita objeto vazio e aceita JSON aninhado, porém não valida integralmente todos os tipos, unidades e premissas. `assets/expected_output.json` não foi usado como prova: nome de arquivo não demonstra suite de testes ou acerto futuro.

Esses achados justificam aproveitar o método e evitar copiar o motor padrão. Não foi feita alteração nos upstreams, nem foram executados seus scripts com dados financeiros.

## Métodos primários para corrigir as lacunas

| Fonte profissional | Autoria/data consultadas | Contribuição à decisão |
|---|---|---|
| [ACCA — All about budgeting, part 1](https://www.accaglobal.com/africa/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/budgeting1.html) | ACCA, artigo de formação técnica; sem data de publicação confirmada nesta leitura, acesso 12/10/2026 | Distinguir orçamento fixo, flexível e ajustado ao volume efetivo. Comparar custo variável realizado com orçamento estático pode penalizar maior atividade sem haver ineficiência. Há exemplo industrial de baterias e reconhecimento da dificuldade de separar custos indiretos fixos/variáveis |
| [ACCA — Relevant costs](https://www.accaglobal.com/sg/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/relevant-costs.html) | ACCA, material técnico; data de publicação não confirmada, acesso 12/10/2026 | Para decisão incremental, comparar diferenças futuras de caixa entre alternativas, separar custo passado/comprometido e custo de oportunidade. Rateio contábil sozinho não decide terceirizar, aceitar pedido ou encerrar produto |
| [Forecasting: Principles and Practice — toolbox](https://otexts.com/fpp3/toolbox.html) | Rob J. Hyndman e George Athanasopoulos, OTexts; edição consultada via URLs de accuracy/tscv, que redirecionaram para capítulo toolbox; acesso 12/10/2026 | Avaliar previsão fora da amostra e com origem móvel respeitando tempo/horizonte. MAPE é indefinido com realizado zero e instável perto de zero. MAE e viés, ou erro escalado quando adequado, evitam o falso “0% de erro”. Fonte não valida metas de precisão de cada negócio |

São métodos gerenciais/estatísticos, não consulta de alíquota, norma contábil brasileira atual ou taxa de financiamento. Nenhuma taxa atual foi afirmada. Se o pedido posterior exigir impostos, encargos legais, reconhecimento formal, norma ou financiamento, verificar período e jurisdição nas fontes competentes; não converter exemplos ACCA/US GAAP em orientação universal.

## Adaptação concreta por negócio

Tabela abaixo é síntese proposta, não valores de benchmark nem alegação de um template único testado.

| Trabalho | Comércio | Serviços | Indústria |
|---|---|---|---|
| Receita | Unidades por categoria × preço líquido; devolução/desconto; sazonalidade | Contratos/horas faturáveis × tarifa, utilização e capacidade; marcos quando aplicáveis | Volume vendido × preço líquido por produto; carteira, rendimento e capacidade |
| Custo | Compra, frete, perdas e estoque, condições documentadas | Pessoas, terceirizados, ociosidade e retrabalho; contratação por data | Matéria-prima, consumo, mão de obra, capacidade e custos em degraus |
| Orçamento/variação | Separar preço, quantidade, mix e promoções com bases coerentes | Separar tarifa, horas, escopo, ocupação e início de contratos | Ajustar custo ao volume produzido; distinguir preço, eficiência, rendimento e capacidade |
| Decisão | Margem de contribuição da promoção/loja/produto e caixa necessário | Admitir pessoa, terceirizar, ajustar capacidade ou precificar contrato | Produzir/comprar, turno extra ou equipamento; restrição produtiva e custo incremental |
| Evidência faltante material | Estoque/recebimento/devoluções por período | Horas disponíveis versus faturáveis e critério de receita | Produção versus vendas, padrão técnico/custo e perdas |

Não supor operação SaaS, financiamento disponível, crescimento positivo ou taxa de imposto. Uma empresa mista pode usar mais de um build; escolhe-se pela receita/custo efetivo, não pelo nome do setor.

## Núcleo e referências sob demanda

O núcleo futuro deve caber em uma sequência simples: entender a decisão e audiência; aproveitar planilhas/relatórios recebidos; verificar período, moeda, escala, entidade e base; distinguir realizado, orçamento aprovado, estimativa e cenário; selecionar a análise proporcional; calcular com rastreabilidade; entregar conclusão, evidência, limites e ação. Não apresentar um menu de modos. Perguntar apenas as lacunas que possam alterar materialmente o resultado.

Exemplos de lacunas: a planilha compara competência com caixa? O período parcial deveria comparar orçamento parcial? A unidade monetária é reais ou milhares? O custo é positivo ou negativo? Os registros incluem subtotais? Uma “premissa” é meta, contrato assinado, histórico ou hipótese? Perguntas resolvidas pelos arquivos não devem ser repetidas.

Referências sugeridas para criação posterior:

- `references/budget-and-forecast.md`: orçamento/forecast distintos, abordagem por drivers, janela/cadência do negócio, cadastro de premissas com fonte/data/dono e ponte entre versões.
- `references/variance-analysis.md`: sinal e base percentual, base zero, materialidade gerencial, orçamento ajustado ao volume, preço/volume/mix, temporal/estrutural, evidência versus hipótese e implicação futura.
- `references/scenarios-and-decisions.md`: sensibilidade, cenário e resposta separados; custo incremental/oportunidade; capacidade e restrições; ponto de mudança da recomendação. Métodos de investimento entram somente quando necessários e com premissas documentadas.
- `templates/financial-review.md`: versão curta adaptável com escopo, tabela comparável, causas, revisão do forecast e ações. Não exigir relatório grande ou designer para responder pergunta simples.
- `templates/assumption-register.md`: valor/unidade, natureza, fonte, período/as-of, responsável e dependências. Probabilidade só quando justificada.

Scripts entram apenas se houver repetição/carga que fórmulas de planilha e ferramentas disponíveis não resolvam bem. Bibliotecas e recálculo dependem do destino; não afirmar que Studio já traz Python/openpyxl/LibreOffice para qualquer agente. Quando faltar dependência, explicar o benefício e oferecer instalação simples com execução pelo agente, sem mandar a pessoa virar desenvolvedora. Nenhuma dependência instalada nesta pesquisa.

Após repetição de uma tarefa ou atrito concreto com o formato, o CFO pode oferecer adaptar a própria skill aos drivers, relatórios e linguagem da empresa; a alteração exige pedido ou aceite da pessoa. Aprendizado operacional não implica guardar indiscriminadamente dados financeiros ou criar memória externa.

## Critérios para a criação e futura avaliação

1. Pedido de orçamento: a meta e os drivers bottom-up podem divergir; mostrar a lacuna e a decisão necessária, sem ajustar receita para “bater a meta”.
2. Pedido de variação: mesma base temporal/entidade/unidade, sem duplicar subtotais; desvios e ponte reconciliam; causa sem suporte aparece como hipótese. Orçamento zero permanece exposto.
3. Pedido de forecast: premissas com origem/as-of, fatos anteriores separados do futuro; zero dado não vira crescimento/margem de mercado. Orçamento original preservado.
4. Pedido de cenário: combinações coerentes, restrições e resposta custeada; mostrar onde a conclusão muda. Não inventar probabilidade.
5. Pedido de decisão: alternativas e efeito incremental, incluindo capacidade e oportunidade; lucro contábil não substitui efeito de caixa. Dados para caixa devem vir da frente correspondente.
6. Artefato: fórmulas/links/unidades conferidos, cálculos reproduzíveis e recálculo quando necessário e disponível. Validar isso não afirma previsão acertada.
7. Previsão: guardar a previsão tal como emitida e comparar com realizado posterior pelo horizonte relevante; usar baseline e erro/viés apropriados. Sem observação posterior ou backtest honesto, precisão permanece não demonstrada.

## Estado e limites da entrega

Pesquisa e decisões desta frente documentadas; leitura estática de fontes e recursos listados, comparação de variantes e licenças verificadas nas revisões fixadas. Sem pacote novo, scripts instalados/executados, guard Hermes, proposta de contratação, conta NetSuite, teste de planilha ou prova com dados reais. Nenhuma mudança no catálogo. Nenhum commit/push feito por esta frente.

A decisão de desenho está resolvida o suficiente para consolidar: síntese própria dos componentes selecionados, com referências carregadas conforme o trabalho e rejeição explícita das premissas automáticas. Auditoria integral de todos os arquivos e execução no runtime só serão necessárias se a consolidação optar por reutilizar um pacote concreto. Não ampliar a busca apenas para aumentar a contagem.
