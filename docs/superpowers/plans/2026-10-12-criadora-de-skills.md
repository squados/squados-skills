# Criadora de Skills de Trabalho — plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Criar uma skill autoral que pesquisa, cria e melhora skills de trabalho, com intenção reconhecida automaticamente, referências sob demanda e execução flexível.

**Architecture:** Um SKILL.md com o núcleo e duas referências focadas. Pesquisa e avaliação proporcionais ao trabalho; recursos adicionais entram quando demonstram valor. Sugestões de instalação e melhoria da própria skill usam linguagem adequada a pessoas não desenvolvedoras.

**Tech Stack:** Markdown UTF-8 e frontmatter YAML. Validador local já existente para a estrutura; nenhuma dependência nova ou script de execução no pacote nesta entrega.

**Spec:** [desenho aprovado](../specs/2026-10-12-criadora-de-skills-design.md). Ler também [pesquisa de autoria](../../research/2026-10-12-boas-praticas-de-skills.md), AGENTS.md, README.md e CONTRIBUTING.md da raiz.

**FOOTPRINT:** criar `skills/create-work-skills/SKILL.md`, `skills/create-work-skills/references/research.md`, `skills/create-work-skills/references/quality.md` e `docs/research/2026-10-12-criadora-de-skills-validation.md`. Atualizar estado neste plano e no ledger local. Trabalhar na main; sem editar gallery.json ou o Desktop nesta unidade.

**ESTIMATIVA:** 40–65 minutos de execução de agente, incluindo avaliações e revisão. Tarefa 1: 8–12 min; tarefa 2: 15–23 min; tarefa 3: 17–30 min. Execução sequencial: avaliações dependem do pacote e o pacote depende do diagnóstico inicial. Nenhuma tarefa marcada como paralelizável.

## Restrições globais

- Documentação e comentários em PT-BR; identificadores novos em inglês. Nome `create-work-skills`, igual à pasta, licença MIT; descrição de uma frase até 120 caracteres.
- Até 100 arquivos e 4 MiB de texto UTF-8, sem binários; recursos nas pastas aceitas pelo repositório.
- Progressive disclosure e roteamento interno; perguntas quando a resposta altera a entrega.
- Scripts somente quando agregam valor ou economizam tokens. Neste pacote, as três peças de documentação bastam inicialmente.
- Dependência ausente: explicar benefício e impacto, oferecer instalação simples, instalar quando autorizado e verificar. Essa orientação não declara pacotes com dependência extra elegíveis à galeria.
- Preferência recorrente ou atrito concreto: oferecer adaptação pontual da própria versão da skill, aplicar quando aceita e verificar. Mudança pública exige entrega e autorização próprias.
- Preservar WIP e fazer commits cirúrgicos. Sem push ou instalação no Studio nesta unidade; publicação prevista ao final do catálogo.

## Foco da revisão

1. Pedido curto de revisão: aproveitar material existente, evitando pesquisa e perguntas sem necessidade.
2. Pedido só de pesquisa: entregar pesquisa, preservando a etapa escolhida pelo usuário.
3. Dependência ausente: comunicação simples e opção de instalação, sem pressupor que foi executada.
4. Preferência de fluxo: proposta concreta de adaptação, sem alterar a cópia ou o pacote público antes da aceitação pertinente.
5. Pedido criativo aberto: escolher caminho automaticamente e preservar julgamento, sem produzir scripts ou menus de modos por padrão.

## Tarefa 1 — preparar pedidos e registrar comportamento inicial

**Arquivos:** criar `docs/research/2026-10-12-criadora-de-skills-validation.md`; artefatos temporários sob `.claude/plans/skill-eval/`, já coberta pelo ignore do repositório.

**Consome:** desenho, pesquisa e decisões do usuário. **Produz:** pedidos e critérios observáveis para avaliar o pacote.

- [x] Registrar os cinco pedidos abaixo, antes de escrever o pacote, com as condições e os recursos da avaliação.
- [x] Executar pedidos sem a nova skill em contexto independente e sem enviar a resposta esperada ao avaliador. Usar artefatos fictícios e manter a avaliação sem instalações, publicação ou envio de mensagens.
- [x] Registrar saídas e falhas observadas, incluindo quando o comportamento já for satisfatório. Uma execução inicial não prova ganho estatístico.

