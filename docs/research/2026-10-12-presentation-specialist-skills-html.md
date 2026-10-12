# Especialista em Apresentações — pesquisa de produção HTML

Data de consulta: 12/10/2026. Frente: formato HTML, composição, navegação, adaptação de tela, exportação, portabilidade e QA. Narrativa e métodos profissionais pertencem às outras frentes. Este dossiê pesquisa componentes para uma futura skill; não instala pacotes nem produz um deck.

## Recomendação

Adotar HTML/CSS/JavaScript simples como caminho inicial para apresentações de escritório: permite arquivo local, visual próprio e nenhuma etapa de build. Aproveitar a arquitetura de palco de `frontend-slides`, a disciplina de conteúdo e contexto de `claude-design` e critérios de navegação/exportação documentados por Reveal e Slidev. Adaptar tudo à intenção real: apresentação projetada pede composição estável; leitura no celular pode pedir recomposição. O agente escolhe a menor abordagem suficiente sem exigir que a pessoa saiba escolher framework.

Reveal.js, Slidev e Marp são alternativas úteis quando resolvem uma necessidade concreta — notas e visão de apresentador, código interativo, fonte Markdown recorrente, exportação estabelecida — ou quando já fazem parte do material recebido. Não devem virar dependência universal só porque existem. Uma apresentação bonita também precisa texto legível, conteúdo verdadeiro, imagens pertinentes e arquivo utilizável no destino.

## Alcance e evidência

Buscas combinaram `frontend-slides`, `HTML presentation SKILL.md`, `reveal`, `slidev`, `marp`, `claude-design Hermes` e `openai/skills slides`. A skill `find-skills` orientou a descoberta; pesquisa web e originais GitHub substituíram o CLI de instalação. Seis SKILL.md originais foram lidos integralmente, mais recursos determinantes abaixo. Outros dez candidatos/linhagens foram triados por página, README ou resultado de busca; não contam como leitura profunda nem evidência independente.

SHA foi obtido por `git ls-remote` e confirmado pelo acesso a recursos imutáveis. Datas abaixo são do commit de referência, extraídas da página GitHub desse commit, não datas de lançamento da skill. API GitHub anônima estava limitada; não se usaram credenciais. As leituras completas de frontend-slides foram divididas em trechos por limite de saída. O exemplo Marp foi relido integralmente após uma primeira saída truncada.

