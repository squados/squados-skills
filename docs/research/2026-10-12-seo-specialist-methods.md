# Especialista SEO: métodos oficiais e critérios de avaliação

Pesquisa em 12/10/2026 para uso interno do SquadOS, em negócios diversos e PT-BR. Esta frente fundamenta componentes das skills; outras frentes estudam pacotes existentes. Não audita um cliente real, altera site, publica conteúdo ou instala ferramentas. Metodologia: `skills/skill-manager/references/research.md`.

## Direção recomendada

A futura skill deve **entender objetivo e página/público → verificar evidência disponível → separar descoberta/rastreamento, indexação, apresentação/ranking e resultado de negócio → formular diagnóstico e prioridades → entregar ação verificável e acompanhamento**.

SEO não equivale a gerar textos com palavras-chave nem a concluir um checklist universal. A importância de uma correção depende do problema observado, páginas afetadas, finalidade e esforço/risco. Melhorar acesso técnico pode ser necessário e ainda não garantir indexação, destaque ou vendas.

As fontes técnicas usadas são oficiais Google Search Central, Search Console e Business Profile. Não se extrapolam suas regras para Bing ou outros mecanismos. Matrizes, prioridades e fixtures são propostas autorais de avaliação, não metodologia certificada ou previsão de rank.

## Alcance e evidência

- Documentação pública atual e blog oficial, com datas mostradas em 2025–2026 quando presentes. Data de revisão do documento não implica mudança de todos os requisitos nesse dia.
- Conteúdo útil/confiável reutilizado da frente Criador de Conteúdo desta mesma sessão, sem nova leitura integral. Fontes detalhadas abaixo são documentação/orientação técnica de plataforma, não experimentos causais sobre clientes.
- Pesquisa externa somente leitura. Não houve acesso a Search Console, Analytics, Merchant Center, Business Profile ou ferramentas pagas; nenhum crédito vidIQ consumido. Não foram levantados volumes de busca, posições, tráfego, backlinks ou vendas de um cliente.
- Nenhum audiovisual foi assistido. Vídeos recentes entram como shortlist com metadata/acesso explícitos; alegações técnicas derivam dos documentos realmente consultados.

## Fontes aprofundadas

### S01 — Utilidade e precisão antes da contagem de palavras

[Conteúdo útil e confiável para pessoas](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), Google Search Central. Rodapé verificado anteriormente nesta sessão: revisão 05/10/2026. Leitura reutilizada de `2026-10-12-content-creator-methods.md`, C03.

**Aproveitar** informação/análise própria, fonte, experiência e revisão de erros/títulos. **Adaptar** à pergunta e finalidade da página. **Descartar** meta universal de palavras, reescrita de concorrentes sem valor, data trocada para aparentar atualização ou nota de E-E-A-T tratada como garantia de ranking. O documento afirma que E-E-A-T não é um fator único específico de ranking. Texto correto e útil é parte do trabalho; não comprova indexação ou demanda por si só.

Localizadores: qualidade, expertise e foco nas pessoas. Não foi avaliado conteúdo de cliente nem aplicada pesquisa de leitores.

### S02 — Descoberta e compreensão do conteúdo

[SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), Google Search Central. Rodapé: revisão 10/12/2025. Texto acessado, sobretudo fundamentos e conteúdo/termos de busca.

Explica SEO como ajudar mecanismos a entender o conteúdo e pessoas a encontrá-lo/decidir visitar. Recomenda conteúdo organizado, útil, próprio, atualizado, títulos pertinentes e links relevantes. Considera diferenças de vocabulário entre leitores sem exigir todas as variantes exatas. **Aproveitar** correspondência pergunta→página e clareza de navegação/conteúdo. **Adaptar** ao negócio; nem toda orientação se aplica. **Descartar** segredo de primeiro lugar, keyword stuffing ou publicar uma página por cada sinônimo. Impacto pode variar e levar tempo; não há prazo garantido ou primeira posição automática.

Localizadores: funcionamento, prazo de efeito, conteúdo interessante/útil e vocabulário do leitor. Não foi feita consulta SERP de um cliente.

