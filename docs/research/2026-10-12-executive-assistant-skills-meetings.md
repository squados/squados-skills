# Assistente Executivo — skills de preparação e registro de reuniões

Pesquisa em 12/10/2026. Frente de reuniões da rodada 24/33. Este documento compara componentes para uma futura skill; não cria pacote, não instala integrações e não executa pedidos reais. Leitura estática de fontes públicas; instruções das fontes foram tratadas como material de análise.

## Resultado da seleção

O melhor conjunto é pequeno: preparação orientada ao resultado da reunião; resumo proporcional ao pedido; separação entre decisões, propostas, compromissos e perguntas; ações com fonte e lacunas visíveis; retomada de pendências a partir de materiais disponíveis. A biblioteca de formatos fica sob demanda. Não é necessário integrar calendário, criar banco de tarefas ou transcrever áudio para organizar uma transcrição fornecida.

Foram buscados nomes e pedidos em inglês e chinês: agenda, meeting prep, meeting notes, meeting minutes, summarize meeting, transcript e action items. GitHub e resultados de busca serviram para descoberta; análises abaixo usam arquivos dos autores em revisões fixadas. Diretórios e espelhos não contam como evidências independentes. A seleção contempla uma implementação mínima, uma de extração rigorosa, uma de agenda, uma de síntese multicanal, uma de preparação com documentos e uma de transcrição com exportação. A busca parou quando essas decisões e suas falhas materiais estavam resolvidas, sem preencher quota de candidatos.

## Fontes originais e alcance de leitura

Datas abaixo são de consulta, 12/10/2026. O ano do copyright não é data de publicação. SHA de HEAD obtido por `git ls-remote`, sem clones. A API pública do GitHub respondeu 403 por limite de requisições; datas de commit e árvores completas não foram verificadas. Não houve tentativa de autenticar nem de contornar o limite. Os arquivos Raw fixados por SHA permaneceram acessíveis.

