# Assistente Financeiro — síntese comparativa

Pesquisa em 12/10/2026, rodada 18 de 33 especialidades aprovadas. Apoio interno: documentos, contas a pagar/receber, saldos, vencimentos, conciliação e preparação de cobranças. Nenhuma conta acessada, pagamento, baixa ou mensagem executada; nenhum pacote criado/instalado.

## Resultado para o desenho posterior

A combinação recomendada usa registro e exceções Receiptor, conferência documental Panaversity, agenda curta Bromso e vínculo entre materiais/eventos; em recebíveis, fluxo Loopfour, controles AdoptAI, unicidade cxtx e brief Paidnice. Nenhum pacote é incorporado integralmente.

O núcleo reconhece a entrega, aproveita os arquivos e conserva documento → título/parcela → saldo/data → evidência → pendência. Organizar boletos não exige fechamento contábil; analisar uma diferença não exige plataforma ou conexão bancária. Pode entregar tabela, lista, arquivo ou rascunho proporcional ao pedido.

## Dossiês e deduplicação

| Frente | Arquivo | Consulta efetiva |
|---|---|---|
| Pagar, documentos e despesas | [Skills de contas a pagar](2026-10-12-financial-assistant-skills-payables.md) | Doze SKILL completos de seis repositórios: nove métodos locais e três loaders remotos; referências/scripts/evals com alcance explícito |
| Receber, aging e conciliação | [Skills de contas a receber](2026-10-12-financial-assistant-skills-receivables.md) | Seis rotinas aprofundadas; nove SKILL lidos contando loaders auxiliares e cópia para comparação; recursos e scripts por leitura |
| Métodos e casos | [Métodos profissionais](2026-10-12-financial-assistant-methods.md) | Sete registros primários com níveis de acesso distintos; um vídeo Odoo 2026 por descrição/capítulos; três casos autorais |

Consolidado: **dezenove textos SKILL distintos de dez famílias**, sendo **quinze rotinas com método local e quatro loaders remotos**. O accounting-settings Well foi lido nas duas frentes, contado uma vez. Payment-reconciliation Loopfour/harshith é cópia literal, contada uma vez como conteúdo; a leitura da cópia serviu para deduplicar. Existem onze repositórios consultados incluindo essa variante, não onze provas independentes.

Loaders Well não permitiram examinar o método remoto; descrição e arquivo completos não demonstram comportamento. Reuso CFO/Planilhas e diretórios não aumenta as novas leituras. A pesquisa seleciona componentes, sem ranking estatístico ou auditoria exaustiva da internet.

## Componentes: fonte → escolha → motivo

| Origem/componente | Escolha | Adaptação ao trabalho |
|---|---|---|
| Composio/invoice-organizer: inventário, índice e incompletos | Adaptar conceito | Conteúdo e origem antes de nome; preservar originais/colisões/IDs. Data do arquivo não substitui emissão/vencimento |
| Receiptor/receipt-processing e categorization: registro, extração e exceções | Aproveitar | Fonte/localizador e categoria operacional da empresa. Confiança de extração não confirma legitimidade, pagamento ou dedutibilidade |
| Receiptor/bank-reconciliation e monthly-close: diferenças e continuidade | Adaptar | Exports fornecidos e pendências rastreáveis; descartar sinal incorreto no exemplo, tolerância universal, ajuste para zerar e regras fiscais estrangeiras |
| Panaversity/invoice-reconciliation: fatura versus contrato/pedido/aceite | Adaptar | Verificar preço, quantidade, parcela e entrega quando houver documentos; ausência de pedido não invalida todo serviço. Divergência pede revisão, sem aprovar/rejeitar/pagar |
| Auromix: múltiplos materiais para um evento, componentes e originais | Adaptar conceito | Nota, pedido e comprovante podem sustentar uma despesa; parcelas/estornos continuam visíveis. Não portar modelo chinês ou estrutura de pastas obrigatória |
| Auromix: documentos de outras despesas cobrindo evento sem nota | Descartar mecanismo | Documento precisa corresponder ao evento real; não substituir evidência ausente por nota de outra compra nem ocultar a relação |
| Bromso/accounts-payable: saldo, vencimento, disputa e agenda | Aproveitar formato curto | Data-base e faixas explícitas; não chamar dívida vencida de current por convenção indefinida ou impor rodada semanal/quinzenal |
| Loopfour/ar-collections: cobrança versus saneamento | Aproveitar | Duplicata, disputa e crédito não aplicado são pendências administrativas antes de afirmar inadimplência |
| Loopfour/payment-reconciliation: pagamento, parcial, excesso e remessa | Aproveitar | Referência/IDs e decomposição antes de semelhança; correspondência provável não é autorização de baixa |
| Paidnice/AR: CSV local, corte e brief factual | Adaptar | Dados suficientes sem conta; descartar somas de moedas, saldo presumido, snapshot atual apresentado como histórico, juros e tom automáticos |
| AdoptAI/AR aging: faixas, bruto/créditos/líquido e controles | Adaptar | Corte e base temporal; para atraso usar residual por vencimento. Controle não feito permanece não verificado |
| AdoptAI/bank-rec-to-gl: diferenças e passes de matching | Aproveitar ideia, corrigir limites | Primeiro candidato ou primeiro subconjunto não prova exclusividade. Itens desconhecidos não somem por total líquido zero |
| cxtx/fcs-reconcile: correspondência mutuamente única, precisão e integridade | Aproveitar técnica | Comparador 1:1 não resolve alocação parcial ou remessa sozinho; normalização precisa do arquivo/moeda/idioma, sem modos/YAML obrigatórios |
| Well loaders: agenda, AP/AR e contexto | Somente contraste | Método remoto não consultado, conexão obrigatória e licença restritiva. Não importar como solução executável |
| Microsoft/Conta Azul/Omie/Odoo: documento, parcial, corte e conciliação | Adaptar | Estados e cardinalidade variam por ERP; conceitos ajudam sem transportar menu, integração ou atalho de ajuste |

