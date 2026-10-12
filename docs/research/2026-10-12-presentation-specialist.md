# Especialista em Apresentações — síntese da pesquisa

Consulta em 12/10/2026. Resultado aprovado: apresentações bonitas e utilizáveis em **HTML** para trabalho de negócios. Esta rodada prepara criação posterior, sem gerar deck, instalar pacotes ou alterar a galeria.

## Alcance e fontes

- [Narrativa, audiência e direção](2026-10-12-presentation-specialist-skills-narrative.md): dez SKILL.md completos de oito repositórios, 22 recursos de comportamento, dois README e sete LICENSE.
- [Produção HTML](2026-10-12-presentation-specialist-skills-html.md): seis SKILL.md completos de seis origens e recursos determinantes; dez candidatos/linhagens adicionais apenas triados.
- [Métodos profissionais](2026-10-12-presentation-specialist-methods.md): doze fontes decisivas, sete profissionais/institucionais e cinco técnicas; duas transcrições de 2025, uma reutilizada da pesquisa de Dados; três casos fictícios.

Total: **16 SKILL.md principais de 14 origens**. As três skills Aaron Vanston pertencem à mesma família. Forks e diretórios não contam como novas provas; SlideSage credita fontes externas de estilos, cujo conteúdo não recebeu automaticamente a licença do port. Revisões, datas, autoria, recursos lidos e limites estão nos dossiês.

As transcrições foram lidas, sem reprodução audiovisual. Nenhum vídeo de 2026 com conteúdo suficiente foi confirmado nesta frente. Pesquisa não demonstra execução dos pacotes, qualidade de um deck produzido ou eficácia numa reunião real.

## Recomendação

Combinar **audiência e mensagem do ppt-prepare, evidência e títulos do SoWhat Decks, aprendizagem do SlideSage, densidade e direção visual de deck.md/Aaron, arquitetura simples de frontend-slides e disciplina de conteúdo do claude-design**. Usar métodos profissionais para situar as escolhas e documentação técnica para verificar o HTML.

A pessoa pede apresentação, melhoria, síntese ou adaptação de público; a skill identifica intenção e aproveita materiais. A finalidade — decidir, informar, propor ou ensinar — é diferente da condição de consumo — fala ao vivo ou leitura autônoma. A combinação dessas duas dimensões orienta estrutura e densidade, sem menus de modos ou formulário obrigatório.

HTML/CSS/JavaScript simples é o caminho inicial recomendado quando resolve a entrega. Reveal, Slidev e Marp entram por recurso necessário, recorrência ou material já recebido; não como dependências universais. Direção visual deve ter intenção própria, adequada à marca e ao conteúdo, sem tema escuro tecnológico, gradiente ou imagem obrigatória por slide.

## Componentes e decisões

