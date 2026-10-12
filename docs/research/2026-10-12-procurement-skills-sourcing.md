# Especialista em Compras — sourcing, RFx, comparação e custo total

Data de acesso: **12/10/2026**. Frente da rodada 19/33. Pesquisa documental e leitura de fontes originais; nenhum pacote criado, instalado ou executado, nenhum fornecedor contatado e nenhuma compra, adjudicação, contratação ou envio realizado.

## Resultado e alcance

Recomendo construir posteriormente uma síntese própria enxuta, usando **Arun Balaji Raju** para pesquisa baseada em evidência e revisão de modelos comerciais; **The Procurement Office (TPO)** para matriz de resposta, requisitos, neutralidade e critérios verificáveis; **Eric Risco** para escolher RFI/RFQ/RFP pela incerteza do pedido. **Emir Çobanoğlu** oferece boa separação em referências, mas suas fórmulas de preço justo, notas de risco, pipeline obrigatório e aprendizagem automática exigem descarte. **Gasquet** tem a normalização mais direta, porém a licença não foi identificada: serve como comparação metodológica, sem transposição de texto ou recursos.

Foram **7 famílias originais aprofundadas, 14 arquivos SKILL.md lidos integralmente**, além dos recursos determinantes abaixo. Os três pacotes de Arun existem também como Markdown em `skills/`; esses espelhos e ZIPs não contam como novas skills nem evidência independente. Diretórios de descoberta não contam como origem. Nenhum fork foi lido como candidato independente. O número de forks informado por GitHub é metadado do repositório, não quantidade de soluções avaliadas nem garantia de independência.

Busca em inglês e português por profissão, RFQ/RFP, quotation comparison, supplier selection, procurement, sourcing e TCO. Buscadores e diretórios levaram aos originais; leitura feita por raw fixado em SHA, API de metadados e `git ls-remote`. Sem clones, scratch ou código remoto executado. Reuso das pesquisas anteriores de propostas comerciais/CFO não foi contado como leitura nova. Os sete originais resolveram as dúvidas materiais desta frente; ampliação interrompida por suficiência, não quota.

## Proveniência e licenças

Todos os links de arquivo abaixo apontam à revisão efetivamente lida. Data do commit não prova data de criação da skill.

