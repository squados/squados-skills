# Analista de Estoque — síntese comparativa

Pesquisa em 12/10/2026, rodada 20 das 33 especialidades aprovadas. Apoio interno a saldos, giro, cobertura, rupturas, excessos e reposição. Nenhum ERP acessado, ajuste lançado, compra emitida, pacote criado/instalado ou script externo executado.

## Resultado para a criação posterior

Combinar entrega curta OneWave, integridade e disponibilidade histórica Intempt, posição/padrões de demanda ECC, distinção entre política e necessidade atual Risco, alternativas de contagem Kishor e conciliação Anthropic. SME oferece bons cuidados com lacunas, mas limita o trabalho a templates e não teve licença confirmada. Asgard ajuda a julgar sazonalidade; seus defaults e exemplos não devem ser portados.

O núcleo deve reconhecer a decisão e trabalhar sobre os dados existentes: **saldo e disponibilidade → demanda/período → restrições e chegadas → cálculo pertinente → evidência e próxima ação**. Conferir uma diferença não exige previsão estatística; calcular cobertura não exige EOQ. A profundidade acompanha o pedido e a qualidade dos dados.

## Dossiês e alcance

| Frente | Arquivo | Consulta efetiva |
|---|---|---|
| Demanda e reposição | [Skills de reposição](2026-10-12-inventory-skills-replenishment.md) | Nove SKILL completos de oito origens, com referências/scripts determinantes |
| Saldo, contagem e excessos | [Skills de controle](2026-10-12-inventory-skills-control.md) | Quatro SKILL completos de quatro origens, recursos e código embutido por leitura |
| Métodos e casos | [Métodos profissionais](2026-10-12-inventory-methods.md) | Onze registros primários com acesso discriminado, materiais recentes identificados e três casos autorais |

Consolidado: **treze SKILL completos de doze origens**, sem duplicar os espelhos de SME e sem contar descrições de diretórios como pacotes lidos. Duas skills tinh2 são relacionadas, não duas provas independentes. Intempt foi consultada em snapshot histórico identificado porque o caminho atual retornou 404. Reuso de fontes de pesquisas anteriores não aumenta a contagem.

