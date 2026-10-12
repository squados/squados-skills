# Especialista em Planilhas — pesquisa de skills: núcleo de criação e edição

Data da consulta: 12/10/2026. Frente da décima pesquisa do catálogo de 33 especialistas. Escopo: criação e edição de arquivos editáveis, fórmulas, tipos, limpeza, validação, preservação e formato. Este documento não cria pacote nem altera a galeria.

## Resultado e alcance real

A melhor base pública geral encontrada é o `xlsx` do Hermes, complementada por regras verificadas diretamente na documentação do openpyxl. O `excel-author` do Hermes e seu upstream financeiro contribuem quando o pedido é um modelo financeiro, não como arquitetura obrigatória de toda planilha empresarial. O pacote local atual de Spreadsheets da OpenAI ajuda a avaliar simplicidade e preservação; seu runtime e seus materiais não devem ser presumidos disponíveis ou redistribuíveis no Studio.

Foram lidos integralmente **7 SKILL.md**: OpenAI Spreadsheets local; Anthropic xlsx; Anthropic financial-services xlsx-author; Hermes xlsx; Hermes excel-author; DSL Builders spreadsheet; theNeoAI spreadsheet-expert. São cinco famílias de mantenedores; `excel-author` e `xlsx-author` pertencem à mesma linhagem metodológica e não contam como confirmações independentes. Foram examinados seis recursos decisivos adicionais: licença Anthropic xlsx; licença financial-services; licença Hermes; referência Hermes de reestruturação; scripts Hermes `csv_to_xlsx.py` e `xlsx_restructure.py`; além dos dois workflows OpenAI e da referência theNeoAI `standards.md`. As contagens de recursos não constituem auditoria integral dos pacotes.

Descoberta por buscas em inglês sobre spreadsheet/excel/xlsx, GitHub e skills.sh. Os forks de Hermes encontrados pelo buscador foram descartados como evidência independente. Popularidade não foi utilizada como comprovação. Não foram instaladas nem executadas skills, scripts, contas, ferramentas pagas ou workbooks reais. Os achados de código abaixo são inspeção estática, não bugs reproduzidos.

## Proveniência, versões e acesso