| Componente | Fontes | Decisão e motivo |
|---|---|---|
| Contexto e audiência | ppt-prepare, communication-storytelling | **Aproveitar/adaptar:** identificar quem precisa decidir/entender e que prova ajuda. **Descartar:** oito gates e confirmação de decisões rotineiras. |
| Mensagem e argumento | SoWhat, ppt-prepare, slide-deck-builder | **Aproveitar:** mensagem central, cadeia de títulos e corpo que sustenta a afirmação. **Descartar:** título persuasivo que excede a evidência. |
| Abertura | SoWhat, Duarte, Cole | **Adaptar:** síntese e decisão cedo para executivos; contexto mínimo quando falta entendimento. **Descartar:** nunca começar com pedido ou sempre criar suspense. |
| Densidade e ritmo | deck.md, Aaron, ppt-prepare | **Adaptar:** fala, leitura e prática pedem densidades diferentes. Uma conclusão principal pode precisar de vários dados. **Descartar:** palavras/minutos/slides como limites universais. |
| Treinamento | SlideSage, CDC | **Aproveitar:** objetivo observável, pré-requisitos, exemplo, prática e feedback quando ajudam. **Descartar:** pitch ou entretenimento obrigatório. |
| Sistema visual | deck.md, Aaron, frontend-slides, claude-design | **Adaptar:** hierarquia, contraste, alinhamento e variedade de composição por função. Espaço vazio pode ser intencional; não preencher por obrigação. |
| HTML e navegação | frontend-slides, Reveal, Hermes | **Adaptar:** arquivo/pasta mínima, percurso previsível, teclado e foco. **Descartar:** editor inline, persistência e servidor por padrão. |
| Proporção e leitura | frontend-slides, Slidev | **Adaptar:** palco estável para projeção; recomposição ou leitura contínua quando outro destino exigir. Layout que cabe não prova texto legível. |
| Portabilidade | Reveal, frontend-slides, TriasJ | **Aproveitar conceito:** conferir recursos externos e pacote entregue. **Descartar:** chamar CDN ou fontes remotas de offline; base64 universal e setup com chave sem necessidade. |
| Exportação | Reveal, Slidev, frontend-slides | **Adaptar sob demanda:** usar recurso disponível, verificar saída e preservar conteúdo. **Descartar:** exportar sempre e presumir fidelidade/edição pelo formato. |
| QA | SoWhat, SlideSage, W3C/MDN | **Aproveitar:** verificar significado, evidência, leitura e operação reais. **Descartar:** pontuação terminal, média autoatribuída ou ausência de overflow como selo de qualidade. |

## Divergências resolvidas

