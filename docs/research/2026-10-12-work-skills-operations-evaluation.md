# Avaliação independente — operações e pessoas

Início do lote em 12/10/2026; execução desta unidade concluída em 13/10/2026. Avaliador não participou da autoria dos pacotes. Onze casos sintéticos executados com leitura explícita dos respectivos SKILL.md e apenas das referências registradas por caso. Nenhuma consulta ao desenho, pesquisa, implementação ou gabaritos externos dos autores antes das respostas. Os casos compartilham este contexto e não são onze sessões independentes. O exemplo coincidente do recurso de treinamento limita especialmente esse caso. Não foi realizado controle sem skill nem ensaio de ativação implícita. Não foram utilizados dados de clientes, contas, contatos, serviços pagos, downloads, publicação ou instalação de dependências. Pacotes permaneceram somente leitura. Esta avaliação registra entregas, não operação real no Studio.

## data-specialist

**Pedido exato**

Dados fictícios de abril: equipe A teve 10 pedidos, receita R$1.000; B teve 5 pedidos, receita R$750. Um pedido adicional de A não tem receita informada. Faça análise breve com ticket e limitações. Não substitua dado faltante por zero nem invente causa da diferença. Entregue tabela e recomendação de conferência.

**Recursos lidos:** `SKILL.md`, `references/comparacoes.md`, `references/comunicacao.md`.

**Resultado integral**

Abril, dados fictícios fornecidos; receita em BRL e unidade de análise pedido. Não há ano, corte de extração nem definição detalhada de receita.

| Equipe | Pedidos com receita conhecida | Receita conhecida | Ticket no subconjunto conhecido | Pedidos adicionais sem receita | Pedidos informados ao todo |
|---|---:|---:|---:|---:|---:|
| A | 10 | R$ 1.000 | R$ 100 | 1 | 11 |
| B | 5 | R$ 750 | R$ 150 | 0 | 5 |
| Total | 15 | R$ 1.750 | R$ 116,67 | 1 | 16 |

Ticket conhecido = receita conhecida ÷ pedidos com receita conhecida. No subconjunto conhecido, B tem ticket R$ 50 maior que A (50% sobre R$ 100); isso não demonstra uma causa nem desempenho superior. A receita total e o ticket de todos os 11 pedidos de A permanecem desconhecidos: se a receita ausente for x, serão R$ 1.000 + x e (R$ 1.000 + x) ÷ 11. Dividir R$ 1.000 por 11 trataria implicitamente a ausência como zero.

Conferência recomendada: identificar o pedido adicional, confirmar sua receita na fonte e verificar que não duplica os dez anteriores; alinhar definição de receita, cancelamentos e corte entre equipes. Depois recalcular totais e tickets completos. Contas conferidas aritmeticamente; não houve acesso à base original.


## presentation-specialist

**Pedido exato**

Crie uma apresentação HTML local de quatro telas para diretoria: (1) decisão sobre piloto de estoque, (2) exemplo 100 físico−20 reservado=80 disponível se sem outros bloqueios, (3) piloto em duas lojas por 30 dias, (4) comparar divergências antes/depois com janela e volume; orçamento R$2.000, sem previsão de economia. Marca azul escuro/creme, leitura autônoma, controles e teclado. Grave HTML real em docs/research/evaluation-artifacts/2026-10-12-presentation-sample.html; sem CDN, resultados inventados, publicação ou promessa PPTX.

**Recursos lidos:** `SKILL.md`, `references/narrativa.md`, `references/html.md`.

**Resultado integral**

Arquivo HTML produzido: [Apresentação local](evaluation-artifacts/2026-10-12-presentation-sample.html). Abra o arquivo em um navegador. Conteúdo completo embutido, fonte do sistema, quatro telas e navegação por Anterior/Próxima, setas, Home e End. O HTML real, incluindo CSS/JavaScript e todo o texto, é parte integral desta resposta, no caminho solicitado.

Texto integral das quatro telas:

1. **Decidir um piloto de estoque com limite de R$ 2.000.** Recomendação: autorizar um piloto em duas lojas durante 30 dias para observar divergências de estoque antes de ampliar o uso. Decisão solicitada: confirmar escopo e orçamento máximo; definir responsáveis, lojas e início antes de executar. O que ainda precisamos aprender: se separar físico, reservado e disponível ajuda a equipe a decidir quanto pode vender; benefício ainda não demonstrado. Os R$ 2.000 são o orçamento informado, sem detalhamento de custos. Apresentação é proposta, sem registro de aprovação nem previsão de economia.
2. **100 físicos − 20 reservados = 80 disponíveis.** Físico: unidades existentes; reservado: unidades comprometidas; disponível: unidades para vender. Condição: se não houver outros bloqueios. Havendo bloqueios, incorporá-los sem dupla contagem. Exemplo didático fornecido, em unidades; não é medição das lojas nem resultado do piloto.
3. **Duas lojas, 30 dias e uma regra comum de conferência.** Antes: escolher lojas/responsáveis, definir SKUs e regra de divergência, registrar linha de base e detalhar custos dentro de R$ 2.000. Durante: registrar físico, reservado, bloqueios e disponível na mesma referência de tempo; conferir população definida e registrar volume; documentar mudanças, exceções e dificuldades. Datas/pessoas precisam ser definidas; janela de linha de base deve ser acordada antes do piloto e sua duração não foi fornecida.
4. **Comparar divergências com janela e volume visíveis.** Plano de medição sem valores coletados: datas da linha de base e dos 30 dias; conferências válidas por loja/SKU na mesma regra; quantidade de divergências e taxa divergentes ÷ conferências válidas. Ao final, decidir entre ajustar, ampliar ou encerrar, conferindo cobertura e mudanças em mix, volume e operação. Antes/depois descreve o recorte e sozinho não demonstra causalidade. Sem resultados ou economia prevista. Fonte: briefing sintético da avaliação.

