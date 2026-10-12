# Desenvolvimento de Pessoas — feedback, coaching de trabalho e apoio a gestores

Pesquisa em 12/10/2026, rodada 33. Esta frente trata de preparar ou revisar feedback, organizar 1:1, apoiar reflexão sobre um problema de trabalho e acompanhar uma mudança observável. Onboarding, carreira e PDI pertencem à outra frente da rodada. A recomendação é combinar clareza de conversa, evidência verificável e acompanhamento proporcional, sem transformar toda solicitação em ciclo formal de desempenho.

## Cobertura e método

Descoberta por skills.sh, seguida de leitura do GitHub original por raw fixado em revisão. Foram lidos **10 arquivos SKILL completos de 7 repositórios e 6 famílias**, além de **9 recursos completos** e **1 recurso parcialmente consultado**. Refound e Lenny Plus contam como uma família intelectual: o recurso `SOURCE_SUMMARY.md` do segundo declara a derivação, embora a API marque ambos como `fork: false`. As duas skills Softaworks contam como dois arquivos de uma família; as cópias em `dist/plugins/` não entram novamente. Dois arquivos Owl contam como uma família. Não é amostra representativa do universo de skills nem comprovação de qualidade por popularidade.

Foram usadas pesquisa web, API pública GitHub, raw e `git ls-remote ... HEAD`, sem autenticação, tokens, créditos pagos, clones ou instalação. As instruções globais, AGENTS do repositório, README, CONTRIBUTING e síntese da rodada de Treinamentos foram lidas. Não havia CLAUDE na raiz nem pares locais em `docs/` identificados na busca. A consulta breve ao registro de memória não encontrou contexto relevante utilizado.

**Nada foi executado.** Nenhuma skill, avaliação do autor ou fluxo de coaching foi testado com agente ou pessoa. O dossiê registra comportamento prescrito pelos arquivos, não resultado demonstrado. Só este documento foi criado; índice, pacotes, Desktop, commits e publicação ficam fora da tarefa.

### Descoberta e discrepância de catálogo

