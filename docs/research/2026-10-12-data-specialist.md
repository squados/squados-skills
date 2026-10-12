# Especialista em Dados — síntese da pesquisa

Consulta em 12/10/2026. Escopo aprovado: analisar dados de negócios, investigar resultados e entregar conclusões, relatórios e gráficos utilizáveis. Não se limita a produto digital, laboratório ou programação; deve atender trabalho interno de operações, vendas, finanças e pessoas. Esta etapa pesquisa, sem criar o pacote.

## Fontes e alcance

- [Análise e diagnóstico](2026-10-12-data-specialist-skills-analysis.md): doze SKILL.md completos de cinco famílias e seis recursos determinantes completos.
- [Gráficos e relatórios](2026-10-12-data-specialist-skills-reporting.md): onze SKILL.md completos de cinco famílias, com especificações, exemplos e recursos decisivos.
- [Métodos profissionais](2026-10-12-data-specialist-methods.md): doze fontes substantivas, incluindo dez documentos e duas entrevistas de 2025 com transcrição gratuita; três casos fictícios com contas conferidas.

Consolidação: **23 SKILL.md principais distintos de oito origens**. Anthropic e OpenAI aparecem nas duas frentes com arquivos diferentes; cada origem conta uma vez. CONNECTORS Anthropic foi lido nas duas frentes, sem nova evidência independente. Linhagens arquivadas e forks não foram contados como outras soluções. Datas, SHA, autoria, licença, recursos e limites de leitura estão nos dossiês.

Nenhum audiovisual foi assistido; duas transcrições foram lidas com timestamps reais. Não foi obtido conteúdo audiovisual de 2026 consultável nesta rodada; há documentação profissional atualizada em 2026. Não houve crédito pago, conta de cliente, execução de skills externas ou artefato analítico de cliente.

## Recomendação

Combinar **proporcionalidade da Anthropic, diagnóstico e reconciliação da OpenAI, rigor estatístico sob demanda do K-Dense e comunicação analítica das fontes de relatórios**, com critérios profissionais independentes. A pessoa descreve a pergunta e a entrega; a skill identifica se precisa responder, explorar, reconciliar, investigar, comparar ou produzir relatório. Nenhum modo precisa ser memorizado.

A sequência útil é pergunta/decisão → significado dos dados → checagens materiais → análise suficiente → comunicação conferível. Uma pequena tabela pode terminar em cálculo e conclusão curta; um relatório pode exigir gráficos e apêndice. Não juntar engines, bibliotecas, intake, notebook, dashboard e protocolo científico por padrão.

## Componentes e decisões

| Componente | Fontes | Decisão e motivo |
|---|---|---|
| Profundidade pelo pedido | Anthropic analyze, OpenAI product-business-analysis | **Aproveitar:** decisão primeiro e método suficiente. **Descartar:** relatório/BI completo obrigatório para toda pergunta. |
| Semântica e cobertura | Anthropic explore-data, OpenAI data quality, [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework) | **Aproveitar:** o que cada linha representa, chaves, definições e qualidade para o uso. Completude não prova precisão; nulo não significa sempre erro. |
| Reconciliação e diagnóstico | OpenAI metric-diagnostics, Anthropic validate-data | **Aproveitar:** reproduzir a variação, comparar totais e decompor numerador/denominador, segmentos e composição. Contribuições precisam fechar com o total, sem sobreposição silenciosa. |
| Limpeza e extremos | K-Dense EDA, Anthropic estatística | **Adaptar:** investigar, preservar original e explicar transformação. **Descartar:** imputação, exclusão automática e alertas por limiar universal. |
| Inferência | K-Dense statistical-analysis, ASA, Magenta Book | **Aproveitar sob demanda:** desenho, unidade, dependência, efeito, intervalo e pressupostos. **Descartar:** tamanho fixo de grupo, APA obrigatória e valor-p como prova causal/econômica. |
| Contexto empresarial | Anthropic context-extractor, Abdo business-analysis | **Adaptar:** definições e repertório comercial quando ajudam. **Descartar:** todos os módulos, nunca perguntar, um profiler único e nota 100/100 como protocolo. |
| Gráfico e tabela | OpenAI visualize-data, Anthropic create-viz, Analysis Function | **Aproveitar:** forma pela comparação, unidades/período/base e dados de apoio. **Descartar:** quotas de pontos, paleta do fornecedor ou quantidade fixa de gráficos. |
| Relato | OpenAI build-report, wshobson, lyndonkl | **Adaptar:** conclusão próxima à evidência, interpretação e limite. **Descartar:** história persuasiva, causa ou ação forçada quando os dados só permitem observação. |
| Dashboard | OpenAI/Anthropic build-dashboard | **Adaptar:** consulta/exploração quando necessária; distinguir snapshot de dados ao vivo. **Descartar:** implantação, descoberta de todas as fontes e stack obrigatória. |
| Precisão e exportação | OpenAI artifact delivery, Anthropic, AntV | **Aproveitar conceito:** verificar cálculo, render e recipiente final; valor original diferente de arredondamento/apresentação. **Descartar:** serviço remoto como caminho padrão e abrir arquivo como prova completa. |
| Scripts | Profiler Abdo/K-Dense/borghei | **Adaptar a ideia:** mecânica recorrente pode economizar trabalho. Implementações não foram aprovadas para cópia; wrapper ou licença não prova correção nem pacote completo. |

