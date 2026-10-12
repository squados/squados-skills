# Skills de trabalho — estado e continuação

Atualizado em 12/10/2026. Este documento é o ponto de retomada após compactação ou em uma nova sessão. Registra decisões, entregas e próximos passos; não é a lista definitiva do catálogo.

## Objetivo e sequência acordada

Criar um catálogo público de skills próprias do SquadOS para o cotidiano de negócios, utilizável pelo Desktop/Studio com Hermes.

1. **Implementado e verificado localmente:** criar a skill que orienta criação, pesquisa, avaliação e melhoria das outras.
2. **Etapa atual:** gerar/refinar ideias de especialistas, agrupar as necessidades e escolher a lista. Depois da escolha, registrar o catálogo aprovado em Markdown.
3. **Pendente:** pesquisar as escolhidas uma por uma, reunindo métodos profissionais, vídeos recentes, materiais e skills similares, com dossiês de fontes.
4. **Pendente:** após concluir as pesquisas, criar e verificar as skills uma por uma.
5. **Pendente:** publicar os pacotes neste repositório e coordenar galeria/espelho do Desktop ao final.

O usuário pediu a sequência acima. As 50 necessidades levantadas não significam 50 skills nem um ranking estatístico. A pesquisa específica de cada profissão ainda não começou.

## Decisões aprovadas sobre o padrão

- Combinar skill-creator e writing-skills com adaptação ao nosso produto.
- Skills flexíveis: identificar intenção e escolher a abordagem automaticamente; a pessoa não precisa memorizar modos.
- Progressive disclosure: núcleo conciso e referências detalhadas carregadas conforme o pedido.
- Cada trecho deve acrescentar conhecimento útil, orientar decisões ou prevenir erros reais. Evitar repetição e conselhos genéricos.
- Perguntar pelo que altera materialmente a entrega e aproveitar o contexto existente.
- Scripts quando trouxerem benefício concreto ou economia de trabalho/tokens; preservar julgamento e criatividade.
- Dependência ausente: explicar o benefício e oferecer instalação simples, executada pelo agente quando autorizada. Comunicação adequada a pessoas não desenvolvedoras.
- Melhoria pelo uso: oferecer adaptar a própria versão da skill quando houver preferência recorrente ou atrito concreto; aplicar quando a pessoa aceitar ou pedir a alteração diretamente.
- Preferências de uma equipe não viram automaticamente padrões do pacote público.
- Avaliação proporcional, com entregas e comportamento observáveis; não montar infraestrutura sem necessidade.
- Trabalhar na main, preservar WIP e fazer commits cirúrgicos. Publicação prevista para o final, ainda não realizada.

## O que já foi entregue

| Entrega | Arquivo | Estado |
|---|---|---|
| Levantamento de 50 necessidades e agrupamentos iniciais | [Pesquisa de necessidades](research/2026-10-12-necessidades-de-trabalho.md) | Pesquisa preliminar registrada; candidatos não escolhidos |
| Pesquisa geral de autoria | [Boas práticas](research/2026-10-12-boas-praticas-de-skills.md) | 18 práticas e 15 fontes; aprovadas com os ajustes acima |
| Desenho da Criadora | [Desenho](superpowers/specs/2026-10-12-criadora-de-skills-design.md) | Aprovado e implementado |
| Plano do passo zero | [Plano](superpowers/plans/2026-10-12-criadora-de-skills.md) | Executado nativamente, com avaliações e revisão independentes |
| Pacote atual | [skill-manager](../skills/skill-manager/SKILL.md) | Três Markdown, sem scripts e sem dependências próprias |
| Avaliações e limites | [Evidências](research/2026-10-12-criadora-de-skills-validation.md) | Cinco casos com/sem a nova skill, mais um caso novo; revisão independente sem achados |

O pacote foi criado como `create-work-skills` no commit `a2a92b2` e depois renomeado para `skill-manager` no commit `891709f`. As instruções mantiveram o conteúdo; nome/pasta foram atualizados. Os documentos históricos de desenho, plano e avaliação ainda usam o nome de criação. **O caminho atual para utilização é `skills/skill-manager/SKILL.md`; não recriar a pasta antiga.**