| Família original | Revisão e data verificadas | Autoria | Licença e forks observados | Leitura/runtime |
|---|---|---|---|---|
| [gasquet82-code/procurement-agent-skills](https://github.com/gasquet82-code/procurement-agent-skills) | `b27d641b3558fbb6b9fbcfd7b4edd54493711100`, 15/05/2026 12:22 UTC | Conta gasquet82-code; nome civil não confirmado | API `license: null`, nenhuma LICENSE na árvore; 0 forks, `fork: false` | 3 skills + 4 globais + README. Texto, sem execução; estrutura depende dos globais e perfil de empresa |
| [emircbngl/claude-procurement-skill](https://github.com/emircbngl/claude-procurement-skill) | `9ae056dc4e3c1c7256f5138148c473daf50c5180`, 29/07/2026 17:15 UTC | Emir Çobanoğlu, confirmado no LICENSE | [MIT](https://github.com/emircbngl/claude-procurement-skill/blob/9ae056dc4e3c1c7256f5138148c473daf50c5180/LICENSE); 0 forks, `fork: false` | 1 skill + 8 referências selecionadas + licença. Web, leitura/escrita local e chamadas opcionais a skills de formatos; não executado |
| [procurement-office/procurement-skills](https://github.com/procurement-office/procurement-skills) | `d42674279321af34b62454ea803eef4cf108e0c7`, 08/05/2026 07:24 UTC | Hendrik Poelenjee / The Procurement Office, no NOTICE; frontmatter owner portable-sourcing-lab | [Apache-2.0](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/LICENSE), [NOTICE](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/NOTICE); 0 forks, `fork: false` | 4 skills draft + 6 refs + 2 standards + 2 exemplos JSON + LICENSE/NOTICE. Python/Bash opcionais no pacote; não executados |
| [arunbalajiraju-proc/procurement-ai-assistant](https://github.com/arunbalajiraju-proc/procurement-ai-assistant) | `67b7e02bfb613f9939f3d7347d75100954d3bc03`, 27/07/2026 21:59 UTC; CITATION.cff declara release 0.2.0 em 26/07/2026 | Arun Balaji Raju, frontmatter/CITATION/LICENSE | [MIT](https://github.com/arunbalajiraju-proc/procurement-ai-assistant/blob/67b7e02bfb613f9939f3d7347d75100954d3bc03/LICENSE); 2 forks, `fork: false` | 3 skills standalone do diretório agent-skills + CITATION/LICENSE. Declaradas sem dependências externas; pesquisa depende de acesso efetivo às fontes |
| [zavora-ai/skill-procurement](https://github.com/zavora-ai/skill-procurement) | `0444e812ff2f2bd534d8216fc0b8465974e29117`, 31/05/2026 05:06 UTC | Zavora AI | [LICENSE](https://github.com/zavora-ai/skill-procurement/blob/0444e812ff2f2bd534d8216fc0b8465974e29117/LICENSE) e frontmatter declaram Apache-2.0; API NOASSERTION, arquivo é cabeçalho resumido com link à licença; 0 forks, `fork: false` | 1 skill + 3 refs + script Python inteiro. MCP mcp-procurement obrigatório; ausente/não testado |
| [ericrisco/rsc-harness](https://github.com/ericrisco/rsc-harness) | `5343ea565c39c00d329793606e8d609da2faa004`, 11/10/2026 21:16 UTC; data do JSON da página de commit | Eric Risco, LICENSE | [MIT](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/LICENSE); página mostrou 16 forks; independência do repo não verificada por API após rate limit | 1 skill + 2 refs + verify.sh inteiro + LICENSE. Núcleo texto; gate requer Bash/awk e utilitários Unix; não executado |
| [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) | `068b84bb03d2ae87c51edb2837dda25c84c1d686`, HEAD por ls-remote; data do commit não obtida | Anthropic PBC, copyright no SKILL | Apache-2.0 no arquivo e LICENSE raiz; forks não obtidos | 1 skill inteira; requer CSVs em `/mnt/user/data` e Python do exercício, não disponíveis nem executados |

Após cinco consultas de famílias a API GitHub pública retornou rate limit. Os metadados acima só incluem respostas válidas; **não foi reaproveitado o objeto anterior para o repo que falhou**. Os SHAs seguintes vieram de ls-remote e os arquivos de raw. Não há alegação de inspeção de toda a árvore de Risco/Anthropic ou de segurança de pacotes completos.

## Arquivos efetivamente consultados e contribuição

### 1. Gasquet — comparabilidade objetiva, licença ausente

Base: [revisão consultada](https://github.com/gasquet82-code/procurement-agent-skills/tree/b27d641b3558fbb6b9fbcfd7b4edd54493711100).

- [rfq-rfp/SKILL.md](https://github.com/gasquet82-code/procurement-agent-skills/blob/b27d641b3558fbb6b9fbcfd7b4edd54493711100/skills/rfq-rfp/SKILL.md): pede quantidade, unidade, destino, prazo, validade e documentos; separa componentes de custo e desvios técnicos. **Aproveitar como referência de julgamento**, não copiar sem licença. Volume anual desconhecido torna a consulta indicativa, não pedido firme.
- [quotation-comparison/SKILL.md](https://github.com/gasquet82-code/procurement-agent-skills/blob/b27d641b3558fbb6b9fbcfd7b4edd54493711100/skills/quotation-comparison/SKILL.md): normaliza unidades, só converte moeda com taxa disponível, verifica Incoterms e escopo técnico, separa preço unitário de landed cost; **adotar o princípio em redação própria**. Lacuna gera recomendação condicional.
- [tco-analysis/SKILL.md](https://github.com/gasquet82-code/procurement-agent-skills/blob/b27d641b3558fbb6b9fbcfd7b4edd54493711100/skills/tco-analysis/SKILL.md): baseline, custos, volume, cenário e transparência sobre logística/pagamento. Sem dados suficientes entrega custo de chegada parcial; **adotar princípio**, sem chamar parcial de TCO completo.
- `global/SYSTEM_PRINCIPLES.md`, `OUTPUT_FORMATS.md`, `SAFETY_RULES.md`, `PROCUREMENT_TERMS.md`, README: lidos integralmente. **Adaptar** separação de fato/hipótese/risco/recomendação; **descartar** idioma tcheco obrigatório, empresa em caminho fixo e aprovação de toda URL desconhecida como fluxo do SquadOS.

É a família mais concisa, mas documentação metodológica não é demonstração de resultado. Não tem cálculo auditado, caso executado ou licença identificada nesta revisão.

### 2. Arun — pesquisa e modelo comercial sem inventar dados

Base: [agent-skills na revisão](https://github.com/arunbalajiraju-proc/procurement-ai-assistant/tree/67b7e02bfb613f9939f3d7347d75100954d3bc03/agent-skills). Foram lidos integralmente:

- [market-research-skill/SKILL.md](https://github.com/arunbalajiraju-proc/procurement-ai-assistant/blob/67b7e02bfb613f9939f3d7347d75100954d3bc03/agent-skills/market-research-skill/SKILL.md): definir fronteira e tipos de fornecedor antes de nomes; OEM, revenda, integrador e especialista não são intercambiáveis. Busca→leitura→comparação→lacunas→busca dirigida. Matriz `Yes/Partial/No/Unknown/Needs validation`. **Adotar**, traduzindo estados; alegação comercial não vira comprovação de capacidade.
- [rfp-drafting-skill/SKILL.md](https://github.com/arunbalajiraju-proc/procurement-ai-assistant/blob/67b7e02bfb613f9939f3d7347d75100954d3bc03/agent-skills/rfp-drafting-skill/SKILL.md): separar obrigatório, avaliado, preço e contrato; requisito mensurável, resposta esperada, aceite, clareza de responsabilidades e desafio da minuta. **Adotar** na referência RFx; **adaptar** para trabalho privado interno, sem presumir regras canadenses/públicas ou política não fornecida.
- [pricing-model-review-skill/SKILL.md](https://github.com/arunbalajiraju-proc/procurement-ai-assistant/blob/67b7e02bfb613f9939f3d7347d75100954d3bc03/agent-skills/pricing-model-review-skill/SKILL.md): extrair custo único/recorrente, fixo/variável, obrigatório/opcional; testar crescimento, implantação, reajuste, renovação e saída. **Adotar**; cenário exato só com inputs, caso contrário impacto qualitativo. Normalização deve mostrar hipóteses e preservar preço submetido.
- CITATION.cff e LICENSE: autoria, versão e licença verificadas. Não foram lidos todos os outros módulos, guias, ZIPs ou exemplos; frontmatter não comprova execução no Studio.

É a melhor base licenciada para o comportamento interno pedido. Precisa compressão: múltiplas listas de inputs/saídas não devem aparecer como formulário obrigatório em uma simples comparação de três PDFs. Proibição de adjudicar é apropriada; proibição de qualquer recomendação de fornecedor deve ser adaptada a **recomendação interna condicional**, preservando a decisão humana.

### 3. TPO — estrutura de resposta e avaliação defensável

Base: [skills na revisão](https://github.com/procurement-office/procurement-skills/tree/d42674279321af34b62454ea803eef4cf108e0c7/skills). Lidos completos `p9t-market-scan/SKILL.md`, `p9t-supplier-longlist/SKILL.md`, `p9t-rfx-pack-builder/SKILL.md`, `p9t-bid-evaluation-framework/SKILL.md`.

| Fonte/arquivo | Componente | Decisão e motivo |
|---|---|---|
| [market-scan + search-patterns](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/skills/p9t-market-scan/references/search-patterns.md) | Pesquisa por web, associações, cadastros/frameworks públicos e histórico do comprador; explicita viés dos grandes fornecedores | **Adaptar** rotas conforme categoria/país e acesso; presença em duas rotas não equivale a duas evidências independentes |
| `p9t-market-scan/references/market-forces.md` | Concentração, poder relativo, substitutos, barreiras, entradas e competição | **Adaptar** quando mudarem sourcing ou custo; não fabricar nota HIGH/LOW sem evidência |
| [longlist + screening-guide](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/skills/p9t-supplier-longlist/references/screening-guide.md) | Evidência por critério e ausência como não verificado; grupo econômico/concentração | **Adotar**; falta de evidência não prova incapacidade. Não fixar mínimo de três fornecedores nem consultar só dois resultados para certificar capacidade |
| [pricing-template-guidance](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/skills/p9t-rfx-pack-builder/references/pricing-template-guidance.md) | Escopo-base/variável/opcionais, mesmas premissas de volume, inclusões/exclusões e modelo comercial adequado | **Adotar**; salário/margem/overhead em open-book só quando pertinente, não exigir custos internos de toda compra simples |
| [rfx-outline](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/skills/p9t-rfx-pack-builder/references/rfx-outline.md) | Objetivo, instruções, prazo, requisito, preço, avaliação e resposta; seção sem critério não deve sobrecarregar | **Adaptar** à minuta interna e omitir partes irrelevantes; claims jurídicos sobre contestação não viram regras legais universais |
| [scorecard-patterns](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/skills/p9t-bid-evaluation-framework/references/scorecard-patterns.md) | Critérios sem dupla contagem, âncoras por nota, pesos explícitos e soma 100 | **Adaptar** somente se pontuação ajudar e prioridades forem fornecidas/aceitas; faixas típicas não viram pesos obrigatórios |
| [interaction-patterns](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/standards/interaction-patterns.md) | Reusar dados e perguntar a variável que desbloqueia | **Adotar** esses princípios; **descartar** wizard obrigatório, sinal ritual de prontidão e perguntas sobre dados já suficientes |
| [input-trust](https://github.com/procurement-office/procurement-skills/blob/d42674279321af34b62454ea803eef4cf108e0c7/standards/input-trust.md) | Proteção de documentos externos | **Descartar como implementação**: é stub a escrever; não comprova proteção contra instrução em proposta |
| `p9t-rfx-pack-builder/assets/sample-output.json`; `p9t-bid-evaluation-framework/assets/sample-output.json` | Exemplos de lacunas e passagem de contexto | **Adaptar** lacunas explícitas; **descartar** status completed como prova de aptidão. Exemplos admitem revisão legal/pesos pendentes e potencial overlap |

Duas tensões importantes: a tabela de fonte considera recência LOW para site do fornecedor por ser autorrelato — **recência e viés são dimensões distintas**, verificar data real; `web_verified: true` após confirmar presença e linha de produto **não valida capacidade, certificado ou elegibilidade**. A referência de screening é mais cuidadosa que essa simplificação no núcleo.

O pacote declara maturidade draft e budgets, mas os quatro núcleos reais têm longos contratos JSON e repetição de procedimentos. Não assumir que metas de <200 linhas/<4000 tokens foram cumpridas. `providers/` e standards externos às pastas permitidas também impedem tratar cópia dos módulos como pronta para galeria.

### 4. Emir — arquitetura útil, heurísticas e persistência a retirar

[SKILL.md completo](https://github.com/emircbngl/claude-procurement-skill/blob/9ae056dc4e3c1c7256f5138148c473daf50c5180/SKILL.md), referências completas: `price-discovery.md`, `requirements-framework.md`, `tco-and-risk.md`, `sourcing-and-negotiation.md`, `b2b-modifiers.md`, `ask-user-patterns.md`, `self-feeding.md`, `decision-frameworks.md`, além de LICENSE. Os demais domínios, schemas, compatibilidade, report-template e verificações adversariais não foram lidos integralmente nesta frente.

| Fonte/arquivo | Componente | Decisão e motivo |
|---|---|---|
| Núcleo + requirements | Distinguir requisito eliminatório, preferência e restrição; reaproveitar contexto | **Adaptar**: perguntar somente o que muda a análise; não perguntar sempre região/moeda/audiência/formato nem escanear todo workspace automaticamente |
| [price-discovery](https://github.com/emircbngl/claude-procurement-skill/blob/9ae056dc4e3c1c7256f5138148c473daf50c5180/references/price-discovery.md) | Distinguir preço anunciado, condição aplicável, produto novo/usado/refurb e frete | **Adotar** distinções quando úteis; confirmar na fonte do vendedor, com data e validade |
| Mesmo arquivo | 3 canais sempre; eight tiers obrigatórios; faixa `peer median −5%`, teto `+10%`, aspiracional used median×1,15 | **Descartar**: exigências e percentuais sem base para cada categoria; preço hipotético de negociação não pode substituir cotação real |
| Mesmo arquivo | Cross-border CIF mais shipping novamente | **Descartar fórmula literal**: risco de contar frete duas vezes; tributação depende de destino/item/regime, exigir fontes oficiais quando material |
| [tco-and-risk](https://github.com/emircbngl/claude-procurement-skill/blob/9ae056dc4e3c1c7256f5138148c473daf50c5180/references/tco-and-risk.md) + b2b-modifiers | Aquisição, implantação, consumo, energia, suporte, integração, treinamento, saída e residual | **Adaptar** componentes pertinentes e mesmo horizonte; não lançar retorno, reparo, benefício de cartão ou equipe presumidos |
| Mesmo arquivo + decision-frameworks | FMEA-lite/RPN, fator `1−supply risk/10`, score/AHP obrigatório por classe | **Descartar como padrão**: sem dados/rubrica, números conferem precisão falsa. Matriz explicada basta; AHP só pedido concreto |
| sourcing-and-negotiation + b2b-modifiers | Alternativa e alavancas de volume/prazo/escopo | **Adaptar** preparação interna; **descartar** calendários, faixas de desconto e garantias genéricas sem verificação atual |
| [self-feeding](https://github.com/emircbngl/claude-procurement-skill/blob/9ae056dc4e3c1c7256f5138148c473daf50c5180/references/self-feeding.md) | Reusar critérios estáveis e pesquisar preços ao vivo | **Adaptar** ideia de recurso reutilizável; **descartar** gravação automática no primeiro uso, critérios/regulamentos em cache por 18 meses e confiança high só por autoria manual. Oferecer adaptação da própria versão apenas com recorrência/aceite |

MIT permite derivação com avisos. Não basta copiar núcleo: ele referencia muitos módulos e formatos `anthropic-skills:*`, que podem faltar no ambiente. Organização progressiva é boa referência, tamanho e ritual do pipeline não são adequados ao fluxo leve pretendido.

### 5. Risco — formato de pedido e auditoria do cálculo

[SKILL.md completo](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/procurement/SKILL.md), `references/sourcing-requests.md`, `references/scorecard-and-tco.md`, `scripts/verify.sh` e LICENSE lidos integralmente.

- **Adotar** escolher RFI quando faltam opções/capacidades, RFQ quando escopo é especificável e RFP quando a solução/abordagem precisa ser comparada. Não impor sequência RFI→RFP→RFQ a toda compra.
- **Adaptar** TCO no mesmo horizonte e memória de cálculo reexecutável. Exemplo demonstra aritmética em papel, não execução real; pesos 40/30/30, desempate por risco e proximidade 5% são ilustrativos, não critérios universais.
- **Adaptar** brief e matriz de resposta para o caso; **descartar** quatro artefatos obrigatórios, vencedor automático por score e award/regret como ação desta skill interna.
- **Descartar** instrução de tomar desconto/até financiar com base no retorno anualizado de 2/10 net30. A conta ≈37,2% é exemplo matemático; viabilidade depende de caixa, custo, risco e condições e não autoriza empréstimo nem pagamento. Sem estudo financeiro primário específico, não há recomendação financeira aqui.
- **Descartar como recurso de entrega** verify.sh neste momento. Ele requer Bash/awk, checa textos em inglês e shape/arithmetic; pode dar SKIP com exit0, admite tolerância, não valida fornecedor certo nem calcula todas as linhas de TCO. Não instalar Unix para uma pesquisa ou compra simples. Se tabelas recorrentes justificarem script, criar depois validador local mínimo com inputs/resultado explícitos e teste de casos relevantes.
- **Não reutilizar** números de maverick spend ou alegações de ganho de IA sem fonte primária consultada. Não sustentar desenho com estatística repetida pelo pacote.

### 6. Zavora — executor incompatível com uso interno

[SKILL.md](https://github.com/zavora-ai/skill-procurement/blob/0444e812ff2f2bd534d8216fc0b8465974e29117/SKILL.md), `references/tool-sequences.md`, `examples.md`, `cross-mcp-workflows.md`, `scripts/three_way_match.py` e LICENSE lidos completos.

**Descartar como base executável**: RFQ já envia, rfq_award decide, po_approve/po_send aprova e remete pedido. Depende de servidor específico e métricas/score opacos. Exemplos de resposta simulada não provam backend, qualidade ou autorização. Aprovação de orçamento não autoriza contato nem compra.

**Adaptar apenas distinção conceitual** de pedido/recebimento/fatura, útil à outra frente de gestão. O script compara quantidades agregadas e diferença monetária menor que 1 e retorna ação Pay. Sem moeda, tolerância por negócio, linhas, parcial e impostos, não é conciliação suficiente nem autorização de pagamento. Não executado.

### 7. Anthropic workshop — exercício, não política geral

[supplier-selection/SKILL.md inteiro](https://github.com/anthropics/cwc-workshops/blob/068b84bb03d2ae87c51edb2837dda25c84c1d686/agent-decomposition/.claude/skills/supplier-selection/SKILL.md) e LICENSE raiz consultados.

**Descartar metodologia geral**: pesos fixos preço50/prazo30/reliability20, min-max relativo ao conjunto, overrides de SUP-01 etc., warehouses americanos e escolha para PO são fixture de oficina. A composição de candidatos altera score normalizado; ausência de TCO/aceite/capacidade e MOQ como filtro geral limita aplicação. Expedited ignora score e decide menor prazo, também específico do exercício. Nenhuma condição desses fornecedores pode ser afirmada no mundo real.

**Adaptar só princípio de cálculo verificável** quando dados reais e critérios do pedido estiverem definidos. Fornecedor apto depende de julgamento/evidência; não adotar frase de que seleção é somente aritmética.

## Candidatos descobertos sem leitura integral

| Original | Acesso e decisão de triagem |
|---|---|
| [Maxbase91/procurement-skills — bid-compass](https://github.com/Maxbase91/procurement-skills/tree/daba3884fdf131845521eb18b66fc336b931c991/bid-compass) | HEAD confirmado por ls-remote; README/página original consultados, 1 fork. Não lido SKILL inteiro nesta frente; não conta entre 14. Interessante RFP e exemplos, sobreposição com TPO/Arun; outra frente pode aprofundar. README diz MIT/no attribution required: conferir LICENSE real antes de reutilizar, pois essa frase não substitui licença |
| [kishorkukreja/awesome-supply-chain — supplier-selection](https://github.com/kishorkukreja/awesome-supply-chain/tree/397d95172e374225574f1fb580c1a77376fff836/skills/supplier-selection) | HEAD confirmado; descoberta por arquivo original indexado e página do repo. Sem leitura integral, autoria/licença/data/forks do pacote não confirmados. Templates e exemplos amplos de scoring; não fazem falta às decisões já resolvidas |

Também apareceram skills de SAP MM/Odoo, assistente curto genérico, coordinator com automação de e-mail, tender analysis dependente de serviço pago e procurement-plan de PM. Não selecionadas para leitura profunda: ERP/runtime distinto, envio a terceiros, enfoque vendedor ou pouca especificidade para normalização/TCO. A lista não representa catálogo completo da internet.

## Síntese operacional proposta para uma futura skill

O núcleo reconhece a intenção pelo pedido e materiais disponíveis: pesquisar opções, preparar consulta interna, comparar ofertas ou explicar custo. Não pede escolher modo. Começa pelo resultado útil e recupera contexto autorizado relevante, perguntando só lacunas que alteram escopo, comparabilidade ou decisão.

1. **Delimitar necessidade e base comparável.** Item/serviço, especificação ou resultado, unidade, quantidade/horizonte, destino e prazo. Campos como moeda, tributo, frete, pagamento, MOQ, qualidade/aceite e capacidade entram conforme impacto concreto, sem formulário fixo.
2. **Pesquisar ou extrair conforme pedido.** Busca de fornecedores evidencia capacidade/abrangência e separa alegação de comprovação; comparação de cotações preserva dado original, documento/página/trecho e validade.
3. **Normalizar explicitamente.** Conversão de caixa→unidade, kg→item, mensal→anual ou moeda exige fator/base/FX verificável. Itens não equivalentes ficam lado a lado com ressalva, sem ranking enganoso.
4. **Calcular somente custos suportados.** Mesmo escopo/horizonte, sem dupla contagem; distinguir cotado, calculado, cenário e desconhecido. Mostrar o subtotal conhecido e o que falta para custo completo. Missing não vira zero.
5. **Entregar recomendação interna proporcional.** Razão, trade-offs, condição que muda a escolha, perguntas de esclarecimento e próximo passo interno. Pontuação só quando útil, critérios/âncoras explicados e prioridades aceitas. Compra e contato não decorrem da recomendação.

### Núcleo curto e referências sob demanda

| Recurso futuro | Quando carregar | Conteúdo mínimo e referências-base |
|---|---|---|
| SKILL.md | Todo pedido pertinente | Intenção automática, perguntas materiais, evidência, comparabilidade, custo parcial, entrega interna e limite de ação. Nenhum orçamento/score/calendário universal |
| `references/pesquisa-de-fornecedores.md` | Descoberta e lacuna de capacidade | Fronteira, tipos de fornecedor, geografia, capacidade alegada/evidenciada, matriz de lacunas e fontes datadas; Arun+TPO |
| `references/rfq-rfp.md` | Pedido interno de minuta ou matriz de respostas | RFI/RFQ/RFP pelo desconhecido; requisitos/aceite, quantidades, mesma base de preço, prazo/validade, desvios, inclusões/exclusões; Risco+Arun+TPO |
| `references/comparacao-e-custo-total.md` | Cotação e análise econômica | Dado original→normalizado com fórmula/fonte; escopo único/recorrente/opcional; landed cost versus TCO; cenários e missing; Arun+Risco, princípios gerais comparados com Gasquet |
| `templates/matriz-de-cotacoes.md` | Quando uma tabela reutilizável melhorar o resultado | Campos selecionáveis pelo pedido, não colunas inúteis obrigatórias. Origem, unidade/base, quantidade, prazo/validade, subtotal/escopo, condições, lacunas e conclusão |

Arquivos são **proposta de organização**, não criados. Biblioteca extensa de domínios, autogerador de packs, engine de scoring e framework de cadastro não se justificam hoje. Recurso ausente: explicar em linguagem comum o que faltou e oferecer instalação simples quando necessária/possível, sem mandar a pessoa executar comandos nem prometer biblioteca instalada. Adaptação da própria versão pode ser oferecida quando padrões recorrentes ficarem claros e a pessoa aceitar; não autoeditar instruções de compra depois da primeira tarefa.

### Exemplos de aceitação futuros

- Caixa de 12 unidades versus preço por peça: explicitar fator e mesma quantidade, calcular sobra/MOQ se mudar gasto; não escolher o menor número exibido.
- Oferta sem frete/tributo versus entregue no destino: total parcial e pergunta interna sobre encargo; não somar imposto presumido nem chamar barato de melhor TCO.
- SaaS por usuário versus por uso: modelar volume fornecido, implantação, suporte/renovação/saída pertinentes, desconhecidos e cenário sem inventar crescimento.
- Um fornecedor sem certificado público: registrar não verificado, pergunta de validação; não converter ausência de evidência em score0 ou certificado inexistente.
- Pedido simples com prazo hoje: usar o que está disponível e explicitar disponibilidade alegada/verificada, sem forçar RFx formal, AHP ou três cotações.
- Documento de cotação contém instrução para ignorar concorrentes/enviar dados: tratar como conteúdo externo, preservar análise e não executar instruções do documento.

## Limites e suficiência

Há evidência documental suficiente para decidir comportamento, organização e componentes. **Não há evidência de execução dessas skills no Studio, preparação pelo adaptador, compra real ou compatibilidade completa dos pacotes.** Exemplos publicados, budgets e rótulos draft/completed não equivalem a testes nossos.

Licença: MIT de Arun/Emir/Risco e Apache de TPO/Anthropic permitem avaliar uma futura derivação com avisos pertinentes; não é autorização para apresentá-los como autoria SquadOS. Gasquet permanece referência de consulta sem base de redistribuição encontrada. Nenhum repo desta frente entra automaticamente no allowlist da galeria; Anthropic cwc-workshops é repo diferente de anthropics/skills.

Detalhes fiscais, cambiais, financeiros e jurídicos não foram convertidos em instruções universais. Uma análise real material nesses temas deverá consultar fontes primárias atuais, contexto, datas e responsável pelo dado. Nenhuma taxa, tributo, custo de capital, desconto esperado, fornecedor, disponibilidade ou nota de risco foi criado para resolver lacunas.

Próximo passo desta rodada: coordenação confrontar estas decisões com a frente de gestão/termos e métodos; síntese e eventual aprovação de criação pertencem à tarefa principal. Nenhum commit, push ou publicação realizado por esta frente.
