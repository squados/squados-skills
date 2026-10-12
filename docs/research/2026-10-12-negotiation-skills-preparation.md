# Especialista em Negociação — skills existentes de preparação

Data da consulta: 12/10/2026. Frente da rodada 14/33: preparação, alternativas, limites, cenários, concessões e brief. Pesquisa autoral para orientar uma skill futura de uso interno. Não houve criação de pacote, instalação, execução de código remoto, contato com terceiros ou negociação real. Este documento não comprova execução, resultados negociais ou compatibilidade com Hermes.

## Decisão recomendada

Usar a revisão atual de **prashaantr/stanford-gsb-negotiation** como referência principal de comportamento: coach privado, inferência da intenção, contexto reaproveitado, lacunas explícitas, avaliação do pacote completo e brief proporcional. Complementar com a distinção entre **limite de autoridade e ponto de saída** em samber e com a separação **fato/hipótese/informação que mudaria a decisão** de l4ci. Club de Negociación oferece bons exemplos de BATNA externo e mapa de interesses, mas exige corrigir inconsistências antes de qualquer adaptação. Foreman serve de contraste para concessões; sua previsão por ponto médio não deve orientar o padrão.

Aproveitar significa usar o componente como referência para síntese autoral. Copiar ou adaptar substancialmente um texto exige preservar sua licença e avisos; a leitura pública não transfere autoria. Nenhum dos cinco repositórios está entre as quatro origens GitHub aceitas atualmente pelo catálogo. Não propor sua inclusão direta em `gallery.json`.

## Descoberta, alcance e contagens

Buscas: `site:skills.sh negotiation BATNA`, `github SKILL.md negotiation preparation BATNA`, `site:skills.sh negotiation strategist`, `site:skills.sh "negotiation"`, `"l4ci" "negotiation-prep" github` e `"samber" "influence-and-negotiation" github`. Consultados skills.sh, Skills Directory, SkillMD e páginas de repositórios. Diretórios ajudam a achar o original; instalações, estrelas, notas e selos de segurança não entraram no julgamento de método.

**Contagem desta frente:** 11 identidades de candidatas triadas abaixo; cinco pacotes com SKILL.md integral efetivamente lido; 27 arquivos integrais consultados, incluindo cinco SKILL.md, recursos decisivos, exemplos e textos de licença. Contagem de arquivos dos pacotes por árvore Git no SHA: Club 7; Stanford 10; l4ci 5; samber 13; Foreman 1 na pasta da skill, com dependências fora dela. Não representa contagem de toda a internet nem auditoria integral dos cinco repositórios.