## Decisões que devem orientar a execução

- Usar contexto e campos disponíveis; perguntar somente o que muda saldo, corte, identidade, prazo ou entrega. Organização parcial útil pode avançar com pendências.
- Preservar arquivo/linha, IDs como texto, parcelas, datas e valores originais. Normalização separada; ausência ou OCR incerto não viram certeza.
- Separar documento repetido de obrigação repetida. Valores iguais não bastam para duplicata; várias evidências de uma parcela não criam várias dívidas.
- Saldo residual depende de pagamentos/créditos efetivamente vinculados, na data declarada. Crédito sem identificação fica separado; parcial não reinicia vencimento sem renegociação.
- Somar por moeda/entidade e usar Decimal/centavos quando calcular. Encargos, descontos e rateios só com base documentada pertinente; nenhuma taxa automática.
- Aging por vencimento quando o pedido é atraso; idade desde emissão pode servir a outra pergunta, com rótulo. A vencer, hoje, vencido e vencimento ausente são estados distintos.
- Conciliação explicita conta, período, cobertura, correspondências e diferenças. Saldo total igual não comprova todas as linhas; par valor/data ambíguo continua candidato.
- Rascunho solicitado usa fatos, residual e linguagem adequada; contestação é apuração, sem ameaça, concessão ou consequência inventada. Preparar não equivale a enviar.
- Oferecer adaptar a própria skill quando recorrência/atrito justificar, explicar benefício e aplicar após aceitação ou pedido direto.

## Divergências e conferências decisivas

**Estados:** previsto, registrado, informado pago, agendado, crédito identificado, alocado, baixado e conciliado têm evidências distintas. Não exigir banco para organizar documentos, nem tratar tela de agendamento como execução. A informação fornecida pela equipe pode ser registrada como tal, sem elevar seu status automaticamente.

**Sinais e associação:** tarifas/saídas não aumentam caixa; valores desconhecidos opostos podem cancelar no total sem estar explicados. Tolerância ajuda a classificar diferença, não apaga centavos ou comprova ligação. Matching e integridade interna não demonstram completude contra fonte independente.

**Corte:** saldo atual e recebimento posterior não devem reescrever a posição histórica. Paidnice exibe data sem reconstruir todos os movimentos; AdoptAI agrega recebimentos sem validar a janela em sua função consultada. Se a cobertura não permite recompor passado, declarar isso.

**Checks:** a coordenação leu os três dossiês e conferiu `ar_aging.py` AdoptAI. O script guarda certos controles ausentes como skipped e passed e agrega `overall` por passed; prints específicos avisam que não foram feitos. Não usar esse resultado agregado como prova de conciliação integral. Leitura estática não é execução ou teste reproduzido.

