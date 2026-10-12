# Gerente de Projetos — skills de planejamento, escopo e cronograma

Pesquisa em 12/10/2026, para uso interno em projetos de negócios. Este documento cobre transformar objetivo em entregas, delimitar escopo, decompor trabalho, estimar, mapear dependências, conciliar capacidade e produzir um plano utilizável. A análise de métodos profissionais e a de acompanhamento/riscos ficam nas outras frentes. Referências a riscos aqui só entram quando interferem diretamente na estimativa ou na sequência.

**Recomendação:** construir posteriormente uma síntese própria curta, com reconhecimento automático do pedido e referências sob demanda. O melhor material operacional encontrado é `JayRHa/AgentSkills/project-planner`; o pacote `gao-schedule` corrige limitações importantes desse planejamento ao explicar capacidade, calendários e validade do caminho crítico. `business-plan-skills/13-implementation-timeline` acrescenta dependências de negócio reais: aquisição, liberação de verba, instalações e aceite. Nenhum deles deve ser importado inteiro como comportamento padrão.

Esta é pesquisa autoral, não uma skill implementada. Nenhum pacote foi instalado, nenhum script externo executado, nenhum arquivo de terceiro copiado para o repositório. As leituras ocorreram por GitHub API e conteúdo raw, sem clones ou temporários. Não houve acesso a contas, publicação ou envio de mensagens externas.

## Alcance, seleção e contagem

