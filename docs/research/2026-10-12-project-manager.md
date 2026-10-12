# Gerente de Projetos — síntese da pesquisa

Rodada 26 do catálogo aprovado; consulta em 12/10/2026. Pesquisa para uma skill própria de uso interno em projetos de negócios. Nenhum pacote individual foi criado, instalado ou executado; nenhum projeto de cliente foi alterado.

## Alcance e recomendação

Consolidar planejamento e acompanhamento proporcionais: resultado esperado, entregas verificáveis, sequência factível, previsão atual e decisões necessárias. Um pequeno projeto pode caber em um documento. Reconhecer pelo pedido se a pessoa precisa planejar, revisar datas, recuperar um projeto, avaliar mudança ou apresentar status; aproveitar seus materiais e práticas existentes.

As três frentes autorizadas produziram:

- [Skills de planejamento](2026-10-12-project-manager-skills-planning.md): sete SKILL completos de sete famílias, 30 arquivos integrais incluindo recursos/licenças e duas leituras parciais.
- [Skills de controle](2026-10-12-project-manager-skills-control.md): dez SKILL completos de cinco famílias, dezoito recursos determinantes e quatro licenças.
- [Métodos e casos](2026-10-12-project-manager-methods.md): dezessete URLs decisivas, níveis de acesso discriminados, materiais recentes e três casos autorais.

Takusaotome/project-manager aparece nas duas frentes, no mesmo pin: contar uma vez. Resultado consolidado: **dezesseis SKILL distintos de onze famílias**, e não dezessete soluções independentes. As contagens de recursos das frentes têm licença compartilhada e não devem ser somadas como arquivos únicos. Forks, integrações e traduções internas não aumentam a evidência. Os exemplos publicados não demonstram desempenho real.

