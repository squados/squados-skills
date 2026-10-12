# Especialista em Planilhas — síntese da pesquisa

Consulta em 12/10/2026. Especialidade aprovada para criar, editar e conferir planilhas de trabalho, com arquivos utilizáveis e editáveis. Pesquisa para criação posterior; nenhum workbook ou pacote novo foi produzido.

## Fontes e alcance

- [Núcleo de criação e edição](2026-10-12-spreadsheet-specialist-skills-core.md): sete SKILL.md completos, incluindo uma referência local atual da OpenAI; recursos decisivos de importação, reestruturação e edição.
- [Negócio, auditabilidade e QA](2026-10-12-spreadsheet-specialist-skills-business.md): seis SKILL.md completos em cinco repositórios, seis apoios de comportamento e cinco licenças.
- [Métodos profissionais](2026-10-12-spreadsheet-specialist-methods.md): quinze documentos/artigos e duas páginas oficiais de webinars recentes; três casos fictícios com gabaritos e perturbações.

Consolidação: **treze SKILL.md principais distintos — doze públicos em dez repositórios e um pacote local**. São nove famílias de mantenedores. Hermes excel-author e seu upstream Anthropic xlsx-author pertencem à mesma linhagem metodológica, sem confirmação independente entre eles. Autoria, licença, SHA/hash local, data observada e escopo lido estão discriminados nas frentes.

Nenhum vídeo foi assistido ou teve transcrição recuperada nesta rodada; páginas e players tentados estão identificados. Não houve uso de conta, crédito, motor de planilha ou execução de script externo. A pesquisa não comprova compatibilidade ou preservação dos pacotes completos.

## Recomendação

Combinar **método geral do Hermes xlsx, simplicidade/preservação observadas no pacote local OpenAI, conciliação e diferenças orçamento/realizado da Anthropic, controles operacionais simples e conferências proporcionais do ICAEW**. Referências financeiras aprofundadas entram quando a tarefa pedir. Não copiar helpers ou construir um framework para toda planilha.

A pessoa pede controle, atualização, importação, correção ou comparação; a skill identifica intenção e entrega o arquivo quando ele é o objeto do trabalho. O workbook deve permitir alimentar dados e atualizar os cálculos pertinentes. Uma análise em prosa ou um HTML não substitui o Excel solicitado. Dados cuida da investigação/conclusão e Apresentações da comunicação HTML quando o pedido exigir essas competências.

## Decisões por componente

| Componente | Fontes | Decisão e motivo |
|---|---|---|
| Estrutura proporcional | OpenAI local, Hermes, ICAEW | **Aproveitar:** usar template e rotina existentes, campos necessários e cálculo legível. **Descartar:** capa, dashboard ou três abas obrigatórias em controle pequeno. |
| Tipos e importação | Hermes CSV, Microsoft/Google | **Adaptar:** tipo por significado da coluna, preservar IDs, datas e números calculáveis. **Descartar:** inferência numérica por célula e locale imposto silenciosamente. |
| Fórmulas editáveis | Hermes, financial xlsx-author, Headcount | **Aproveitar:** parâmetros de negócio identificados e dependências compreensíveis. **Descartar:** totais colados como valores quando precisam responder às entradas, ou proibição de toda constante matemática. |
| Preservação | Hermes restructuring, OpenAI local, MiniMax | **Adaptar:** inventário e alteração localizada conforme recursos presentes. **Descartar:** promessa universal de round-trip e mudança estrutural gratuita. |
| Conciliação | Anthropic reconciliation | **Aproveitar:** fontes/corte compatíveis, correspondências e pendências explicadas. **Descartar:** forçar diferença zero por plug ou parear apenas por valor parecido. |
| Orçamento e caixa | Anthropic variance, Open Accountant | **Adaptar:** previsto/realizado distintos, continuidade de saldo, vencimento e premissas. **Descartar:** previsão universal por média móvel ou receita confundida com recebimento. |
| Estoque e comissões | Modelos SMB, síntese operacional | **Adaptar:** regra real do negócio e casos de borda. Não importar ERP, supply-chain ou CFO para suprir uma tabela simples. |
| Recálculo e QA | MiniMax, Microsoft, LibreOffice, openpyxl | **Aproveitar a preocupação; corrigir execução:** fórmula, cache, cálculo e conferência do resultado são estados distintos. **Descartar:** script intacto e selo de sucesso por existência/exit 0. |
| Estilo e uso | ICAEW, Microsoft accessibility | **Adaptar:** cabeçalhos, formatos, largura, filtros e entrada reconhecível. Cor auxilia sem ser única portadora de significado; convenções financeiras não governam toda planilha. |
| Ferramentas | DSL Builders, OpenAI local, Hermes | **Escolher pelo benefício:** biblioteca, aplicação ou sessão disponível. **Descartar:** Java/Maven, Artifact Tool, conectores ou LibreOffice obrigatórios para todo pedido. |

