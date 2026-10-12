# Agente de Propostas Comerciais — pedidos estruturados, escopo e consistência

Pesquisa em 12/10/2026. Frente da décima primeira skill do lote de 33; insumo para criação posterior, sem criar ou instalar pacote, alterar galeria, executar as skills examinadas, enviar proposta ou contratar serviço.

## Decisão recomendada

Adotar uma disciplina simples: aproveitar os materiais e o modelo da pessoa; distinguir o que o comprador pediu, o que o fornecedor comprovou e o que está propondo; conferir que narrativa, escopo, prazo, preço e condições descrevem o mesmo negócio. RFP, orçamento, proposta comercial e SOW exigem profundidades diferentes. A resposta segue o formato obrigatório do comprador quando ele existe; fora disso, a menor estrutura útil ao pedido.

As contribuições mais fortes são a matriz de requisitos com localização e evidências, a ligação entre escopo e entregas com critérios de aceite, e a conferência das exclusões entre estimativa e documento. Não importar os métodos inteiros: os pacotes examinados incluem pressupostos de procurement americano, consultoria específica, fórmulas de probabilidade de vitória sem calibração demonstrada e cláusulas jurídicas genéricas.

## Alcance e contagens

- Descoberta com duas consultas ao `npx --yes skills find`: `rfp` e `statement of work`; busca web por `SKILL.md` com RFP, statement of work, deal desk e quoting. O comando consultou o catálogo; nenhuma skill foi instalada. Instalações e estrelas não decidiram qualidade.
- **5 repositórios de origem analisados substantivamente; 13 SKILL.md lidos integralmente.** Gener8v: 6; Alireza Rezvani: 3; OneWave AI: 1; Meaningfy: 1; Peter Bamuhigire: 2. A leitura truncada de alguns lotes foi complementada por consultas menores aos arquivos afetados.
- **17 recursos de comportamento consultados:** 3 Gener8v, 6 Alireza, 5 OneWave, 2 Meaningfy e 1 Peter. Manifesto abaixo. Além deles, foram lidos README de descoberta e 3 arquivos LICENSE completos, separados dessa contagem.
- **3 fontes profissionais primárias consultadas:** FAR 15.204-5, FAR 37.602 e Código Civil brasileiro, art. 427 e contexto imediato. As regras americanas são referências de método em seu próprio contexto; não foram tratadas como exigências brasileiras.
- Duas origens adicionais foram sondadas: `borghei/Claude-Skills` foi identificado com licença declarada MIT + Commons Clause na página da skill; `mohitagw15856/pm-claude-skills` teve descoberta por índice e tentativa de arquivo SOW que devolveu 404. Nenhuma integra a contagem das 13 leituras completas. Outros resultados, como bidwriter, Clawfu e diretórios de skills, foram pistas, sem auditoria integral.
- Cópias nos distribuidores e nos diretórios `.codex`/`.gemini` de Alireza, forks como nasikgmx e borahanmirzaii, e páginas de Tessl/GetClaudeSkills não são fontes independentes. A análise usa os caminhos canônicos pinados. As skills de Peter declaram origem de técnicas no ECC/Santa Method; são adaptações reconhecidas, não uma segunda prova independente da eficácia dessas técnicas.
- Nenhum clone, download de pacote, conta, chave, envio, assinatura, execução de script examinado, geração de proposta real, commit ou push. Apenas consulta remota e este dossiê local. Não houve teste de entrega comercial real.

## Proveniência verificável

O HEAD de cada origem foi confirmado com `git ls-remote`; as leituras relevantes usaram raw URLs com o SHA completo. As datas abaixo vieram de `committedDate` da página do commit, e descrevem o commit do repositório, **não a última mudança individual de cada skill**. A API pública do GitHub retornou rate limit; não foi usada para concluir licença ou revisão.

