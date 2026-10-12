# Pesquisa de skills: transporte, frete, rotas e distribuição

Data de acesso: **12/10/2026**. Frente de pesquisa para uma futura skill **Analista de Logística**, de uso interno em negócios. Este documento compara conteúdo existente e propõe componentes; não cria, instala, executa ou publica a skill.

## Resultado e alcance

A combinação mais útil é o julgamento operacional de `domain-experts/logistics-analyst`, o enquadramento de custos e cenários de `awesome-supply-chain` e a tradução de regras verificáveis de `skillsbench`. O catálogo `babysitter` ajuda a descobrir entregas e campos, mas seus exemplos declarativos não demonstram as capacidades prometidas. Nenhum pacote deve ser incorporado inteiro: existem instruções e códigos ilustrativos incompatíveis com uma análise confiável e enxuta.

Foram lidos **14 SKILL.md completos, em quatro famílias originais**, além dos três recursos comportamentais referenciados por `logistics-analyst` e quatro arquivos de licença. A leitura inicial em lote de arquivos longos truncou; os cinco arquivos selecionados de Kishor foram relidos separadamente, e o trecho truncado de rotas foi recuperado. `distribution-center-network` teve leitura parcial e fica **fora das 14 leituras completas**. Foram consultadas quatro fontes profissionais primárias adicionais: Google OR-Tools, OSRM, DHL e ICC.

A busca usou `logistics`, `transportation`, `freight`, `route optimization`, `distribution`, `network design`, `carrier`, `load planning` e `SKILL.md`. SkillsMP e EliteAI serviram à descoberta; todos os julgamentos decisivos vêm de arquivos originais no GitHub. A busca também trouxe roteadores de skills/LLMs sem relação com transporte, descartados por contexto. A presença em diretório ou popularidade não valida o pacote.

Não foram usados login, contas, chaves, instalação, clone, execução remota, envio de dados, compra, contratação ou transação. A API GitHub anônima retornou limite de requisições; o SHA foi obtido com `git ls-remote` e o conteúdo foi lido diretamente de URLs raw fixadas nessa revisão. Não houve execução dos exemplos: os problemas de código abaixo são achados de inspeção estática.

### Revisões e licença verificadas

