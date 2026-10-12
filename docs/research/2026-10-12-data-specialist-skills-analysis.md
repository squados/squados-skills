# Especialista em Dados — skills de análise, exploração e diagnóstico

Data da consulta: 12/10/2026. Frente de pesquisa sobre o trabalho interno de empresas: entender números, investigar diferenças e orientar decisões em operações, financeiro, vendas e RH. Esta frente não cria pacote, não altera a galeria e não instala nem executa as skills consultadas. Relatórios, visualização e métodos profissionais têm frentes próprias.

## Resultado e alcance

A base mais útil combina três contribuições: **proporção ao pedido** do `analyze` da Anthropic, **decomposição e reconciliação** do `metric-diagnostics` da OpenAI e **disciplina estatística** do K-Dense. Nenhuma candidata resolve integralmente o destino sem adaptação. O padrão deve partir do pedido de trabalho e dos materiais disponíveis, escolher o mínimo método suficiente e entregar a resposta com evidência compreensível.

Foram lidos **12 SKILL.md completos de 5 famílias autorais**, além de **6 recursos determinantes completos**. As licenças de três famílias foram lidas integralmente; o cabeçalho Apache 2.0 da Anthropic foi identificado; a licença de `openai/plugins` não foi localizada nos caminhos consultados. Todos os SKILL.md e recursos analisados foram obtidos em SHA fixo, não apenas pela descrição do diretório.

Descoberta: pesquisa na web por profissão, EDA, diagnóstico de indicadores, estatística e análise de negócio; páginas do skills.sh e resultados dos repositórios originais. A skill `find-skills` orientou a descoberta, sem usar comandos de instalação. A seleção favoreceu diferenças de método e relevância, não estrelas ou instalações. Não é um censo do ecossistema.

Os recursos completos foram: Anthropic `data/CONNECTORS.md` e `data/skills/data-context-extractor/references/domain-template.md`; K-Dense `skills/statistical-analysis/references/test_selection_guide.md` e `skills/exploratory-data-analysis/scripts/tabular_profile.py`; borghei `data-analytics/data-analyst/scripts/data_profiler.py`; Abdo `assets/profile_data.py`.

**Limites de leitura e execução:** os imports transitivos do CLI K-Dense, os demais scripts e referências científicas, os builders/templates HTML do Abdo, os demais scripts borghei e as skills irmãs chamadas pela OpenAI não foram auditados nesta frente. O arquivo K-Dense `_tabular.py` foi obtido, mas não analisado; não integra a contagem de recursos lidos. Nenhum teste, análise numérica ou runtime original foi executado. Referências a validações presentes no texto das candidatas são declarações dos autores, não resultados desta pesquisa.

## Originais, autoria, revisão e licença

Os SHA abaixo foram confirmados com `git ls-remote ... HEAD`; os textos foram lidos em `raw.githubusercontent.com/<repo>/<SHA>/<path>`. A API pública do GitHub apresentou limite de requisições. Datas de commit não foram verificadas; não se confundem com datas visíveis no frontmatter ou a data desta consulta.