### S03 — Elegibilidade técnica não é garantia de indexação

[Requisitos técnicos do Google Search](https://developers.google.com/search/docs/essentials/technical), Google Search Central. Rodapé: revisão 18/12/2025. Documento acessado.

Requisitos mínimos: Googlebot não bloqueado, resposta HTTP de sucesso e conteúdo indexável. A página explicita que atendê-los não garante indexação. Robots.txt impede rastreamento, mas uma URL pode aparecer sem seu conteúdo; para impedir indexação, `noindex` precisa ser acessível ao crawler. **Aproveitar** distinção crawl/index e diagnóstico de bloqueio/resposta/conteúdo. **Adaptar** às URLs que devem realmente aparecer. **Descartar** “200 significa indexado”, usar robots como proteção de informação privada ou exigir indexar toda URL do site. Relatórios/inspeção servem como evidência quando acessíveis, não dados que a skill pode inventar.

Localizadores: requisitos, Googlebot, status e conteúdo indexável. Nenhuma URL de cliente inspecionada.

### S04 — Canonicalização exige coerência entre sinais

[Definir URL canônica](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), Google Search Central. Rodapé: revisão 10/07/2026. Texto acessado.

Descreve redirecionamentos e `rel="canonical"` como sinais fortes e sitemap como sinal mais fraco para páginas duplicadas/muito semelhantes. Recomenda coerência entre métodos e links internos; desaconselha robots/removal/noindex como mecanismos de canonicalização. **Aproveitar** verificar intenção e evidência antes de alterar sinais. **Adaptar** ao CMS e comportamento real das URLs. **Descartar** canonical como comando garantido, duplicata como penalidade automática ou canonicalizar paginações/categorias distintas só porque parecem semelhantes. A escolha do Google pode divergir da preferência declarada; corrigir isso exige investigação, não substituição cega.

Localizadores: métodos/sinais, motivos, práticas e comparação. Não houve mudança ou validação de código em site real.

### S05 — Queda pede segmentação e hipóteses alternativas

[Diagnosticar quedas de tráfego](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops), Google Search Central. Rodapé: revisão 10/12/2025. Texto acessado.

Considera problemas técnicos, atualizações, sazonalidade/interesse, migração e anomalias de dados. Recomenda comparar períodos equivalentes, consultas, URLs, país, dispositivo e tipo de busca. Pequenas oscilações podem não exigir mudanças radicais. **Aproveitar** isolamento da queda e verificação das causas com dados. **Adaptar** período ao negócio e maturação. **Descartar** chamar toda queda de penalidade/core update, presumir causalidade por proximidade temporal ou reescrever o site inteiro antes do diagnóstico. Gráfico ilustrativo não determina causa sozinho. Trends pode orientar hipótese de demanda, sem fornecer as vendas do cliente.

Localizadores: causas, padrões, comparação/períodos e páginas afetadas. Não foram consultados dados da conta ou situação atual de atualização específica.

### S06 — Métricas Search Console têm definição/contexto

[Relatório de desempenho: visão geral](https://support.google.com/webmasters/answer/7576553), Google Search Console Help. Sem data de publicação/revisão visível. Página acessada.

Define cliques, impressões, CTR e posição média e dimensões como consulta, página, país, dispositivo e tipo de apresentação. Resultados de uma busca manual podem diferir por tempo, local, dispositivo e histórico; posição média é agregada. **Aproveitar** comparação com filtros/definições e cuidado ao diagnosticar médias. **Adaptar** à pergunta e exportação realmente disponível. **Descartar** rank manual como verdade universal, média do site como posição de toda página ou CTR como prova de venda. O relatório descreve desempenho em busca; métricas comerciais exigem fonte/definição própria. Não foram verificadas todas as limitações de API/exportação nesta frente.

Localizadores: métricas, dimensões, período e tipo de busca. Conta/autenticação e dados reais não acessados.

### S07 — Dados estruturados: sintaxe, qualidade e elegibilidade

[Diretrizes gerais de dados estruturados](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), Google Search Central. Rodapé: revisão 10/07/2026. Texto acessado.

Exige informação relevante, atual e representativa do conteúdo visível, além de requisitos técnicos e específicos da feature. Rich Results Test captura erros técnicos, mas não todos os problemas de qualidade. Marcação correta não garante apresentação. A ação manual específica de structured data pode afetar elegibilidade de rich result, sem alterar ranking web. **Aproveitar** tipo pertinente/conteúdo real e verificação técnica/qualitativa. **Adaptar** a feature ainda suportada e ao CMS. **Descartar** schema como boost garantido, avaliações inventadas ou validação de sintaxe como prova de resultado. Definição de vocabulário não garante suporte do mecanismo.

Localizadores: garantia/qualidade, formatos e conteúdo. Nenhum schema foi gerado/instalado ou Rich Results Test executado em cliente.

### S08 — Busca local depende de dados reais e contexto geográfico

[Melhorar presença local no Google](https://support.google.com/business/answer/7091?hl=en), Google Business Profile Help. Sem data de publicação visível. Texto acessado.

Orienta informação completa/correta, verificação, horários/categoria, fotos e feedback. Explica relevância, distância e proeminência; não há como pagar/pedir melhor ranking local. **Aproveitar** consistência entre oferta/localização real e necessidade do usuário. **Adaptar** às condições e recursos do negócio/perfil. **Descartar** promessa de dominar o mapa em qualquer local, reviews artificiais ou inventar endereço/área para ampliar alcance. Resultados locais não são a mesma superfície que a posição de um artigo. Recursos de estoque dependem de elegibilidade regional; não se presume disponibilidade.

Localizadores: informações do perfil e fatores de ranking. Nenhuma conta, verificação ou edição foi realizada.

### S09 — E-commerce: URLs representam conteúdo e variantes

[Estrutura de URLs para e-commerce](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites), Google Search Central. Rodapé: revisão 10/12/2025. Texto acessado.

Explica riscos de múltiplas URLs para mesmo conteúdo, mudanças contínuas de parâmetros e fragmentos para conteúdos diferentes. Recomenda estrutura coerente, URLs distintas para paginação e consistência de links/sitemap/canonical. **Aproveitar** mapear comportamento real de categoria/produto/variante antes de tratar duplicatas. **Adaptar** à plataforma existente, que pode já resolver parte das regras. **Descartar** redesenho preventivo de URLs ou bloquear filtros/paginação sem compreender conteúdo e objetivo de indexação. A recomendação não estabelece que toda variante deva ter página independente nem dispensa requisitos específicos de produtos.

Localizadores: estrutura importa, boas práticas e consistência. Não foram auditados catálogo/checkout ou recursos de Merchant Center.

### S10 — Recursos de Search mudam; templates precisam acompanhar

[Atualização sobre simplificação dos resultados](https://developers.google.com/search/blog/2025/11/update-on-our-efforts), John Mueller / Google Search Central. Publicação 05/11/2025. Texto do anúncio acessado.

Informa retirada gradual de features de pouco uso e mudança de suporte de tipos nos relatórios/API Search Console a partir de janeiro/2026, remetendo ao changelog para ações específicas. **Aproveitar** confirmar recurso atual antes de recomendar markup/relatório. **Adaptar** atualização de referências à tarefa concreta. **Descartar** tabela permanente de tipos “bons para SEO”, importar listas de terceiros ou assumir que remoção de feature significa queda de ranking. Esta frente não conferiu cada tipo retirado; não entrega inventário completo de deprecações.

Localizadores: corpo do anúncio e link de changelog. Não foram realizadas migrações de schema ou automações de atualização.

## Como escolher abordagem e prioridade

Proposta de avaliação derivada das fontes, sem importar checklist de cem itens:

1. **Definir resultado/página:** descoberta útil, contatos, compra, agendamento ou outra finalidade. Conhecer oferta/público e páginas relevantes.
2. **Verificar estado dos dados:** público HTTP/HTML disponível, relatórios fornecidos ou autenticação real. Declarar lacunas e o que foi acessado.
3. **Separar camadas:** a página pode ser acessível e não indexada; indexada e pouco exibida; exibida e pouco clicada; clicada e pouco útil comercialmente. Cada camada pede evidência diferente (S03, S05–S07).
4. **Hipótese e ação:** observação sustentada, explicação possível, evidência que falta, menor ação/teste que resolve. Prioridade acompanha alcance, impacto plausível, esforço/dependência e confiança.
5. **Entrega e acompanhamento:** recomendação executável, responsável, validação, risco e período/contexto de observação. Corrigido no código não significa recrawled/indexado ou melhor em SERP.

Bloqueio comprovado de páginas comerciais importantes pode preceder novas pautas. Falta de ranking sem bloqueio exige avaliar pergunta/página, conteúdo e contexto, sem supor problema técnico. Mudança visual de snippet pode não resolver queda de demanda. A ordem deve ser justificada pelo caso, não por roteiro universal.

### Intenção e conteúdo sem volume inventado

Usar pergunta/tarefa do usuário, vocabulário real, oferta e evidência de busca quando acessível. Separar temas candidatos de termos com dados. Uma sugestão do modelo não é keyword pesquisada; autocomplete ou SERP observada não fornece volume exato. Quando não há dados, pode produzir hipóteses/briefing e explicar como conferir prioridade.

Uma página deve responder algo que consegue entregar: serviço local, categoria, comparação, instrução ou produto. Identificar conteúdo existente antes de multiplicar páginas. Alternativas e FAQs devem resolver dúvidas, sem repetir frase-chave mecanicamente. O método de observar finalidade e lacunas é proposta nossa; não se atribui ao Google uma taxonomia rígida de intenção ou fórmulas de word count.

### Dados faltantes e conclusões honestas

Sem Search Console, uma revisão pública pode ver resposta/HTML/link ou conteúdo acessível, mas não conhecer canonical escolhida pelo Google, histórico de desempenho da conta ou razões internas de não indexação. Sem Analytics/CRM, não afirmar conversão/receita. Sem login do perfil, não afirmar verificação/insights privados de Business Profile.

Um diagnóstico deve separar verificado, hipótese e pendente. Se uma ferramenta necessária faltar no ambiente, registrar a opção de preparação/instalação para execução futura no momento pertinente; não declarar instalada, executar instalador externo ou substituir sua saída por números imaginários. Documentação pública e dados exportados pelo usuário podem bastar em muitos pedidos.

### Validação não termina no parser

Para correção técnica, conferir resultado implantado e comportamento relevante quando execução estiver autorizada; recrawl/inspeção e observação posterior são estados diferentes. Para structured data, validar sintaxe e conteúdo real, depois reconhecer que elegibilidade não garante display. Para conteúdo, revisão de fato/clareza/necessidade e avaliação de desempenho são etapas distintas.

Indexação e desempenho requerem observação do mecanismo, não apenas teste do HTML. Resultado comercial requer evento/fonte apropriados. Este dossiê não define um prazo padrão para melhorar posições, nem promove índices de ferramentas como verdade de negócio.

## Matriz de qualidade dos componentes

Heurísticas propostas para comparar arquivos de skills, não notas preditivas de ranking.

| Componente | Sinal útil | Falha material | Base |
|---|---|---|---|
| Escopo/contexto | Pergunta, negócio, páginas e objetivo; reaproveita dados | Auditoria universal antes de pedido simples; posição como único objetivo | S01, S02 |
| Research/keywords | Distingue hipótese, dado e finalidade de página | Volume/competição inventados, benchmark sem região/data | S02, S06; proposta de rastreabilidade |
| Técnico | Diferencia crawl/index, status, bloqueio e conteúdo | Robots tratado como noindex; 200 como garantia | S03 |
| Canonical | Verifica duplicata e coerência de sinais, CMS e objetivo | Canonical cego para toda URL; noindex para consolidar | S04, S09 |
| Queda | Segmenta período/páginas/consultas e hipóteses | Toda queda vira penalidade; correlação temporal como prova | S05, S06 |
| On-page | Resposta clara, conteúdo próprio, títulos/links pertinentes | Densidade/palavras fixas, páginas repetidas por sinônimo | S01, S02 |
| Structured data | Tipo atual, fatos visíveis e validação técnica/qualitativa | Schema obrigatório em tudo; nota sintática promete rank | S07, S10 |
| Local | Dados reais e contexto de localização/relevância | Promessa de mapa, endereços/reviews fictícios | S08 |
| E-commerce | Categoria/produto/variante/paginação mapeados | Alteração em massa sem compreensão de URLs/estoque | S09 |
| Plano/avaliação | Evidência, prioridade, dependência e estados de validação | Nota de auditoria sem ação; cliques viram receita | S03, S05–S07 |

## Três fixtures fictícios PT-BR

Exemplos autorais de diagnóstico, não dados reais ou recomendações de alteração já autorizadas.

### A. Site institucional com queda após atualização

Contexto fictício: o time relata “caiu pela metade” depois de atualizar o site; envia apenas print do analytics de uma semana. Não há Search Console, comparação anual, URLs afetadas ou histórico de mudanças.

**Resposta adequada:** separar se a queda refere-se a tráfego total, orgânico, cliques Search ou eventos; confirmar período/instrumentação. Propor comparar consultas/páginas/dispositivo e datas equivalentes no Search Console, revisar sinais técnicos de URLs importantes e contexto de migração/anomalia/demanda. O diagnóstico inicial permanece hipótese, sem “Google penalizou”.

**Formato útil:** tabela do que se sabe, hipótese, evidência necessária e prioridade de investigação. Uma revisão pública não deve inventar o relatório privado. Não pedir apagar páginas ou criar vinte artigos sem identificar camada afetada.

**Qualidade a testar:** não trata média/print como causa; preserva WIP e distingue correção implantada de recuperação observada. Reprovado: atribuir ao core update por proximidade temporal ou prometer recuperação em sete dias.

### B. Loja de móveis com categorias, filtros e variantes

Contexto fictício: produto tem URLs com parâmetros de cor e ordenação, categoria paginada e várias URLs mostrando o mesmo item. O cliente não sabe o que sua plataforma configura para canonical. Não há crawl realizado.

**Resposta adequada:** mapear exemplos e comportamento real, intenção de cada URL e seleção no CMS; verificar sinais disponíveis antes de recomendar. Conjunto duplicado pode pedir coerência de canonical/links/sitemap; conteúdo distinto de categoria/paginação não deve ser apagado por semelhança visual. Markup de produto só usa dados reais/visíveis e requisitos atuais da feature.

**Formato útil:** mapa de tipos de URLs com intenção, evidência, hipótese, ação por tipo e validação proposta. Evitar receita de bloquear todos os filtros ou trocar toda estrutura. Se a plataforma já resolve, não adicionar mecanismos duplicados.

**Qualidade a testar:** diferencia parâmetro de duplicação comprovada; não confunde schema válido com rich result exibido. Reprovado: canonicalizar todas as páginas para a home, inventar avaliações ou declarar produto indexado a partir de HTTP 200.

### C. Oficina local que atende um município

Contexto fictício: oficina relata que não aparece em buscas de bairros distantes; perfil e página pública existem, mas estado de verificação/dados de desempenho não foram fornecidos. Objetivo: receber contatos pertinentes dentro da capacidade real.

**Resposta adequada:** conferir informação pública real e o que falta saber do perfil; distinguir relevância, distância e proeminência. Página deve explicar serviço/localização/condições reais, com próxima ação clara. Não fabricar atendimento em cidades onde a oficina não opera, nem criar endereço ou reviews.

**Formato útil:** pendências por superfície (site e perfil), páginas/serviços pertinentes, ação recomendada com evidência e medida de contatos qualificados quando fonte estiver disponível. Aparição de uma busca manual fora da área não demonstra ranking fixo da empresa.

**Qualidade a testar:** respeita geografia e dados reais; não garante primeiro lugar no mapa nem confunde pagamento em anúncios com posição orgânica.

## Avaliação em uso real

O relatório deve permitir verificar uma recomendação: observação, URL/relatório, data e filtro, fonte técnica aplicável, hipótese e ação. Cobertura do checklist não é impacto. Prioridades devem explicar por que a mudança importa e quais dados podem alterá-las.

Revisar resultado contra a autorização: diagnóstico e plano não equivalem a alterações do site, publicação de conteúdo, contratação de ferramenta ou mudanças de perfil. A skill pode entregar briefing para Criador/Copywriter e tarefas técnicas para implementação; esses handoffs precisam especificar finalidade e aceitação sem alegar execução.

Para medir, manter comparações e definições estáveis, contextualizar sazonalidade/tipo de busca e mudanças simultâneas. Search Console registra desempenho em Search; contatos/vendas precisam fonte comercial e definição. Uma variação antes/depois não isola automaticamente efeito de SEO. Registrar implementação, verificação técnica, reprocessamento pelo mecanismo e resultado observado separadamente.

## Vídeos e materiais recentes oficiais

Nenhum audiovisual foi reproduzido; nenhuma transcrição integral foi recuperada. A shortlist não fundamenta procedimentos ausentes dos documentos acima.

| Material / autoria e canal | URL | Data disponível | Acesso nesta frente | Limite |
|---|---|---|---|---|
| Search Console, AI, and HTTPs updates Search Console (Q4 ’25) / John Mueller, Google Search Central | [YouTube](https://www.youtube.com/watch?v=o0AGWPU96TQ) | 17/11/2025 no resultado de busca | Metadata/descrição do resultado; página de vídeo throttled | Candidato; sem recomendação extraída do conteúdo audiovisual |
| Google Search News, edição abril/2026 / Google Search Central; título exato não recuperado | [YouTube](https://www.youtube.com/watch?v=hBUuXgR-PSw) | Mês da edição na descrição; data absoluta não confirmada | Metadata/descrição de busca; vídeo throttled | Candidato recente, sem alegar conteúdo integral avaliado |
| Trilhas oficiais de fundamentos e SEO técnico / Daniel Waisberg, Google Search Central | [Anúncio original](https://developers.google.com/search/blog/2026/10/seo-learning-paths) | 06/10/2026 | Texto do anúncio e links das duas playlists; playlists throttled | Reorganiza vídeos de várias épocas; anúncio de 2026 não implica vídeos novos |

O anúncio das trilhas distingue fundamentos/medição e temas técnicos avançados. Serve como biblioteca para dúvidas específicas, não como obrigação de APIs/crawl budget/rendering avançado em todo site pequeno. Não se pode declarar assistida a playlist nem técnico validado pelo anúncio.

## Lacunas e fronteiras

1. Nenhum site real foi auditado, alteração implantada ou resultado de conta medido. Fixtures e docs não comprovam execução da futura skill.
2. Pesquisa aprofundada concentra Google. Regras Bing, vocabulário schema.org, acessibilidade W3C e outras superfícies não foram auditados nesta frente; ampliar só se o pedido exigir, sem aplicar automaticamente conclusões Google.
3. Renderização JS, hreflang, facetas, performance/CWV, produtos/merchant e migrations complexas têm requisitos próprios. Não declarar cobertura integral a partir das páginas introdutórias consultadas.
4. Tipos/relatórios de rich results mudam. O anúncio S10 alerta sobre atualização, mas não substitui a documentação vigente da feature específica. Sem recursos antigos apresentados como válidos por inércia.
5. Não há dados locais de demanda/volume, perfil, tráfego ou conversão. Ferramentas/dependências não foram presumidas instaladas e vidIQ permaneceu sem uso.
6. Núcleo recomendado: objetivo/escopo, evidência, diagnóstico por camada, prioridades e validação. Referências sob demanda: intenção/on-page, técnico/canonical, queda/GSC, local, e-commerce/dados estruturados. Bibliografia e histórico ficam no dossiê.

Estado desta frente: dez fontes aprofundadas oficiais, incluindo uma reutilizada da mesma sessão; dossiê local, sem commit, pacote/índice alterado ou publicação externa. Demais edições preservadas.