A descoberta combinou buscas por `project-manager`, `project-planner`, `work breakdown`, `implementation-timeline` e `gantt` em inglês, páginas do [skills.sh](https://skills.sh/) e repositórios originais. Instalações e estrelas serviram apenas para descobrir candidatos; não são critérios de qualidade ou evidência de funcionamento.

Foram analisadas **7 famílias com SKILL.md integral**, das quais **5 contribuem para planejamento** e **2 servem sobretudo como contraponto**. Foram lidos integralmente **30 arquivos externos distintos**, incluindo as 7 skills, recursos selecionados e textos de licença; **2 arquivos adicionais tiveram leitura parcial**. As listas abaixo discriminam os arquivos. Consultas de metadata/API, páginas de descoberta e repetições de leitura não entram nessa contagem.

As 7 famílias têm a seguinte distribuição de licenças observadas: **5 MIT em seus repositórios**, **1 pacote de conteúdo declarado domínio público dos EUA, com tooling MIT separado**, e **1 skill que declara Apache-2.0 dentro de um repositório identificado como AGPL-3.0**. Esta última exige investigação de proveniência antes de redistribuir conteúdo. Não se conclui incompatibilidade automática: uma licença específica pode reger uma parte do repositório, mas autoria e avisos precisam estar claros.

Foi encontrada uma duplicação interna no Wayland: a skill da biblioteca e a cópia de runtime compartilham corpo e metadata, com diferenças de formatação. Contam como **uma família**, não como duas evidências independentes. Não foi comprovada relação de cópia entre as demais famílias; ter o mesmo nome não basta para afirmar independência de autoria nem plágio.

| Família | Papel na comparação | Autor/origem observada | Snapshot do repositório consultado | Última alteração do SKILL no snapshot |
|---|---|---|---|---|
| [JayRHa / project-planner](https://github.com/JayRHa/AgentSkills/blob/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/project-planner/SKILL.md) | Base operacional mais completa | Copyright Jannik Reinhard; repositório JayRHa | `7ce3d8d6af7ca3905c688c649000b98e8e57db4a`, 28/07/2026 | 13/06/2026 |
| [takusaotome / project-manager](https://github.com/takusaotome/claude-skills-library/blob/b542ac73ab54a40299a9f407b0ebdb425d107e96/skills/project-manager/SKILL.md) | Revisão de plano e requisitos | Claude Skills Library Contributors | `b542ac73ab54a40299a9f407b0ebdb425d107e96`, 05/10/2026 | 30/12/2025 |
| [Peter Bamuhigire / 13-implementation-timeline](https://github.com/peterbamuhigire/business-plan-skills/blob/d3d5013744b8a668e21647e45161c1c7f80fdc3d/skills/pipeline/13-implementation-timeline/SKILL.md) | Sequência de negócio e gates materiais | Peter Bamuhigire | `d3d5013744b8a668e21647e45161c1c7f80fdc3d`, 29/09/2026 | 29/09/2026 |
| [Wayland / project-manager](https://github.com/FerroxLabs/wayland/blob/4c030c7b01c241df7b6e3535635a970f10d781af/src/process/resources/skills-library/bodies/agents/business/project-manager/SKILL.md) | Coordenação e trade-offs | Metadata `foundry-skills`; distribuição FerroxLabs | `4c030c7b01c241df7b6e3535635a970f10d781af`, 22/09/2026 | 07/06/2026 |
| [JG Systems Consulting / gao-schedule](https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/blob/9e9554be701c807a14240b50bd7601ba3b13eb9b/packs/gao-schedule/SKILL.md) | Qualidade técnica do cronograma | Síntese JG Systems Consulting de GAO-16-89G, dezembro/2015 | `9e9554be701c807a14240b50bd7601ba3b13eb9b`, 08/10/2026 | 24/06/2026 |
| [InBharat / project-planner](https://github.com/inbharatai/claude-skills/blob/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/project-planner/SKILL.md) | Contraponto: descrição ampla sem método | Frontmatter `author: Claude Code`; copyright InBharat AI | `02077f8b2c05946a71fa087dee6d614c0b4e4e0d`, 14/03/2026 | 14/03/2026 |
| [i-onlabs / timeline-creator](https://github.com/i-onlabs/claude-code-skills/blob/28ec3ee7284f2d26a133917ceb2faf28318b2adb/timeline-creator/SKILL.md) | Contraponto: visualização sem modelo de planejamento | Copyright Claude Code Enhanced Agents & Skills; distribuição i-onlabs | `28ec3ee7284f2d26a133917ceb2faf28318b2adb`, 26/04/2026 | 21/12/2025 |

Datas do snapshot são do commit do repositório; datas da última alteração são de consultas ao histórico do caminho do SKILL nesse snapshot. Não representam data de publicação da skill ou data de revisão profissional.

### Descobertas excluídas ou preliminares

- [shubhamsaboo/awesome-llm-apps/project-planner no skills.sh](https://www.skills.sh/shubhamsaboo/awesome-llm-apps/project-planner): descoberta relevante pela procura e pelo texto exibido, mas o caminho original não foi localizado na árvore completa do snapshot `4bf51ab704fb2c5b3803cd5191b30d7dcdb51dc2` (29/09/2026), cuja API informou `truncated: false`. A consulta de histórico ao caminho presumido `agent_skills/project-planner/SKILL.md` também não retornou commits. Pode haver caminho histórico diferente ou desalinhamento do diretório. **Não conta como skill original lida, nem como pacote auditado.**
- [hieutrtr/ai1-skills/project-planner](https://www.skills.sh/hieutrtr/ai1-skills/project-planner) e [task-decomposition](https://www.skills.sh/hieutrtr/ai1-skills/task-decomposition): as páginas mostram foco Python/React, módulos, arquivos e implementação de software. Não foram aprofundadas: o caso de destino inclui iniciativas administrativas, instalações, eventos e mudanças operacionais.
- [GitHub awesome-copilot / breakdown-plan](https://github.com/github/awesome-copilot/blob/main/skills/breakdown-plan/SKILL.md): descoberta de hierarquia e dependências, porém orientada a artifacts de software, issues GitHub e automação de criação. Não foi considerada evidência integral nesta frente.
- [openai/plugins / gantt-chart-visualization](https://www.skills.sh/openai/plugins/gantt-chart-visualization): descoberta útil para a diferença entre gráfico e planejamento, mas construir uma superfície interativa de Gantt excede o pedido de uma especialista de negócios. Não foi auditada integralmente nesta frente.

## Comparação por componentes

### 1. JayRHa: plano derivado de entregas, com suporte real e script limitado

O pacote contém uma instrução operacional, quatro referências curtas, template, exemplo de lançamento e calculador CPM. É a alternativa com melhor ligação entre contexto, decomposição e saída utilizável. Define marcos de duração zero, diferencia esforço de duração e explicita dependências obrigatórias, preferenciais e externas. O exemplo é de website, mas os componentes gerais se aplicam a negócios.

| Fonte/arquivo | Contribuição | Decisão para a futura skill | Motivo |
|---|---|---|---|
| `SKILL.md` + `references/clarifying-questions.md` | Resultado esperado, limite de prazo, capacidade, terceiros e exclusões; perguntar só o que falta | **Adaptar** | Aproveitar a leitura de materiais existentes e evitar entrevista obrigatória; perguntar quando a lacuna muda o plano |
| `references/wbs-method.md` | Cobertura do escopo sem sobreposição; distinguir entregas de atividades | **Aproveitar conceito; adaptar execução** | A regra de cobertura ajuda a não esquecer aceite, aquisição ou treinamento. A regra fixa 8–80 horas e agrupamento em cerca de 7 itens não devem obrigar toda iniciativa |
| `references/estimation.md` | Esforço versus duração, disponibilidade parcial, limites da adição de pessoas, histórico como base | **Aproveitar** | Combate planos que dividem horas por pessoas sem verificar se o trabalho admite divisão |
| `references/estimation.md` | PERT para todo trabalho não trivial; reserva padrão de 15–30%; confiança aproximada de 90% | **Adaptar ou descartar automatismo** | Faixas e bases de estimativa ajudam. Percentuais e probabilidades universais geram precisão artificial sem distribuições, correlações e riscos do caso |
| `references/dependencies-and-critical-path.md` | Predecessores, tipos de vínculo, folga, recomputação | **Adaptar** | Começar pela relação em palavras; usar FS/SS/FF e cálculos quando agregarem valor ao pedido |
| `templates/project-plan.md` | Documento com objetivo, escopo, pressupostos, responsáveis, marcos e dependências | **Adaptar** | Uma tabela curta pode bastar; não gerar todas as 9 seções para qualquer pergunta |
| `examples/website-launch.md` | Exemplo de dependência jurídica externa e marco condicionado a trabalho | **Aproveitar didática; não reproduzir estimativas** | As durações são ilustrativas; o exemplo não demonstra validação real de capacidade ou execução de um projeto |
| `scripts/critical_path.py` | Cálculo determinístico de ES/EF/LS/LF e folga, só FS | **Descartar como script pronto; estudar a lógica** | Há erros de representação e lacunas de validação descritos adiante; não resolve calendário nem alocação |

O texto manda seguir todas as etapas e não pular esclarecimentos. A referência de perguntas, por sua vez, permite pressupostos declarados. A adaptação deve resolver essa tensão: avançar sobre o que já é conhecido e pedir apenas a informação necessária à próxima decisão.

### 2. GAO: confiabilidade da sequência e viabilidade da capacidade

O pacote é uma base de conhecimento sem scripts. A autoria da transformação é JG Systems Consulting; a autoridade profissional indicada é o relatório governamental **GAO-16-89G, dezembro de 2015**. Não é uma certificação da skill pelo GAO. O guia oficial e atualizações de metodologia devem ser conferidos na frente profissional antes de qualquer afirmação normativa.

| Fonte/arquivo | Contribuição | Decisão | Motivo |
|---|---|---|---|
| `SKILL.md` | Cronograma completo, bem construído, crível e controlado | **Adaptar** | Usar como critérios de revisão em linguagem de trabalho; não impor um IMS governamental a uma iniciativa pequena |
| `chapters/ch02-...md` | Todas as partes necessárias, incluindo fornecedores, aprovações e aceite; vínculos com entregas | **Aproveitar** | Torna visíveis trabalhos que não estão na equipe principal e impede datas sem antecessores reais |
| `chapters/ch02-...md` | Distinguir marco, atividade e agrupamento; minimizar datas forçadas e esperas escondidas | **Aproveitar** | Um marco de “contrato assinado” não substitui preparar, negociar e aprovar o contrato |
| `chapters/ch03-...md` | Recursos incluem pessoas, equipamento, material, local e verba; produtividade, disponibilidade e calendário afetam duração | **Aproveitar** | É a principal correção ao CPM simplificado e atende negócios além de software |
| `chapters/ch03-...md` | Detalhar o próximo trabalho; manter futuro em pacotes mais amplos | **Adaptar** | O grau de detalhe segue conhecimento e decisão. Não inventar tarefas semanais de um ano inteiro |
| `chapters/ch03-...md` | Nivelar recursos; datas desejadas não justificam durações menores | **Aproveitar** | Um especialista necessário em dois projetos ao mesmo tempo exige escolha de capacidade ou sequência |
| `chapters/ch04-...md` | Continuidade de caminho crítico; reconciliar detalhe e resumo; múltiplos caminhos e efeito de calendários | **Aproveitar sob demanda** | “Lista de tarefas importantes” não comprova qual sequência determina a entrega |
| `SKILL.md` e capítulos | Monte Carlo, S-curves, IMS, EVM e aparato de auditoria | **Descartar do núcleo; avaliar referência específica** | Complexidade só justificada por cronograma e dados que demandem essa análise; nenhuma simulação foi feita nesta pesquisa |

A diferença decisiva: **CPM calcula a duração mínima da rede lógica sob suas hipóteses; um compromisso de calendário exige validar recursos e calendário.** Mostrar as duas coisas separadas evita que uma tabela aritmeticamente coerente se torne uma promessa impossível.

### 3. Business-plan-skills: sequência operacional concreta, com contexto regional forte

A skill integra uma pipeline de plano de negócios, com seções vizinhas e vocabulário de financiadores. A contribuição relevante é tratar aquisição e verba como predecessores, e implantação física/operacional como continuidade de serviço. Ela é mais ampla que software, mas não portátil inteira: mistura conteúdo de Uganda, outros pacotes e regras de liberação.

| Fonte/arquivo | Contribuição | Decisão | Motivo |
|---|---|---|---|
| `SKILL.md` | Plano sequenciado com dono, critérios e recursos; atividade sem entrada conhecida pode ficar sem data ou em faixa | **Aproveitar** | Permite entrega parcial honesta, em vez de calendário com dias inventados |
| `references/scope-deliverables-and-change-control.md` | Separar objetivo, escopo, entrega e critério de aceite; charter leve | **Aproveitar a distinção; redigir síntese própria** | Exemplos como instalação de câmara fria ajudam a testar transferência para negócios |
| `references/procurement-and-gating-schedule.md` | Assinatura do contrato e liberação de recursos são dependências diferentes | **Adaptar** | Evita iniciar compra, instalação ou contratação antes da condição material necessária; não transportar legislação ou prazos regionais |
| `references/facility-change-continuity-and-cutover.md` | Readiness, continuidade, go/no-go, estabilização e fechamento | **Adaptar sob demanda** | Útil para mudança de escritório, evento, transição de fornecedor ou nova unidade com serviço ativo |
| `SKILL.md` | Fases fixas fundação/lançamento/crescimento/escala e plano de 90 dias obrigatório | **Descartar como padrão** | Um projeto de evento ou renegociação contratual não segue automaticamente um ciclo de startup |
| `SKILL.md` | Handoffs, release records, doutrina financeira e referências que saem da pasta | **Descartar do pacote mínimo** | O valor é a reconciliação de pressupostos; não depende de importar toda a pipeline ou bloquear toda conversa em intake |

Os próprios recursos reconhecem necessidade de confirmar fontes e jurisdição. A referência de escopo pede confirmar autor/editor do livro citado; a de continuidade aponta um playbook sem identificação bibliográfica suficiente. Não atribuir tais métodos a autoridade verificável antes dessa checagem. A síntese pode usar distinções profissionais gerais e fontes primárias confirmadas pela outra frente, sem copiar essas notas.

### 4. Takusaotome: revisão ampla, mas checklist pesado e viesado para TI

O SKILL tem cinco workflows e mais de mil linhas; mistura requisitos, plano, progresso, riscos e custos. O template de requisitos tem 14 seções, matrizes, assinaturas, NFRs, APIs e implantação. Isso oferece repertório para pedidos formais de implantação empresarial, mas custa contexto e exige abstrair o que serve para projetos administrativos.

| Fonte/arquivo | Contribuição | Decisão | Motivo |
|---|---|---|---|
| `SKILL.md`, workflows 1–2 | Problema de negócio, objetivo, escopo/exclusões, critérios de aceite, capacidade, dependências | **Aproveitar perguntas de revisão** | São verificações transferíveis a uma contratação ou mudança operacional |
| `assets/requirements_definition_template.md` | Requisito ligado a objetivo, origem e verificação; pressupostos e restrições visíveis | **Adaptar** | Em negócios, substituir ligação design/teste por entrega/evidência de aceite quando for mais adequado |
| Mesmo template | APIs, dados, segurança, testes e WBS por ciclo de desenvolvimento | **Descartar do padrão geral** | Não obrigar formato de engenharia de requisitos de software em todos os projetos |
| `SKILL.md` | MoSCoW rigoroso, CCB universal, sponsor C-level, testing de 20–30%, contingência de 10–20% | **Descartar automatismos** | Regra de governança e proporção dependem do contexto, autoridade e criticidade reais |
| `SKILL.md` | Alternativas diante de prazo inviável: escopo, capacidade, sequência ou prazo | **Aproveitar** | Uma proposta comparável ajuda a pessoa responsável a decidir; o agente não altera equipe ou compromisso sozinho |
| `SKILL.md` | Exemplos de resultados numéricos de CRM e migração | **Não contar como case comprovado** | O documento não fornece evidência externa de execução para esses números |

Não se confirmou conformidade com ISO/IEC/IEEE 29148, PMBOK ou AACE apenas porque o autor a declara. A seção de referência PMBOK foi inspecionada parcialmente e não entra na contagem de arquivos integrais. O script de saúde, referências de risco e templates de progresso não foram auditados nesta frente.

### 5. Wayland: coordenar capacidade e mudanças, sem inventar credenciais

| Fonte/arquivo | Contribuição | Decisão | Motivo |
|---|---|---|---|
| `SKILL.md`, responsabilidades/processo | Marcos com significado, responsáveis, capacidade, dependências e trade-offs | **Adaptar** | Boa cobertura da função, mas saída principal é relatório de status, não um template de planejamento detalhado |
| Regras 6, 8 e 9 | Diferenciar trabalho terminado de aceito; cronograma coerente; validar prazo com executores | **Aproveitar** | Impede declarar uma entrega apenas por o agente ter escrito um plano |
| Edge cases | Reconhecer projeto herdado, time distribuído e prioridades conflitantes | **Adaptar** | Aproveitar contexto e indicar decisão pendente; não impor standups ou dashboard antes de entender a dor |
| Persona | PMP/CSM, 14 anos e carteira acima de US$50M | **Descartar** | Credenciais e experiência atribuídas à persona não são evidência nem qualificação real do agente |
| Process/tool restrictions | Horas/story points, tarefas 1–5 dias, proibição categórica de shell | **Adaptar ou descartar** | A granularidade segue o pedido; uma ferramenta local de cálculo pode ter ganho concreto, sem autorizar implementação, envio ou operação externa |
| Autoria/licença | `foundry-skills`, Apache-2.0 no frontmatter, repositório AGPL-3.0 | **Usar conhecimento; adiar cópia** | Proveniência e avisos de distribuição precisam ser reconciliados antes de reutilizar expressão textual |

### 6. Contrapontos: promessa de planner e promessa de Gantt

**InBharat:** o SKILL é curto e tem licença MIT no repositório, mas as instruções dizem entender contexto e produzir resultado profissional sem explicar decomposição, estimativa, dependência ou revisão. Exemplos de “setup production-ready” são genéricos. **Descartar como fonte de método**. Uma descrição que promete WBS/Gantt não equivale a capacidade operacional demonstrada.

**i-onlabs timeline-creator:** o SKILL extrai tarefas/datas, calcula porcentagem de duração e desenha barras HTML. Não ensina como descobrir trabalho, justificar datas, sequenciar, detectar conflito de capacidade ou validar o fim. A referência de design é genérica e não fornece algoritmo de cronograma. **Aproveitar apenas a ideia de visualização sob demanda; descartar como motor de planejamento.** Templates HTML e biblioteca SVG não foram lidos, e não há validação de render nesta pesquisa.

## Defeitos e limites encontrados por leitura estática

1. **JayRHa, `scripts/critical_path.py`, `critical_chain`:** filtra todos os nós críticos em ordem topológica. `print_table` os une com setas, e a saída JSON também usa essa lista como `critical_path`. Isso não recupera caminhos contínuos. Contraexemplo deduzido, sem executar: A e B independentes, duração 2 cada, ambos precedendo C de duração 1. Todos têm folga zero, mas a sequência exibida A → B → C inventa A → B; os caminhos são A → C e B → C. A aritmética de folga pode estar correta enquanto a representação da sequência está errada.
2. **Mesmo script, `load_tasks`:** converte duração com `float` sem rejeitar valores negativos ou não finitos. Também arredonda a folga a 6 casas antes de comparar a criticidade a `1e-9`; isso limita a precisão do critério para entradas fracionárias pequenas. São lacunas estáticas, não teste runtime.
3. **Mesmo pacote:** a documentação ensina SS/FF/SF e lead/lag, mas o script modela só FS. Não há campos de recurso, calendário ou disponibilidade. Manualmente somar lead/lag não substitui um algoritmo que respeite vínculos diferentes. Uma futura calculadora precisa declarar exatamente seu modelo; não apresentar suporte geral a tudo que a referência descreve.
4. **JayRHa, `examples/website-launch.md`:** as atividades `hosting`, `form` e `pages` podem se sobrepor na rede; o contexto informa apenas um desenvolvedor. O exemplo não verifica alocação nem traduz disponibilidade parcial do designer e redator consistentemente em calendário. O resultado “12 dias” é um resultado ilustrativo da rede, não prazo de equipe comprovado.
5. **Takusaotome, `SKILL.md`, validação de estimativa:** o exemplo diz benchmark de ¥5.000–¥15.000 por usuário e depois aceita ¥101.200 por usuário como razoável. A comparação não sustenta o veredito. Percentis P10/P50/P90 e precisão ±10% aparecem sem uma análise reproduzível que os gere.
6. **Takusaotome, mesmo SKILL:** SPI de valor agregado é interpretado como porcentagem de atraso de calendário. O índice compara trabalho realizado e planejado em valor; isoladamente não determina quantos dias o projeto atrasará. Não usar a frase “17% atrasado” como previsão de data final.
7. **Business-plan-skills, `SKILL.md`:** a fórmula de PERT perde o operador de divisão antes do 6; aparecem textos `Week 14` e `714 days` em contexto que sugere perda de hífens. Isso torna calendário/formula ambíguos, e não deve ser corrigido por adivinhação em plano real. A ausência de divisor é verificável; a intenção de faixas 1–4 e 7–14 é hipótese editorial.
8. **Timeline-creator, `SKILL.md`:** a barra tem largura percentual de duração, porém o exemplo não codifica deslocamento pelo início. Sem posicionar a barra no eixo temporal, duas tarefas de mesma duração mas datas distintas aparecem iguais. É um molde de barra, não Gantt comprovado. Nenhuma alegação de interatividade foi validada.

Esses achados orientam seleção e futura validação. Não foram feitas correções nos repositórios de terceiros.

## Proposta de organização aplicável ao destino

### Núcleo curto

Reconhecer o que a pessoa está tentando fazer: começar um projeto, transformar materiais em plano, revisar uma sequência, estimar um prazo ou replanejar diante de uma mudança. Não exigir nomes de modos ou rituais. Ler o material disponível e preservar decisões fechadas. Identificar o resultado, entregas aceitas, limites de escopo, prazo desejado ou obrigatório, capacidade e dependências que mudam o plano. Fazer a próxima pergunta quando a resposta altera uma decisão material.

Entregar o menor artefato que sustenta o pedido: plano em Markdown, tabela editável ou revisão do plano existente. Cada linha de trabalho relevante deve permitir entender o resultado, responsável ou papel proposto, predecessores, estimativa/base e critério de aceite. Nem todo pedido exige arquivo novo; o formato pedido e o material existente prevalecem.

Antes de atribuir datas, conferir capacidade compartilhada, horas realmente disponíveis, dias úteis, indisponibilidades, espera por terceiros e condições de financiamento/contratação. Separar dado confirmado, proposta e pressuposto. Se faltar duração ou capacidade decisiva, mostrar intervalo ou marco sem data e explicar o que falta para fechar a previsão.

Quando o plano não cabe na restrição, comparar poucas alternativas concretas: reduzir/deferir entregas, mudar sequência, obter capacidade viável ou ajustar prazo. Dizer quais compromissos dependem de decisão humana. Produzir um plano não autoriza atribuir tarefas no sistema de terceiros, comprar, contratar, mandar convites ou mudar operação.

### Referências carregadas pelo pedido

| Recurso futuro possível | Carregar quando | Conteúdo que se justifica |
|---|---|---|
| Escopo e entregas | Objetivo difuso, múltiplos interessados ou revisão de escopo | Inclusões/exclusões, decomposição por resultado, evidência de aceite; síntese autoral de JayRHa, GAO e planejamento operacional |
| Estimativa e capacidade | Pedido de prazo/esforço, equipe parcial ou recursos compartilhados | Esforço/duração/espera, histórico, calendário, intervalos, gargalos; sem porcentagem universal |
| Dependências e cronograma | Vários trabalhos condicionados, prazo apertado ou análise de atraso | Relações reais, rede sem ciclos, caminho contínuo, folga e limite do modelo; referências GAO sob demanda |
| Implantação operacional | Mudança de unidade, fornecedor, serviço ou instalação | Aquisição e verba, acesso, continuidade, treinamento, go/no-go e estabilização; sem regras de Uganda por padrão |
| Plano ou revisão formal | Sponsor pede documento completo ou projeto exige rastreabilidade | Template proporcional, bases das estimativas, responsáveis propostos e critérios verificáveis; sem importar as 14 seções de requisitos de software |

Essa tabela é uma recomendação de conteúdo; não uma exigência de criar cinco arquivos ou menus. Os recursos podem ser combinados onde isso reduzir duplicação. Bibliografia, histórico, candidatos descartados e comparações de licença permanecem neste dossiê, fora do pacote executável.

### Scripts: decisão restrita a ganho concreto

Não há razão demonstrada para incluir scripts no núcleo inicial apenas porque JayRHa possui um. Cálculo local passa a fazer sentido quando a quantidade de tarefas, alternativas ou recomputações aumenta a chance de erro manual. Se surgir essa necessidade, usar uma implementação autoral pequena ou um componente licenciado auditado, com validação de IDs/durações/vínculos, detecção de ciclos e saída que represente caminhos reais. Declarar suporte a FS, calendários e recursos conforme o que foi implementado, sem promover CPM simples a otimizador de capacidade.

Critérios de aceitação futuros úteis: caminhos críticos paralelos; predecessor ausente; ciclo; duração zero/negativa/não finita; pessoa disputada por duas atividades; feriado; aprovação externa sem data; tarefa de duração fixa; mudança de entrega que desloca o marco final. São casos profissionais que discriminam um planejador útil de uma tabela convincente; não são testes executados nesta pesquisa.

## Manifesto de leitura e licenças

As bases abaixo são links fixados no snapshot. Os nomes de arquivos após cada base indicam a leitura integral; o caminho é relativo à base. Isso torna explícito o que foi realmente inspecionado sem redistribuir conteúdo de terceiros.

| Base fixada | Arquivos integrais | Quantidade |
|---|---|---:|
| [JayRHa/project-planner](https://github.com/JayRHa/AgentSkills/tree/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/project-planner) | `SKILL.md`; `references/clarifying-questions.md`; `references/wbs-method.md`; `references/estimation.md`; `references/dependencies-and-critical-path.md`; `scripts/critical_path.py`; `templates/project-plan.md`; `examples/website-launch.md` | 8 |
| [Licença JayRHa](https://github.com/JayRHa/AgentSkills/blob/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/LICENSE) | `LICENSE`, MIT, copyright Jannik Reinhard | 1 |
| [Takusaotome/project-manager](https://github.com/takusaotome/claude-skills-library/tree/b542ac73ab54a40299a9f407b0ebdb425d107e96/skills/project-manager) | `SKILL.md`; `assets/requirements_definition_template.md` | 2 |
| [Licença Takusaotome](https://github.com/takusaotome/claude-skills-library/blob/b542ac73ab54a40299a9f407b0ebdb425d107e96/LICENSE) | `LICENSE`, MIT, copyright Claude Skills Library Contributors | 1 |
| [Peter/implementation-timeline](https://github.com/peterbamuhigire/business-plan-skills/tree/d3d5013744b8a668e21647e45161c1c7f80fdc3d/skills/pipeline/13-implementation-timeline) | `SKILL.md`; `references/scope-deliverables-and-change-control.md`; `references/procurement-and-gating-schedule.md`; `references/facility-change-continuity-and-cutover.md` | 4 |
| [Licença Peter](https://github.com/peterbamuhigire/business-plan-skills/blob/d3d5013744b8a668e21647e45161c1c7f80fdc3d/LICENSE) | `LICENSE`, MIT, copyright Peter Bamuhigire | 1 |
| [GAO schedule pack](https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/tree/9e9554be701c807a14240b50bd7601ba3b13eb9b/packs/gao-schedule) | `SKILL.md`; `chapters/ch02-gao-schedule-capturing-and-sequencing-activities.md`; `chapters/ch03-gao-schedule-resources-and-durations.md`; `chapters/ch04-gao-schedule-traceability-and-critical-path.md`; `PACK.yaml`; `LICENSE` | 6 |
| [Licença do tooling JG](https://github.com/jgsystemsconsulting/jgs-se-knowledge-packs/blob/9e9554be701c807a14240b50bd7601ba3b13eb9b/LICENSE) | `LICENSE`, MIT restrito ao tooling/scaffolding; conteúdo dos packs licenciado separadamente | 1 |
| [Wayland/library project-manager](https://github.com/FerroxLabs/wayland/blob/4c030c7b01c241df7b6e3535635a970f10d781af/src/process/resources/skills-library/bodies/agents/business/project-manager/SKILL.md) | `SKILL.md` integral; Apache-2.0 declarado no frontmatter | 1 |
| [InBharat/project-planner](https://github.com/inbharatai/claude-skills/tree/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/skills/project-planner) e [licença](https://github.com/inbharatai/claude-skills/blob/02077f8b2c05946a71fa087dee6d614c0b4e4e0d/LICENSE) | `SKILL.md`; `LICENSE`, MIT, copyright InBharat AI | 2 |
| [i-onlabs/timeline-creator](https://github.com/i-onlabs/claude-code-skills/tree/28ec3ee7284f2d26a133917ceb2faf28318b2adb/timeline-creator) e [licença](https://github.com/i-onlabs/claude-code-skills/blob/28ec3ee7284f2d26a133917ceb2faf28318b2adb/LICENSE) | `SKILL.md`; `references/design_patterns.md`; `LICENSE`, MIT, copyright Claude Code Enhanced Agents & Skills | 3 |
| **Total integral** | 7 SKILL.md + 23 recursos/licenças | **30** |

Leitura adicional parcial: [Takusaotome `references/pmbok_knowledge_areas.md`](https://github.com/takusaotome/claude-skills-library/blob/b542ac73ab54a40299a9f407b0ebdb425d107e96/skills/project-manager/references/pmbok_knowledge_areas.md) e [Wayland cópia de runtime](https://github.com/FerroxLabs/wayland/blob/4c030c7b01c241df7b6e3535635a970f10d781af/src/process/resources/skills/project-manager/SKILL.md). Essas leituras não sustentam afirmação de auditoria integral desses dois arquivos. A identificação AGPL-3.0 do repositório Wayland veio da metadata de licença da GitHub API, não de revisão jurídica.

As licenças MIT exigem preservar avisos ao copiar conteúdo ou trechos substanciais. O pack GAO declara domínio público para o material governamental nos EUA e distingue possíveis elementos de terceiros; não transformar isso em parecer de domínio público global. O manifesto do pack diz ter sintetizado notas e evitado reproduzir figuras de terceiros. Não foi auditado o guia inteiro nem feita revisão jurídica dessa afirmação. A opção mais simples para o destino é síntese própria com fontes, mantendo documentação de proveniência se houver adaptação textual futura.

## Limites que permanecem

- A pesquisa não cobre todo o universo de skills ou todo projeto empresarial. A seleção favorece componentes úteis para planejamento geral e contrasta soluções operacionais, bases de conhecimento e promessas genéricas.
- Não houve ensaio de execução, benchmark de qualidade, teste de scripts, render de Gantt ou verificação de um projeto real com responsáveis. Exemplos publicados são exemplos documentais.
- Os recursos não selecionados de cada pacote não foram lidos integralmente. Bibliotecas PMBOK, materiais de risco, referências de SaaS, change management, doutrinas financeiras e links para outros repositórios continuam fora desta auditoria. Licença do repositório não prova automaticamente a origem de todo material referenciado.
- Um pacote estudado não está autorizado como origem `github` na galeria do Studio apenas por estar público. Os repositórios analisados fora da allowlist servem como referência para a futura skill própria; não editar `gallery.json` nem prometer contratação direta.
- O ganho de uma calculadora, a forma de entrega e a necessidade de referência formal devem ser demonstrados por pedidos reais. A pesquisa resolve o desenho de componentes, sem fechar a validação profissional, a implementação ou a instalação da futura Gerente de Projetos.