Na metodologia, APM change control foi conferida novamente pela coordenação; Teal Book capítulo 8 também. Uma fonte adicional, [GAO-26-107629](https://files.gao.gov/reports/GAO-26-107629/index.html), de 04/06/2026, foi lida seletivamente: highlights e tabelas 5/9. São **dezoito URLs metodológicas contando essa conferência adicional**, sem duplicar APM/Teal Book. Nenhuma gravação ou transcrição foi consumida; páginas editoriais, Q&A e metadados de vídeo estão separados de audiovisual assistido.

## Componentes que merecem entrar

| Componente e referência | Escolha para a futura skill | Razão prática |
|---|---|---|
| JayRHa: decomposição e estimativas; GAO: qualidade do cronograma | Adaptar entregas, precedência, esforço, duração, calendário e disponibilidade | Datas precisam corresponder ao trabalho e à capacidade; esclarecer a lacuna que altera a previsão |
| Peter Bamuhigire: implantação operacional | Adaptar aquisição, verba, acesso, continuidade e aceite quando pertinentes | Assinar contrato e liberar recurso são condições distintas; evitar aplicar fases de startup a todos os projetos |
| Kesslernity: registros com evidência e classificação | Síntese conceitual própria de riscos, problemas, premissas e dependências | Ocorrência confirmada pede ação; hipótese ou ausência de informação não significa aprovação |
| Mohit: comunicação dirigida à decisão | Adaptar consequência, alternativas e decisão necessária à audiência | Relatório útil mostra o que muda e quem precisa decidir; periodicidade e tamanho seguem o pedido |
| APM: mudança da referência aprovada | Analisar efeitos, alternativas e autoridade dentro do contexto fornecido | Uma previsão atualizada e uma alteração do compromisso aprovado são operações distintas |
| Teal Book: proporcionalidade e informação concisa | Aproveitar o princípio, sem transportar governança pública | Evitar estrutura maior que o projeto e recursos que ninguém utiliza |
| Takusaotome: valor agregado | Somente sob demanda, com PV/EV/AC comparáveis e regra de medição | Índice de valor não é atraso em dias; denominador ausente impede o cálculo |
| Yysun: fatos antes da narrativa | Usar distinção conceitual e preservar histórico relevante | Linguagem por audiência pode mudar; fatos e evidência de aceite precisam permanecer |

O [capítulo de adaptação do Teal Book](https://projectdelivery.gov.uk/teal-book/home/part-b-tailoring-and-adopting/chapter-8-tailoring/), atualizado em julho/2026, trata métodos e informação proporcionais ao contexto. Seu regime governamental não vira obrigação para empresas. A auditoria GAO de 2026 ilustra como vínculos incompletos, datas sem realizado e baseline incompleta comprometem previsões; não obriga implantar uma estrutura de auditoria em cada projeto.

## Divergências e falhas que orientam a escolha

O código [critical_path.py de JayRHa](https://github.com/JayRHa/AgentSkills/blob/7ce3d8d6af7ca3905c688c649000b98e8e57db4a/project-planner/scripts/critical_path.py) foi conferido integralmente pela coordenação, sem execução. `critical_chain` reúne todos os nós sem folga; a apresentação encadeia essa lista como caminho. Para A/B independentes de duração 2 e C de duração 1 depois de ambos, a cadeia A→B→C inventa uma relação: existem A→C e B→C. O modelo também não inclui calendário ou capacidade. Não incorporar o script como calculadora pronta.

No [project_health_check.py de Takusaotome](https://github.com/takusaotome/claude-skills-library/blob/b542ac73ab54a40299a9f407b0ebdb425d107e96/skills/project-manager/scripts/project_health_check.py), a coordenação conferiu os trechos de cálculo/entrada: SPI/CPI retornam 1 se seus denominadores não forem positivos. Defaults podem ainda converter informação ausente em diagnóstico de qualidade/equipe. Mostrar lacunas; não tratar ausência como desempenho satisfatório. A divergência de campos do exemplo e demais falhas está discriminada no dossiê de controle.

Mohit apresenta classificação contraditória entre score e heatmap; notas ordinais não são probabilidades medidas. KISS aceita Approved sem aprovador e normaliza impacto inválido para baixo. Kesslernity inicia um exemplo de decisão desconhecida como acordada. Esses componentes ajudam a selecionar verificações, mas seus automatismos não merecem ser transplantados.

Descartar do padrão: certificações/experiência fictícias da persona, reservas percentuais universais, Scrum obrigatório, comitê universal, rituais de perguntas ou quatro arquivos obrigatórios, semáforo sem base, visual Gantt apresentado como planejamento validado. Uma data planejada passada não prova execução; esforço gasto não prova entrega aceita; entrega aceita não prova benefício alcançado.

## Organização enxuta proposta

O núcleo reconhece o trabalho, aproveita materiais, explica pressupostos relevantes e entrega o formato necessário. Referências sob demanda podem reunir planejamento/cronograma/capacidade, acompanhamento/riscos/mudanças e encerramento/benefícios. Essa divisão orienta conteúdo; não exige criar três arquivos nem mostrar modos ao usuário.

Não há ganho demonstrado para incluir scripts no primeiro desenho. Cálculos repetitivos ou redes maiores podem justificá-los depois, com modelo declarado, validação de entradas e caminhos reais. Dependências ausentes seguem a oferta simples de instalação com a autorização disponível. Preferências recorrentes ou atritos podem motivar oferta de adaptação da própria skill; não transformar o calendário ou alçada de uma empresa em padrão público.

## Casos de avaliação futura e conferências

Os [três casos autorais](2026-10-12-project-manager-methods.md) usam calendário explicitamente fornecido e projetos fictícios. A coordenação conferiu soma de horas, dias úteis e custo incremental com Python local próprio; nenhum código externo ou skill foi executado.

1. Planejamento: 60 h-pessoa; B/C disputam Ana. Sequência com capacidade de 4 h/dia e fechamento em 02/11 termina em 09/11/2026, dez dias úteis inclusivos. A rede sem restrição de capacidade produziria prazo inviável de 06/11.
2. Mudança: tradução exige 8 h e serviço de R$400. Acréscimo 8×150+400 = R$1.600, 16% sobre R$10.000; fim condicionado em 11/11, dois dias úteis depois. A solicitação continua pendente e a baseline preservada.
3. Acompanhamento: ausência comprovada desloca a previsão para 10/11, um dia útil depois da baseline. Aviso de possível indisponibilidade permanece risco, sem probabilidade inventada; tradução pendente não entra no compromisso autorizado.

## Proveniência, acesso e estados pendentes

Pins, arquivos e licenças estão nos dossiês. Kesslernity usa CC-BY-SA-4.0, conferida pela coordenação; não copiar seus templates para um pacote MIT. Yysun não teve licença identificada. Wayland declara Apache no frontmatter em repositório identificado AGPL, com proveniência pendente. GAO pack distingue conteúdo governamental de tooling; não presumir domínio público global nem licença para figuras de terceiros. Síntese autoral e links preservam a separação entre curadoria e autoria.

Pesquisa resolve componentes e critérios; ainda faltam desenho final, pacote, avaliações com agente, compatibilidade/guard Hermes, proposta revisável, instalação e uso real no Studio. Sem push, galeria ou espelho alterados. PMBOK completo, livros comerciais e materiais audiovisuais permanecem não consultados; nenhuma chamada paga vidIQ foi feita.