| Candidata descoberta | Decisão de leitura nesta frente |
|---|---|
| [clubdenegociacion/negotiation-skill](https://github.com/clubdenegociacion/negotiation-skill) | Selecionada: sete elementos, MAAN e preparação estruturada |
| [prashaantr/teach-claude-something-new](https://github.com/prashaantr/teach-claude-something-new/tree/main/business/stanford-gsb-negotiation) | Selecionada: pacote atual enxuto e limites explícitos |
| [l4ci/latticework negotiation-prep](https://github.com/l4ci/latticework/tree/main/skills/negotiation-prep) | Selecionada: fatos/hipóteses, BATNA, ZOPA e exemplo completo |
| [samber/cc-skills influence-and-negotiation](https://skills.sh/samber/cc-skills/influence-and-negotiation) | Selecionada: mandato, escalonamento e contexto; original conferido |
| [fatihguner/foreman competitive-negotiation](https://github.com/fatihguner/foreman/tree/main/plugins/foreman/skills/competitive-negotiation) | Selecionada como contraponto distributivo e planejamento de concessões |
| [wondelai/skills negotiation](https://github.com/wondelai/skills/tree/main/negotiation) | Encaminhada à frente de simulação/revisão; não contada como leitura integral aqui |
| [mikesmayer/claude-business-skills negotiation](https://github.com/mikesmayer/claude-business-skills/tree/main/negotiation) | Frontmatter visível atribui wondelai v1.2.0; possível cópia/linhagem, não evidência independente |
| [borghei/Claude-Skills mediation-analysis](https://github.com/borghei/Claude-Skills/tree/main/legal/mediation-analysis) | Escopo jurídico e declaração MIT + Commons Clause; não selecionada, licença integral não auditada |
| [majiayu000/claude-skill-registry negotiation-expert-infrastructure](https://github.com/majiayu000/claude-skill-registry/tree/main/skills/data/negotiation-expert-infrastructure) | Registro/espelho e calculadora imobiliária/expropriação; origem e módulos externos não resolvidos, fora do padrão geral |
| [coinluu/negotiation-war-room-skill](https://github.com/coinluu/negotiation-war-room-skill) | Descoberta de repertório extenso, power score e múltiplos playbooks; não selecionada para aprofundamento após decisões de preparo resolvidas |
| [wuraaang/claude-code-skills howtotalk](https://github.com/wuraaang/claude-code-skills/tree/main/howtotalk) | Comunicação geral; componente BATNA visto na descoberta, sem profundidade necessária para a seleção de preparo |

Cinco fontes selecionadas não são forks segundo o campo `fork` da API GitHub. Isso não demonstra originalidade textual ou direitos sobre técnicas citadas. Compartilhar Fisher/Ury, sete elementos ou Voss tampouco cria cinco demonstrações independentes da eficácia desses métodos. Club e Stanford usam sete elementos com comportamentos diferentes; samber mistura escolas; Foreman é parte de um sistema próprio. A relação mikesmayer → wondelai é sugerida pela atribuição preservada no frontmatter, sem comparação completa ou auditoria de histórico nesta frente.

## Revisões, autoria e licença

Os SHAs abaixo vieram de `git ls-remote ... HEAD`; árvores e último commit de SKILL.md foram consultados por `gh api`, em leitura. A API anônima respondeu 403 por limite de requisições; a consulta autenticada já disponível funcionou. Não foi feito clone. Os caminhos inicialmente divulgados para Stanford omitiram `business/` e retornaram 404; a árvore atual resolveu o caminho. Datas são do commit do arquivo, não prova de lançamento ou validade de mercado.

| Fonte | HEAD fixado / último commit da SKILL | Data UTC da SKILL / autoria verificável | Licença efetivamente lida |
|---|---|---|---|
| Club | `fc3f40a7882ea5306fd81cc48f4f7f97fb6831b6` / mesmo SHA | 2026-04-05 01:14:50; commit `isaacgbc`; crédito declarado Club de Negociación — Consultoría Francisco Gutiérrez | MIT integral em README, copyright 2026 Club. API identifica licença como null; não há LICENSE dedicado na árvore. Frontmatter da SKILL não declara licença |
| Stanford | `e8b1d4b9a68d8ee6555358472b86da6ef8230b6f` / mesmo SHA | 2026-07-22 06:27:31; PrashaantR | `business/stanford-gsb-negotiation/LICENSE.txt`: MIT, copyright 2025 sem titular preenchido. Repositório não tem licença detectada na raiz; licença local é a evidência relevante. Não é produto oficial Stanford; a própria SKILL adverte isso |
| l4ci | `b2335b7c2bd3b8f368b898151949497953127213` / `ecca174f31d3091e593ceac425c6ec0024768584` | 2026-06-19 16:28:31; Volker Otto | LICENSE raiz MIT, copyright 2026 Volker Otto; frontmatter sem licença |
| samber | `123cb155f5ab5751fc13c8027fbfa5eb0d3773c6` / `f866b800353719270a9ea101a41c5e2a2618d460` | 2026-09-02 18:52:33; Samuel Berthe; SKILL v1.1.2 | LICENSE raiz MIT, copyright 2026 Samuel Berthe; frontmatter MIT |
| Foreman | `0700130bac7f054647873f98a8ad42f6a15f8316` / `8469851ee35b509d37867088b2762ef7288f05ba` | 2026-09-05 11:03:35; Fatih Guner; SKILL v1.0.0 | LICENSE raiz MIT, copyright 2026 Fatih Guner; frontmatter sem licença |

Para adaptação textual futura, preservar copyright e texto de permissão MIT aplicável; o campo ausente do Stanford merece esclarecimento antes de usar porções substanciais ou redistribuir. Não transformar o nome Stanford, créditos de professores ou referências a livros em endosso institucional. Nenhum conteúdo de livro foi importado neste dossiê.

## Inventário de leitura e limites

Todos os caminhos podem ser consultados de forma imutável como `https://raw.githubusercontent.com/<repo>/<HEAD>/<caminho>`. As URLs de entrada fixadas abaixo sustentam a comparação, sem depender de snapshots dos diretórios.

| Fonte / entrada fixada | Arquivos integrais lidos | Limite |
|---|---|---|
| [Club SKILL](https://raw.githubusercontent.com/clubdenegociacion/negotiation-skill/fc3f40a7882ea5306fd81cc48f4f7f97fb6831b6/SKILL.md) | SKILL.md; README.md; references/seven-elements.md; references/maan-guide.md; references/collaborative-framework.md; assets/preparation-template.md | 6/7 arquivos; package.json não lido. Não executei instalador nem prática |
| [Stanford SKILL](https://raw.githubusercontent.com/prashaantr/teach-claude-something-new/e8b1d4b9a68d8ee6555358472b86da6ef8230b6f/business/stanford-gsb-negotiation/SKILL.md) | SKILL.md; LICENSE.txt; references/preparation.md; references/frameworks.md; references/research-templates.md; references/examples.md | 6/10; live-coaching, difficult-tactics, emotion-scripts e tactics ficam fora desta frente. Brief e preparo cobertos; simulação não auditada aqui |
| [l4ci SKILL](https://raw.githubusercontent.com/l4ci/latticework/b2335b7c2bd3b8f368b898151949497953127213/skills/negotiation-prep/SKILL.md) | Os cinco arquivos da pasta: SKILL.md; README.md; references/negotiation.md; references/example.md; references/negotiation-prep-meridian-offer-2026-06-19.md; mais LICENSE raiz | 5/5 da pasta + licença. Exemplo explicitamente fictício, sem execução independente |
| [samber SKILL](https://raw.githubusercontent.com/samber/cc-skills/123cb155f5ab5751fc13c8027fbfa5eb0d3773c6/skills/influence-and-negotiation/SKILL.md) | SKILL.md; references/prepare.md; references/context-intake.md; references/memory.md; LICENSE raiz | 4/13 da pasta + licença. Evals, táticas, objeções e playbooks não lidos; nenhuma alegação de execução ou taxa de erro validada |
| [Foreman SKILL](https://raw.githubusercontent.com/fatihguner/foreman/0700130bac7f054647873f98a8ad42f6a15f8316/plugins/foreman/skills/competitive-negotiation/SKILL.md) | SKILL.md; plugins/foreman/content/RUNTIME.md; plugins/foreman/content/policies/advisory.md; LICENSE raiz | 1/1 da pasta, mas pacote depende do content/runtime externo. Catalog, run.mjs e skills relacionadas não auditados nem executados |

Tamanho da pasta por `size` da árvore Git: Club 91.275 bytes; Stanford 39.406; l4ci 36.327; samber 275.937; Foreman 24.466 na pasta, sem somar dependências externas. Esses tamanhos são inventário, não custo de tokens, segurança ou compatibilidade.

## Comparação dos componentes

| Fonte/arquivo → componente | Decisão | Motivo e adaptação concreta |
|---|---|---|
| Stanford SKILL → coach privado e intenção inferida | Aproveitar | Serve preparo, análise ou mensagem sem menu obrigatório; não presume autorização para falar, enviar ou aceitar. Papel e entrada disponíveis explícitos |
| Stanford SKILL → ledger de negociação | Adaptar | Reaproveitar conversa e arquivos já fornecidos; registrar só fatos materiais, proposta atual, concessões e pendências. Um resumo no brief basta; não criar persistência automática |
| Stanford preparation → intake proporcional | Aproveitar | Pergunta só o que altera a decisão; desconhecidos não impedem ajuda parcial. Separar limite econômico, autoridade e prazo real |
| Stanford frameworks → reserva como pacote completo | Aproveitar | Distingue BATNA, aspiração e abertura; inclui tempo, custo, risco, escopo e relacionamento. Não converter tudo em um salário ou preço isolado |
| Stanford preparation → duas/três ofertas equivalentes | Adaptar | Ofertas aproximadamente equivalentes ao usuário revelam preferências. Só gerar quando houver múltiplos assuntos, preferências e limites suficientes; equivalência precisa de critério explícito |
| Stanford research-templates → critério objetivo comparável | Aproveitar | Geografia, data, nível, composição e custos totais; verificar fatos atuais que alteram a estratégia. Evita usar preço anunciado como transação concluída ou salário-base como remuneração total |
| Stanford examples → deadline e status da proposta | Aproveitar | Trata aumento e prazo como relato, urgência artificial como hipótese; não chama discussão de acordo. Exemplos declarados fictícios ajudam a testar forma, não resultado |
| Club maan-guide → alternativa fora da mesa | Aproveitar | Exemplos corretos/incorretos distinguem outra oferta, manter o estado atual e pedir desconto. Uma vontade de achar outro fornecedor não é alternativa executável |
| Club seven-elements/template → interesses, opções, legitimidade, compromissos | Adaptar | Boa cobertura e campos fonte/hipótese; manter os sete elementos reais, sem exigir ficha longa ou dez opções em todo pedido |
| Club SKILL prepare → lista rotulada sete elementos | Descartar como estrutura exata | Substitui Compromissos por ZOPA, embora a referência correta inclua Compromissos. Conservar ZOPA como análise condicional dentro de alternativas/pacotes |
| Club maan-guide → fórmula genérica da reserva | Descartar | Soma custos no enunciado e usa custo negativo no exemplo; direção muda entre comprador/vendedor e utilidades não monetárias. Comparar fluxos e pacotes, explicando perspectiva/unidade, sem uma fórmula universal |
| Club → notas MAAN 1–10, opções 5–8/10+, sempre colaborativo | Adaptar/descartar rigidez | Qualidade da alternativa se descreve por viabilidade/evidência/custo, sem falsa escala objetiva. Postura respeitosa não obriga acordo, concessão ou colaboração substantiva em todo contexto |
| Club collaborative-framework → percentuais 15–30%, superioridade universal | Descartar como evidência | Não há estudo primário identificável junto dessas porcentagens. Não transferir promessa causal ou taxa de sucesso |
| l4ci SKILL → fato/hipótese/confiança/informação que mudaria conclusão | Aproveitar | Reduz invenção sobre alternativas e interesses da contraparte; transformar hipóteses decisivas em perguntas verificáveis, em vez de perfil psicológico |
| l4ci SKILL → cinco analistas obrigatórios + redispatch até todos retornarem | Descartar | Custo e ferramentas desnecessários para preparo comum; os cinco eixos são úteis como raciocínio, não infraestrutura obrigatória |
| l4ci negotiation.md → BATNA, alvo, reserva e ZOPA separados | Adaptar | Não aceitar automaticamente qualquer acordo acima da BATNA: ainda verificar interesses críticos, riscos, autoridade e implementação. ZOPA desconhecida continua desconhecida |
| l4ci relatório Meridian → exemplo extenso com rótulos | Adaptar criticamente | Cabeçalho informa ficção, mas o corpo trata BATNA verbal como forte, estima teto com empresa de 400 pessoas e afirma ZOPA ampla. Não imitar esse salto; o desconhecido deve limitar a conclusão |
| samber prepare → mandato e escalonamento separados de saída | Aproveitar | Diferencia o que a pessoa pode autorizar do mínimo da organização. Pedir responsável/condição de consulta quando necessário, nunca inventar autoridade |
| samber prepare → cinco pontos por eixo | Adaptar | Abrir/ideal/meta/escalonar/sair é útil em negociação complexa; em pedido simples, meta, limite e autoridade bastam. Não exigir cinco respostas por assunto |
| samber context-intake → rastrear fonte e contradições | Aproveitar | Contexto e concessões anteriores importam; contradição é dúvida a resolver, não automaticamente arma ou prova de mentira |
| samber context-intake → 3–20 agentes, todos conectores, gate de última fala | Descartar | Pesquisa obrigatória de todas as fontes invade escopo e encarece; preparação futura pode não ter fala anterior. Pesquisar só lacuna material e fontes autorizadas |
| samber memory → seis arquivos automáticos | Descartar como padrão | Reuso de contexto cabe no brief. Persistência adicional só se houver recorrência e desejo claro; nunca criar memória externa só por ter acesso |
| samber prepare → BATNA guardada durante execução | Descartar | Orienta agir como se fosse único negócio; não remover comparação com alternativas quando uma nova proposta muda a decisão. Revisar BATNA sob fatos novos, sem teatralizar ameaça |
| samber prepare → MICE/microexpressões, silêncio/olhar revelam motivo | Descartar como diagnóstico | Observação não confirma ego, mentira ou intenção privada. Sem entrada audiovisual nem base verificável, não alegar leitura de comportamento |
| Foreman competitive → concessão condicional e vínculos entre assuntos | Adaptar | Usar condição, contrapartida, custo, autorização e efeito no pacote. Pode quebrar impasse sem desconto; não exige concessão em todas as rodadas |
| Foreman competitive → alvo pela média e contraproposta extrema | Descartar como default | Exemplos demonstram aritmética, não previsibilidade do resultado. Ponto médio não prova preço justo, ZOPA ou melhor abertura |
| Foreman competitive → fingir relutância/dificuldade de aprovação | Descartar | Só relatar restrições verdadeiras. Não fabricar aprovação difícil, escassez ou urgência para gerir percepções |
| Foreman advisory → fatos/hipóteses, perguntas materiais, exemplos ilustrativos | Aproveitar | Política externa é mais cuidadosa que algumas generalizações da SKILL; preservar essa disciplina na síntese |
| Foreman RUNTIME → Node ≥22.19, state.json e catálogo | Descartar do pacote de negociação | Serve persistência do framework; não resolve brief ou concessões. Nenhuma necessidade de executar ou portar runtime |

## Divergências que afetam o uso

**Criar valor e distribuir valor:** Club prioriza construção colaborativa; Foreman trata o problema como distributivo. Padrão recomendado: explorar prioridades e diferenças quando houver vários termos; defender interesse e reserva usando critério verificável quando houver disputa real de valor. Firmeza não requer intimidação. Não classificar toda negociação como soma zero nem prometer ganho conjunto possível sempre.

**Abrir cedo ou tarde:** Foreman recomenda normalmente ir primeiro; samber diz ancorar tarde; Stanford condiciona abertura a evidência e risco. Adotar decisão contextual: o usuário conhece faixa/critério suficiente? Uma oferta extrema cria risco de ruptura? Já existe proposta? Sem base, preparar perguntas e pausa antes de número. Não há benchmark desta frente que resolva a decisão por percentual.

**BATNA e reserva:** BATNA é curso de ação externo; reserva é pacote que a pessoa compara com ele. Custo e risco podem alterar a equivalência, mas o agente não decide preferências privadas nem substitui autoridade. Oferta concorrente verbal não equivale a alternativa executável garantida. Não ter outra proposta não obriga aceitar qualquer coisa: status quo, pausa ou não contratar podem ser alternativas com custos próprios.

**ZOPA:** cenários devem explicitar hipóteses; desconhecer a reserva da contraparte não comprova ausência de acordo. Em vários assuntos, duas faixas monetárias que não se cruzam podem admitir pacote por prazo, escopo ou risco. Não anunciar faixa precisa onde só há palpite.

**Concessões:** sequência planejada ajuda a evitar desconto impulsivo, mas escada fixa de 3–5 rodadas pode prejudicar uma proposta clara ou negociação cooperativa. Preparar trocas possíveis e condição de revisão; usar passos decrescentes apenas quando apropriados e autorizados. Novo fato pode mudar a estratégia inteira.

## Proposta de organização posterior

### Núcleo curto

Reconhecer pedido e entrega; reutilizar contexto existente; identificar interesses, proposta atual e desconhecidos que alteram a decisão; distinguir BATNA/aspiração/reserva/autoridade; perguntar proporcionalmente; sugerir pacote e próximo passo privado. Não inventar números, descontos, urgência, alternativas, motivos ou permissões. Se faltarem dados para recomendação firme, entregar análise condicional com uma pergunta decisiva, em vez de ficha completa obrigatória.

Formato mínimo de brief: situação e decisão; objetivo e interesses ordenados; proposta atual; alternativa executável e lacunas; limite/condição de consulta; pacote ou opções; perguntas importantes; concessões condicionais possíveis; pausa/saída; o que precisa ser confirmado. Expandir só o necessário ao caso.

### Referências sob demanda

- `references/preparation.md`: alternativa real, custos e prazo, comparação de pacote, reserva, contexto e perguntas; métodos autorais com fontes primárias revisadas pela frente profissional.
- `references/packages-and-concessions.md`: pacotes, equivalência para o usuário, concessões condicionais, autorização, custos de entrega e pressupostos da contraparte.
- `references/criteria-and-evidence.md`: comparabilidade, data, unidades, fonte, faixa e incerteza; limites de preço anunciado, oferta verbal e dados não comparáveis.
- `templates/negotiation-brief.md`: brief curto com campos omitíveis, desconhecidos e propostas separadas de compromissos. Uma versão de uma página pode atender reunião; não obrigar formato em toda pergunta.

Esses nomes são proposta de organização, não arquivos criados. Bibliografia, descoberta e histórico de candidatos permanecem no dossiê de pesquisa, fora do núcleo executável.

### Cálculos, dependências e recorrência

Nenhum script necessário ao preparo padrão. Um cálculo mecânico poderia agregar custo total, parcelas ou cenários com probabilidades fornecidas; nunca estimar sozinho probabilidade de acordo ou fabricar score de poder. Se surgir volume recorrente, propor recurso específico com benefício claro, preservando a opção de comparação textual ou tabela simples. Dependência ausente pede oferta compreensível de alternativa ou preparação autorizada, não instrução de terminal à pessoa.

Se o usuário repetir negociações com critérios próprios e aceitar adaptação, oferecer ajustar a própria skill e um modelo de brief reutilizável. Não criar sistema de memória, conta, conector ou pacote automaticamente. Reuso do contexto já disponível vem antes de novas perguntas.

## Critérios para revisão da skill futura

Estes são critérios de leitura e casos propostos, **não testes executados**:

- Usuário traz proposta completa: reaproveita termos e pergunta só a lacuna material.
- Usuário não tem alternativa confirmada: distingue opção em prospecção, status quo e alternativa executável; não fabrica outra oferta.
- Usuário fornece meta, mas não autoridade: prepara opções condicionais e condição de consulta, sem oferecer desconto em seu nome.
- Contraparte diz orçamento final ou prazo hoje: registra como relato e prepara verificação, sem diagnosticar mentira.
- Preços não cruzam, mas há prazo/escopo negociáveis: explora pacote sem declarar ZOPA impossível por um único número.
- Usuário pede só brief: entrega brief; não exige subagentes, conectores, memória ou curso de técnicas.
- Cenário com duas ofertas: compara pacote inteiro e explicita custo, risco e prazo; não soma monetizações subjetivas sem critério do usuário.
- Conteúdo privado e limite de reserva: permanece no aconselhamento interno; draft futuro inclui apenas divulgação escolhida e autorizada.
- Pedido envolve cláusula, vínculo trabalhista ou acordo jurídico material: delimita incerteza específica e necessidade de revisão profissional, sem fingir conclusão legal.

## Lacunas e limite da conclusão

Não há negociação real observada, métrica de sucesso, benchmark de agente, execução de evals ou validação funcional. Exemplos de Stanford e l4ci são explicitamente fictícios; casos e porcentagens de outros textos não tiveram verificação primária nesta frente. O estudo seleciona componentes de instrução, não comprova eficácia de técnicas.

Compatibilidade Hermes e empacotamento permanecem não demonstrados. Frontmatter ausente, dependências externas, recursos fora do contrato e ferramentas de Claude precisam de revisão posterior se um pacote vier a ser adaptado. Nenhuma decisão de catálogo, autoria SquadOS, publicação ou distribuição de terceiros foi tomada. Busca encerrada porque as decisões materiais de preparo, contexto, limites, pacote e concessões estão resolvidas; não há necessidade de acumular mais skills para uma quota.