**Conclusão cedo e contexto:** o [artigo atual de Nancy Duarte](https://www.duarte.com/blog/how-to-effectively-present-to-senior-executives/) e a [entrevista de Cole](https://techleadjournal.dev/episodes/207/) ajudam a adaptar a ordem à audiência. O leitor deve entender a utilidade cedo; a escolha não pede suspense artificial, ocultação de riscos ou uma regra única de abertura.

**Uma mensagem e vários dados:** separar quando a audiência precisa alternar tarefas mentais ou a composição perde legibilidade. Uma comparação de cenários pode exigir dois blocos e várias métricas para provar uma única conclusão. Não dividir automaticamente por subitem, nem reduzir texto para manter um número arbitrário de slides.

**Arte e evidência:** imagens, diagramas e gráficos precisam ajudar a entender ou dar presença visual pertinente. Dados, condições e riscos continuam íntegros. Não fabricar números, cases, logos, compromissos ou ROI para preencher estrutura. A cadeia de títulos deve continuar verdadeira quando lida sem o corpo.

**Arquivo local e recursos avançados:** a documentação [Reveal instalação](https://revealjs.com/installation/) permite setup básico sem build, enquanto [speaker view](https://revealjs.com/speaker-view/) exige servidor no uso local desse recurso. Não presumir que tudo funciona por abertura direta. O agente cuida da preparação necessária quando autorizada; a pessoa não precisa escolher framework ou executar comandos.

**Offline e portabilidade:** arquivo único, pasta portátil e dependência online são estados diferentes. A proibição de fontes de sistema do frontend-slides conflita com portabilidade; fontes e assets remotos precisam tratamento explícito. Notas escondidas no HTML continuam acessíveis a quem recebe o arquivo: não tratá-las como proteção de confidencialidade.

**Exportação editável e estática:** [Slidev core-exporting no SHA consultado](https://github.com/slidevjs/slidev/blob/73053ab2b9653ed475960301b56e1ce4439d9c75/skills/slidev/references/core-exporting.md) distingue PPTX raster de `pptx-editable`, com texto/shapes e fallback parcial; fontes não são embutidas. PPTX é formato vizinho, sem substituir o HTML aprovado. [Reveal PDF](https://revealjs.com/pdf-export/) documenta Chrome/Chromium, slides altos em múltiplas páginas e fragments separados por padrão. Não prometer export perfeito sem conferir o resultado.

## Conferências e avaliação posterior

A coordenação leu os três dossiês e conferiu documentação Reveal e exportação oficial Slidev. A conta de escala é direta: `28 × 390/1920 ≈ 5,69 px`. É ilustração matemática de corpo reduzido, sem render executado. A legibilidade deve ser avaliada na condição prometida, e não só pelo tamanho declarado no CSS de origem.

A frente HTML identificou por leitura risco de impressão com `.reveal` oculto, dependência de Bash/instalação no exportador frontend-slides, referência obrigatória ausente e exemplo que pode revelar credencial em TriasJ. Não importar esses componentes sem revisão; nenhuma exploração ou execução foi feita. As competências de leitura, exportação e segurança do pacote completo continuam sem prova.

Os [casos fictícios](2026-10-12-presentation-specialist-methods.md) orientam avaliação prática futura:

- Diretoria: pedido de piloto com custo, prazo e risco preservados; decisão clara e detalhe acessível, sem garantia ou ROI inventado.
- Proposta de treinamento: seis encontros, 30 pessoas e R$ 24 mil, sem desenvolvimento; HTML compreensível enviado e usado em reunião, com condições e lacunas visíveis.
- Treinamento de procedimento: objetivo observável, exemplos, prática e explicação das respostas conforme material recebido; sequência compatível com o tempo.

No HTML real, conferir todo o percurso, primeiro/último slide, slides densos, gráficos, tabelas, foco e controles. Revisar tela secundária quando prometida; recursos/fontes/assets, arquivo entregue e eventual impressão precisam inspeção própria. CSS de impressão, contraste e teclado têm [orientação técnica nos métodos](2026-10-12-presentation-specialist-methods.md), sem constituir certificação integral de acessibilidade. Nenhum deck desses casos foi produzido nesta etapa.

## Núcleo e referências

Núcleo futuro: reconhecer pedido/audiência/consumo, aproveitar materiais, estruturar mensagem e prova, definir direção visual, produzir HTML e revisar conteúdo/uso. Recursos sob demanda: síntese executiva; propostas; treinamento; evidência e gráficos; direção visual; HTML/navegação/portabilidade; exportação e QA. A bibliografia fica nos dossiês, fora da skill executável.

Scripts/templates só depois de benefício concreto: exportação repetida, conversão ou checagem mecânica que evite erro. Não importar engine narrativo, biblioteca de estilos inteira ou runtime de outro produto. Ferramenta necessária ausente: explicar resultado que permite e oferecer instalação/preparação simples ou alternativa suficiente, usando autorização existente.

Quando uma preferência recorrente ou atrito justificar, oferecer adaptar a própria versão — por exemplo, marca, vocabulário, estilo de apresentações de referência ou organização de reuniões da equipe. Aplicar com aceitação ou pedido, preservando contexto individual fora do padrão público. Essa capacidade não pede menu de configuração nem reescrita automática a cada apresentação.

## Autoria, licenças e estado

MIT foi lida em várias origens narrativas e técnicas; licenças e avisos concretos estão discriminados nas frentes. lyndonkl e TriasJ têm licença indefinida nos caminhos consultados; robonuggets declara MIT no README sem aviso completo localizado. Estilos derivados do SlideSage requerem cadeia de origem própria. Hermes claude-design declara MIT no frontmatter; upstream vivo não comprova versão empacotada no Desktop. Nenhuma dessas constatações autoriza copiar assets ou mudar fontes permitidas da galeria.

As referências profissionais foram sintetizadas com links, sem redistribuir livros, transcrições, imagens ou PDFs. Antes de adaptação substancial, verificar licença específica e preservar avisos. Limites do pacote textual da galeria são diferentes dos arquivos gerados no trabalho; não embutir navegador, node_modules ou fontes binárias no pacote para prometer execução.

Pesquisa registrada, ainda sem skill nova, deck, instalação, proposta Hermes, aprovação, uso real no Studio ou publicação. Temporários de leitura em `.scratch/reports-research` e `.scratch/presentation-narrative` permanecem fora do commit: remoções nativas foram rejeitadas pela revisão automática, sem contorno. Isso não bloqueia a pesquisa; não representa limpeza concluída.