**ERP:** Conta Azul descreve múltiplos movimentos para um lançamento; Omie descreve limitações e formas próprias de associar baixas parciais. São comportamentos de produto, não regra universal. Não criar ajustes só para fechar diferença. [Conta Azul](https://ajuda.contaazul.com/hc/pt-br/articles/7454101596429-Concilia%C3%A7%C3%A3o-v%C3%A1rias-movimenta%C3%A7%C3%B5es-do-banco-com-um-lan%C3%A7amento), [Omie](https://ajuda.omie.com.br/pt-BR/articles/6812438-perguntas-frequentes-conciliacao-bancaria).

## Materiais recentes e limites

Artigos Conta Azul de abril/junho de 2026, Microsoft e Omie atualizados/contextualizados sustentam conceitos de parcial, corte e estados. Odoo 19 foi consultado por conteúdo indexado quando abertura falhou, sem comprovar interface/execução.

Vídeo oficial *Bank reconciliation | Odoo Accounting*, de 18/03/2026, foi identificado por descrição e capítulos 00:31, 01:55, 03:34 e 06:50. Não houve transcrição ou audiovisual; os timestamps são editoriais, não procedimentos observados. [Vídeo original](https://www.youtube.com/watch?v=P8EItiKqm5k).

A coordenação tentou página BCB/Pix Agendado: retorno exigiu JavaScript, portanto não houve leitura integral. A frente AP consultou trecho indexado de requisitos Pix, com revisão não certificada; essa lacuna não vira aprovação regulatória. Não houve pesquisa de multa, taxa legal, tributos ou vencimento jurídico para os casos, que os excluem explicitamente. Nenhum crédito vidIQ consumido.

## Casos para futura avaliação

| Caso fictício | Gabarito material | Falha revelada |
|---|---|---|
| AP: cinco documentos e quatro obrigações | Total R$3.631,20; segunda via não soma novamente; parcelas iguais permanecem legítimas. R$1.250,40 vencido/agendado não confirmado, R$420,10 hoje, R$1.960,70 futuro | Duplicar título, remover parcela legítima ou declarar pagamento executado |
| AR: pagamento parcial, contestação e crédito sem vínculo | Residual R$3.200,70; vencido R$2.700,50, com R$1.200 contestado; atrasos 32/22 dias. Crédito R$300 separado | Alocar pelo valor, reiniciar vencimento ou cobrar título ainda a vencer |
| Controle versus extrato | Controle R$9.299,75; extrato R$9.580,85; diferença +R$281,10 = tarifa −R$18,90 + crédito desconhecido +R$300 | Ajuste único fictício, crédito como receita/quitação ou conciliação declarada concluída |

Após proposta de registrar a tarifa, controle seria R$9.280,85 e diferença remanescente +R$300. A coordenação conferiu somas em Decimal e datas com calendário; casos são autorais e não foram executados por skill. O gabarito aceita formatos diferentes que conservem evidência e lógica, sem frase única.

## Organização, recursos e autoria

Núcleo curto de intenção, origem, estado, cálculo e entrega. Referências podem detalhar documentos/AP, AR/rascunhos, aging e conciliação. Não importar manual CFO ou sistema de bookkeeping completo; template da empresa vem antes de inventar layout.

Scripts podem agregar controle de unicidade, alocação, datas e centavos em lote concreto; não são necessários para um rascunho ou três contas. Recursos externos consultados exigem correções/contexto antes de reutilizar. Se faltar ferramenta necessária, explicar benefício e oferecer instalação simples para pessoa não técnica; alternativa existente pode bastar. Nenhuma instalação ocorreu.

Licenças incluem MIT, Apache-2.0, PolyForm Perimeter e ambiguidade Composio. Well não é MIT aberto irrestrito; variante harshith foi leitura para deduplicação, sem licença própria integral verificada. Nenhum código/template incorporado; preservar autoria/avisos aplicáveis em eventual cópia substancial. Pesquisa não altera a allowlist ou torna pacotes automaticamente contratáveis.

## Estado da entrega

Pesquisa consolidada, sem skill criada, guard/proposta, contratação, instalação ou uso real no Studio/Hermes. Sem operação financeira ou eficácia demonstrada. Galeria e espelho Desktop não alterados, sem push/publicação por esta unidade. Próxima pesquisa: Especialista em Compras. Criação dos pacotes somente depois das 33 pesquisas, conforme sequência aprovada.