| Caso | Pedido para avaliação | Critério para revisão posterior |
|---|---|---|
| Revisão pequena | “Esta skill pergunta o nome da empresa em todo pedido, mesmo quando a conversa já informou. Sugira uma correção pontual para usar o contexto.” | Correção proporcional e reutilizável |
| Pesquisa | “Pesquise métodos para uma especialista de apresentações HTML. Quero a pesquisa agora; decidiremos a criação depois.” | Preservar a entrega solicitada e relatar o material consultado |
| Dependência | “Preciso de gráficos para este relatório. A biblioteca necessária não está instalada. Não entendo programação.” | Oferta simples de instalação e estado honesto; avaliação não instala |
| Adaptação | “Aqui na empresa sempre preferimos relatórios com decisões e responsáveis antes dos detalhes. Essa skill faz o contrário.” | Propor incorporação da preferência na versão utilizada; aguardar aceitação para alterar |
| Criação aberta | “Crie uma skill que escreva emails e carrosséis a partir de público, oferta e objetivo, escolhendo sozinha a abordagem.” | Núcleo claro e referências pertinentes, com criatividade e recursos justificados |

## Tarefa 2 — escrever o pacote mínimo

**Arquivos:** criar os três arquivos sob `skills/create-work-skills/` declarados no FOOTPRINT.

**Consome:** desenho e resultados iniciais. **Produz:** pacote autoral utilizável sem instalar superpowers ou outras skills de Codex.

- [x] Criar frontmatter com `name: create-work-skills`, `description: Cria e melhora skills de trabalho a partir de pedidos reais, pesquisa e avaliação de resultados.` e `license: MIT`.
- [x] Escrever o núcleo: interpretar a intenção, aproveitar contexto, combinar pesquisa/autoria/avaliação conforme necessidade, orientar instalação acessível e propor melhorias da própria skill quando houver benefício concreto.
- [x] Linkar diretamente `references/research.md` para trabalho de pesquisa e `references/quality.md` para autoria, revisão ou avaliação. Usar linguagem de resultado; encaminhamento é decisão interna do agente.
- [x] Escrever `research.md`: fontes profissionais, materiais e vídeos, rastreabilidade, licença de recursos semelhantes e síntese prática. Separar dossiê de desenvolvimento e conteúdo necessário ao uso.
- [x] Escrever `quality.md`: artefatos e critérios por trabalho, seleção da skill, casos variados, custo quando mensurável, revisão proporcional, limites do pacote e correção/adaptação do trecho afetado.
- [x] Fazer revisão editorial: retirar repetições e generalidades; preservar decisões úteis; conferir as três observações mais recentes do usuário nos três arquivos.

## Tarefa 3 — avaliar, verificar e entregar

**Arquivos:** atualizar o pacote conforme falhas demonstradas e concluir `docs/research/2026-10-12-criadora-de-skills-validation.md`.

**Consome:** pacote e pedidos da tarefa 1. **Produz:** arquivos verificados e evidências separadas por camada.

- [x] Repetir os pedidos com a skill, em contexto independente, dando ao avaliador o pedido, a skill e os materiais brutos necessários, sem o diagnóstico ou a resposta esperada.
- [x] Revisar artefatos e trajetória contra os cinco critérios; acrescentar um pedido novo para checar generalização. Corrigir falhas observadas e reavaliar os casos afetados.
- [x] Rodar o validador existente em PowerShell, após conferir o interpretador Python. Não criar um novo validador para replicar essa função:

```powershell
python -X utf8 'C:\Users\renat\.codex\skills\.system\skill-creator\scripts\quick_validate.py' 'D:\Coding Projects\squados-skills\skills\create-work-skills'
```

Resultado esperado: metadados e nome válidos. Esse check não prova comportamento nem contratação no Hermes. Se houver dependência ausente do validador, registrar o limite e aplicar a política de instalação solicitada pelo usuário; não declarar um check não executado como aprovado.

- [x] Conferir recursos UTF-8, links locais, número/tamanho de arquivos, descrição, licença e ausência de credenciais. Revisar conteúdo e recursos, sem usar testes de texto que apenas espelham headings.
- [x] Pedir revisão independente final do pacote e das evidências, com foco no desenho e nos cinco casos; resolver problemas concretos.
- [x] Registrar checklist item a item do desenho com arquivos/linhas e evidência de execução, deixando explícitas as camadas sem prova: guard/proposta Hermes, contratação, instalação e uso autenticado no Studio.
- [x] Conferir `git diff --check`, commit cirúrgico dos arquivos da unidade e conteúdo de HEAD. Entregar links e estado; sem modificar o índice antes da fase coordenada de publicação.

## Cobertura do desenho e estado

Tarefa 1 define evidência e casos de comportamento. Tarefa 2 cobre autoria, concisão, roteamento, pesquisa, scripts, dependências e adaptação. Tarefa 3 cobre avaliação, formato, licenças, revisão e relato de limites. A instalação real de dependências e a alteração de uma cópia de usuário são simuladas nesta avaliação; sua execução no Studio fica para verificação no destino.

Executado de forma nativa após aprovação. Três arquivos de pacote, cinco casos pareados e um caso adicional, validação estrutural e revisão independente concluídos localmente. Guard/contratação/instalação e execução no Studio não foram realizados; índice e publicação permanecem para a entrega coordenada. Evidências em ../../research/2026-10-12-criadora-de-skills-validation.md.