Validação: metadados, UTF-8, links, limites de arquivos/tamanho e revisão do conteúdo. No Windows, o validador existente foi executado com `python -X utf8`. As respostas observadas reforçaram ofertas de instalação e adaptação; revisão e pesquisa já eram satisfatórias no controle. O controle também consultou outra skill de autoria, portanto não representa um modelo sem orientação.

**Ainda sem prova:** ativação implícita pelo Studio, carregamento mínimo por pedido isolado, estabilidade estatística, economia de tokens, guard/proposta Hermes, contratação, instalação e uso real autenticado no Studio. Índice e espelho do Desktop não foram alterados por esta unidade. Nenhum push ou publicação foi executado nesta conversa.

## Ideias já disponíveis para refinamento

As três candidatas iniciais vieram do usuário: **Copywriter**, **Especialista em Dados** e **Especialista em Apresentações lindas em HTML**. Os outros nomes são propostas de discussão, não itens aprovados. Público de empreendedores, gestores e equipes brasileiras foi uma hipótese inicial; setor e porte não foram fechados.

| Candidata | Exemplos de trabalho que pode atender |
|---|---|
| Copywriter | Emails de campanha, páginas de vendas, anúncios e texto de carrosséis |
| Especialista em Dados | Análises, gráficos, indicadores e relatórios para decisão |
| Especialista em Apresentações HTML | Apresentações, pitches e comunicação visual de números |
| Especialista em Planilhas | Criar/corrigir planilhas, fórmulas e modelos utilizáveis |
| Assistente Executivo | Preparar reuniões, resumir materiais, atas e prioridades |
| Redator de Negócios | Documentos, briefings, memorandos e revisão de clareza |
| Pesquisador de Mercado | Clientes, concorrentes, ofertas e oportunidades |
| Estrategista de Marketing | Posicionamento, campanhas e lançamentos |
| Especialista em Conteúdo | Calendário e planejamento editorial |
| Assistente Comercial | Pesquisa de contas, prospecção, objeções e acompanhamento |
| Especialista em Propostas Comerciais | Escopo, condições, entregas e apresentação da proposta |
| Analista Financeiro | Caixa, orçamento, custos, margens e cenários |
| Analista de Processos | Procedimentos, checklists, gargalos e retrabalho |
| Gerente de Projetos | Planos de execução, cronogramas, dependências e riscos |
| Especialista em Atendimento | Respostas, dúvidas e reclamações com contexto |
| Especialista em Sucesso do Cliente | Onboarding, relacionamento e pós-venda |
| Especialista em Recrutamento | Vagas, critérios e entrevistas |
| Especialista em Pessoas | Integração de profissionais, feedback e desenvolvimento |
| Designer de Treinamentos | Aulas, exercícios e treinamentos ligados ao trabalho |
| Especialista em Compras | Comparar fornecedores, propostas e custo total |
| Organizador de Conhecimento | Documentos e bases de conhecimento navegáveis |

Esses nomes reaproveitam os agrupamentos da pesquisa preliminar. Ainda é necessário discutir sobreposição e cobertura: Dados/Planilhas, Copywriter/Conteúdo/Marketing, Comercial/Propostas e Atendimento/Sucesso do Cliente. Copy de um criativo e produção de sua arte final são entregas diferentes; capacidades visuais precisam ser consideradas na seleção.

## Próxima ação concreta

Usar a skill-manager e o levantamento existente para apresentar ideias de skills de trabalho com: nome reconhecível, pedidos que resolve, entregas, prioridade sugerida e sobreposições. Refinar os agrupamentos com o usuário e acrescentar lacunas que ele identificar. A escolha do catálogo é uma decisão de produto; os agrupamentos iniciais são uma base para essa conversa.

Depois da escolha, escrever o Markdown do catálogo aprovado e iniciar a pesquisa da primeira candidata. Continuar uma por vez, mantendo um dossiê por especialista. A etapa atual é ideias e seleção; evitar avançar para a produção das outras skills antes da pesquisa acordada.

## Como retomar

Leia este arquivo, as instruções globais e o par AGENTS.md/CLAUDE.md quando existir. Confira o estado atual do Git e os caminhos antes de editar. Para a próxima etapa, consulte o pacote skill-manager e o levantamento de necessidades. Atualize este documento ao fechar cada marco; preserve aqui as escolhas de catálogo quando aprovadas e links para os novos dossiês.