Verificação efetiva do artefato está registrada ao final deste documento. Não houve publicação, exportação PPTX, uso de imagens, CDN ou instalação. Impressão não foi solicitada nem verificada visualmente.


## spreadsheet-specialist

**Pedido exato**

Prepare especificação utilizável de planilha de pedidos com colunas SKU, quantidade, preço e receita; SKUs 0012 e 0013 são texto. Linhas: 0012,2,R$30; 0013,3,R$20. Entregue tabela com fórmulas e total, diga qual fórmula usa para linhas futuras e o que seria preciso conferir num arquivo XLSX. Este pedido é a especificação, não gerar arquivo; não afirme recálculo/render executados.

**Recursos lidos:** `SKILL.md`, `references/calculos.md`.

**Resultado integral**

Especificação para aba `Pedidos`, linha 1 com cabeçalhos. A coluna A deve ser configurada como **Texto antes de digitar/importar**. B e C são entradas numéricas; D contém fórmulas. O símbolo R$ é formato de célula, não parte do valor numérico.

| Linha Excel | A · SKU (texto) | B · Quantidade | C · Preço unitário (BRL) | D · Receita (fórmula) | Resultado esperado |
|---|---|---:|---:|---|---:|
| 2 | 0012 | 2 | 30,00 | `=B2*C2` | R$ 60,00 |
| 3 | 0013 | 3 | 20,00 | `=B3*C3` | R$ 60,00 |
| 4 · Total atual | — | — | — | `=SOMA(D2:D3)` | R$ 120,00 |

Para uso contínuo, transformar o intervalo de dados numa tabela do Excel chamada `Pedidos`, sem incluir a linha de total como pedido. Coluna calculada Receita: `=[@Quantidade]*[@Preço]`. Total na linha de totais da tabela: `=SOMA(Pedidos[Receita])`, somando todos os pedidos independentemente de filtros. Novas linhas da tabela deverão herdar a fórmula; conferir isso na plataforma de destino. Se não usar tabela, copiar a fórmula relativa `=B4*C4`, `=B5*C5` etc. e ampliar o intervalo do total ao acrescentar linhas.

Uma linha ainda incompleta deve ficar identificada como pendente e fora do total de receitas confirmadas; não usar multiplicação com branco como evidência de receita zero. Antes de usar um XLSX, conferir tipos dos SKUs e zeros à esquerda, valores numéricos, referências, expansão da tabela, fórmulas preservadas, erro/branco, formatação e legibilidade. Recalcular num motor compatível, reabrir resultados e alterar uma entrada para conferir propagação: quantidade 0012 de 2 para 3 deverá mudar receita para R$ 90 e total para R$ 150, retornando depois ao original. Aqui foram conferidas apenas especificação e contas; não foi criado, recalculado ou renderizado um XLSX.


## executive-assistant

**Pedido exato**

Ata interna: “Joana disse que pode revisar o catálogo na sexta se receber fotos até quarta. Marcos pediu orçamento, sem definir dono. A reunião decidiu piloto de duas lojas por 30 dias; verba máxima R$2.000. Data de início não definida.” Prepare resumo e acompanhamento, separando decisões, propostas, compromissos condicionais e pendências; não envie convites.

**Recursos lidos:** `SKILL.md`, `references/reunioes.md`, `references/prioridades.md`.

**Resultado integral**

Resumo interno: a reunião decidiu um piloto de duas lojas por 30 dias, com verba máxima de R$ 2.000. O início não foi definido. Joana sinalizou disponibilidade para revisar o catálogo na sexta, condicionada ao recebimento das fotos até quarta. Marcos solicitou orçamento, mas isso não atribuiu a ele sua preparação.

| Natureza | Registro fiel | Acompanhamento interno |
|---|---|---|
| Decisão | Piloto em duas lojas por 30 dias; verba máxima R$ 2.000 | Definir início, lojas e responsáveis; ainda sem donos/prazos atribuídos |
| Disponibilidade / compromisso condicional | Joana pode revisar na sexta **se** receber fotos até quarta | Confirmar disponibilidade e recebimento; responsável pelo envio das fotos desconhecido |
| Solicitação | Marcos pediu orçamento | Designar dono e prazo do orçamento; não constam da ata |
| Propostas | Não há outra proposta explicitamente identificada | Encaminhamentos desta tabela são sugestões de acompanhamento, sem aceite registrado |
| Pendência | Data de início não definida | Obter decisão com responsável competente |

