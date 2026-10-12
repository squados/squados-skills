# Assistente Financeiro — contas a receber e conciliação

Pesquisa da rodada 18/33, consultada em 12/10/2026. Esta frente cobre saldo aberto, aging, pagamentos parciais, conciliação de recebimentos e preparação **interna** de cobranças. Não cria a skill, não instala nem executa os pacotes, não acessa contas, não envia mensagens e não faz baixas ou lançamentos. A proposta abaixo é autoral; leitura de código não comprova execução nem segurança do pacote inteiro.

## Decisão principal

Aproveitar o fluxo curto de `ar-collections` e `payment-reconciliation` da família JustPaid/Loopfour; incorporar os controles de aging do AdoptAI e a unicidade de correspondência do `fcs-reconcile`; adaptar o snapshot e o brief factual do Paidnice/Denymbird. Nenhum pacote selecionado atende integralmente ao destino sem adaptação. O resultado deve começar pela resposta e pelo saldo que os materiais sustentam, com exceções rastreáveis, sem transformar arquivos incompletos em dívida confirmada.

O melhor eixo é **documento → saldo na data de corte → evidência de recebimento → alocação demonstrada → pendências internas**. Aging e cobrança vêm depois da leitura correta do saldo. Pagamento informado pelo cliente, comprovante, crédito no extrato e baixa no controle são evidências diferentes.

## Alcance, descoberta e deduplicação

Busca em português e inglês por `accounts receivable`, `AR aging`, `payment reconciliation`, `partial payments`, `collections`, `bank-rec` e `SKILL.md`, em resultados públicos e repositórios originais. Diretórios e índices serviram à descoberta; decisões abaixo se apoiam nos arquivos originais, consultados por HTTP em revisão fixa. Nenhum clone, temporário, download de binário ou execução foi necessário.

Foram aprofundadas **seis skills de trabalho, em quatro famílias independentes**: uma Paidnice, duas AdoptAI, duas JustPaid/Loopfour e uma cxtx. Também foram lidos integralmente um loader de AR e seu loader auxiliar do Well, e o `payment-reconciliation` duplicado de harshith-vaddiparthy para comparação: **nove SKILL.md integrais ao todo**, contando auxiliares e duplicata. Estes não representam nove métodos independentes.

Triagem adicional: `legioncodeinc/littlebird-skills/invoice-chaser`, `gokulsvision/crewm8-cfo-skills`, `erphq/skills`, `JoelLewis/finance_skills`, `dtsong/accounting-skills`, `megandmartin/agent-skills-repo` e `nroze22/reconcile-payments`. Não se afirma análise integral desses pacotes. O Littlebird exige plano/conector e tem AGPL; o pacote JoelLewis encontrado trata conciliação de custódia de investimentos; outros acrescentariam conectores ou repetição sem resolver a lacuna principal. O nome `ar-advisory` apareceu apenas como hipótese inicial de descoberta e não foi confirmado: não conta como fonte.

`loopfour/finance-skills` e `harshith-vaddiparthy/finance-skills` têm `payment-reconciliation/SKILL.md` **byte a byte igual** nas revisões abaixo. A API não marca Loopfour como fork; igualdade de arquivo comprova duplicação de conteúdo, não uma direção genealógica que não foi investigada. Contar como uma família. Os dossiês anteriores de CFO/Planilhas e fontes das outras frentes podem orientar a consolidação, mas não são novas leituras nem evidências independentes desta frente.

## Proveniência verificável

Datas abaixo são as datas de commit da revisão consultada, não datas presumidas de publicação da skill. O copyright identifica o titular declarado; o dono do repositório não substitui essa autoria.

