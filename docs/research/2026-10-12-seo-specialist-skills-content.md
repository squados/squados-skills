# Pesquisa de skills: intenção, conteúdo e SEO local

Consulta: **12/10/2026**. Destino: futura Especialista SEO interna, em PT-BR, para negócios diversos. Esta rodada compara métodos; não cria skill, executa scripts, instala ferramentas, usa conta/crédito, altera site ou modifica gallery.json. Auditoria técnica, indexação e implementação de schema pertencem à outra frente.

## Método e alcance

Metodologia: `skills/skill-manager/references/research.md`. Descoberta no skills.sh; cinco SKILL.md completos lidos nas fontes GitHub via HTTPS, com revisões fixas. Recursos decisivos também lidos; scripts somente inspecionados. SHAs novos confirmados com `git ls-remote` somente leitura. Alegações mutáveis relevantes foram conferidas em documentação primária Google.

Não foi feito ranking por estrelas/instalações. A adaptação de Chris Cooke foi selecionada por diferença verificável de método, preservando Corey Haines como autor original, sem repetir o upstream como uma segunda fonte independente. O pacote de keyword research mudou: o link antigo em `seo-geo/research/` retornou 404; o atual é `seo-geo/survey/keyword-research/`.

## Proveniência

Datas abaixo são das revisões do **repositório**, não da última alteração de cada skill nem de teste comercial. Licenças identificadas pelos textos da revisão; isso não constitui auditoria jurídica de todo pacote.