Ordem sugerida: resolver envio das fotos antes do prazo relativo de quarta, confirmar a revisão de Joana, atribuir orçamento e definir início do piloto com as condições necessárias. A data da reunião não foi fornecida; “quarta” e “sexta” permanecem relativas, sem conversão para datas. Nenhum convite foi enviado nem tarefa atribuída automaticamente.


## project-manager

**Pedido exato**

Planeje piloto curto: coleta de dados 2 dias por Ana, depois configuração 3 dias por Bruno, depois validação 2 dias por Ana. Ana só pode 1 dia por semana; Bruno está disponível. Sem data de início confirmada. Mostre dependências e a restrição de capacidade; não some durações como prazo calendário garantido ou invente datas aprovadas.

**Recursos lidos:** `SKILL.md`, `references/cronograma.md`.

**Resultado integral**

| Etapa | Responsável informado | Esforço | Dependência | Evidência de término proposta |
|---|---|---:|---|---|
| Coleta | Ana | 2 dias de trabalho | Início a confirmar | Dados necessários reunidos e conferidos |
| Configuração | Bruno | 3 dias de trabalho | Coleta concluída | Configuração disponível para validação |
| Validação | Ana | 2 dias de trabalho | Configuração concluída | Casos do piloto executados e divergências registradas |

Sequência: **coleta → configuração → validação**. Esforço total: 7 dias de trabalho, dos quais 4 de Ana e 3 de Bruno. Isso não é um prazo calendário de 7 dias.

Ana dispõe de um dia por semana. Cada bloco dela precisa de duas oportunidades semanais de trabalho. Bruno, disponível, precisa encaixar seus três dias depois da coleta; a validação só começa depois deles. Como as quatro oportunidades de Ana são sequenciais e usam sua mesma capacidade, ocupam ao menos quatro semanas de alocação no modelo semanal informado, podendo haver semanas adicionais dependendo do dia disponível, calendário e término da configuração. Isso não significa quatro semanas exatas decorridas: dias em bordas de semana podem ficar próximos, e as convenções de disponibilidade não foram detalhadas.

Cronograma utilizável sem datas: reservar A1/A2 para coleta; após A2, reservar B1/B2/B3 para configuração; depois reservar as próximas duas disponibilidades semanais de Ana, A3/A4, para validação. A3 não pode ser antecipada para antes de B3.

Para transformar em datas: confirmar início, dia semanal de Ana, dias úteis/feriados, disponibilidade integral de Bruno e critérios de validação. Se for necessário terminar antes, negociar capacidade adicional ou delegar parte do trabalho com capacidade confirmada, sem presumir produtividade maior. Plano condicionado, sem datas ou prazo aprovados inventados.


## product-specialist

**Pedido exato**

Três lojistas relatam confusão entre reservado e disponível, um quarto prefere a tela atual. Vendas pede alertas automáticos mas não trouxe evidência. Temos uma semana de dev e queremos reduzir erros na decisão de vender. Recomende investigação e experimento/especificação mínima com critérios, sem apresentar solução como validada nem adicionar plataforma nova.

**Recursos lidos:** `SKILL.md`, `references/descoberta.md`, `references/direcao.md`.

**Resultado integral**

Recomendo priorizar a compreensão da diferença entre reservado e disponível. Há três relatos de confusão, um de preferência pela tela atual e nenhum suporte apresentado para alertas automáticos. Esses quatro relatos não medem prevalência no mercado nem demonstram erros causados pela tela.

Investigação curta: pedir a cada um dos quatro lojistas que mostre uma decisão recente sobre vender, quais números consultou, o que entendeu e como conferiu. Preservar a razão de quem prefere a tela atual. Verificar se a dificuldade vem de rótulos, ausência de bloqueios ou dados divergentes antes de alterar a regra.

Hipótese proposta: rótulos claros e relação visível entre físico, reservado e disponível podem reduzir decisões incorretas em cenários da tarefa. Experimento mínimo dentro de uma semana de dev, condicionado ao esforço confirmado: protótipo da mesma tela com os três campos explicados e regra de cálculo visível, sem alertas nem infraestrutura nova. Primeiro testar compreensão; uma alteração produtiva só se justifica depois da evidência pertinente.

Especificação mínima: manter dados e ações existentes; distinguir físico, reservado e disponível; mostrar condição dos bloqueios; não computar quantidade ausente como zero. Exemplo de teste sem bloqueios: 100 físico, 20 reservado, 80 disponível; decidir se pode vender 85 deve resultar “não, excede o disponível”. Usar outro caso equivalente para evitar acerto só por memorização e um caso com dado ausente para verificar que a pessoa pede conferência. Política concreta de outros bloqueios precisa vir do produto antes de especificar sua conta.

