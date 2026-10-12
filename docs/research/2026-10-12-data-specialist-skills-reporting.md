# Especialista em Dados — pesquisa de gráficos, relatórios e entregas

Pesquisa consultada em 12/10/2026. Esta frente resolve a passagem de análise para comunicação de decisão: seleção do gráfico, relato acionável, dashboard quando necessário, dados de apoio e QA. Estatística, SQL e diagnóstico aprofundado pertencem à frente complementar. Não foi criada, instalada ou executada nenhuma skill; não houve artefato de negócio, chamada paga, conta, publicação ou alteração do catálogo.

## Conclusão aplicável

A melhor combinação é um contrato pequeno de conclusão → evidência → gráfico adequado → implicação → limite/próximo passo, com referências acionadas pela entrega. OpenAI oferece o contrato mais explícito de relatório e QA; Anthropic oferece caminhos locais mais simples para gráficos e HTML; wshobson dá modelos de comunicação úteis. Nenhuma dessas fontes deve ser copiada inteira: há acoplamento a runtime, prescrições excessivas, divergências e erros nos exemplos.

O trabalho de Dados deve preservar a conclusão e sua sustentação. Não exigir dashboard, história de três atos, hipótese confirmada, quantidade fixa de KPIs ou relato longo para todo pedido. Uma resposta curta com gráfico pode ser a entrega correta. A ausência de evidência pode levar a uma conclusão inconclusiva e a um próximo teste, sem fabricar causa ou ação.

## Alcance, seleção e procedência

Descoberta por skills.sh e busca web: `data storytelling visualization report`, `dashboard reporting data analysis`, fontes Anthropic e orientação profissional de comunicação estatística. Os resultados deram variedade suficiente para resolver formato, interpretação, dependências e QA; a busca parou por suficiência, sem quota. Instalações e estrelas ajudaram apenas a encontrar candidatas; não foram usadas como prova de qualidade.

Foram lidos integralmente **11 SKILL.md de 5 repositórios originais**: OpenAI (3), Anthropic (3), wshobson (2), AntV (2), lyndonkl (1). Dez contribuem à comparação principal; o segundo AntV é um contraste técnico de entrega por API. São cinco famílias autorais, não onze evidências independentes. OpenAI compartilha a família consultada pela frente analítica e deve ser contado uma vez na consolidação. O repositório arquivado `openai/role-specific-plugins` não foi contado como fonte adicional. O resultado antigo `narrative-text-visualization` de skills.sh corresponde hoje a `antv-t8-ntv`: conferir a origem atual evitou contar ambos.

GitHub API sem credenciais respondeu com rate limit. A obtenção de fontes ocorreu com clones rasos somente para leitura, sem instalar dependências ou rodar scripts. Cada URL abaixo fixa o SHA recuperado; as datas são do último commit do checkout, **não** prova da última edição de cada skill nem publicação original.

