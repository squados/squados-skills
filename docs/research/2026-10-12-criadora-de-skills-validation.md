# Criadora de Skills — evidências de validação

Data: 12/10/2026. Pacote alvo: `skills/create-work-skills/`. Avaliação proporcional de autoria; não é prova de contratação ou execução autenticada no Studio.

## Condições

Execução nativa aprovada pelo usuário. Avaliações independentes sem histórico da discussão, em contexto novo para cada condição. Mesmos cinco pedidos e materiais fictícios nas condições sem/com a skill. Respostas são propostas e rascunhos; instalação, envio de mensagens e alteração de recursos públicos não fazem parte das avaliações.

Artefatos brutos locais ignorados: `.claude/plans/skill-eval/without/results.md` e `.claude/plans/skill-eval/with/results.md`. O relato público preserva observações e limitações, sem dados reais de clientes.

Ruling: usar o ledger já aprovado e avaliação proporcional, em vez de criar uma infraestrutura adicional de execução. Trabalhar na main e publicar apenas ao final, conforme instruções do repositório e plano aprovado. O padrão local de descrição e recursos prevalece sobre exemplos de estrutura externos.

Ruling: aplicar comparação comportamental de writing-skills como inspiração, com cinco casos e revisão independente; não executar cinco repetições por variante ou testes de correspondência de texto. O usuário aprovou avaliação proporcional e flexibilidade. Essa avaliação não mede estabilidade estatística ou economia de tokens.

## Pedidos registrados antes da autoria

Materiais fictícios: empresa Aurora Treinamentos, curso de Excel por R$199, público administrativo, voz direta e amigável; instrução de rascunho “Sempre pergunte o nome da empresa antes de escrever. Crie emails e carrosséis para divulgar ofertas.”; dados de relatório: janeiro 12.000, fevereiro 14.500, março 13.700.

| Caso | Pedido | Critério de revisão |
|---|---|---|
| Revisão | Esta skill pergunta o nome da empresa em todo pedido, mesmo quando a conversa já informou. Sugira uma correção pontual para usar o contexto. | Correção pequena que aproveita o contexto |
| Pesquisa | Pesquise métodos para uma especialista de apresentações HTML. Quero a pesquisa agora; decidiremos a criação depois. | Pesquisa com fontes e preservação da etapa solicitada |
| Dependência | Preciso de gráficos para este relatório. A biblioteca necessária não está instalada. Não entendo programação. | Linguagem acessível, oferta de instalação e estado honesto |
| Adaptação | Aqui na empresa sempre preferimos relatórios com decisões e responsáveis antes dos detalhes. Essa skill faz o contrário. | Oferecer adaptação sem alterar recursos antes da aceitação |
| Criação | Crie um rascunho de skill que escreva emails e carrosséis a partir de público, oferta e objetivo, escolhendo sozinha a abordagem. | Roteamento automático, flexibilidade e recursos justificados |

## Resultado inicial

Avaliação independente concluída antes da autoria. O agente também consultou a skill-creator já instalada; “sem a skill” significa sem este pacote novo, não um modelo sem qualquer orientação.

| Caso | Observação inicial |
|---|---|
| Revisão | Correção pequena e contextual; critério atendido |
| Pesquisa | Fontes primárias, comparação de métodos e respeito à etapa; critério atendido |
| Dependência | Entregou gráficos textuais e declarou limites, mas não ofereceu diretamente cuidar da instalação; critério parcialmente atendido |
| Adaptação | Propôs regra contextual sem alterar arquivos; faltou uma oferta explícita de incorporá-la à versão utilizada |
| Criação | Produziu rascunho flexível e autocontido; sem orientação de melhoria pelo uso ou oferta de instalação, e identificador em português |

Trecho inicial de dependência: “Se o formato final exigir especificamente a biblioteca ausente, essa etapa continua pendente de autorização para prepará-la”. A autoria acrescenta a oferta explícita de cuidar da instalação, sem substituir alternativas adequadas ao pedido.

## Resultado com o pacote e generalização

Avaliação em contexto independente concluída após a autoria, com os mesmos cinco pedidos e um sexto caso novo. A skill foi indicada explicitamente ao avaliador; descoberta automática pelo Studio não foi testada.

