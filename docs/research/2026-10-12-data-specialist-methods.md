# Especialista em Dados — métodos profissionais

Pesquisa consultada em 12/10/2026. Frente: dados de negócios recebidos → qualidade e análise → gráficos → conclusão e decisão. Aplicável a vendas, operações, finanças e pessoas em empresas diversas. Não cria, instala nem executa a futura skill. Os casos abaixo são fictícios e suas contas foram conferidas; não constituem uma demonstração de execução da skill.

## Alcance e contagem

**12 fontes substantivas consultadas:** dez documentos profissionais ou oficiais e duas entrevistas de 2025 com transcrição gratuita. São páginas distintas, mas várias pertencem à mesma família Government Analysis Function; não representam 12 métodos independentes. As referências de software foram consultadas em sua documentação atual. Nenhuma conta, crédito, vidIQ ou curso pago foi usado.

A busca resolveu as dúvidas sobre granularidade, uniões, qualidade, interpretação de percentuais, períodos comparáveis, comunicação e limites de inferência. Não se procurou uma quota de vídeos ou fontes. A comparação de pacotes existentes pertence às outras frentes.

## Fontes, acesso real e contribuição

| ID | Fonte original, autoria e data visível | Material efetivamente consultado | Contribuição e decisão |
|---|---|---|---|
| F1 | [Government Data Quality Framework](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework), governo britânico, 03/12/2020 | HTML: princípios, necessidades de usuários e seis dimensões de qualidade | **Adaptar:** avaliar completude, unicidade, consistência, atualização, validade e precisão segundo a decisão. Dados completos podem estar errados; não exigir perfeição universal. |
| F2 | [Framework: guidance](https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework-guidance), governo britânico, 03/12/2020 | HTML: dados críticos, metadados e comunicação de qualidade | **Aproveitar:** registrar origem, cobertura, transformações e problemas. Distinguir ausência sistemática de campo não aplicável e dizer como isso limita a análise. |
| F3 | [Understand star schema](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema), Microsoft Learn; data de atualização não exposta no texto retornado | HTML: fatos, dimensões, relacionamentos e granularidade consistente | **Adaptar:** declarar o que uma linha representa e como as tabelas se relacionam. **Descartar como padrão obrigatório:** montar Power BI ou um data warehouse para analisar uma planilha pequena. |
| F4 | [DataFrame.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html), pandas, documentação retornada como 3.0.6 na abertura atual | HTML: `validate`, `indicator`, chaves e alerta sobre nulos | **Aproveitar sob demanda:** conferir cardinalidade e não correspondências. `many_to_many` permite a operação sem validar unicidade; nulos podem casar com nulos, diferentemente de SQL usual. Não assumir que pandas está instalado. |
| F5 | [Data visualisation: charts](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/), Analysis Function Central Team, 19/05/2022 | HTML: escolha de gráfico, acessibilidade, barras, linhas, eixos, rótulos e exemplos | **Adaptar:** escolher gráfico pela comparação; barras com base zero, linhas com escala clara, fonte/período/unidade e alternativa textual ou tabela. **Descartar:** regra universal de começar todo eixo em zero ou limites estéticos rígidos sem contexto. |
| F6 | [Communicating quality, uncertainty and change](https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/), Data Quality Hub, 17/12/2018 | HTML: incerteza, revisões e resultados provisórios | **Adaptar:** declarar limitações que alteram a interpretação e marcar números provisórios. A página está em revisão e avisa que sua acessibilidade aguarda atualização; para gráficos acessíveis, preferir F5. |
| F7 | [Writing about data](https://analysisfunction.civilservice.gov.uk/policy-store/writing-about-data/), GSS Presentation Champions Network, 03/04/2025 | HTML: público, linguagem simples, pontos principais e contexto | **Aproveitar:** explicar o significado para o trabalho, concentrar o texto nos achados relevantes e tornar limitações transparentes. A predecessora “Writing about statistics” foi aberta, identificada como arquivada e substituída por esta; não conta como fonte substantiva adicional. |
| F8 | [Magenta Book: guidance on evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), HM Treasury/Evaluation Task Force, atualização 15/05/2026 | HTML: seleção de abordagem, contrafactual, comparações e avaliação baseada em teoria | **Adaptar:** tendência temporal e associação não bastam para atribuir causalidade. Avaliação causal exige desenho e evidência apropriados; métodos baseados em teoria também precisam testar mecanismos e explicações alternativas. Não tornar experimento requisito para toda descrição de negócio. |
| F9 | [ASA statement on significance and p-values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf), American Statistical Association, 07/03/2016 | Texto extraído do comunicado oficial, três páginas, incluindo seis princípios | **Aproveitar em inferência:** valor-p não mede tamanho/importância do efeito nem probabilidade de hipótese verdadeira. Decisão não deve depender só de um corte; informar desenho, efeito, pressupostos e limitações. O comunicado resume a declaração, não é um tutorial de testes. |
| F10 | [Tratamento de dados pessoais pelo Poder Público](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-poder-publico-anpd-versao-final.pdf/@@display-file/file), ANPD, versão 2.0, junho/2023; página criada 28/01/2022 e modificada 23/01/2025 | PDF textual: capa/expediente, seção Necessidade, p. 25, e contexto sobre divulgação/compartilhamento | **Adaptar:** minimizar dados pessoais ao necessário para a finalidade. O documento trata do Poder Público; não transplantar suas bases e procedimentos jurídicos para empresas privadas. A data modificada da página não comprova revisão material do PDF. |
| F11 | [Entrevista com Cole Nussbaumer Knaflic, episódio 207](https://techleadjournal.dev/episodes/207/), Tech Lead Journal/Henry Suryawirawan, 24/02/2025 | Página e transcrição gratuita: 00:12:25 negócios; 00:15:51 planejar/criar/entregar; 00:28:57 ideia principal; 00:46:42 ferramentas | **Adaptar:** começar pela audiência e mensagem, planejar antes da ferramenta e comunicar a conexão entre achados. A profissional relata uso amplo de Excel/PowerPoint; isso é prática declarada, não benchmark de ferramentas. Não assistido. |
| F12 | [Crafting the Narrative — Storytelling with Data](https://corporatefinanceinstitute.com/resources/finpod/storytelling-with-data/), CFI/Meeyeon e Paul Barnhurst, 12/08/2025, duração indicada 17:15 | Página e transcrição gratuita: 01:31 insights/ação; 05:18 o que ocorreu/por que importa/próximo passo; 10:07 ausência de ação na entrega | **Adaptar:** conclusão conectada à decisão com recomendação explícita quando o pedido exige ação. É entrevista que promove curso, não estudo experimental; exemplos de causa relatados pelo entrevistado não autorizam atribuir causa em dados observacionais próprios. Não assistido. |

Os timestamps de F11 são inícios de capítulos na transcrição. Os de F12 são marcações de turnos; não afirmam o segundo exato de cada frase. Nenhum audiovisual foi reproduzido ou inspecionado visualmente. A [página de webinars Datawrapper](https://www.datawrapper.de/webinars) foi consultada como descoberta; informa gravação para inscritos. Sem registro, conta ou transcrição pública obtida, ficou fora dos 12 materiais substantivos. Não se obteve vídeo de 2026 com conteúdo consultado; há duas transcrições reais de 2025 e documentação metodológica atualizada em 2026.

## Método recomendado para a futura skill

Esta é uma síntese proposta para o destino, não a reprodução integral de um framework.

1. **Reconhecer o pedido e a decisão.** Aproveitar a conversa, arquivos e definições disponíveis. Identificar público, período, métrica e comparação. Perguntar só pelo que muda materialmente a interpretação: “venda” pode significar pedido, pagamento ou faturamento. Se faltarem dados, avançar na inspeção que já seja útil e indicar o necessário.
2. **Conhecer os dados recebidos.** Descrever arquivos/abas, colunas, unidade de cada linha, chaves, moeda, datas, fuso e origem. Verificar cobertura e se a base é universo observado ou amostra. Separar cadastro, transação, item, pessoa e saldo: misturá-los altera contagens e totais. F1–F4.
3. **Checar qualidade proporcionalmente.** Contar linhas e entidades; verificar duplicatas segundo chave de negócio, campos ausentes, tipos, unidades, limites e valores extremos. Não eliminar uma repetição legítima, converter ausência em zero ou excluir extremo automaticamente. Preservar originais e explicar alterações relevantes. Conferir antes/depois de união: linhas, chaves, correspondências, totais e granularidade. F1–F4.
4. **Analisar a comparação correta.** Declarar numerador, denominador e filtros; usar soma dos numeradores dividida pela soma dos denominadores para uma taxa agregada compatível. Distinguir variação relativa de pontos percentuais e média simples de ponderada. Comparar janelas equivalentes; separar preço, volume e composição quando necessário. Os casos abaixo demonstram a necessidade aritmética dessas decisões.
5. **Escolher poucos gráficos úteis.** Barras para categorias; linhas para tempo; distribuição quando média esconde dispersão; dispersão para associação, com cautela causal. Mostrar título descritivo, unidade, período e base. Não depender apenas de cor; manter tabela que permita conferir valores. Não impor um dashboard a todo pedido. F5.
6. **Concluir com limites.** Separar observação comprovada, hipótese explicativa e recomendação. Explicar o impacto da qualidade faltante e o que poderia mudar a conclusão. Se houver inferência, verificar desenho, independência/unidade, seleção, tamanho de efeito, pressupostos e comparações exploratórias; não inventar intervalos ou significado de testes. Um intervalo frequencista não significa simplesmente “95% de chance do parâmetro estar neste intervalo”; sobreposição de dois intervalos também não resolve sozinha o teste da diferença. F6, F8–F9.
7. **Entregar para o trabalho da pessoa.** Primeiro a resposta à pergunta, depois evidência e próximos passos proporcionais. Conforme o pedido: resumo no chat, tabela/planilha conferível, gráficos legíveis ou relatório. Narrativa não autoriza preencher causas desconhecidas. Recomendação pode ser investigar ou aguardar cobertura suficiente. F7, F11–F12.

### Dados pessoais no pedido concreto

Quando a base contiver identificação pessoal, avaliar quais campos são necessários à pergunta e à entrega. Para desempenho por filial, nomes, CPF ou contatos podem ser dispensáveis; para investigar registros duplicados, uma chave interna pode bastar. Agregar resultados quando isso atende à finalidade, evitando exposição individual desnecessária. Não enviar a base a serviços externos nem publicá-la por conveniência operacional. Esta é uma adaptação prática do princípio de necessidade de F10; não presume anonimização garantida, nem constitui auditoria jurídica completa.

### Núcleo curto e referências por intenção

| Conteúdo | Onde faz sentido | Por quê |
|---|---|---|
| Pedido/decisão, inspeção, qualidade material, análise, gráfico e conclusão conferível | Núcleo | Fluxo universal, com ferramenta escolhida pelo tamanho e formato reais |
| União de tabelas e granularidade | Referência acionada por múltiplas tabelas ou métricas repetidas | Evitar inflação silenciosa sem carregar instruções de banco em toda consulta |
| Percentuais, composição e períodos | Referência acionada por comparação/taxa/série | Resolver a interpretação exigida pelo pedido |
| Inferência, experimentos e previsão | Referência acionada quando o pedido exigir generalização, efeito ou futuro | Mais pressupostos e limites; não impor ML a descrição básica |
| Planilhas e exportação | Reutilizar capacidade de formato disponível | Fórmulas, tipos e recálculo dependem da entrega; não duplicar uma skill inteira |
| Gráficos/acessibilidade | Referência acionada por entrega visual | Mecânica de criação e verificação conforme o formato |

**Dependências:** não obrigar Python em três contas ou uma tabela pequena. Para arquivos maiores ou transformações repetidas, scripts podem tornar a mecânica verificável. Verificar runtime/bibliotecas presentes e oferecer instalação quando uma dependência necessária faltar; não afirmar que o Studio já a fornece. Se a instalação não estiver autorizada, oferecer entrega viável com as ferramentas existentes. Scripts próprios só para mecânica necessária, sem infraestrutura preventiva.

**Adaptação útil:** incorporar no artefato do pedido as definições de receita, status, chaves e filtros confirmados; reaproveitá-las em atualizações daquele trabalho. Quando uma preferência recorrente ou um atrito concreto justificar, oferecer uma mudança específica na própria versão da skill, por exemplo: “Posso adaptar sua versão para usar receita líquida e comparar sempre janelas equivalentes nos relatórios mensais.” Aplicar essa mudança com aceitação ou pedido da pessoa, mantendo as convenções daquela empresa na sua versão, sem transformá-las em padrão público. Não criar armazenamento de dados pessoais ou alterar permanentemente a skill com aprendizados de uma empresa sem autorização. Referências devem ser reconhecidas pela intenção do pedido, sem menu técnico exigido do usuário.

## Casos fictícios para avaliar a futura execução

As tabelas são entradas mínimas com gabarito. A avaliação deve julgar qualidade, insight, gráfico e comunicação, não apenas a existência de um arquivo. As contas foram conferidas em PowerShell em 12/10/2026; não se instalou biblioteca nem executou pacote.

### Caso 1 — varejista: pedido repetido após união com itens

Pedido: “Qual foi o faturamento por cliente? Junte os pedidos com seus itens e faça um gráfico.”

| Pedido | Cliente | Receita do pedido |
|---|---|---:|
| P1 | A | R$ 100 |
| P2 | B | R$ 200 |

| Pedido | Item | Valor do item |
|---|---|---:|
| P1 | I1 | R$ 60 |
| P1 | I2 | R$ 40 |
| P2 | I3 | R$ 200 |

**Problema:** união por pedido passa de duas para três linhas. Somar `receita do pedido` após expansão gera R$ 400: P1 aparece duas vezes. Correto: R$ 300, cliente A R$ 100 e B R$ 200. A inflação é R$ 100 ou 33,33%. Os três itens são legítimos; remover arbitrariamente “duplicados” de pedido na tabela de itens perderia dados.

**Esperado:** declarar granularidades, preservar receita no nível do pedido ou agregar itens corretamente, reconciliar R$ 300 e dois pedidos únicos. Gráfico de barras por cliente, eixo desde zero, rótulos monetários e base “dois pedidos”. Insight: B representa 66,67% da receita observada. Limite: não prova maior rentabilidade; custos não foram recebidos.

**Reprovação:** gráfico soma R$ 400, cliente A vira R$ 200, ou total corrigido sem explicar a multiplicação/sem preservar detalhe legítimo.

### Caso 2 — serviços: taxa cai no total apesar de melhorar nos segmentos

Pedido: “A conversão caiu em fevereiro. Qual canal está piorando?” Entradas de janeiro e fevereiro completos, com a mesma definição de lead e conversão.

| Mês | Canal | Leads | Conversões | Taxa |
|---|---|---:|---:|---:|
| Janeiro | Indicação | 100 | 80 | 80% |
| Janeiro | Prospecção | 100 | 20 | 20% |
| Fevereiro | Indicação | 10 | 9 | 90% |
| Fevereiro | Prospecção | 270 | 81 | 30% |

**Gabarito:** total janeiro 100/200 = 50%; fevereiro 90/280 = 32,14%. Queda de 17,86 pontos percentuais. Ambos os canais melhoraram 10 pontos. A participação de Indicação nos leads passou de 50% para 3,57%. Média simples de 90% e 30% daria 60% e não é a taxa total de fevereiro.

**Esperado:** duas visões complementares: barras com taxas por canal/mês e composição dos leads, mostrando denominadores. Insight: a mudança da composição explica aritmeticamente a discrepância entre agregado e segmentos. Padronizando fevereiro pela composição 50%/50% de janeiro, a taxa seria 60%; é cálculo de comparação, não contrafactual causal comprovado.

**Decisão:** investigar por que a origem dos leads mudou e se a definição/coleta permaneceu estável. A taxa por canal observada melhora, mas esses tamanhos desiguais, especialmente dez leads por indicação, não provam melhora duradoura. Não concluir que o canal causou conversão nem prometer recuperar 60% ao alterar investimento.

**Reprovação:** acusar piora de um canal inexistente nos dados, calcular média simples como total ou fazer recomendação causal conclusiva sem desenho adequado.

### Caso 3 — operação comercial: mês aberto e entrega sem cobertura completa

Pedido: “As vendas despencaram em abril? Faça a evolução e me diga se preciso cortar a meta.”

| Janela | Receita observada | Cobertura |
|---|---:|---|
| Março completo | R$ 100.000 | Mês fechado |
| Março, dias 1–12 | R$ 40.000 | Recorte confirmado |
| Abril, dias 1–12 | R$ 48.000 | Exportação até dia 12 |

**Gabarito:** R$ 48 mil contra R$ 100 mil produz −52%, mas compara janela parcial com completa. Dias 1–12 contra dias 1–12 produzem +20%. Essa comparação ainda pode sofrer calendário, dias úteis, feriados, sazonalidade e atrasos de registro; não garante fechamento acima da meta.

**Esperado:** marcar abril como parcial, separar mês fechado de acumulado comparável e preferir linha acumulada diária se os dados diários forem recebidos. Com apenas esses três totais, usar barras para os dois recortes equivalentes e tabela de contexto; não inventar pontos diários. Insight: o recorte equivalente recebido cresceu; não há suporte para afirmar queda de 52% no desempenho mensal. Pedir/obter calendário e ritmo diário se a decisão de meta exigir projeção; simples extrapolação linear não vira previsão confiável.

**Extensão de qualidade da mesma operação:** entre 100 entregas, 80 têm status conhecido, sendo 72 pontuais; 20 estão sem status. Pontualidade entre conhecidos = 90%; completude de status = 80%. No universo de 100, pontualidade possível vai de 72% a 92%, dependendo dos ausentes. Esse intervalo é limite aritmético, não intervalo de confiança. Não apresentar 90% como taxa comprovada de todas as entregas, nem preencher ausências como atrasos ou sucessos sem regra acordada.

**Reprovação:** “queda de 52%, corte a meta”, gráfico liga totais não comparáveis sem anotação, extrapolação vendida como certeza ou 90% de pontualidade sem informar cobertura.

## Checagem de uma entrega real posterior

- Pergunta respondida e decisão/contexto reconhecidos, sem entrevista que repita informações já dadas.
- Dados originais preservados; origem, cobertura, definição das métricas e transformações relevantes registradas.
- Granularidade, chaves, uniões, ausências e denominadores conferidos; totais reconciliados com entradas.
- Comparações temporais equivalentes ou limitação explicitamente apresentada.
- Tabela de valores permite conferir gráficos; eixo, escala, unidade, título e período são legíveis no formato final.
- Arquivo solicitado abre e mantém tipos/fórmulas adequados; quando há fórmulas, valor exibido/recálculo realmente verificado ou pendência declarada.
- Achados, hipóteses, recomendações e incerteza distinguidos. Ausência de evidência não virou evidência de ausência.
- Dados pessoais desnecessários não aparecem em gráfico, relatório ou envio externo.
- A entrega mostra resultado utilizável e seu limite; não chama proposta, teste fictício ou JSON válido de execução real comprovada.

## Limites, autoria e distribuição

Não foram copiados código, templates, assets ou transcrições. As técnicas foram sintetizadas com atribuição e as situações numéricas são próprias. F1/F2 expõem Open Government Licence v3.0; a página da ANPD expõe aviso de licença, que não deve ser presumido como permissão para adaptar e redistribuir qualquer recurso associado. Não se auditou licença de redistribuição de cada documento ou software: consulta com paráfrase e link não constitui aprovação para empacotar arquivos de terceiros.

A documentação F4 retornou 3.0.5 no resultado de busca e 3.0.6 na abertura; usa-se a versão observada na página aberta. Isso não identifica a versão do ambiente de execução. Nenhuma capacidade Hermes/Studio, dependência instalada, compatibilidade de pacote ou execução autenticada foi comprovada nesta frente. Pesquisa metodológica suficiente para a proposta; criação e avaliação real da futura skill permanecem etapas posteriores.