| Pacote original / autoria verificável | Revisão de referência e data visível | Licença / limite | Arquivos efetivamente lidos |
|---|---|---|---|
| [frontend-slides — Zara Zhang](https://github.com/zarazhangrui/frontend-slides/tree/9906a34d640d2111f724544cbc50f7f130569ae1) | `9906a34d640d2111f724544cbc50f7f130569ae1`, 23/06/2026, 13:08:18 −07:00 | LICENSE MIT, copyright 2025 Zara Zhang | SKILL.md completo; html-template.md; viewport-base.css; animation-patterns.md; STYLE_PRESETS.md; scripts/export-pdf.sh; LICENSE. Biblioteca bold-template-pack e conversor PPTX não auditados. |
| [claude-design — BadTechBandit / NousResearch](https://github.com/NousResearch/hermes-agent/tree/ff2d02f998f9f9e45543eea30fb935f47e4504a7/skills/creative/claude-design) | `ff2d02f998f9f9e45543eea30fb935f47e4504a7`, commit 13/10/2026, 01:11:36 +05:30 = **12/10/2026, 19:41:36 UTC** | Frontmatter declara MIT e autor BadTechBandit, versão 1.1.0. Não transforma prompts hospedados da Anthropic em ativos com direitos automaticamente comprovados. | SKILL.md completo. A referência é o repositório vivo Hermes, não uma afirmação de que esse SHA já está empacotado no Desktop. |
| [revealjs — Glaucia Lemos](https://github.com/glaucia86/skills/tree/e0a3ce68fcd9ff42105931155e1171b77be86fa9/revealjs) | `e0a3ce68fcd9ff42105931155e1171b77be86fa9`, 25/08/2026, 11:17:45 −03:00 | LICENSE MIT, copyright 2026 Glaucia Lemos | revealjs/SKILL.md completo; references/advanced-features.md completo; LICENSE. Busca retornou caminho antigo `skills/revealjs/`; consulta atual confirmou pasta na raiz. |
| [slidev — projeto Slidev / Anthony Fu](https://github.com/slidevjs/slidev/tree/73053ab2b9653ed475960301b56e1ce4439d9c75/skills/slidev) | `73053ab2b9653ed475960301b56e1ce4439d9c75`, commit 02/10/2026, 16:30:24 +09:00 | LICENSE MIT, copyright 2020–PRESENT Anthony Fu | SKILL.md completo; references/core-exporting.md, layout-canvas-size.md, build-remote-assets.md completos; LICENSE. Outros índices de recursos não foram lidos integralmente. |
| [create-revealjs-presentations — TriasJ](https://github.com/TriasJ/claude-custom-skills/tree/7f7fd38e91013bce49641f5f9fd3f09fef0a7f38/create-revealjs-presentations) | `7f7fd38e91013bce49641f5f9fd3f09fef0a7f38`, 16/04/2026, 08:39:28 −06:00 | Sem licença no frontmatter, sem LICENSE na árvore raiz consultada e sem licença explícita identificada no README. **Não redistribuir como base licenciada sem resolver.** | SKILL.md completo; scripts/present.js completo; árvore do pacote; README do repo. reference/deployment.md, exigido pelo SKILL, retornou 404 no SHA. Não auditados templates e integrações auxiliares. |
| [marp-slides — robonuggets](https://github.com/robonuggets/marp-slides/tree/7ef93e98bcc728d4c2f0a8ea83b0d1ed8982ceef) | `7ef93e98bcc728d4c2f0a8ea83b0d1ed8982ceef`, 08/04/2026, 11:59:53 +10:00; SKILL updated 2026-04-08, v2.0 | README declara MIT, mas árvore consultada tem apenas README, SKILL e examples; sem arquivo LICENSE ou license no frontmatter. Declaração é evidência menor que aviso completo. | SKILL.md completo; README completo; examples/marp_coffee.md completo. Demais 21 exemplos não auditados. |

Nenhum teste ou instalação dos seis foi executado. Qualidade visual declarada pelos autores e presença de exemplos são sinais de método; não equivalem a demonstração nesta sessão.

## Descoberta complementar e linhagens

| Candidato descoberto | Tratamento nesta frente |
|---|---|
| [dreamid27/frontend-slides](https://github.com/dreamid27/frontend-slides), [wengzige/frontend-slides](https://github.com/wengzige/frontend-slides) | README e descrições reproduzem nome, fases, arquivos auxiliares e arquitetura de frontend-slides; tratados como linhagem derivada, não mais duas provas independentes. Sem auditoria de diferenças. Preferência pelo original Zara Zhang. |
| [duhman/slidev](https://github.com/duhman/slidev) | README declara v52+, núcleo de aproximadamente mil linhas e arquivo compilado. Página indica arquivamento em 20/07/2026. Preferência pelo skill oficial do projeto; não carregar esse núcleo enorme junto. |
| [yoanbernabeu/slidev-skills](https://github.com/yoanbernabeu/slidev-skills), [Zewang0217/slidev-skill](https://github.com/Zewang0217/slidev-skill) | Referências de sintaxe vizinhas. Mesma tecnologia não torna automaticamente fork; não foi provada genealogia. Dedupe funcional: não acumular guias repetidos de Slidev. |
| [claude-office-skills/md-slides](https://github.com/claude-office-skills/skills/tree/main/md-slides) | Markdown/Marp com dependência anunciada de office-mcp; triagem, sem necessidade para o caminho simples. |
| [pagopa/marp-presentation](https://github.com/pagopa/pagopa-platform-integration-test/tree/main/.github/skills/marp-presentation) | Contrato específico do repo, extensão VS Code e render opcional. Referência vizinha, não transferir paths e pressupostos daquele repo. |
| [mordor-forge/slide-deck](https://github.com/mordor-forge/slide-deck) | Preview anuncia uv e watchers Linux/macOS. Não adotar operação Unix/servidor universal no Windows; não se auditou o script. |
| [dro42/presentation-kit](https://github.com/dro42/presentation-kit) | README anuncia escolha entre ferramentas e pré-requisitos sem instalação silenciosa. Útil postura, mas várias ferramentas/agents/hooks custam mais que o pedido simples; pacote não auditado. |
| [OpenAI slides original](https://github.com/openai/skills/tree/e6afb0d74cc75d220df2faf3dd6c635c2dc6a108/skills/.curated/slides) / [JetBrains atribuição de origem](https://github.com/JetBrains/skills/tree/main/slides) | Descoberta confirma foco PptxGenJS, renderização e validação de PPTX. Referência vizinha para QA; não é candidata HTML desta frente. Reexportações OpenAI não contam como autores/soluções independentes. SKILL e scripts desse pacote não auditados aqui. |

## Matriz de componentes

| Fonte/arquivo → componente | Decisão | Motivo e adaptação necessária |
|---|---|---|
| frontend-slides/SKILL.md → identificar criar, converter ou melhorar | **Aproveitar** | Reconhece intenção automaticamente e preserva o existente em edição. Conversão é tarefa específica; não instalar parser PPTX em pedido HTML comum. |
| frontend-slides/SKILL.md → descobrir estética por amostras concretas | **Adaptar** | Uma amostra ajuda quando direção está aberta; três alternativas não são obrigação após identidade já fornecida. Usar conteúdo real no preview; rótulos do processo ficam fora do slide. |
| frontend-slides/SKILL.md → separar fala e leitura pela densidade | **Aproveitar/adaptar** | Inferir pelo pedido, perguntar só quando muda materialmente a entrega. Evitar questionário repetindo duração/audiência já conhecidas. Conteúdo excedente pede divisão ou recomposição, não fonte minúscula. |
| frontend-slides/viewport-base.css → palco 1920×1080 e escala uniforme | **Adaptar** | Bom para projeção/exportação e preservação de layout, mas proporção e tamanho devem respeitar referência e destino. Não impor 16:9 a todo pedido; não chamar miniatura em telefone de leitura responsiva. |
| frontend-slides/html-template.md → CSS/JS embutidos, navegação simples | **Aproveitar/adaptar** | Pouca infraestrutura. Template contém funções de teclado/toque ainda como comentários: são orientação, não controlador pronto demonstrado. Implementar e verificar de fato quando houver deck. |
| frontend-slides/html-template.md → edição inline e localStorage por padrão | **Descartar como obrigação** | Amplia comportamento sem pedido; armazenamento não salva necessariamente o arquivo de origem. Se edição for necessária, explicar diferença e entregar exportação que preserve alterações. |
| frontend-slides/SKILL + STYLE_PRESETS → proibição de fontes de sistema | **Descartar** | Contraria offline e identidade existente. Tipografia deliberada pode ser fonte instalada ou fallback. Fonte remota e licença de fonte exigem verificação específica. |
| frontend-slides/scripts/export-pdf.sh → rasterizar cada slide | **Adaptar, sob demanda** | Pode preservar aparência, perde seleção de texto. Script é Bash, instala Playwright/Chromium dinamicamente, cria HTTP e manipula DOM; não copiar como rotina padrão Windows. Print CSS ou ferramenta existente deve vir primeiro. |
| frontend-slides/animation-patterns.md → CSS transform/opacity e movimento contextual | **Adaptar** | Movimento precisa ajudar leitura. Recurso ainda cita scroll snap/Intersection Observer apesar do núcleo fixo; não juntar paradigmas incompatíveis. Reduzir movimento não basta se elementos continuam invisíveis na impressão. |
| claude-design/SKILL.md → contexto, materiais existentes e conteúdo sem filler | **Aproveitar** | Preserva marca e fatos, evita métricas/testemunhos inventados e ícones sem função. Faltas substantivas são lacunas explicitadas; imagem bonita não substitui evidência. |
| claude-design/SKILL.md → operação CLI, arquivos e ferramentas reais | **Aproveitar** | Remove protocolos do produto hospedado; não promete tool inexistente. Caminho local, CSS/JS simples e verificação correspondente ao que foi realmente feito. |
| claude-design/SKILL.md → dez sinais de estilo genérico | **Adaptar** | Útil crítica de composição antes de trocar cor. Score não é detector objetivo de qualidade; não penalizar Inter, cartões ou gradiente se escolhidos com propósito ou identidade aprovada. |
| claude-design/SKILL.md → persistir slide e Tweaks | **Descartar como obrigação** | Não necessários para todo deck. Preferir navegação previsível e chrome mínimo; opções surgem quando o uso as exige. |
| glaucia86/revealjs/SKILL + advanced-features → navegação, fragments, hash, notas, overview | **Adaptar sob demanda** | Recursos concretos que podem justificar Reveal. Fragments servem à fala, mas podem multiplicar páginas no PDF; notas exigem ambiente adequado. Não carregar highlighter e Notes sem necessidade. |
| glaucia86/revealjs/SKILL → CDN reveal.js@5 “self-contained” | **Descartar essa qualificação** | É um arquivo, mas requer internet e `@5` flutua entre releases. Se online for aceitável, fixar versão exata; para offline distribuir/embutir recursos licenciados e testar sem rede. |
| Slidev/core-exporting → export PDF/PNG e etapas de click | **Adaptar sob demanda** | Ferramenta útil para deck técnico e fluxo existente, requer Node/ecossistema Vue/Vite e navegador de exportação. Não é sem instalação só por a skill ser Markdown. |
| Slidev/core-exporting → PPTX raster e pptx-editable | **Aproveitar como distinção técnica** | SHA atual documenta shapes/texto selecionável no segundo modo, com SVG/canvas/iframe/fórmulas/gradientes/filtros como imagens e fallback por slide; fontes não embutidas. Não afirmar que toda exportação Slidev é raster. PPTX permanece referência vizinha. |
| Slidev/build-remote-assets → cache de imagens externas | **Adaptar** | Cache declarado ajuda build, mas não comprova fontes, vídeos, iframes ou links disponíveis offline. Inventariar a saída e verificar o arquivo/pasta entregue sem rede. |
| TriasJ/SKILL → imagens pertinentes, base64, static fallbacks e atribuição | **Adaptar como conhecimento** | Ideias úteis de entrega portátil e fallback; licença insuficiente impede copiar recursos. Evitar base64 universal para vídeo/grandes mídias. |
| TriasJ/SKILL → fetch-media obrigatório, Gemini, servidor e dois pacotes sempre | **Descartar** | Introduz dependências, chave, fluxo e volume sem benefício em muitos pedidos. Gerar mídia é opcional, explícito e sujeito a ferramentas disponíveis; nunca expor segredo para verificar configuração. |
| TriasJ/SKILL → ler `.env` e imprimir trecho GEMINI | **Descartar** | O próprio exemplo pode revelar chave. Confirmar disponibilidade sem mostrar valor; nenhuma credencial no pacote ou logs. |
| TriasJ/scripts/present.js → servidor local de apresentador | **Não copiar** | Só justificado por notas/apresentador. Leitura estática mostra path montado de URL sem confinamento explícito ao diretório: requer revisão antes de uso. Não se executou nem demonstrou exploração. |
| robonuggets/SKILL + exemplo coffee → SVG/CSS, composição editorial e variedade | **Adaptar** | Técnicas sem biblioteca para gráficos simples. Exemplo é conteúdo de demonstração, não informação cliente. Labels reduzidos e fontes remotas pedem revisão; não universalizar paleta/thin type ou copiar exemplo. |
| robonuggets/SKILL → charts over numbers, gauges/cards por padrão | **Descartar como regra absoluta** | Um número verdadeiro e contextualizado pode ser melhor que gráfico decorativo. Gráfico deve explicar relação real; unidade/período/fonte e escala precisam permanecer visíveis. |

## HTML simples e frameworks: decisão pelo benefício

| Abordagem | Ajuda de verdade quando | Custo/limite | Escolha nesta pesquisa |
|---|---|---|---|
| Arquivo HTML com CSS/JS simples | Deck de trabalho pontual, marca própria, abertura local, entrega sem setup | Navegação e print precisam ser implementados/verificados; recurso externo pode quebrar offline | **Padrão recomendado**, com núcleo curto e referências sob demanda. |
| Reveal.js | Notas/apresentador, overview, pilhas verticais, fragments ou recurso já presente | JS/CSS/plugin como dependências; CDN depende da rede; speaker view exige servidor local em certas condições | Alternativa quando recurso necessário justifica. [Instalação](https://revealjs.com/installation/), [apresentador](https://revealjs.com/speaker-view/), [PDF](https://revealjs.com/pdf-export/). |
| Slidev | Aula/talk técnico com código, Mermaid/math, live demo, autoria Markdown/Vue recorrente | Build, Node/gestor de pacotes, runtime e navegador de exportação; saída SPA não é equivalente a arquivo que abre por file:// | Alternativa técnica/stack existente; [skill oficial no SHA](https://github.com/slidevjs/slidev/tree/73053ab2b9653ed475960301b56e1ce4439d9c75/skills/slidev). |
| Marp | Conteúdo Markdown editável recorrente e render padronizado | CLI/renderer; print estático perde interação; permissões HTML/local files exigem entender a origem | Alternativa editorial recorrente; [projeto oficial](https://marp.app/) e [CLI](https://github.com/marp-team/marp-cli). |

A documentação oficial Reveal foi consultada pela coordenação: instalação básica abre index.html sem build; notas locais exigem servidor; PDF é confirmado para Chrome/Chromium. Slide alto pode ser dividido em mais de uma página e fragments têm páginas separadas por padrão. Esta frente leu a referência advanced-features da skill corroborando parâmetros de print, fragments e navegação; não testou file:// ou servidor.

## Portabilidade, tela e exportação

**Offline real.** Classificar separadamente arquivo único, pasta portátil e dependência online. Procurar `src`, `href`, CSS `url()`/`@import`, fetch/import, fontes, plugins, iframes, mapas e mídia. CSS/JS inline com Google Fonts remoto ainda depende da rede. Imagens em assets tornam a entrega uma pasta; se a pessoa precisa encaminhar um único HTML, embutir imagens apropriadas e recursos permitidos ou explicar o pacote. Fontes precisam fallback e licença; base64 não cria direito de distribuição. Abrir cópia da entrega sem internet é o teste material posterior, não tarefa desta pesquisa.

**Escala e leitura.** `min(viewportWidth/designWidth, viewportHeight/designHeight)` preserva composição. Em 390px de largura, um corpo 28px no palco 1920 vira aproximadamente **5,69px CSS**: cálculo de proporção, não medição renderizada. Mesmo corpo 24px recomendado como mínimo por claude-design vira 4,88px. Assim, layout que “cabe” pode ser ilegível. Para apresentação ao vivo, preservar palco e revisar na tela/projetor; para leitura em telefone, simplificar/recompor conteúdo, permitir zoom acessível ou derivar leitura contínua quando esse for o destino. Não impor versão móvel extra a todo pedido.

**Navegação.** Teclado, botões visíveis simples e toque quando relevante; contador ou seção para orientação; foco claro. Não capturar Space/arrows durante digitação ou interação de formulário. Não depender de hover para controles móveis. Notas de apresentador são úteis conforme ocasião, não obrigatórias nem proibidas universalmente. Notas no arquivo HTML são acessíveis a quem recebe o arquivo, mesmo escondidas na tela; decidir a entrega conforme público.

**Print/export.** Uma página por slide exige @page, dimensões/margens, quebra, remoção de transform e controle de visibilidade; revelar conteúdo animado e esconder chrome. O viewport-base.css de frontend-slides faz vários desses passos, mas não inclui @page, e apenas torna `.slide` visível: elementos `.reveal` podem continuar ocultos se não forem tratados. Seu export-pdf.sh força `.reveal` por outro mecanismo e rasteriza. Essa leitura indica risco concreto a corrigir numa implementação posterior, não falha executada.

PDF estático não preserva interação; páginas de etapas podem ser desejáveis para fala ou indesejáveis para circulação. Conferir ordem, contagem, fontes, fundos, gráficos, seleção de texto quando pedida, links e peso final. Existência do PDF é verificação insuficiente. Impressão direta costuma ser mais simples; automação do navegador só entra quando exportação/QA repetida ou fidelidade exige. Não prometer layout, seleções ou edição perfeita em conversão para PowerPoint.

**Dados e visuais.** Rótulos diretos, unidades, período e fonte; eixo/escala apropriados, sem distorção por transformação SVG; dados fictícios identificados como exemplo, nunca usados como prova. Screenshot real de produto pode ser mais pertinente que ilustração sintética. Reservar área para legendas e fonte antes de encaixar imagem; se preciso, dividir slide. Fonte do ativo, autoria, licença e condição de uso vão ao registro de entrega pertinente, não só a notas escondidas.

## QA útil para a futura skill

Núcleo deve pedir verificação proporcional, com evidência precisa, sem impor script/gate pesado a toda entrega:

1. Conferir conteúdo real, identidade e leitura sequencial dos títulos; remover lacunas não assumidas e placeholders não desejados.
2. Abrir a entrega salva, conferir erros e navegação essencial; testar primeiro/último slide e elementos interativos.
3. Inspecionar **todos** os slides na tela principal, incluindo longos títulos, tabelas e gráficos. Verificar clipping e sobreposição: scrollHeight sozinho não detecta painéis cobrindo outros.
4. Testar tamanho secundário quando prometido — celular quando leitura móvel é requisito, proporção diferente quando projeção importa. Legibilidade é avaliada após escala, não pelo número no CSS de origem.
5. Para entrega offline, testar arquivo/pasta final sem rede e fora dos paths de desenvolvimento. Para PDF pedido, inspecionar resultado renderizado, contagem e conteúdo final de fragments.
6. Reportar o que foi produzido e o que foi verificado; navegador indisponível é limite declarado. Não trocar evidência visual por promessa de qualidade, sem exigir captura a pedido meramente textual.

Scripts só se repetição, conversão complexa ou necessidade de execução os justificar. Um verificador pode checar recursos ausentes e overflow; não substitui olhar os slides e entender dados. Não construir bibliotecas/engines próprias para esse trabalho agora.

## Organização recomendada da futura versão própria

- **SKILL.md conciso:** reconhecer criar/converter/editar; aproveitar contexto; definir entrega/público/destino; decidir menor abordagem; trabalhar conteúdo e sistema visual; produzir artefato completo; verificar e entregar com limitações reais.
- **references/html-presentations.md:** palco versus reflow, teclado/foco/toque, print, fontes/assets, offline e fronteiras de notas. Carregar quando HTML é confirmado, não durante toda pesquisa de assunto.
- **references/export-and-quality.md:** PDF, fragments, checklist visual e ferramentas condicionais. Carregar quando exportar ou validar demanda esses detalhes.
- **Referências de framework opcionais:** consultar documentação/versionamento quando framework recebido ou recurso requerido justificar. Não reunir catálogo gigante de sintaxe no núcleo.
- **templates/scripts:** acrescentar somente depois que repetição real ou execução demandar; exemplos curtos neutros servem melhor que 22 decks ou uma biblioteca bold inteira.

Não exigir que a pessoa forneça todos os detalhes antes de começar. O agente infere intenção e aproveita os materiais, perguntando apenas sobre decisões que afetam substancialmente a apresentação. Dependência ausente pode ser explicada assim: “Para mostrar suas notas em uma segunda tela, preciso preparar um pequeno recurso local de apresentação; o HTML simples continua abrindo diretamente.” Ou: “Posso entregar o arquivo que abre no navegador sem instalar nada; para gerar automaticamente o PDF com esse layout, preciso preparar o recurso de exportação.” Isso explica benefício e custo em linguagem de trabalho; não obriga o usuário a executar comandos.

O pacote textual da futura skill deve respeitar ≤100 arquivos, ≤4 MiB UTF-8 e pastas admitidas (`references/`, `templates/`, `scripts/`, `assets/`), conforme instruções locais. Esses limites pertencem à **contratação da skill**, não ao deck do cliente gerado depois. Não empacotar navegador, fonte binária, imagem/MP4 nem node_modules na skill para “garantir tudo”. Dependências do artefato podem ser opcionais, com preparação real demonstrada quando requerida; não afirmar que o Studio traz ferramentas não verificadas. Autoria e avisos legais preservados se houver adaptação licenciada.

## Lacunas e estado

Dúvidas materiais resolvidas: HTML simples versus framework, origem dos seis métodos, distinção offline/CDN, palco versus leitura móvel, notes/apresentador e print/export, necessidade de progressive disclosure e QA real. Riscos decisivos de fontes/scripts identificados por leitura, não por execução.

Não realizado: auditoria de todos os arquivos/bibliotecas/templates dos candidatos; execução de decks ou scripts; instalação de dependências; chamadas pagas; pesquisa em contas privadas; publicação, gallery, criação da nova skill, commit ou push. Licença de TriasJ permanece lacuna para redistribuição e robonuggets pede preservação/clarificação do aviso antes de cópia substancial. Essa lacuna não impede usar conhecimento técnico e documentação oficial para compor uma versão própria, com escopo adaptado e sem copiar pacote.

O SHA Hermes usa data local UTC+05:30 no dia seguinte; a conversão acima evita apresentar fonte futura por comparação simplista da data civil. Datas não equivalem a implantação no Desktop.