Critério local proposto **antes** das sessões: cada participante explicar a diferença e decidir corretamente nos casos completos, reconhecendo a impossibilidade de concluir no incompleto, sem instrução durante a tentativa. Registrar acertos/total de decisões por pessoa e tela, erro concreto, ajuda recebida e dúvida; alternar ordem e casos equivalentes para reduzir efeito de aprendizagem. Conservar como evidência contrária qualquer confusão nova do lojista que prefere a tela atual. Critério é operacional proposto para este teste, sem validade estatística presumida.

Se houver erro recorrente ou regressão de compreensão, revisar a hipótese antes de implementar; se houver indícios positivos, avançar com mudança pequena e observar erros em decisões reais com população/janela/volume explícitos. Tempo de dev é restrição, não compromisso de entrega confirmado. Resultado do protótipo não prova ganho causal, adoção ou benefício em produção.


## logistics

**Pedido exato**

Dos 20 pedidos da mesma coorte,15 entregues até prazo,2 entregues atrasados,3 ainda em trânsito com prazo já vencido. Frete totalR$400 para 20 pedidos; não sabemos peso/destino por pedido. Analise prazo e custo com denominadores claros; não retire em trânsito atrasado para melhorar taxa e não diagnostique transportadora sem dados.

**Recursos lidos:** `SKILL.md`, `references/operacao.md`.

**Resultado integral**

Coorte de 20 pedidos no corte fornecido; todos já atingiram seu prazo. Datas da coorte e corte não foram informadas.

| Estado no corte | Pedidos | Parcela dos 20 |
|---|---:|---:|
| Entregues dentro do prazo | 15 | 75% |
| Entregues atrasados | 2 | 10% |
| Em trânsito com prazo vencido | 3 | 15% |
| Total | 20 | 100% |

Pontualidade da coorte: 15 ÷ 20 = **75%**. Cinco pedidos (25%) não chegaram até o prazo: dois chegaram tarde e três continuam pendentes e vencidos. Entregas confirmadas: 17 ÷ 20 = 85%; isso é conclusão de entrega, não pontualidade. Entre os já entregues, 15 ÷ 17 = 88,24% pontuais, mas esse indicador parcial não substitui os 75% da coorte. Não há dados de completude para calcular OTIF.

Frete médio informado por pedido da coorte: R$ 400 ÷ 20 = **R$ 20**. Sem peso, destino, quantidade de remessas, serviços ou adicionais por pedido, não é possível identificar causa do custo nem comparar transportadoras de modo equivalente.

Prioridade interna: conferir status e previsão dos três pedidos vencidos, preservando promessa original e evidência de entrega; reunir datas de despacho/entrega, serviço, destino e custo por pedido dos cinco fora do prazo. Investigar explicações com esses dados, sem atribuir falha à transportadora agora. Análise feita sobre dados sintéticos; nenhuma contratação ou contato ocorreu.


## contract-assistant

**Pedido exato**

Compare somente redação: versãoA “Pagamento em 10 dias após entrega”; versãoB “Pagamento em 10 dias úteis após aceite por escrito. O cliente pode pedir uma revisão.” Jurisdição não informada. Identifique mudanças e dúvidas para revisão da equipe, cite os trechos e não declare validade ou lei aplicável, nem complete cláusula de aceite como aprovada.

**Recursos lidos:** `SKILL.md`, `references/revisao.md`, `references/obrigacoes.md`.

**Resultado integral**

Cobertura: somente os dois trechos fornecidos; não foram recebidos contratos completos, datas, estado de assinatura ou jurisdição.

| Aspecto | Versão A | Versão B | Mudança de redação / dúvida para revisão |
|---|---|---|---|
| Gatilho | “após entrega” | “após aceite por escrito” | B condiciona o início do prazo ao aceite documentado, evento diferente da entrega. Quem aceita, por qual meio e em quanto tempo? |
| Unidade do prazo | “em10 dias” | “em10 dias úteis” | B explicita dias úteis. A não esclarece unidade. Qual calendário e regra de contagem as partes pretendem? |
| Revisão | Não aparece no trecho A | “O cliente pode pedir uma revisão.” | B acrescenta possibilidade de uma revisão. Qual escopo, prazo de solicitação e efeito sobre aceite/pagamento? |

A mudança pode deslocar a referência comercial de vencimento se entrega e aceite não coincidirem; não é possível calcular vencimento sem eventos e contagem definidos. A ausência de revisão no trecho A não demonstra que o contrato completo a proíba. “Uma revisão” não esclarece prazo, limites ou cobrança.

Encaminhamento à equipe: esclarecer gatilho/contagem, responsável e evidência do aceite, calendário e relação entre revisão, aceite e pagamento. Não incluí texto de aceite presumidamente aprovado. Comparação textual, sem conclusão sobre validade, exigibilidade, lei aplicável ou favorecimento de uma parte cuja posição não foi informada.


## quality-specialist

**Pedido exato**

Registramos 8 pedidos com etiqueta incorreta em 100 conferidos. 5 ocorreram no turno da manhã, mas não temos volumes por turno. Uma pessoa suspeita do modelo de impressão; ainda não testamos. Faça contenção proporcional, plano de investigação e critério de verificar correção; não declare causa pelo turno ou por votação.

