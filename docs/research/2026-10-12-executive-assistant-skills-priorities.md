# Assistente Executivo — prioridades, acompanhamento e resumo para decisão

Pesquisa de 12/10/2026. Frente de skills existentes da rodada 24/33. Documento original em PT-BR; não cria pacote, instala dependências ou muda o catálogo.

## Recomendação

Combinar o método progressivo e sem dependência de `chief-of-staff-methodology` com a ancoragem das prioridades no contexto real de `chief-of-staff` e a checagem de duplicidade do acompanhamento de `todoist-due-drafts`. Adaptar os componentes, sem copiar os pacotes. A entrega inicial deve funcionar com conversa, notas e arquivos autorizados: plano diário ou semanal, resumo para decisão ou rascunho de cobrança interna conforme o pedido.

O resumo mostra o que precisa de decisão e a recomendação; o plano explicita compromisso, dependência, capacidade e prazo disponíveis. Urgência descreve consequência e tempo, importância descreve contribuição e obrigação. Uma data próxima não basta para tornar algo estratégico. Não impor quatro quadrantes, ritual diário, três prioridades exatas ou documento estratégico com formato obrigatório.

## Descoberta e alcance

Buscas públicas por `SKILL.md executive-assistant`, `chief-of-staff` e `executive-brief`. Diretórios e resultados serviram para descobrir; a avaliação usou os repositórios originais e arquivos completos. Seleção por diferenças materiais: prioridade ligada a objetivos, preparação de decisões, acompanhamento contextual e contraste com automação pessoal dependente de serviços.

Foram lidos cinco SKILL.md selecionados, mais `email-drafting/SKILL.md`, recurso decisivo do acompanhamento. Não houve execução dos pacotes, instalação, conta, convite, acesso a caixa ou agenda, envio ou monitor futuro. A metodologia local foi `skills/skill-manager/references/research.md`. Não há alegação de cobertura de toda a internet.

A API pública do GitHub respondeu com limite de requisições; a inspeção prosseguiu por raw público, `git ls-remote` somente para descobrir HEAD e página `.patch` para autoria/data. Sem clone, arquivos temporários ou credenciais. SHA identifica HEAD observado; a data abaixo é a do commit do repositório, não uma certificação da atualização específica de cada skill. A primeira leitura dos arquivos de Lightbulb, Magnus e Snarktank foi em `main`, imediatamente após descobrir HEAD; links abaixo fixam a revisão para rastreabilidade. Mgonto e referências complementares foram consultados também pelo SHA.

## Fontes selecionadas e proveniência

| Família / autoria visível | Revisão observada e data visível | Arquivos efetivamente lidos | Licença e limite |
|---|---|---|---|
| Lightbulb Moment Labs / Kevin Fremon | `e8773e786408667323807c0d0e4af36859b02c16`, 28/04/2026 | SKILL.md, north-star-template.md, examples/example-brief.md, LICENSE | MIT verificada no LICENSE, copyright 2026 Lightbulb Moment Labs; preservar aviso em eventual cópia |
| Magnus Hedemark / magnus919 | `dcfba034d1b6f9692a882ff76f028b0073d009af`, 12/10/2026 | chief-of-staff-methodology/SKILL.md; references/executive-briefing.md, gatekeeping-and-triage.md, institutional-memory.md, source-index.md, force-multiplication.md | `license: MIT` declarada no frontmatter; LICENSE raiz e da pasta retornaram 404. Não afirmar auditoria legal do acervo inteiro |
| mgonto / Gonto | `28f5065274b43360d7f564f5833c97f9377d3313`, 11/03/2026 | README.md; todoist-due-drafts/SKILL.md; executive-digest/SKILL.md; email-drafting/SKILL.md; config/DEBUG_LOGGING.md | Sem licença no frontmatter desses arquivos; LICENSE raiz retornou 404. Não redistribuir conteúdo sem esclarecer permissão |
| snarktank / clawchief; commit atribuído a R2 | `1fcd1b61357963c1bc6f396a93ef0bd5f9a9c7c1`, 09/04/2026 | skills/executive-assistant/SKILL.md; clawchief/priority-map.md; clawchief/auto-resolver.md | Sem licença no frontmatter; LICENSE raiz retornou 404. Autoria humana individual não estabelecida pelo commit |

Links primários:

- [Lightbulb: SKILL completo](https://github.com/lightbulbmomentlabs/chief-of-staff/blob/e8773e786408667323807c0d0e4af36859b02c16/SKILL.md), [template](https://github.com/lightbulbmomentlabs/chief-of-staff/blob/e8773e786408667323807c0d0e4af36859b02c16/north-star-template.md), [exemplo](https://github.com/lightbulbmomentlabs/chief-of-staff/blob/e8773e786408667323807c0d0e4af36859b02c16/examples/example-brief.md), [licença](https://github.com/lightbulbmomentlabs/chief-of-staff/blob/e8773e786408667323807c0d0e4af36859b02c16/LICENSE).
- [Magnus: SKILL completo](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/SKILL.md), [briefing](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/references/executive-briefing.md), [triagem](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/references/gatekeeping-and-triage.md), [memória institucional](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/references/institutional-memory.md), [origem](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/references/source-index.md), [mecanismos de apoio](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/chief-of-staff-methodology/references/force-multiplication.md).
- [Mgonto: acompanhamento](https://github.com/mgonto/executive-assistant-skills/blob/28f5065274b43360d7f564f5833c97f9377d3313/todoist-due-drafts/SKILL.md), [digest](https://github.com/mgonto/executive-assistant-skills/blob/28f5065274b43360d7f564f5833c97f9377d3313/executive-digest/SKILL.md), [regras de rascunho](https://github.com/mgonto/executive-assistant-skills/blob/28f5065274b43360d7f564f5833c97f9377d3313/email-drafting/SKILL.md), [logging](https://github.com/mgonto/executive-assistant-skills/blob/28f5065274b43360d7f564f5833c97f9377d3313/config/DEBUG_LOGGING.md), [README/dependências](https://github.com/mgonto/executive-assistant-skills/blob/28f5065274b43360d7f564f5833c97f9377d3313/README.md).
- [Snarktank: SKILL completo](https://github.com/snarktank/clawchief/blob/1fcd1b61357963c1bc6f396a93ef0bd5f9a9c7c1/skills/executive-assistant/SKILL.md), [prioridades](https://github.com/snarktank/clawchief/blob/1fcd1b61357963c1bc6f396a93ef0bd5f9a9c7c1/clawchief/priority-map.md), [resolução](https://github.com/snarktank/clawchief/blob/1fcd1b61357963c1bc6f396a93ef0bd5f9a9c7c1/clawchief/auto-resolver.md).

### Recursos ausentes e dependências

Mgonto exige configuração pessoal, OpenClaw, gog/Gmail, Todoist CLI e, para contexto de reuniões, Granola/Grain via mcporter. `scripts/skill_log.py`, `scripts/cron_canary.py` e `style/DIGEST_RULES.md` retornaram 404 nos caminhos públicos consultados; a instrução aponta para workspace do usuário. Esses recursos não foram lidos nem executados. `email-drafting` remete ainda a guias pessoais e humanizer não inspecionados nesta frente. Logo, não há pacote autocontido demonstrado. O texto do logging foi lido integralmente; não existe revisão estática dos scripts ausentes.

Snarktank requer gog, Google Workspace, arquivos locais de tarefas/notas e política pessoal. Os dois recursos que determinam prioridade e autonomia foram lidos integralmente; não houve avaliação completa de sua ingestão de reuniões, roteamento comercial ou sistema de tarefas. Magnus e Lightbulb não exigem runtime externo para os componentes selecionados; isso não prova adequação do pacote à galeria.

## Comparação por componente

| Fonte / arquivo | Contribuição | Decisão | Motivo e adaptação ao Assistente Executivo |
|---|---|---|---|
| Magnus SKILL.md | Separar preparação, autoridade e compromisso confirmado | Aproveitar | Proposta não vira decisão; nota de discussão não vira tarefa aceita |
| Magnus SKILL.md, Task Creation Discipline | Exigir dono e data sustentáveis para criar tarefa externa | Adaptar | Em material local, registrar compromisso com `responsável não informado` ou `prazo não informado`; não perder uma obrigação real porque um campo falta. Perguntar apenas quando a lacuna muda decisão ou execução |
| Magnus executive-briefing.md | Decisão, fatos, lacunas, alternativas reais e recomendação | Aproveitar | Ajusta forma à audiência e não obriga quantidade de seções, páginas ou alternativas fictícias |
| Magnus gatekeeping-and-triage.md | Consequência de atraso e dono autorizado | Adaptar | Triagem local focada no pedido; não implantar sistema de gatekeeping ou canal corporativo |
| Magnus institutional-memory.md | Registrar motivo, origem e estado de decisão/compromisso | Adaptar | Pequeno registro no arquivo autorizado quando útil à continuidade; não criar banco, memória paralela ou retenção administrativa sem demanda |
| Magnus force-multiplication.md | Julgar apoio por resultados observáveis | Aproveitar | Avaliar menos retrabalho e melhores handoffs; não prometer fórmula de produtividade |
| Lightbulb SKILL.md + template | Prioridades relacionadas ao objetivo existente e regras atuais | Adaptar | Aceitar objetivo informado na conversa/arquivo; reconhecer atualizações mais recentes sem exigir frontmatter ou citação literal para toda obrigação |
| Lightbulb SKILL.md + example-brief.md | Entregar rascunho, aceitar correção e omitir seções vazias | Aproveitar | Ajustar capacidade/contexto na primeira versão e refazer quando a pessoa corrigir |
| Lightbulb SKILL.md | Hard-fail sem north-star; três prioridades; foco exclusivo em receita e produto | Descartar | Assistente atende obrigação operacional, pessoal e institucional; documento formal e formato fixo não são pré-requisitos |
| Mgonto todoist-due-drafts | Verificar rascunho e resposta existentes antes de cobrar; usar contexto concreto | Adaptar | Checar materiais disponíveis e autorizados; se não há acesso à caixa, declarar esse limite e entregar rascunho interno. Não afirmar que a pessoa não respondeu |
| Mgonto executive-digest | Deduplicar e destacar pendência cujo estado mudou | Adaptar | Identidade pela obrigação e evidência; não exigir IDs de serviço, estado JSON ou cron para resumo pontual |
| Mgonto executive-digest | Qualquer resposta de membro da equipe encerra item; apagar rascunho antigo automaticamente | Descartar | Resposta pode apenas acusar recebimento. Conclusão exige cumprir o resultado; preservar item e rascunho quando incerto |
| Mgonto executive-digest | Excluir tarefa sem data, abortar se Gmail indisponível, janelas fixas | Descartar | Compromisso importante sem prazo permanece visível. Fonte indisponível não invalida material local suficiente |
| Mgonto email-drafting | Linguagem/voz da conversa e prioridade ao resultado prometido | Adaptar | Português e tom do destinatário; promessa de anexo não presume que arquivo existe. Texto produzido continua rascunho |
| Mgonto email-drafting | Completar tarefa depois de enviar email/draft | Descartar | Criar rascunho não equivale a enviar nem cumprir o compromisso |
| Mgonto debug logging + referências a scripts | Logs, canário, hooks e cron obrigatórios | Descartar | Sem ganho real para ler notas e produzir plano; scripts ausentes e risco de registrar informação privada |
| Snarktank priority-map.md | Contexto muda o que merece atenção; agrupar duplicações | Adaptar | Compromisso e objetivo fornecidos; não transplantar nomes, programas, metas e relações pessoais do autor |
| Snarktank priority-map.md | Ignorar item fora de pessoas/programas importantes; rankear confiança/lealdade | Descartar | Obrigação nova e risco real podem vir de desconhecido; não criar perfis subjetivos de pessoas |
| Snarktank auto-resolver.md + SKILL.md | Reutilizar fonte atual e executar trabalho interno já autorizado | Adaptar | Preparar resultado concreto na mesma interação; não pedir permissão repetida para leitura/rascunho interno |
| Snarktank auto-resolver.md + SKILL.md | Enviar mensagens, arquivar emails, alterar eventos e criar follow-up futuro por padrão | Descartar | Preparação interna não delega envio, agenda, exclusão ou monitoramento futuro |

## Deduplicação e descartes de descoberta

Magnus declara derivação de `magnus919/hermes-profiles`, commit `867a555`, com reescrita. São uma família de origem; o antecedente não foi contado como segunda validação nem sua licença presumida. Os três SKILL.md de mgonto compõem uma família operacional, não três evidências independentes de eficácia. A semelhança funcional entre Lightbulb e Snarktank não permite afirmar parentesco; não foi observado aviso de derivação entre eles.

[borghei/Claude-Skills chief-of-staff](https://github.com/borghei/Claude-Skills/blob/main/c-level-advisor/chief-of-staff/SKILL.md) foi descoberto como orquestrador de conselheiros/board, com licença declarada MIT + Commons Clause; não selecionado nem lido integralmente. [mattpocock/skills](https://skills.sh/mattpocock/skills/chief-of-staff) prioriza subagentes e objetivo prolongado; apenas descoberta, não solução para pedido diário local. [scuba-stack html-executive-brief](https://github.com/danielchappell/scuba-stack/blob/main/skills/html-executive-brief/SKILL.md) e [shoemoney executive-brief](https://github.com/shoemoney/shoemoney-skills) foram encontrados, mas sua ênfase em engenharia, épicos e inventário técnico amplia indevidamente o escopo. Não recomendados nem usados como pacote avaliado. A frente de reuniões cobre agenda/notas; não duplicar aqui sua seleção Zapier.

## Síntese executável para criação posterior

### Núcleo mínimo

1. Reconhecer entrega e período: priorizar o dia, organizar a semana, resumir para decisão ou preparar acompanhamento. Reutilizar contexto já disponível e permitido; não reapresentar questionário nem pedir conector como primeira etapa.
2. Levantar apenas o que muda a entrega: objetivo atual, compromissos, prazos reais, dependências, disponibilidade/capacidade informada e autoridade. Não inventar esforço, horário, responsável ou data. Se faltam, marcar lacuna e prosseguir na parte possível.
3. Justificar a ordem com contribuição, compromisso, consequência do atraso e desbloqueio. Explicitar conflitos: tarefa importante pode esperar por dependência; tarefa urgente pode exigir só resposta mínima. Não somar score artificial nem transformar urgência em importância.
4. Fazer plano proporcional à capacidade conhecida. Se duas entregas competem pelo mesmo intervalo, mostrar escolha e recomendação, sem prometer ambas. Capacidade desconhecida produz ordem sugerida, não agenda ocupada fictícia. Semana inclui marcos e dependências reais; não lote automático de novos projetos.
5. Separar fato/relato/hipótese, decidido/proposto, compromisso confirmado/ação sugerida, planejado/em andamento/concluído. Preservar dono e prazo não informados. Conclusão exige evidência do resultado ou confirmação autorizada, não presença de email/rascunho.
6. Entregar forma mais útil: lista curta com razões, tabela se facilita comparar, resumo com recomendação, ou mensagem interna pronta para revisar. Sem seções vazias, repetição de notas ou relatório por hábito.
7. Antes de acompanhar, verificar material atual para duplicação, conclusão ou mudança. Rascunho inclui assunto, destinatário conhecido, contexto, pedido claro e próximo passo sustentado. Destinatário ou data ausentes permanecem abertos; nunca anunciar envio, evento ou lembrete que não ocorreu.

### Referências sob demanda

- `references/prioridades.md`: capacidade, bloqueios, prazos, conflitos e ajustes diário/semanal, sem matriz obrigatória.
- `references/resumo-executivo.md`: evidência, decisão pretendida, alternativas reais, recomendação e passagem para responsável autorizado.
- `references/acompanhamento.md`: obrigação, duplicidade, conclusão comprovada e rascunho interno com lacunas explícitas.

Nomes são proposta, não arquivos criados. Bibliografia e revisão de licenças ficam no dossiê, não no fluxo padrão. Scripts só entram depois de ganho concreto demonstrado por volume, cálculo ou repetição. Se uma dependência passa a ser necessária, confirmar disponibilidade e oferecer instalação simples em linguagem comum quando autorizada; nenhuma instalação ocorreu nesta pesquisa. Monitor futuro exige pedido explícito e mecanismo real. Recorrência ou desgaste podem justificar oferecer adaptar a própria skill, sem criar ritual, serviço ou automação por padrão.

## Exemplo original de aplicação

Material informado: revisão para conselho até quinta; Carla aceitou entregar números na terça; três horas disponíveis hoje; minuta depende dos números; convite de parceria sem prazo; resposta `recebido` de Carla.

Saída adequada: preparar hoje o esqueleto da minuta com campos pendentes, acompanhar números de Carla na terça e recomendar avaliar a parceria depois do compromisso com conselho. Não atribuir prazo à parceria. `Recebido` não comprova números entregues. Se terça já passou e não há atualização nos materiais disponíveis, registrar situação incerta e produzir: “Carla, estamos fechando a minuta para quinta. Você consegue confirmar a situação dos números combinados para terça e o que falta?” O texto é rascunho interno; não foi enviado e nenhum lembrete foi criado. O agente só agenda três horas de atividades se houver estimativas sustentadas que caibam nelas; caso contrário entrega a ordem e a lacuna de duração.

## Avaliação futura e lacunas

Critérios abaixo são plano de avaliação, não testes executados nem demonstração de eficácia:

- Pedido em português com notas coladas e nenhum conector gera entrega útil sem instalação.
- Capacidade curta e prazos conflitantes geram recomendação de escolha; não cronograma impossível.
- Urgente de baixo impacto e importante sem prazo recebem razões distintas, sem ritual de quadrantes.
- Responsável/data ausentes permanecem desconhecidos; sugestão não vira compromisso aceito.
- Resposta `recebido`, rascunho pronto e tarefa planejada não são reportados como resultado concluído.
- Cobrança já atendida ou duplicada nos materiais é omitida; acesso parcial à caixa é declarado.
- Resumo separa fatos, hipótese, recomendação e decisão real; nenhuma alternativa fictícia para completar template.
- Pedido de acompanhamento produz texto interno; envio, agenda e vigia futura exigem autorização correspondente.
- Pedido semanal usa disponibilidade e dependências existentes sem implantar gerenciador completo.
- Correção da pessoa muda a versão sem defender contexto antigo; recorrência permite propor adaptação da skill própria.

Restam: execução real no Studio/Hermes, avaliação com pedidos representativos, revisão de licença antes de copiar recursos e checagem de empacotamento se algum pacote externo for considerado para distribuição. O texto não demonstra que essas skills estão instaladas, publicadas, aprovadas ou funcionando no destino. Não foi necessário ampliar a busca após resolver as escolhas materiais de contexto local, prioridade, briefing e acompanhamento.
