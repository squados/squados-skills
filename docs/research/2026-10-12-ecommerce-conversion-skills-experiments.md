# Especialista em Conversão de Ecommerce — mensuração, diagnóstico e experimentos

Frente de pesquisa da rodada 23/33, consultada em **12/10/2026**. Entrega: componentes para uma futura skill própria, capaz de responder a pedidos de conversão com dados fornecidos, exportações e acessos já autorizados. Não cria o pacote executável, altera a galeria, instala dependências, acessa lojas ou contas, lança testes ou executa scripts externos.

## Recomendação

Combinar a definição cuidadosa de funil e os planos de experimento do ChatData com a comunicação concisa da decomposição de receita de Mahmoud Omar. A composição exige adaptações: remover vínculo obrigatório a serviço externo e telemetria; manter os cálculos proporcionais à pergunta; distinguir contribuição aritmética, hipótese causal e efeito experimental; escolher prazo conforme tráfego elegível, maturidade do resultado e ciclos do negócio.

O núcleo precisa reconhecer se a pessoa quer explicar uma queda, localizar uma perda, priorizar melhorias, planejar um teste ou avaliar seu resultado. Pedido de auditoria visual pode avançar com observações e hipóteses mesmo sem analytics; pedido de taxa ou vencedor precisa de evidência correspondente. Uma lacuna material limita aquela conclusão, sem impedir todo trabalho útil.

## Alcance e proveniência

Busca PT/EN por skills de A/B testing, experiment design, funnel analysis e ecommerce conversion. Resultados de busca e diretórios serviram para descobrir repositórios; a comparação usa arquivos originais. Quatro SKILL.md foram lidos integralmente, de duas famílias independentes. Foram lidos integralmente três recursos de referência, um script, seu arquivo de versão e as duas licenças. Não houve execução, auditoria integral dos repositórios ou comprovação com dados reais.

Os SHAs foram obtidos com `git ls-remote`, sem clone. A API pública do GitHub retornou limite de requisições; depois disso, a leitura usou raw, páginas de commit e cabeçalhos públicos de patch. Não houve autenticação, arquivo temporário ou instalação. A data do commit do repositório não é uma data de revisão individual de cada skill.