| Família / pacote | Revisão, data UTC | Autoria e licença lida | Arquivos e alcance |
|---|---|---|---|
| [Denymbird/accounts-receivable-skills](https://github.com/Denymbird/accounts-receivable-skills/tree/baa270e109ed979ed67d715dbf23796a7b3c659f) | `baa270e109ed979ed67d715dbf23796a7b3c659f`; 23/09/2026 23:38:40 | LICENSE: Copyright 2026 Paidnice; MIT | `skills/accounts-receivable/SKILL.md` integral; refs `getting-data.md`, `late-fee-policy.md`, `tone-ladder.md` integrais; `scripts/ar.py`: parser/normalização, snapshot, aging, DSO, juros, prioridade, briefs, statements e CLI inspecionados; LICENSE integral |
| [adoptai/cpa-skills](https://github.com/adoptai/cpa-skills/tree/b6dd2b1b480eea0fb40817f2362ab0989a41ac97) | `b6dd2b1b480eea0fb40817f2362ab0989a41ac97`; 23/09/2026 05:59:16; branch padrão consultada `dev` | LICENSE: Copyright 2026 AdoptAI; MIT | `skills/ar-aging-tie-out/SKILL.md` e `skills/bank-rec-to-gl/SKILL.md` integrais; `ar_aging.py`: leitura, datas, recomposição, créditos, posteriores e gates; `reconcile.py`: parser, seis passes, classificação, saldos e main. Formatação das abas não foi auditada integralmente; LICENSE integral |
| [loopfour/finance-skills](https://github.com/loopfour/finance-skills/tree/6f02e8a0ac9f306a6d2d20bc3d9b7c8aec6f6065) | `6f02e8a0ac9f306a6d2d20bc3d9b7c8aec6f6065`; 06/05/2026 20:36:56 | Projeto JustPaid/Loopfour; LICENSE Copyright 2026 Loopfour; MIT | `skills/ar-collections/SKILL.md` e `skills/payment-reconciliation/SKILL.md` integrais; pacotes são playbooks de texto; LICENSE integral |
| [cxtx/finance-copilot-skills](https://github.com/cxtx/finance-copilot-skills/tree/f501f033c2ad517a7140e993e9ef3ab66c131bbf) | `f501f033c2ad517a7140e993e9ef3ab66c131bbf`; 11/08/2026 03:12:00 | LICENSE Copyright 2026 cxtx; MIT; SKILL declara v0.3.0 Preview | `skills/fcs-reconcile/SKILL.md`, refs `matching-rules.md` e `field-glossary.md`, scripts `matcher.py`, `normalizer.py`, `config.py`, `integrity.py`, `summary.py`, `classifier.py`, `guard.py`, contrato `docs/contracts/fcs-reconcile/input-contract.md`, dois testes (`test_matcher_invariant.py`, `test_e2e_golden.py`), requirements e LICENSE lidos; outros módulos não auditados |
| [WellApp-ai/skills](https://github.com/WellApp-ai/skills/tree/72b879d5aab908e4600c91789d1867435de7d6d8) | `72b879d5aab908e4600c91789d1867435de7d6d8`; 12/10/2026 15:36:37 | Well App, Inc.; PolyForm Perimeter 1.0.0, LICENSE integral; API retorna NOASSERTION, que não significa ausência de licença | `skills/accounts-receivable-aging/SKILL.md` e `skills/accounting-settings/SKILL.md` integrais. São loaders de instruções remotas: implementação real não foi obtida |
| [harshith-vaddiparthy/finance-skills](https://github.com/harshith-vaddiparthy/finance-skills/tree/054e33572df3470e8bdb9851c6e70d43ba054835) | `054e33572df3470e8bdb9851c6e70d43ba054835`; 03/05/2026 00:00:44 | API indica MIT; não se usou essa indicação como leitura de licença de nova fonte | `skills/payment-reconciliation/SKILL.md` integral, somente para verificar duplicação com Loopfour |

Links de arquivo decisivos: [Paidnice AR](https://github.com/Denymbird/accounts-receivable-skills/blob/baa270e109ed979ed67d715dbf23796a7b3c659f/skills/accounts-receivable/SKILL.md), [script AR](https://github.com/Denymbird/accounts-receivable-skills/blob/baa270e109ed979ed67d715dbf23796a7b3c659f/skills/accounts-receivable/scripts/ar.py), [AdoptAI aging](https://github.com/adoptai/cpa-skills/blob/b6dd2b1b480eea0fb40817f2362ab0989a41ac97/skills/ar-aging-tie-out/scripts/ar_aging.py), [AdoptAI conciliação](https://github.com/adoptai/cpa-skills/blob/b6dd2b1b480eea0fb40817f2362ab0989a41ac97/skills/bank-rec-to-gl/scripts/reconcile.py), [cxtx matcher](https://github.com/cxtx/finance-copilot-skills/blob/f501f033c2ad517a7140e993e9ef3ab66c131bbf/skills/fcs-reconcile/scripts/matcher.py), [cxtx config](https://github.com/cxtx/finance-copilot-skills/blob/f501f033c2ad517a7140e993e9ef3ab66c131bbf/skills/fcs-reconcile/scripts/config.py).

## Comparação por componente

| Fonte / arquivo → componente | Decisão | Contribuição e adaptação necessária |
|---|---|---|
| Loopfour `ar-collections/SKILL.md` → separar cobrança de saneamento | **Adotar** | Créditos não aplicados, duplicidade, disputa e pagamento não alocado ficam em pendências administrativas; não entram automaticamente numa lista de inadimplentes |
| Loopfour AR → prioridade com evidência e responsável | **Adaptar** | Ordenar por saldo, atraso e bloqueio concreto; registrar responsável quando fornecido. Saúde, renovação e churn não são obrigatórios; não impor lógica SaaS nem escalada executiva |
| Loopfour `payment-reconciliation/SKILL.md` → trilha pagamento/documento | **Adotar** | Preservar IDs/arquivos, usar referência e remessa antes de semelhança; separar parcial, excesso, tarifas, estorno e crédito sem alocação; ação contábil fica em proposta interna |
| Loopfour conciliação → confiança exact/strong/probable/weak | **Adaptar** | Apresentar base objetiva e candidatos, sem fabricar probabilidade. Nome/data/valor semelhantes ajudam a investigar; não autorizam baixa |
| Paidnice `ar.py` → Decimal e corte estável | **Adaptar** | Reproduzir aritmética determinística e declarar corte/origem. Snapshot não é prova de cobertura nem histórico reconstruído; é preciso conservar linha original, IDs e saldo referente ao corte |
| Paidnice `getting-data.md` → CSV local como entrada suficiente | **Adotar** | Começar pelo arquivo que já existe, sem pedir cadastro, chave ou integração. Instruções específicas Xero/QBO só ajudam quando esse é o sistema real |
| Paidnice `cmd_briefs` → fatos exatos para rascunho | **Adaptar** | Documento, vencimento e saldo rastreáveis em texto curto; não inserir o tom coercivo da tabela. Rascunho solicitado é entrega interna e não exige confirmação prévia de cada linha se incertezas estiverem explícitas |
| Paidnice `late-fee-policy.md`, `tone-ladder.md`, CLI → taxas padrão e escalada por idade | **Descartar** | Rate default 2%, pisos exemplificativos, ameaça de suspensão/referral e promoção Paidnice não são política do usuário. Sem encargos inventados, coerção, cobrança externa ou contratação de SaaS |
| AdoptAI `ar-aging-tie-out/SKILL.md` → total e faixas independentes | **Adotar** | Recalcular faixas; mostrar bruto devedor, créditos e líquido; validar corte, duplicidade e datas incoerentes; igualdade do total com o razão não comprova todas as linhas |
| AdoptAI `ar_aging.py` → aging por emissão e dias após prazo | **Adaptar** | Para cobrança, envelhecer **saldo remanescente por vencimento**; para outra análise, idade desde emissão com rótulo explícito. Não chamar faixa correta por vencimento de errada só porque o código usa emissão |
| AdoptAI aging → allowance, related parties e US unclaimed property | **Descartar do núcleo** | São análises contábeis/jurisdicionais específicas; podem orientar investigação solicitada, não checklist universal nem conclusão de perda esperada |
| AdoptAI `bank-rec-to-gl/SKILL.md` → diferença sem ajuste artificial | **Adotar** | Não fabricar item para zerar diferença. Mostrar saldo de cada fonte, itens pendentes, causa quando comprovada e valor não explicado |
| AdoptAI `reconcile.py` → seis passes e agregações | **Adaptar** | Ordem por evidência é útil; busca primeiro candidato/mais próximo e primeiro subconjunto não garante unicidade. Correspondências ambíguas ficam propostas; agrupamento depende de remessa/lote identificável |
| cxtx `matcher.py` e `config.py` → unicidade recíproca | **Adotar** | Chave única dos dois lados + valor igual; se múltiplos candidatos, registrar conflito. Config exige `amount` em chave composta; não simplificar removendo essa proteção |
| cxtx `matching-rules.md` → diferença dentro de tolerância | **Adotar** | Tolerância monetária classifica diferença, não apaga centavos nem transforma diferença em liquidação |
| cxtx `field-glossary.md`, `normalizer.py` → IDs e número longo | **Adaptar** | Conservar zeros à esquerda e valor original; alertar número já danificado, sem “reparação” imaginada. Conversão de vírgula/decimal e direção precisa PT-BR e contexto do arquivo |
| cxtx `integrity.py`, `summary.py` → preservação e cobertura | **Adaptar** | Não sobrescrever entrada; contabilizar destino de cada linha. Hash é útil em lotes/reexecuções, dispensável como ritual em pedido pequeno. Identidade interna de soma não prova completude contra um extrato independente |
| cxtx SKILL → confirmação de modo, YAML e instruções ao operador | **Descartar da experiência padrão** | A intenção é reconhecida do pedido. O usuário não escolhe “modo”, nem edita configuração técnica. Perguntar somente lacuna que altera o resultado |
| cxtx → proibição de detalhe no modelo e “zero erro” | **Não prometer** | A pesquisa leu estrutura, não uma prova de isolamento do Studio. Monkeypatch de socket no processo não é isolamento de SO, e unicidade não garante que a origem é verdadeira |
| Well loaders → contexto de moeda/identidade | **Referência de descoberta somente** | Loader depende de Well/MCP e instruções remotas; PolyForm tem restrição concorrencial. Não copiar como base aberta, não conectar para a pesquisa, não afirmar conteúdo remoto analisado |

## O que o código muda no julgamento

### Paidnice: texto mais forte que a implementação

`SKILL.md` manda separar moedas; `cmd_snapshot`, `cmd_aging`, `cmd_priority`, `cmd_briefs` e `cmd_statement` somam saldos sem agrupar por moeda. O snapshot conserva `currency`, mas as agregações não a usam. Adaptação precisa impedir total BRL+USD, inclusive dentro do mesmo cliente.

`normalize` usa total como saldo quando `amount_due` falta; um status de quitação ou `paid_date` pode levar a saldo zero. Registra exceção, mas o número assumido continua nas análises. Para o destino, “saldo não informado” permanece lacuna, sobretudo em parcial. A escolha `dmy` quando todas as datas são ambíguas é implícita; registrar convenção inferida e perguntar quando as duas leituras alteram vencimento/corte.

`cmd_snapshot` elimina duplicatas por `(customer, number)`, mantendo a primeira. Dois exports com snapshots diferentes, IDs de empresas distintas ou moedas diferentes podem colidir. Não apagar versão original; decidir duplicata real por identificador de origem/contexto, distinguir reapresentação de evento parcial. `cmd_dso` filtra emissão apenas pelo limite inferior, sem limite superior no corte; o total de faturas exportadas não é necessariamente receita a prazo completa. DSO fica sob demanda e sem conclusão quando o denominador não está coberto.

`cmd_priority` calcula pesos 50/30/20, usa valor absoluto do atraso histórico e bônus de promessa rompida: um cliente que paga cedo pode receber pontuação histórica inadequada. O CSV não modela disputas explicitamente. Descartar score e inferência automática de intenção; usar ordenação simples explicada. `cmd_statement --as-at` troca data exibida sem reconstruir saldo/cálculo naquela data. Não reproduzir esse recurso como posição histórica. O HTML interpola nomes e referências sem escape: reutilização exigiria escape de dados externos, não apenas aviso de prompt injection.

### AdoptAI: distinguir controle realizado e controle ausente

`ar_aging.py` calcula bucket por data de emissão. Isso pode ser uma convenção válida em um relatório específico, mas não substitui atraso por vencimento. A lógica `d0` converte ausência de valor em zero; `pdate` aceita formatos americanos, não data numérica brasileira explícita. Tratar ausência como problema de qualidade, não saldo zero.

`load_receipts` agrega `(customer, invoice_no)` sem filtrar `receipt_date > as_of`; data anterior ao corte pode aparecer como recebimento posterior. Qualquer valor maior que zero gera a descrição “collected after period end”, mesmo parcial. Deve validar janela e apresentar montante recebido, saldo remanescente e evidência, sem afirmar quitação integral.

Testes ausentes de saldo do razão, bucket original ou allowance são `skipped: True, passed: True`; `overall = all(passed)` pode produzir `TIED OUT` sem o controle do razão. Etapa não feita permanece **não verificada**. Uma análise útil pode ser entregue com escopo parcial, mas não como conciliação completa.

No `bank-rec-to-gl/reconcile.py`, a cascata escolhe primeira combinação disponível sem comprovar exclusividade. `build_rec` aceita `unidentified == 0` pelo total líquido: um crédito e débito desconhecidos podem cancelar numericamente e continuar desconhecidos. A função `main` registra erro de abertura+movimentação≠fechamento em `flags`, mas essas flags não invalidam `rec['reconciled']`; retorno zero e nome limpo não provam integridade dos dados. Preferir o método profissional descrito, sem adotar o script bruto. Não transferir regras americanas de cheques/stale/escheatment ao Brasil.

### cxtx: bom comparador, alcance limitado

O matcher evita reutilização de linha, desvia qualidade ruim e duplicatas, verifica unicidade nos dois lados e exige igualdade monetária; data pode ter tolerância configurada na chave composta. Portanto a referência que diz campos “todos iguais” precisa respeitar essa exceção explícita de data. Normalizador remove vírgula como milhares e reconhece direção em chinês; não está pronto para `1.234,56` ou etiquetas brasileiras.

É um comparador de **linhas 1:1**: não aloca vários pagamentos a uma fatura nem uma remessa a várias faturas. Um pagamento de 400 contra documento de 1.000 é uma diferença no comparador, não prova de erro nem baixa parcial automaticamente. A camada de saldo/alocação é conhecimento adicional necessário.

Os testes lidos verificam cada linha exatamente uma vez, contagens, igualdade de resumos e conteúdo de abas/manifestos. Isso é evidência de desenho de testes, **não resultado executado nesta pesquisa**. `summary.py` calcula somas dos próprios outcomes; a identidade monetária interna não substitui conferir abertura, encerramento e totais independentes. Também “match rate” usa número de outcomes como denominador: não o apresentar como proporção de valor recebido.

## Convenção profissional de estados e corte

A documentação primária [Odoo 19 — Payments](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments/online.html) distingue pagamento vinculado, crédito sem vínculo, parcial e conciliação com banco; a configuração pode mudar os estados. [Bank reconciliation](https://www.odoo.com/documentation/19.0/applications/finance/accounting/bank/reconciliation.html) mantém diferença aberta quando o pagamento é menor e saldo não alocado quando é maior. Essas distinções orientam o método; não são instruções para operar Odoo nem uma taxonomia universal de todos os ERPs.

| Fato encontrado | Interpretação permitida | Próximo trabalho interno |
|---|---|---|
| Documento emitido, com vencimento futuro | Saldo a vencer, se o saldo estiver sustentado | Agenda de vencimentos |
| Documento com data vencida e saldo aberto no controle | Vencido conforme essa fonte/corte | Verificar créditos e recebimentos antes do rascunho |
| Pessoa diz que pagou / envia comprovante | Pagamento alegado ou comprovante localizado | Procurar lançamento/crédito correspondente; não marcar baixa |
| Crédito identificado em extrato | Movimento de recebimento nesse extrato | Identificar cliente/documento/remessa e alocar |
| Pagamento parcialmente vinculado | Valor alocado + saldo remanescente | Aging do remanescente conforme vencimento original, salvo renegociação documentada |
| Mais dinheiro que saldo do documento | Crédito/excesso pendente de alocação | Conferir adiantamento, outro documento ou duplicidade; sem decidir estorno |
| Documento e recebimento ligados, saldo baixado no controle | Baixa conciliada conforme materiais revisados | Informar cobertura e data; nenhuma nova baixa realizada pelo assistente |
| Extrato incompleto / controle desatualizado | Posição parcial; ausência de movimento não prova ausência de pagamento | Pedir complemento material ou entregar pendência explícita |

O saldo no corte precisa refletir somente pagamentos/créditos aplicáveis até aquela data, sem usar saldo atual para afirmar passado. Pagamento posterior pode ser apresentado como evento posterior, sem mudar o atraso histórico. Uma nota de crédito não é necessariamente entrada de dinheiro. Cancelamento não vira recebimento. Promessa de pagamento não é pagamento realizado.

## Proposta para o núcleo da futura skill

O núcleo deve reconhecer o pedido e entregar a menor resposta útil. Se os materiais já trazem datas, moeda, empresa e período, usar esse contexto; perguntar somente o que muda saldo, identificação, corte, convenção de datas ou condição de cobrança.

1. **Entender a entrega:** posição de recebíveis, faixa de atraso, conciliação ou rascunho. Não pedir que a pessoa escolha um modo.
2. **Ler com rastreio:** preservar arquivos, IDs, número do documento como texto e linhas originais. Normalizar em coluna/camada separada; registrar convenção de data, moeda, unidade e sinais.
3. **Recompor o saldo quando possível:** valor do documento menos pagamentos e créditos demonstradamente aplicados, mais ajustes documentados; eventos sem vínculo ficam separados. Na ausência de cobertura, manter saldo da fonte rotulado ou lacuna, sem inventar.
4. **Conciliar por evidência:** referência/ID, remessa, cliente e valor. Correspondência exclusiva é forte; valores iguais e nomes parecidos sem vínculo são candidatos. Pagamentos em lote, parciais e taxas requerem decomposição demonstrável, sem dupla aplicação.
5. **Calcular a posição:** corte explícito, atraso pelo vencimento, saldo remanescente, faixas existentes na empresa ou faixas declaradas na entrega. Totais separados por moeda e entidade; fechar contagens/somas e listar exclusões.
6. **Entregar primeiro o resultado:** resumo curto, tabela de saldo/status/evidência, pendências com próximo passo. Rascunhos só quando pedidos, com valores/documentos rastreáveis e linguagem factual; preparação interna não vira envio, promessa ou ação realizada.

Não construir infraestrutura, watchers, conexão bancária, envio, cadastro em SaaS ou workflow jurídico. Não prometer bibliotecas instaladas. Se faltar dependência para um arquivo de saída solicitado, explicar em linguagem comum e oferecer instalação simples pelo agente, sem transformar o usuário em desenvolvedor; nesta rodada nenhuma instalação ocorre. Após uso recorrente, oferecer adaptar uma versão própria somente com aceite ou pedido; não reescrever a skill automaticamente após um único uso.

## Referências sob demanda e scripts

| Recurso proposto | Carregar quando | Conteúdo necessário |
|---|---|---|
| `references/receivables-and-aging.md` | Aging, saldo parcial ou corte histórico | Definições, vencimento vs emissão, crédito separado, pagamentos posteriores, cobertura e exemplos de faixas |
| `references/payment-reconciliation.md` | Extrato/controle, remessas ou diferença | Evidência/ambiguidade, alocação parcial e lote, tarifas comprovadas, excesso, estorno, identidade de controle |
| `references/internal-collection-drafts.md` | Pedido de preparação de cobrança | Fatos da dívida conforme fonte, pendências que suspendem conclusão, disputa, roteiro factual curto sem consequências inventadas |
| Template de tabela, se recorrência justificar | Entrega repetida com mesmo formato | Documento/cliente/ID, emissão, vencimento, moeda, valor original, saldo/corte, evidência de pagamento, alocado, remanescente e exceção |

Scripts têm benefício concreto em volumes maiores, repetição de faixas/saldos e controle de centavos. Não são requisito para redigir um único rascunho a partir de fatos claros. Uma eventual implementação pequena deve preferir o runtime já disponível, cálculo decimal ou centavos inteiros e entrada simples. Não incorporar os 929 linhas do AR Paidnice, o framework cxtx completo ou dependências de outros produtos apenas porque existem.

Uma adaptação real precisaria testar invariantes que importam: cada pagamento usado no máximo uma vez; somatório alocado não excede pagamento/documento sem crédito explícito; bruto, créditos e líquido separados; corte exclui futuro; recebimento parcial não zera saldo; ausência não vira zero; diferentes moedas não se somam; desconhecidos não desaparecem por compensação. Tais testes ainda não foram implementados.

## Exemplos autorais de aceitação futura

Exemplos sintéticos para desenho, sem execução nem dados reais:

- Documento BRL 1.000,00 vencido em 30/09; recebimento conciliável de 400,00 em 05/10; corte 12/10: saldo 600,00, atraso 12 dias, com IDs do evento. Comprovante isolado de 400,00 muda a evidência, mas não comprova baixa.
- Mesmos valores, corte 30/09: o recebimento de 05/10 é posterior; não reduzir saldo histórico para 600,00 sem suporte correspondente ao corte.
- Dois documentos de 500,00 e um crédito bancário de 500,00 sem referência: manter candidatos; não escolher o primeiro da planilha.
- Documento `000123` reaparece em dois exports: preservar ambos até verificar mesma origem e versão. Mesmo número em outra empresa não é duplicata.
- BRL 600,00 e USD 300,00: dois totais; câmbio somente quando solicitado e com taxa/data/fonte demonstradas.
- Crédito desconhecido +200,00 e débito desconhecido -200,00: diferença líquida zero, dois itens ainda não explicados.
- Documento em disputa ou recebimento não alocado: fila de conferência interna antes de rascunho que afirme inadimplência.

## Compatibilidade, licença e limite da entrega

MIT nas quatro famílias aprofundadas permite avaliar adaptação com preservação de avisos se houver cópia substancial. Esta pesquisa não copia código nem distribui pacotes. PolyForm Perimeter do Well não é licença aberta sem restrição concorrencial; AGPL do Littlebird exige análise própria antes de eventual reutilização, que não ocorreu.

Nenhum desses repositórios externos está automaticamente habilitado como origem `github` na galeria atual. `fcs-reconcile` ainda referencia docs fora da pasta, inclui `requirements.txt`, `agents/`, `examples/`, `tests/` e exemplos XLSX: não pode ser tratado como pacote pronto para o adaptador do Studio. Paidnice requer Python; AdoptAI requer `openpyxl` (o SKILL bancário cita pandas, enquanto o script lido importa somente openpyxl); cxtx tem pandas/openpyxl/PyYAML e locks. Ambiente, instalação, compatibilidade Windows, guard do Hermes e execução real permanecem não verificados.

A pesquisa termina por suficiência: estão resolvidas as decisões sobre saldo parcial, aging, moeda, unicidade, rastreio e limites de rascunhos. Permanecem para a criação/validação posterior a estrutura do pacote próprio, eventual cálculo automatizado, testes com arquivos sintéticos e prova em pedido real. Não houve nova pesquisa legal porque não se recomenda encargo, sanção ou medida de cobrança; se um pedido futuro exigir esse cálculo, contrato e regra primária aplicável devem ser verificados naquele contexto, sem aviso jurídico universal.
