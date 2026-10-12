# Assistente Financeiro — métodos e casos de referência

Pesquisa da rodada 18/33, consultada em 12/10/2026. Escopo: rotina interna de documentos, contas a pagar/receber, vencimentos, saldos, aging, conciliação e rascunhos de mensagens. A comparação de skills existentes pertence às outras frentes da pesquisa. Este arquivo registra métodos profissionais para julgar seus componentes; não cria pacote executável, não instala ferramentas e não realiza operações financeiras.

## Resultado da pesquisa

Recomenda-se uma assistente que organiza o pedido recebido, preserva o vínculo entre documento, título, parcela e evidência de pagamento e entrega uma lista útil com pendências concretas. Pode começar com arquivos e informação da equipe. Extrato é necessário quando a entrega depende de comprovar movimentação ou conciliação, não para toda organização de documentos. Nenhum saldo sem fonte/data deve parecer posição bancária atual.

A principal contribuição profissional é separar eventos que um texto informal tende a misturar: emissão de fatura, valor exigível, pagamento informado, comprovante, crédito identificado, baixa registrada e conciliação. ERP diferentes implementam esses eventos de maneiras diferentes; a skill deve explicar o estado observado e sua evidência, sem transportar menus, permissões ou regras de um fornecedor como regra universal.

## Fontes primárias e decisões por componente

Todas as URLs abaixo são públicas e gratuitas para leitura. Uso do ERP pode exigir licença/conta; a pesquisa não contratou nem acessou ERP. Material público não implica licença para redistribuição: a contribuição é síntese autoral, sem copiar cursos, manuais ou templates.