## Falhas e divergências que orientam a criação

**Cardinalidade precisa de unicidade.** O [profiler Abdo](https://github.com/AbdoBasyioni/business-analysis-skill/blob/e8fdb7a93a59875ae5a3ffb239fdf0c2b336b3ae/assets/profile_data.py) rotula 1:1 pela igualdade da quantidade de distintos, sem validar ocorrências por chave. A coordenação conferiu a expressão e um contraexemplo próprio: tabelas `[A,A,B]` e `[A,B,B]` possuem dois distintos cada, porém quatro pares correspondentes; as chaves não são únicas. Não foi executado o profiler original. Sobreposição sugere candidato a relacionamento, não comprova sua cardinalidade.

**Grão muda após unir tabelas.** A [documentação Microsoft](https://support.microsoft.com/en-us/excel/learn-to-combine-multiple-data-sources-power-query) mostra como expandir itens acrescenta linhas por pedido. A análise deve conferir o nível da medida e totais antes/depois, sem apagar detalhe legítimo como se toda repetição fosse erro. A [documentação pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html) oferece validações sob demanda; não implica pandas instalado ou obrigatório.

**Regras de domínio não são universais.** Receita negativa pode representar devolução; percentual acima de 100 pode representar crescimento; identificador numérico não deve virar medida automaticamente. O profiler borghei pode contabilizar uma chave única como issue; sua abordagem é comparativa e possui licença condicionada. Restrições científicas de identificação e formatos de laboratório não devem impedir análise empresarial legítima.

**Descrição antiga não prova capacidade atual.** K-Dense distingue suporte automatizado, opcional, documentado e ausente; diretórios antigos anunciavam mais de 200 formatos. O script principal é um wrapper com imports transitivos não auditados. Não copiar um arquivo e prometer toda a capacidade do pacote.

**Arquivos HTML podem exigir rede.** O [dashboard Anthropic](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/build-dashboard/SKILL.md) afirma offline e usa CDN. Dados embutidos não bastam para garantir abertura sem internet. A frente de relatórios também registra interpolação de dados sem escape e crescimento tratado como benefício; a implementação precisa ser revista se algum componente for reutilizado.

**Exemplos não são cálculos validados.** A inspeção de wshobson encontrou total ponderado divergente e SQL que pode repetir gasto, alterar denominador de retenção ou perder o ano ao contar meses. São achados estáticos, sem execução da query. Templates demonstram intenção; não substituem recálculo e validação com a fonte.

**Narrativa não autoriza causa.** Decomposição contábil de volume/preço/mix explica componentes matemáticos, sem provar mecanismo causal. O [Magenta Book atualizado em 2026](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html) apoia escolha proporcional de evidência; entrevistas de [Cole Nussbaumer Knaflic](https://techleadjournal.dev/episodes/207/) e [CFI/Paul Barnhurst](https://corporatefinanceinstitute.com/resources/finpod/storytelling-with-data/) ajudam comunicação. Preservar diferença entre observação, hipótese, estimativa e recomendação.

## Casos para avaliação futura

Os [três casos fictícios](2026-10-12-data-specialist-methods.md) têm gabaritos e falhas discriminados. A coordenação conferiu novamente a aritmética, sem executar as skills:

| Caso | Resultado esperado | Erro detectado |
|---|---|---|
| Pedido unido a itens | Receita correta R$ 300, com dois pedidos; somar receita repetida produziria R$ 400 | Inflação por união e remoção indevida de itens legítimos |
| Taxa e composição de canais | Janeiro 50%; fevereiro 32,14%, embora ambos os canais melhorem 10 pp | Média simples de taxas e falsa atribuição causal; composição mudou |
| Mês aberto | Abril dias 1–12 cresce 20% no recorte equivalente; comparação com março inteiro daria −52% | Comparação temporal injusta e previsão apresentada como certeza |
| Extensão de cobertura | 72 pontuais entre 80 conhecidos: 90% entre conhecidos, cobertura 80%, limites totais 72–92% | Ausentes tratados como zero/sucesso e limite aritmético chamado de IC |

A futura execução deve produzir valores rastreáveis e gráficos coerentes com esses valores, sem inventar pontos diários, clientes, custos ou causalidade. Melhorar uma taxa observada em dez leads não comprova melhora duradoura. Uma conclusão inconclusiva ou um pedido focal de definição pode ser adequado.

Verificação do entregável: totais reconciliados, filtros e comparadores compatíveis, fonte/corte/unidades legíveis, escala adequada, tabela de apoio e inspeção no formato final. Inferência requer suas próprias checagens; não significância não prova equivalência. Intervalos de cobertura, confiança e previsão são coisas diferentes.

## Núcleo, referências e convivência com outras skills

O núcleo pode limitar-se a entender a pergunta, inspecionar dados, verificar riscos materiais, escolher análise e comunicar resposta/evidência/limite. Detalhes carregados por intenção: granularidade/uniões; taxas/composição/períodos; diagnóstico; inferência/previsão; gráficos; relatórios/dashboard; definições da empresa.

Dados cuida da análise e conclusão. Planilhas cuida de workbook editável, fórmulas, estilos e recálculo quando essa é a entrega. Apresentações cuida da sequência e narrativa em HTML sem diluir evidência. Um arquivo XLSX recebido não exige criar outro workbook; pedir um gráfico não exige slide ou dashboard. As fronteiras orientam colaboração, sem alterar o catálogo escolhido.

Escolher recursos pelo formato, volume e ferramentas disponíveis. Scripts podem ajudar bases grandes, reconciliação e contas repetidas; uma tabela pequena não exige programa. Dependência necessária ausente: explicar benefício e oferecer instalação simples ou alternativa disponível, sem afirmar que o Studio já possui a biblioteca.

Quando recorrência ou atrito justificar, oferecer adaptação concreta da própria versão: por exemplo, adotar a definição confirmada de receita líquida e o fechamento semanal da equipe. Aplicar com aceitação ou pedido; convenções individuais ficam no contexto/versão apropriada, sem se tornarem padrão público. Bibliografia e histórico extensos continuam no dossiê, fora da skill executável.

## Licenças e estado

Anthropic data tem Apache-2.0; K-Dense, Abdo, wshobson e AntV têm MIT observada. Borghei inclui Commons Clause; OpenAI/plugins e lyndonkl não tiveram permissão de redistribuição verificável localizada nos caminhos consultados. Não copiar texto, scripts ou assets desses pacotes para o produto sem base resolvida. Método profissional pode ser sintetizado em redação própria com fontes; reutilização permitida preserva avisos e atribuição pertinentes.

Nenhuma origem pesquisada muda a allowlist github da galeria. Conteúdo textual de pacote, imagens geradas no trabalho, dependências do runtime e dados do cliente têm papéis distintos. Não empacotar bibliotecas, fontes ou credenciais sem necessidade e contrato compatível.

Pesquisa documental e cálculos fictícios registrados; ainda sem pacote, instalação, guard/proposta Hermes, aprovação, execução real no Studio ou publicação. Compatibilidade, segurança integral e disponibilidade de conectores não foram demonstradas. A pasta temporária de leitura `.scratch/reports-research` permanece fora do commit: remoção PowerShell foi rejeitada pela revisão automática com motivo “blocked by policy”; não houve contorno da decisão.
