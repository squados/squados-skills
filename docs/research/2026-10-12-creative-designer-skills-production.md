# Designer de Criativos — produção, carrosséis e exportação

Pesquisa em 12/10/2026, somente leitura HTTP e de arquivos. Não houve instalação, geração paga, execução dos pacotes, mudança do harness, publicação ou implementação da skill. Esta frente complementa direção de arte e métodos profissionais; não define três skills separadas.

## Seleção e revisão verificável

Cinco SKILL.md originais foram lidos integralmente, em três repositórios. Os três Baoyu têm a mesma autoria e componentes repetidos: constituem uma linhagem, não três confirmações independentes. Diretórios e busca serviram à descoberta; as decisões abaixo vêm das fontes originais. Canvas-design ficou para a frente de direção de arte. Mikefluff/carousel-builder e social-media-skills/carousel-writer foram encontrados, mas não receberam leitura integral nem são evidência decisiva desta frente.

| Origem | Revisão consultada e data do commit | Licença consultada | Papel |
|---|---|---|---|
| Jim Liu, `JimLiu/baoyu-skills` | `1567581c26ec29f4216c6e6835415bf30343b0e3`, 10/09/2026 | [MIT na raiz](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/LICENSE) | Séries de cards, infográficos, operação de imagens |
| Malik Idrees, `idrsdev/social-carousel-generator` | `44e6ee5979864a21fd9e47425fcd6fa8242bfe99`, 05/04/2026 | [MIT na raiz](https://github.com/idrsdev/social-carousel-generator/blob/44e6ee5979864a21fd9e47425fcd6fa8242bfe99/LICENSE) | Composição HTML/CSS e exportação PNG |
| OpenAI, `openai/skills` | `49f948faa9258a0c61caceaf225e179651397431`, 24/06/2026 | [Apache-2.0 no pacote imagegen](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/imagegen/LICENSE.txt) | Geração, edição e referências raster |

Datas são dos commits do repositório, não atestados de manutenção individual. SHA fixo permite repetir a leitura; disponibilidade de modelos e direitos sobre imagens de entrada não foram comprovados pela licença da skill. Se houver incorporação literal futura, preservar avisos e identificar modificações; a síntese metodológica não exige redistribuir os pacotes.

## Componentes comparados

### 1. Baoyu XHS Images

Fonte: [SKILL.md](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-xhs-images/SKILL.md). Recursos lidos: `references/elements/canvas.md` e `references/workflows/prompt-assembly.md`.

| Componente → contribuição | Decisão e motivo |
|---|---|
| Estratégias narrativa, informativa e visual → séries com progressão diferente | Adaptar ao objetivo do pedido; não gerar três alternativas sempre |
| Layout × estilo × paleta → separar estrutura da estética | Aproveitar a distinção, sem catálogo obrigatório de presets |
| Prompt salvo por card e referência visual comum → consistência e revisão localizada | Adaptar: referência aprovada conforme seu papel; capa não é sempre a melhor âncora |
| Setup bloqueante, confirmação repetida, limites de cards e percentuais fixos → previsibilidade | Descartar como regra universal; perguntas somente quando faltam decisões materiais |
| Proibição global de HTML/SVG e texto sempre desenhado → unidade raster | Descartar no designer amplo; composição determinística atende texto exato e fonte de marca |

As regras de área segura são específicas de XHS. O prompt-base contém nome de provedor e estética desenhada mesmo com escolha flexível no núcleo. Exige tradução e remoção dessas amarras na síntese, sem transferir alegações de engajamento.

### 2. Baoyu Infographic

Fonte: [SKILL.md](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-infographic/SKILL.md). Recursos lidos: `references/structured-content-template.md` e `references/layouts/binary-comparison.md`.

| Componente → contribuição | Decisão e motivo |
|---|---|
| Dados → estrutura visual → rótulos exatos → prompt | Aproveitar a separação; bom para comparação, processo e oferta com números |
| Preservação literal de dados, citações e instruções do cliente | Aproveitar para dados e copy aprovada; adaptação editorial somente quando o pedido autoriza |
| Relação entre tipo de informação e layout | Adaptar como raciocínio, sem exigir rótulo de template |
| Objetivos de aprendizagem, tom de professor e 3–5 combinações sempre | Descartar como padrão de anúncio; muitos pedidos não são educativos |
| Toda produção depende de gerador raster | Adaptar; infográfico com valores exatos pode usar HTML/SVG e exportar PNG |

É método documentado, não prova de render correto. Não herdar a restrição de copiar literalmente todo conteúdo quando a pessoa pede condensação; proteger as partes cujo significado e redação não podem mudar.

### 3. Baoyu Image Gen

Fonte: [SKILL.md](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-image-gen/SKILL.md). Recursos lidos: `references/providers/codex-cli.md`, `scripts/providers/codex-cli.ts` e `scripts/codex-imagegen/validator.ts`.

| Componente → contribuição | Decisão e motivo |
|---|---|
| Papéis de referências e preservação de identidade | Aproveitar: não substituir produto/pessoa por descrição genérica |
| Tarefas salvas, retomada e resultado por item | Adaptar apenas quando lote justificar; script só se reduzir erros ou trabalho |
| Chave de API versus login do produto | Aproveitar a distinção; nenhum deles comprova disponibilidade no Studio |
| Muitos provedores, retries, cache e wrapper que inicia `codex exec` | Descartar da base; custo de dependências sem necessidade demonstrada |

O validador inspecionado verifica tamanho e assinatura PNG, não decodificação completa ou qualidade. O wrapper documenta flags ignoradas e limites de referência; não se deve prometer tamanho exato por uma flag. Claims de latência e modelos permanecem claims upstream, sem benchmark ou contrato de serviço verificado nesta pesquisa.

### 4. Social Carousel Generator

Fonte: [SKILL.md](https://github.com/idrsdev/social-carousel-generator/blob/44e6ee5979864a21fd9e47425fcd6fa8242bfe99/skills/social-carousel-generator/SKILL.md). Lidos todos os recursos do pacote: schema, JSON exemplo, pipeline, setup de fontes, gerador exemplo e dois scripts de fontes; também a licença.

| Componente → contribuição | Decisão e motivo |
|---|---|
| Tokens de marca + HTML/CSS/SVG → screenshot de elemento PNG | Adaptar; texto editável, dimensões controláveis e composição previsível |
| Fontes locais incorporadas → render sem CDN | Adaptar com formato, glifos e licença conferidos |
| Templates com números decorativos, fontes, paleta e dimensões fixos | Descartar como estilo obrigatório |
| Instalação global e `--break-system-packages` | Descartar; verificar ambiente e oferecer preparação explicada ao não desenvolvedor |

Leitura revelou inconsistências: verificador fixa Inter/Caveat apesar de aceitar fontes customizadas; downloader sobrescreve a mesma chave por peso sem preservar `unicode-range`; exemplo declara TTF enquanto instruções usam WOFF2. São riscos identificados por código, sem reprodução. A espera fixa de 900 ms e `overflow:hidden` não comprovam fontes prontas ou ausência de corte. O caminho interessa; copiar o gerador inteiro não é recomendação.

### 5. OpenAI Imagegen

Fonte: [SKILL.md](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/imagegen/SKILL.md). Recursos lidos: `references/prompting.md`, `references/cli.md` e licença integral. Inventário inspecionado: assets PNG/SVG, script Python, referências e configuração de agente; script Python e receitas extensas não foram auditados.

| Componente → contribuição | Decisão e motivo |
|---|---|
| Novo asset versus edição; imagem de estilo versus alvo | Aproveitar; evita trocar indevidamente o original |
| Texto literal, invariantes e uma alteração por iteração | Aproveitar para fidelidade e controle de revisão |
| Prompt proporcional à especificidade da pessoa | Aproveitar; não inventar slogans, objetos ou cores quando o pedido já é preciso |
| Salvar o escolhido no projeto e inspecionar resultado | Aproveitar como entrega utilizável |
| Tool nativo versus CLI com chave | Adaptar ao runtime real; o Codex disponível nesta conversa não comprova serviço equivalente no Desktop |

A CLI é alternativa explicitamente distinta na fonte. O pacote inclui `agents/` e PNG binário: sua estrutura original não demonstra compatibilidade direta com a contratação atual do Hermes.

## Síntese recomendada para a futura skill única

As decisões abaixo são inferências de projeto, não features já implementadas ou resultados medidos.

1. Reconhecer se a pessoa quer peça isolada, série, adaptação de tamanho, variante ou correção. Aproveitar copy, marca e assets presentes; inferir o óbvio e perguntar apenas pelo que muda a entrega.
2. Escolher a técnica pela necessidade: composição HTML/SVG para texto preciso, diagramas e identidade controlada; geração/edição de imagem para fotografia, ilustração e alterações raster. Combinação de fundo gerado com texto composto é uma técnica legítima quando escolhida desde o início, diferente de prometer que um gerador entregou sozinho todo o resultado.
3. Escolher estrutura e expressão visual independentemente, mantendo liberdade fora de templates. Não importar quotas de estilos, quantidade de slides ou proporção de espaço vazio.
4. Em séries, usar uma ficha visual curta e referência coerente; em identidade de produto/pessoa, priorizar assets originais. As fontes divergem sobre referência gerada: não unir cadeia obrigatória de capa com proibição universal de referência gerada.
5. Produzir arquivo realmente utilizável e preservar fonte editável ou prompts quando ajudam revisão. Preview inline não substitui arquivos persistidos quando a pessoa pediu um pacote.
6. Verificar capacidades instaladas antes de escolher ferramenta. Se faltar algo necessário, explicar a necessidade e oferecer a instalação/preparação pelo agente; não pedir ao não desenvolvedor que execute terminal nem instalar vários provedores preventivamente.

## Qualidade e evidência de aceite

Estes são critérios propostos para execução futura. Nenhum foi exercitado nesta pesquisa.

| Critério | Evidência necessária |
|---|---|
| Exportação | Abrir/decodificar cada final; conferir dimensões, formato, transparência quando pedida e arquivos efetivamente entregues |
| Corte e overflow | Inspecionar render final e limites do layout; conferir texto, produto, logo e CTA em cada adaptação, sem confiar em `overflow:hidden` |
| Tipografia PT-BR | Fontes efetivamente carregadas, peso e formato corretos, acentos e símbolos presentes; leitura na escala de uso |
| Contraste | Conferência de texto real e fundo; medição quando aplicável, sem transformar ratio num selo de legibilidade de toda a arte |
| Fidelidade | Comparar visual e copy com material aprovado; números, preço, condições, nome e URL não podem derivar durante geração |
| Consistência | Revisar a série lado a lado e cada card em tamanho útil; referência comum não garante identidade |
| Variantes | Mudança identificável ligada a hipótese criativa; alterar apenas cor não comprova um teste de conceito |
| Evidência comercial | Aprovação visual é separada de CTR, conversão e receita; os pacotes não demonstram resultado de campanha |

Antes de exportação HTML, aguardar fontes e imagens de forma verificável em vez de tempo arbitrário; não incluir textos do cliente como HTML cru. Crop deve ser conferido por destino e pedido, não importado de outro canal. OCR pode apoiar a checagem, mas resultado visual continua sujeito a revisão.

## Pacote, artefatos e limites

O adaptador descrito nas instruções locais aceita UTF-8, até 100 arquivos e 4 MiB, em pastas específicas; isso vale para **o pacote instalado**, não para os PNG/PDF/JPEG produzidos no trabalho. Não colocar fontes binárias, imagens de exemplo ou browser dentro da skill nem codificar binários em base64 para contornar o propósito do limite. Licença de script não resolve licença de fonte, fotografia, produto ou marca.

Baoyu e idrsdev não pertencem à allowlist `github` da galeria atual. Pesquisá-los e aprender métodos é possível; publicação direta no índice e reempacotamento exigem decisões e validações próprias. Esta frente não inspecionou o adaptador atual do Desktop; os limites acima vêm das instruções do repositório, não de validação de contratação nesta execução.

O núcleo futuro deve conter intenção, escolha técnica, fidelidade e revisão. Referências sob demanda podem cobrir carrosséis, geração/edição e exportação. Um script de exportação/checagem só entra depois de demonstrar vantagem em pedido real; nada nesta leitura exige framework, manifest universal ou biblioteca de dezenas de templates.

Lacunas restantes: render no Studio/Hermes, suporte real de referências na ferramenta escolhida, fonts/glyph coverage, dependências e locks disponíveis, licença dos assets do cliente, crop do destino quando não fornecido e avaliação de campanha. Pesquisa suficiente para decidir componentes; insuficiente para declarar pacote distribuível ou Designer funcionando.
