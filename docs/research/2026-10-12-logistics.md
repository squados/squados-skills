# Analista de Logística — síntese da pesquisa

Rodada 28 do catálogo aprovado; consulta em 12/10/2026. Futura skill de uso interno para análise, planejamento e documentos de logística. Nenhuma contratação de frete, emissão, atendimento externo, alteração de operação ou execução de pacote ocorreu.

## Alcance e seleção

- [Transporte, frete e distribuição](2026-10-12-logistics-skills-transport.md): quatorze SKILL completos de quatro famílias, três recursos comportamentais, licenças e quatro fontes profissionais.
- [Operações logísticas](2026-10-12-logistics-skills-operations.md): onze SKILL completos de três famílias, nove recursos determinantes e licenças.
- [Métodos e casos](2026-10-12-logistics-methods.md): nove fontes profissionais/documentais, três materiais audiovisuais e três casos autorais, com níveis de acesso discriminados.

Domain Experts/logistics-analyst e vocabulary aparecem nas duas frentes; contar uma vez. Resultado: **24 SKILL distintos de seis famílias** — Kishor, Domain Experts, A5C, SkillsBench, AgentLogistics e Evos. Conteúdo declarativo, exemplos, forks e diretórios não são validações independentes.

Os métodos reúnem treze URLs profissionais contando as quatro adicionais da frente de transporte, mais três materiais audiovisuais. Artigos distintos DHL/ICC permanecem URLs distintas, sem virar autoridades independentes. SCOR teve extratos indexados, APQC acesso parcial; não houve leitura integral desses padrões/benchmarks. Uma transcrição pública GS1 de março/2026 foi consultada integralmente pela frente metodológica, sem timestamps e sem assistir ao vídeo. Os outros dois materiais ficaram em apresentação/ementa.

A coordenação leu os três dossiês integralmente, o artigo DHL Global Forwarding completo e os trechos decisivos de algoritmos Kishor e caso 8 Evos. Não executou código externo. Os gabaritos tiveram conferência aritmética própria.

## Componentes recomendados

| Componente e referência | Decisão para o pacote posterior | Ganho para o trabalho |
|---|---|---|
| Domain Experts: elegibilidade, custo completo e janela real | Adaptar a definição local, moeda, período e serviço | Comparar alternativas que atendem ao compromisso, antes do preço |
| Kishor: modal, consolidação, rede/frota e custo a servir | Adaptar perguntas e cenários, sem transportar calculadores | Reconhecer capacidade, espera, custos de transição e condições individuais |
| SkillsBench: regras traduzidas em restrições e revisão independente | Aproveitar conceitualmente sob demanda | Conferir carga, sequência, tempo e pedidos não atendidos de um plano candidato |
| A5C: campos de entrada/saída de rota, carga e auditoria | Aproveitar repertório; descartar promessas de capacidade pronta | Ter dados pertinentes não significa ter solver, tráfego ou encaixe 3D comprovado |
| AgentLogistics: estados, unidades, ondas e divergências | Adaptar para registros e produtividade existentes | Separar previsto, separado, carregado, recebido, inspecionado e liberado |
| Evos: exceções de devolução | Usar como leitura crítica, com política real | Não transformar exemplos de reembolso, fraude ou jurisdição estrangeira em padrão |
| GS1: unidade logística vinculada a documentos/eventos | Sob demanda para operação que usa/pede esse padrão | SSCC e GTIN identificam entidades diferentes; leitura não prova automaticamente conteúdo/condição |
| DHL: peso físico e base de cobrança | Conferir cotação/modalidade/região | Peso tarifável não é peso físico; divisor de um serviço não vale para todos |
| FedEx, SCOR e convenção local: entrega e indicadores | Adaptar com alcance da evidência explícito | Status, POD, quantidade e condição sustentam afirmações diferentes |