| Família original | SHA consultado | Autoria e data visível | Situação de licença |
|---|---|---|---|
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins/tree/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06) | `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06` | Anthropic; SKILL.md selecionados sem data de revisão declarada | [LICENSE](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/LICENSE): cabeçalho Apache 2.0 identificado; não houve auditoria jurídica completa |
| [openai/plugins](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a) | `0722921d5542fc593105c27bd52630babd8b8c2a` | OpenAI; SKILL.md selecionados sem data de revisão declarada | Não localizada em `LICENSE`, `LICENSE.md`, `LICENSE.txt` na raiz, nem `plugins/data-analytics/LICENSE*`. Referência de método; redistribuição de texto/código pendente de base verificável |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/a1043ef544e3a100c28e70a736b6cf32554d0677) | `a1043ef544e3a100c28e70a736b6cf32554d0677` | K-Dense Inc.; EDA 1.4, revisada 30/09/2026; estatística 2.0, revisada 01/10/2026 | [LICENSE.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/a1043ef544e3a100c28e70a736b6cf32554d0677/LICENSE.md): MIT, copyright 2025 K-Dense Inc. |
| [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills/tree/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0) | `4a698e8d07856fdca9ec3e69082a9d68c8dd45d0` | Amin Borghei; `data-analyst` 1.0.0, atualizado 31/03/2026 | [LICENSE](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/LICENSE): MIT + Commons Clause; não tratar como MIT simples ou incorporar no produto comercial sem resolver a restrição |
| [AbdoBasyioni/business-analysis-skill](https://github.com/AbdoBasyioni/business-analysis-skill/tree/e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae) | `e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae` | Abdelrahman Mahmoud Ali Basiony; crédito também usa Eng: 3bdo Mahmoud; SKILL sem versão/data de revisão declarada | [LICENSE](https://github.com/AbdoBasyioni/business-analysis-skill/blob/e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae/LICENSE): MIT, copyright 2026; preservar aviso legal se houver reutilização |

### Duplicação e páginas desatualizadas

- `openai/role-specific-plugins` aparece arquivado nos resultados. Os mesmos nomes foram tratados como linhagem anterior, não fontes independentes. A leitura substantiva usou `openai/plugins`.
- O endereço histórico `K-Dense-AI/claude-scientific-skills` resolve a linhagem hoje publicada como `scientific-agent-skills`. `anderson-ntlabs`, `kellsaro` e `IgorOffline` apareceram como forks/espelhos; não entram na contagem independente.
- Resultados antigos descrevem EDA para mais de 200 formatos. O texto atual distingue formatos automatizados, opcionais, apenas documentados e não suportados. A análise usa o conteúdo atual no SHA fixo.
- Nomes anteriores `data-exploration` e `data-validation` ainda aparecem em README/resultados; os arquivos atuais lidos são `explore-data` e `validate-data`. Os caminhos antigos responderam 404 no SHA consultado.
- Não foi localizada skill pública de análise empresarial dentro de `openai/skills` nesta busca; isso não é prova de ausência. A família pertinente encontrada foi `openai/plugins`.

## As 12 candidatas completas

| ID | Fonte e arquivo completo | Trabalho concreto | Decisão para a composição posterior |
|---|---|---|---|
| A1 | [Anthropic — analyze](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/analyze/SKILL.md) | Pergunta pontual, investigação ou relatório formal, com CSV/Excel/resultado colado quando não houver warehouse | Aproveitar proporcionalidade; adaptar acesso e formatos ao ambiente |
| A2 | [Anthropic — explore-data](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/explore-data/SKILL.md) | Entender o que cada linha representa, chaves, cobertura, dados ausentes e dimensões | Adaptar perfil ao pedido; evitar varrer cada coluna por padrão |
| A3 | [Anthropic — statistical-analysis](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/statistical-analysis/SKILL.md) | Descrever dispersão, tendências, anomalias, diferenças e incerteza em linguagem de negócio | Aproveitar foco empresarial; substituir atalhos de inferência por referência técnica mais precisa |
| A4 | [Anthropic — validate-data](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/validate-data/SKILL.md) | Revisar cálculo e conclusão antes de apresentação: junções, denominadores, períodos, vieses | Aproveitar catálogo de falhas e recálculo independente; adaptar regras de domínio |
| A5 | [Anthropic — data-context-extractor](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/data-context-extractor/SKILL.md) | Capturar definições, exclusões, entidades e erros recorrentes específicos da empresa | Adaptar como oferta opcional de ajuste da própria skill; não exigir bootstrap em toda análise |
| O1 | [OpenAI — metric-diagnostics](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/metric-diagnostics/SKILL.md) | Investigar por que um indicador mudou, com contribuição de segmentos e reconciliação | Aproveitar método; adaptar busca abrangente, notebooks e relatório obrigatório |
| O2 | [OpenAI — analyze-data-quality](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/analyze-data-quality/SKILL.md) | Julgar se a base é confiável para a decisão, com testes que dependem do tipo de dado | Aproveitar verificações selecionadas por risco real; adaptar execução e entrega |
| O3 | [OpenAI — product-business-analysis](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/product-business-analysis/SKILL.md) | Transformar dados em escolha, prioridade e estimativa de impacto | Aproveitar decisão primeiro e recortes que podem alterá-la; adaptar acoplamentos ao plugin |
| K1 | [K-Dense — exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/a1043ef544e3a100c28e70a736b6cf32554d0677/skills/exploratory-data-analysis/SKILL.md) | Perfil local delimitado, auditoria de ausências, influência de valores extremos e distinção EDA/inferência | Adaptar higiene analítica; descartar abrangência científica e restrições de identificação como padrão empresarial |
| K2 | [K-Dense — statistical-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/a1043ef544e3a100c28e70a736b6cf32554d0677/skills/statistical-analysis/SKILL.md) | Seleção de testes segundo desenho, dependência, efeito pretendido e pressupostos | Aproveitar referência sob demanda; adaptar comunicação e dependências; não impor APA ao trabalho diário |
| B1 | [borghei — data-analyst](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/data-analytics/data-analyst/SKILL.md) | SQL, perfil, coortes, funil e recomendação | Comparativo conceitual; não copiar recursos com Commons Clause |
| D1 | [Abdo — business-analysis](https://github.com/AbdoBasyioni/business-analysis-skill/blob/e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae/SKILL.md) | Análise de planilhas empresariais multiaba, lucro, descontos, cobrança e concentração | Adaptar componentes comerciais; descartar protocolo monolítico, idioma fixo e promessa de 100/100 |

## Fonte → componente → decisão → motivo

| Fonte/arquivo | Contribuição observada | Decisão | Motivo e adaptação necessária |
|---|---|---|---|
| A1 `analyze/SKILL.md` | Ajustar profundidade entre resposta direta, investigação e relatório | **Aproveitar** | Reconhecer intenção automaticamente; uma pergunta simples pode terminar com número, contexto e cálculo, sem diagnóstico completo |
| A2 `explore-data/SKILL.md` | Representação de cada linha, classificação de colunas, chaves, cobertura e atualização | **Aproveitar** | Evita somar IDs ou misturar pedido com item de pedido; inventário compacto antes das contas |
| A2 `explore-data/SKILL.md` | Alertas universais de nulos de 5%/20%, dimensões por cardinalidade e correlações entre todos os pares | **Adaptar** | São heurísticas; uma coluna opcional pode ter 90% de nulos válidos. Perfil e correlações dependem da pergunta e semântica |
| A3 `statistical-analysis/SKILL.md` | Separar média/mediana, sazonalidade, extremo genuíno e erro; efeito prático e incerteza | **Aproveitar** | Útil em atraso, produtividade, salário e faturamento sem converter o trabalho inteiro em ciência de dados |
| A3 `statistical-analysis/SKILL.md` | Atalhos de amostra e descrição simplificada de significância | **Adaptar** | Não transformar “30 eventos por grupo” em garantia nem p menor que alfa em prova causal; K2 oferece desenho e dependência mais explícitos |
| A4 `validate-data/SKILL.md` | Junção que multiplica linhas, média de médias, período parcial, mudança de denominador e recálculo independente | **Aproveitar** | Catálogo diretamente aplicável a erros de planilhas empresariais; usar checagens que possam afetar o resultado |
| A4 `validate-data/SKILL.md` | Receita nunca negativa, percentuais sempre 0–100%, UTC universal e nunca média de médias | **Adaptar** | Devoluções/estornos e crescimento podem violar limites válidos; média ponderada com pesos corretos é possível; calendário comercial deve preservar fuso/corte apropriado |
| A5 + `domain-template.md` | Entidade, fórmula, fonte, filtros, relacionamentos e armadilhas por domínio | **Adaptar** | Depois de usos recorrentes, oferecer registrar definições da empresa na própria skill/referência; não criar memória ou pacote sem pedido |
| Anthropic `CONNECTORS.md` | Categoria de ferramenta como placeholder e alternativas por plataforma | **Adaptar** | Categoria não comprova ferramenta disponível; arquivos locais precisam funcionar como primeiro caminho quando não houver conexão |
| O1 `metric-diagnostics/SKILL.md` | Reproduzir a mudança antes de buscar causas; decompor taxas em numerador/denominador e separar composição de desempenho | **Aproveitar** | Evita inventar explicação para erro de medição ou crescimento só por aumento da base |
| O1 `metric-diagnostics/SKILL.md` | Contribuições aditivas com grupos exclusivos e residual declarado | **Aproveitar** | Explicação deve fechar com o total. Interações entre preço/volume/mix pedem convenção documentada; não somar efeitos sobrepostos |
| O1/O3 | Descobrir todas as fontes, notebook e relatório obrigatórios por padrão | **Adaptar** | Fazer busca só nas fontes necessárias e disponíveis; reprodutibilidade pode ser um script/cálculo pequeno. Não impor artefato para pergunta pontual |
| O2 `analyze-data-quality/SKILL.md` | Verificações escolhidas por uso, forma do dado, datas e risco de decisão | **Aproveitar** | Mais útil que escore genérico de qualidade. Retornos negativos podem ser válidos; auditar a regra de negócio antes de marcar erro |
| O2 | Recomendar automação apenas para regra estável, importante e sustentável | **Aproveitar** | Evita infraestrutura e scripts preventivos; executar checagem pontual primeiro, automatizar quando recorrência justificar |
| O3 `product-business-analysis/SKILL.md` | Começar pela decisão; escolher recortes que possam mudar a recomendação; dimensionar oportunidade | **Aproveitar** | Diferencia maior volume de maior oportunidade: comparar tamanho, margem, crescimento e capacidade de ação conforme o pedido |
| K1 `exploratory-data-analysis/SKILL.md` | Declarar limite de leitura, origem, valores ausentes, transformações e influência de extremos | **Aproveitar** | Um prefixo de linhas ordenadas não é amostra aleatória; não imputa, exclui ou extrapola silenciosamente |
| K1 `scripts/tabular_profile.py` | CLI local delimitado, tokens de ausência explícitos, limite de tamanho/linhas e saída agregada | **Adaptar** | Ganho real para arquivos repetidos. É wrapper dependente de `_capabilities`, `_common` e `_tabular`; copiar só esse script não reproduz o pacote |
| K1 | Formatos de laboratório, mascaramento total de identificadores e raiz explicitamente aprovada sempre | **Descartar do núcleo** | RH e vendas podem requerer identificação autorizada de entidades. A preocupação com exposição deve acompanhar o pedido e a entrega, sem impedir trabalho legítimo por regra de laboratório |
| K2 + `test_selection_guide.md` | Pergunta estatística, unidade de amostragem, pareamento, agrupamento, Welch, efeito e intervalo | **Aproveitar sob demanda** | Não tratar múltiplas linhas do mesmo funcionário como pessoas independentes; Mann–Whitney não é teste automático de mediana; diagnóstico de normalidade não escolhe teste sozinho |
| K2 | APA, Bayesianismo e ambiente científico completo | **Adaptar/descartar do padrão** | Linguagem empresarial primeiro; instalar ou usar biblioteca só para análise que precise dela. Dependências e versões declaradas não foram verificadas neste ambiente |
| B1 `data-analyst/SKILL.md` | Coortes/funil e estrutura observação, implicação e ação | **Referência conceitual** | Método útil, mas não copiar; licença restringe comercialização. Hipótese com limiar e SQL não são pré-requisitos para toda pergunta |
| B1 `scripts/data_profiler.py` | Perfil CSV/JSON com biblioteca padrão | **Não copiar** | Leitura integral mostrou carga em memória, tipos por >80% de parse numérico e flags por limiar fixo; pode tratar identificador numérico como medida, emitir valores textuais e marcar chave única como issue |
| D1 `business-analysis/SKILL.md` | Inventário de abas, reconciliação, lucro versus receita, concentração, descontos e capital de giro | **Adaptar** | Bom repertório de negócio sob demanda; não presumir que duas abas precisem produzir insight cruzado ou que toda análise de RH deva virar monetização |
| D1 `assets/profile_data.py` | Perfil único de todas as abas e candidatas a chaves de junção | **Adaptar ideia, não implementação** | Script imprime exemplos de células e primeiras linhas; atribui cardinalidade pela quantidade de distintos, que não prova unicidade |
| D1 | Nunca perguntar, nunca iterar análise, investigar todo módulo, limite de seções contraditório e 100/100 obrigatório | **Descartar** | Ambiguidade material exige pergunta; evidência inesperada exige iteração. Escore próprio não prova correção; roteiro fixo amplia tarefa e incentiva causalidade indevida |

## Achados verificáveis na leitura de código

### 1. Cardinalidade inferida incorretamente no profiler do Abdo

[assets/profile_data.py](https://github.com/AbdoBasyioni/business-analysis-skill/blob/e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae/assets/profile_data.py) compara conjuntos de valores para estimar sobreposição e emite `1:1` quando a quantidade de valores distintos de duas colunas é igual. Duas tabelas podem possuir os mesmos dois IDs repetidos em dez linhas cada; a igualdade de distintos permanece, mas a junção pode multiplicar linhas. É insuficiência demonstrada por inspeção da expressão, não por execução. Portanto, sobreposição é candidata a relacionamento; unicidade e contagens por chave devem ser verificadas separadamente.

### 2. O profiler borghei pode gerar falso diagnóstico de qualidade

[scripts/data_profiler.py](https://github.com/borghei/Claude-Skills/blob/4a698e8d07856fdca9ec3e69082a9d68c8dd45d0/data-analytics/data-analyst/scripts/data_profiler.py) considera numérica uma coluna se mais de 80% dos valores não nulos puderem virar `float`; não valida que seja medida em vez de ID. `POTENTIALLY_UNIQUE_KEY` entra em `quality_flags`, e a contagem `columns_with_issues` contabiliza qualquer flag. Uma chave bem formada pode ser contabilizada como issue. Não há limite de tamanho/chunk no carregamento nem validação explícita de finitude no parse mostrado. Nenhum desses limites foi testado em runtime.

### 3. K-Dense tem capacidade explícita, mas o wrapper não basta

[scripts/tabular_profile.py](https://github.com/K-Dense-AI/scientific-agent-skills/blob/a1043ef544e3a100c28e70a736b6cf32554d0677/skills/exploratory-data-analysis/scripts/tabular_profile.py) delega parsing, limites e emissão aos módulos importados. A consulta comprova o contrato exposto, não todas as garantias internas. Excel/Parquet são classificados como referência, não suporte automatizado direto no CLI descrito. Uma futura adaptação para empresa exigiria analisar a rotina real de I/O e a ferramenta de planilha disponível.

## Divergências que não devem ser misturadas

1. **Análise mínima versus projeto completo:** Anthropic `analyze` reconhece pergunta pontual; OpenAI exige relatório por padrão salvo dispensa explícita; Abdo exige BI completo e todos os módulos aplicáveis. Para o destino, adotar proporcionalidade: resposta direta quando suficiente, artefato quando pedido ou quando a decisão exigir material durável.
2. **Perguntar sempre versus nunca perguntar:** borghei impõe intake, Abdo impede perguntas de mapeamento. Adotar perguntar somente quando semântica, população, fonte ou período ambíguo mudar conta/conclusão; aproveitar documentos e conversa antes.
3. **Estatística simples versus inferência rigorosa:** A3 oferece linguagem acessível; K2 detalha desenho e limitações. Núcleo simples, referência rigorosa carregada ao comparar grupos, ler experimento ou quantificar incerteza.
4. **Outlier como erro versus observação importante:** referências consistentes favorecem investigar. Preservar dado original; separar erro confirmado, extremo válido e população distinta. Sensibilidade pode comparar resultado com/sem extremo, sem exclusão silenciosa.
5. **“Por quê” quantitativo versus causa real:** decomposição contábil explica componentes de uma variação; correlação e coincidência temporal não demonstram mecanismo causal. Rotular observado, explicação provável e hipótese operacional.
6. **Contexto empresarial durável versus análise pontual:** A5 é valiosa depois de detectar definições recorrentes. Oferecer adaptação da própria skill com regras de receita, folha, clientes ou pedidos quando útil; não transformar toda planilha em bootstrap de warehouse.

## Proposta para o futuro pacote, sem criação nesta etapa

### Núcleo curto

- Identificar a decisão/pergunta e usar o contexto já fornecido.
- Confirmar só lacunas materiais: significado, período, população, unidade/moeda e o que cada linha representa.
- Identificar fonte e cobertura; escolher método suficiente antes de ampliar exploração.
- Calcular com ferramentas disponíveis; manter dados originais e apontar limpeza/transformação efetuada.
- Verificar denominadores, períodos, junções, total e números que sustentam o achado.
- Entregar resposta primeiro, suporte essencial e limites que mudam a interpretação.
- Se houver padrão recorrente específico da empresa, oferecer registrar/adaptar contexto da própria skill.

### Referências carregadas por intenção

| Pedido reconhecido | Referência útil | Exemplo de trabalho empresarial |
|---|---|---|
| “Por que caiu/subiu?” | Diagnóstico e decomposição | Receita por preço/volume/mix; prazo por área; conversão por origem |
| “Os números não batem” | Reconciliação, chaves, filtros e corte | Vendas versus financeiro; pedidos versus itens; folha versus cadastro |
| “Quem concentra resultado/problema?” | Segmentação, concentração e coortes | Clientes, fornecedores, lojas, tipos de chamado; não somente produto digital |
| “Essa diferença é confiável?” | Desenho, testes, efeito e incerteza | Tempos antes/depois; pesquisa interna; experimento de processo |
| “O que esperamos nos próximos meses?” | Previsão simples, baseline, backtest e cenários | Demanda, atendimento, estoque, orçamento; declarar limites |
| “Use nossas definições daqui em diante” | Glossário e métricas do domínio | Receita líquida, pessoa ativa, turno, desconto, pedido cancelado |

### Scripts e dependências

Não há evidência de necessidade de scripts próprios para todo pedido. Ganhos concretos possíveis: perfil reutilizável de abas, checagem de chaves/junções, reconciliação de totais e decomposição repetida. Primeiro confirmar ferramenta existente e repetição do trabalho; depois avaliar script pequeno, sem recriar parser/engine de planilha.

CSV/JSON pode ter caminho com biblioteca padrão; Excel geralmente pede biblioteca ou ferramenta específica; inferência rigorosa pede bibliotecas apropriadas. Nada nesta pesquisa comprova disponibilidade no Studio. Uma futura skill deve explicar a dependência em linguagem de trabalho e, quando necessário, **oferecer preparar o ambiente**, sem exigir que a pessoa execute comando. Compatibilidade com Windows, locks, tamanho do pacote e guard Hermes serão verificados na fase de criação, não inferidos das licenças ou texto das candidatas.

## Pontos resolvidos e pendências materiais

Resolvidos: fontes diversas, tratamento de forks, SKILL completos, diferença entre exploração/diagnóstico/decisão, proporcionalidade, pitfalls de junção, limites dos profilers, núcleo versus referências e benefício condicionado de scripts.

Pendências para criação futura: licença verificável do conteúdo OpenAI caso se proponha cópia; escolha/inspeção de qualquer script a redistribuir; recursos transitivos e dependências; exemplos executados com dados sintéticos empresariais; contrato e runtime de destino. O dossiê é suficiente para a composição da pesquisa desta especialidade; não há justificativa para continuar ampliando candidatos apenas por contagem.

## Fontes de descoberta

- [skills.sh — validate-data, Anthropic](https://skills.sh/anthropics/knowledge-work-plugins/validate-data): diretório de descoberta; não usado como fonte única nem como prova de qualidade.
- [Anthropic — Data Analyst Plugin](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/README.md): orientação de família, com caveat de nomes históricos frente aos arquivos efetivamente consultados.
- [OpenAI — Data Analytics README](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/README.md): família atual descoberta; focados lidos no SHA, não presumidos a partir do README.
- [K-Dense — scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills): original atual; fontes pinadas de cada componente estão nas tabelas acima.

Estado: pesquisa documental registrada. Nenhum pacote criado, dependência instalada, skill executada, catálogo modificado, commit ou push feito por esta frente.