**Recursos lidos:** `SKILL.md`, `references/acoes.md`, `references/medicao.md`.

**Resultado integral**

Evidência: 8 pedidos com etiqueta incorreta entre 100 conferidos, ou **8% no recorte**. Cinco dos oito ocorreram de manhã; sem total conferido em cada turno, isso não estabelece taxa maior de manhã. O modelo de impressão é uma hipótese relatada por uma pessoa, sem teste.

Contenção proposta: conferir etiqueta contra pedido antes de liberar os próximos pedidos do fluxo afetado enquanto se delimita a falha; identificar e corrigir as oito divergências conhecidas, preservando registro do que foi alterado. Avaliar o estado dos oito para orientar tratamento interno proporcional, sem presumir que foram despachados nem interromper toda a operação. Responsável operacional precisa ser designado; não foi informado.

Investigação: registrar por pedido o conteúdo esperado/impresso, data/turno, quantidade conferida por turno, versão do modelo, impressora/configuração e etapas de geração/conferência. Reproduzir o erro com dados sintéticos conhecidos; comparar modelo suspeito e referência correta mantendo entrada/impressora constantes, e depois variar uma condição por vez. Buscar também casos corretos no mesmo modelo. Outra hipótese é associação incorreta do pedido à etiqueta; examinar o vínculo antes de atribuir culpa à pessoa. Registrar evidência que apoia e contradiz cada hipótese.

Ação corretiva depende do mecanismo sustentado; alteração do modelo ou do fluxo permanece proposta enquanto não testada. Não prescrever treinamento sem evidência de lacuna.

Verificação proposta: após a mudança, repetir os casos que reproduzem a falha e casos corretos de referência, exigindo associação e campos corretos em todos eles. Na operação, propor acompanhamento das próximas 100 conferências consecutivas do mesmo fluxo, com critério de zero etiquetas incorretas e cobertura dos turnos/modelos afetados; negociar a janela antes de chamar a ação eficaz. Uma falha reabre investigação e não pode ser removida do denominador. Zero em 100 sustentaria apenas conformidade nesse recorte; não demonstra ausência permanente de falhas ou ganho causal. Se não houver exposição relevante, eficácia permanece pendente.


## people-development

**Pedido exato**

Prepare conversa de feedback: em duas reuniões, Pedro apresentou números sem período e precisamos voltar à fonte; há exemplos anotados. Ele diz que o relatório recebido não tinha o período e nunca recebeu padrão. Queremos melhorar a análise, sem avaliação disciplinar. Dê roteiro e plano curto com apoio e evidência de progresso; não infira desinteresse ou personalidade.

**Recursos lidos:** `SKILL.md`, `references/feedback.md`.

**Resultado integral**

Roteiro proposto para conversa de melhoria, sem avaliação disciplinar:

“Pedro, quero combinar como deixar as análises conferíveis. Em duas reuniões, os números apresentados estavam sem período, e precisamos voltar à fonte. Tenho os exemplos anotados para vermos juntos; quero confirmar se o registro corresponde ao que aconteceu. Você contou que o relatório recebido não trazia o período e que nunca recebeu um padrão. Vamos olhar a origem e o apoio que faltou antes de definir a próxima entrega. Como você recebeu os dados e o que conseguiu conferir?”

Após ouvir e revisar os exemplos: “Proponho que a equipe forneça um padrão simples: indicador, valor, período, fonte e limitações. Se o período não vier na fonte, sinalizar ‘período não informado’ e pedir esclarecimento; não completar por suposição. Vamos revisar juntos a primeira análise com esse padrão e depois conferir sua aplicação numa próxima oportunidade.”

Plano curto proposto:

| Ação | Responsabilidade proposta | Evidência |
|---|---|---|
| Verificar os exemplos e a ausência de período na fonte | Pedro + gestor | Fonte e exemplo alinhados, sem atribuição indevida |
| Disponibilizar padrão e acesso a quem esclarece a origem | Gestor/equipe que fornece relatório | Modelo compartilhado com um exemplo correto e um com lacuna |
| Preparar próxima análise usando o padrão | Pedro, com apoio inicial | Valores ligados a período e fonte; ausências explicitadas |
| Revisar a primeira aplicação e depois uma aplicação independente | Gestor + Pedro | Campos conferidos na fonte; registrar ajuda e dúvidas restantes |

Acordar na conversa as oportunidades e prazos possíveis, sem estudo fora do expediente presumido. Avanço será observado pela rastreabilidade das próximas análises, não pela reunião realizada. Fonte incompleta e padrão não comunicado são condições a tratar; os fatos não sustentam desinteresse ou diagnóstico de personalidade. Roteiro preparado, conversa e acordo ainda não realizados.


## training-specialist

**Pedido exato**

