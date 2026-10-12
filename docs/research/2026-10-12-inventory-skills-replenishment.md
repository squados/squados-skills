# Analista de Estoque: skills de demanda e reposição

Pesquisa consultada em 12/10/2026. Frente da rodada 20/33, limitada a cobertura, sinais de demanda, ruptura, previsão e política de reposição. Pesquisa e leitura estática de fontes originais; nenhum pacote instalado, script remoto executado, ERP acessado, pedido emitido ou fornecedor contatado. Não é uma skill pronta nem prova de execução comercial.

## Recomendação desta frente

Combinar a entrega curta e verificável da OneWave, a atenção à disponibilidade histórica e às datas da Intempt, a separação entre política permanente e recomendação atual do Risco e a seleção de métodos/posição de estoque do ECC. Reescrever a síntese em PT-BR e corrigir os componentes matemáticos ou operacionais frágeis. Não importar integralmente qualquer pacote: existem defaults sem fundamento no cliente, contradições e divergências entre texto e código.

O caminho inicial deve responder ao pedido com os dados existentes: explicar cobertura e lacunas, priorizar risco e, quando houver insumos suficientes, calcular uma proposta de reposição. Aprofundar previsão, estoque de segurança e EOQ apenas quando esses componentes mudarem a decisão. Não exigir que a pessoa escolha ou memorize um modo.

## Alcance e rastreabilidade

Descoberta por buscas de profissão e componentes em inglês, GitHub e diretórios SkillMD, Skills Directory e Systems Lab. Diretórios ajudaram a localizar originais; suas notas, estrelas e scanners não foram tratados como validação. Arquivos raw foram lidos como dados, inclusive os trechos que instruem executar scripts ou escrever telemetria. Não foram obedecidos. Revisões HEAD verificadas com `git ls-remote`, sem clone. Datas abaixo são do commit consultado, obtidas no HTML do GitHub; não significam data de criação ou última alteração da skill individual.