| Família / autoria verificável | SHA e data do checkout | Originais lidos | Licença consultada / decisão |
|---|---|---|---|
| OpenAI, `openai/plugins` | `0722921d5542fc593105c27bd52630babd8b8c2a`, 08/10/2026 | [build-report](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/build-report/SKILL.md), [build-dashboard](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/build-dashboard/SKILL.md), [visualize-data](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/data-analytics/skills/visualize-data/SKILL.md) | Não encontrado LICENSE na raiz, no plugin data-analytics ou nessas skills; frontmatter sem licença. Aprender método com atribuição; não redistribuir texto/código sem resolver permissão. Licenças de outros plugins não cobrem este por inferência. |
| Anthropic, `anthropics/knowledge-work-plugins` | `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06`, 11/10/2026 | [data-visualization](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/data-visualization/SKILL.md), [create-viz](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/create-viz/SKILL.md), [build-dashboard](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/skills/build-dashboard/SKILL.md) | [data/LICENSE](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/data/LICENSE) lido: Apache-2.0. Preservar licença/avisos e identificar modificações se reutilizar conteúdo. É outro pacote; não aplicar a ele a licença source-available de docx/pdf/xlsx/pptx de `anthropics/skills`. |
| Seth Hobson / `wshobson/agents` | `46891e7e60da0e52baf1050b7b6391b64e84c6d9`, 04/10/2026 | [data-storytelling](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/business-analytics/skills/data-storytelling/SKILL.md), [kpi-dashboard-design](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/plugins/business-analytics/skills/kpi-dashboard-design/SKILL.md) | [LICENSE](https://github.com/wshobson/agents/blob/46891e7e60da0e52baf1050b7b6391b64e84c6d9/LICENSE) lido: MIT, copyright 2024 Seth Hobson; preservar aviso se copiar porções substanciais. |
| AntV Visualization Team | `a105fa12a9fa41fccccc2eba7f4b34973628f5d3`, 22/09/2026 | [antv-t8-ntv](https://github.com/antvis/chart-visualization-skills/blob/a105fa12a9fa41fccccc2eba7f4b34973628f5d3/skills/antv-t8-ntv/SKILL.md), [chart-visualization](https://github.com/antvis/chart-visualization-skills/blob/a105fa12a9fa41fccccc2eba7f4b34973628f5d3/skills/chart-visualization/SKILL.md) | [LICENSE](https://github.com/antvis/chart-visualization-skills/blob/a105fa12a9fa41fccccc2eba7f4b34973628f5d3/LICENSE) lido: MIT, copyright 2025 AntV Visualization Team. Isso não confirma licença/disponibilidade/custo do serviço remoto nem de todas as dependências. |
| `lyndonkl/claude`, autoria atribuída ao mantenedor; sem identidade legal inferida | `4acc337d4dbdb19da6469eb2504c16669c1cafa1`, 22/08/2026 | [visualization-choice-reporting](https://github.com/lyndonkl/claude/blob/4acc337d4dbdb19da6469eb2504c16669c1cafa1/skills/visualization-choice-reporting/SKILL.md) | README diz uso livre/open source com Claude Code, porém não foi encontrado LICENSE padronizado nem licença no frontmatter. Permissão genérica não resolve redistribuição comercial em outro runtime. Consultar método; não copiar pacote. |

### Recursos que determinaram o julgamento

- OpenAI: `build-report/specifications/executive-report.md`, `technical-report.md` e `build-dashboard/specifications/html-dashboard.md` integralmente; `build-report/scripts/deliver_portable_artifact.mjs` integralmente; `plugins/data-analytics/package.json` integralmente. Inspeção dirigida de `src/analytics-app-core.md`, `verify_portable_artifact.mjs` e `build_portable_artifact.mjs` por termos de empacotamento, navegador, fonte e credenciais. Não houve auditoria integral dos grandes renderers ou contrato MCP.
- wshobson: os dois `references/details.md` integralmente, incluindo exemplos SQL, Python, templates e números ilustrativos. Não rodados.
- AntV: ambas as skills carregam sua implementação decisiva no próprio Markdown; links externos da biblioteca T8 não foram auditados integralmente. A alegação `<20KB` é do autor, não medição desta pesquisa.
- lyndonkl: `resources/methodology.md` integralmente; template e rubric JSON tiveram inspeção parcial, incluindo instruções de audiência/acessibilidade e falhas. Não são apresentados como auditoria integral do pacote. A matriz usa apenas o núcleo e metodologia, cuja leitura foi completa.
- Anthropic: `data/CONNECTORS.md` e `data/LICENSE` integralmente; os gráficos e dashboard têm padrões decisivos dentro dos três SKILL.md, lidos completos. Não houve instalação de conectores.

## Comparação de abordagens

| Abordagem | Contribuição concreta | Bom encaixe | Limite observado |
|---|---|---|---|
| OpenAI report | Espinha da conclusão antes do renderer; cada conclusão com evidência, interpretação, caveat e implicação; relatório executivo e técnico distintos | Documento durável, leitura por pessoas sem contexto do chat | Grande carga de instruções; obriga superfície, schema e publicação automática em Work Mode; não portável diretamente ao Studio |
| OpenAI visualization | Pergunta determina família; grão, denominador e suficiência antes de plotar; revisão no recipiente final; dados de apoio mais ricos que x/y | Gráficos analíticos e múltiplos gráficos coerentes | Regras de paleta/marca e limiares numéricos específicos viram ritual se transplantados; runtime MCP/GenUI obrigatório não é ferramenta Hermes confirmada |
| OpenAI dashboard | Fonte autoritativa, reconciliação entre cartões/gráficos/tabelas, resumo→drivers→detalhe; snapshot explicitamente diferente de live | Exploração e acompanhamento de métricas | Descoberta de todas as fontes e implantação Sites por padrão pode aumentar custo/escopo; usar só fontes pertinentes e destino autorizado |
| Anthropic visualization / create-viz | DataFrame→Matplotlib/Seaborn estático ou Plotly interativo; código reproduzível, escalas e acessibilidade | Arquivos CSV ou dados colados; PNG/SVG ou HTML solicitado | Snippets demonstram padrões, não provas; imagem PNG sempre não serve a todo destino; dual axis sugerido em create-viz conflita com cautela da skill de visualização |
| Anthropic dashboard | Um arquivo HTML, dados embutidos, filtros compartilhados, tabela e CSS para impressão | Snapshot local fácil de abrir | Promessa offline conflita com CDN Chart.js/date adapter; exemplos incompletos e renderTable usa HTML sem escape. Exige correção antes de reutilizar |
| wshobson storytelling | Conclusão primeiro, comparação, anotação, narrativa curta, próximo passo; modelos trend/comparison/problem-solution | Relato de resultado comercial ou reunião | Confundir associação com causa e números ilustrativos com resultados; três atos/três pontos não podem ser obrigatórios |
| wshobson KPI | Separar métricas estratégicas/táticas/operacionais; mostrar base, meta e frequência | Contexto de KPI do usuário | Quantidades fixas, semântica vermelho/verde e infra OLAP/scheduler não devem entrar por default. SQL de exemplo contém falhas materiais |
| AntV T8 | Valores visíveis e valores originais separados; distinção entre magnitude, delta, ratio e avaliação | Relato HTML com micrográficos semânticos, se isso melhorar leitura | Exige runtime novo, anotação de tudo, mínimo de 800 palavras e apenas fontes públicas. Tudo conflita com dados internos e pedidos curtos |
| AntV API | Contrato JSON curto de tipo/dados→imagem | Contraste de implementação compacta | Envia dados a endpoint externo e depende de rede; não adotável por padrão para dados de empresa. Serviço não chamado nem preço verificado |
| lyndonkl reporting | Pergunta→perfil→forma→padrão/contexto/significado/ação; alternativa textual, fonte e timestamp | Instrução profissional simples e matriz de escolha | Não forçar ação/cause quando dados só sustentam observação; no-scroll, contagens e nota subjetiva não são gate objetivo |

## Matriz fonte → componente → decisão

| Fonte / arquivo | Componente | Decisão | Motivo e adaptação |
|---|---|---|---|
| OpenAI `build-report/SKILL.md`, executive/technical specs | Conclusão, evidência visual, interpretação, ressalva e próximo passo próximos | **Adotar conceito** | Evita despejar números; profundidade varia com pedido/audiência. Não copiar títulos ingleses obrigatórios. |
| OpenAI `build-report/SKILL.md` | Relato pode terminar em monitorar ou pergunta aberta | **Adotar conceito** | Nem toda análise justifica mudança. Evidência insuficiente deve permanecer explícita. |
| OpenAI `build-report/SKILL.md` | Preservar seções/fonte/dados numa revisão; corrigir componente afetado | **Adotar conceito** | Pedido de trocar gráfico não autoriza resumir ou apagar o relatório aprovado. |
| OpenAI `visualize-data/SKILL.md` | Pergunta e comparação determinam gráfico; alternativas para dados esparsos | **Adaptar** | Manter teste de suficiência e grão; usar 8–12/12–20 pontos como pistas, jamais quotas que autorizem ampliar período sem significado. |
| OpenAI `visualize-data/SKILL.md` | Contrato compacto do gráfico / mapa de gráficos | **Adaptar** | Guardar em notas de trabalho quando múltiplos gráficos ou leitura ambígua, não exigir arquivo formal para todo gráfico. |
| OpenAI `visualize-data/SKILL.md` | Branding, blossom, roots, quatro linhas proibidas | **Descartar** | Normas específicas da marca/runtime; famílias repetidas são aceitáveis quando perguntas e dados o justificam. |
| OpenAI root skills | Work Mode, GenUI, MCP artifact obrigatório, Sites automático | **Descartar** | Não são capacidades comprovadas do Studio; publicação é intenção distinta. Sem menus de modes para a pessoa. |
| OpenAI `deliver_portable_artifact.mjs` | Distinguir structural_only de navegador/verificação completa | **Adotar conceito** | Fonte do código identifica estados honestos de QA; não copiar renderer nem instalar runtime inteiro. |
| Anthropic `data-visualization` / `create-viz` | Matplotlib local estático vs Plotly interativo | **Adaptar** | Escolher pelo resultado, disponibilidade e benefício. Confirmar pacotes/fontes; propor instalação mínima caso ausente, sem pressupor preinstalação. |
| Anthropic `build-dashboard` | Arquivo local com dados embutidos, filtros coerentes e reconciliação | **Adaptar** | Um HTML real pode atender sem servidor. Offline só se recursos também forem locais/embutidos e isso tiver sido verificado. |
| Anthropic `build-dashboard` | Criar amostra automaticamente ao faltar dado real | **Descartar como fallback** | Dados demonstrativos só quando pedido de mockup/amostra estiver claro; falta da fonte autoritativa não vira análise fictícia. |
| Anthropic `build-dashboard` | Snippets com CDN, innerHTML e sinal→bom/ruim | **Descartar código cru** | Revisar segurança/render; alta de churn e alta de receita têm significados diferentes. Não corrigido upstream nesta pesquisa. |
| wshobson `data-storytelling` e details | Comparação/annotation/resumo comercial | **Adaptar** | Usar padrões quando esclarecem resultado. Não transformar toda entrega em pitch persuasivo. |
| wshobson `kpi-dashboard-design` e details | Fórmulas SQL, thresholds, infra de refresh | **Descartar código como base validada** | Exemplos não executados e erros detectados estaticamente; freshness/snapshot e definição de KPI são os conceitos aproveitáveis. |
| AntV `antv-t8-ntv` | Valor original/unidade/significado distintos | **Adotar conceito** | Útil para arredondamento, porcentagem e cor semântica; sintaxe T8 inteira só se houver benefício específico. |
| AntV `antv-t8-ntv` | 800 palavras, todos os valores anotados, somente fonte pública | **Descartar** | Reduz adaptabilidade, exclui dados internos e obriga saída longa. |
| AntV `chart-visualization` | POST de dados para imagem em serviço remoto | **Descartar padrão** | Desnecessário para desenho local; dados e custo teriam de ser revistos para pedido específico. |
| lyndonkl `SKILL.md` / methodology | Padrão, contexto, significado e ação; texto alternativo e tabela | **Adotar conceito com cautela** | Interpretação deve ter nível de confiança; ação opcional. Não copiar recursos sem licença resolvida. |
| lyndonkl rubric (trechos) | Acessibilidade menos crítica por uso interno / nota mínima como prova | **Descartar** | Uso interno não resolve necessidade de acessibilidade; nota subjetiva não prova cálculos, render ou conclusão. |

## Divergências e falhas que mudam a síntese

1. **Título conclusivo ou neutro.** Anthropic, wshobson e lyndonkl preferem insight no gráfico; OpenAI prefere título de gráfico neutro e argumento no texto adjacente. Ambos funcionam. Para gráfico isolado, título com conclusão **sustentada** ajuda; num relatório, evitar repetir a mesma conclusão em título da seção, gráfico e legenda. Manter métrica/unidade/período em subtítulo ou contexto acessível.
2. **História persuasiva ou cautela analítica.** O modelo problem-solution de wshobson inclui impacto/ROI e linguagem de causa; exemplos são ilustrativos. Nunca transformar retenção associada a onboarding em efeito de onboarding. Distinguir o observado, a explicação possível e o que precisaria ser testado. Um resultado negativo ou inconclusivo também deve ser comunicado.
3. **Relato vs dashboard.** Relatório responde questão com leitura linear; dashboard serve consulta/acompanhamento/exploração. Não abrir dashboard para uma resposta simples; não substituir um relatório pedido por cartões e tabelas sem interpretação. Núcleo reconhece intenção automaticamente.
4. **Arquivo local vs runtime de plugin.** OpenAI usa contrato canonical artifact mais React/Recharts/reader/MCP; Anthropic HTML reduz setup, porém CDN impede garantia offline. Adaptar a menor forma que resolve a entrega. Nenhum desses renderers foi validado no Studio.
5. **Ação e boa direção.** Anthropic `renderKPI` usa crescimento positivo como bom; isso falha em churn/custo/erros. AntV `assessment` separa julgamento de delta e é conceito útil: crescimento não equivale a benefício.
6. **Erros verificáveis na leitura.** A comparação ponderada EMEA de wshobson apresenta total 2,9; pesos e notas mostrados produzem 3,05 (APAC 4,05, que arredonda a 4,1). O exemplo CAC junta gasto mensal a cada usuário e soma o gasto repetido; a retenção agrupa o denominador pelos usuários ligados à atividade do mesmo mês, podendo igualar numerador e denominador; `EXTRACT(MONTH FROM age(...))` não é índice total de meses para intervalos acima de um ano. São constatações estáticas, sem executar skill/query. Não usar snippets como cálculo auditado.
7. **Implementação do HTML Anthropic.** Dados embutidos não tornam scripts CDN offline. `renderTable` interpola dados externos em `innerHTML`; antes de reutilizar precisaria escapar ou usar texto/DOM seguro. Se múltiplas tabelas usarem `window.sortTable`, sobrescrevem handler compartilhado. Dataset ilustrativo e métodos placeholder não constituem dashboard pronto.
8. **Gate de tamanho ou nota.** 800 palavras, 5–7 KPIs, uma tela, 3 pontos ou média ≥3,5 podem orientar exemplo, mas não provam adequação. Uma conclusão importante pode ser mais curta, e detalhes podem exigir expansão. Critério é cumprir questão, evidência e usabilidade.

## Referência profissional independente

Foi consultado [Data visualisation: charts — Government Analysis Function](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/), autoria Analysis Function Central Team, publicação visível 19/05/2022, com orientação que recebe atualizações. Acrescenta mensagem antes da forma, alternativa textual/tabela conforme finalidade, fonte exata e download dos dados representados, preferindo SVG para gráficos exportáveis. Isso sustenta **tabela de apoio e proveniência legível**, além da imagem. É orientação de publicação estatística; suas normas legais do Reino Unido não são transplantadas como exigência do produto. Não foi consultado audiovisual nem realizado teste com leitores de tela.

## Contrato recomendado para a futura skill

O núcleo deve ser curto e flexível:

1. Reconhecer pergunta/decisão/audiência e aproveitar arquivo, conversa, definições e preferência de formato já fornecidos. Perguntar apenas quando informação ausente muda materialmente análise ou entrega.
2. Fixar fonte, período, população, grão, unidades e denominadores. Separar informação real de amostra e descrever lacunas. Frente analítica valida cálculo/resultado.
3. Formular conclusão proporcional à evidência: observado, hipótese, estimativa, incerteza. Não impor confirmação, causa ou recomendação.
4. Selecionar o menor gráfico/tabela que esclarece a comparação e o menor formato utilizável que atende ao pedido. Dashboard requer necessidade de explorar/acompanhar; narrativa HTML requer benefício para leitura.
5. Produzir conclusão acompanhada de evidência, contexto e limite. Próximo passo é ação, monitoramento ou investigação quando a evidência permite; não preencher por obrigação.
6. Revisar valores contra origem e render no destino real. Preservar dados e cálculo de apoio suficientes para conferir, sem vazar dados sensíveis nem transformar a entrega num log técnico.
7. Entregar arquivo/resultado concreto, formato, data de corte, dependências relevantes e limites de verificação. Em revisão, preservar conteúdo aprovado e atualizar só o necessário.

Referências sob demanda, sem copiar acervo inteiro:

- `visualization.md`: escolha de famílias; escala, unidades, denominador, pontos/linhas esparsos, labels, comparação de painéis e acessibilidade.
- `reporting.md`: resultados comerciais ou técnicos, interpretação próxima ao gráfico, trade-offs e evidência inconclusiva; exemplos curtos sem números prometidos.
- `dashboards.md`: quando um painel ajuda, snapshot vs live, filtros, reconciliação e dados embutidos. Sem stack fixa ou arquitetura de refresh preventiva.
- `delivery-verification.md`: reconciliação de números, render/export real, tabela de apoio, metadados e estados de QA não executado/parcial/completo.

Scripts só entram se houver necessidade repetida demonstrada: por exemplo, validar totais ou verificar pacote offline. Não criar framework artifact/renderer, escolher BI, montar aplicação ou instalar biblioteca apenas para satisfazer estrutura da skill. Quando preferência recorrente ou atrito concreto justificar, oferecer adaptar a própria versão da skill, explicando a mudança e o benefício; aplicar com aceitação ou pedido. Reaproveitar definições/projeto existentes, sem transformar convenções de uma empresa em padrão público nem criar infraestrutura sem necessidade.

## Formatos e fronteiras com outras especialistas

| Pedido | Entrega de Dados | Relação com vizinhas |
|---|---|---|
| “O que aconteceu com nossas vendas?” | Conclusão, comparação por período/segmento, gráfico e caveat; relato proporcional | Arquivo XLSX pode ser fonte, não exige novo workbook |
| “Qual região priorizar?” | Critérios explícitos, evidência comparável e trade-offs; separar scoring assumido e fatos | Sem virar apresentação por padrão |
| “Quero acompanhar volume e atrasos por equipe” | Painel quando filtros/consulta recorrente ajudam; timestamp e snapshot/live claros | Não contratar infra BI para um snapshot |
| “Faça planilha com fórmulas e gráficos” | Fornece análise/definições e validação da conclusão | Especialista em Planilhas cuida workbook editável, fórmulas, estilos e recálculo |
| “Transforme resultado em apresentação” | Preserva dados, conclusões e limitações | Especialista em Apresentações cuida narrativa visual/HTML e sequência; sem diluir evidência |
| “Me dê um gráfico para compartilhar” | Arquivo gráfico legível com fonte/contexto e dados de apoio quando útil | PNG/SVG/HTML conforme destino; não força PDF/slide/dashboard |

## Dependências, custo e QA pendente

Matplotlib, Seaborn, pandas, NumPy e Plotly não foram verificados como instalados. Fontes não foram verificadas; sistema padrão é possibilidade, não promessa. OpenAI package.json declara React 19, Recharts 3, Vite 8 e playwright-core 1.61, além do core de artefatos e browser compatível. Copiar só SKILL.md não entrega esse runtime. T8 precisa JS via CDN ou biblioteca local; AntV chart API envia dados para terceiro e sua disponibilidade/preço não foram comprovados. Warehouse/BI exige fonte e acesso reais, conforme CONNECTORS Anthropic; dados colados/arquivos podem atender sem conta.

Não foi pago nada ou instalado pacote. Consulta de fontes públicas e obtenção de código não provam custo operacional futuro. Local evita custo por chamada de render externo, mas consome runtime, memória e tempo; performance depende de volume e ambiente. Referências devem oferecer preparar a dependência mínima quando faltar e quando ela trouxer benefício, ou usar formato já disponível. Não prometer “Studio já traz” nem empurrar a pessoa para setup de desenvolvedor.

**Gates futuros distintos:** conteúdo/contrato da skill; dependências preparadas; cálculo conferido; arquivo gerado; render e filtros/export verificados; pedido real executado; publicação quando pedida. Aqui só pesquisa e inspeção de fonte. Não há prova de execução dos 11 pacotes, qualidade de screenshots, segurança integral, compatibilidade Windows/Hermes, performance, instalação pela galeria ou funcionalidade ponta a ponta. Licenças indefinidas de OpenAI/lyndonkl impedem reutilização direta até resolução; métodos podem ser sintetizados em instruções originais com fontes.

As dúvidas materiais desta frente foram resolvidas: o núcleo é comunicação analítica flexível, a entrega segue intenção e evidência, e as referências detalham formato/QA. Não precisa de mais descoberta para criar a proposta posterior, depois de consolidar com a frente analítica e receber autorização de criação. Nenhum item foi incluído no catálogo; `openai/plugins`, `anthropics/knowledge-work-plugins` e os repositórios independentes não passam a ser origens permitidas de galeria pela existência desta pesquisa.