Planeje treino da tarefa de conferir proposta para 12 pessoas, sessão 45 minutos por pessoa; só 4 podem sair da operação de cada vez. Entre 20 devoluções,12 foram por acesso,5 por habilidade e 3 sem causa identificada. Só três pessoas estão com lacuna de habilidade confirmada. Explique público/intervenção recomendada e logística se a liderança quiser envolver todos, com prática e evidência. Não invente regra fiscal nem prometa ROI.

#### Variação após identificar sobreposição com exemplo da referência
São 14 pessoas, 40 minutos por pessoa, máximo 3 fora da operação; de 17 devoluções, 9 são por acesso, 4 por habilidade e 4 com causa desconhecida; só quatro pessoas com lacuna confirmada. Recomende público/intervenção, logística se todos forem envolvidos, prática/evidência. Não conclua causas gerais ou ROI.

**Recursos lidos:** `SKILL.md`, `references/needs-and-design.md`, `references/materials-and-practice.md`, `references/evaluation-and-transfer.md`.

**Resultado integral**

Recomendo prática dirigida às **três pessoas com lacuna de habilidade confirmada**, acompanhada da remoção dos bloqueios de acesso. Entre 20 devoluções, 12 são classificadas por acesso (60%), 5 por habilidade (25%) e 3 sem causa identificada (15%); são proporções das devoluções fornecidas, não de toda a operação, nem contagem de pessoas. As cinco devoluções por habilidade não equivalem a cinco pessoas.

Separar intervenções: corrigir/verificar acesso nos casos correspondentes; treinar a tarefa para as três pessoas identificadas; investigar as três devoluções sem causa antes de escolher resposta. Uma introdução comum para todos pode ser útil se a liderança quiser padronização, mas a amostra não demonstra lacuna de habilidade em todas as 12 pessoas.

Logística: uma turma das três pessoas confirmadas cabe no máximo de quatro afastadas. Se envolver todos: **três turmas de quatro × 45 minutos = 135 minutos de facilitação sequencial**, sem contar preparação/transições. Cada pessoa participa 45 minutos; carga total dos participantes = 12 × 45 = 540 minutos-pessoa (9 horas-pessoa). Não remover mais de quatro simultaneamente; confirmar cobertura e acesso antes de marcar horários.

Objetivo proposto: conferir uma proposta contra sua solicitação e condições aprovadas, identificar divergência ou informação ausente e devolver registro que permita corrigir, sem criar regra fiscal. Material: solicitação/condições fonte, proposta fictícia, checklist breve e folha de resposta. Checklist interno real deve ser fornecido/conferido antes de aplicar em trabalho real.

Agenda de 45 minutos por turma: 5 min de objetivo/acesso; 8 min de exemplo demonstrado; 12 min de tentativa individual; 10 min de feedback sobre evidências; 7 min de nova tentativa equivalente; 3 min de fechamento e aplicação. Soma 45. O facilitador não resolve a tentativa individual antes de observá-la.

Exercício autoral fictício: solicitação aprovada pede revisão de até 30 produtos por R$ 600, prazo de quatro dias úteis após receber dados completos, sem publicação. Proposta de exercício diz 40 produtos, R$ 600, quatro dias úteis após contratação e inclui publicação. Participante entrega quadro “campo / fonte / proposta / divergência / informação a confirmar”. Critério: detectar as três divergências de escopo, gatilho do prazo e publicação, preservar preço correto e não inventar condições. Uma segunda proposta equivalente deve variar valores/escopo, mantendo tarefa e critérios, sem repetir resposta decorada.

Orientação ao facilitador: gabarito do exercício — 30 versus 40 produtos; dados completos versus contratação; publicação excluída versus incluída. A política do exemplo é só material fictício, não regra da empresa. Acesso bloqueado deve ser registrado como impedimento operacional e resolvido; não virar nota zero de habilidade. Alternativa em papel/texto pode permitir a prática, sem comprovar resolução de acesso real.

Evidência: registrar quem participou, realizou cada tentativa, divergências identificadas, falsas divergências e ajuda recebida. Propor conferir próxima proposta real das três pessoas com fonte disponível e feedback do responsável designado. Participação, aprendizagem observada e aplicação real são etapas separadas; nenhum teste foi aplicado aqui e não há demonstração de eficácia ou ROI.

**Limite específico:** a referência `needs-and-design.md` já contém o exemplo 20 devoluções (12/5/3) e a logística 12 pessoas / grupos de 4 / 45 minutos. O caso original não é independente desses exemplos, embora a resposta e o exercício acima tenham sido produzidos nesta execução.


## training-specialist — variação adicional

**Pedido exato recebido durante a execução**

> Acrescente uma variação independente training-specialist: 14 pessoas, 40 minutos por pessoa, máximo 3 fora da operação; de 17 devoluções, 9 acesso, 4 habilidade, 4 causa desconhecida; só quatro pessoas com lacuna confirmada. Recomendação de público/intervenção, logística se todos envolvidos, prática/evidência; não concluir causas gerais/ROI. Preserve original com seu limite. Não redefinir como controle semskill.

**Recursos usados:** os mesmos quatro arquivos do caso original, já lidos. Nenhuma pesquisa/desenho/gabarito externo consultado.

**Resultado integral**