| Fonte original e arquivos consultados | Revisão, autoria e data visível | Licença e limite |
|---|---|---|
| [Hermes xlsx](https://github.com/NousResearch/hermes-agent/blob/ff2d02f998f9f9e45543eea30fb935f47e4504a7/skills/productivity/xlsx/SKILL.md), `references/restructuring.md`, `scripts/csv_to_xlsx.py`, `scripts/xlsx_restructure.py`, raiz `LICENSE` | Nous Research; skill 1.1.0; SHA `ff2d02f998f9f9e45543eea30fb935f47e4504a7`; commit HEAD 12/10/2026 19:41:36 UTC (GitHub exibe 13/10 01:11:36 +05:30) | MIT declarada na skill e confirmada na licença da raiz; manter aviso. Scripts restantes e dependências não auditados integralmente. |
| [Hermes excel-author](https://github.com/NousResearch/hermes-agent/blob/ff2d02f998f9f9e45543eea30fb935f47e4504a7/optional-skills/finance/excel-author/SKILL.md) | Anthropic, adaptada por Nous Research; 1.0.0; mesmo SHA acima | Apache-2.0 declarada; origem financeira explicitada. Não herda permissão da skill proprietária `anthropics/skills/xlsx`. |
| [Anthropic xlsx-author](https://github.com/anthropics/financial-services/blob/574ed3624aebd0418c7e96cd101262f30210ab26/plugins/vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md), raiz `LICENSE` | Anthropic; SHA `574ed3624aebd0418c7e96cd101262f30210ab26`; data do commit não recuperada | Apache-2.0 confirmada na raiz. Avisos, arquivo NOTICE se houver e contexto dos componentes exigem revisão antes de copiar. |
| [Anthropic xlsx](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/xlsx/SKILL.md), `LICENSE.txt` | Anthropic PBC; SHA `dbd4588f9e1033efb41dad4bef2f7947c8993d44`; HEAD 09/10/2026 18:45:49 UTC | Proprietária/source-available. `LICENSE.txt` restringe reprodução, derivados e distribuição; não copiar texto, script ou pacote. Conhecimento técnico deve ser sustentado por documentação pública e formulação própria. |
| [DSL Builders spreadsheet](https://github.com/dsl-builders/spreadsheet-skill/blob/bab49493dd3742a3903c8717cee9ab6277937d29/SKILL.md) | DSL Builders; 1.0.0; SHA `bab49493dd3742a3903c8717cee9ab6277937d29`; HEAD 23/06/2026 14:35:56 UTC | Apache-2.0 no frontmatter; raiz consultada contém README/SKILL e não confirmou arquivo LICENSE. Permissão declarada, documentação legal insuficiente para recomendar cópia integral. |
| [theNeoAI spreadsheet-expert](https://github.com/theneoai/awesome-skills/blob/61fe4f2bb47d6b61505b1b78c2b8ae5fd1ca38dd/skills/tool/analytics/spreadsheet-expert/SKILL.md), `references/standards.md` | theNeoAI/Lucas Hsueh; 1.0.0; SHA `61fe4f2bb47d6b61505b1b78c2b8ae5fd1ca38dd`; HEAD 15/05/2026 23:42:31 UTC | MIT declarada no frontmatter; licença completa e recursos não confirmados. Amostra técnica apresenta erros e boilerplate; não usar como base. |
| OpenAI Spreadsheets local `C:/Users/renat/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.1007.11041/skills/spreadsheets/SKILL.md`, `workflows/create_workflows.md`, `workflows/edit_workflows.md` | OpenAI, pacote `26.1007.11041`; SHA256 do SKILL `B8290A0C6A18182DC1FBB9432AAE518A25BF5354978B7D4C60A834D0E79821AA`; data editorial não declarada | Referência local do produto; licença de redistribuição e SHA Git público não estabelecidos. Não copiar pacote ou pressupor `@oai/artifact-tool` no Studio. |

SHAs HEAD foram obtidos com `git ls-remote`, sem clone. Datas referem-se ao commit HEAD do repositório, não à última alteração individual da skill. A API pública GitHub retornou limite de requisições; arquivos principais consultados por raw e datas por página de commit. O financial-services foi lido em `main` imediatamente após obter o SHA HEAD; não houve download de snapshot integral.

### Candidatos descobertos que não entram na contagem

[skills.sh/openai/skills/spreadsheet](https://www.skills.sh/openai/skills/spreadsheet) apresenta uma versão antiga baseada em openpyxl. No HEAD público `49f948faa9258a0c61caceaf225e179651397431` (23/06/2026 02:36:12 UTC), os caminhos `skills/spreadsheet`, `.curated/spreadsheet` e `.curated/spreadsheets` não resolvem; a árvore `.curated` consultada não lista planilhas. A página do diretório é descoberta histórica, não confirmação de distribuição atual. Não substituir original por cópia de terceiros.

A busca também encontrou [OpenAI SharePoint spreadsheets](https://github.com/openai/plugins/blob/main/plugins/sharepoint/skills/sharepoint-spreadsheets/SKILL.md), mas o arquivo não resolveu no SHA público `0722921d5542fc593105c27bd52630babd8b8c2a`. Não foi lido integralmente no original atual e não é candidata avaliada. A conexão de nuvem não seria requisito padrão desta especialista.

## Matriz de componentes

| Fonte / componente | Contribuição | Decisão | Motivo para o Studio |
|---|---|---|---|
| Hermes xlsx / SKILL | Inventário de abas, fórmulas e valores; criação, edição, tabelas, validação, CSV | **Adaptar** | Abrange trabalho interno real com artefato editável. Separar inspeção, alteração localizada e criação; não impor um CLI para toda tarefa. |
| Hermes xlsx / `references/restructuring.md` | Mapa de objetos afetados por inserir/excluir linhas e colunas | **Aproveitar como conhecimento**, após conferência | Evita acreditar que mover células preserva todo o modelo; referência sob demanda em alterações estruturais. |
| Hermes xlsx / `xlsx_restructure.py` | Reescrita de referências A1 e relatório de mudanças | **Não copiar como está** | Limites declarados e discrepâncias estáticas abaixo; benefício potencial somente se corrigido e validado para casos suportados. |
| Hermes xlsx / `csv_to_xlsx.py` | Encoding/delimitador explícitos, tipos, cabeçalho, filtros e freeze panes | **Adaptar método; descartar inferência cega** | Importação brasileira exige tipos por coluna e códigos preservados. Um número aparente pode ser CPF, CEP, matrícula ou SKU. |
| Hermes excel-author / fórmulas, entradas e fontes | Modelo flexível, referências rastreáveis e verificações | **Adaptar para referência financeira** | Banco de investimento não representa toda planilha operacional. Comentário em cada entrada e `Checks` obrigatória sobrecarregam tarefas pequenas. |
| Anthropic financial xlsx-author / modo headless vs live | Escolha entre arquivo e sessão Excel disponível | **Aproveitar decisão** | Entregar arquivo editável como padrão; sessão conectada somente quando existir e fizer parte do pedido. Não inventar ferramentas Office. |
| Anthropic xlsx / pacote proprietário | Comparador de limites e exigência de preservação | **Descartar cópia** | Permissão de redistribuição ausente e restrições explícitas. As decisões técnicas ficam ancoradas em documentação primária. |
| OpenAI local / simplicidade e workflows | Prioridade pedido → template → domínio; preservação de estrutura; tipos; ausência versus zero | **Aproveitar como critérios próprios, sem copiar** | Evita workbook com abas, explicações e cenários que ninguém pediu; excelente contraste com arquitetura financeira universal. |
| OpenAI local / tooling, outputs e política de fórmulas | Artifact Tool, marcação de operação, convenções de saída do Codex | **Descartar do contrato Studio** | Infraestrutura de outro produto. Restrições como excluir LET/arrays não são lei universal de Excel. |
| DSL Builders / arquivo estruturado e query de confirmação | Verificar dados esperados depois de exportar | **Aproveitar princípio** | Verificação tem que inspecionar a entrega, não apenas existência do arquivo. JSON spec permanente só quando repetição traz benefício concreto. |
| DSL Builders / CLI-first Maven/jbx/jbang | Runtime de criação/consulta determinística | **Descartar como dependência padrão** | Exige ferramenta adicional e oferece edição limitada; openpyxl pode resolver pedidos mais diretamente. |
| theNeoAI / tabela de plataforma, tamanho e transformação | Reconhecer destino, tipos, operação e atualização | **Adaptar a pergunta material** | Informação útil quando não inferível do arquivo; sem interrogatório genérico. |
| theNeoAI / snippets e persona | Fórmulas modernas, automações e exemplos | **Descartar como base técnica** | Há inconsistências: exemplo Excel com DIVIDE (função DAX), suposta redução de INDIRECT mantém dois INDIRECT; regra universal IFERROR mascara falhas. Claims de casos/percentuais não têm prova. |

## Lacunas e conflitos que mudam a execução

### Preservação não é apenas salvar como XLSX

Inserir uma coluna pelo openpyxl não atualiza automaticamente todas as fórmulas, tabelas e gráficos. `move_range(..., translate=True)` traduz fórmulas movidas, mas não as referências externas ao bloco ou nomes definidos. Isso é limitação documentada, não defeito imaginado. [Documentação primária de alterações estruturais](https://openpyxl.readthedocs.io/en/stable/editing_worksheets.html).

No auxiliar Hermes lido, a exclusão total de uma faixa de validação produz `parts=[]`, mas o bloco só modifica `sqref` quando há partes; a validação antiga pode ficar. A exclusão total de uma tabela produz `new=None`, mas o bloco só atualiza quando `new` é verdadeiro; a tabela antiga pode permanecer. Esses caminhos contradizem a expectativa de remoção completa do objeto. O script abre com `load_workbook(args.file)` sem `keep_vba`; portanto não oferece prova de preservação `.xlsm`. Trata-se de análise estática, sem execução.

A referência Hermes admite limites para gráficos, desenhos, regras de formato condicional e nomes complexos. O SKILL generaliza que openpyxl descarta gráficos ao carregar/salvar; a documentação oficial é mais específica: não lê todos os itens, pode perder shapes, e cópia de worksheet não copia imagens/gráficos. Evitar a regra falsa “todo gráfico sempre some”; verificar o recurso real e a operação. [Tutorial e flags oficiais](https://openpyxl.readthedocs.io/en/stable/tutorial.html).

Consequência: inspeção inicial lista abas, fórmulas, nomes, tabelas, validações, filtros, proteção, macros, links e objetos relevantes. Edição estreita respeita o modelo. Reestruturação escolhe ferramenta conforme os objetos presentes e verifica dependências afetadas; não remonta o arquivo inteiro por conveniência.

### Tipos e limpeza precisam de significado

O conversor Hermes tenta `int` antes de `float`, data e texto para cada célula. Assim `00123` vira `123`; colunas podem ficar com tipos misturados e decimais brasileiros como `12,5` ficam texto. Seu `--no-infer` preserva texto, mas também impede tipos úteis. São efeitos dedutíveis do código, sem teste executado.

Recomendação própria: definir o tipo por coluna conforme cabeçalho, fonte, exemplos e finalidade. Preservar identificadores como texto; números e percentuais como valores numéricos; datas como datas somente quando a interpretação é segura. Distinguir branco, zero e indisponível. Confirmar separador decimal, encoding e delimitador quando ambíguos. Limpeza de duplicatas precisa de chave e regra de conservação; não apagar linhas só porque duas células coincidem. Reconciliação inclui registros e totais antes/depois e resumo das transformações significativas. Não impor aba Raw/Clean/Analysis/Model/Output quando duas áreas bastam.

### Validação de entrada e validação da entrega são coisas diferentes

Dropdown, faixa numérica e data mínima ajudam quem preencherá o arquivo; não demonstram que os dados já presentes são válidos. openpyxl escreve validações, mas não as executa. Validação sem range não é salva; `showDropDown=True` pode esconder a seta no Excel/LibreOffice. [Documentação primária de validações](https://openpyxl.readthedocs.io/en/stable/validation.html).

Oferecer campos editáveis claros e regras úteis ao fluxo. Conferir valores existentes e fórmulas independentemente. Proteção de folha evita edição acidental; não é criptografia nem controle de acesso.

### Fórmula moderna versus compatibilidade

theNeoAI privilegia XLOOKUP, LET e arrays; o pacote OpenAI local restringe a introdução de várias dessas construções, enquanto a Anthropic explica limites do seu LibreOffice específico. Não combinar proibições e preferências como se todas fossem universais. Destino, versão, engine de recálculo e função solicitada determinam escolha. Preservar fórmulas válidas de um template; usar alternativas simples quando a engine disponível não suporta o recurso. Uma proibição de runtime antigo não comprova incapacidade de um Excel atual.

Fórmulas devem expressar cálculos que a pessoa continuará alterando. Transformações fixas de importação podem ocorrer fora do workbook quando essa é a entrega correta; não converter toda limpeza em fórmula. Evitar calcular totais em Python e colar como valores quando o usuário precisa que mudem com as entradas. Dar tratamento específico a chave ausente e denominador zero; não envolver todas as fórmulas em `IFERROR(...,0)` e esconder referências quebradas.

### Arquivo editável versus conclusão

Reconhecer automaticamente a intenção: “organize este controle de férias”, “arrume os cálculos desta planilha”, “monte o orçamento” e “converta o CSV” devem produzir ou alterar planilha quando ela é o objeto do trabalho. Planilhas garante células, tipos, fórmulas e uso cotidiano; Dados conduz investigação e conclusão; Apresentações prepara a comunicação HTML. Colaboração pode ocorrer quando a tarefa pede ambas, mas uma análise em prosa ou HTML não substitui o workbook solicitado.

CSV serve a transferência de uma tabela; não carrega múltiplas abas, fórmulas, estilos e controles como um workbook. `.xlsx` é o padrão de novo arquivo editável quando o pedido exige esses recursos. Preservar `.xlsm` quando necessário e suportado; `.xls`, `.ods`, Sheets e sessões Excel requerem avaliação específica. Não prometer round-trip perfeito por simplesmente trocar a extensão.

## Proposta de núcleo e recursos sob demanda

**Núcleo conciso:** reconhecer arquivo como entrega; aproveitar contexto/template; perguntar só o que muda a solução; inspecionar antes de editar; criar a estrutura mais simples útil; preservar tipos e origem; usar fórmulas para cálculos editáveis; manter entradas e exceções visíveis; conferir valores, dependências e comportamento; entregar link para arquivo com orientação breve de uso e limites reais.

**Referências sob demanda:** importação/limpeza brasileira; edição e preservação; fórmulas por engine/plataforma; tabelas, dropdowns e formulários; modelos financeiros; gráficos/impressão; recálculo/QA; grande volume e atualização recorrente. Instruções técnicas, APIs e exemplos extensos ficam nelas. Uma tabela de tarefas pode selecionar a referência sem exigir um “modo” ao usuário.

**Scripts:** nenhum é obrigatório só porque outras skills os incluem. Um auxiliar pequeno de inventário/verificação pode ser útil se evitar repetição e perda concreta, mas helpers de reestruturação exigem testes de referências, nomes, tabelas e validação. Não transportar os scripts Hermes sem corrigir os caminhos demonstrados nem gerar um framework/spec engine universal.

**Dependências para não desenvolvedores:** confirmar o ambiente disponível no pedido real. Se faltar biblioteca: explicar “Para criar e manter as fórmulas desse arquivo preciso de uma biblioteca de planilhas. Posso instalar o necessário neste ambiente?”; recálculo pode exigir um aplicativo compatível. Diferenciar oferecer instalação de mandar a pessoa rodar comandos. Ausência de engine não vira resultado “fórmulas funcionando” sem prova. Uma alternativa útil pode ser oferecida, informando o que muda; não substituir silenciosamente a entrega.

**Auto-adaptação:** quando um pedido revelar uma convenção repetida e útil, oferecer incorporar ao especialista o padrão de colunas, períodos, fontes ou forma de preencher. Não armazenar dados sensíveis ou alterar a skill automaticamente sem o pedido adequado. No trabalho pontual, apenas adaptar a entrega.

## Limites e critério de parada

As dúvidas desta frente foram resolvidas: existe fonte geral pública relevante; há método financeiro reaproveitável sob licença distinta; tipos/limpeza exigem adaptações reais; preservação e edição estrutural demandam verificação específica; o runtime Codex não é contrato do Studio. Não ampliar a busca por mais wrappers de openpyxl sem uma lacuna concreta.

Permanecem para a síntese e criação posteriores: escolha/validação de engine no Studio; licença completa de recursos eventualmente copiados; teste real de preservação e fórmulas; contrato de QA/recálculo detalhado pela frente correspondente. Nenhum destes foi declarado executado. O dossiê é pesquisa e proposta, não certificado de compatibilidade de pacotes.