| Família original | Pin consultado | Data visível da revisão | Autoria/licença verificada | Limite |
|---|---|---|---|---|
| [kishorkukreja/awesome-supply-chain](https://github.com/kishorkukreja/awesome-supply-chain/tree/397d95172e374225574f1fb580c1a77376fff836) | `397d95172e374225574f1fb580c1a77376fff836` | 06/10/2026, página do commit | [LICENSE](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/LICENSE): MIT, copyright 2026 Kishor Kukreja | A licença do repo não relicencia papers e bibliotecas externas citadas. |
| [wonsukchoi/domain-experts](https://github.com/wonsukchoi/domain-experts/tree/0101c5456f7e4d718a5dd7657c4514448039a303) | `0101c5456f7e4d718a5dd7657c4514448039a303` | 12/10/2026, patch do commit | [LICENSE](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/LICENSE): MIT, copyright 2026 Wonsuk Choi e contributors | Papel marcado `maturity: draft`; não é certificação profissional. |
| [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter/tree/feb68abe397acc14f32b34984975c48fedba2b33) | `feb68abe397acc14f32b34984975c48fedba2b33` | 31/08/2026, página do commit | [LICENSE.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/LICENSE.md): MIT, copyright 2025 A5C AI | A tentativa inicial `/LICENSE` deu 404; o arquivo correto é `LICENSE.md`. |
| [benchflow-ai/skillsbench](https://github.com/benchflow-ai/skillsbench/tree/9a1f4dd5f7659f75707435da3ce854b6e48321d1) | `9a1f4dd5f7659f75707435da3ce854b6e48321d1` | 23/07/2026, patch do commit | [LICENSE](https://github.com/benchflow-ai/skillsbench/blob/9a1f4dd5f7659f75707435da3ce854b6e48321d1/LICENSE): Apache-2.0 | A skill foi lida; o benchmark completo e suas dependências não foram auditados/executados. |

Datas acima pertencem ao commit do repo, não à última modificação de cada skill. Datas de agregadores podem divergir: SkillsMP mostrava atividade de janeiro/2026 para frete, enquanto o repo consultado já contém revisão de outubro. Para commits de merge, a primeira data de um `.patch` pode ser de um commit interno; por isso Kishor e A5C usam `authoredDate`/`committedDate` da página do SHA, e não a primeira data do patch.

Esses quatro repositórios não estão na allowlist `github` atual da galeria do SquadOS. Pesquisa e possível síntese autoral não significam que se possa simplesmente adicioná-los ao índice. Se houver reprodução substancial no futuro, preservar autoria, licença e avisos, com avaliação do pacote exato; este dossiê usa paráfrases e análise própria.

## Inventário das leituras completas

Cada link aponta para o arquivo efetivamente consultado, fixado por SHA.

| # | Skill e arquivo original | O que resolve e contribuição | Método, entrega e custo | Julgamento |
|---|---|---|---|---|
| 1 | [logistics-analyst/SKILL.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/SKILL.md) | Escolha de modal, comparação de transportadoras, auditoria de frete, tendência por corredor. | Decisão pelo custo completo e janela do cliente; memo com componentes e evidência. Markdown com três refs; sem execução embutida. | **Adaptar**: melhor núcleo profissional; contextualizar unidades, termos e definições. |
| 2 | [freight-optimization/SKILL.md](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/freight-optimization/SKILL.md) | Modal, consolidação, milk run, carregamento, seleção/RFP. | Checklist amplo e exemplos Python com tarifas/pesos norte-americanos; pandas/numpy/scikit-learn. Relatório de gastos e oportunidades. | **Adaptar** método; **descartar** benchmarks e scripts como padrão executável. |
| 3 | [route-optimization/SKILL.md](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md) | Distingue TSP, VRP, capacidade, janelas, múltiplos depósitos e pickup/delivery. | MIP, heurísticas, metaheurísticas e exemplo OR-Tools; relato com sequência, duração e carga. | **Adaptar** classificação e campos; **descartar** implementação sem reparo/validação. |
| 4 | [network-design/SKILL.md](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/network-design/SKILL.md) | Centralizar/descentralizar CDs, direto/híbrido, greenfield/brownfield. | Custos fixos, transporte, estoque e serviço; cenários e sensibilidade; MIP ilustrativo com PuLP. | **Adaptar** cenários e custo a servir; **descartar** aproximações como prova de viabilidade. |
| 5 | [fleet-management/SKILL.md](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/fleet-management/SKILL.md) | Dimensionamento, frota própria/locada, substituição, ociosidade e manutenção. | Percentil da demanda, filas, simulação e TCO; numpy/scipy/simpy. | **Adaptar** decomposição e cenários; **descartar** calculadores numéricos atuais como fundamento. |
| 6 | [last-mile-delivery/SKILL.md](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/last-mile-delivery/SKILL.md) | Custo por entrega, primeira tentativa, densidade, acesso, janelas e retirada. | Análise de concentração geográfica e alternativas de serviço, com benchmarks e ROI ilustrativos. | **Adaptar** mecanismos; **descartar** resultados fixos, API genérica e robôs como padrão. |
| 7 | [route-optimization-engine/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/route-optimization-engine/SKILL.md) | Descoberta dos campos de rota: parada, janela, serviço, capacidade, disponibilidade. | Declara otimização/tempo real e cita OR-Tools/VROOM/OSRM/HERE; YAML de entrada/saída. | **Adaptar** esquema de dados; **descartar** promessa automática de tráfego/compliance/ótimo. |
| 8 | [carrier-selection-optimizer/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/carrier-selection-optimizer/SKILL.md) | Comparar capacidade, serviço, custo, contrato e spot. | Lista de capacidades e exemplo declarativo; depende de TMS/dados de rating/APIs. | **Adaptar** elegibilidade e comparação; score/pesos só se pertinentes e explicáveis. |
| 9 | [transportation-spend-analyzer/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/transportation-spend-analyzer/SKILL.md) | Gastos por corredor, modal, transportadora e período; adicionais. | Cubo de gastos, contrato vs. spot e custo×serviço; sugere benchmarks comerciais. | **Aproveitar** segmentação; **adaptar** oportunidade/economia; **descartar** benchmark sem acesso. |
| 10 | [network-optimization-modeler/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/network-optimization-modeler/SKILL.md) | Custo a servir, capacidade, localização, cenários, risco. | Entradas/saídas exemplificadas; cita solvers comerciais e GIS. | **Adaptar** comparação de cenários; exemplos são desenho, não simulação demonstrada. |
| 11 | [load-optimization-calculator/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/load-optimization-calculator/SKILL.md) | Peso, volume, empilhamento, incompatibilidade e ordem de descarga. | Declara 3D packing; lista py3dbp/rectpack/solvers; exemplo de posições. | **Aproveitar** restrições; **descartar** sugestão de encaixe 3D comprovado sem solver/validação. |
| 12 | [freight-audit-validator/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/freight-audit-validator/SKILL.md) | Divergência de tarifa, peso, adicionais, duplicidade e recuperação. | OCR/EDI/plataformas citados, classificação de diferença, exemplo com autoaprovação. | **Adaptar** registro de divergências; **descartar** pagamento/autoaprovação/claim enviado. |
| 13 | [incoterms-compliance-checker/SKILL.md](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/business/logistics/skills/incoterms-compliance-checker/SKILL.md) | Internacional: custo, risco, local nomeado, seguro e formalidades. | Exemplo CIF com HS, impostos e custo posto; sugere APIs de compliance. | **Adaptar** separação custo/risco; **descartar** taxas/classificações fixas e garantia de compliance. |
| 14 | [logistics-rules-to-optimization/SKILL.md](https://github.com/benchflow-ai/skillsbench/blob/9a1f4dd5f7659f75707435da3ce854b6e48321d1/tasks/bike-rebalance/environment/skills/logistics-rules-to-optimization/SKILL.md) | Traduz regras de operação em conservação, capacidade, vinculação, sequência e incompatibilidade. | Estado de carga, janela, atendimento dividido; exige recomputar resultado independentemente. Código voltado à modelagem matemática. | **Aproveitar** tradução/checagem; **adaptar** fórmulas para referência sob demanda. |

Os cinco pacotes Kishor selecionados e `route-optimization-engine` A5C tiveram estrutura da pasta consultada no GitHub: os exemplos necessários estão no próprio Markdown, sem recursos auxiliares exibidos na pasta. Os demais A5C citam processos externos e ferramentas; foram lidos os SKILL.md completos, mas não toda a orquestração JavaScript/TMS da família. Portanto, a comparação cobre o comportamento declarado das skills, não a segurança/funcionalidade do sistema externo completo.

### Recursos determinantes lidos integralmente

| Fonte/arquivo | Contribuição | Decisão e motivo |
|---|---|---|
| [logistics-analyst/references/playbook.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/references/playbook.md) | Custo componente a componente, janela efetiva do cliente, auditoria de fatura e memo preenchido. | **Adaptar** como exemplos curtos: definição de OTIF depende do contrato; custo completo de transporte não deve ser confundido com custo posto de importação. |
| [logistics-analyst/references/red-flags.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/references/red-flags.md) | Sinal → hipótese → primeira pergunta → dado de confirmação. | **Aproveitar** estrutura diagnóstica, sem transformar “geralmente significa” em conclusão causal. |
| [logistics-analyst/references/vocabulary.md](https://github.com/wonsukchoi/domain-experts/blob/0101c5456f7e4d718a5dd7657c4514448039a303/roles/logistics-analyst/references/vocabulary.md) | Definição em contexto e erro comum para freight terms. | **Adaptar** vocabulário PT-BR, com LTL/FTL/NMFC apresentados como contexto dos EUA, não regra universal brasileira. |

## Deduplicação e qualidade de evidência

SkillsMP aponta para o arquivo original de Kishor; EliteAI aponta para A5C. Não são autores adicionais nem replicações de resultado. As sete skills A5C usam a mesma estrutura declarativa e pertencem a uma família; as cinco Kishor compartilham estilo, exemplos sintéticos e dependências. **14 arquivos não equivalem a 14 validações independentes.** Não apareceu evidência suficiente de cópia entre as quatro famílias para afirmar derivação, mas métodos comuns de OR não contam como descobertas independentes.

O papel Wonsuk oferece um exemplo aritmético preenchido e referências úteis. Kishor oferece código e dados aleatórios, mas “working implementations” no README não demonstra execução correta para nossos pedidos. A5C descreve capacidades, integrações e resultados de exemplo: não traz, nesses SKILL.md, algoritmo, credenciais, dados de tráfego ou evidência de execução que materialize as promessas. SkillsBench usa uma skill dentro de uma tarefa de benchmark; a existência do benchmark não comprova que esta skill sozinha resolveu um problema de negócio nem que suas regras cobrem todo VRP.

## Componentes a aproveitar, adaptar e descartar

### Julgamento e custos

| Fonte/arquivo → componente | Decisão | Motivo e adaptação aplicável |
|---|---|---|
| Wonsuk SKILL + playbook → elegibilidade por perfil, janela e custo completo | **Adaptar** | Filtrar opções que atendem a necessidade antes de ranquear. Abrir base, combustível, pedágio, adicionais, seguro, embalagem/manuseio, reentrega e custos de falha quando aplicáveis e disponíveis. Separar cotação confirmada de estimativa histórica. |
| Wonsuk SKILL → faixas de peso e “20–30 embarques/um mês” | **Descartar como regra fixa** | EUA e ilustração; amostra mínima depende da decisão, dispersão, risco e segmento. Mostrar quantidade, cobertura e variabilidade, sem fabricar limiar estatístico universal. |
| Kishor freight → seleção de modal e consolidação | **Adaptar** | Usar tarifas contratuais/vigentes e perfil real. “Mais barato” só entre alternativas viáveis; consolidar exige respeitar disponibilidade, prazo de cada pedido, transit time e capacidade. |
| Kishor freight → tarifs/savings/benchmarks embutidos | **Descartar** | Preços, percentuais e volumes exemplificativos não vêm do negócio, da moeda ou de mercado verificado. Não preencher lacuna com benchmark genérico. |
| A5C spend → corredor×modal×transportadora×período | **Aproveitar** | Melhor unidade de análise para reconhecer concentração e causa de custo. Comparações requerem mesmo perfil, período, moeda e escopo de custo. |
| A5C carrier → pontuação multicritério | **Adaptar** | Serviço mínimo e capacidade são restrições quando obrigatórios; pesos só agregam preferências graduais. Um score não pode compensar proibição operacional ou violação de prazo. |
| A5C audit + Wonsuk → divergências com documento/contrato | **Adaptar** | Apontar item, valor cobrado, regra aplicável, evidência, cálculo e pendência. Produzir rascunho revisável de contestação, sem enviar, liberar pagamento ou alterar contrato. Ausência no BOL isoladamente não prova cobrança indevida. |

### Rotas, carregamento e rede

| Fonte/arquivo → componente | Decisão | Motivo e adaptação aplicável |
|---|---|---|
| Kishor route → classificação TSP/VRP/janelas/pickup-delivery | **Adaptar** | Escolher método pelo pedido, escala e dados. Não forçar solver quando basta comparar cenários ou organizar sequência manualmente. |
| A5C route → tempo de serviço por parada | **Aproveitar** | Duração operacional inclui deslocamento, espera, atendimento, carga/descarga, pausas e retorno; distância sozinha não comprova rota executável. |
| SkillsBench → estado e validação independente | **Aproveitar** | Recalcular carga em cada trecho, atendimento, precedência, janelas, duração e custo; listar pedidos não atendidos. Uma resposta plausível sem checagem é só candidata. |
| A5C load → empilhamento, compatibilidade, ordem de descarga | **Aproveitar** | Volume somado suficiente não prova encaixe físico. Peso total suficiente não prova distribuição por eixo. Para plano real, validar restrições/medidas e limite aplicável com responsável. |
| Kishor network → as-is/brownfield/greenfield, custos e serviço | **Adaptar** | Comparar configuração atual com poucas alternativas pertinentes. Somar custos de transição e capacidade de pico, não só média anual. Horizonte/unidade iguais entre custos fixos e fluxo. |
| Kishor network → lei da raiz quadrada para estoque | **Adaptar somente como aproximação** | Depende de hipóteses; não extrapolar a redes correlacionadas, diferentes lead times ou mixes sem explicitar limites. Não substituir análise de estoques. |
| Kishor last-mile → tentativas, densidade, acesso, serviço | **Adaptar** | Usar também negócios B2B, distribuição regional, coletas e áreas rurais. Entrega fracassada custa e consome capacidade, mesmo sem receita/conclusão. |
| Kishor fleet → frota base e capacidade flexível de pico | **Adaptar** | Útil para escolher própria/terceira/locada; considerar jornada, disponibilidade real e manutenção. Média de utilização isolada não autoriza corte de frota. |
| A5C Incoterms → custo separado de risco | **Adaptar sob demanda** | Só quando comércio internacional/contrato exigir; registrar versão, termo, local nomeado, transporte e partes. Não usar matriz simplificada como contrato ou aconselhamento jurídico. |

### Achados estáticos que impedem reaproveitar os scripts como estão

| Arquivo e âncora verificável | Achado concreto | Consequência para futura skill |
|---|---|---|
| [route-optimization, `nearest_neighbor_vrp`, linha 227](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md#L227) | `while unvisited` externo continua quando não existe cliente que cabe; sai apenas do loop interno, adiciona rota vazia e não remove a demanda impossível. | Pedido individual acima da capacidade pode impedir progresso. Validar inviabilidade/progresso antes de rodar qualquer algoritmo semelhante. |
| [route-optimization, `generate_neighbor`, linha 501](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md#L501) | Recebe `demands`/`capacity`, mas troca/realoca sem usar esses parâmetros; annealing aceita por custo/distância. | Menor distância pode vir de solução acima da capacidade. Validar todos os vizinhos ou resultado e nunca chamar isso de rota viável sem prova. |
| [route-optimization, `solve_mdvrp`, linha 678](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md#L678) | Itera clusters, mas chama solver com a matriz e demandas globais, sem recortar clientes nem ajustar depósito. | Não materializa a separação por depósito que o texto promete. |
| [route-optimization, `solve_vrp_ortools`, linha 1079](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md#L1079) | Exemplo configura custo de arco; não configura dimensões de capacidade/janela e extrai `solution` sem checar ausência. | Nome VRP e uso de biblioteca não comprovam restrições de negócio. |
| [network-design, `_calculate_distances`, linha 574](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/network-design/SKILL.md#L574) | Comentários dizem great-circle/Haversine, mas o cálculo é distância euclidiana lat/lon multiplicada por 69. | Nem distância viária nem Haversine implementada; não usar como quilômetros/milhas executáveis. |
| [network-design, objetivo, linha 614](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/network-design/SKILL.md#L614) | `transport_rate` declarado $/mile é multiplicado por milhas e fluxo de unidades; não há transformação de unidades em cargas. | Dimensão de custo incoerente se tarifa por viagem for tratada como tarifa por unidade. |
| [freight-optimization, consolidação, linha 316](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/freight-optimization/SKILL.md#L316) | Usa `due_date.max()` do grupo e `ready_date.min()`, não demonstra cumprimento de todos os prazos/disponibilidades; economia em linha 342 usa custos fixos fictícios. | Não prometer consolidação possível/economia demonstrada com essa regra. |
| [freight-optimization, cost score, linha 658](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/freight-optimization/SKILL.md#L658) | Normalização divide por máximo−mínimo sem tratar preços idênticos. | Scores podem ser indefinidos justamente quando custo não diferencia. |
| [fleet-management, TCO, linha 343](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/fleet-management/SKILL.md#L343) e [linha 359](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/fleet-management/SKILL.md#L359) | Soma depreciação no total anual e depois adiciona aquisição e deduz residual novamente no custo de posse. | Duplica a parcela aquisição−residual. Não comparar compra/locação por esse resultado. |
| [fleet-management, simulação, linha 192](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/fleet-management/SKILL.md#L192) | `arrival_time` é passado ao processo, mas não usado para aguardar; gerador cria processos com `timeout(0)`. | Tempos de chegada declarados não governam a simulação; dimensionamento seria outro problema. |
| [last-mile-delivery, janela, linha 287](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/last-mile-delivery/SKILL.md#L287) | Calcula eficiência histórica, mas devolve sucesso/preço predefinidos. | Não é estimativa aprendida dos dados. |
| [last-mile-delivery, ROI microhub, linha 486](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/last-mile-delivery/SKILL.md#L486) | Docstring define demanda anual e depois multiplica por 365; acrescenta prêmio fixo por entrega. | Periodicidade pode inflar benefício. Tratar inputs e horizonte explicitamente. |

O coordenador desta pesquisa também conferiu os trechos decisivos de não progresso/capacidade/multidepósito e de unidades/distância na rede. Inspeção estática não é execução reproduzida, benchmark ou auditoria completa. Estes achados justificam aprender com os componentes conceituais e escrever cálculos mínimos próprios quando necessários.

## Fontes profissionais que resolvem lacunas

| Fonte primária, autoria e data | Conteúdo efetivamente consultado | Aplicação e limites |
|---|---|---|
| [Google OR-Tools: Vehicle Routing](https://developers.google.com/optimization/routing), Google; página atualizada em 22/01/2025 | Guia web, variantes/restrições e limitações de solução. | Solver de rotas pode devolver solução boa sem provar ótimo. Relatar método, restrições efetivamente modeladas e condição da solução. Documentação CC-BY-4.0, exemplos Apache-2.0 segundo rodapé. Sem instalar/rodar solver. |
| [OSRM API 5.24.0: Table](https://project-osrm.org/docs/v5.24.0/api/#table-service), projeto OSRM; versão visível 5.24.0, sem data editorial confirmada | Documentação das matrizes, unidades, perfil e células sem rota/fallback. | Matriz de tempos usa segundos, distância usa metros; distância é a da rota mais rápida e não necessariamente menor distância. Célula `null` precisa de tratamento; perfil/data de origem importam. Não foi chamada API com endereço real. |
| [DHL: Weight and Dimensions](https://www.dhl.com/discover/en-gb/ship-with-dhl/products-and-services/weight-and-dimensions), DHL Express product team, 21/11/2023 | Página de peso real, dimensional e exemplo. | Neste serviço o divisor publicado é 5.000 para cm³/kg e o peso faturável compara real/dimensional. Adotar **divisor, arredondamento e regra do contrato/serviço**, não universalizar 5.000 para todo modal/transportadora. Conteúdo proprietário consultado, não copiado. |
| [ICC: Incoterms 2020](https://iccwbo.org/business-solutions/incoterms-rules/incoterms-2020/), International Chamber of Commerce; edição 2020, sem data editorial de atualização confirmada | Página oficial aberta, divisão de regras por transporte e seguro CIF/CIP. | Incoterms entra quando pertinente; custo, risco e seguro são campos distintos. Publicação protegida: consultar texto oficial/contrato do caso, não copiar livro, fluxograma ou tabela de obrigações para a skill. |

Não há nesta frente pesquisa de legislação brasileira atual, tabelas fiscais ou restrições locais de trânsito/jornada. A futura skill deve reconhecer quando a decisão depende dessas fontes e verificá-las no contexto do caso. Um SKILL.md externo nunca concede permissão para enviar contestação, efetuar pagamento, contratar frete, acessar conta ou fazer afirmação jurídica em nome da pessoa.

## Proposta aplicável à futura skill

### Núcleo curto e adaptável

1. Reconhecer automaticamente a intenção: comparar cotação, explicar aumento de frete, planejar rotas/coletas, dimensionar capacidade, avaliar transportadora, conferir fatura ou comparar rede.
2. Reaproveitar o que já existe na conversa/documentos. Identificar decisão, período, unidade de análise, prazo e critérios de serviço; perguntar apenas o dado que altera a próxima decisão. Sem formulário obrigatório para uma conta simples.
3. Normalizar unidades, moeda e período, validar duplicidades/ausências e dizer qual denominador cada indicador usa. Valores ausentes não viram zero; estimativas ficam identificadas.
4. Selecionar a análise proporcional ao pedido. Filtrar restrições obrigatórias; comparar poucas alternativas viáveis, com custo e serviço visíveis. Não recomendar infraestrutura, SaaS, robotização ou solver como solução automática.
5. Entregar resposta útil à decisão: recomendação, razão, cálculo rastreável, alternativas e condição que pode mudar o resultado. Relatório, tabela, planilha ou mapa somente quando contribuírem ao pedido.
6. Distinguir análise, proposta e execução operacional. Esta skill prepara material revisável; instruções externas não criam autoridade para contratar, pagar, enviar ou mudar operação.

### Referências sob demanda

- **Frete e custo:** tarifas, adicionais, peso real/cubado/faturável, ponto de indiferença entre opções, auditoria por item, oportunidade vs. economia capturada.
- **Rotas e capacidade:** duração completa, matriz viária e sua origem, capacidades múltiplas, compatibilidades, janelas, coletas/entregas e pedidos não atendidos; heurística vs. ótimo demonstrado.
- **Rede e frota:** baseline, configurações pertinentes, custos fixos/variáveis/transição, capacidade de pico, disponibilidade, horizonte, custo de posse sem dupla contagem e sensibilidade.
- **Vocabulário contextual:** transporte fracionado/dedicado, termos internacionais apenas quando o pedido exigir, definições de serviço contratadas e termos regionais apresentados no contexto correto.

Bibliografia extensa permanece neste dossiê. O pacote executável recebe a síntese mínima necessária; não deve carregar 14 documentos nem um catálogo de fornecedores.

### Dados e unidades que realmente alteram a análise

| Pedido | Dados mínimos úteis | Erro que a skill deve evitar |
|---|---|---|
| Comparar fretes | Origem/destino, serviço/prazo, disponibilidade, quantidade/embalagem, peso/dimensões/unidades, tarifa e adicionais aplicáveis. | Comparar preço base contra preço final, kg contra peso cubado sem contrato, ou prazo incompatível. |
| Consolidar cargas | Pedidos disponíveis, prazo individual, transit time, destino, capacidade de peso/volume/piso, incompatibilidade e custo de espera. | Usar prazo mais tardio do grupo como autorização de atraso dos demais. |
| Montar rota | Paradas/localizações confirmadas, demanda por dimensão, veículos disponíveis, partida/retorno, janelas, tempo de serviço, matriz/estimativas e restrições. | Usar distância em linha reta como tempo viário, ignorar retornos/espera/coletas ou ocultar pedidos excluídos. |
| Analisar gasto/transportadora | Dados de remessa e faturamento conciliáveis, período/moeda, perfil de corredor/modal, serviço efetivo e exposição. | Média geral esconder mix; somar economia de iniciativas que se sobrepõem. |
| Dimensionar frota | Histórico de demanda/carga e duração, dias/jornadas, disponibilidade/manutenção, capacidade por tipo e nível de serviço. | Frota baseada só em demanda média ou soma de carga sem tempo de ciclo. |
| Avaliar rede | Demanda por região/período, instalações fixas/candidatas, custos/capacidades comparáveis, serviço e restrições de mudança. | Tarifa por viagem multiplicada por unidades; custos anuais comparados com fluxo mensal sem conversão. |

Peso dimensional é uma regra de faturamento; não substitui peso físico no limite do veículo. Capacidade de armazenamento, throughput e expedição também não são a mesma grandeza. Utilização por peso, volume, posição/pallet e tempo devem aparecer separadas quando relevantes; uma média composta pode esconder a restrição dominante. Cubagem de frete e encaixe tridimensional têm perguntas diferentes.

### Exemplos autorais de comportamento desejado

- **“Qual dessas duas cotações compensa?”** Usar os anexos, identificar escopo do serviço e prazo, somar componentes conhecidos e separar adicionais incertos. Se uma opção não cumpre a data, mostrar isso antes de discutir diferença de preço. Se a diferença depende de peso faturável ausente, perguntar só esse dado.
- **“Nosso frete ficou caro.”** Comparar períodos equivalentes por corredor/modal/perfil; separar tarifa, combustível/adicionais, volume, peso cubado, mix e falhas/reentregas. Indicar contribuição dos fatores, sem atribuir causalidade a uma média.
- **“Organize estas entregas de amanhã.”** Produzir plano candidato com sequência, carga, horário e exceções. Se não houver matriz viária, declarar premissa e evitar ETA preciso; se uma demanda exceder a capacidade, identificar a incompatibilidade antes de tentar ordená-la.
- **“Vale ter mais um CD?”** Comparar rede atual e a alternativa concreta com horizonte comum, custo a servir, capacidade/serviço e custos de transição. Fazer sensibilidade das hipóteses que podem inverter a decisão. A recomendação não aprova investimento nem realiza mudança operacional.

### Scripts: somente quando o ganho for concreto

O núcleo pode funcionar com texto e tabelas. Para muitas remessas, um cálculo reproduzível de normalização, conciliação de faturas ou agregação por corredor pode reduzir erro e trabalho. Antes de adicionar script, explicitar o ganho, o formato de entrada, validações e disponibilidade da dependência. Evitar biblioteca/solver/API por padrão.

Para rotas, qualquer script futuro deve retornar situação da solução, paradas não atendidas, método, limites de busca e validação independente. Heurística só recebe rótulo de plano viável depois de checar restrições; “ótimo” depende de prova/condição do solver para o modelo explicitamente declarado. Mesmo ótimo do modelo não prova que endereço, tráfego, tarifa ou restrição real estejam corretos. Não inventar roteiro viário, código executado ou economia obtida.

## Lacunas e limite da entrega

- `distribution-center-network` foi identificado e parcialmente lido; sua amplitude não adicionou dúvida material além de `network-design`, por isso não expandido nem contado como análise integral.
- Não foi demonstrada execução de pacote, algoritmo ou pedido real em ambiente do Studio. Não foram preparados Hermes, dependências, proposta de contratação, instalação ou aprovação.
- Exemplos quantitativos das fontes são didáticos; não existem aqui tarifas de uma empresa, matriz viária do caso, dados de fatura, desempenho operacional nem SLA aprovado.
- Comércio internacional, fiscalidade, mercadoria perigosa, cadeia fria e jornadas/restrições locais exigem contexto e fontes próprias. O documento identifica o encaminhamento e não oferece parecer desses assuntos.
- Os quatro originais permitem estudar componentes, mas a redistribuição de conteúdo específico e a compatibilidade de qualquer pacote futuro devem ser verificadas na criação. A documentação de ferramentas comerciais e os materiais ICC/DHL não ganham licença MIT por serem citados.

Esta frente está consolidada como pesquisa documental: fontes originais, revisões, licenças, componentes úteis, descarte motivado e limites. A futura skill e sua validação com pedidos reais permanecem uma etapa posterior.