Recomendo treino da tarefa para as quatro pessoas com lacuna confirmada, junto à solução dos bloqueios de acesso. As 17 devoluções classificadas são nove por acesso (52,94%), quatro por habilidade (23,53%) e quatro sem causa (23,53%). Essa distribuição caracteriza as devoluções informadas, sem concluir causas gerais da operação. As quatro pessoas com lacuna são um dado separado: não se deduz identidade ou quantidade de pessoas das quatro devoluções.

Acesso precisa de correção e teste pelo responsável pertinente; os casos sem causa precisam de investigação. Os dez participantes restantes não têm lacuna confirmada; envolvê-los numa padronização geral pode ser decisão da liderança, sem classificá-los como deficientes.

Com no máximo três fora da operação, o grupo dirigido de quatro requer **duas turmas**, por exemplo três + uma, com 40 minutos cada: 80 minutos de facilitação sequencial e 160 minutos-pessoa. Se todos os 14 participarem, serão **cinco turmas: 3 + 3 + 3 + 3 + 2**, cada uma de 40 minutos: 200 minutos (3h20) de facilitação sequencial e 560 minutos-pessoa (9h20). Preparação, troca de turma e recuperação da operação não estão incluídas nesses totais. Cobertura, acessos e horário ainda precisam ser confirmados, sem agenda inventada.

Objetivo: conferir proposta usando a solicitação e as condições aprovadas como fonte, registrar divergência e lacuna sem inventar regra. Sessão por turma: 4 min de objetivo/acesso; 7 min de demonstração; 10 min de prática individual; 8 min de feedback; 8 min de nova tentativa equivalente; 3 min de aplicação/fechamento. Soma: 40 minutos por participante.

Material fictício para prática: a fonte aprovada pede revisão de 12 produtos por R$ 240, inclui uma rodada de revisão e não informa prazo. A proposta de exercício apresenta 12 produtos por R$ 280, duas rodadas e prazo “amanhã”. Participante deve entregar registro rastreável com divergência e pendência. Critério: apontar preço e quantidade de revisões divergentes, manter o escopo de 12 produtos e indicar que o prazo da proposta não tem suporte na fonte. Não completar prazo nem política fiscal.

Orientação ao facilitador: observar a tentativa antes de explicar; demonstrar o vínculo fonte/campo quando houver dificuldade, dar nova tentativa com dados equivalentes e registrar ajuda. Não avaliar capacidade pela falha de acesso. Material em texto/papel permite praticar a conferência, mas não prova resolução do acesso ao sistema.

Registrar convidados, participantes, tentativas completas, divergências detectadas, falsos apontamentos e ajuda, com denominadores distintos. Propor conferir uma próxima proposta real de cada pessoa treinada, com fonte e acesso disponíveis, para observar aplicação e oferecer retorno. Presença não comprova aprendizagem; acerto fictício não comprova aplicação; mudança operacional não prova contribuição causal ou ROI. Nenhuma sessão ou avaliação de pessoas foi executada aqui.

**Limite da variação:** números, limite de turma e exercício foram alterados, exigindo nova conta, mas o avaliador já havia lido os exemplos originais. É variação adicional no mesmo contexto, não uma sessão virgem, controle sem skill ou prova de generalização.

## Autoavaliação crítica, feita após produzir as respostas

Critério utilizado: adequação observada a cada pedido, fidelidade ao material, utilidade da entrega e limites da evidência. Não há escore científico, porcentagem de eficácia do catálogo ou comparação causal entre uso e ausência de skill. O avaliador também produziu as respostas: esta revisão é autocrítica, não um segundo juiz independente.

| Caso | Adequação observada | Limite ou melhoria ainda pertinente |
|---|---|---|
| data-specialist | Tabela e tickets sobre cobertura conhecida, receita ausente preservada e conferência proposta | A comparação entre subconjuntos não resolve o ticket completo de A; base original não inspecionada |
| presentation-specialist | HTML real, quatro telas, marca, condição do cálculo, navegação e proposta sem benefícios inventados | Render/legibilidade no navegador ainda pendentes nesta unidade; teste de lógica não cobre dimensões reais |
| spreadsheet-specialist | Especificação com SKUs texto, fórmulas e total 120; extensão por tabela; distinção entre conta e recálculo | Compatibilidade de referências estruturadas e comportamento de linha incompleta precisam de implementação/conferência no XLSX, que não foi pedido |
| executive-assistant | Decisão, disponibilidade condicional, solicitação e lacunas separadas; datas relativas mantidas | Joana “pode revisar” não deve virar compromisso incondicional: a resposta conserva disponibilidade a confirmar |
| project-manager | Dependências e quatro dias de Ana com restrição semanal visíveis; esforço sete distinto de calendário | Quatro semanas de alocação não são quatro semanas decorridas garantidas; datas dependem do calendário/dia de Ana |
| product-specialist | Problema priorizado por relatos e teste mínimo; preferência contrária preservada, sem alertas/plataforma | Casos e critério são propostas; esforço deve ser confirmado e teste de compreensão não prova redução real de erros |
| logistics | 75% pontuais sobre 20, atrasados em trânsito preservados, R$ 20/pedido e ausência de OTIF | Status/contas sintéticos não comprovam entrega nem permitem atribuir causa à transportadora |
| contract-assistant | Compara apenas gatilho/unidade/revisão com citações exatas e dúvidas | Contrato completo/jurisdição não consultados; nenhuma interpretação de validade ou contagem aplicável |
| quality-specialist | Taxa 8% definida, turno sem denominador, modelo como hipótese, contenção e teste | Critério zero/100 é proposta local, não exigência recebida nem garantia estatística; cobertura/exposição precisam ser negociadas |
| people-development | Roteiro observável e apoio à origem/padrão; perspectiva de Pedro preservada | Acordos e aplicação seguem propostos; faltam datas/capacidade reais, sem inferência pessoal |
| training-specialist | Público dirigido e logística correta, agenda/exercício/evidência utilizáveis | Caso original compartilha exemplo do recurso; variação numérica adicional reduz repetição literal, sem eliminar contaminação ou contexto comum |

