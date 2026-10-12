# Pesquisa de skills: pesquisa secundária e decisão de mercado

Consulta: **12/10/2026**. Destino: futura Pesquisadora de Mercado interna, em PT-BR, para empresas diversas. Entrega: comparação de métodos, componentes e limites. Nenhuma skill foi criada/instalada, código externo executado, conta usada, fonte contatada ou pesquisa publicada. gallery.json não foi alterado.

## Método e acesso

Aplicada a metodologia de `skills/skill-manager/references/research.md`. Descoberta no skills.sh e leitura primária por GitHub/HTTPS bruto; cinco SKILL.md completos e recursos pertinentes, com SHAs fixos. Revisões novas confirmadas por `git ls-remote` somente leitura; datas extraídas das páginas de commit. ECC reutiliza revisão já verificada nesta sessão, com leitura nova de sua skill de pesquisa.

A amostra foi escolhida por contribuições distintas: orientação à decisão, dimensionamento auditável, verificação de fontes, coleta concorrencial e acesso a provedores de pesquisa. Estrelas, instalações e badges não sustentam eficácia ou segurança. Não pretende representar toda a internet. Entrevistas, surveys e síntese de voz do cliente pertencem à outra frente.

## Proveniência e licenças

Datas são da revisão do **repositório**, não da última alteração de cada skill nem de ensaio comercial. Autoria individual não é inferida automaticamente do autor de commit. As licenças foram localizadas na revisão e identificadas pelo texto da raiz; não houve auditoria jurídica de todo recurso de terceiros.

