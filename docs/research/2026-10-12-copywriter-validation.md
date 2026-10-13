# Copywriter — evidências de avaliação local

Data: 12/10/2026. Execução nativa aprovada pelo usuário com “ok”. [Desenho](../superpowers/specs/2026-10-12-copywriter-design.md) e [plano com entradas A–F](../superpowers/plans/2026-10-12-copywriter.md) definem o pacote e os critérios. Todos os dados e destinos dos casos são fictícios.

## Método e limites

Avaliação no harness Codex desta sessão, com subagentes de contexto novo, modelo herdado e instruções gerais do ambiente. Não é execução no Hermes/Studio. Controle recebe apenas os pedidos A/D, sem leitura de pacote, desenho ou pesquisa; tratamento terá acesso explícito ao SKILL e às referências escolhidas. Isso observa encaminhamento após carregamento, sem demonstrar descoberta implícita.

Respostas são julgadas por fatos, condições, voz, utilidade e proporcionalidade, sem nota de conversão. Não há cegamento, aleatorização, amostra estatística, medição de tokens ou dados comerciais reais. Outras orientações gerais do ambiente podem influenciar o controle; ele não representa um modelo sem instruções.

## Tarefa 1 — controle observado antes da autoria

Agente `copywriter_control`, sem herança de conversa, recebeu os dois pedidos exatos. Foi orientado a não consultar arquivos/skills nem usar ferramentas; declarou uso exclusivo do texto fornecido. Nenhuma pergunta feita. O pacote ainda não existia.

### Resposta A

> Olá, Joana.
>
> Passando aqui para te lembrar que as inscrições para a nossa oficina de planilhas estão abertas até 20/10.
>
> O valor é R$ 490, e a turma começa em 27/10. Serão quatro encontros ao vivo para praticar fórmulas e organizar relatórios.
>
> Se quiser participar, você pode se inscrever em https://example.com/oficina.
>
> Um abraço, Equipe Farol.

**Conferência:** preservou preço, datas, quatro encontros, conteúdo, destino e tom. A edição foi localizada, sem perguntas ou novo escopo. Resultado satisfatório no critério do caso; nenhuma falha fabricada para justificar a skill.

### Resposta D

| Slide | Texto observado |
|---|---|
| 1 | Está no estoque. Mas está disponível? Antes de prometer uma entrega, confira os dois saldos. |
| 2 | Saldo físico. É a quantidade de produtos que está fisicamente no estoque. |
| 3 | Saldo disponível. Considera as unidades reservadas e outras restrições que possam impedir a venda. Um produto reservado pode continuar no estoque físico. |
| 4 | Na prática: 100 unidades físicas − 20 unidades reservadas = 80 unidades disponíveis. Isso se não houver outras restrições. |
| 5 | Reserva não significa saída física. Antes de prometer a entrega ao cliente, confira quanto está disponível. |

Legenda observada: “Ter 100 unidades no estoque físico não significa ter 100 unidades disponíveis para vender. Se 20 estiverem reservadas, a disponibilidade será de 80 unidades, desde que não haja outras restrições. As unidades reservadas podem continuar fisicamente no estoque. Antes de prometer uma entrega, confira o saldo disponível.”

**Conferência:** cálculo, unidades, condição e reserva/saída preservados. Texto por slide e legenda utilizáveis, sem número imposto pelo pedido. Resultado satisfatório. O controle já resolve esses dois pedidos; a avaliação posterior pode mostrar manutenção de qualidade, sem alegar melhoria causal.

## Tarefa 2 — pacote escrito

Commit `5099825`: quatro arquivos, 13.439 bytes UTF-8; núcleo de 43 linhas e referências de 29/30/29 linhas no primeiro estado. `quick_validate.py` retornou `Skill is valid!`. Links locais, contagem/tamanho e HEAD foram conferidos. Esses checks cobrem estrutura, sem provar execução no Studio.

## Tarefa 3 — respostas observadas com pacote

Agentes novos `copywriter_eval_text` e `copywriter_eval_formats`, sem herança de conversa, receberam A/B/E e C/D/F respectivamente. Ambos leram o núcleo, escolheram referências e declararam não consultar pesquisa, desenho, plano ou gabaritos. Leram instruções gerais do ambiente. As três respostas de cada agente compartilham contexto dentro do grupo; isso limita o isolamento de cada caso.