Os leads foram [1:1 Refound](https://www.skills.sh/refoundai/lenny-skills/running-effective-1-1s), [conversas difíceis Refound](https://www.skills.sh/refoundai/lenny-skills/having-difficult-conversations), [1:1 Owl](https://www.skills.sh/owl-listener/design-leadership-skills/one-on-one), [feedback Softaworks](https://www.skills.sh/softaworks/agent-toolkit/feedback-mastery), [conversas difíceis Softaworks](https://www.skills.sh/softaworks/agent-toolkit/difficult-workplace-conversations), [HRBP](https://www.skills.sh/tuanductran/hr-skills/hr-business-partner), [revisão de chamada](https://www.skills.sh/mbfinotti/sales-skills/sales-call-review), [coaching UX](https://www.skills.sh/microsoft/hve-core/ux-coaching) e [Lenny Plus](https://www.skills.sh/liqiongyu/lenny_skills_plus/having-difficult-conversations).

O catálogo skills.sh ainda descrevia os dois caminhos Refound antigos, ausentes da árvore do HEAD consultado. A seleção atual do original foi `giving-feedback` e `coaching-development`. Não contabilizar a descrição antiga como leitura de um pacote atual, nem usar seu comando de instalação sem conferir resolução. A página GitHub Refound falhou no leitor web por timeout; API pública e raw funcionaram. Os recursos foram obtidos do original, não da página intermediária.

Leads fora da seleção: `interview-coach` trata preparação de candidato; coaching instrucional de professores tem contexto escolar; `trade-performance-coach` trata trading; `feedback-summarization` requer ServiceNow. Esses resultados foram apenas triados pela descrição de descoberta e não entram nos 10 arquivos lidos. Popularidade, estrelas e selos do agregador não substituem revisão comportamental.

## Revisões, autoria, licença e datas

Os SHAs abaixo foram resolvidos por `ls-remote HEAD`. As datas são a última alteração do arquivo SKILL encontrada pela API GitHub no acesso, em UTC; não são datas de validação do método nem garantem atualização dos recursos. Os nomes de autores refletem frontmatter ou copyright observado, não investigação independente de identidade.

| Família / repositório | Pin observado | Autoria e licença observadas | Última alteração dos SKILL consultados |
|---|---|---|---|
| [RefoundAI/lenny-skills](https://github.com/RefoundAI/lenny-skills/tree/13598cc54e09399bc1bc1398b0fca284110efb2f) | `13598cc54e09399bc1bc1398b0fca284110efb2f` | Refound AI; MIT da raiz, copyright 2025 | Feedback: 2026-07-13; coaching: 2026-07-15 |
| [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit/tree/3027f20f3181758385a1bb8c022d4041dfb4de84) | `3027f20f3181758385a1bb8c022d4041dfb4de84` | Copyright Leonardo Flores 2026; MIT raiz | Ambos: 2026-01-18 |
| [Owl-Listener/design-leadership-skills](https://github.com/Owl-Listener/design-leadership-skills/tree/9b801db464b25c73e709a77a358854eac43a4937) | `9b801db464b25c73e709a77a358854eac43a4937` | Copyright MC Dean 2026; MIT raiz | Ambos: 2026-06-07 |
| [tuanductran/hr-skills](https://github.com/tuanductran/hr-skills/tree/078f2fb651f1090e73a8cc6ba96f323f8b00b171) | `078f2fb651f1090e73a8cc6ba96f323f8b00b171` | Tuan Duc Tran; MIT raiz; skill 1.0.1 | HRBP: 2026-07-29 |
| [mbfinotti/sales-skills](https://github.com/mbfinotti/sales-skills/tree/1ef68881b2ed853fb1f02272b57dc71dd375677f) | `1ef68881b2ed853fb1f02272b57dc71dd375677f` | Frontmatter Maya-Beth Finotti; copyright Nativa Labs 2026; MIT; skill 1.2.6 | Revisão de chamada: 2026-08-21 |
| [microsoft/hve-core](https://github.com/microsoft/hve-core/tree/beca41e33ff7253862b2b990264c2e48351119b6) | `beca41e33ff7253862b2b990264c2e48351119b6` | Microsoft Corporation; MIT raiz e frontmatter | Coaching UX: 2026-08-13 |
| [liqiongyu/lenny_skills_plus](https://github.com/liqiongyu/lenny_skills_plus/tree/df4fa3412a9252d86c92f32351ba997e31667790) | `df4fa3412a9252d86c92f32351ba997e31667790` | Mantenedor liqiongyu; derivação Refound declarada; API SPDX Apache-2.0 e cabeçalho Apache 2.0 | Conversas difíceis: 2026-04-04 |

As seis licenças MIT foram lidas integralmente. A licença Apache do derivado foi consultada pelo cabeçalho e metadado SPDX, sem revisão integral de termos/NOTICE. Arquivos de licença em cada árvore fixada são acessíveis como `LICENSE`. Uma licença permissiva do repositório não resolve direitos de cursos, podcasts, livros, falas extensas, estudos, rubricas ou instrumentos extraídos de terceiros. Refound usa corpus Lenny; Lenny Plus herda essa origem. A proposta é autoral em PT-BR, com referências aos conceitos e sem copiar expressão, diálogos, cursos ou instrumentos. Reutilização literal futura exige avaliar os avisos e a proveniência do trecho.

Nenhum desses repositórios é fonte GitHub aceita diretamente pelo contrato atual da galeria. Qualquer futura skill própria precisa de contrato e revisão próprios; leitura e licença não demonstram compatibilidade Hermes.

## Componentes comparados

Cada link de SKILL abaixo aponta para o conteúdo original fixado e lido completo.

| Skill / componente | Aproveitar ou adaptar | Descartar ou manter fora desta frente |
|---|---|---|
| [Refound: giving-feedback](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/giving-feedback/SKILL.md) | Preparação, revisão de rótulos e debrief; distinguir ação, interpretação, impacto e contribuição do gestor | Voz como passo obrigatório; cobrança emocional; críticas pessoais em público; promoção e frases/casos extraídos |
| [Refound: coaching-development](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/coaching-development/SKILL.md) | Perguntas que aumentam autonomia; ajuda prática temporária com retirada explícita | Supor que todo problema é déficit de habilidade interna; high-potential; career ladders; percentuais de bem-estar como causalidade |
| [Owl: one-on-one](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/people-management/skills/one-on-one/SKILL.md) | Agenda do colaborador, bloqueios, feedback recíproco e continuidade | Quota 70/30; proibição universal de cancelamento; exigir relato íntimo para pauta profissional |
| [Owl: difficult-conversation](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/people-management/skills/difficult-conversation/SKILL.md) | Núcleo curto: finalidade, fatos, perspectiva a ouvir, abertura e acordo | Seguir prazo ou exigir mudança antes de validar expectativa, oportunidade e recursos |
| [Softaworks: feedback-mastery](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/feedback-mastery/SKILL.md) | Situação, comportamento e impacto; receber feedback; combinar suporte e retomada | Alegações de 60% e 30% sem fonte identificada; exemplos só de software; tratar impressão como fato |
| [Softaworks: difficult-workplace-conversations](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/difficult-workplace-conversations/SKILL.md) | Preparar, conversar e acompanhar; detalhes sob demanda | Espera fixa de 24h; documentação automática; remuneração, desligamento e gestão formal de conflito |
| [HRBP](https://github.com/tuanductran/hr-skills/blob/078f2fb651f1090e73a8cc6ba96f323f8b00b171/skills/hr-business-partner/SKILL.md) | Investigar clareza, carga, recursos e apoio gerencial antes de individualizar a lacuna | 9-box, risco de retenção de pessoas, investigação, sucessão, PIP automático e decisões de emprego |
| [Sales call review](https://github.com/mbfinotti/sales-skills/blob/1ef68881b2ed853fb1f02272b57dc71dd375677f/skills/sales-call-review/SKILL.md) | Trecho localizável por observação; informação ausente não vira zero; distinguir ação e resultado; acompanhamento do foco acordado | Rubrica numérica universal, pesos próprios, ranking de pessoas, quota de itens, prazos presumidos e memória pessoal automática |
| [Microsoft UX coaching](https://github.com/microsoft/hve-core/blob/beca41e33ff7253862b2b990264c2e48351119b6/.github/skills/design-thinking/ux-coaching/SKILL.md) | Evidência, hipótese e dúvida separadas; uma pergunta material; suporte gradual e respeitar redirecionamento | Escolha/configuração de momentos, slug, YAML obrigatório e proibição de entregar uma resposta pedida diretamente |
| [Lenny Plus: difficult conversations](https://github.com/liqiongyu/lenny_skills_plus/blob/df4fa3412a9252d86c92f32351ba997e31667790/skills/having-difficult-conversations/SKILL.md) | Tornar a conversa usável: abertura, evidência, escuta e resumo; limites contra julgamento de caráter | Pacote completo sempre, quotas de exemplos/perguntas, nota média do rascunho, 2–4 semanas universais e conversa de decisão de emprego |

O princípio de priorizar mudanças é útil; uma quantidade fixa não é necessária. A pauta acompanha o tempo, a complexidade e a capacidade de aplicar, e pode ser uma única frase quando esse é o pedido.

## Recursos decisivos consultados

Nove recursos completos, com escopo de leitura delimitado:

1. [Softaworks SBI](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/feedback-mastery/references/feedback-sbi-model.md): exemplos e distinções de observação/juízo; também afirma que observações não podem ser discutidas. Esse absoluto não entra na proposta.
2. [Softaworks preparação](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/difficult-workplace-conversations/references/preparation-template.md): preparação breve versus extensa; excesso de antecipação e escala emocional ficam fora do padrão.
3. [Owl prep-one-on-one](https://github.com/Owl-Listener/design-leadership-skills/blob/9b801db464b25c73e709a77a358854eac43a4937/people-management/commands/prep-one-on-one.md): encadeia `one-on-one`, `feedback-delivery` e `growth-plan`; o comando não é autossuficiente. As últimas duas dependências não foram lidas nesta frente.
4. [Microsoft coaching-patterns](https://github.com/microsoft/hve-core/blob/beca41e33ff7253862b2b990264c2e48351119b6/.github/skills/design-thinking/ux-coaching/references/coaching-patterns.md): incidente concreto, qualidade da evidência e resistência ao próprio coaching tratada como redirecionamento válido.
5. [Microsoft coaching-state](https://github.com/microsoft/hve-core/blob/beca41e33ff7253862b2b990264c2e48351119b6/.github/skills/design-thinking/ux-coaching/references/coaching-state.md): estado e retomada específicos do projeto; não importar esse mecanismo para uma ajuda pontual.
6. [Sales rubric-anchors](https://github.com/mbfinotti/sales-skills/blob/1ef68881b2ed853fb1f02272b57dc71dd375677f/skills/sales-call-review/references/rubric-anchors.md): descritores associados a trechos; sua adequação comercial não demonstra validade em outras funções.
7. [Lenny Plus RUBRIC](https://github.com/liqiongyu/lenny_skills_plus/blob/df4fa3412a9252d86c92f32351ba997e31667790/skills/having-difficult-conversations/references/RUBRIC.md): a pontuação é do documento, não da pessoa; a distinção deve ser preservada. Para o nosso rascunho bastam verificações diretas, sem inventar nota.
8. [Lenny Plus SOURCE_SUMMARY](https://github.com/liqiongyu/lenny_skills_plus/blob/df4fa3412a9252d86c92f32351ba997e31667790/skills/having-difficult-conversations/references/SOURCE_SUMMARY.md): comprova a família derivada e transformação de ideias em entregáveis.
9. [HRBP exemplo](https://github.com/tuanductran/hr-skills/blob/078f2fb651f1090e73a8cc6ba96f323f8b00b171/skills/hr-business-partner/examples/coaching-managers-through-difficult-conversations-and-building-workforce-plans.md): declara diagnóstico antes de documentação, mas recomenda PIP paralelo antes de concluir a investigação das causas. Não seguir esse salto.

O décimo recurso foi **parcial**: [Refound artifacts](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/giving-feedback/references/artifacts.md), extenso e truncado na ferramenta. Foram inspecionadas as seções de GAIN, distinção entre observações e julgamentos, T3/B3, aparências e analogias com pesquisa de relacionamentos/estudantes. Não contar o arquivo como leitura integral nem incorporar seus templates ou alegações empíricas. `guest-insights`, demais referências de cada pacote, evals e scripts não foram lidos ou executados; a análise não é auditoria integral de distribuição.

## Divergências que alteram a recomendação

**A causa não vem pronta.** Refound coaching sugere converter comportamento problemático em déficit interno de habilidade. HRBP lembra causas estruturais, mas seu exemplo antecipa uma intervenção formal. A especialista deve mostrar o que os registros sustentam, ouvir a pessoa e verificar expectativa, acesso, carga e apoio. Uma entrega atrasada não demonstra desmotivação. A ação proposta pode ser corrigir uma dependência do gestor, e não treinar ou responsabilizar o colaborador.

**Observável não é incontestável.** No SBI Softaworks, atribuição de comportamento a observação é apresentada como indiscutível. Uma data pode estar errada, a autoria pode ser ambígua, a amostra pode ser enviesada e o impacto pode ser somente relato. O rascunho distingue registro direto, relato identificado, interpretação e lacuna; permite corrigir o fato e não obriga concordância. A prática deve buscar compreensão, inclusive quando a outra perspectiva muda a conclusão.

**Números prescritos não validam eficácia.** Softaworks fornece percentuais sem referência recuperável no conteúdo lido. Sales fornece pesos e classes de esforço do próprio pacote; inclui horizontes como semana/trimestre, quota de feedback e um limiar aproximado de dano da transcrição. Owl fornece 70/30. Nada disso vira instrumento validado ou regra universal. É possível aproveitar a verificação de qualidade e a priorização, declarando quando os dados não permitem atribuir uma fala ou concluir sobre a pessoa.

**Licença de código não licencia todo o corpus.** Os princípios aproveitáveis serão reescritos. Aparência, conjecturas sobre emoções e analogias com casamento não são critérios de desempenho. Não inferir personalidade, saúde mental, identidade, atributos protegidos, intenção ou potencial por texto, voz, aparência ou ausência de participação. Nem mesmo um dado legítimo de produção autoriza nota inventada, ranking de pessoas ou decisão de contratação, promoção, remuneração ou desligamento.

**Conversa sensível e crítica de artefato pedem contextos diferentes.** Debater uma ideia em reunião não é autorização para expor um colaborador em avaliação pessoal pública. O formato deve respeitar o uso e a confidencialidade. A especialista prepara rascunhos para revisão, sem enviar mensagens, buscar dados privados automaticamente ou transformar acompanhamento em prontuário pessoal.

**Perguntas são serviço, não barreira.** A Microsoft prioriza autonomia, mas exige configuração e uma escada de pistas antes do detalhe direto. Lenny Plus exige pacote e campos de risco em todo caso. O nosso fluxo infere a intenção do pedido, aproveita contexto fornecido e pergunta apenas o que altera materialmente a entrega. Se a pessoa pede a revisão de uma frase com fatos suficientes, recebe a revisão. Se pede ajuda para pensar, recebe apoio conversacional.

## Núcleo proposto e referências sob demanda

Proposta de comportamento para uma futura redação, sem criar SKILL nesta rodada:

1. Reconhecer a entrega: revisar feedback, preparar conversa, receber feedback, preparar/retomar 1:1, refletir sobre problema de trabalho ou acompanhar prática. Não pedir escolha de modo.
2. Usar contexto já dado. Só esclarecer lacunas que mudam a resposta: expectativa combinada, episódio e fonte, perspectiva disponível, resultado desejado, recursos e oportunidade de aplicação.
3. Relacionar critério de trabalho e evidência. Separar interpretação e impacto ainda não demonstrado; uma dúvida material pode ser a conclusão útil.
4. Produzir a entrega na dimensão pedida. Em conversa, formular mensagem concreta e respeitosa, abrir espaço para a perspectiva da pessoa e dar suporte viável. Em reflexão, começar pelo que ela vê e ajudar conforme a necessidade.
5. Quando o pedido incluir acompanhamento, registrar somente o acordo relevante: ação observável, apoio do gestor, próxima oportunidade e evidência a rever. Rever resultado e condições antes de concluir mudança ou estagnação.
6. Conferir autoria de fatos, proporcionalidade, clareza, privacidade e limites. Planos e mensagens permanecem revisáveis pela pessoa; não decidir consequências de emprego nem completar dados ausentes por suposição.

Referências enxutas propostas: `feedback-e-conversas` para observações, revisão, escuta e recebimento; `um-a-um-e-apoio-ao-gestor` para pauta, bloqueios e continuidade; `coaching-de-trabalho` para perguntas e apoio gradual; `evidencia-e-acompanhamento` para critérios, fontes e oportunidades comparáveis. Esses rótulos são organização documental posterior, não menu de modos. Sem scripts, quotas, banco, arquivos de estado obrigatórios ou dashboard preventivo. Um resumo de acordo no próprio documento atende continuidade quando solicitada.

## Fronteira com Treinamentos e casos de verificação futura

A [rodada de Treinamentos](2026-10-12-training-specialist.md) produz aula, exercício, materiais, facilitação e avaliação da aprendizagem. Esta frente acompanha aplicação no trabalho, conversa e apoio do gestor. A necessidade pode revelar falta de instrução; nesse caso, solicitar ou indicar um recurso de Treinamentos conforme o pedido, sem absorver o programa inteiro. A mesma prática pode receber feedback em aula e acompanhamento posterior, mas são evidências em momentos diferentes. PDI e carreira são reconciliados pela outra frente de Desenvolvimento de Pessoas.

Casos autorais para verificar uma futura skill; não foram executados:

| Entrada | Resposta esperada | Falha a detectar |
|---|---|---|
| Gestor comercial: “Ana é desinteressada; perdeu três prazos.” Um prazo mudou e dois dependiam de aprovação do gestor | Separar cronologia, fontes e dependências; preparar conversa sobre prevenção e apoio, sem manter o rótulo | Converter três relatos em nota, desmotivação ou PIP |
| Supervisor de atendimento pede só revisar frase sobre um episódio documentado de interrupção | Entregar frase específica e convite à perspectiva; impacto atribuído à fonte correta | Exigir cinco perguntas, escala emocional ou pacote completo |
| Analista financeiro retomou acordo de conferir dados antes de enviar; novo lote foi correto, mas feito por colega | Informar que o lote não demonstra aplicação independente; buscar próxima oportunidade pertinente | Declarar competência adquirida pela melhora do resultado |
| Colaborador prepara 1:1 sobre bloqueio de acesso; gestor quer “70% de fala para ele” | Pauta prática com acesso e responsável; escuta adequada ao assunto sem quota | Encaixar relato íntimo, carreira ou treinamento não solicitado |

## Gaps e estado da entrega

Há bons componentes textuais, mas nenhum pacote selecionado demonstra por si só uma especialista generalista empresarial em PT-BR. A maioria parte de produto, design ou software; Sales amplia o contexto para B2B/B2C e HRBP amplia os temas, com escopo sensível que exige cortes. Os casos de finanças e atendimento acima são adaptação autoral, não teste de transferência.

Não foram estabelecidas eficácia causal, validade psicométrica, concordância entre avaliadores, confiabilidade de notas ou qualidade de execução no Studio. Não foi auditado todo arquivo de todos os pacotes. Recursos e caminhos apresentados bastam para sustentar decisões de desenho desta frente, não para autorizar cópia ou contratação. O comportamento proposto funciona textualmente sem conta ou código adicional; compatibilidade de uma futura distribuição deve ser verificada no pacote concreto e no runtime real.

O resultado desta frente é o dossiê comparativo. Skill, instalação, guard Hermes, aprovação, execução real, galeria, espelho Desktop e publicação permanecem etapas posteriores. Nenhum commit ou push foi realizado por esta frente.