| Família | Revisão fixada | Autoria e data verificável | Licença e alcance |
|---|---|---|---|
| [ChatData](https://github.com/parasdoshicom/getchatdata) | `cd3918b7c643a3c91d7961ac6b355b42587a00d2` | Paras Doshi na licença; cabeçalho do [commit](https://github.com/parasdoshicom/getchatdata/commit/cd3918b7c643a3c91d7961ac6b355b42587a00d2) identifica Insight Extractor Inc.; 08/09/2026, 14:35:36 −07:00; `package-info.json` declara 1.7.2 | [MIT](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/LICENSE), copyright 2026 Paras Doshi; lida integralmente |
| [Growth Marketing OS](https://github.com/growthack88/growth-marketing-os) | `c7852deefb3cd90029f02d328b9e59cea39ef585` | Mahmoud Omar no frontmatter/licença; página do [commit](https://github.com/growthack88/growth-marketing-os/commit/c7852deefb3cd90029f02d328b9e59cea39ef585) declara autoria/commit em 10/10/2026, 15:55:49 +03:00 | [MIT](https://github.com/growthack88/growth-marketing-os/blob/c7852deefb3cd90029f02d328b9e59cea39ef585/LICENSE), copyright 2026 Mahmoud Omar; lida integralmente |

Os conteúdos externos continuam nas origens. MIT permite adaptação sob suas condições; copiar trechos substanciais ou código exigiria preservar licença, autoria e avisos. As origens acima não são admitidas diretamente pelo contrato atual de `source.github` da galeria. Pesquisa de método e eventual síntese própria não equivalem a publicar esses pacotes como autoria SquadOS.

### Arquivos efetivamente consultados

| ID | Arquivo completo | Papel no método |
|---|---|---|
| C1 | [experiment-design/SKILL.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/skills/experiment-design/SKILL.md) | Hipótese, decisão, efeito mínimo útil, unidade, população, exposição, potência e regra de parada |
| C2 | [experiment-analysis/SKILL.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/skills/experiment-analysis/SKILL.md) | Alocação, SRM, população analisada, maturidade, efeito, incerteza e limites de dano |
| C3 | [funnel-analysis/SKILL.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/skills/funnel-analysis/SKILL.md) | Identidade, sequência, janela, coorte, denominador e composição de segmentos |
| G1 | [funnel-decomposition/SKILL.md](https://github.com/growthack88/growth-marketing-os/blob/c7852deefb3cd90029f02d328b9e59cea39ef585/skills/funnel-decomposition/SKILL.md) | Decompor mudança de receita e entregar explicação com tabela e ações |
| C4 | [working-agreement.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/references/working-agreement.md) | Contrato de evidência, contexto, acesso, vinculação e telemetria |
| C5 | [tools.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/references/tools.md) | Contratos de entrada, métodos e limites dos helpers; apresenta fontes metodológicas |
| C6 | [worked-failures.md](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/references/worked-failures.md) | Casos sintéticos de ordem, SRM, composição, duplicação, maturidade e decisão |
| C7 | [analyze.py](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/scripts/analyze.py) | Leitura estática completa das rotinas de experimento, amostra, funil, decomposição e perfil |
| C8 | [package-info.json](https://github.com/parasdoshicom/getchatdata/blob/cd3918b7c643a3c91d7961ac6b355b42587a00d2/plugins/chatdata/scripts/package-info.json) | Dependência local efetiva de C7, usada para proveniência da saída |

Não foram lidos os helpers de status, telemetria, retenção, joins, DuckDB, contexto local, instalação, hooks ou todos os testes e resultados de avaliações do ChatData. C5 menciona esses componentes; isso não valida suas implementações. G1 é uma skill curta sem recurso executável vinculado que determine o cálculo; nenhum outro pacote de Growth Marketing OS foi auditado. Alegações de experiência e resultados em contas reais de G1 não foram verificadas.

### Reuso e deduplicação

[Marketing e Tráfego — mensuração](2026-10-12-marketing-traffic-skills-measurement.md) já analisou Corey Haines `analytics`, `ab-testing`, `attribution`, Clamp e Digital Marketing Pro. Esses achados são reaproveitados como contexto, **sem contar nova leitura ou origem**. O caminho histórico Corey `ab-test-setup` respondeu 404 na busca; a revisão anterior usa `ab-testing`. Forks encontrados de marketingskills não aumentam evidência independente.

[Especialista de Dados — análise](2026-10-12-data-specialist-skills-analysis.md) já cobre grão, joins, validação, estatística e diagnóstico de métricas. A futura especialista de conversão reutiliza esses princípios e acrescenta decisões próprias de loja: pedido aprovado, cancelamento, devolução, margem e recuperação econômica. Não precisa repetir uma plataforma de análise de dados nem criar outro sistema de contexto.

`vermapragya/analytics-skill`, `tarunccet/pm-skills`, `coupler-io/skills` e outros resultados de funil foram descobertos, sem leitura integral nesta frente; não recebem avaliação de pacote nem status de aprovados. A busca parou quando as diferenças materiais entre definição, diagnóstico, priorização e inferência estavam cobertas. As candidatas de jornada, PDP e checkout pertencem à frente paralela e não são recontadas aqui.

## Comparação por componente

| Fonte/arquivo → componente | Decisão | Por que e como adaptar |
|---|---|---|
| C1 → definir decisão e efeito mínimo útil antes do teste | **Aproveitar** | Evita testar uma diferença sem valor econômico. Distinguir efeito em pontos percentuais de aumento relativo e de receita esperada. |
| C1/C2 → identidade estável, alocação e exposição separadas | **Aproveitar** | Uma pessoa recorrente não vira várias observações independentes. Declarar unidade de randomização e unidade de análise; tratar clusters, interferência e vazamento entre variantes conforme desenho. |
| C1 → cálculo de amostra e duração | **Adaptar** | Usar baseline e tráfego elegível reais. A aproximação binária de C7 não atende receita contínua, pedidos repetidos, clusters ou desenho sequencial. Sem inputs, informar o cálculo pendente, sem inventar amostra ou prazo. |
| C2 → SRM, maturidade, perdas e limites de dano | **Aproveitar** | Investigar mismatch com contagens de alocação e logs de exposição antes de chamar vencedor. Diferenciar perda de observação, desistência real e exclusão após tratamento. |
| C2/C7 → intervalo, p-valor e resultado candidato | **Adaptar** | C7 separa intervalo Newcombe/Wilson de teste normal agrupado. Não combinar critérios após olhar os resultados; usar método pré-especificado. Resultado do script é candidato condicionado ao desenho, jamais autorização automática para publicar. |
| C3 → funil definido antes de medir | **Aproveitar** | Declarar fechado/aberto, ordem, entrada, reentrada, janela, fuso e população. Medir pessoas, sessões ou pedidos de forma consistente; taxas de eventos não substituem taxas de pessoas. |
| C3/C7 → primeira entrada e maturidade completa | **Adaptar** | Bom padrão para um funil fechado por pessoa, mas não obrigatório para toda loja. Retorno em outra sessão, atribuição e compra posterior podem exigir outra definição. Não mudar silenciosamente a regra para obter taxa mais favorável. |
| C3/C7 → decomposição de composição e desempenho | **Aproveitar** | Recortes medidos na entrada reduzem condicionamento após tratamento. Segmentar por dispositivo, canal, novo/recorrente e categoria quando podem alterar a decisão; reconciliar agregado com grupos disjuntos e exaustivos. |
| C4 → contexto existente, permissões e evidência | **Adaptar** | Aproveitar materiais e acessos já autorizados; manter limites de leitura, custo e dados. Não exigir framework local de revisão para todo cálculo simples. Definição ausente limita a resposta oficial, mas permite hipótese e análise exploratória rotuladas. |
| C4 → conta vinculada, status.py e telemetria | **Descartar do pacote próprio** | O acordo exige vínculo no dashboard e contador antes de análise, embora C5 descreva helpers offline. É acoplamento comercial/operacional daquela skill, sem necessidade concreta do especialista SquadOS. Ler a fonte não autoriza executá-la ou contornar suas instruções de uso. |
| C3 → helper obrigatório e bloqueio de alternativa | **Adaptar** | Verificação deve sustentar o cálculo, não a existência de um script específico. Um cálculo curto pode ser conferido independentemente; consulta reproduzível é melhor quando a base exige sequência e deduplicação. Não apresentar método alternativo sem declarar mudança e limites. |
| C6 → exemplos de falhas verificáveis | **Aproveitar como inspiração** | Casos sintéticos são bons critérios de revisão futura; não demonstram impacto real da skill. Manter exemplos em referência sob demanda. |
| G1 → visitantes × taxas condicionais × ticket | **Adaptar** | A identidade só reconcilia receita se unidades, caminho e universo coincidirem. Compras que pulam etapas, múltiplos pedidos por comprador e divergência de receita bruta/líquida invalidam aplicação direta. |
| G1 → contribuição percentual e ação por alavanca | **Adaptar** | Explicar quanto cada fator contribuiu para a diferença, com método explícito. Substituição sequencial depende da ordem; log-decomposição exige tratamento de zeros. Delta próximo de zero ou fatores compensatórios tornam percentuais instáveis; mostrar valores absolutos e reconciliação. |
| G1 → maior contribuição é diagnóstico; resto é ruído | **Descartar** | Contribuição aritmética não identifica causa nem autoriza ignorar danos pequenos ou outros fatores. Um segmento menor pode ter problema grave ou forte potencial econômico. |
| G1 → prazo de 72 horas, corte de 10%, exatamente três ações | **Descartar como regra** | Não há suporte universal no arquivo. Prazo depende da maturidade e amostra; número de ações depende da decisão; limiar de relevância depende de volume, risco e economia. |
| G1 → perguntar uma vez e preencher etapas ausentes | **Adaptar** | Aproveitar o que foi fornecido e perguntar apenas a lacuna decisiva. Não fabricar taxas; projeções condicionais podem avançar, mas diagnóstico medido exige etapas ou uma decomposição compatível com os dados disponíveis. |

## O que a leitura estática do helper permite afirmar

C7 usa biblioteca padrão Python, lê CSV em memória e emite JSON; não contém chamada de rede. Isso se refere a **esse arquivo**, não a todo o plugin e seus hooks. Seu `main` lê `package-info.json`; copiar somente o Python omite uma dependência real. Python disponível no destino não foi verificado.

O funil remove duplicatas pela combinação pessoa/evento/timestamp, usa primeira entrada, timestamps estritamente crescentes e janela fixa desde a entrada. Exclui entradas sem acompanhamento completo; informa registros futuros, duplicados e ambiguidades de horário. Essa chave não substitui `event_id` confiável: eventos legítimos no mesmo instante e eventos repetidos com timestamps diferentes precisam de regra de negócio e proveniência. Não calcula automaticamente todos os tempos de passagem nem resolve identidade, consentimento ou bots.

O experimento aceita duas populações independentes com desfecho binário. Reporta diferença absoluta/relativa, intervalo Newcombe com Wilson, p-valor normal quando não esparso e SRM por qui-quadrado com um grau de liberdade. Usa limiar SRM 0,001, sem torná-lo uma garantia de integridade. O tamanho amostral é aproximação de horizonte fixo, alocação igual, sem correção automática para clusters, perdas, consultas repetidas ou múltiplas comparações.

A decomposição simétrica separa composição e mudança de taxas e informa residual de reconciliação. O código verifica rótulos únicos e contagens coerentes, mas não consegue provar que os segmentos fornecidos são disjuntos/exaustivos, nem que a extração tem cobertura correta. Nenhum desses cálculos foi executado nesta pesquisa. Fórmula visível, fixture documentado, resultado de teste e desempenho de um agente são evidências distintas.

## Adaptação profissional mínima para ecommerce

### Medição e reconciliação

Começar pelo significado da métrica e da linha da fonte: pessoa, sessão, evento, pedido ou item de pedido. Registrar numerador, denominador elegível, período, fuso, janela de conversão, data de extração e maturidade. Uma sessão com três eventos `purchase` não representa três pedidos; três pedidos de uma pessoa não representam três compradores.

Confirmar o estado comercial: criado, pago/aprovado, cancelado, reembolsado ou entregue, conforme a decisão. Definir receita bruta/líquida, desconto, frete, impostos, devoluções e moeda; reconciliar eventos com pedidos e receita aprovados. Junção de pedido com itens não pode repetir o valor total do pedido. Não usar soma de valores distintos como correção genérica, pois pedidos diferentes podem ter o mesmo valor.

Comparar períodos e coortes com acompanhamento equivalente. Mesmo período de calendário não garante mesma composição ou maturidade. Mostrar mudança de canal/dispositivo/novo versus recorrente antes de atribuir tudo ao checkout; um agregado pode piorar enquanto taxas internas melhoram. Composição explica a aritmética, sem estabelecer o efeito causal de mudar uma página.

### Diagnóstico e prioridade

Entregar perda observada e hipótese, evidência que apoiaria ou enfraqueceria a hipótese e próxima verificação útil. Maior queda percentual não implica maior oportunidade: considerar volume elegível, parcela recuperável plausível, receita/margem, esforço, prazo e risco. Quantificar impacto como cenário com premissas; não prometer uplift.

Um score de impacto/confiança/esforço pode ajudar a ordenar, mas é julgamento operacional. Não convertê-lo em probabilidade estatística, retorno garantido ou precisão artificial. Quando faltarem dados econômicos, priorizar uma investigação que possa mudar a decisão, sem inventar ticket, margem ou recuperação.

### Experimentos

O plano deve declarar população, alocação, unidade estável, exposição, métrica principal, efeito mínimo útil, potência, inferência, maturidade, duração e regra de parada. Definir métricas de proteção relevantes, como margem por unidade elegível, cancelamentos, devoluções, erros de pagamento e suporte. Métrica de receita exige estimador e variância apropriados; conversão binária não valida sozinha esse resultado.

Avaliar SRM, vazamento entre variantes, perdas desiguais e regras pós-tratamento antes do vencedor. Evitar filtrar apenas quem adicionou ao carrinho se a intervenção altera essa ação; a seleção muda a população. Segmentar depois de observar o resultado pode gerar hipótese, mas não uma confirmação sem tratamento de multiplicidade e validação posterior.

Horizonte fixo e inferência sequencial são desenhos diferentes. Consultas operacionais para segurança não autorizam interromper um teste fixo ao aparecer `p < 0,05`. Método sequencial precisa ser definido e implementado antes; não é uma correção improvisada ao final. Intervalo que cruza zero não demonstra ausência de efeito; p-valor alto não demonstra equivalência. Um resultado favorável pequeno pode não alcançar o benefício mínimo útil.

## Núcleo e referências sob demanda propostos

**Núcleo enxuto:** reconhecer intenção; aproveitar contexto; conferir definições materiais; escolher análise compatível; separar fato, hipótese e cenário; entregar resposta e próximos passos proporcionais. Não impor ferramenta, dashboard, dossiê extenso, questionário fixo ou experimento a toda solicitação.

| Recurso futuro | Quando carregar | Ganho concreto |
|---|---|---|
| `references/measurement.md` | Taxas, queda, receita ou fontes divergentes | Grão, elegibilidade, eventos/pedidos, maturidade, duplicação e reconciliação |
| `references/funnel-diagnosis.md` | Localizar perdas ou explicar mudança | Ordem, reentrada, decomposição, mix e hipóteses verificáveis |
| `references/experiments.md` | Planejar/revisar A/B ou avaliar vencedor | Unidade, SRM, potência, efeito, CI, parada, perdas e limites de dano |
| `references/prioritization.md` | Escolher o que corrigir/testar | Volume recuperável, economia, esforço, premissas e riscos |
| `templates/experiment-plan.md` | Documento operacional solicitado | Plano revisável com lacunas específicas; aprovação/lançamento em etapa posterior |
| Script pequeno, apenas se necessário | Base ou inferência que exija cálculo reproduzível | Sequência/deduplicação e cálculo verificável, com contratos delimitados; nunca framework obrigatório |

Não incorporar agora scripts, infraestrutura, instalação ou telemetria. Na criação posterior, conferir dependências existentes; quando faltar recurso concreto, oferecer o caminho simples de instalação em linguagem de trabalho e aproveitar autenticação já autorizada. A execução pelo agente é posterior à autorização correspondente; a pessoa não precisa receber comandos de terminal como requisito da pesquisa.

Quando definições de receita, etapas ou restrições da loja se repetirem, a especialista pode oferecer ajustar a própria skill para reutilizá-las. Isso é uma proposta baseada em recorrência real, sem memória automática inventada, conta adicional ou criação compulsória de serviço.

## Critérios de aceitação futuros — não executados

Os casos abaixo orientam a criação e a avaliação profissional posterior. Não são uma suíte já implementada nem uma alegação de confiabilidade determinística do agente.

| Pedido/caso | Evidência que a futura entrega deve apresentar |
|---|---|
| “Nossa conversão caiu”, dados com canais mudando de peso | Taxa agregada, numeradores/denominadores por segmento e contribuição de mix; checkout causal permanece hipótese |
| Purchase antes da entrada, duplicação e coorte recente | Ordem e deduplicação explícitas; janela incompleta fora do denominador principal; exclusões contabilizadas |
| Export mistura pessoas, sessões e eventos | Definição coerente ou taxa limitada ao universo disponível, sem trocar unidades silenciosamente |
| Receita de eventos diverge da receita aprovada | Reconciliação por pedido/status, cobertura, cancelamentos e reembolsos; conclusão financeira limitada até resolver diferença |
| Maior abandono percentual em etapa com pouco volume | Prioridade justificada por oportunidade e economia, sem escolher mecanicamente a maior porcentagem |
| A/B 50/50 observado como 60/40 sem explicação | SRM e investigação de alocação/exposição; efeito pode ser descritivo, mas vencedor fica sem sustentação |
| Mesma pessoa recebe variantes em várias sessões | Reconhecimento de contaminação e dependência; não calcular potência como se sessões fossem pessoas independentes |
| Teste fixo interrompido no primeiro p favorável | Regra de parada e consultas revisadas; não legitimar conclusão com CI fixo convencional |
| Efeito positivo com intervalo amplo e benefício útil maior | Estimativa, incerteza, limiar econômico e risco; recomendação condicional, sem garantia de uplift |
| Auditoria de checkout sem analytics | Observações e hipóteses úteis; nenhuma taxa ou causa inventada; pergunta apenas pelo dado que muda a decisão |
| Dependência indisponível ou contexto repetitivo | Capacidade real conferida, alternativa delimitada e instalação/adaptação oferecida sem pressupor que o Studio já possui o recurso |

## Limites e próximas verificações

A leitura foi estática e pública. Nenhuma skill foi contratada, instalada ou executada; não foram utilizados dados de cliente, teste em loja ou serviço pago. Os casos de C6 são sintéticos. A descrição de G1 como aplicada em contas reais é uma afirmação da fonte, sem caso identificável validado nesta frente.

Na criação posterior, conferir fórmulas e desenhos com documentação profissional primária, revisar os recursos eventualmente incorporados e avaliar casos representativos com dados autorizados. A frente de métodos desta rodada complementa as fontes profissionais; links metodológicos presentes em C5 foram identificados, sem presumir leitura integral dos artigos nesta frente. Pesquisa, pacote verificável, proposta revisável, aprovação/instalação e execução real continuam sendo etapas distintas.
