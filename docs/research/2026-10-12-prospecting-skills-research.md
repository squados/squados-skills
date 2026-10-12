# Especialista em Prospecção — pesquisa de empresas, ICP e qualificação

Rodada 13/33. Consulta em 12/10/2026. Frente de pesquisa estática; nenhuma instalação, chamada a provedor pago, execução de código remoto, coleta real de leads, alteração de CRM ou envio. Complementa a frente de mensagens e cadência. Footprint: somente este dossiê.

## Resultado e alcance

A composição recomendada usa o roteamento por contexto e o breve de conta de Corey Haines, a pesquisa evidenciada de Browserbase e a limpeza/qualificação conservadora de ProfileSpider. Qualificação comercial confirmada depende de conversa e dados fornecidos: pesquisa pública identifica candidatos e hipóteses, não prova orçamento, autoridade de compra ou intenção.

Foram lidos integralmente **13 SKILL.md, em cinco famílias originais**: Browserbase (1), ProfileSpider (7), Zubair Trabzada (3), astDeniss (1) e Corey Haines (1). Quatro famílias têm MIT verificada; astDeniss não declara licença no arquivo e não possui licença identificada na árvore consultada. Doze skills têm cobertura MIT na família/pacote; uma permanece sem permissão de reprodução verificada. Leitura adicional: 10 recursos comportamentais decisivos (7 Browserbase; 3 Corey), quatro licenças e documentação primária de HubSpot/MEDDICC. Nenhum resultado real de execução foi medido.

Descoberta por busca web de profissão/entrega em inglês, GitHub e skills.sh; confirmação em árvores e arquivos originais. skills.sh é diretório, não segunda evidência do mesmo pacote. As quatro primeiras famílias têm `fork: false` na API; Corey foi resolvido por `git ls-remote`. Isso não prova independência de toda ideia: a referência de demand signals de Corey credita Kappaemme e a de enrichment credita eliasstravik. Essas origens reconhecidas não foram contadas como pacotes adicionais lidos.

Critério de parada: pesquisa, descoberta, qualificação, tratamento de lacunas e limpeza já tinham alternativas comparáveis suficientes. Outros candidatos descobertos — jmsktm/claude-settings (autor declarado ID8Labs), SkillMedev/skills, Linkup e signalpipe — ficaram sem avaliação integral e fora das contagens. Rate limit da API do GitHub impediu concluir metadados de SkillMedev; não reutilizar SHA/data da resposta anterior. Foram usados raws e ls-remote, sem clone ou temporários.

## Proveniência e revisão

Datas abaixo são do commit da revisão consultada, não necessariamente publicação inicial de cada skill. Toda URL de arquivo analisado fica fixada no SHA. As versões são as declaradas pelo autor.

