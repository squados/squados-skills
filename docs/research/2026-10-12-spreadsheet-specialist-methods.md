# Especialista em Planilhas — métodos profissionais e avaliação

Pesquisa em 12/10/2026. Frente de métodos da décima pesquisa de 33. Documento de pesquisa para criação posterior; não cria pacote, workbook ou item do catálogo. Comparações de skills pertencem às outras frentes. Nenhuma instalação, conta, operação de planilha real ou publicação foi realizada.

## Direção recomendada

A especialista deve resolver o pedido de trabalho no formato que a pessoa usa: organizar dados, criar um controle, corrigir cálculos, resumir resultados ou atualizar um arquivo existente. O núcleo serve tanto um caixa de cinco linhas quanto uma análise maior. Não obrigar um modelo financeiro, uma aba de capa, um dashboard ou scripts em todo pedido.

O padrão é aproveitar contexto e arquivos, identificar a decisão ou rotina, preservar o que já funciona e entregar algo que a pessoa consiga alimentar e conferir. Uma pergunta só é necessária quando a resposta muda números, escopo, preservação ou destino. Ferramentas, funções e formato seguem o ambiente disponível; não presumir Excel, Google autenticado, LibreOffice, Python ou bibliotecas instaladas.

## Referências profissionais e decisões

O [ICAEW, edição 2024 dos vinte princípios](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition), sustenta proporcionalidade ao risco, finalidade e público, entradas/processos/saídas compreensíveis, qualidade dos dados, fórmulas simples e consistentes, parâmetros separados e checks. A síntese útil é clareza e conferência, com documentação proporcional. Não copiar seu template nem transformar cada controle em metodologia completa.