| Origem/autoria | SHA consultado | Data do commit | Licença observada e limite |
|---|---|---|---|
| [gener8v](https://github.com/gener8v/gener8v.claude-skills.rfp-response/commit/93373236bd76ecb223f4509bee6bc610778a6ffe) | `93373236bd76ecb223f4509bee6bc610778a6ffe` | 04/03/2026, 15:43:33 −05:00 | README declara MIT e gener8v; `LICENSE` na raiz retornou 404; frontmatters não declaram licença. Base insuficiente para copiar recursos sem confirmação adicional. Aprendizado conceitual em redação própria. |
| [Alireza Rezvani](https://github.com/alirezarezvani/claude-skills/commit/19392f7a08264ed00486a251f5b2098321771f94) | `19392f7a08264ed00486a251f5b2098321771f94` | 26/08/2026, 15:53:02 +02:00 | LICENSE MIT, copyright 2025 Alireza Rezvani; deal-desk/rfp-responder declaram MIT e autor `claude-code-skills`. Contract-and-proposal-writer não declara licença própria; raiz lida. Avisos precisam acompanhar eventual adaptação textual. |
| [OneWave AI](https://github.com/onewave-ai/claude-skills/commit/fc5b7851a6c7ba367e05797df46ad3679df355dd) | `fc5b7851a6c7ba367e05797df46ad3679df355dd` | 02/10/2026, 04:18:41 −04:00 | LICENSE MIT, copyright 2025 OneWave AI; SKILL sem licença no frontmatter. |
| [Meaningfy / skillery](https://github.com/meaningfy-ws/skillery/commit/d45306b43d6203abb866830e1dcb2f2dd846aafa) | `d45306b43d6203abb866830e1dcb2f2dd846aafa` | 15/09/2026, 23:28:16 +02:00 | `proposal-writing/SKILL.md` declara Apache 2.0. Arquivo legal de raiz não auditado; não autoriza concluir licença do pacote inteiro. Autoria atribuída ao projeto, sem inventor individual confirmado. |
| [Peter Bamuhigire](https://github.com/peterbamuhigire/proposal-skills/commit/860f0cb3cc296a48e8848eb0fd37d75c000e7ee7) | `860f0cb3cc296a48e8848eb0fd37d75c000e7ee7` | 29/09/2026, 13:14:45 +03:00 | LICENSE MIT, copyright 2026 Peter Bamuhigire. As duas skills reconhecem adaptações do ECC; dual review nomeia Ronald Skelton/Santa Method. README registra que a licença do ECC não foi inventariada ali: preservar essa lacuna caso se pretenda copiar trechos derivados. |

Leitura parcial de repositório não comprova segurança ou licença de todos os arquivos. Bibliotecas citadas não foram verificadas no Desktop, e nenhum pacote foi certificado compatível com a galeria.

## Arquivos efetivamente lidos

Links de raiz abaixo apontam à revisão auditada; os caminhos listados são relativos a ela.

### Gener8v — seis skills e três apoios

[Árvore auditada](https://github.com/gener8v/gener8v.claude-skills.rfp-response/tree/93373236bd76ecb223f4509bee6bc610778a6ffe/rfp-toolkit).

SKILL completos: `collateral-analyzer/SKILL.md`, `requirements-mapper/SKILL.md`, `section-drafter/SKILL.md`, `empathy-reviewer/SKILL.md`, `compliance-validator/SKILL.md`, `proposal-assembler/SKILL.md`.

Apoios: `requirements-mapper/assets/coverage-matrix-template.md`, `compliance-validator/references/rfp-compliance-patterns.md`, `proposal-assembler/assets/assembly-template.md`. Outros templates e referências citados pelas skills não foram auditados. README também foi lido; ele não substitui uma licença formal ausente.

### Alireza — três skills e seis apoios

[Árvore auditada](https://github.com/alirezarezvani/claude-skills/tree/19392f7a08264ed00486a251f5b2098321771f94).

SKILL completos: `commercial/skills/rfp-responder/SKILL.md`, `commercial/skills/deal-desk/SKILL.md`, `business-growth/skills/contract-and-proposal-writer/SKILL.md`.

Apoios: `commercial/skills/rfp-responder/assets/rfp_intake_template.md`, `commercial/skills/rfp-responder/scripts/rfp_parser.py`, `commercial/skills/rfp-responder/scripts/response_drafter.py`, `commercial/skills/rfp-responder/references/shipley_method_canon.md`, `commercial/skills/deal-desk/assets/deal_intake_template.md`, `commercial/skills/deal-desk/scripts/discount_approval_router.py`. LICENSE lido à parte. O preditor de winrate, o scorer de negócios, o redliner jurídico e suas referências não foram auditados nem executados.

### OneWave — uma skill e cinco apoios

[Árvore auditada](https://github.com/onewave-ai/claude-skills/tree/fc5b7851a6c7ba367e05797df46ad3679df355dd/sow-generator).

SKILL completo: `sow-generator/SKILL.md`. Apoios no mesmo diretório: `references/required-inputs.md`, `references/document-structure.md`, `references/pricing-templates.md`, `references/change-management.md`, `references/legal-terms.md`. `risk-management.md` não foi lido. LICENSE de raiz lido à parte.

### Meaningfy — uma skill e dois apoios

[Árvore auditada](https://github.com/meaningfy-ws/skillery/tree/d45306b43d6203abb866830e1dcb2f2dd846aafa/skills/proposal-writing).

SKILL completo: `skills/proposal-writing/SKILL.md`. Apoios: `references/scope-boundary-checklist.md` e `references/sow-template.md`. A estimativa, o pacote de decisão e as demais skills dependentes não foram lidos; nenhum fluxo completo foi demonstrado.

### Peter — duas skills e um apoio

[Árvore auditada](https://github.com/peterbamuhigire/proposal-skills/tree/860f0cb3cc296a48e8848eb0fd37d75c000e7ee7).

SKILL completos: `skills/meta/bid-red-team-dual-review/SKILL.md` e `skills/meta/submission-proof-and-receipt-discipline/SKILL.md`. Apoio: `rules/common/core.md`. README e LICENSE lidos à parte. O repositório declara 115 skills, mas **somente duas foram examinadas integralmente nesta frente**. Não importar a contagem de seu catálogo para a nossa cobertura.

## Matriz de componentes e decisões

| Fonte/arquivo | Componente observado | Decisão | Motivo e destino |
|---|---|---|---|
| Gener8v `collateral-analyzer/SKILL.md` | Inventário de documentos; contradições, lacunas, vocabulário do comprador | **Adaptar** | Aproveitar antes de redigir; perguntar só o que muda a proposta. Não exigir RFP quando o pedido é uma proposta espontânea ou orçamento. Histórico oferece referência, não substitui dados atuais. Núcleo. |
| Gener8v `requirements-mapper/SKILL.md` e coverage template | Requisito literal, seção/página, obrigatório/preferencial, evidência e ação | **Adotar em redação própria** | Rastreabilidade útil em RFP. Reduzir para lista simples em pedido pequeno. Separar requisito explícito de prioridade inferida; não tornar inferência uma obrigação. Referência RFP. |
| Gener8v `requirements-mapper/SKILL.md` | `Assertable`: presumir capacidade por porte/maturidade ou norma do setor | **Descartar** | Expectativa não confirma capacidade. Substituir por informação não comprovada/pendente e proposta de abordagem condicionada. Certificação, experiência e SLA exigem evidência própria. |
| Gener8v `section-drafter/SKILL.md` | Ordem prescrita do comprador; conexão evidência→aplicação; lacunas honestas | **Adaptar** | Boa redação quando baseada no caso. Plano de obter certificação não pode ganhar data inventada; separar capacidade atual de entrega futura proposta. Núcleo + RFP. |
| Gener8v `empathy-reviewer/SKILL.md` | Revisão de vocabulário, genericidade, superlativos e responsabilidade | **Adotar em redação própria** | Ajuda profissional simples: cliente reconhece seu problema e quem entrega. Não acrescentar reescrita genérica a texto aprovado; preservar nomes e condições. Núcleo. |
| Gener8v `compliance-validator/SKILL.md` e compliance patterns | Releitura da RFP após revisão; anexos, adendos, páginas e formato financeiro | **Adaptar** | Conferir depois da última edição, inclusive formato final renderizado. `Ambiguous — assumed compliant` vira **pendente/ambíguo**, nunca pass presumido. Consequência de falha vem do edital específico. |
| Gener8v `proposal-assembler/SKILL.md` e assembly template | Referências internas, nomes, anexos e ordem final; relatório de pendências | **Adaptar** | Documento externo e nota de revisão interna separados quando útil. Documento montado pode ser rascunho revisável mesmo com pendências; não chamá-lo pronto para submissão. |
| Gener8v assembler | Remover todos os marcadores `[ASSERTION]` e resumir apenas quantidade/ratio | **Descartar** | Contagem não conserva o sentido nem resolve a falta de prova. Manter qualificações materiais no texto externo; remover só anotações internas resolvidas. |
| Alireza `rfp-responder/SKILL.md` e intake | Matriz obrigatório/ponderado/opcional; fonte verificável; lacunas em primeiro plano | **Adaptar** | Bom recorte de RFP ditada pelo comprador. Usar estados atendido/parcial/pendente/não atendido conforme análise substantiva; método Shipley fica contextualizado. Referência RFP. |
| Alireza `rfp_parser.py` | Regex de cues em inglês e extração de data | **Descartar como validador** | Não cobre PT-BR, perguntas sem cues ou obrigações em tabela; `deadline` perde hora/fuso. Pode auxiliar busca, jamais provar cobertura. Não trazer parser agora. |
| Alireza `response_drafter.py` | Atribuir `STRONG` por duas tags sobrepostas e tipo da prova | **Descartar** | Não lê o conteúdo da evidência nem valida sua vigência/escopo. Similaridade lexical não comprova atender. Script guarda `verifiable_source` fornecida, sem verificá-la. |
| Alireza `rfp-responder`/Shipley canon | Winrate, thresholds fixos, 3–5 temas e percentuais de influência | **Descartar como padrão** | Estatísticas e fórmulas não foram corroboradas nas fontes primárias; modelo não foi executado/calibrado. Pode orientar conversa de bid/no-bid se a pessoa já trabalha assim, sem probabilidade numérica inventada. |
| Alireza `deal-desk/SKILL.md` e intake | Comparar negócio solicitado com política existente; exceções e responsável | **Adaptar** | Skill prepara informação para decisão, não aprova. Preservar alçada e condições reais do usuário. Resumo de desvios só quando há política ou revisão solicitada; não criar departamento de deal desk. |
| Alireza `discount_approval_router.py` | Bands, perfis e cadeia com override de política | **Descartar como implementação padrão** | Mesmo com override de bands, há modificadores enterprise/SMB e regra fixa de desconto acima de 50%. Cadeia contém cargos, embora SKILL prometa nomes; não satisfaz aprovação humana nominal sozinho. |
| Alireza `contract-and-proposal-writer/SKILL.md` | Distinguir proposta/SOW/contrato e preencher dados | **Adaptar** | Tipo de documento importa. Não forçar um dos quatro mercados estrangeiros nem instalar Pandoc. Proposta não precisa virar contrato. |
| Alireza contract writer | Cláusulas de juros, IP, liability, disputa e alegações legais por país | **Descartar** | Regras genéricas, sem revisão jurídica atual demonstrada; não cobre Brasil. Não importar cláusula, jurisdição ou prazo de cura como padrão. |
| OneWave `sow-generator/SKILL.md` e document structure | Escopo→entregas→marcos→pagamento; aceite mensurável; dependências com responsável | **Adotar conceito / adaptar extensão** | Relações evitam vender uma coisa e cobrar outra. Identificadores e tabelas só quando volume justifica. Critério de aceite deriva da entrega e acordo, não satisfação vaga ou meta comercial garantida. Referência escopo. |
| OneWave required inputs/pricing | Não adivinhar condição crítica; preço fixo/T&M/retainer | **Adaptar** | Manter modelo informado, moeda/unidades e premissas. Se o valor falta, tratar como pendência ou estimativa autorizada; não presumir preço fixo nem juros/Net 30. |
| OneWave change-management | Mudança documenta impacto em prazo, escopo e valor | **Adaptar** | Explicar tratamento de extras quando relevante. Usar aprovadores/prazos fornecidos; descartar percentuais e comitês exemplificativos. |
| OneWave legal terms/document structure | 16 seções obrigatórias, 500–800 linhas, aceite presumido por silêncio e cláusulas americanas | **Descartar** | Rigidez gera custos e obrigações indevidas. Não inserir aceite automático, foro, multa, transferência de IP, seguro ou prazo de garantia apenas para preencher template. |
| Meaningfy proposal-writing/scope checklist/SOW template | Exclusões da estimativa e do SOW são a mesma lista; limite explícito de cada item | **Adotar conceito** | Invariante forte de consistência. A proposta não promete o que foi excluído do valor. Núcleo de QA. |
| Meaningfy mesmos arquivos | Oferta P1 Decision Phase obrigatória, P2 sempre separado, delegação a quatro outras skills | **Descartar** | É o modelo comercial específico daquela consultoria, ainda declarado provisional. Não atende venda de produto, agência ou implementação integral. Não importar suas dependências. |
| Peter dual review/core | Rubrica de precisão, evidência, completude e consistência | **Adaptar** | Útil à revisão de risco material. Duas avaliações independentes somente quando necessárias e disponíveis/autorizadas; não afirmar independência em duas passadas do mesmo contexto. Referência QA. |
| Peter core | Não inferir critérios de avaliação de edital anterior | **Adotar conceito** | Ordem e pesos atuais precisam vir do documento atual. Não inventar critérios omitidos. Referência RFP. |
| Peter receipt discipline | Separar arquivo pronto, envio, evidência de recebimento; arquivo exato/versão | **Adotar conceito / adaptar recurso** | Envio necessita autorização própria. Checksum/recibo para submissão formal e risco de versão, sem banco ou dispatch framework. Pedido comum não precisa registro de portal. Referência entrega. |

## Falhas concretas do código lido

A avaliação é estática, **nenhum script foi executado**. Estes exemplos são inferências diretamente da implementação, não bugs reproduzidos em runtime:

1. Em `rfp_parser.classify_requirement`, a detecção de `NICE_CUES` precede `MANDATORY_CUES`. Uma linha que contém ao mesmo tempo obrigação e opção pode ser rotulada inteira como opcional. O regex só conhece cues em inglês; o parser não trata semântica de exceções, tabelas nem perguntas sem essas palavras. Requisitos precisam ser divididos e interpretados no documento original.
2. `extract_deadline` devolve só o grupo da data da primeira ocorrência. Mesmo o exemplo interno tem hora e `ET` em outra linha; o campo estruturado de prazo não conserva esses dados. Uma entrega formal exige data, hora, fuso e adendo aplicável, lidos diretamente da fonte.
3. `response_drafter.assign_proof` usa contagem de tags e tipo da evidência. Dois termos coincidentes em uma evidência de escopo diferente podem receber `STRONG`; nenhuma rotina dessa função abre a fonte. Resultado lexical deve ser tratado como pista de busca, não atendimento.
4. `discount_approval_router` aceita uma política de bandas customizada, porém mantém modificadores do perfil e o aviso fixo para desconto acima de 50%. Cargos retornados não são os nomes reais prometidos pelo frontmatter; estimativas de ciclo vêm de constantes. Importá-lo criaria política não fornecida pelo usuário.

Não corrigir esses repositórios nem desenvolver substitutos nesta pesquisa. A decisão é **não empacotar esses automatismos** na primeira versão.

## Conflitos e síntese profissional

### Atender ao requisito não é apenas mencioná-lo

Gener8v oferece uma camada útil de evidências, mas `Assertable` permite afirmações pela expectativa de capacidade. Alireza proíbe inventar provas, porém seu script reduz a prova a tags. A síntese é uma matriz lida semanticamente: requisito, fonte/localização, resposta/localização, evidência aplicável e estado. Capacidade atual, proposta de execução futura e comprovação de experiência são colunas/conceitos distintos.

Estados recomendados para pedido estruturado: **atendido** quando cada parte exigida foi coberta e a evidência necessária existe; **parcial** quando uma parte identificável falta; **pendente** quando informação, verificação ou decisão ainda falta; **não atendido** quando a lacuna está confirmada. A aplicabilidade pode ser registrada separadamente com motivo. Prioridade inferida não ganha o status de requisito obrigatório.

### Formato do comprador e narrativa de venda

Uma resposta ao questionário respeita seus campos, nomes, unidades, ordem e anexos. A regra de reordenar por valor ou tema comercial não sobrepõe uma estrutura mandatória. Se houver liberdade editorial, organizar o documento para a decisão da pessoa e mover detalhes a anexos. A [FAR 15.204-5](https://www.acquisition.gov/far/15.204-5) confirma que instruções de submissão e fatores de avaliação são elementos separados e que podem ser exigidos volumes específicos; isso sustenta a técnica de lê-los separadamente, no contexto federal americano.

### Escopo e aceite proporcional

A [FAR 37.602](https://www.acquisition.gov/far/37.602) descreve trabalho orientado a resultado com padrões mensuráveis para avaliação. Sua contribuição transferível é definir o que será entregue e como verificar; sua aplicação jurídica não é transferida. Não impor um método de horas se a oferta é por resultado, nem eliminar rate card quando a oferta é por hora. Aceite precisa ser possível no prazo e sob controle das partes: entregar treinamento pode ser compromisso; aumentar vendas em 30% pode ser meta condicionada, não garantia derivada automaticamente desse treinamento.

### Precisão não depende de tamanho

OneWave ajuda a rastrear objetos, mas exige todos os blocos enterprise. Meaningfy é bem mais compacto e mantém limites claros, porém só oferece consultoria P1. Síntese: proposta simples conserva objetivo, entrega/escopo, prazo, valor/condições e próximo passo; acrescentar exclusões ou premissas que realmente mudam a interpretação. SOW/RFP com marcos, dependências e anexos usa tabelas/referência própria. Não criar três níveis de preço, SLA, registro de riscos ou comitê só porque um modelo externo tem.

### Documento, intenção e efeito jurídico

Preservar texto jurídico e políticas fornecidos; sinalizar discrepâncias e preparar perguntas/alterações para revisão. Não inserir termos de aceite por silêncio, garantia, multa, confidencialidade, propriedade intelectual, foro ou jurisdição sem base e autorização pertinente. Na [Lei 10.406/2002, art. 427](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm), a proposta de contrato pode obrigar o proponente conforme seus termos e circunstâncias. **Rascunho, proposta enviada e documento assinado são estados operacionais diferentes, mas ausência de assinatura não prova ausência de efeito jurídico.** Essa fonte resolve o limite de linguagem; esta pesquisa não analisa validade jurídica de cláusulas nem determina a situação de uma proposta concreta.

Premissa deve continuar visível como condição; dado confirmado não vira estimativa; sugestão comercial não vira compromisso do fornecedor; condição nova negociável não substitui política existente silenciosamente. A nomenclatura de estado ajuda a operação, sem prometer conclusões jurídicas universais.

## QA comercial e documental recomendado

A revisão verifica o negócio completo após a última alteração, não apenas português e aparência:

| Conferência | Evidência necessária | Exemplo de falha que precisa aparecer |
|---|---|---|
| Origem e vigência | Brief, RFP e adendos mais recentes; política/modelo fornecido | Copiar condição do cliente anterior ou critério de outro edital |
| Identidade e objetos | Cliente, fornecedor, objeto, opção escolhida e versão consistentes | Capa de um cliente, anexo de outro; plano A no texto e plano B no preço |
| Requisito e resposta | Localização na fonte e no documento; prova pertinente | Obrigação citada mas não respondida; certificação expirada ou sem escopo pertinente |
| Escopo e exclusões | Entregas, quantidades/unidades, limites e itens não precificados | Texto promete migração que a planilha exclui |
| Prazo | Início condicionado, duração, calendário e dependências conhecidos | Data fixa incompatível com prazo de acesso do cliente |
| Valores | Quantidade × preço, subtotal, desconto, impostos/despesas informados e total | Total final mistura recorrência mensal com taxa única |
| Pagamento | Parcelas e gatilhos consistentes com preço e aceite | Parcelas somam 110%; cobrança ligada a marco inexistente |
| Condições | Validade, moeda, reajuste/renovação quando existentes, exceções e autorizadores reais | Prazo de validade inventado; desconto excede política sem responsável |
| Documento final | Tabelas legíveis, referências/anexos existentes, páginas no formato pedido | PDF corta preço; sumário aponta página estimada; anexo não enviado |
| Handoff | Arquivo editável/final solicitado e pendências materiais identificadas | Documento exportado chamado enviado; checklist interno dentro de anexo externo |

Exemplo de reconciliação matemática **fictício**, sem proposta real: 10 unidades × R$ 200 = R$ 2.000; desconto informado de 10% = R$ 200; total após desconto = R$ 1.800. Duas parcelas iguais seriam R$ 900. Se o texto trouxer duas parcelas de R$ 1.000, apontar diferença de R$ 200; não inventar imposto para reconciliar. Confirmar separadamente incidência de impostos, frete e recorrência. Sem informação, não assumir que total bruto/líquido são a mesma coisa.

Datas e valores reaparecidos devem ser reconciliados em todas as seções após mudança de opção ou condição. Margem e rentabilidade só podem ser calculadas quando custos e definição de margem existem; desconto sobre preço não é queda idêntica de margem. Moedas diferentes não se somam sem taxa, data e fonte fornecidas/verificadas.

## Núcleo e referências sob demanda

Proposta de organização para futura síntese, **nenhum arquivo de skill foi criado**:

| Local futuro | Conteúdo enxuto | Quando carregar |
|---|---|---|
| Núcleo SKILL.md | Aproveitar contexto/modelo, escolher entrega, perguntar lacunas materiais, redigir, conferir negócio e formato, declarar estado | Qualquer pedido de proposta |
| `references/rfp-responses.md` | Matriz de requisitos/evidência, instruções vs avaliação, adendos, volumes, prazo/fuso, incompletude | RFP/RFI/RFQ, licitação ou questionário ditado pelo comprador |
| `references/scope-and-acceptance.md` | Escopo/entregas/aceite/marcos/dependências; exclusões alinhadas; mudança com impacto | SOW ou serviço com risco material de escopo |
| `references/commercial-consistency.md` | Preço/quantidade/moeda/recorrência, parcelas, política de desconto e pendências | Orçamento, tabela comercial ou revisão de números |
| `references/document-quality.md` | Forma solicitada, leitura visual, tabelas, referências, anexos, assinatura/envio separados | DOCX/PDF/planilha/slides ou pacote formal |
| Template compacto opcional | Somente fallback quando a pessoa não trouxe modelo; adaptação ao negócio | Proposta simples sem modelo |

Não incluir bibliografia extensa, roteiro de research, 13 skills embutidas, gerador jurídico, score de winrate ou infraestrutura de envio no pacote. O texto executável precisa falar em cliente, entrega, prazo, investimento, pendência e condição — não em harness, parser, JSON ou framework.

## Formatos, ferramentas e adaptação ao ambiente

- Respeitar o pedido: texto no chat, Markdown editável, DOCX, PDF, apresentação ou planilha financeira. A exigência de Markdown-only do Gener8v é uma escolha daquele pipeline, não do usuário.
- Usar recursos documentais disponíveis quando a entrega exigir. Confirmação de dependência é anterior à promessa de exportação. Não assumir Pandoc, LibreOffice, Python ou renderer porque aparecem na fonte; comandos de instalação Mac/Linux do contract writer não atendem automaticamente o Windows/Studio.
- Para proposta curta, escrever diretamente e revisar é suficiente. Para tabela financeira longa, aritmética mecânica pode justificar script próprio simples; usar Decimal/centavos, separar unidades, não embutir percentuais de imposto nem política comercial. Aqui apenas a necessidade foi avaliada: nenhum script foi criado.
- Se exportação solicitada depende de recurso ausente, comunicar o resultado e a opção de preparação em linguagem de trabalho, com custo/necessidade concretos. Não converter instalação extra em requisito universal de toda proposta.
- Preservar modelo, texto aprovado, campos, identidade e política da pessoa. Ajustes recorrentes observados podem justificar melhoria da própria skill: regra geral reutilizável no núcleo ou referência adequada; informação confidencial do cliente e condições da negociação não viram instruções globais. Toda adaptação segue a autorização/revisão do ambiente, sem alterar silenciosamente política comercial.
- Caso seja solicitada submissão futura, usar autorização explícita para envio e identificar destino, versão e canal. Assinatura/aceitação dependem das pessoas habilitadas. Sem envio autorizado, entrega é o arquivo e a informação necessária à revisão.

## Limites e conclusão desta frente

As dúvidas materiais desta frente foram resolvidas por comparação de componentes: rastrear requisitos e evidências, delimitar escopo, reconciliar compromisso com números, respeitar formato e separar preparo de submissão. Continuar adicionando catálogos similares não mudaria a recomendação.

Permanecem limites explícitos: nenhuma execução comercial de referência observada; métodos de winrate e estatísticas citados nos pacotes não corroborados; nenhuma cláusula jurídica validada; nenhuma compatibilidade do pacote inteiro com Hermes/Desktop certificada; recursos não listados no manifesto não foram auditados. Licença Gener8v exige esclarecimento antes de copiar, Apache de Meaningfy exige conferência dos arquivos legais antes de redistribuição e conteúdo derivado ECC exige preservar sua origem e verificar licença se houver adaptação textual.

A futura skill pode ser escrita em redação própria a partir desta síntese e das demais frentes, preservando o escopo aprovado. Esta entrega é **pesquisa documental**, não publicação, instalação nem prova de que um agente já produz propostas de ponta a ponta.