| ID | Origem / autoria | Revisão / data visível | Licença |
|---|---|---|---|
| A | Sanket Dongre / vibe-building-skills, copyright nominal | `e9714d8decbc9a76eaab3bd85866117b8010e9bc`; [commit](https://github.com/sanky369/vibe-building-skills/commit/e9714d8decbc9a76eaab3bd85866117b8010e9bc) 12/07/2026 | [MIT](https://github.com/sanky369/vibe-building-skills/blob/e9714d8decbc9a76eaab3bd85866117b8010e9bc/LICENSE), lida nesta sessão |
| B | aaron-he-zhu, autor no frontmatter | `e08093343de6df31848e58eec238e494426166e3`; [commit](https://github.com/aaron-he-zhu/aaron-marketing-skills/commit/e08093343de6df31848e58eec238e494426166e3) 12/10/2026; skill 20.1.0 | [Apache-2.0](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/e08093343de6df31848e58eec238e494426166e3/LICENSE), também declarada na skill atual |
| C | Garrett Smith / GMB Gorilla, copyright nominal | `405ce209775f8cb8f9dbaa511656594bb682cf9f`; [commit](https://github.com/garrettjsmith/localseoskills/commit/405ce209775f8cb8f9dbaa511656594bb682cf9f) 15/08/2026; skill 1.0.0 | [MIT](https://github.com/garrettjsmith/localseoskills/blob/405ce209775f8cb8f9dbaa511656594bb682cf9f/LICENSE) |
| D | every-app/open-seo; copyright Ben Senescu | `89e5a00717cdf049b7c2b4e29646edb3a7d4995b`; [commit](https://github.com/every-app/open-seo/commit/89e5a00717cdf049b7c2b4e29646edb3a7d4995b) 08/10/2026 | [MIT](https://github.com/every-app/open-seo/blob/89e5a00717cdf049b7c2b4e29646edb3a7d4995b/LICENSE) |
| E | Chris Cooke, adaptação do trabalho de Corey Haines | `a74b69d7452c6aca23a2c00a1c3c212c9859e3b5`; [commit](https://github.com/bigchriscooke/seo-playbook-skills/commit/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5) 22/09/2026; skill 1.0.0, verificação declarada 18/09 | [MIT do pacote](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/LICENSE), texto integral com avisos dos dois autores |

As origens estão fora da allowlist github atual da galeria. Consulta para aprender não autoriza distribuição sem preservar autoria, licença e avisos aplicáveis.

## Matriz comparativa

| Principal, integral | Intenção / contexto | Método e entrega | Flexibilidade e limite |
|---|---|---|---|
| A — [seo-content](https://github.com/sanky369/vibe-building-skills/blob/e9714d8decbc9a76eaab3bd85866117b8010e9bc/skills/marketing/seo-content/SKILL.md) | Artigo ou revisão com consulta, público, material original e voz. | Confere resultados, intenção e lacuna; entrega brief, texto e metadata. | Usa premissas quando falta dado e não inventa experiência. Fórmulas de comprimento, densidade, quantidade de links/FAQ e linguagem de garantia de ranking são prescritivas demais. Schema automático fica fora deste escopo. |
| B — [keyword-research](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/e08093343de6df31848e58eec238e494426166e3/seo-geo/survey/keyword-research/SKILL.md) | Semente, mercado/idioma, negócio, site e métricas disponíveis. | Descobre, classifica, agrupa e prioriza; rastreia fonte, período, localidade e tipo de evidência. | Unknown não vira N/A nem score; atenção Wikipedia não vira volume. Oito fases anunciadas, memória obrigatória e mínimo de oportunidades/números são excessos. Helpers e planos gratuitos declarados não foram executados/verificados. |
| C — [local-content-briefs](https://github.com/garrettjsmith/localseoskills/blob/405ce209775f8cb8f9dbaa511656594bb682cf9f/skills/local-content-briefs/SKILL.md) | Tema/contexto ou cluster de negócio local. | Brief de conceitos, perguntas, entidades e estrutura para decisão do leitor. | Intenção de priorizar conceito sobre repetição é útil. Contradiz a própria liberdade de extensão com quotas de conceitos, entidades, palavras e FAQs; promete efeitos sem medição. Requisitos de AI/schema precisam revisão. |
| D — [local-seo](https://github.com/every-app/open-seo/blob/89e5a00717cdf049b7c2b4e29646edb3a7d4995b/plugins/openseo/skills/local-seo/SKILL.md) | Localização, identificador do negócio e consultas locais; depende de projeto OpenSEO. | Compara perfis e visibilidade numa grade geográfica; explica cobertura e custo por busca. | Ausência na grade depende do número de resultados; não prova invisibilidade. Integração, writeback e relatório obrigatório são acoplamentos; prioridades universais de categoria versus frequência não são diagnóstico causal. |
| E — [ai-seo-better-than-corey-haines](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/SKILL.md) | Superfícies de busca AI, perguntas validadas, páginas e acesso real. | Painel repetível, contagens separadas de menção/recomendação/citação e ledger de claims. | Amostra menor permitida; fonte inacessível permanece lacuna. Não promete ganhos. O título é comparação datada de método, não ensaio de ranking; diagnóstico de crawler/schema deve ser encaminhado à frente técnica. |

## Componentes aproveitáveis e descartáveis

| Fonte / recurso | Decisão / motivo |
|---|---|
| A — [article-templates.md](https://github.com/sanky369/vibe-building-skills/blob/e9714d8decbc9a76eaab3bd85866117b8010e9bc/skills/marketing/seo-content/references/article-templates.md), integral | **Aproveitar** formatos como exemplos opcionais. **Descartar** skeleton obrigatório, FAQ em toda peça e JSON-LD automático apresentado como caminho a rich results. |
| B — [keyword-intent-taxonomy.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/e08093343de6df31848e58eec238e494426166e3/seo-geo/survey/keyword-research/references/keyword-intent-taxonomy.md), integral | **Aproveitar** intenção mista e revisão na SERP. **Descartar** percentuais de conversão e comprimentos típicos como previsão; palavras da consulta são pistas, não prova da intenção local. |
| B — [keyword-prioritization-framework.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/e08093343de6df31848e58eec238e494426166e3/seo-geo/survey/keyword-research/references/keyword-prioritization-framework.md), integral | **Aproveitar** relevância comercial e incerteza. **Não copiar** score: com pesos normalizados somando 1, a soma dividida por 5 tem máximo 1, mas os cortes apresentados são 4–5; escala inconsistente. |
| B — [example-report.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/e08093343de6df31848e58eec238e494426166e3/seo-geo/survey/keyword-research/references/example-report.md), integral | **Adaptar** a tabela e razão da prioridade. **Descartar** volumes, dificuldades, potencial e estrelas ilustrativos como dados de pesquisa real; ausência de fonte/mercado impede reutilização factual. |
| C, principal acima | **Aproveitar** perguntas que ajudam o cliente e peculiaridade real da área atendida. **Descartar** quantidades mínimas de entidades/conceitos, localização inventada e cidade apenas substituída em template. Pasta consultada apresentou somente SKILL.md. |
| D, principal acima | **Aproveitar** identidade da unidade, coordenada e limite do resultado retornado. **Adaptar** custo e amostragem à pergunta. **Descartar** presumir crédito, integração/report instalado ou persistência remota autorizada. |
| E — [platform-verification.md](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/references/platform-verification.md), integral | **Aproveitar** consultar operador atual antes de declarar requisito. Não generalizar Google para todos os assistentes; links OpenAI/Perplexity foram identificados, não revalidados nesta rodada. |
| E — [content-patterns.md](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/references/content-patterns.md), integral | **Aproveitar** claim→fonte→período→limite→decisão e templates sem fatos fictícios. Resultado de experimento não vira promessa para plataformas atuais. |
| E — [comparison.md](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/references/comparison.md), integral | **Aproveitar** comparação delimitada ao snapshot e preservação da autoria. **Descartar** interpretar o nome como eficácia superior comprovada. |
| E — [claim_check.py](https://github.com/bigchriscooke/seo-playbook-skills/blob/a74b69d7452c6aca23a2c00a1c3c212c9859e3b5/skills/ai-seo-better-than-corey-haines/scripts/claim_check.py), integral, não executado | Scanner de padrões ingleses não navega nem verifica verdade; **adaptar** apenas se um uso real justificar ferramenta PT-BR. Zero findings não certifica accuracy nem atualização. |

## Conferência em fontes primárias Google

Estas páginas foram efetivamente abertas em 12/10/2026. Síntese restrita aos limites que mudam a adaptação dos pacotes:

- [Conteúdo útil e orientado a pessoas](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), atualização visível 05/10/2026: Google não define comprimento preferido; originalidade, utilidade e fontes ajudam a avaliação. E-E-A-T não é, por si só, um fator específico de ranking. Isso contraria quotas mecânicas como critério de qualidade.
- [Guia AI Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), atualização visível 10/07/2026: prioriza conteúdo próprio que acrescente experiência/conhecimento, organização útil e informação local/produto atual. Não requer fragmentar páginas, reescrever para AI, cobrir toda variação de query ou criar llms.txt; Google declara ignorar esse arquivo para visibilidade/ranking Search. Aponta um relatório de performance generativa no Search Console, cujo acesso/disponibilidade na propriedade não foi verificado. Não generalizar essas regras a outras engines. A página [AI features](https://developers.google.com/search/docs/appearance/ai-features), atualizada 10/12/2025, foi lida como apoio: elegibilidade não garante exibição e não há schema especial exigido.
- [Fatores de ranking local](https://support.google.com/business/answer/7091), sem data editorial visível: relevância, distância e proeminência ajudam a explicar diferenças geográficas. Categoria, reviews ou frequência isoladamente não demonstram causa de uma posição observada.
- [Changelog Search](https://developers.google.com/search/updates): o registro de 08/05/2026 informa encerramento dos FAQ rich results a partir de 07/05; em 15/06 a documentação foi removida. O antigo URL FAQPage redirecionou para updates. As prescrições de A/C para FAQ schema como benefício de rich result ficaram desatualizadas; perguntas úteis continuam possíveis sem essa promessa.
- [Search Analytics API](https://developers.google.com/webmaster-tools/v1/searchanalytics/query): consulta exige autorização e período, retorna dados da propriedade com cliques, impressões, CTR e posição; não garante todas as linhas. Esses dados não são volume total do mercado. Nenhuma API foi chamada.

## Adaptação sugerida para SquadOS

Inferências da comparação, ainda sem pacote implementado:

1. Escolher a abordagem pelo pedido: descobrir consultas, melhorar uma página, produzir brief ou entender presença local/AI. Não expor oito fases ou exigir escolher modos.
2. Partir do público, oferta e materiais reais; SERP atual ajuda a testar intenção, mas é uma observação com idioma, região, dispositivo e data. Não concluir demanda apenas da redação de uma pergunta.
3. Prioridades podem considerar relevância, resultado pretendido, competição observada e esforço; não fabricar volume/dificuldade para cumprir tabela. Com dado crítico ausente, entregar shortlist com lacuna e próximo teste.
4. Reutilizar fidelidade ao material e promessa cumprida dos dossiês de Conteúdo/Pesquisa de Mercado. SEO não autoriza experiência falsa, CTA deslocado ou reescrita do conteúdo aprovado para atingir densidade.

| Negócio / pedido | O que muda a entrega |
|---|---|
| Serviço local | Unidade/área realmente atendida, pergunta de quem quer contratar e informações consistentes; sem criar páginas de bairros por mera quota. |
| Curso ou B2B | Consulta precisa corresponder ao conteúdo/serviço e ao estágio do comprador; tráfego sem adequação à oferta não resolve o objetivo. |
| E-commerce | Distinguir categoria, produto e guia de escolha por intenção; usar fatos atuais de disponibilidade e preço. Não foi consultada uma skill específica de e-commerce nesta amostra. |
| Busca AI | Amostra observada distingue menção de citação e informa condições da coleta; não vira participação de mercado ou promessa de inclusão. |

## Métricas e acesso

Toda métrica usada deve preservar fonte/export, consulta, país/região, idioma, período, data de coleta e definição do provedor. Dificuldades de fornecedores distintos não são diretamente equivalentes. Volumes de terceiros são estimativas do fornecedor; GSC observa desempenho da própria propriedade. Autocomplete, Wikipedia e perguntas sintéticas são pistas/proxies, não volumes medidos de busca.

Sem acesso real a GSC, GA, Semrush, Ahrefs ou OpenSEO, registrar ausência e trabalhar com material fornecido/evidência pública suficiente. Existência da integração não demonstra instalação, saldo, permissão ou disponibilidade. Esta rodada não fez chamada paga vidIQ ou outro provedor.

Cliques/CTR de mídia paga não provam ganho orgânico. Monitoramento SEO precisa definir consulta/página, janela, baseline, sazonalidade e mudança realizada; variação antes/depois não prova causalidade isolada. Auditoria técnica, schema e mudanças de crawler ficam com a outra frente; implementação/publicação são entregas separadas.

## Lacunas e aceitação futura

Não houve instalação, validação Hermes, script executado, pesquisa paga, observação autenticada de ranking ou ensaio PT-BR. B teve três recursos decisivos lidos, mas não instructions-detail, conectores, evidence-cycle, templates de cluster ou memória completos. D não teve report renderer/API backend auditados. E teve recursos citados e scanner lidos, mas cenários de avaliação não foram executados. Licença localizada não comprova segurança/compatibilidade do pacote completo.

Avaliar futuramente um brief de serviço local, revisão de conteúdo existente e shortlist de termos com export real/ausência parcial de métricas. Critérios: intenção sustentada, fontes e recortes explícitos, utilidade ao leitor, decisão proporcional, números verificáveis, preservação de fatos e ausência de promessa de ranking/AI visibility. Contrato estrutural válido, pacote executável e resultado SEO observado continuam estados distintos.