## Achados que mudam a execução

**Fórmulas gravadas não são fórmulas calculadas.** [openpyxl](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html) não avalia fórmulas; `data_only` lê resultados armazenados segundo o [tutorial](https://openpyxl.readthedocs.io/en/stable/tutorial.html). Cache pode faltar ou estar antigo. A coordenação leu essas páginas, cujo cabeçalho identifica 3.1.3, sem inferir versão instalada no Studio. No caminho openpyxl, representação de função/argumentos segue inglês/vírgula; interface e formatação podem ser PT-BR.

**Recálculo precisa de evidência no resultado.** O [script MiniMax consultado](https://github.com/MiniMax-AI/skills/blob/60aaae52bb2af8162732751a4332f62a5fef518b/skills/minimax-xlsx/scripts/libreoffice_recalc.py#L99) copia XLSX para diretório temporário e usa esse mesmo diretório como saída; caminho esperado coincide com a cópia de entrada. Existência do arquivo após returncode zero não demonstra que foi reescrito/recalculado. A coordenação conferiu o código e as linhas no raw original; é risco identificado por inspeção, sem reprodução do motor. O checker também pode omitir aba e shared consumer, e diverge nos códigos de saída entre formatos; detalhes na frente de QA.

**Preservação depende da operação e do recurso.** [openpyxl editing](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html) não gerencia automaticamente todas as dependências em inserção/exclusão. O helper Hermes pode conservar validação/tabela totalmente excluída e não configura VBA; não usar intacto como garantia. A biblioteca possui capacidades de preservação específicas, portanto afirmações de que todo gráfico/pivot/VBA sempre desaparece também são inadequadas. Conferir o arquivo concreto, ferramenta e operação.

**CSV não é workbook.** Conversor Hermes transforma `00123` em número pela inferência; `--no-infer` preserva texto, mas não resolve sozinho tipos de todas as colunas. CSV transfere uma tabela, sem abas, estilos e fórmulas equivalentes ao XLSX. Separadores, encoding, datas e zeros à esquerda precisam do contrato do receptor; aspas não garantem interpretação do Excel por duplo clique.

**Erro escondido pode virar valor falso.** `IFERROR(...,0)` serve quando zero é a regra acordada, sem constituir correção universal. Falta de chave, taxa ou referência pode precisar pendência explícita. Vazio não significa zero; saldo negativo pode ser informação importante; alta de despesa não é automaticamente resultado favorável.

**Modelos e defaults precisam reconciliar.** Pontes de variação devem fechar com o total, incluindo convenção para interações preço/volume/mix. Retenção do último registro exige regra explícita; [Table.Distinct](https://learn.microsoft.com/en-us/powerquery-m/table-distinct) não garante em geral qual duplicado sobrevive. Não chamar qualquer residual de causa ou remover duplicados sem semântica.

## Avaliação posterior

Os [casos fictícios](2026-10-12-spreadsheet-specialist-methods.md) avaliam arquivo editável, regra, preservação, tipos e recálculo; a coordenação conferiu a aritmética novamente com valores decimais:

| Caso | Resultado e perturbação | Falha que detecta |
|---|---|---|
| Caixa | Saldo conhecido R$ 1.295,25 e uma saída pendente; entrada +R$ 50 leva a R$ 1.345,25 | Vazio convertido em zero, cache antigo, perda da aba auxiliar |
| Estoque | SKU 0012 saldo 3/reposição 1; SKU 0034 saldo 0/reposição 2; saída extra leva primeiro saldo a −1/reposição 5 | ID sem zeros, negativo truncado, regra de contagem tratada como movimento |
| Comissões | Total conhecido R$ 66,67 e uma pendência; taxa 6% leva a R$ 80,00 | Cancelamento pago, taxa/texto errados, valor congelado e alterações fora do escopo |

Não foram criados workbooks, fórmulas executadas ou caches produzidos nesses casos. A fase prática deve inspecionar fórmula/regra, resultado esperado, recálculo no motor disponível e arquivo final. Alterar uma entrada e observar o efeito correto é prova mais útil que encontrar a string de uma fórmula.

Estados separados: gerado; abre; fórmula inspecionada; cache lido; recalculado; render conferido; preservação conferida; pedido real executado. Verificação deve cobrir o que importa ao arquivo recebido, sem impor suíte sobre recursos inexistentes. Se faltar motor, entregar o possível e indicar recálculo pendente; não fabricar cache como evidência.

## Núcleo e referências

Núcleo futuro: aproveitar pedido/template, perguntar por regra material, inspecionar antes de editar, criar estrutura simples, preservar tipos e recursos, usar cálculos editáveis e conferir entrega. Orientação breve de uso acompanha o arquivo. Referências por intenção: importação/locale; fórmulas e recálculo; preservação/reestruturação; tabelas e validações; orçamento/caixa; estoque/comissões; conciliação; gráficos e impressão.

Scripts apenas para benefício concreto, como grandes importações, inventário ou conferências repetidas; não criar motor de fórmulas próprio. Confirmar ferramentas e versões no pedido real. Dependência necessária ausente: explicar utilidade e oferecer instalação/preparação simples ou alternativa suficiente, sem mandar a pessoa rodar comandos. Instalação possível para execução não equivale à elegibilidade do pacote na galeria.

Quando preferência recorrente ou atrito justificar, oferecer adaptar a própria versão: padrão de colunas, calendário, definição de saldo ou forma de alimentar modelos. Aplicar com aceitação ou pedido; a regra da empresa permanece em sua versão/contexto. Bibliografia e histórico extensos ficam no dossiê, fora da skill executável.

## Licenças e estado

Hermes xlsx e vários modelos independentes têm MIT observada; financial-services xlsx-author tem Apache-2.0 confirmada, distinta do [xlsx proprietário Anthropic](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx/LICENSE.txt), que restringe cópia/derivados/distribuição. A coordenação leu a restrição; não copiar o pacote. A referência local OpenAI não teve licença de redistribuição estabelecida; é inspiração de critérios, sem transportar runtime ou texto. Declarações incompletas de DSL/theNeoAI não equivalem a revisão legal integral. O LICENSE raiz knowledge-work consultado contém corpo Apache e texto adicional atípico ao final; registrar revisão e revisar recursos/avisos concretos antes de eventual reprodução.

Consulta com síntese própria não autoriza distribuir código, templates ou assets. Pacotes completos, recursos transitivos, macros, conexões e preservação precisam de verificações próprias se forem usados. Nenhuma origem pesquisada altera a allowlist github ou a seleção atual da galeria.

Pesquisa e gabaritos registrados; ainda sem skill nova, instalação, contratação Hermes, uso real no Studio ou publicação. Não houve contas, crédito pago, motor de cálculo, nova dependência ou push. As duas pastas temporárias de leitura de rodadas anteriores permanecem fora dos commits após rejeições de remoção já registradas; nenhum contorno foi realizado.