A [FAST Standard Organisation](https://fast-standard.org/) apresenta flexibilidade, adequação, estrutura e transparência para modelos financeiros. Aproveitar simplicidade e lógica legível; adaptar consistência ao arquivo recebido. Descartar a imposição de convenções de modelagem financeira a estoque, cadastro ou lista diária. O site consultado não mostra uma data de revisão geral; não apresentar como novidade de 2026 nem como certificação da futura skill.

As seguintes decisões são uma síntese própria para este destino, com evidências técnicas nas seções seguintes:

| Situação | Conduta recomendada | Motivo prático |
|---|---|---|
| Criar controle simples | Uma tabela legível, campos necessários, cálculo e check apropriado | A pessoa começa a usar sem preencher uma entrevista de modelagem |
| Melhorar arquivo existente | Inspecionar antes de editar; alteração localizada; cópia de saída quando houver risco de perda | Arquivos reais trazem fórmulas, nomes, objetos e regras que uma reconstrução pode apagar |
| Dados incompletos | Preservar desconhecido como desconhecido e mostrar a pendência | Zero é um valor; vazio não comprova ausência de movimento |
| Correção de cálculo | Investigar regra e dependências; mostrar antes/depois e exemplo independente | Fórmula sintaticamente válida pode representar a regra errada |
| Repetição recorrente | Primeiro fórmulas/tabela; automação só com ganho concreto | Código acrescenta dependência e manutenção |
| Importação de CSV | Descobrir delimitador, encoding, tipos e datas antes de converter | Código de produto e número de telefone não são quantidades |
| Entrega em Sheets | Confirmar autorização e destino no contexto; usar ferramenta disponível | Upload e edição em nuvem são ações externas, não simples geração de XLSX |

## Contratos técnicos que mudam a execução

### Fórmula escrita, cálculo e cache são coisas diferentes

A documentação [openpyxl: fórmulas](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html) afirma que a biblioteca não calcula fórmulas e exige nomes de funções em inglês e argumentos separados por vírgulas. Uma fórmula PT-BR para a interface do Excel não deve ser colada literalmente no arquivo por esse caminho. Compatibilidade de funções novas precisa de checagem específica; prefixar `_xlfn.` não comprova execução no aplicativo de destino.

O [tutorial openpyxl](https://openpyxl.readthedocs.io/en/stable/tutorial.html) diferencia fórmula de resultado armazenado: `data_only=True` lê o valor registrado no último cálculo, não executa a fórmula. Pode faltar cache ou ele estar antigo. A leitura de valores serve para inspeção; não usá-la como objeto de edição que deve preservar as fórmulas. O tutorial alerta que salvar sobrescreve sem aviso e que formas podem desaparecer. `keep_vba` preserva elementos VBA, sem editá-los; não promete preservação universal.

A página stable consultada identifica documentação **3.1.3**; isso descreve a fonte lida, não a versão instalada no Studio nem necessariamente a versão mais nova disponível.

O [Excel: recálculo, iteração e precisão](https://support.microsoft.com/en-us/excel/change-formula-recalculation-iteration-or-precision-in-excel) distingue modo de cálculo e precisão. Não confundir duas casas exibidas com arredondamento da regra; mudar a precisão para o valor exibido altera os cálculos. Registrar motor, modo e efetiva atualização quando o pedido exigir números atuais.

O [LibreOffice: Recalculate](https://help.libreoffice.org/latest/en-US/text/scalc/01/06080000.html?DbPAR=CALC) diferencia o recálculo comum do recálculo de todas as fórmulas. Salvar/converter um arquivo com um processo headless não deve ser tomado automaticamente como prova suficiente: a futura execução precisa verificar valores conhecidos após o recálculo, erros e preservação. Não instalar LibreOffice nesta pesquisa.

### Preservação exige mais que abrir e salvar

[openpyxl: inserção, exclusão e movimentação](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html) informa que inserções/exclusões não gerenciam automaticamente dependências como fórmulas, tabelas e gráficos. `move_range(..., translate=True)` traduz referências das células movidas, não todas as referências externas ao intervalo nem nomes definidos. Evitar mudanças estruturais gratuitas; quando necessárias, verificar os consumidores afetados.

Inventário proporcional proposto para arquivo recebido: abas e ordem, intervalos usados, fórmulas, tipos e formatos, tabelas, nomes definidos, validações, filtros, linhas/abas ocultas, proteção, gráficos/objetos, macros, links externos e consultas. Não exigir revisão exaustiva de recursos inexistentes. Não executar macros nem atualizar conexões externas incidentalmente.

Comparar o arquivo anterior e o final nos elementos tocados e nos elementos que precisam permanecer intactos. ZIP/XML válido ou leitura sem exceção comprova estrutura, não equivalência funcional de todo o workbook. Se a ferramenta não preserva um recurso presente, escolher outra ferramenta disponível ou delimitar a entrega antes de modificar o original.

### Circularidade e erros

A [Microsoft: circular references](https://support.microsoft.com/en-gb/excel/remove-or-allow-a-circular-reference-in-excel?nochrome=true) orienta localizar e corrigir referências circulares; iteração serve a modelos em que a circularidade é deliberada. Para controles cotidianos, não habilitar iteração para esconder um erro. Preservar e investigar configurações existentes de modelos especializados.

Recomendação própria: revisar `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, `#NUM!` e erros de expansão no escopo pertinente. Diferenciar erro técnico de ausência esperada. Não aplicar `IFERROR(...,0)` a tudo: isso pode transformar código inexistente, valor inválido ou divisão impossível em resultado comercial aparentemente legítimo. Uma pendência deve continuar visível e localizável.

### Tipos, locale e formato de saída

A [Microsoft: importação/exportação de texto](https://support.microsoft.com/en-us/excel/get-started/import-or-export-text-txt-or-csv-files?ad=US&rs=en-US&ui=en-US) documenta controle de tipos na importação, incluindo zeros à esquerda e datas. A [lista oficial de formatos Excel](https://support.microsoft.com/en-US/Excel/file-formats-that-are-supported-in-excel) distingue formatos de workbook e texto; CSV salva apenas a aba ativa. Logo, uma exportação CSV não substitui um arquivo com abas, fórmulas, estilos ou macros.

Em [Google Sheets: locale e cálculo](https://support.google.com/docs/answer/58515?hl=en-GB), locale, fuso, idioma das funções e cálculo são configurações distintas. Alterar locale afeta moeda, datas e números para todos os colaboradores; não mudar silenciosamente para fazer uma fórmula passar. Usar o fuso existente, salvo requisito contrário.

[Google: Office files](https://support.google.com/docs/answer/9406611?hl=en-GB) distingue edição no formato Office, que salva mudanças no arquivo, de conversão para Sheets, que cria uma cópia. Importar, converter e editar são ações diferentes. A especialista deve explicar qual executou, conferir exportação e não prometer compatibilidade completa por ter aberto o XLSX na nuvem.

Proposta aplicada: conservar IDs como texto, valores monetários como números, datas com semântica verificada e percentuais como proporções. Definir delimitador e decimal conforme sistema receptor, não apenas país. CSV UTF-8 com `;` e decimal `,` pode servir um fluxo PT-BR específico; não é formato universal. Para valores numéricos, evitar escrever `R$ 1.234,56` como texto quando a coluna deve somar. Campos contendo delimitador, aspas ou quebra exigem escape correto. Declarar como faltantes são representados.

### Estilo que favorece uso

As [práticas de acessibilidade Microsoft](https://support.microsoft.com/en-au/accessibility/excel/accessibility-best-practices-with-excel-spreadsheets) favorecem cabeçalhos claros, tabelas simples, contraste e nomes úteis; células mescladas dificultam navegação assistiva. Adaptar ao cotidiano: largura suficiente, datas e moedas consistentes, cabeçalho visível, entrada reconhecível e alertas com texto. Cor pode ajudar, mas não ser o único significado. Não transformar vazio numérico em texto apenas para preencher visualmente: uma coluna de status pode explicar a falta.

Não há evidência de que azul para inputs, preto para fórmulas e verde para links seja regra universal de planilha comercial. Se o arquivo tiver convenção, respeitá-la; se não, usar distinção discreta explicada em uma linha. Gráfico entra quando responde uma pergunta, não como decoração obrigatória.

### Duplicados e importações repetidas

Em [Table.Distinct, Microsoft Learn](https://learn.microsoft.com/en-us/powerquery-m/table-distinct), revisão visível em **13/08/2026**, o registro sobrevivente não é garantido em geral devido a folding/otimizações; buffering pode tornar remoção previsível. Portanto, “ordenar e remover duplicados” não comprova que ficou o mais recente.

O artigo profissional [Leila Gharani: Keep the Latest Record](https://www.xelplus.com/power-query-keep-latest-record/), publicado **09/06/2026**, alterado **03/07/2026**, mostra o problema num estoque e compara buffering com agrupamento por timestamp. Fonte lida: artigo textual, não vídeo. Aproveitar a conferência contra fonte e regra explícita de retenção. Não copiar a query inteira ou inferir que buffering é necessário em todo CSV. Empates precisam de regra ou aviso.

## Materiais recentes em vídeo: nível real de consulta

| Material | Autor/data verificável | O que foi consultado | Contribuição e limite |
|---|---|---|---|
| [50+ new Excel features from this half decade](https://www.icaew.com/technical/technology/excel-community/webinars-excel/2025/50-new-excel-features-from-this-half-decade) | ICAEW Excel Community; palestrante David Benaim, Xlconsulting; 03/04/2025 | Página oficial, descrição, links e iframe Brightcove | Existe programa recente de funções/recursos e indicação de legendas automáticas. O player retornou página sem texto. Transcrição e audiovisual não consultados; nenhum timestamp ou técnica específica atribuído ao vídeo |
| [AI and Excel: Clean, Create, Code & Customise](https://www.icaew.com/technical/technology/excel-community/webinars-excel/2026/ai-and-excel) | ICAEW Excel Community; Andrew Paw e Fay Bordbar; 08/09/2026 | Página oficial e iframe Brightcove | A descrição aborda limpeza, criação, automação, consistência e validação/auditabilidade de resultados de IA. Legendas automáticas anunciadas; texto da transcrição não recuperado. Nenhum timestamp ou alegação de prática assistida |

Foram buscados materiais gratuitos 2025–2026 de Leila Gharani. O candidato [Power Query for Beginners](https://www.youtube.com/watch?v=x7mzOYEn0XA) apareceu em indexação externa com data 24/07/2025, mas o YouTube retornou erro nesta consulta; a página [toolkit oficial](https://www.xelplus.com/learn-power-query/) foi acessível, sem transcrição textual. Não contar data do espelho como confirmação primária nem usar capítulos de espelho como conteúdo assistido. Não houve consulta paga, vidIQ, créditos ou login. A lacuna de transcrição não bloqueia os critérios resolvidos por documentação oficial e artigo profissional textual; a pesquisa parou sem perseguir quantidade.

## Fluxo e organização para criação posterior

O núcleo pode ser curto: reconhecer intenção a partir do pedido e materiais; aproveitar o arquivo; esclarecer regra material; escolher abordagem compatível; executar alteração/geração; conferir números, estrutura e apresentação; entregar com o estado verdadeiro. Perguntas sobre biblioteca, linguagem ou ferramenta não pertencem ao caminho de quem pediu “organize minhas vendas”.

Carregar referências sob demanda para importação/locale, fórmulas/recálculo, preservação de arquivo, apresentação e automação repetida. Exemplos profissionais e bibliografia ficam neste dossiê. Scripts futuros só entram se evitarem trabalho repetitivo ou erros demonstrados — por exemplo, inspecionar inventário e comparar fórmulas, validar CSV ou recalcular e conferir resultados. Não criar framework genérico de planilhas nem motor de fórmulas próprio.

Se faltar capacidade essencial, a oferta pode ser: “Posso preparar o arquivo agora. Para conferir os cálculos automaticamente, falta um programa de planilhas neste computador. A instalação mínima indicada é [opção compatível identificada]; ela permite [benefício concreto].” Antes disso, verificar se Excel ou outro motor já disponível resolve. Não empilhar Python, LibreOffice e conectores por padrão. O agente faz os passos técnicos autorizados; não pedir comandos ao usuário.

Quando uma preferência recorrente ou atrito concreto justificar, oferecer adaptar a própria versão da skill: por exemplo, padrão de colunas, definição de saldo ou calendário de fechamento. Explicar benefício e aplicar com aceitação ou pedido, sem transformar convenções da empresa em padrão público. No pedido pontual, preservar o modelo existente e acrescentar só o que resolve o problema. Não confundir instalação autorizada para execução com elegibilidade atual de contratação na galeria.

## Evidências de entrega

| Estado | Evidência necessária | O que não prova |
|---|---|---|
| Gerado | Arquivo existe, formato e nome corretos, conteúdo estrutural legível | Abre no aplicativo, calcula ou é bonito |
| Abre | Aplicativo identificado abre sem reparo/perda relatada | Valores atualizados ou preservação completa |
| Fórmulas verificadas | Fórmulas e referências pertinentes inspecionadas, regra e consistência conferidas | Motor executou as fórmulas |
| Cache inspecionado | Leitura dos resultados armazenados, presença e origem registradas | Cache recente, completo ou correto |
| Recalculado | Motor/versão identificado, recálculo efetivo e salvamento; valores reabertos e conferidos | Igualdade entre todos os aplicativos |
| Render conferido | Visual final, larguras, clipping, formatos, gráficos pertinentes | Correção aritmética |
| Preservação conferida | Comparação antes/depois dos elementos relevantes e mudanças intencionais | Funcionalidade de recursos não exercitados |
| Pedido real executado | Arquivo e dados reais autorizados, ação e resultado observado | Aprovação universal para outros arquivos |

Não usar “100% funcional” porque um script terminou. Entrega sem motor pode conter fórmulas e valores esperados conferidos independentemente, mas deve dizer que o recálculo no aplicativo permanece pendente. Não inventar caches para simular evidência.

## Casos fictícios PT-BR para avaliação posterior

Não são workbooks criados ou testados; são especificações e gabaritos independentes. Os dados e cálculos abaixo são próprios e fictícios. Avaliar o resultado entregue no seu formato final, inclusive valores lidos após recálculo quando aplicável.

### Caso 1 — caixa diário com incompletude explícita

Pedido: “Atualize meu caixa de outubro com estes lançamentos e me diga o saldo.” Arquivo hipotético `caixa-outubro.xlsx`: aba `Caixa`, saldo inicial numérico de **R$ 1.000,00**; fórmulas sequenciais de saldo, formato PT-BR, aba auxiliar existente que deve permanecer.

| Data | Documento (texto) | Entrada | Saída | Situação |
|---|---|---:|---:|---|
| 01/10/2026 | 0001 | 250,00 | 0,00 | Confirmado |
| 02/10/2026 | 0002 | 0,00 | 80,50 | Confirmado |
| 03/10/2026 | 0003 | 125,75 | 0,00 | Confirmado |
| 04/10/2026 | 0004 | 0,00 | vazio | Saída ainda não informada |

Gabarito: saldos confirmados **R$ 1.250,00; R$ 1.169,50; R$ 1.295,25**. Entradas **R$ 375,75**, saídas conhecidas **R$ 80,50**; `1000 + 375,75 - 80,50 = 1295,25`. Check independente `saldo conhecido - inicial - entradas + saídas conhecidas = 0`.

A linha 4 não prova uma saída zero nem saldo final fechado. Resultado deve dizer **“Saldo conhecido: R$ 1.295,25; saldo final pendente: 1 saída sem valor”**, preservando zero e vazio. Aceitar fórmula que marca essa linha como pendente; reprovar preenchimento automático com zero. Os IDs mantêm quatro caracteres.

Checagens: fórmulas anteriores e aba auxiliar preservadas; novo lançamento validado; cache antigo não tratado como atual. Perturbação de avaliação: entrada 1 muda de 250,00 para 300,00. Depois de recálculo, saldo conhecido esperado **R$ 1.345,25** e pendência permanece. Um valor igual ao anterior denuncia cache/recálculo insuficiente.

### Caso 2 — estoque por movimento e CSV sem perda de IDs

Pedido: “Veja o que preciso repor; devolva o Excel e um CSV para importar.” Origem hipotética UTF-8, delimitador `;`, decimais `,`, IDs textuais `0012` e `0034`. Regra fornecida: saldo = inicial + entradas - saídas; alerta quando saldo < mínimo; sugestão para atingir mínimo, sem lote obrigatório.

| Código | Inicial | Entradas | Saídas | Mínimo |
|---|---:|---:|---:|---:|
| 0012 | 10 | 5 | 12 | 4 |
| 0034 | 0 | 0 | 0 | 2 |

Gabarito: `0012 = 10 + 5 - 12 = 3`, reposição **1**; `0034 = 0`, reposição **2**. Saldo agregado **3 unidades**, mínimo agregado **6**, sugestão **3**. Zero é estoque conhecido, não dado faltante. Uma saída adicional de 4 para `0012` dá saldo **−1** e sugestão **5**; não truncar saldo negativo silenciosamente.

CSV de valores esperados, conforme contrato fictício do receptor:

```csv
codigo;saldo;reposicao
0012;3;1
0034;0;2
```

No XLSX, `codigo` é texto, cálculos numéricos e filtros úteis. No CSV, bytes `0012` permanecem, mas a interpretação como texto exige importador adequado; aspas não garantem que abrir com duplo clique no Excel mantenha zeros. Conferir contagem de registros, nomes de colunas e números exportados. CSV não carrega fórmulas ou duas abas do Excel.

Variação de regra: se dados forem **contagens instantâneas**, não somar como movimentos. Para mesmo produto/local, contagem 9 em 10/10 às 09:00 e 3 às 15:00 dá estoque **3**, não 12. Sem critério de desempate, duas contagens diferentes no mesmo horário são pendência. Essa variação avalia reconhecimento da intenção sem impor Power Query.

### Caso 3 — comissões e preservação de fórmula/localidade

Pedido: “Corrija as comissões nesta planilha sem mexer no restante.” Arquivo hipotético PT-BR com abas `Vendas`, `Regras` e `Histórico`, tabela existente e fórmula errada que paga cancelamentos. Regra já documentada: pagar **5% sobre recebimento de venda ativa**, arredondar cada comissão a centavos; venda cancelada recebe 0; recebido ainda desconhecido fica pendente. A taxa está em célula numérica separada em `Regras`, não escondida no cálculo.

| ID | Pessoa | Situação | Recebido |
|---|---|---|---:|
| 0001 | Ana | Ativa | 1.000,00 |
| 0002 | Ana | Cancelada | 500,00 |
| 0003 | Bruno | Ativa | 333,33 |
| 0004 | Bruno | Ativa | vazio |
| 0005 | Bruno | Ativa | 0,00 |

Gabarito: **R$ 50,00; R$ 0,00; R$ 16,67; pendente; R$ 0,00**. Ana **R$ 50,00**, Bruno conhecido **R$ 16,67**, total conhecido **R$ 66,67**, uma pendência. Recebimentos ativos conhecidos **R$ 1.333,33**; recebimento cancelado **R$ 500,00** fora da base. A fórmula errada que paga também cancelamento acrescenta **R$ 25,00** e pode produzir total **R$ 91,67**: a correção deve eliminar essa diferença.

Uma fórmula localizada que a pessoa digita pode começar por `SE` e usar `;`; a representação produzida por openpyxl deve seguir funções inglesas e vírgulas. Não converter indiscriminadamente fórmulas existentes pela aparência do idioma; distinguir representação interna de exibição. Não escrever `5` onde se espera `0,05`.

Perturbação: taxa muda para **6%**. Após recálculo, comissões conhecidas **R$ 60,00 + R$ 20,00 = R$ 80,00**; cancelada e zero continuam zero; pendência permanece. Check: soma das linhas conhecidas = soma dos totais por pessoa. `Histórico`, tabela, nomes, validações, estilos e fórmulas fora do escopo mantêm seu conteúdo. Nenhuma nova macro, iteração ou conta é necessária.

## Inventário das fontes e limites de reutilização

**17 fontes selecionadas: 15 documentos/artigos de método ou técnica e 2 páginas de webinars recentes.** Não contar buscas, espelhos, player vazio ou links relacionados como evidências independentes. Todas consultadas em 12/10/2026. Datas não visíveis permanecem não verificadas.

| Fonte | Autoria / edição visível | Contribuição | Nível consultado |
|---|---|---|---|
| ICAEW 20 principles | ICAEW, edição 2024 | Qualidade proporcional e lógica auditável | Página e resumo oficial; sem download de template |
| FAST | FAST Standard Organisation, sem revisão geral visível | Clareza de modelos; aplicação limitada ao contexto | Homepage, não standard completo |
| openpyxl simple_formulae | openpyxl docs 3.1.3 | Escrita de fórmulas, ausência de avaliação | Página técnica |
| openpyxl tutorial | openpyxl docs 3.1.3 | Cache, flags, risco de perda ao salvar | Página técnica, trechos de leitura/salvamento |
| openpyxl editing_worksheets | openpyxl docs 3.1.3 | Dependências e referências ao alterar estrutura | Página técnica |
| Microsoft import/export text | Microsoft, data de revisão não exibida | Tipos, zeros e datas | Página oficial |
| Microsoft file formats | Microsoft, data de revisão não exibida | XLSX/XLSM/CSV e aba ativa | Página oficial |
| Microsoft recalculation | Microsoft, data de revisão não exibida | Cálculo, precisão, iteração | Página oficial |
| Microsoft circular references | Microsoft, data de revisão não exibida | Circularidade e usos especializados | Página oficial |
| Microsoft accessibility | Microsoft, data de revisão não exibida | Tabelas legíveis e navegação | Página oficial |
| Google locale/calculation | Google, data de revisão não exibida | Separação locale/fuso/funções/cálculo | Página oficial |
| Google Office files | Google, data de revisão não exibida | Edição versus conversão | Página oficial |
| LibreOffice Recalculate | The Document Foundation, ajuda latest | Recálculo comum versus todas as fórmulas | Página oficial; versão instalada desconhecida |
| Microsoft Table.Distinct | Microsoft, 13/08/2026 | Retenção não garantida de duplicados | Página técnica |
| XelPlus Keep the Latest Record | Leila Gharani, 09/06/2026; revisão 03/07/2026 | Exemplo profissional de verificação de estoque | Artigo completo; vídeo não assistido |
| ICAEW 50+ features | David Benaim / Excel Community, 03/04/2025 | Atualidade de recursos e candidato audiovisual | Página; player sem texto |
| ICAEW AI and Excel | Andrew Paw e Fay Bordbar / Excel Community, 08/09/2026 | Validação de IA mencionada na descrição | Página; player sem texto |

Nenhum workbook, screenshot, template, script, transcrição ou recurso de terceiros foi redistribuído. Este documento usa síntese própria e links. Acesso gratuito e autoria identificada não autorizam empacotar conteúdo; para copiar um recurso na criação futura, verificar sua licença específica, atribuição, avisos e compatibilidade com o destino. A homepage FAST menciona licença Creative Commons em sua seção de notícias, mas a licença e o texto do standard não foram auditados aqui. Documentação e cursos acessíveis não foram tratados como open source.

## Dúvidas resolvidas e pendências

Resolvido para a proposta: núcleo de trabalho cotidiano; clareza proporcional; preservação; tipos/locale; fórmulas e checks; circularidade; CSV e Sheets; critérios separados de cálculo e apresentação; 3 casos com gabaritos e perturbações verificáveis.

Pendências da criação/execução posterior: comparar candidatas nas outras frentes; identificar ferramentas reais do Studio e versões; escolher só recursos necessários; verificar licenças de qualquer arquivo copiado; testar os casos em artefatos e motor reais. Transcrições dos webinars não foram recuperadas; técnicas não dependem desse audiovisual. Nenhuma execução real de planilha foi demonstrada nesta pesquisa.