| Fonte, autoria, data e acesso real | Componente útil | Decisão e motivo | Limite |
|---|---|---|---|
| [Vendor invoices overview](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-invoices-overview), Microsoft Learn; atualização visível 06/05/2026; artigo consultado | Diferenças entre documento, registro, aprovação e lançamento; divergência de total; possível número repetido; relatório de títulos abertos com data de corte | **Adaptar:** procurar duplicação e incompatibilidades antes de somar obrigações; manter IDs, fornecedor e parcela. Pedido/recebimento ajudam quando já existem no trabalho | Controles do Dynamics dependem de configuração. Mesmo número ou valor, isoladamente, não prova duplicação. Serviços recorrentes podem existir sem pedido de compra |
| [Customer aging report](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-aging), Microsoft Learn; data não exibida na extração; artigo consultado em 12/10/2026 | Distingue data do saldo, data usada no aging e critério temporal; apresenta pagamentos ainda não liquidados separadamente | **Adotar conceito/adaptar formato:** declarar base do saldo e vencimento como critério padrão quando o pedido é atraso; usar somente saldo residual nas faixas | Não tratar todas as datas como equivalentes; preservar moeda. Banner de autorização apareceu, mas corpo do artigo estava legível publicamente; nenhum login realizado |
| [Como fazer baixa parcial](https://ajuda.contaazul.com/hc/pt-br/articles/7184294182797-Lan%C3%A7amentos-financeiros-como-fazer-baixa-parcial), Conta Azul; 11/06/2026; artigo consultado | Pagamento/recebimento abaixo do total deixa saldo restante; detalhe do título e movimentos podem mostrar estados distintos | **Adotar:** pagamentos parciais reduzem apenas a parcela efetivamente identificada. **Adaptar:** preservar evidência e estado, inclusive baixa informada sem conciliação | Documentação do produto; não autoriza executar baixas e não prova que uma alegação ou screenshot confirma crédito |
| [Várias movimentações do banco com um lançamento](https://ajuda.contaazul.com/hc/pt-br/articles/7454101596429-Concilia%C3%A7%C3%A3o-v%C3%A1rias-movimenta%C3%A7%C3%B5es-do-banco-com-um-lan%C3%A7amento), Conta Azul; 30/04/2026; artigo consultado | Pagamento fracionado, principal/encargos e relações entre movimentos e título | **Adaptar:** permitir relação N:1 e preservar datas/IDs das partes; apresentar diferença e explicação documentada | **Descartar como instrução geral:** criar ajuste só para zerar diferença. Tarifa/desconto exige causa/evidência; uma diferença desconhecida permanece pendente |
| [Perguntas frequentes: conciliação bancária](https://ajuda.omie.com.br/pt-BR/articles/6812438-perguntas-frequentes-conciliacao-bancaria), Danilo Nascimento / Omie; índice informa 11/09/2026, página mostra atualização relativa; artigo consultado | Arquivo do extrato pode faltar movimento; data de débito difere da data de pagamento; baixa e conciliação têm situações distintas; agrupamentos alteram apresentação | **Adotar:** explicitar completude do período e distinguir datas/estados; consultar particularidade do ERP sob demanda | Texto diz não aceitar N:1 direto e oferece associação de baixas parciais. Não universalizar essa limitação, nem seguir atalhos de ignorar/criar movimentos para fechar saldo |
| [Payments — Odoo 19](https://www.odoo.com/documentation/19.0/applications/finance/accounting/payments/online.html), Odoo; versão 19.0, data editorial não visível; conteúdo indexado consultado, abertura direta falhou | Crédito/pagamento não vinculado pode existir sem quitar uma fatura; registro e conciliação têm etapas diferentes | **Adaptar:** manter crédito sem identificação/vínculo em linha própria; não escolher título só porque o valor combina | Estados dependem das contas de compensação configuradas no Odoo. A leitura foi do corpo indexado; não se confirmou interface nem funcionamento |
| [Bank reconciliation — Odoo 19](https://www.odoo.com/documentation/19.0/applications/finance/accounting/bank/reconciliation.html), Odoo; versão 19.0; data editorial não visível; trecho indexado consultado, abertura direta retornou timeout | Relaciona movimento com contrapartida e preserva transação com data, rótulo, parceiro e valor | **Adaptar:** confrontar movimentos com registros existentes e listar não correspondidos | Não adotar afirmação genérica de obrigatoriedade ou modelos automáticos como rito universal; conteúdo acessado parcialmente |

### Vídeo original recente e nível de evidência

[Bank reconciliation | Odoo Accounting](https://www.youtube.com/watch?v=P8EItiKqm5k), canal oficial **Odoo**, publicado em **18/03/2026**. A pesquisa consultou página indexada, descrição e capítulos: **00:31** lançamentos de transação; **01:55** visão de transações; **03:34** exemplos de conciliação; **06:50** editar e desfazer conciliação. O vídeo é referência gratuita original de 2026. Abertura direta falhou; **não foi assistido e não foi obtida transcrição**. Os timestamps são os capítulos publicados, não evidência de que um procedimento foi observado. Aproveitar como recurso de aprofundamento de ERP; não fundamentar uma técnica nova apenas no título/descrição.

A busca também encontrou vídeo de Hussien Soliman, 09/10/2025, sobre funcionalidades Odoo 19, mas a fonte oficial já atende à descoberta audiovisual. Não foi selecionado nem assistido. Não se buscou quantidade de vídeos: os artigos brasileiros recentes e os contratos de dados resolvem as dúvidas de método; demonstração audiovisual continua não verificada.

## Síntese autoral para a execução

1. **Entender a entrega pelo pedido.** “Organize esses boletos” permite organizar títulos e vencimentos; “quem está atrasado?” pede saldo residual e aging; “o saldo está certo?” pede confronto das bases. Aproveitar moeda, período, fonte e dados presentes. Perguntar somente quando uma lacuna muda resultado material, como data de corte ou qual parcela recebeu um crédito sem vínculo.
2. **Extrair preservando a origem.** Por título, conservar identificador, contraparte, documento, parcela, moeda, valor original, vencimento, baixas identificadas, saldo, estado e referência ao arquivo/linha. Não exigir todas as colunas em uma entrega simples. Campo desconhecido permanece desconhecido; OCR duvidoso é explicitado.
3. **Separar documento repetido de obrigação repetida.** Segunda via/PDF e boleto da mesma parcela podem representar o mesmo título. Dois títulos com valores iguais ou parcelas distintas podem ser legítimos. Agrupar evidências do mesmo título sem apagar documentos; marcar suspeitas que não puderem ser resolvidas. Não excluir obrigação só por semelhança de texto ou valor.
4. **Calcular na base declarada.** Saldo por título = original menos pagamentos/créditos efetivamente vinculados, mais encargos menos abatimentos autorizados/documentados. Sem vínculo, pagamento fica separado. Usar precisão decimal ou centavos inteiros; não arredondar cada soma informalmente. Total original, recebido e em aberto têm denominadores distintos.
5. **Organizar prazo sem inventar atraso.** Informar data do saldo e critério do aging. Por padrão de trabalho, vencido significa vencimento anterior à data de corte; vence hoje fica separado. Faixas usuais 1–30, 31–60, 61–90 e >90 são uma convenção adaptável, não lei. Título sem vencimento fica “vencimento não informado”. Não alterar vencimento após parcial sem renegociação documentada.
6. **Confrontar quando pedido.** Conferir saldo inicial, movimentos, saldo final, conta/moeda e período. Relacionar movimento e título com IDs, contraparte e evidência; valor igual sozinho não basta. Mostrar diferenças, possíveis causas e próxima verificação. “Bateu o saldo total” não prova que todos os títulos estão certos.
7. **Entregar algo acionável.** Uma tabela/lista com próximos vencimentos, saldos, documentos faltantes, pagamentos informados não confirmados e responsáveis já conhecidos; ou rascunho respeitoso que menciona título, parcela e valor sustentado. Uma contestação pede apuração e separação do valor controvertido. Envio, alteração de registro, pagamento ou acesso a conta não são parte destes casos de pesquisa.

Juros, multa, feriados, descontos, retenções e renegociação só entram quando materialmente solicitados e documentados. Não existe taxa padrão inferida do título. Nenhuma regra legal é necessária para os três casos abaixo; eles não pretendem aplicar CDC, taxa legal ou regras de Pix.

### Organização proporcional da futura skill

Núcleo curto: compreender pedido, preservar origem/IDs, distinguir evidência/estado, calcular saldo e produzir entrega útil. Referências sob demanda: documentos/AP; AR e rascunhos; aging; conciliação/despesas; planilhas/precisão. Não carregar um manual de CFO, valuation, forecast ou fluxo de caixa estratégico em toda tarefa.

Script só é útil se reduzir erro/trabalho real, por exemplo consolidar muitos títulos e validar soma em centavos; não criar infraestrutura para estes três exemplos. Se falta ferramenta para ler determinado formato, explicar uma opção simples de instalação ou oferecer formato alternativo, com linguagem comum; não exigir que a pessoa rode comandos nem instalar por conta desta pesquisa. Quando preferência recorrente ou atrito concreto justificar, oferecer adaptar a própria skill, explicando mudança e benefício; aplicar após aceitação ou pedido direto.

## Três casos fictícios autorais e gabaritos

São **critérios futuros de aceitação**, não testes executados da skill. Pessoas, empresas, documentos e dados são fictícios. Valores em BRL; não há impostos, juros, multa ou desconto nos casos. Bases são fornecidas no enunciado para não inventar certeza.

### 1. AP — segunda via e pagamento não confirmado

Pedido: “Organize o que temos para pagar e os vencimentos; a equipe disse que já agendou um deles.” Corte em 12/10/2026, base: documentos recebidos e informações da equipe, sem confirmação bancária. As quatro obrigações abaixo estão em aberto no controle fornecido.

| Registro/documento | Título/parcela e fornecedor | Valor | Vencimento | Evidência |
|---|---|---:|---|---|
| boleto-a.pdf | AP-101, NF-880/1, Papelaria Aurora | 1.250,40 | 10/10/2026 | Boleto original |
| segunda-via-a.pdf | AP-101, NF-880/1, Papelaria Aurora | 1.250,40 | 10/10/2026 | Mesma referência, beneficiário e parcela; segunda via |
| contrato-b-p1.pdf | AP-102, contrato-72/1, Limpeza Horizonte | 980,35 | 14/10/2026 | Parcela 1 de 2 |
| contrato-b-p2.pdf | AP-103, contrato-72/2, Limpeza Horizonte | 980,35 | 14/11/2026 | Parcela 2 de 2 |
| fatura-c.pdf | AP-104, FAT-19/1, Oficina Cedro | 420,10 | 12/10/2026 | Fatura emitida; nenhum pagamento informado |

A equipe anexou a AP-101 uma tela escrita “agendado”, sem confirmação de execução. A base não informa saldo bancário.

**Gabarito:** 5 documentos de cobrança representam **4 títulos**, R$ **3.631,20** no controle. Soma bruta dos documentos R$ 4.881,60 superestima em R$ 1.250,40. Vencido segundo calendário: R$ 1.250,40, com pagamento **agendado informado/não confirmado**; vence hoje R$ 420,10; futuro R$ 1.960,70. Preservar as duas parcelas legítimas de R$ 980,35. Não marcar AP-101 pago, não repetir pagamento e não dizer que o total é saldo bancário ou desembolso autorizado. Próximo passo material: verificar execução/status antes de decidir o que ainda pagar; a organização documental já pode ser entregue.

Critérios futuros: mantém ambas as evidências da AP-101; não duplica obrigação; não elimina AP-103 pelo valor repetido; separa agenda de confirmação e “hoje” de atraso; apresenta soma e base corretamente.

### 2. AR — parcial, aging e valor contestado

Pedido: “Liste as pendências dos clientes e prepare mensagens para eu revisar.” Saldo e aging em 12/10/2026, por vencimento. O controle fornecido identifica uma baixa confirmada vinculada de R$ 900,25 em 25/09 à AR-201. O extrato também contém crédito de R$ 300,00 sem pagador/título identificado, ainda não alocado.

| Título/parcela e cliente | Original | Recebido vinculado | Vencimento | Observação |
|---|---:|---:|---|---|
| AR-201, FAT-501/1, Estúdio Ipê | 2.400,75 | 900,25 | 10/09/2026 | Pagamento parcial confirmado na base |
| AR-202, FAT-502/1, Ateliê Vento | 1.200,00 | 0,00 | 20/09/2026 | Cliente contesta integralmente a entrega; sem abatimento aprovado |
| AR-203, FAT-503/1, Café Luar | 500,20 | 0,00 | 15/10/2026 | Ainda não venceu |

**Gabarito:** AR-201 residual **R$ 1.500,50**, atraso **32 dias**, faixa 31–60. AR-202 **R$ 1.200,00**, **22 dias**, faixa 1–30, com contestação destacada. AR-203 **R$ 500,20** a vencer. Original total **R$ 4.100,95**; recebido vinculado **R$ 900,25**; aberto por títulos **R$ 3.200,70**; vencido por títulos **R$ 2.700,50**, sendo **R$ 1.200,00 contestado**. Crédito não alocado **R$ 300,00** em linha própria; não reduzir arbitrariamente AR-201, aging ou qualquer cliente. Não usar pagamento parcial para reiniciar vencimento.

Rascunho para Estúdio Ipê: “Olá! No nosso controle de 12/10, a FAT-501, parcela 1, tem R$ 1.500,50 em aberto após o recebimento de R$ 900,25. Vocês podem confirmar a previsão para o saldo? Se houver outro pagamento, podemos verificar os dados para atualizar o controle.”

Rascunho de apuração para Ateliê Vento: “Olá! Registramos a contestação da FAT-502, parcela 1, de R$ 1.200,00. Podemos conferir o ponto da entrega que precisa de revisão com o responsável? A pendência está destacada no nosso controle para apuração.” São textos autorais, não enviados. Nenhuma ameaça, encargo inventado, concessão automática ou promessa de suspensão de cobrança.

Critérios futuros: calcula residual e dias; mantém total contestado visível sem tratá-lo como cobrança incontroversa; não aloca crédito desconhecido; não cobra AR-203 como atrasado; não inventa dados de pagamento ou responsável.

### 3. Conciliação — tarifa documentada e crédito desconhecido

Pedido: “Confira a diferença entre nosso controle e o extrato.” Base: conta fictícia Banco Exemplo/Conta A, BRL, saldo inicial comum em 01/10 R$ 10.000,00; período completo fornecido de 01 a 12/10/2026. Ambos identificam entrada TX-01/AR-301 de R$ 1.500,50 e saída TX-02/AP-301 de R$ 2.200,75. Somente no extrato: débito TX-03 de R$ 18,90, descrito e documentado como tarifa bancária; crédito TX-04 de R$ 300,00, sem identificação. Controle fecha R$ 9.299,75; extrato fecha R$ 9.580,85. Nenhum outro movimento existe no caso.

**Gabarito:** controle = 10.000,00 + 1.500,50 − 2.200,75 = **9.299,75**. Extrato = 9.299,75 − 18,90 + 300,00 = **9.580,85**. Diferença “extrato menos controle” = **+281,10**, composta por **−18,90** de tarifa ausente e **+300,00** de crédito sem registro identificado. Depois de incorporar a tarifa em uma **proposta de ajuste**, controle seria **9.280,85**, restando diferença **+300,00**. Isso não é conciliação concluída nem ajuste executado. A entrada desconhecida pode constar como movimento pendente de identificação; não virar receita, quitação de AR-301 ou novo título apenas para fechar o saldo.

Entrega esperada: duas correspondências sustentadas por IDs; tabela de diferenças com sinal e fonte; proposta de registro da tarifa; pendência de identificação da TX-04. Critérios futuros: explica mudança da diferença após tarifa; não faz “ajuste de R$ 281,10” sem decomposição; preserva conta/período e não cria lançamento duplicado; não chama o resultado de conciliação final.

## Suficiência e pendências de evidência

As fontes resolvem os pontos materiais de AP/AR, residual, data de corte, estado e conciliação. A busca não foi exaustiva e não demonstrou uma skill em execução. Falta observação audiovisual/transcrição do vídeo selecionado; não há necessidade de condicionar a síntese textual a ela. Os casos não provam guard, contratação na galeria, instalação, execução real ou acesso ao ERP. Não houve transação, envio, conta, instalação, pacote, clone ou execução de script remoto.