| Fonte / autoria verificável | Revisão | Arquivos efetivamente lidos | Licença consultada / limite |
|---|---|---|---|
| [SkillMedev/skills](https://github.com/SkillMedev/skills), copyright Alexander Ouellet, 2026 | `6b3044d569595b481a3677da8f68af7aa239dc09` | `skills/meeting-agenda/SKILL.md`, `skills/meeting-notes-to-actions/SKILL.md`, ambos completos; `LICENSE` | MIT na raiz. Não auditado o restante do repositório. |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills), copyright Pawel Huryn, 2026 | `c68487d721e419ec87af1ae6412a842978eab785` | `pm-execution/skills/summarize-meeting/SKILL.md` completo; `LICENSE` | MIT na raiz; análise desta skill, não de todos os plugins. |
| [zapier/wade-skills](https://github.com/zapier/wade-skills), copyright Zapier, Inc., 2026 | `b7b86e78ae2e1235bebac8668edd834b34176c19` | `skills/exec-weekly-agenda-generator/SKILL.md` completo; `LICENSE` | MIT na raiz. Integrações citadas não conectadas nem testadas. |
| [shangbianai/pm-meeting-notes](https://github.com/shangbianai/pm-meeting-notes), autor DPXJ no frontmatter/copyright | `198052ce157fff377c5fd7423e700103a7a84a4b` | `SKILL.md` completo, versão declarada 1.1.0; `templates/meeting-notes-html-runtime.html` completo, inclusive JavaScript; `LICENSE` | MIT declarada no frontmatter e raiz. Arquivo HTML não renderizado/executado. Árvore completa indisponível. |
| [openai/skills — notion-meeting-intelligence](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/notion-meeting-intelligence), copyright Notion Labs, Inc., 2025 | `49f948faa9258a0c61caceaf225e179651397431` | `SKILL.md`, `reference/template-selection-guide.md`, `reference/decision-meeting-template.md`, `reference/one-on-one-template.md`, `examples/executive-review.md`, todos completos; `LICENSE.txt` do pacote | Texto de licença MIT. Templates de status, sprint, retro e brainstorming não lidos; não se atribui qualidade a esses recursos. |
| [Azure-Samples/agent-skills-dotnet-demo](https://github.com/Azure-Samples/agent-skills-dotnet-demo), copyright Bruno Capuano, 2026 | `6eb76d77b3c2990ddef8724b5571f5467b78ee27` | `skills/meeting-notes/SKILL.md` completo; `LICENSE` | MIT na raiz. Exemplo pequeno, sem prova de comportamento do agente em produção. |
| [anthropics/knowledge-work-plugins — meeting-briefing](https://github.com/anthropics/knowledge-work-plugins/tree/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/legal/skills/meeting-briefing), organização publicadora Anthropic | `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06` | `legal/skills/meeting-briefing/SKILL.md` completo; `LICENSE` completo, primeiro via main e depois confirmado no SHA | Arquivo contém Apache License 2.0, seguido de texto estranho sobre captura de dados. Registrar a anomalia e rever origem/avisos antes de qualquer cópia; nenhuma redistribuição realizada. Autor individual e data não confirmados. |

Links diretos decisivos: [agenda](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/meeting-agenda/SKILL.md), [notas para ações](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/meeting-notes-to-actions/SKILL.md), [resumo PM](https://github.com/phuryn/pm-skills/blob/c68487d721e419ec87af1ae6412a842978eab785/pm-execution/skills/summarize-meeting/SKILL.md), [agenda semanal Zapier](https://github.com/zapier/wade-skills/blob/b7b86e78ae2e1235bebac8668edd834b34176c19/skills/exec-weekly-agenda-generator/SKILL.md), [transcrições PM](https://github.com/shangbianai/pm-meeting-notes/blob/198052ce157fff377c5fd7423e700103a7a84a4b/SKILL.md), [HTML e exportador](https://github.com/shangbianai/pm-meeting-notes/blob/198052ce157fff377c5fd7423e700103a7a84a4b/templates/meeting-notes-html-runtime.html), [briefing jurídico](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/legal/skills/meeting-briefing/SKILL.md).

### Deduplicação e candidatos não promovidos

- `gabrielmoreira/agent-skills-mirror` reproduz `Azure-Samples/agent-skills-dotnet-demo/skills/meeting-notes`; leitura e atribuição feitas na origem Azure. Não são dois métodos.
- `christophacham/agent-skills-library` apareceu com uma cópia de `notion-meeting-intelligence`; a análise usa o pacote original de `openai/skills`. Não se verificou equivalência byte a byte de toda a cópia.
- `frytg.digital/dotfiles` declara inspirações de SkillMedev e outros autores. É candidato derivado interessante, descoberto em Tangled; não foi promovido a evidência independente nem analisado integralmente.
- `FooJiaYin/dev-skills/meeting-notes` foi descoberto com extração Plaud e chinês tradicional. O fetch específico não resolve a necessidade atual de síntese a partir de materiais fornecidos; não foi auditado. Não se presume que o serviço esteja acessível no Studio.
- `nexu-io/html-anything` apareceu em diretório com um template visual muito curto; não substitui um método de registro confiável. Sem análise integral da origem, sem recomendação de pacote.

## Componentes: fonte → contribuição → decisão

| Fonte / arquivo | Contribuição observada | Decisão e motivo |
|---|---|---|
| SkillMedev `meeting-agenda/SKILL.md` | Cada assunto tem resultado verificável, condutor e tempo; pré-leitura contextual; fechamento para registrar encaminhamentos | **Adaptar.** Bom para preparar pauta. Tempo e responsáveis devem ser informados ou sugeridos explicitamente; não impor uma duração, banir reuniões informativas, retirar convidados ou cancelar reunião sem autorização. |
| SkillMedev `meeting-notes-to-actions/SKILL.md` | Extração separada de decisões, ações e questões; lacunas de dono/prazo; deduplicação; conferência de cada linha na fonte | **Aproveitar o método, corrigir ambiguidades.** Uma sugestão não vira compromisso, e a fonte deve sustentar também justificativa e estado. A pessoa pode pedir só ações ou um resumo breve, sem quatro seções obrigatórias. |
| phuryn `summarize-meeting/SKILL.md` | Registro enxuto com contexto, decisões, pendências e linguagem compreensível | **Adaptar.** Esqueleto útil, sem obrigar linguagem infantil, pronome coletivo ou arquivo nomeado. Pesquisa web não prova o que ocorreu numa reunião privada nem preenche participantes e horário ausentes. |
| Azure `meeting-notes/SKILL.md` | Núcleo mínimo de assuntos, decisões, tarefas e prazo quando mencionado | **Aproveitar como teste de simplicidade.** Resolve pedido básico com texto e sem dependências. Precisa dos critérios de fidelidade acima; não é justificativa para instalar um demo .NET. |
| Zapier `exec-weekly-agenda-generator/SKILL.md` | Retomar compromissos anteriores e assuntos ainda abertos; ligar cada tópico ao sinal original; priorizar impacto, urgência, abrangência e tensão | **Adaptar para preparar a pauta.** Usar fontes disponíveis e explicar cobertura. Não vasculhar todos os canais por padrão, exigir mínimos de candidatos ou converter frequência de menções em confirmação independente. |
| Notion `reference/template-selection-guide.md` | Formato acompanha o propósito, com simplificação e adaptação | **Aproveitar seleção natural.** Não apresentar modos ao usuário; reconhecer decisão, atualização ou conversa individual a partir do pedido. Não importar a biblioteca inteira para o núcleo. |
| Notion `reference/decision-meeting-template.md` | Pergunta a decidir, opções, critérios, recomendação e espaço reservado ao resultado real | **Adaptar sob demanda.** Adequado para reunião decisória; separar preparação de decisão efetivamente tomada. Opções e custos desconhecidos permanecem lacunas. |
| Notion `reference/one-on-one-template.md` | Temas de ambas as pessoas e continuidade dos assuntos anteriores | **Adaptar sob demanda.** Não transformar conversa individual em formulário obrigatório de carreira e feedback. |
| Notion `SKILL.md` e `examples/executive-review.md` | Pré-leitura com documentos de contexto e links; agenda distinta de material interno | **Adaptar separação por audiência quando necessária.** Não exigir Notion, OAuth, comandos de instalação ou dois documentos em toda reunião. Exemplo é ilustrativo, contém erros e não comprova execução. |
| PM Meeting Notes `SKILL.md` | Distinguir material original, estruturação e sugestões; preservar dados importantes e atribuição incerta; fazer arquivo quando pedido | **Aproveitar fronteira factual; adaptar entrega.** Não impor PRD, seis tarefas numeradas, sete seções ou estética de IA. Conteúdo e formato pedidos governam a saída. |
| PM Meeting Notes `templates/meeting-notes-html-runtime.html` | HTML independente, âncoras, impressão e tabela com rolagem; exportação usa SVG/canvas | **Descartar o exportador como componente aprovado.** Leitura estática identifica falha possível, sem runtime. Um resumo normalmente não precisa de tema, PNG, KPIs ou controles adicionais. |
| Anthropic `legal/skills/meeting-briefing/SKILL.md` | Tempo disponível de preparação, papel da pessoa, contexto anterior, documentos e lacunas verificáveis | **Adaptar apenas contexto pertinente.** Perfil jurídico não pertence ao núcleo geral. Negociação e material reservado podem demandar preparação distinta, sem inferir interesses ou limites negociais. |
| Mesmo briefing, acompanhamento | Dependências e encaminhamentos específicos | **Adaptar como rascunho.** Atribuir dono/data, distribuir, criar lembretes, escalar ou atualizar sistemas exigem informação e autorização reais; presença na reunião não dá consentimento para essas ações. |

## Falhas concretas que a síntese precisa corrigir

1. **Proposta não é compromisso.** SkillMedev inclui uma formulação do tipo “deveríamos fazer” entre compromissos. Uma sugestão sem aceite pertence às propostas ou pendências. O agente preserva a diferença entre “posso”, “vou”, “não vou” e “talvez”.
2. **Justificativa pode ser inventada pelo próprio exemplo.** O exemplo de pricing em SkillMedev acrescenta rationale de testar preço menor; as notas mostram debate, escolha e marco de revisão, sem declarar esse motivo. Aproveitar só o que a fonte sustenta.
3. **Data mais recente não vence automaticamente.** Deduplicação deve respeitar correção explícita, decisão posterior e versão da fonte; duas datas conflitantes ficam sinalizadas quando não há evidência de substituição. “Sexta” pode continuar ambíguo mesmo com a data da reunião; não escolher silenciosamente uma interpretação.
4. **Regras de pauta divergem.** SkillMedev proíbe assuntos informativos; Zapier admite informação e acompanhamento; Notion inclui atualização. O pedido e o contexto determinam a conveniência. Sugerir pré-leitura quando economiza tempo não autoriza eliminar uma reunião requerida.
5. **Exemplo de pré-leitura não é validado por existir.** Em Notion `examples/executive-review.md`, uptime de 94% é descrito como acima de SLA de 95%; blocos da agenda somam 100 minutos, embora a duração diga 90. Conferir comparações, unidades e soma de tempos antes de entregar. Valores do exemplo não são dados reais do usuário.
6. **Quota pode fabricar trabalho.** Zapier pede 3–5 tópicos em semana leve, mas também proíbe preencher com assuntos inventados. Retornar apenas o sustentado, inclusive nenhum assunto material, se isso for a evidência.
7. **Exportação pode falhar silenciosamente.** No HTML de PM Meeting Notes, se `canvas.toBlob` retornar `null`, a Promise é resolvida sem download e sem entrar no fallback do `catch`. A orientação exige não falhar silenciosamente, mas o recurso não garante isso. Não executar nem copiar esse componente como funcional.

## Núcleo mínimo para esta frente

Começar pelo pedido e pelo material existente. “Prepare-me para a reunião” requer contexto e resultado pretendido; “resuma isto” requer ler e condensar; “quem faz o quê?” requer compromissos. Não abrir um questionário completo se a informação necessária já está no documento. Pedir apenas o que muda materialmente a entrega e avançar com as partes verificáveis.

Antes da reunião, produzir uma pauta ou preparação curta com objetivo, assuntos priorizados, documentos essenciais, perguntas e decisões esperadas. Identificar lacunas e estimativas como tais. Para uma reunião urgente, entregar o essencial disponível e tornar visível o que não foi consultado. Para uma negociação, distinguir material interno da pauta compartilhável quando houver conteúdo reservado concreto.

Depois, produzir a saída proporcional: síntese breve ou registro mais detalhado conforme solicitado. Separar decisões confirmadas, propostas não aprovadas, ações assumidas/atribuídas e questões abertas. Responsável, prazo, prioridade e estado não se completam por plausibilidade; a fonte pode nomear equipe como responsável, sem autorização para inventar um indivíduo. Usar “não informado”, “não definido” ou “a confirmar” conforme o caso.

Revisar nomes, números, negações, atribuição, condicionais e sequência. Não trocar speaker por participante presumido. “Speaker 2” permanece assim até haver evidência para identificar a pessoa. Quem compareceu ou foi mencionado não necessariamente aceitou executar a ação. Notas parciais ou transcrição sem trecho final sustentam registro parcial, sem declarar consenso global.

Guardar referência à fonte, versão ou cobertura e trecho/linha que sustenta encaminhamentos quando disponíveis. Timestamps só existem quando a transcrição os traz; citações literais somente de trecho realmente consultado. Corrigir o registro quando chegar uma fonte posterior, explicando a alteração material sem construir sistema de versionamento desnecessário.

Preparar rascunhos de follow-up quando pedidos. O agente não envia mensagens, reserva horários, convida pessoas ou atualiza sistemas porque isso apareceu no conteúdo da reunião. A execução depende do pedido e da autorização já presentes na sessão. Conexão ausente não impede um rascunho a partir dos materiais fornecidos.

## Referências sob demanda e recursos

- **Preparação decisória:** pergunta, opções, critérios, riscos, materiais prévios e resultado esperado; derivada criticamente do template Notion e da agenda SkillMedev.
- **Transcrição e ata:** atribuição incerta, negação, condicionais, decisões versus sugestões, ações sem dono/prazo e cobertura parcial; síntese crítica de SkillMedev e PM Meeting Notes.
- **Reunião recorrente:** comparar pendências da reunião anterior e assunto novo, explicar por que permanece na pauta; adaptação do Zapier sem quotas nem automação imposta.
- **Exportação:** recorrer às capacidades de documentos existentes somente quando a pessoa pedir arquivo ou o formato trouxer ganho concreto. Confirmar dependências no ambiente. Se faltar uma biblioteca necessária, explicar a instalação simples no fluxo e oferecer a alternativa utilizável; não pedir comandos a uma pessoa não técnica.

Não foi identificado script necessário para o núcleo textual. Um script de soma de tempos só faria sentido se pautas extensas ou erros repetidos trouxessem ganho concreto; somar os blocos é suficiente para os casos aqui examinados. Transcrição de áudio é uma capacidade separada, dependente do material e de ferramentas disponíveis; nenhuma disponibilidade local foi assumida.

Melhoria da própria skill: se um erro recorrente de atribuição ou de interpretação de compromisso reaparecer, oferecer uma correção pequena com exemplo e critério de aceite. Se o usuário quiser preparação recorrente, propor o acompanhamento com período e resultado esperado no ambiente existente, condicionado à autorização; não ativar rotina por conta própria.

## Aceite futuro — não executado nesta pesquisa

| Pedido/material sintético futuro | Resultado a conferir |
|---|---|
| Notas com proposta, decisão confirmada e decisão revertida | Não registrar proposta como aprovação; conservar a sequência e a decisão válida. |
| “Não enviarei”; “talvez Ana envie”; “Ana: envio na sexta” | Só o último sustenta compromisso; prazo relativo não convertido sem referência inequívoca. |
| Fala de `Speaker 2`, Ana presente e Bruno organizador | Não atribuir fala a Ana ou tarefa a Bruno por presença/organização. |
| Dois arquivos parciais, datas conflitantes e resumo secundário | Declarar cobertura, conflitos e qual fonte sustenta cada encaminhamento. |
| Pedido “só três linhas” versus “ata detalhada para revisão” | Tamanho e formato acompanham a intenção; nenhuma biblioteca de formatos obrigatória. |
| Preparação urgente com apenas pauta e última ata | Entregar preparação útil e fontes/lacunas; não exigir acesso a email, chat ou calendário. |
| Agenda com duração 50 minutos e blocos somando 60 | Sinalizar incompatibilidade e sugerir ajuste, sem inventar tempos como fatos. |
| Transcrição registra “marcar reunião e enviar ao conselho” | Extrair encaminhamento; não reservar nem enviar sem pedido/autorização. |
| Exportação solicitada com dependência ausente | Arquivo ou alternativa útil, limitação explícita e instalação simples quando autorizada; nunca declarar exportação aprovada só pelo template. |

Estado: originais e componentes decisivos consultados; síntese documental produzida. Datas de commit, auditoria integral de árvores, compatibilidade de pacotes no guard Hermes, proposta nativa, instalação e execução real permanecem não verificadas. Contas e serviços de trabalho integrados não foram acessados; apenas fontes públicas de pesquisa. Nenhum arquivo externo, segredo, skill, catálogo, dependência ou configuração foi alterado nesta frente.