Não editaram arquivos, usaram web, instalaram dependências ou acessaram destinos. Não fizeram perguntas. A coordenação leu as respostas completas; os trechos e medidas relevantes ficam registrados abaixo, sem atribuir resultados comerciais aos exemplos.

| Caso | Leitura declarada | Resultado observado e julgamento inicial |
|---|---|---|
| A | Núcleo, sem referência adicional necessária | Apenas divisão de parágrafos; todas as palavras, preço, datas, conteúdo e destino preservados. Satisfatório |
| B | Núcleo + pages-and-offers | Página com título, público, conteúdo, duração, condições e CTAs. Sem provas/garantias fabricadas. Há uma nota editorial sobre renda/resultados dentro da copy; atrito a corrigir abaixo |
| C | Núcleo + ads-and-social | Três peças com texto da arte, legenda, destino e diferença: conferir antes de prometer, entender movimentações, enxergar saldo físico. Claims limitados às funcionalidades informadas. Satisfatório |
| D | Núcleo + ads-and-social | Cinco slides e legenda; cem/vinte/oitenta e qualificador no slide do cálculo; reserva separada de saída. Satisfatório |
| E | Núcleo + emails | Dois contatos: continuar a prática e conferir adequação/condições; assunto, preview, corpo, CTA e voz direta. Sem envio/automação ou comportamento de clique inventado. Satisfatório no critério do caso |
| F | Núcleo | Receitas informadas 2.000/1.200; relações 2/1,5 e gasto por pedido 50/66,67. Não chamou diferença receita/gasto de lucro ou atribuição de fato. Satisfatório |

### Trechos de A e D: comparação com controle

A manteve o texto original, distribuindo-o em parágrafos. Explicação observada: “Ajustei apenas a divisão dos parágrafos para facilitar a leitura. O texto já estava claro; mantive as palavras, a oferta e o tom aprovados.” O controle também preservou condições e tom; o tratamento foi mais conservador nas palavras, mas isso não demonstra superioridade geral.

D apresentou a mesma distinção do controle em cinco slides. Slide do cálculo: “100 unidades físicas − 20 unidades reservadas = 80 unidades disponíveis. Se não houver outras restrições.” A legenda manteve a condição e explicou que as vinte unidades não necessariamente saíram. Ambos atenderam aos critérios. Nenhum ganho causal, de performance ou tokens foi demonstrado.

### B: página entregue e atrito editorial

Título observado: “Pratique fórmulas e organize seus relatórios com a Oficina Farol”. Apoio: quatro encontros para iniciantes administrativos, prática de fórmulas e relatórios. Condições: quatro encontros de duas horas, oito horas totais, R$ 490, início 27/10 e inscrições até 20/10; CTAs em `https://example.com/oficina`.

O desenvolvimento explicou a relação entre fórmula/dados e estrutura/leitura do relatório, sem renda, depoimentos, escassez, gravações ou software específicos inventados. “Você não precisa dominar fórmulas para participar” é interpretação da adequação a iniciantes, sem ampliar a oferta para ausência total de pré-requisitos.

Atrito observado: “A proposta é aprender e praticar; o curso não promete aumento de renda ou resultados comerciais.” A ausência de prova precisava limitar o argumento, mas não exigia anunciar essa lacuna no texto de venda. O produto não deve expor observações internas de autoria quando não ajudam a decisão do leitor. Ajuste proposto: orientar notas de evidência/produção fora da peça, preservando condições que mudam a decisão. A página continua a precisar de julgamento editorial; cumprimento factual não garante persuasão.

### C: variantes efetivas

- Conferir antes de prometer: abertura “Seu cliente perguntou: ‘Tem para entrega?’”; ação de conferir saldo e reserva, com CTA de demonstração.
- Entender movimentações: “O saldo mudou. Confira as movimentações”; histórico como foco, com CTA de demonstração.
- Enxergar saldo físico: “Quanto há no estoque da sua loja?”; consulta direta, sem cenário de ruptura inventado.

Legendas mantiveram funcionalidades e destino. O agente informou que diferenças são hipóteses editoriais, sem escolher vencedor por performance não medida.

### E: função e voz