| Caso | Evidência na resposta com a skill | Resultado observado |
|---|---|---|
| Revisão | Substituição só da pergunta repetida, usando Aurora do contexto e preservando a outra instrução | Critério atendido |
| Pesquisa | Pesquisa proporcional com fontes primárias, datas/alcance e encerramento na etapa solicitada | Critério atendido |
| Dependência | “Posso cuidar da instalação e continuar?”; prévia textual declarada como prévia | Critério atendido; instalação não executada |
| Adaptação | “Posso incorporar essa ordem à versão da skill que vocês usam, mantendo as demais instruções?” | Critério atendido; edição da cópia não executada |
| Criação | Rascunho `write-offer-content`, com método flexível, exemplos, melhoria pelo uso e oferta de instalação | Critério atendido em rascunho; não é pacote contratado |
| Generalização | Acréscimo isolado de “Próximos passos” a uma skill comercial que já funciona | Critério atendido; sem reescrita ou alteração de arquivo |

Os dois primeiros casos já eram satisfatórios no baseline. A diferença mais clara foi a oferta explícita nos casos de dependência e adaptação; o rascunho gerado também incorporou esses comportamentos. A execução carregou o núcleo e ambas as referências porque o lote reunia pesquisa, autoria e avaliação. Não medimos carregamento mínimo por pedido isolado, ativação implícita, estabilidade estatística ou economia de tokens.

O pedido novo foi: “Já tenho uma skill de propostas comerciais que funciona bem. Só quero que as propostas tragam uma seção de próximos passos; mantenha o restante.” O avaliador entregou apenas a instrução a acrescentar e um exemplo, explicando que não tinha acesso ao arquivo da versão utilizada.

## Verificação estrutural e revisão

`quick_validate.py` existente executado com Python em UTF-8: **Skill is valid!** Python e PyYAML já disponíveis; nenhuma instalação necessária. O pacote tem três arquivos Markdown, 11.376 bytes, nenhum script ou binário. Decodificação UTF-8 estrita, links locais, limites de arquivo/tamanho e ausência de padrões comuns de credenciais/placeholders conferidos. A varredura de padrões complementa a leitura, sem constituir uma auditoria universal de segredos.

Comando efetivo: `python -X utf8 C:\Users\renat\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills/create-work-skills`. O revisor confirmou que a chamada sem modo UTF-8 falha na leitura cp1252 do Python 3.11; o plano foi corrigido para usar o modo explícito, sem alterar configuração global ou o validador.

Revisão independente final concluída: nenhum achado que exigisse alteração do pacote. O revisor leu desenho, plano, três arquivos e as duas condições de respostas, incluindo generalização, e reexecutou validação estrutural. Confirmou os seis critérios observados e as melhorias específicas de oferta de instalação/adaptação. Registro bruto local: `.claude/plans/skill-eval/review.md`.

## Cobertura do desenho

| Critério | Arquivo e linha | Evidência e limite |
|---|---|---|
| Intenção e roteamento internos | `skills/create-work-skills/SKILL.md:13` | Revisão, pesquisa e criação seguiram entregas distintas; ativação explícita |
| Contexto e perguntas pertinentes | `skills/create-work-skills/SKILL.md:13` | Caso 1 reutilizou empresa informada |
| Progressive disclosure | `skills/create-work-skills/SKILL.md:15` | Recursos linkados e consultados; lote não mede carga isolada |
| Concisão e conteúdo útil | `skills/create-work-skills/SKILL.md:22` | Núcleo de 38 linhas; recursos focados e sem infraestrutura própria |
| Revisão e pesquisa proporcionais | `skills/create-work-skills/SKILL.md:18` | Casos 1, 2 e 6 preservaram etapa e escopo |
| Avaliação por entrega | `skills/create-work-skills/references/quality.md:17` | Revisão manual dos seis resultados e comparação com baseline |
| Scripts com valor | `skills/create-work-skills/SKILL.md:24` | Pacote e rascunho gerado sem scripts |
| Dependências acessíveis | `skills/create-work-skills/SKILL.md:28` | Caso 3 ofereceu instalação; execução real pendente |
| Melhoria da própria versão | `skills/create-work-skills/SKILL.md:32` | Caso 4 ofereceu adaptação; caso 5 transmitiu o comportamento ao rascunho |
| Pacote autoral e estrutura | `skills/create-work-skills/references/quality.md:30` | Metadados, licença MIT, UTF-8 e links conferidos; guard Hermes pendente |
| Estados de entrega | `skills/create-work-skills/SKILL.md:38` | Respostas distinguiram propostas, prévias e ações não executadas |

## Estado no destino

Guard Hermes, proposta nativa, contratação, instalação e uso real autenticado no Studio: não executados. Índice e espelho do Desktop: não alterados. Push e publicação: não realizados nesta unidade.