A [orientação DHL Global Forwarding](https://www.dhl.com/gb-en/home/global-forwarding/freight-forwarding-education-center/calculating-chargeable-weights.html) distingue modalidades e condições regionais, incluindo cobrança por contêiner em FCL. Seu exemplo não substitui fator, arredondamento e adicionais da cotação pertinente. O núcleo deve perguntar por esses dados somente quando alterarem a comparação.

## Falhas que orientam o descarte

Em [route-optimization Kishor](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/route-optimization/SKILL.md), a coordenação conferiu `nearest_neighbor_vrp`, `generate_neighbor`, annealing e `solve_mdvrp`: demanda individual impossível pode deixar o loop sem progresso; vizinhos não conferem capacidade; clusters não entram no solver por depósito. A constatação é estática, sem execução ou benchmark. Não incorporar esses exemplos como calculadora pronta.

Em [network-design](https://github.com/kishorkukreja/awesome-supply-chain/blob/397d95172e374225574f1fb580c1a77376fff836/skills/network-design/SKILL.md), o trecho de distância usa euclidiana em lat/lon ×69, apesar do comentário Haversine; o objetivo multiplica tarifa declarada por milha por fluxo de unidades. Não tratar isso como matriz viária ou custo de viagem validado. Outros achados de frota, frete e última milha ficam discriminados no dossiê, com escopo de leitura e sem demonstração runtime.

O [caso 8 de devoluções Evos](https://github.com/ai-evos/agent-skills/blob/1eda1feb184cfde82175d4ffa5feccf6501a4394/capabilities/returns-reverse-logistics/references/edge-cases.md) orienta preço documentado e também o menor entre preço de compra e atual. A coordenação confirmou a contradição nos trechos. Descartar a regra; a política real e decisões comerciais não se inferem de um exemplo.

AgentLogistics declara preview e avaliação ao vivo pendente. Parte dos fluxos é genérica e aponta recursos fora da pasta atômica. A5C declara integrações/capacidades sem demonstrá-las nos arquivos comparados. Licença ou presença de código não prova compatibilidade, segurança ou resultado.

## Padrão enxuto e progressivo

Reconhecer o pedido: cotação, gasto, rota, capacidade, fila, conferência, indicador, devolução ou procedimento. Aproveitar documentos, confirmar definições que mudam a decisão e entregar a menor resposta utilizável. Referências futuras podem reunir transporte/custo/capacidade, operações/indicadores e reversa; não criar WMS/TMS, menu de modos ou scorecard obrigatório.

Pedidos, linhas, produtos, volumes, remessas e viagens exigem vínculo e unidade explícitos. Indicadores têm corte, população, compromisso e tratamento de pendências. OTIF conta a interseção de prazo/completude no mesmo elemento; não multiplica percentuais agregados. Pedido perfeito pode incluir outras condições. Pedido dividido não se avalia como remessa única sem regra fornecida.

Na reversa, receber não significa liberar para venda; aprovação comercial não significa pagamento; orçamento não é gasto; recuperação possível não é receita. Separar custos comuns, incrementais e valores do produto para evitar dupla contagem. Consumo de dados de estoque/compras continua restrição e interface, sem iniciar essas especialidades automaticamente.

Scripts só com benefício concreto em volume/cálculo/recomputação, entradas verificáveis e modelo declarado. Heurística pode produzir candidato; viabilidade exige checar restrições, e ótimo requer condição/prova do modelo. Ferramenta ausente necessária recebe explicação simples e oferta de instalação com autorização. Preferência recorrente ou atrito pode motivar oferta de ajuste da própria skill, preservando políticas particulares na versão da equipe.

## Casos autorais e verificação

Os [três casos](2026-10-12-logistics-methods.md) são fictícios e ainda não foram executados contra uma skill. Python local próprio conferiu aritmética, sem código remoto:

1. Frete: carga 1,20 m³/160 kg. A custa R$652 e atende o prazo; B custa R$557,84, mas perde o corte; C não comporta volume; D custa R$700 e atende. A é recomendação condicionada às premissas, sem contratação realizada.
2. Entrega: OTIF confirmado de 1/4 pedidos = 25% e 3/6 linhas = 50%; P04 sem POD é pendência. Quantidade comprovada 46/60 não significa que as outras catorze foram perdidas. Denominador e corte ficam visíveis.
3. Reversa: custo incorrido R$170; cenário total R$255, com R$85 condicionais. Recuperação líquida incremental após reparo proposto R$135, sem venda/resultado técnico comprovados. Dez recebidas, seis vendáveis, quatro com disposição pendente; crédito aprovado não foi pago/lançado.

## Proveniência e estados

Pins, datas, licenças e recursos estão nas frentes. Famílias MIT e Apache observadas exigem preservar avisos pertinentes em eventual reutilização substancial. Padrões, papers, ICC e sites de transportadoras mantêm direitos próprios. Síntese autoral, sem cópia de pacotes, templates ou materiais protegidos; pesquisa não amplia a allowlist da galeria.

Ainda faltam desenho final, criação, avaliação com agente, compatibilidade/guard/proposta Hermes, instalação e uso real. Sem push, galeria ou espelho alterados. Não houve conta, emissão, pagamento ou chamada paga vidIQ. Fiscalidade, aduana, cadeia fria, carga perigosa e restrições locais precisam de fontes específicas quando um pedido concreto depender delas; esta pesquisa não oferece conformidade integral nesses assuntos.