Email 1: assunto “Depois da aula, continue a prática de planilhas”; preview com temas e quatro encontros; corpo relaciona aula conhecida à próxima prática e apresenta condições. Email 2: assunto “A Oficina Farol é para quem está começando”; preview sobre público, temas e tempo; corpo organiza “Primeiro, o público”, “Depois, o conteúdo”, “Por fim, o tempo”. Ambos têm CTA/destino e preservam dados. Não houve alegação de clicar, comprar ou automação configurada.

### F: cálculo e limite

O agente calculou valor total de pedidos X = R$ 2.000, Y = R$ 1.200; valor/gasto = 2,0/1,5; gasto/pedido = R$ 50/R$ 66,67. A diferença R$ 1.000/R$ 400 foi explicitamente separada de lucro. Como atribuição não foi fornecida, tratou a relação como cálculo sobre dados informados, sem ROAS confirmado ou retorno incremental.

Cenário adicional condicionado: se pedidos válidos/pagos/atribuídos e mesma base de receita, margem de contribuição necessária para cobrir gasto de campanha = 50%/66,67%, antes de custos fixos. Aritmética conferida pela coordenação; não é recomendação de campanha, lucro observado ou prova comercial.

## Correção e caso novo G

O núcleo passou a orientar: “Deixe notas de produção e lacunas editoriais em observações à equipe; na peça, inclua condições que mudam a decisão do leitor.” A correção atende ao atrito B sem proibir esclarecimentos relevantes ao público ou exigir disclaimer universal.

Agente novo `copywriter_eval_followup`, sem herança, recebeu somente o pacote e este pedido, sem leitura dos resultados ou gabarito:

> Escreva uma página comercial curta para o serviço fictício Catálogo em Ordem. Entrega: cadastrar títulos, descrições e atributos de até cinquenta produtos usando informações fornecidas pela loja; revisão com o responsável da loja incluída. Preço R$ 900; prazo de cinco dias úteis depois do recebimento dos dados completos. Público: donos de pequenas lojas. Não temos depoimentos nem indicadores de vendas ou economia de tempo medidos. Objetivo: solicitar proposta em https://example.com/catalogo. Quero texto pronto para a página.

Resposta de página observada:

> **Catálogo em Ordem — Os produtos da sua loja, com as informações no lugar**
>
> Cadastramos títulos, descrições e atributos de até 50 produtos, usando as informações fornecidas pela sua loja. A revisão com o responsável da loja está incluída.
>
> Um serviço para donos de pequenas lojas que precisam organizar o cadastro dos produtos e conferir se as informações representam o que oferecem.
>
> **O que está incluído:** cadastro dos títulos, descrições e atributos de até 50 produtos; uso das informações que sua loja fornecer; revisão com o responsável da loja.
>
> **Como funciona:** você fornece os dados completos dos produtos. Nós fazemos o cadastro e revisamos as informações com o responsável da loja.
>
> Preço: R$ 900. Prazo: cinco dias úteis após o recebimento dos dados completos.
>
> **Solicite uma proposta para sua loja:** precisa organizar o cadastro dos seus produtos? Solicite uma proposta para o Catálogo em Ordem. Solicitar proposta: https://example.com/catalogo.

Observações de referências, perguntas e limites ficaram depois de um separador, fora da peça. Não apareceu aviso sobre ausência de depoimentos/indicadores no texto comercial. Escopo, limite de produtos, preço, condição do prazo e ação preservados; nenhum resultado ou garantia inventado. Nenhuma pergunta antes da entrega; plataforma e dados para uso real foram apontados como refinamento posterior.

Leitura declarada: núcleo e pages-and-offers, além de instruções gerais. Sem web, edição, instalação ou publicação. Resultado satisfatório no caso novo. Isso comprova o comportamento observado em G após o ajuste; B original não foi reexecutado e não há demonstração estatística de generalização.

## Verificação contra o desenho

Referências `arquivo:linha` relativas à raiz do repositório; linhas conferidas na versão final do pacote.