Coordenação leu os três dossiês e conferiu uma fonte recente primária, incorporada à frente de métodos: [FreshRetailNet-50K v5](https://arxiv.org/html/2505.16319v5), Wang e outros, revisão de 18/06/2026. Consulta seletiva de resumo, introdução, §3.1, §4.1 e §6, sem código/dataset/experimentos executados. O estudo distingue vendas observadas de demanda estimada durante rupturas; seu recorte de perecíveis chineses e janela curta limita generalização/sazonalidade. Aproveitar essa distinção, sem impor modelos de ML ou prometer os ganhos publicados à skill. São onze registros metodológicos contando esse acréscimo, com profundidades diferentes.

## Fonte → componente → escolha → motivo

| Origem/componente | Escolha | Adaptação ao trabalho |
|---|---|---|
| OneWave: proposta curta por SKU, prioridade e item novo separado | Adaptar | Mostrar base, cálculo, chegada e restrição; falta de histórico fica explícita. Sem lista semanal ou rotina fixa por padrão |
| Intempt: dias disponíveis, datas de promoção/ETA, integridade e conflito de prazo | Aproveitar estrutura | Venda zero, indisponibilidade e registro faltante são diferentes. Média dos dias disponíveis é proxy; não recuperação comprovada de toda demanda |
| Intempt: modos, defaults e bloqueio de toda entrega por input faltante | Descartar | Perguntar só lacuna material e entregar a parte válida. Sem multiplicador 2x, folga/sete dias, contexto de empresa automático ou rodapé promocional |
| Risco: política versus compra atual, proteção contínua/periódica e serviço por ciclo | Adaptar com correções | Separar quando e quanto; explicitar hipóteses e posição. Núcleo diverge da referência no buffer periódico; verifier estrutural não prova política correta |
| ECC: posição, método conforme padrão, MOQ e calendário | Adaptar conceito | Reservas/backorders/comprometido podem sobrepor; mapear antes de subtrair. Percentil de ciclo não equivale diretamente a fill rate; melhorias ML publicadas na skill não são evidência nossa |
| A5C: EOQ/custos e políticas | Referência conceitual; descartar implementação pronta | Código ignora efeito de lead_time_std apesar da descrição e assume doze períodos/ano. Faixas de desconto precisam de alternativas factíveis |
| HGarg: dados, cálculo e interpretação separados | Aproveitar ideia profissional | Sem licença encontrada. WMAPE omite erro em dias zero; avaliação com lags reais não demonstra previsão de todo horizonte; política usa média bruta, não campeão anunciado no HTML |
| tinh2: baseline, horizonte e segmentação de erros | Aproveitar ideia profissional | Sem licença localizada. Retirar investigação de codebase, proibição de perguntas e telemetria automática |
| Equipt: calendário reverso e janela útil | Adaptar | Prazo e data de venda governam chegada. Crescimento, buffers e descontos vêm de dados/cenário informado |
| SME: lacuna não é zero, corte/unidade e causa investigada | Adaptar conceitualmente | Redação própria, sem licença confirmada. Descartar só-template/proibição de analisar dados reais e múltiplos formatos obrigatórios |
| Kishor: alternativas de contagem e investigação | Adaptar método | Capacidade, tolerância e frequência reais. Descartar código com percentual zero para registro zero divergente, agenda concentrada e retorno econômico sem fundamento |
| Anthropic: conciliação de razão e auxiliar na mesma data | Adaptar | Útil para valores e pendências; não substitui contagem física. Materialidade e aging ilustrativos não viram defaults |
| Asgard: sazonalidade/estoque estratégico antes de baixa | Adaptar ressalva | Baixa movimentação não prova obsolescência. Rejeitar cortes universais e exemplos operacionais sem revisão |
| Microsoft/MIT/OTexts/Sebrae | Adaptar princípios profissionais | Significado das colunas, unidades e corte, hipóteses de reposição/custo, demanda intermitente e ABC contextual. Não instalar ERP nem transportar procedimentos do produto como requisito |

## Divergências que mudam a decisão

**Físico, disponível e posição:** entradas futuras não estão disponíveis hoje. Pedido firme com ETA posterior à falta não elimina o intervalo. Reserva e backorder podem expressar o mesmo compromisso; evitar dupla subtração. Transferência não é consumo consolidado e lançamento não é necessariamente ocorrência no corte.

**Venda e demanda:** média observada inclui o efeito da oferta limitada. Mostrar disponibilidade histórica quando houver, separar observado/estimado/cenário e não inventar vendas perdidas exatas. Zeros genuínos, faltantes e ruptura pedem tratamentos diferentes. Demanda intermitente não recebe normalidade automática.

**Cobertura e giro:** mesma unidade/base de custo, local e período. CMV divide estoque médio a custo; faturamento não substitui CMV nessa fórmula. Demanda zero torna dias de cobertura pouco interpretáveis; denominador zero não vira zero silencioso. Média de início/fim é aproximação quando faltam observações intermediárias.

**Quantidade e atendimento:** quantidade suficiente no total pode chegar tarde. Reposição considera horizonte de proteção, saldo/entradas/compromissos, MOQ, múltiplos, validade e caixa pertinentes. Estoque de segurança exige objetivo de serviço e hipóteses; CSL e fill rate são distintos. EOQ só com custos/período/hipóteses definidos, sem fabricar custo de manutenção ou meta de 95%.

**Excesso e classificação:** ABC declara critério, janela e fronteira. Participação financeira não elimina criticidade técnica. Baixo giro pode refletir sazonalidade, ruptura, lançamento ou peça de contingência. Excesso ao alvo e valor ao custo não são perda contábil comprovada; idade desde venda não é idade do lote.

## Organização mínima proposta

Núcleo curto: reconhecer intenção, aproveitar dados, esclarecer base material, selecionar análise, mostrar resultado verificável e limites. Referências candidatas sob demanda: dados/saldo/conciliação; indicadores e excessos; reposição e chegadas; previsão/serviço/custos. A criação posterior decidirá o menor conjunto útil, sem acumular todos os recursos sugeridos nas frentes.

Tabela/chat pode bastar. Planilha e script entram por volume, repetição ou risco de cálculo concreto. Conferir disponibilidade de dependências; faltando uma necessária, explicar o benefício e oferecer instalação simples executada pelo agente quando autorizada. Ao observar preferência recorrente ou atrito, oferecer adaptar a própria versão e aplicar com aceite/pedido. Uma política de empresa não vira regra do pacote público.

## Casos autorais e conferências

Os casos completos estão na frente de métodos. Coordenação recalculou com expressões locais Decimal/data, sem executar código remoto nem a futura skill:

- **Disponibilidade:** físico144, bloqueado12, reservado36 → livre96, insuficiente para promessa100 hoje. Entrada firme48 emD4 leva a88 ao fimD7 sob consumo adicional8/dia; pedido24 sem data fica fora da projeção confirmada.
- **Censura e prazo:** 40 vendidos/10dias=4, mas 40/5dias disponíveis=8 como proxy/cenário. Alvo56 menos20 → compra36 no cenário; chegada após quatro dias deixa falta12 antes dela. Conta agregada não demonstra trajetória viável nem serviço garantido.
- **MOQ e validade:** alvo40, livre18, necessidade22; mínimo120 gera saldo138, excesso98 ao alvo. Sob validade e demanda fictícias explicitadas, sobram78 no vencimento. ABC depende da política; peça críticaW permanece relevante. EOQ de subquestão independente134,164/custo402,49; mínimo240/custo472,50, diferença70,01.

Coordenação também conferiu [Asgard seasonal](https://github.com/asgard-ai-platform/skills/blob/4e7f4f8e389847757a5a4236c2f1ed9813359179/ecom-inventory-health/references/seasonal-forecasting.md): totais anuais6470/6595 corretos; índices somam11,96, não12; média calculada544,375, não546. Ordem01/04 com45dias chega16/05, depois da necessidade01/05. Corrigiu a acusação provisória de totais errados antes da consolidação.

Conferência seletiva do [A5C original](https://github.com/a5c-ai/babysitter/blob/feb68abe397acc14f32b34984975c48fedba2b33/library/specializations/domains/science/industrial-engineering/skills/inventory-optimizer/SKILL.md) confirmou ramo que ignora variabilidade do prazo e doze períodos fixos. [Microsoft on-hand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list) foi aberto como fonte de saldos. Gabarito aritmético e leitura estática não são validação operacional.

## Lacunas e estado

Vídeos recentes Sebrae foram identificados por páginas/descrição; conteúdo de estoque pede login e não foi analisado como audiovisual/transcrição. ASCM e Odoo têm acesso parcial registrado; PDFs MIT e manuscrito Columbia foram lidos seletivamente. Sem ferramentas pagas ou vidIQ.

Licenças: MIT/Apache nos inventários não dispensam avisos; ECC Apache frontmatter/MIT raiz ambíguo; SME/HGarg/tinh2 sem licença encontrada nas consultas. Fonte pública não autoriza cópia. Pacotes e dependências completos não foram auditados, nem aprovados para galeria. Pesquisa suficiente para orientar desenho; criação, avaliações comportamentais, guard/proposta Hermes, instalação, uso real e publicação continuam pendentes.

Próxima especialidade: **Pesquisador de Concorrentes**, com foco em Ecommerce.