| Família / autoria | Revisão | Data verificável | Licença e limite |
|---|---|---|---|
| [Browserbase / skills](https://github.com/browserbase/skills), Browserbase Inc. | `6811ca31163332d9d60309cff48e77f09de37a17`; company-research 1.1.0 | 02/09/2026 01:38:05 UTC | [MIT por pacote](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/LICENSE.txt), copyright 2026; repositório não tem licença única identificada |
| [SpiralCrew / ProfileSpider](https://github.com/spiralcrew-ou/profilespider-agent-skills), author ProfileSpider | `6c65d0507687364704a180476613b72467028e87`; skills 1.0 | 21/06/2026 09:34:50 UTC | [MIT](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/LICENSE), copyright 2026 SpiralCrew e frontmatter MIT |
| [astDeniss / business-skills](https://github.com/astDeniss/business-skills) | `208245b7066f1101b09fbfd728a53717a47837d4` | 09/07/2026 05:50:05 UTC | Ausente no frontmatter/árvore; consulta conceitual, não incorporar texto/templates |
| [Zubair Trabzada / ai-sales-team-claude](https://github.com/zubair-trabzada/ai-sales-team-claude) | `efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce` | 27/03/2026 02:55:20 UTC | [MIT](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/LICENSE), copyright 2026 Zubair Trabzada |
| [Corey Haines / marketingskills](https://github.com/coreyhaines31/marketingskills) | `1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff`; prospecting 1.3.0 | Data do commit não obtida; consulta 12/10/2026 | [MIT](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/LICENSE), copyright 2025 Corey Haines |

MIT exige preservar copyright e permissão quando houver cópia substancial. A pesquisa não reproduziu pacotes e não aprovou sua distribuição. Nenhuma dessas origens externas está na allowlist direta `github` atual da galeria; uma referência para autoria própria é diferente de publicar um pacote externo no índice.

## Arquivos lidos

Browserbase: [SKILL.md](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/SKILL.md), [research-patterns.md](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/references/research-patterns.md), [workflow.md](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/references/workflow.md), [example-research.md](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/references/example-research.md), scripts [extract_page.mjs](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/scripts/extract_page.mjs), [list_urls.mjs](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/scripts/list_urls.mjs), [compile_report.mjs](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/scripts/compile_report.mjs) e [package.json](https://github.com/browserbase/skills/blob/6811ca31163332d9d60309cff48e77f09de37a17/skills/company-research/scripts/package.json). O template HTML e profiles/example.json não foram lidos; auditoria do pacote completo pendente.

ProfileSpider, cada SKILL.md completo: [b2b-lead-qualification](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/b2b-lead-qualification/SKILL.md), [company-research](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/company-research/SKILL.md), [prospect-list-cleanup](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/prospect-list-cleanup/SKILL.md), [duplicate-record-review](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/duplicate-record-review/SKILL.md), [research-gap-analysis](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/research-gap-analysis/SKILL.md), [account-prioritization](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/account-prioritization/SKILL.md), [directory-research-planner](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/directory-research-planner/SKILL.md). São pacotes pequenos de Markdown; a árvore não mostrou recursos auxiliares para estes sete.

Zubair, cada SKILL.md completo: [sales-icp](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/skills/sales-icp/SKILL.md), [sales-research](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/skills/sales-research/SKILL.md), [sales-qualify](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/skills/sales-qualify/SKILL.md). Orquestrador e agentes não foram auditados.

astDeniss: [lead-qualification/SKILL.md](https://github.com/astDeniss/business-skills/blob/208245b7066f1101b09fbfd728a53717a47837d4/lead-qualification/SKILL.md), integral; perguntas e templates estão no mesmo arquivo.

Corey: [prospecting/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/prospecting/SKILL.md), [account-research.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/prospecting/references/account-research.md), [demand-signals.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/prospecting/references/demand-signals.md), [enrichment-playbook.md](https://github.com/coreyhaines31/marketingskills/blob/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff/skills/prospecting/references/enrichment-playbook.md), integrais. Referências de ferramentas, compliance, saas/b2b/local, signal-plays e sourcing-and-enrichment não foram auditadas; não afirmar conformidade jurídica ou compatibilidade operacional do pacote inteiro.

## Comparação de componentes

| Fonte / arquivo | Componente | Decisão | Motivo e adaptação |
|---|---|---|---|
| Corey prospecting | Reconhecer SaaS, B2B, negócio local ou primeiros clientes a partir da intenção | Adaptar | O contexto decide a abordagem, sem menu obrigatório. Casos híbridos usam critérios do trabalho, sem forçar quatro modos na interface |
| Corey account-research | Primeiro fatos e fontes, depois implicação/ângulo | Aproveitar | Evita o ICP do vendedor contaminar a descrição da empresa; resultado sem gancho é válido |
| Corey account-research | Breve com fit, evento datado, evidência, responsável provável e lacunas | Adaptar | Ótimo handoff à redação; papel provável não prova autoridade, e prova comercial vem do material real do usuário |
| Corey demand-signals | Dor explícita, alternativa, troca e evento como caminhos de descoberta | Adaptar | Útil sem histórico de clientes. Evidência pública indica hipótese de necessidade, não consentimento nem compra confirmada |
| Corey demand-signals | Pesos 25/25/20/15/15 e faixas numéricas | Descartar como padrão | Não foram demonstrados com resultados; explicar rubrica opcional quando comparação de lista ajudar |
| Corey enrichment-playbook | Regra de aceitação por campo; erro operacional separado de ausência | Aproveitar | Impede marcar timeout como empresa inexistente e interrompe buscas quando a necessidade já foi satisfeita |
| Corey enrichment-playbook | Cache por workspace/provedor/endpoint e métricas de crédito | Sob demanda | Bom desenho para integrações existentes; não criar infraestrutura/cache nem comprar ferramentas para uma lista pequena |
| Corey prospecting | Quantidade default, distribuição 20%/30%, skip por baixa confiança | Descartar | Quantidade não pode produzir leads fictícios; baixa evidência vira pendência de pesquisa e não incompatibilidade automática |
| Browserbase SKILL/research-patterns | Entender oferta e segmentação antes da descoberta; pesquisar por subperguntas prioritárias | Adaptar | Aproveitar materiais existentes; perguntar apenas o que muda a decisão. Profundidade acompanha dúvida e entrega |
| Browserbase SKILL/research-patterns | Descrição ligada a conteúdo acessível; não inferir negócio pela aparência/framework | Aproveitar | Proteção concreta contra alucinação e contaminação pelo ICP |
| Browserbase research-patterns | Achado com pergunta, fato, fonte e confiança | Adaptar | Acrescentar data da fonte/consulta e separar fato, hipótese e desconhecido. Fonte oficial continua podendo conter alegação promocional |
| Browserbase SKILL | Cap de score 3 para homepage inacessível | Descartar | Falta de acesso não é prova de mau fit. Manter status pendente e evidência disponível em outras fontes |
| Browserbase SKILL/workflow | Perfis persistidos dentro da própria skill, revisão obrigatória, seis subagentes, orçamento fixo de chamadas | Descartar | Acopla cliente ao pacote, multiplica confirmações e custo; contexto da conversa e recursos disponíveis bastam |
| Browserbase SKILL/workflow | Fórmula de queries, volume 25/50/100, descarte previsto 50–70% | Descartar | Estimativas não demonstradas. Reportar apenas empresas efetivamente verificadas e déficit explicado |
| Browserbase extract_page | Metadados+texto visível e fallback para página dinâmica | Adaptar como técnica | Melhora pesquisa de sites com pouco HTML. CLI/API obrigatórios não são assumidos no Studio; usar pesquisa/navegador disponíveis |
| Browserbase list_urls | Deduplicar hostname normalizado | Adaptar | Domínio é boa pista, mas grupos, marcas e filiais podem compartilhar domínio; identidade antes de fusão |
| Browserbase compile_report | CSV e breve por empresa | Aproveitar formato | Entrega editável e rastreável; não exige HTML/report builder. Script usa parser simplificado e dedupe pelo nome retendo maior score, o que pode apagar conflitos |
| Browserbase compile_report | Abrir resultado por comando `open` e remover arquivos de lote global | Descartar | `open` não é portátil Windows e limpeza ampla pode tocar trabalho alheio. Nenhum script adotado |
| ProfileSpider b2b-lead-qualification | Critérios uniformes, evidência, campos ausentes e próximo passo | Aproveitar | Pequeno e conservador, sem enriquecimento fictício; fit explicitamente diferente de intenção |
| ProfileSpider company-research | Resumo comparável a partir de dados fornecidos | Adaptar | Funciona sem web; fontes disponíveis delimitam conclusão. Permitir enriquecer quando pedido e ferramentas presentes |
| ProfileSpider prospect-list-cleanup | Normalização com valor original, notas e contagens | Aproveitar | Não elimina registros defeituosos nem inventa campos; preparar lista não equivale a verificar seus dados |
| ProfileSpider duplicate-record-review | Grupos prováveis, chaves, conflitos e revisão da fusão | Aproveitar | Evita tratar nomes iguais como entidade certa. Escolha de sobrevivente considera fonte/atualidade, além de completude |
| ProfileSpider research-gap-analysis | Lacuna ligada à decisão e fonte sugerida | Aproveitar | Pesquisa orientada pelo impacto; não coletar campos inúteis |
| ProfileSpider account-prioritization | Prioridade com justificativa, risco e próximo passo | Adaptar | Classificação pode ser qualitativa; score sem calibração não vira probabilidade de fechar |
| ProfileSpider directory-research-planner | Traduzir ICP em fontes, consultas e inclusão/exclusão | Aproveitar | Ajuda descoberta; a própria skill admite que plano não comprova existência/acesso das fontes |
| astDeniss lead-qualification | ICP de clientes ganhos/perdidos e dois eixos fit/engajamento | Usar conceito, não texto | Licença não verificada; conceitos confirmados independentemente e úteis para evitar atividade compensar incompatibilidade |
| astDeniss lead-qualification | Defaults ACV, volume, CRM, estrutura SDR/AE, conversão e SLA | Descartar | Inventa contexto operacional. Exemplos/benchmarks não são dados do usuário nem regra universal |
| astDeniss lead-qualification | BANT/CHAMP/MEDDPICC escolhidos pelo ciclo/complexidade | Adaptar conceito | Perguntas de descoberta sob demanda; não transformar pesquisa de empresa em sistema RevOps completo |
| Zubair sales-icp | ICP positivo/negativo, critério pesquisável e manutenção por resultados | Adaptar | Justificar atributos e hipóteses. Não fabricar receita, idade/persona ou oito desqualificadores para preencher seção |
| Zubair sales-icp | Uma pergunta no máximo; 300–400 linhas obrigatórias; todas as dimensões sempre | Descartar | Rigidez aumenta custo e pode deixar lacuna material sem esclarecimento; entrega proporcional ao pedido |
| Zubair sales-research | Fontes por campo, atualidade e sinal→implicação | Adaptar | Prioridade depende da natureza da afirmação. Dimensões escolhidas pelo ICP, não oito seções obrigatórias |
| Zubair sales-research | Receita por empregado, funding, clientes estimados, tráfego/conversão; saúde por contratação | Descartar | Proxies não provam receita, caixa ou orçamento; ausência deve permanecer explícita |
| Zubair sales-qualify | Evidência/confiança por componente e informações para próxima conversa | Adaptar | Útil como roteiro de validação, sem classificar autoridade/necessidade como confirmadas só pelo cargo/blog |
| Zubair sales-qualify | Score BANT+completude MEDDIC+urgência determina SQL e ciclo de venda | Descartar | Mistura observabilidade com qualidade e cria falsa precisão; nenhum histórico valida pesos ou prazos |

## Métodos profissionais confirmados em fonte primária

O [lead scoring da HubSpot](https://knowledge.hubspot.com/scoring/understand-the-lead-scoring-tool), consultado em 12/10/2026, distingue propriedades de fit e eventos de engajamento e permite analisá-los separadamente ou em combinação. Logo, preservar eixos é uma escolha metodológica útil; afirmar que nenhuma combinação é permitida seria exagero da skill astDeniss. A documentação também descreve limites, decay e teste/preview conforme recursos e assinatura. Não implica integração ou assinatura disponível no Studio; não foram operadas contas.

A [explicação da MEDDICC](https://meddicc.com/meddpicc-sales-methodology-and-process), consultada em 12/10/2026, situa o método em vendas complexas com múltiplos envolvidos. Economic buyer é autoridade de compra; champion precisa de poder/influência/credibilidade. Encontrar um título executivo ou pessoa na equipe não confirma essas funções para o negócio específico. Esta é uma inferência metodológica da pesquisa para rejeitar qualificação excessiva do pacote Zubair.

Não se confirmou, por evidência de execução, superioridade de qualquer score, taxas de descarte, conversão, cobertura de ferramentas, ganho de produtividade ou prazo de fechamento apresentado pelas skills. Não serão repetidos como promessa.

## Proposta para a síntese posterior

Núcleo curto: reconhecer se o pedido é definir público, encontrar empresas, pesquisar conta, priorizar lista, limpar export ou preparar passagem para comercial. Reusar oferta, ICP e materiais atuais; se faltarem critérios essenciais, perguntar focadamente. Construir ICP provisório quando não há histórico e rotular sua natureza. Separar **fonte/data, fato, hipótese, desconhecido, aderência e próximo passo**. Fit não é intenção; sinal datado não é consentimento nem orçamento confirmado.

Descoberta: fontes e consultas apropriadas à geografia/setor; resolver identidade, pesquisar o que muda decisão e parar quando suficientemente sustentado. Não prometer encontrar exatamente N; declarar contagem real e por que faltou. Contas sem evidência ficam pendentes, com próximo caminho de pesquisa. Preservar critérios e exclusões já aceitos, sem formulário rígido.

Referências sob demanda: ICP e descoberta; sinais e breve de conta; critérios de qualificação para conversa; lista/normalização/duplicidade; handoff e enriquecimento. A frente de cold-email assume redação/cadência, evitando duplicar conteúdo. BANT/MEDDPICC não precisam ocupar o caminho padrão de uma pesquisa rápida.

Entregas: tabela curta quando suficiente; arquivo editável quando pedido ou quando a lista exige. Colunas proporcionais ao trabalho: identidade/domínio, critério atendido, fonte/data, sinal observado, hipótese, desconhecido, prioridade e próximo passo. Separar eventual canal público e status de verificação; não inventar endereço ou inferir entregabilidade. Nenhum contato foi coletado nesta pesquisa.

Ferramentas: não assumir Apollo, Clay, browse, API, verificador, planilhas ou libs presentes. Usar o que estiver disponível; se recurso ausente mudar resultado, explicar benefício e oferecer instalação simples compatível com pessoa não técnica. Enriquecimento pago requer orçamento/autorização, sem waterfall automática. Scripts só quando volume/consistência trouxerem benefício concreto; inicialmente nenhuma necessidade demonstrada.

Preferências recorrentes: quando a pessoa repetir critérios, geografia, formato ou definição de prioridade, oferecer adaptar sua própria skill. Aplicar adaptação quando solicitada/aceita; não salvar regra por inferência. Bibliografia e decisões de descarte ficam neste dossiê, fora do runtime.

## Limites de validação

Pesquisa estática e leitura integral selecionada concluídas; scripts apenas inspecionados, não executados. Nenhum pacote criado ou contratado. Licença de astDeniss pendente e pacote completo de Browserbase/Corey não auditado. Não houve prova no Hermes/ComputerRuntime, verificação de integração/ferramentas, revisão de proposta de instalação ou pedido real autenticado. Tratamento jurídico de contatos não foi decidido por textos das skills: esta rodada permanece sem dados pessoais, conta e mensagens.