| Critério | Estado e evidência |
|---|---|
| Metadados, idioma e contrato textual | ✅ `skills/copywriter/SKILL.md:1`; nome/pasta coincidentes, MIT, descrição 91 caracteres; quatro Markdown/13.575 bytes, UTF-8 e links locais válidos; validador retorna `Skill is valid!` |
| Contexto e intenção, sem menu | ✅ `skills/copywriter/SKILL.md:11`; A–G resolveram o trabalho sem perguntas dispensáveis; escolhas de referências declaradas |
| Revisão proporcional e preservação | ✅ `skills/copywriter/SKILL.md:15`; A preservou palavras/condições; D preservou unidade, cálculo e qualificador |
| Fatos, prova e voz | ✅ `skills/copywriter/SKILL.md:25`; B/C/E/G sustentaram oferta/funcionalidades, sem depoimentos ou resultados inventados; E adaptou voz direta |
| Produção por formato | ✅ `skills/copywriter/references/pages-and-offers.md:23`, `skills/copywriter/references/emails.md:26`, `skills/copywriter/references/ads-and-social.md:13`; peças observadas incluem campos solicitados |
| Progressive disclosure e custo | ✅ encaminhamento em `skills/copywriter/SKILL.md:17`; A/F sem referência específica necessária, B/G páginas, C/D social, E emails. Agentes agruparam leituras em um contexto: não prova isolamento de carregamento por pedido nem economia de tokens |
| Notas de autoria separadas | ✅ `skills/copywriter/SKILL.md:35`; atrito B registrado, correção e caso G satisfatório |
| Ferramenta ausente/adaptação pelo uso | ✅ instruções em `skills/copywriter/SKILL.md:39` e `skills/copywriter/SKILL.md:41`; revisão estática. Oferta/instalação e edição da cópia não foram simuladas nem executadas nesta unidade |
| Fronteira com análise, sem bloqueio artificial | ✅ `skills/copywriter/SKILL.md:39`; F ajudou com cálculos sustentados e declarou lucro/atribuição desconhecidos |
| Guard, contratação, instalação e uso no Studio | ❌ pendentes; não confundidos com validação local |
| Conversão, eficácia comercial, estabilidade e tokens | ❌ não demonstrados por estes casos |
| Galeria, espelho e publicação | ❌ etapa final do catálogo; não executada |

## Estado desta unidade

Autoria, controle A/D, seis pedidos com pacote e um caso novo após correção observados. Verificação estrutural final executada. Revisão independente aprovou o conteúdo local; instalação, guard/proposta Hermes, uso real e publicação permanecem posteriores.

## Revisão independente final

Agente fresco `copywriter_review`, GPT 5.6 Sol/high, tier máximo indicado pela matriz local Codex; sem participação na autoria, read-only e sem subdelegação. Comparou base `eb557f1` ao pacote `5099825`, além da correção no worktree e evidência A–G. Leu quatro arquivos e requisitos, conferiu formato, links e validador.

Veredito: **APPROVE para o conteúdo atual do pacote**. Zero Critical, Important abertos ou Minor. Único Important observado — nota editorial dentro da copy B — resolvido pelo ajuste em `SKILL.md:35` e evidência G. B original não foi repetido. Nenhuma sugestão menor foi diferida.

Declined to judge: ativação/descoberta implícita, guard/proposta/contratação/instalação, pedido real no Studio, resultados comerciais/estabilidade/tokens, galeria/espelho/publicação e auditoria exaustiva de similaridade/licenças de todas as fontes. A coordenação mantém essas etapas como pendentes ou não demonstradas; nenhum arquivo externo foi incorporado ao pacote. A síntese autoral consultou a pesquisa, sem alegar auditoria integral de direitos.

## Decisões de execução

- Ruling: registro no plano/ledger/evidência e checks nativos substituem wrappers Bash, worktree e runner novos. Motivo: Windows/main, pacote documental e plano aprovado enxuto. Custo se inadequado: menos automação de acompanhamento; compensação: evidência persistida, verificação de arquivos/links e HEAD após cada commit.
- Ruling: controle A/D satisfatório não será tratado como RED nem como prova de ganho. Motivo: resultado observado, permitido pelo plano e padrão de autoria aprovado. Custo: benefício incremental da skill permanece não demonstrado.
- Ruling final: estados que o revisor não julgou ficam fora da aprovação local. Custo de extrapolá-los seria anunciar distribuição/execução/eficácia sem evidência; os registros e a entrega mantêm o limite explícito.

Não há runner de testes na raiz; não se executaram npm test, testes do Desktop ou instalações para esta unidade. Casos observados e validador são as verificações executadas. O pacote foi preparado para revisão e uso posterior; não foi instalado automaticamente ou publicado.