### Achados e conflitos efetivamente observados

1. **Sobreposição de fixture no treinamento (limite de desenho da avaliação):** `skills/training-specialist/references/needs-and-design.md:7` contém as 20 devoluções 12/5/3; a linha 17 contém 12 pessoas, grupos de quatro, 45 minutos e 135 minutos. O input original repete esses valores. Isso limita o poder discriminante do caso e não é falha funcional da skill. A variação adicional exige 5 turmas/200 minutos e público dirigido em 2 turmas/80 minutos, mas segue no mesmo contexto após exposição.
2. **Verificação de apresentação incompleta nesta unidade (falha de cobertura do executor):** `skills/presentation-specialist/SKILL.md:19` e `skills/presentation-specialist/references/html.md:9` pedem verificar leitura e cortes no arquivo final. A revisão estática e o DOM simulado verificaram controles e conteúdo, mas não renderização. Isso deve permanecer pendente até inspeção em navegador. Não foi disfarçado como conformidade integral ou problema no pacote.
3. **Sem conflito bloqueante entre pacote e pedido encontrado nos outros casos.** As instruções para perguntar por lacuna decisiva não obrigaram interrupção: as entregas independentes avançaram e as lacunas ficaram identificadas. A especificação de planilha respeita o formato expressamente solicitado; o XLSX não é um requisito deste input, apesar do domínio habitual do pacote. Critérios locais de produto e qualidade foram propostos, sem reivindicar aprovação ou validação científica.

Os limites explícitos não devem ser convertidos em novos sistemas, formalidades ou restrições públicas da skill. Não alterei nenhum pacote para ajustar esta avaliação. As respostas são proporcionalmente detalhadas para serem revisáveis; em uso conversacional, várias poderiam ser reduzidas após definir contexto e formato preferidos.

### Verificações realizadas

- Todos os onze pedidos originais comparados literalmente com o arquivo de inputs por script Node local: presentes sem alteração.
- Cálculos independentes executados com Node existente: tickets 100/150 e total conhecido 1.750/15; receitas 60/60 e total 120; pontualidade 15/20, frete 400/20; etiqueta 8/100; turmas 3×45/12×45 e variação ceil(14/3)×40/14×40. Os resultados e arredondamentos foram revisados no texto.
- HTML inspecionado: quatro sections, CSS/JS embutidos, nenhum src/href remoto, CDN, import ou recurso CSS externo. Isso comprova estrutura autossuficiente; funcionamento offline em navegador ainda não foi demonstrado.
- Script do HTML executado em DOM simulado: Anterior/Próxima, setas, Home/End, limites, uma tela ativa, indicação de posição, botões nos extremos, transferência de foco quando um botão fica desabilitado e não interceptação de campos/modificadores. Passou. Não substitui um navegador real nem inspeciona estilo calculado, foco visual, leitor de tela, corte ou legibilidade.
- Impressão, exportação, XLSX, envio, instalação, contratação e execução de pedidos reais no Studio não fizeram parte da execução. Nenhum deles foi declarado aprovado.

### Estado da entrega

Onze respostas originais e uma variação de treinamento registradas; HTML real produzido nos dois paths de responsabilidade desta unidade, no checkout compartilhado. Pacotes não alterados, nenhum commit/push/publicação feitos por este avaliador. Integração e eventual renderização final pertencem ao responsável pelo lote. Evidência de proposta, aprovação/instalação e execução real permanece distinta das respostas sintéticas.

### Complemento da coordenação em 13/10/2026
A lacuna de renderização declarada nesta unidade foi coberta depois pela coordenação: Chromium real headless, quatro telas em 1440×1000 e 390×844, botões/setas/Home/End/extremos, ausência de overflow horizontal/erros/requests remotos. Screenshots desktop1/4 e mobile4 inspecionadas com leitura legível. [Prova](2026-10-12-work-skills-presentation-render-validation.json). Isso não altera o alcance original do executor; impressão, PPTX, leitor de tela e funcionamento real no Studio seguem não testados.