| ID | Fonte e autoria verificável | Revisão / data visível | Licença |
|---|---|---|---|
| A | ECC / Affaan Mustafa, copyright nominal | `b92f181b3b748d1abbc2afd94af6aa7d8c8fca29`; [commit](https://github.com/affaan-m/ecc/commit/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29) 11/10/2026 no fuso exibido, 12/10 UTC | [MIT](https://github.com/affaan-m/ecc/blob/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29/LICENSE) |
| B | labdotsa contributors; frontmatter autor labdotsa | `aca67c220ac4ca8b82d2fc480c7c77828c6f0cf7`; [commit](https://github.com/labdotsa/skills/commit/aca67c220ac4ca8b82d2fc480c7c77828c6f0cf7) 22/08/2026 | [MIT](https://github.com/labdotsa/skills/blob/aca67c220ac4ca8b82d2fc480c7c77828c6f0cf7/LICENSE) |
| C | Joe Amditis, copyright nominal no pacote journalism | `e3e2172f760b8f13c7d827092c03bdb58e40b263`; [commit](https://github.com/jamditis/claude-skills-journalism/commit/e3e2172f760b8f13c7d827092c03bdb58e40b263) 04/10/2026 | [MIT](https://github.com/jamditis/claude-skills-journalism/blob/e3e2172f760b8f13c7d827092c03bdb58e40b263/LICENSE) |
| D | rediumvex, copyright nominal | `3b41ab59ec9be2f47ae6d841521c243ee15a5e29`; [commit](https://github.com/rediumvex/ai-marketing-claude/commit/3b41ab59ec9be2f47ae6d841521c243ee15a5e29) 10/04/2026 | [MIT](https://github.com/rediumvex/ai-marketing-claude/blob/3b41ab59ec9be2f47ae6d841521c243ee15a5e29/LICENSE) |
| E | SandBase / sandbaseai; manutenção do repositório, autoria individual não confirmada | `cbab58188611e626ccaf54ac346b437d12ea4729`; [commit](https://github.com/sandbaseai/sandbase-skills/commit/cbab58188611e626ccaf54ac346b437d12ea4729) 26/09/2026 | [Apache-2.0](https://github.com/sandbaseai/sandbase-skills/blob/cbab58188611e626ccaf54ac346b437d12ea4729/LICENSE) |

As cinco origens estão fora da allowlist github atual da galeria. Consulta para aprender não autoriza redistribuição sem preservar atribuição, licença e avisos pertinentes.

## Matriz de comportamento

| Fonte principal, integral | Contexto / método | Entrega / dependências | Flexibilidade e limite |
|---|---|---|---|
| A — [market-research](https://github.com/affaan-m/ecc/blob/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29/skills/market-research/SKILL.md) | Mercado, categoria, concorrente ou tese; exige fontes, dados recentes e evidência contrária. | Resumo, achados, implicações, riscos e recomendação; separa fato, inferência e recomendação. | Trata vendor claims como alegações e fonte como dados. Método de coleta/modelagem pouco detalhado; formato deve acompanhar decisão, sem transformar toda consulta em due diligence. |
| B — [market-sizing](https://github.com/labdotsa/skills/blob/aca67c220ac4ca8b82d2fc480c7c77828c6f0cf7/skills/market-sizing/SKILL.md) | Define unidade, região, período, moeda, valor e decisão; constrói equações e contagens observáveis. | Modelo bottom-up, verificação top-down independente, drivers, reconciliação e cenários; documento autossuficiente. | Distingue TAM, SAM e capacidade alcançável. Não faz média para esconder divergências. Modelo completo é excessivo para pergunta pequena; definição incerta pode justificar entrega parcial em vez de aprovação formal obrigatória. |
| C — [source-verification](https://github.com/jamditis/claude-skills-journalism/blob/e3e2172f760b8f13c7d827092c03bdb58e40b263/journalism-core/skills/source-verification/SKILL.md) | Claim exato e nível de confiança; SIFT distingue fonte, autenticidade, suporte, atualidade e representatividade. | Trilha com evidência favorável, contrária, ausente e estado da verificação. Recursos carregados por tipo. | Incerteza pode permanecer não resolvida. Checklist jornalístico e cadeia de custódia integral precisam proporcionalidade no escritório. Contato, uploads e publicação exigem autorização própria. |
| D — [market-competitors](https://github.com/rediumvex/ai-marketing-claude/blob/3b41ab59ec9be2f47ae6d841521c243ee15a5e29/skills/market-competitors/SKILL.md) | Alternativas para o mesmo público; coleta posicionamento, CTA, preço e prova social públicos. | Matriz, histórico, lacunas e hipóteses de diferenciação; usa dois scripts próprios. | Proíbe números inventados e permite falta de Wayback. Datas fixas 2023–2025 ficaram antigas; white space de comunicação não demonstra demanda nem oportunidade econômica. |
| E — [market-research](https://github.com/sandbaseai/sandbase-skills/blob/cbab58188611e626ccaf54ac346b437d12ea4729/research/market-research/SKILL.md) | Pergunta/target/contexto; descobre e inspeciona capabilities, schema e preço antes do uso. | Síntese com fontes, lacunas e observações separadas de interpretação; depende de SandBase. | Declara pesquisa somente leitura e prossegue com evidência disponível. API map não prova acesso, cobertura, resultado ou crédito; método fica acoplado ao provedor. |

## Componentes: aproveitar, adaptar, descartar

| Fonte / recurso exato | Componente | Decisão e motivo |
|---|---|---|
| A, principal acima | Alegação comercial distinta de fato corroborado; evidência contrária visível | **Aproveitar** no núcleo. **Adaptar** extensão do relatório à pergunta; não executar os diferentes modos como pipeline obrigatório. |
| B, principal acima | Equação com unidades, premissas e faixa; mercado alcançável limitado por capacidade | **Aproveitar** em dimensionamento. **Adaptar** horizonte e custo da pesquisa. **Descartar** participação de mercado arbitrária e exigência de modelo completo em toda comparação. |
| C — [source-credibility.md](https://github.com/jamditis/claude-skills-journalism/blob/e3e2172f760b8f13c7d827092c03bdb58e40b263/journalism-core/skills/source-verification/references/source-credibility.md), integral | Identidade, expertise, interesses e corroboração | **Aproveitar** para avaliar o claim específico. Credibilidade não torna toda afirmação verdadeira; várias páginas que repetem uma origem não são confirmação independente. |
| C — [documents.md](https://github.com/jamditis/claude-skills-journalism/blob/e3e2172f760b8f13c7d827092c03bdb58e40b263/journalism-core/skills/source-verification/references/documents.md), integral | Proveniência e consistência de documento | **Adaptar** a relatório, demonstração e registro consultados. Inspeção visual e metadata são sinais, não autenticação conclusiva. |
| C — [verification-trail-and-archiving.md](https://github.com/jamditis/claude-skills-journalism/blob/e3e2172f760b8f13c7d827092c03bdb58e40b263/journalism-core/skills/source-verification/references/verification-trail-and-archiving.md), integral | Registrar claim, URL, ações, conflitos e razão da conclusão | **Aproveitar** rastreabilidade proporcional. **Descartar** arquivamento automático por submissões externas e multiplicação de screenshots/hashes para todo dado público. |
| D — [competitor_scanner.py](https://github.com/rediumvex/ai-marketing-claude/blob/3b41ab59ec9be2f47ae6d841521c243ee15a5e29/scripts/competitor_scanner.py), integral, não executado | Extração mecânica de sinais | **Não transportar** como verificação: preço vem de regex em HTML, subhead do primeiro H2 e CTA do primeiro match. Palavras de confiança/depoimento só indicam presença textual, não validade. Precisa leitura humana/agente da página e termos. |
| D — [analyze_page.py](https://github.com/rediumvex/ai-marketing-claude/blob/3b41ab59ec9be2f47ae6d841521c243ee15a5e29/scripts/analyze_page.py), integral, não executado | Parser e fetcher usados pelo scanner | **Descartar** implementação nesta pesquisa: não renderiza JS, regras de CTA são inglesas e fetch desabilita verificação TLS. Scores por contagens de elementos não demonstram força concorrencial. |
| E — [sandbase-api-map.md](https://github.com/sandbaseai/sandbase-skills/blob/cbab58188611e626ccaf54ac346b437d12ea4729/research/market-research/references/sandbase-api-map.md), integral | Descoberta de esquema, custo e execução assíncrona | **Aproveitar** princípio de conferir acesso e capacidade antes de prometer coleta. **Descartar** dependência fixa de SandBase: se fonte/conta não está disponível, usar alternativa real ou registrar lacuna. |

## Contrato de evidência sugerido

Inferência para SquadOS, não uma skill implementada: começar pela decisão, limites do mercado e materiais existentes. Pesquisar fontes proporcionais à incerteza; aprofundar comparáveis, sizing ou verificação só quando contribuírem. O relatório apresenta resposta e implicação, com fontes próximas aos claims materiais e detalhe auditável conforme o pedido.

| Informação | Registro que muda a interpretação |
|---|---|
| Número de mercado | Unidade, população incluída, base temporal, região, fonte original, transformações e premissas. Receita, gasto e valor econômico não são intercambiáveis. |
| Preço e oferta | Data consultada, moeda, país, plano/unidade, impostos, periodicidade, elegibilidade e condições visíveis. Página publicada não prova preço efetivamente contratado. |
| Alternativa concorrente | Mesmo problema e público, substituto indireto e opção de não comprar; critérios que tornam comparação válida. Lista de ranking não define sozinha o conjunto. |
| Resultado de empresa | Alegação da empresa, filing/registro, medição própria ou evidência independente; separar estágio de disponibilidade de eficácia prometida. |
| Fonte paga | Existência e trecho acessível, data e escopo do que foi lido. Snippet ou resumo não equivale ao relatório integral. |
| Crescimento / tendência | Série e período comparáveis, mudanças de definição, sazonalidade e limitações; tráfego ou buscas não equivalem a vendas. |

O acesso pode ser integral, parcial, metadata/snippet ou indisponível. Material não acessado permanece lacuna. Quando fontes conflitam, mostrar diferenças de período, universo e método antes de escolher ou delimitar uma faixa. Recência adequada depende da pergunta: preço exige observação recente; um censo pode continuar útil com seu ano explícito.

Em sizing, manter equação reproduzível e cenários coerentes; não criar um TAM preciso a partir de premissas frágeis. Quantificar um universo elegível não prova disposição a pagar. Entrevistas e surveys reais produzem outra classe de evidência; comentários, buscas, anúncios ativos e painéis sintéticos são sinais/proxies com limites próprios, não observação de clientes entrevistados.

## Limite do especialista

A Pesquisadora de Mercado responde questões de categoria, alternativas, segmentos, condições de entrada e tamanho plausível de oportunidade. A futura Pesquisadora de Concorrentes de E-commerce terá recorte operacional de produtos, preço, frete e oferta; aqui esses dados ajudam a decisão de mercado, sem virar monitoramento de SKU por padrão.

Pesquisa secundária não autoriza contatar empresas, formular compra, criar conta, acessar bases pagas, publicar ou iniciar gasto. Não presumir conta de provedor apenas porque o pacote lista sua API. Design de entrevista, recrutamento, amostragem e síntese VOC devem ser encaminhados quando a pergunta exige evidência primária de pessoas.

## Lacunas e avaliação futura

Não houve execução dos scripts, API, instalação, verificação Hermes, ensaio PT-BR ou avaliação de eficácia. Recursos de C sobre redes, imagem, vídeo, sintéticos e entrevistas não foram lidos: não eram necessários à decisão de pesquisa secundária aqui. A/B são autossuficientes no SKILL principal; B mostra apenas SKILL.md na pasta consultada. E teve mapa lido, mas provedores, preços e schemas conectados não foram chamados/verificados.

O scanner D evidencia limitações concretas; não foi feita auditoria integral de segurança do repositório. Fontes primárias dos métodos SIFT e de sizing não foram revisitadas fora dos pacotes; esta rodada compara implementação das skills, sem provar validade universal de todos os frameworks. Não se adicionou candidato redundante apenas para ampliar contagem.

Aceitação futura: pesquisa de uma categoria brasileira, comparação de alternativas com preços condicionais e estimativa com poucos dados. Exigir limites, fontes realmente consultadas, distinção fato/claim/inferência, números com unidade, comparabilidade, lacunas e conclusão proporcional. O resultado pode ser decisão sustentada, faixa útil ou evidência insuficiente; não precisa terminar em recomendação positiva.