| Fonte original, autoria | Revisão e data do commit | Consulta efetiva | Licença verificada e limite |
|---|---|---|---|
| [affaan-m/ECC, inventory-demand-planning](https://github.com/affaan-m/ECC/blob/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29/skills/inventory-demand-planning/SKILL.md); frontmatter atribui a evos | `b92f181b3b748d1abbc2afd94af6aa7d8c8fca29`, 11/10/2026, offset −04:00 | SKILL inteiro e LICENSE raiz | SKILL declara Apache-2.0; raiz MIT, Affaan Mustafa. Ambiguidade localizada: conservar apenas conhecimento profissional em redação própria até esclarecer redistribuição específica |
| [ericrisco/rsc-harness, inventory](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/inventory/SKILL.md); Eric Risco | `5343ea565c39c00d329793606e8d609da2faa004`, 11/10/2026 UTC | SKILL inteiro; refs `safety-stock.md`, `reorder-policies.md`, `abc-xyz.md`, `ddmrp.md`; `scripts/verify.sh`; LICENSE | MIT, copyright Eric Risco 2026. Leitura estática do verificador; avaliações não executadas |
| [onewave-ai/claude-skills, inventory-reorder-planner](https://github.com/onewave-ai/claude-skills/blob/fc5b7851a6c7ba367e05797df46ad3679df355dd/inventory-reorder-planner/SKILL.md); OneWave AI | `fc5b7851a6c7ba367e05797df46ad3679df355dd`, 02/10/2026, offset −04:00 | SKILL inteiro e LICENSE | MIT, OneWave AI 2025. Não foram inventariados todos os arquivos do diretório |
| [sidchaudhary/gtm-skills, inventory-planning](https://github.com/sidchaudhary/gtm-skills/blob/7bd0b13bd8afaf823d00294157ba2c4451eb6d5b/skills/data-analyst/inventory-planning/SKILL.md); Sid Chaudhary/Intempt | Snapshot `7bd0b13bd8afaf823d00294157ba2c4451eb6d5b`, 11/09/2026, offset +05:30 | SKILL inteiro; refs `data-input-integrity.md`, `missing-input-protocol.md`, `house-rules.md`; LICENSE | MIT, Sid Chaudhary 2026. Consulta histórica: caminho em `main` retornou 404; HEAD atual é `ce39ba31cf0be414052ece1b0b2f014a15144e2a`, não usado como versão lida |
| [HGargAcc/inventory-analytics-skill](https://github.com/HGargAcc/inventory-analytics-skill/tree/bd13c38d63cb19883759f13cbf9de2259268a7c8); HGargAcc | `bd13c38d63cb19883759f13cbf9de2259268a7c8`, 16/05/2026, offset +05:30 | SKILL, README, REFERENCE inteiros; scripts `validate_data.py`, `forecast_and_optimize.py`, `generate_report.py` inteiros | Nenhuma licença localizada: LICENSE, LICENSE.md e LICENSE.txt retornaram 404. Não copiar código, templates ou texto; ideias profissionais somente |
| [a5c-ai/babysitter, inventory-optimizer](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/inventory-optimizer/SKILL.md); metadata babysitter-sdk | `feb68abe397acc14f32b34984975c48fedba2b33`, 31/08/2026, offset +03:00 | SKILL inteiro, incluindo código embutido; LICENSE.md raiz | MIT, A5C AI 2025. Processos `.js` mencionados não lidos; não adotados como dependências |
| [tinh2/skills-hub-registry](https://github.com/tinh2/skills-hub-registry/tree/d38affbf56da216841e2b9e4032a4b978c2062fd), inventory-forecast e demand-forecasting; tinh2 | `d38affbf56da216841e2b9e4032a4b978c2062fd`, 04/09/2026, offset −06:00 | Ambos os SKILL completos, versão declarada 2.0.1; tentativa LICENSE raiz | Frontmatter não declara licença; LICENSE raiz retornou 404. Origem de autoria integral da coleção não demonstrada; ideias somente |
| [Salah-XD/equipt, seasonal-inventory-plan](https://github.com/Salah-XD/equipt/blob/6380fd246d95eedb65077f466d37534a557d48dc/plugins/equipt-business/skills/seasonal-inventory-plan/SKILL.md); metadata Salah-XD | `6380fd246d95eedb65077f466d37534a557d48dc`, 10/06/2026, offset +05:30 | SKILL inteiro e LICENSE raiz | MIT, Equipt 2026. Sem execução ou validação de exemplos |

Não são oito provas independentes de desempenho: são oito origens consultadas, uma delas com duas skills relacionadas. Os diretórios repetem essas origens. O candidato kayforkind/inventory-demand-planning foi localizado com estrutura e métodos próximos ao ECC, mas a origem e filiação não foram confirmadas nesta frente; não entrou na comparação aprofundada nem contou como evidência adicional. Asgard ficou com a frente de controle; não foi duplicada aqui.

## Comparação de componentes

| Fonte/arquivo → componente | Decisão | Motivo e correção necessária |
|---|---|---|
| OneWave SKILL → entrega de proposta por SKU, lista da semana e urgência antes da chegada | Adaptar | Resultado fácil de revisar; adicionar posição de estoque, datas e premissas, pois saldo isolado pode duplicar compra |
| OneWave SKILL → produto sem histórico separado e sazonalidade só evidenciada | Aproveitar conceitualmente | Impede apresentar julgamento como cálculo; analogia ou estimativa explicitada continuam possíveis |
| Intempt SKILL → velocidade por dias disponíveis, zero venda versus indisponibilidade, chegada na ETA | Adaptar | Corrige erro operacional comum; média dos dias disponíveis é proxy, não recuperação garantida de demanda perdida, principalmente quando ruptura coincide com pico |
| Intempt refs → período parcial, chave/duplicidade, ausência versus zero, atualização dos dados | Adaptar | Verificar antes de calcular; executar só checks pertinentes ao pedido e mostrar os não verificáveis |
| Intempt SKILL → calendário de promoção, projeção por fases e limite de cobertura incompatível com prazo longo | Aproveitar a estrutura | Mostra conflito em vez de emitir dois rótulos incompatíveis. Não importar multiplicador promocional, folga ou teto padrão para o cliente |
| Risco SKILL/refs → tabela de política separada da necessidade atual; ROP separado de quantidade | Adaptar | Políticas respondem quando/quanto; proposta responde o que sugerir agora. Só produzir os dois arquivos se o pedido precisar deles |
| Risco safety-stock → variância de demanda versus prazo e serviço por ciclo | Adaptar | Unidades explícitas são úteis; suposições de independência, distribuição e período precisam acompanhar cálculo |
| Risco verify.sh → invariantes estruturais | Descartar como verificador pronto | Header desconhecido e ausência de CSV terminam com sucesso; números passam por coerção `awk`; gatilhos se baseiam em on_hand. Leitura não comprova política comercial |
| Risco ddmrp → zonas e posição líquida | Referência futura somente | Não selecionar DDMRP automaticamente pelo CV; demanda qualificada, horizonte de pico e dimensionamento exigem contexto e método profissional adicional |
| ECC SKILL → método por padrão, revisão periódica, MOQ/múltiplos e posição de estoque | Adaptar conceitualmente | Melhor encadeamento de decisões; retirar cenário obrigatório de grandes redes, sistemas presumidos e regras quantitativas universais |
| ECC SKILL → promoção separada do baseline, efeito posterior, feriado móvel e mudança de regime | Referência sob demanda | Necessário quando calendário altera a compra; elasticidades e percentuais só com dados ou cenário explicitamente escolhido |
| A5C SKILL → EOQ, custo relevante e alternativas com desconto | Referência conceitual; descartar implementação pronta | Comparar custo total é útil, mas cálculo de descontos não restringe claramente a quantidade ao teto da faixa; exige reconstrução das alternativas factíveis |
| A5C SKILL → safety stock variável e políticas anuais | Descartar código | `lead_time_std` é recebido e ignorado no resultado; funções rQ/RS fixam 12 períodos/ano. Não usar com dados diários/semanais sem correção e avaliação |
| HGarg scripts → separar perfil dos dados, cálculo determinístico e interpretação | Aproveitar ideia profissional | Arquitetura de cálculo auditável é útil; pacote sem licença não autoriza copiar. Pipeline rígido e provedor Groq não são necessários ao destino |
| tinh2 SKILL → avaliação por horizonte, backtest, baseline e erros por segmento | Aproveitar ideia profissional em referência | Checklist de auditoria tem cobertura útil; investigação de codebase inteira, proibição de perguntas e telemetria automática não pertencem ao fluxo do analista |
| Equipt SKILL → calendário reverso, data limite para nova compra e revisão pós-temporada | Adaptar | A chegada precisa anteceder a janela útil de venda; descartar buffers, crescimento, prazo e descontos presumidos |

## Falhas decisivas encontradas na leitura

**Risco:** o núcleo sugere adicionar uma parcela com raiz do intervalo de revisão ao buffer de lead time; a referência `reorder-policies.md` usa o período combinado dentro da raiz. Essas expressões não são equivalentes. Para demanda independente e estacionária, a referência é a aproximação coerente; não somar buffers como se fossem a mesma regra. A expressão rotulada como King para correlação não representa um parâmetro geral de covariância: não transportar essa identificação para cálculo genérico. A referência explica corretamente serviço como probabilidade de não faltar no ciclo, mas usa a expressão “cauda gorda” para normal; remover essa caracterização.

**ECC:** relaciona z-score a “target fill rate” no fluxo, embora os percentis normais apresentados não definam diretamente fill rate em unidades. WMAPE em unidades também não vira métrica monetária só por ponderar volumes. Os percentuais de melhoria por ML e as metas, promoções e buffers são alegações da skill, sem estudos vinculados; não os apresentar como evidência comprovada. A divisão ABC por margem é alternativa contextual à classificação por valor de consumo do Risco, e precisa ser nomeada, não misturada silenciosamente.

**HGarg:** `wmape()` exclui dias de venda observada zero do numerador e denominador. Previsão positiva em um dia de demanda realmente zero deve contribuir com erro absoluto; mascarar esses dias melhora artificialmente o score. Todas as vendas zero não demonstram “erro de 100%”; podem deixar a métrica indefinida. Features são construídas antes do corte temporal; lags do teste contêm vendas reais do próprio holdout. Isso pode ser coerente com avaliação de um passo com novas observações, mas não demonstra previsão fixa de todo o horizonte. Interpolação antes do corte pode usar informação futura, conforme a posição das lacunas. Os dois candidatos também podem comparar conjuntos de datas diferentes depois de dropna.

Ainda em HGarg, a seleção do campeão não alimenta uma previsão futura usada na política: média e desvio de vendas brutas alimentam SS/ROP, e as previsões dos modelos são descartadas. O HTML afirma que estatísticas do vencedor dirigem a política, contradizendo o script. Vencer com Fourier não comprova sazonalidade estrita; a seleção depende dos candidatos e do holdout. Dados sintéticos e relatórios publicados pelo autor são demonstrações da origem, não execução revalidada nesta pesquisa. O README requer Groq na orquestração; os três scripts consultados têm caminho determinístico sem chamada Groq. `run_pipeline_llm.py`, outputs e template não foram lidos, portanto não há revisão do caminho com provedor.

**Intempt:** regras de parar quando falta qualquer input conflitam com o protocolo que permite reter campos e degradar a análise; três perguntas máximas não justificam inventar informação material. A regra final de zero velocidade precisa preservar a verificação anterior de disponibilidade, para não chamar ruptura de estoque morto. Não transportar rodapé promocional, contexto de empresa criado automaticamente, encadeamento obrigatório de outras skills, modos declarados ou defaults numéricos.

## Síntese operacional proposta para criação posterior

### Núcleo mínimo

1. Reconhecer a decisão: entender cobertura, investigar falta, propor reposição ou revisar política. Aproveitar arquivos, números e histórico já recebidos; perguntar apenas o que muda materialmente a entrega solicitada.
2. Confirmar SKU-local-unidade-período-data de corte; distinguir venda, consumo, transferência e devolução. Estabelecer o significado das colunas antes de somá-las. Dias ausentes, zeros medidos e indisponibilidade são estados distintos.
3. Produzir uma recomendação proporcional à evidência. Mostrar prioridades, cálculo verificável, restrição e próximo passo. Se faltar custo, reter EOQ; se faltar prazo, reter data firme de reposição; se faltar disponibilidade histórica, indicar limitação da velocidade. Não bloquear o restante que continua válido.
4. Se houver base para quantidade: considerar posição e chegadas datadas, demanda ao longo do horizonte de proteção, política vigente, restrições do fornecedor, orçamento/validade quando relevantes e arredondamento visível. A proposta permanece para decisão; não cria pedido real.
5. Comparar recomendação anterior com realização quando a pessoa trouxer outro ciclo. Oferecer adaptação própria ao detectar rotina recorrente ou atrito; obter aceite para personalização. Recorrência não arma monitor automaticamente.

### Conceitos que precisam permanecer exatos

Cobertura atual do disponível por taxa histórica é medida descritiva. Cobertura futura integra previsão por data e chegadas que podem efetivamente ser usadas. Não somar toda entrada futura ao estoque de hoje: uma entrega posterior à ruptura não elimina o intervalo sem atendimento. Saldo físico, estoque bloqueado, disponível, reserva, trânsito, pedido firme e backorder precisam de mapeamento. A expressão de posição do ECC é ponto de partida, não autorização para subtrair reservas e comprometidos duas vezes nem somar trânsito novamente se já estiver em pedidos abertos.

Giro físico deve casar quantidade consumida com estoque médio na mesma unidade/período; giro financeiro casa custo vendido com estoque médio a custo. Cobertura por vendas futuras, dias de estoque contábil e giro são medidas diferentes. Demanda observada durante disponibilidade não demonstra demanda irrestrita no período; pedidos pendentes também podem já constar na série usada para previsão. Evitar duplicação.

Na revisão contínua, o horizonte de proteção normalmente corresponde ao lead time; na periódica, abrange lead time e intervalo entre revisões. Sob hipóteses declaradas, SS por demanda estável e prazo fixo pode usar dispersão agregada no horizonte; quando o prazo varia, a aproximação incorpora essa variação. Para sazonalidade, autocorrelação, promoção ou demanda intermitente, não inserir um desvio histórico bruto numa fórmula normal automaticamente. Erro de previsão de um passo não é automaticamente erro acumulado do horizonte. Serviço por ciclo, fill rate em unidades e completude por linha/pedido não são intercambiáveis.

EOQ é cenário econômico com demanda, custo de pedido e manutenção no mesmo período, não comando obrigatório nem gatilho. Sem custos observados ou hipótese explicitamente aceita, não produzi-lo. Valor de compra, validade, espaço, caixa, MOQ, múltiplos e descontos podem tornar o lote teórico inviável. Registrar efeito do arredondamento e saldo resultante, sem presumir que a solução mais barata da fórmula será a decisão comercial.

### Referências sob demanda

| Recurso futuro | Quando carregar | Conteúdo mínimo |
|---|---|---|
| `references/dados-e-demanda.md` | Export inconsistente, faltas históricas ou comparação temporal | Chaves, unidades, período parcial, ausência/zero, censura, critérios de estimativa |
| `references/reposicao.md` | Pedido sobre quando/quanto repor | Posição sem sobreposição, calendário/ETA, horizonte de proteção, MOQ/múltiplos e proposta revisável |
| `references/previsao.md` | Pedido realmente exige demanda futura | Baseline, padrão, sazonal/intermitente/novo, comparação temporal por horizonte, métricas e limites |
| `references/estoque-de-seguranca-e-custos.md` | Meta de serviço ou comparação econômica informada | Definições de serviço, hipóteses, SS, EOQ e alternativas factíveis |
| `references/sazonalidade-e-promocoes.md` | Campanha, coleção ou janela de venda | Datas, incremento evidenciado, canibalização/efeito posterior, chegada e corte de compra |

Não acrescentar scripts por antecipação. Um script local só se justifica quando volume, repetição ou risco de cálculo mostrar ganho concreto. Não afirmar bibliotecas já instaladas no Studio. Se a criação futura precisar de dependência faltante e houver autorização, oferecer preparação simples para pessoa não desenvolvedora. Bibliografia, versões pesquisadas e histórico ficam neste dossiê, fora do núcleo executável.

## Avaliação futura, não executada

| Situação a avaliar | Evidência exigida na entrega futura |
|---|---|
| Pedidos abertos suficientes, físico baixo | Proposta não duplica compra; chegada posterior à necessidade mostra intervalo de ruptura |
| Reserva, comprometido e backorder sobrepostos | Mapeamento evita dupla subtração e explica saldo usado |
| Vinte dias indisponíveis numa janela de trinta | Venda observada não vira demanda baixa; disponibilidade parcial continua proxy, não “demanda recuperada” |
| Dia faltante versus zero real | Não preencher zero ou interpolar silenciosamente; critério e efeito explícitos |
| Promoção futura e recebimento dentro da campanha | Velocidade muda nas datas corretas; não aplicar multiplicador desde hoje |
| Sem histórico ou demanda intermitente | Estimativa/similar claramente separada de previsão validada; normalidade não presumida |
| Prazo semanal e vendas diárias | Conversão de unidades/períodos demonstrada; nenhum 12-períodos oculto |
| Meta fill rate informada | Não converter diretamente em z de serviço por ciclo |
| Custo de pedido/manutenção ausente ou zero | EOQ retido quando indefinido; análise útil restante preservada |
| MOQ acima do lote e desconto por faixa | Alternativas factíveis, caixa/cobertura e arredondamento comparados |
| Forecast positivo em dia de demanda real zero | Erro absoluto contabilizado; denominador total zero tratado como indefinido |
| Avaliação de trinta dias | Origem fixa versus atualização diária explicitadas; features disponíveis no instante correto; baseline nas mesmas datas |
| Script não encontrou dados | Estado sem dados não apresentado como validação comercial aprovada |

## Limites e estado de entrega

Leitura concluída para os arquivos declarados e comparação documental produzida. Não há auditoria integral de segurança, licença de todas as dependências ou compatibilidade de empacotamento de nenhuma origem. Não houve benchmarks locais, renderização de entregas remotas, treinamento, contratação, proposta nativa Hermes, aprovação, instalação ou teste autenticado real. A galeria aceita fontes específicas; os repositórios desta pesquisa servem para aprendizado e eventual adaptação própria, não inclusão direta fora do contrato.

A frente de métodos/casos deverá fundamentar censura, serviço e hipóteses estatísticas com fontes profissionais, e a coordenação deverá reconciliar o desenho com saldo/controle/excessos. Dúvidas restantes são de dados e validação futura, não motivo para acumular mais pacotes redundantes. Este arquivo não foi commitado nem publicado por esta frente.
