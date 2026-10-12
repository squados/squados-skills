# Agente de Propostas Comerciais — pesquisa de skills de vendas

Data da consulta: 12/10/2026. Frente: propostas de venda e serviços, contexto do cliente, proposta de valor, escopo, entregáveis, preço, condições e clareza da decisão. Destino: especialista de negócios diversos do SquadOS; esta pesquisa não cria o pacote nem altera a galeria.

## Decisão recomendada

Construir posteriormente uma síntese própria e curta: aproveitar a composição de fatos aprovados e os limites de escopo de B2BForce; a concisão de Skill Me e Consulting Proposal; e o encadeamento cliente → situação atual → mecanismo → mudança esperada → alternativas de Value Proposition. A proposta deve permitir uma decisão informada, inclusive adiar ou reduzir o escopo. Não deve obrigar três ofertas, demonstrar ROI positivo por construção nem substituir uma lacuna por um número plausível.

A referência B2BForce é a mais consistente para serviços profissionais, mas seu workspace, gates e renderer não devem ser transplantados. Propostas de produtos, fornecimento, manutenção, treinamento, eventos e outros negócios precisam de adaptação por intenção, sem selecionar um “modo” ou impor uma estrutura de consultoria.

## Alcance e método

Descoberta em skills.sh, busca web por `sales proposal`, `business proposal`, `consulting proposal`, `proposal writer`, `pricing` e `value proposition`, e navegação dos repositórios originais. Leitura integral de **sete SKILL.md principais e dois auxiliares**, além dos recursos determinantes descritos abaixo. Uma cópia descoberta foi comparada com sua origem e eliminada da contagem. São nove skills distintas em sete famílias de repositórios; as duas famílias de Zubair Trabzada não constituem demonstrações independentes de eficácia comercial.

As revisões foram fixadas com `git ls-remote ... HEAD`; conteúdo e licenças, por raw URLs com SHA. Datas de commit foram extraídas das páginas `/commit/<SHA>`; são datas da revisão do repositório, não necessariamente da criação de cada skill. A API pública GitHub atingiu rate limit: nenhuma credencial foi solicitada, e a pesquisa continuou por raw e páginas públicas. Não foram clonados, instalados ou executados pacotes; nenhum envio, assinatura, acesso a conta ou chamada paga ocorreu.

Descobertas relacionadas a deck, geração de PDF, RFP ou métodos profissionais foram encaminhadas à consolidação de outras frentes: `ChuluuMGL/proposal-ppt-skill`, `mamba-mental/agent-skill-manager/business-document-generator`, `yoligehude14753/docforge`, `MichaelRochonnn/mckinsey-bcg-consulting`. Elas não contam como candidatas profundamente analisadas nesta frente. Diretórios e agregadores são descoberta, não fonte da licença ou prova de qualidade.

## Proveniência verificável

| ID | Origem e autoria observada | SHA fixado e data do commit | Licença consultada | Conteúdo lido |
|---|---|---|---|---|
| S1 | SkillMedev/skills; copyright Alexander Ouellet | `6b3044d569595b481a3677da8f68af7aa239dc09`, 04/10/2026 | MIT na raiz | sales-proposal-writer inteiro; árvore do pacote contém somente SKILL.md |
| S2 | b2bforce/b2bforce; copyright B2BForce | `7682ed90c62190a0f3c09eb135596d08bd6890bc`, 21/08/2026 | MIT na raiz e frontmatter | sales-proposal inteiro, proposal-structure inteiro, validate-proposal.sh inteiro; gates relevantes de AGENTS.md. CLAUDE.md remoto não encontrado |
| S3 | zubair-trabzada/ai-sales-team-claude; copyright Zubair Trabzada | `efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce`, 26/03/2026 | MIT na raiz | sales-proposal inteiro, incluindo sequência de acompanhamento; orquestrador para entender o contexto |
| S4 | ncklrs/startup-os-skills; mantenedor ncklrs; autor individual do texto não demonstrado | `916259640e86c4cdb64e69a2aee35e78a638a487`, 26/02/2026 | README afirma MIT; LICENSE retorna 404, raiz contém README e skills. Sem aviso completo verificável | proposal-writer inteiro e sete rules: arquitetura, resumo executivo, stakeholders, apresentação de preço, ROI, termos e diferenciação |
| S5 | zubair-trabzada/geo-seo-claude; copyright Zubair Trabzada | `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c`, 05/10/2026 | MIT na raiz | geo-proposal inteiro; comparado à cópia RonManatee |
| S6 | phuryn/pm-skills; copyright Pawel Huryn; template atribuído no texto a Paweł Huryn e Aatir Abdul Rauf | `c68487d721e419ec87af1ae6412a842978eab785`, 10/10/2026 | MIT na raiz | value-proposition inteiro; template PPTX externo e cursos vinculados não consultados |
| S7 | mohitagw15856/pm-claude-skills; copyright Mohit Aggarwal | `760fe9aea4300dbc682c42a94d8b59ad0c83b1a7`, 12/10/2026 | MIT na raiz | consulting-proposal, client-discovery e rate-card inteiros; exportador PDF não examinado |

As licenças MIT lidas permitem adaptação com preservação dos avisos quando houver cópia ou porção substancial. Isso não licencia marcas, dados de clientes ou materiais externos citados. Para S4, aprender com a abordagem é distinto de redistribuir texto: **não copiar recursos enquanto a licença completa e atribuição não estiverem esclarecidas**. Nenhum desses repositórios externos é automaticamente uma origem admitida pelo JSON do Studio.

Deduplicação: `RonManatee/geo-seo`, revisão `5d8c0afe3b44bf9123f6849e97541f85eefabaca` de 29/04/2026, conserva links de instalação para o original e copyright Zubair. Seu `skills/geo-proposal/SKILL.md` é idêntico, em comparação sensível a caixa, ao arquivo de S5: 11.883 caracteres em ambos. Contar uma linhagem; não atribuir autoria a RonManatee. Não foi identificado outro par idêntico na amostra; coincidência de ideias comuns não demonstra independência ou cópia.

## Comparação por componente

| Fonte / arquivo | Contribuição | Decisão | Motivo e adaptação necessária |
|---|---|---|---|
| S1 / SKILL.md | Abertura na linguagem do comprador, texto curto e próximo passo simples | Aproveitar | Faz o documento começar pelo trabalho do cliente; sem exigir uma citação literal quando só houver briefing escrito |
| S1 / SKILL.md | Estimar dor se faltarem números; validade de 14/30 dias; opções obrigatórias | Descartar | Rótulo “estimado” não cria base. Validade e preço são condições do fornecedor; não ferramentas automáticas de pressão |
| S2 / SKILL.md | Compor briefing, oferta e prova aprovada | Adaptar | Reutilizar anexos e contexto existentes; exigir os fatos necessários, sem exigir arquivos/ICP/persona em caminhos específicos |
| S2 / proposal-structure.md | Entregável verificável, exclusões adjacentes, dependências e processo de alteração | Aproveitar | É a defesa mais útil contra ambiguidade. Frequência, quantidade, limite de revisões, responsabilidades e aceite entram conforme o serviço |
| S2 / SKILL.md e gates de AGENTS.md | Permissões separadas para nome, quote e uso público; exemplo fictício não é evidência | Adaptar | Levar o princípio para materiais fornecidos; registrar fonte e permissão sem criar uma base ou frontmatter obrigatório |
| S2 / SKILL.md | Workspace operacional, aprovação de bid prévia, 6–8 páginas, PDF obrigatório, Bash/uv/WeasyPrint | Descartar como padrão | Custo e dependências desnecessários para um pedido simples. A afirmação de maior conversão por comprimento não veio acompanhada de estudo verificável |
| S3 / SKILL.md | Buscar análise anterior antes de perguntar; entregas por fase com participação do cliente | Adaptar | Bons mecanismos de contexto e responsabilidade; não exigir três fases, três dores ou três cases para todo negócio |
| S3 / SKILL.md | Três tiers obrigatórios, “mais popular”, ROI positivo no cenário conservador e seis emails | Descartar | Incentiva resultados favoráveis por desenho e falsa popularidade; acompanhamento é outra entrega, sob pedido. “Conservador” não é prova |
| S4 / rules de estrutura, executivo e stakeholders | Resumo autossuficiente; navegação conforme a decisão de quem lê | Adaptar | Resumo deve mostrar inclusive custo e condição principal. Kits paralelos para cada executivo só quando necessários |
| S4 / rules de preço e termos | Tabela comparável e custo total visível | Adaptar | Preservar unidades, período, adicionais e compromissos reais; eliminar decoys, falsa precisão e concessões não aprovadas |
| S4 / rule de diferenciação | Comparar status quo, alternativa interna e fornecedores por prioridades reais | Adaptar | Não depreciar opções, inventar superioridade ou citar benchmarks sem fonte; admite alternativa preferível à oferta |
| S5 / SKILL.md | Transformar achado de auditoria em problema comercial e trabalho proposto | Adaptar apenas a ligação | Não converter score em faturamento, escolha de pacote ou impacto garantido |
| S5 / SKILL.md | Valores, métricas de mercado, ganho de score, ROI, prazo e termos pré-preenchidos | Descartar | Exemplo transforma números setoriais e ofertas fixas em fatos do usuário; incompatível com negócios diversos |
| S6 / SKILL.md | Seis perguntas: cliente, problema, antes, mecanismo, depois, alternativas | Adaptar | Referência sob demanda quando a oferta estiver confusa. Uma oferta concreta não precisa de um projeto de posicionamento completo |
| S7 / consulting-proposal | Sete blocos compactos e perguntar só o que não está disponível | Aproveitar estrutura flexível | Boa alternativa leve; tiers e precificação por valor são opções, não regra universal |
| S7 / client-discovery e rate-card | Processo de compra, sucesso, capacidade e custos reais | Adaptar sob demanda | Discovery ajuda lacunas; rate-card ajuda discutir método de preço, sem transformar a proposta em consultoria financeira ou rejeitar preço por hora |

## Falhas concretas que mudam a decisão

**O validator de S2 é uma triagem estrutural, não uma prova comercial.** O script aceita ao menos três linhas iniciadas por `|` na seção de preço, mas não comprova exatamente uma tabela. Para prova, procura números por substring em qualquer registro referenciado; não vincula número a métrica, unidade, cliente ou período, nem exige `verified: true`. Uma quote passa se qualquer registro tiver aprovação, sem validar o texto contra o registro correto. `conditional` é aceito sem verificar o cumprimento da condição. São limites observados por leitura de código, não testes executados. O código útil de referência não justifica portar esse verificador nem dizer que garante ausência de fabricação.

**Os exemplos de S4 precisam de revisão numérica.** Em `pricing-presentation.md`, quatro pagamentos de US$24.000 totalizam US$96.000 contra US$84.000 anuais: adicional de 14,29%, embora o exemplo diga 10%. O mesmo exemplo chama benefício de US$270.000 / preço de US$84.000 de ROI 3,2x. Esse múltiplo é benefício bruto/preço; com a fórmula de ROI líquido que outro recurso do pacote usa, o resultado seria 221,43%. Esta é uma verificação aritmética do exemplo, não a validação de projeções de mercado. Antes de aproveitar um modelo, reconciliar totais, bases, percentuais, moeda e horizonte.

Não foi demonstrado aumento de vendas por execução real de nenhuma candidata. Templates, instruções e claims de “winning proposals” não equivalem a resultados controlados. Não carregar seus cases exemplificativos como prova do fornecedor.

## Divergências e caminho coerente

| Divergência | Decisão para negócios diversos |
|---|---|
| Três páginas em S1, 6–8 em S2, até 15 em S3, faixas por ACV em S4 | Comprimento acompanha decisão, complexidade e exigência recebida. Uma cotação simples cabe em poucos parágrafos; proposta complexa ganha resumo e anexos |
| S1 aceita “escopo solto” antes do contrato; S2 e S7 defendem fronteiras explícitas | Explicitar entrega e limites suficientes para entender o que se compra; detalhes de execução só quando ajudam a decisão |
| “Nunca preço antes de valor” versus resumo executivo autossuficiente | Abrir com necessidade e solução em poucas linhas; tornar preço/total e condições encontráveis imediatamente, inclusive no resumo quando útil |
| Tiers obrigatórios versus tabela única com opções permitidas | Uma oferta pode ser suficiente. Comparar duas ou três alternativas reais quando o usuário tiver escolhas de escopo; recomendar por adequação, sem fabricar decoy |
| ROI como regra versus resultado observável e mecanismo controlável | Entrega e resultado de negócio são distintos. ROI apenas se pedido ou necessário, com bases reais, premissas rastreáveis e possibilidade de resultado negativo |
| Estimar entradas versus parar por todo campo ausente | Lacuna impeditiva recebe pergunta curta. Lacuna não impeditiva vira campo a confirmar; nenhum número é inventado para concluir o documento |
| Preço por valor versus tarifa/hora/retainer | Preservar o modelo da oferta real. Explicar o que a unidade compra e limites; mudança do modelo comercial exige decisão do fornecedor |

## Núcleo curto e referências sob demanda

Proposta para a criação futura, ainda sujeita à consolidação das três frentes:

1. Reconhecer o pedido: criar, revisar, comparar versões, esclarecer oferta ou completar condições. Reusar materiais e texto aprovado antes de perguntar.
2. Identificar cliente, decisão pretendida, necessidade, oferta, entregas/limites e condições reais. Separar fato, projeção fundamentada e lacuna.
3. Escolher a menor estrutura suficiente. Descrever por que a oferta atende ao caso; ligar entrega ao resultado esperado sem garantir desempenho fora de controle.
4. Explicitar escopo, quantidade/frequência quando relevante, dependências, responsabilidades, marcos e aceite. Condições adicionais entram conforme a oferta.
5. Apresentar preço, moeda, base, total, recorrência, extras, pagamento e validade somente quando fornecidos/aprovados. Conferir aritmética e coerência entre versões.
6. Usar prova verdadeira e autorizada, ou explicar o método/capacidade disponível. Não preencher ausência com case plausível.
7. Concluir com decisão e próximo passo apropriados ao pedido. Entregar rascunho utilizável e lacunas que realmente precisam ser resolvidas; não enviar ou assinar.

Referências pequenas: **clareza da oferta e alternativas**, **escopo de projeto e serviço recorrente**, **condições e comparação comercial**, **provas e lacunas**, **revisão numérica**. Exemplos futuros devem cobrir negócios distintos e estar explicitamente identificados como ilustrativos; jamais oferecer preços ou promessas prontos para adoção. Detalhes RFP/SOW, renderizadores e QA de formatos devem vir da outra frente, sem duplicação.

Nenhum script é necessário no núcleo. Para tabelas extensas, um cálculo verificável pode ajudar; não há benefício concreto em portar Bash, criar CRM ou instalar renderer só para produzir uma proposta. PDF/DOCX/PPTX ficam condicionados ao formato pedido e à capacidade do ambiente confirmada. Quando correções recorrentes ou atrito justificarem, oferecer adaptar a própria versão da skill, explicando a mudança e aplicando com aceitação ou pedido. Não tornar preço, promessa ou dado de cliente uma regra universal nem atualizar “verified” por inferência.

Termos jurídicos, responsabilidade, propriedade intelectual e dados não recebem cláusulas padrão automaticamente: preservar material aprovado e apontar os pontos sem definição. Esta frente não avaliou legislação ou forneceu orientação jurídica.

## Fontes primárias fixadas

- S1: [SKILL.md](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/sales-proposal-writer/SKILL.md), [licença](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/LICENSE).
- S2: [SKILL.md](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/.agents/skills/sales-proposal/SKILL.md), [estrutura](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/.agents/skills/sales-proposal/references/proposal-structure.md), [validator](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/scripts/validate-proposal.sh), [gates](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/AGENTS.md), [licença](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/LICENSE).
- S3: [SKILL.md](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/skills/sales-proposal/SKILL.md), [licença](https://github.com/zubair-trabzada/ai-sales-team-claude/blob/efef8b8a4ce8c93d8d6b4af9d1423db38f0de2ce/LICENSE).
- S4: [SKILL.md](https://github.com/ncklrs/startup-os-skills/blob/916259640e86c4cdb64e69a2aee35e78a638a487/skills/proposal-writer/SKILL.md), [diretório rules](https://github.com/ncklrs/startup-os-skills/tree/916259640e86c4cdb64e69a2aee35e78a638a487/skills/proposal-writer/rules), [pricing-presentation](https://github.com/ncklrs/startup-os-skills/blob/916259640e86c4cdb64e69a2aee35e78a638a487/skills/proposal-writer/rules/pricing-presentation.md), [README com afirmação MIT](https://github.com/ncklrs/startup-os-skills/blob/916259640e86c4cdb64e69a2aee35e78a638a487/README.md).
- S5: [original SKILL.md](https://github.com/zubair-trabzada/geo-seo-claude/blob/989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c/skills/geo-proposal/SKILL.md), [licença](https://github.com/zubair-trabzada/geo-seo-claude/blob/989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c/LICENSE), [cópia deduplicada](https://github.com/RonManatee/geo-seo/blob/5d8c0afe3b44bf9123f6849e97541f85eefabaca/skills/geo-proposal/SKILL.md).
- S6: [SKILL.md](https://github.com/phuryn/pm-skills/blob/c68487d721e419ec87af1ae6412a842978eab785/pm-product-strategy/skills/value-proposition/SKILL.md), [licença](https://github.com/phuryn/pm-skills/blob/c68487d721e419ec87af1ae6412a842978eab785/LICENSE).
- S7: [consulting-proposal](https://github.com/mohitagw15856/pm-claude-skills/blob/760fe9aea4300dbc682c42a94d8b59ad0c83b1a7/skills/consulting-proposal/SKILL.md), [client-discovery](https://github.com/mohitagw15856/pm-claude-skills/blob/760fe9aea4300dbc682c42a94d8b59ad0c83b1a7/skills/client-discovery/SKILL.md), [rate-card](https://github.com/mohitagw15856/pm-claude-skills/blob/760fe9aea4300dbc682c42a94d8b59ad0c83b1a7/skills/rate-card/SKILL.md), [licença](https://github.com/mohitagw15856/pm-claude-skills/blob/760fe9aea4300dbc682c42a94d8b59ad0c83b1a7/LICENSE).

## Limites e estado da entrega

Pesquisa documental e inspeção de fontes concluídas para esta frente; dúvidas materiais sobre método, custo, dependências e adaptação resolvidas no alcance. Não houve avaliação em execução, prova de resultado comercial, validação de segurança de todos os arquivos ou teste de integração Hermes. S4 continua com lacuna de licença para cópia. Template externo de S6, quatro rules de S4 fora do foco e exportadores de S7 não foram analisados; não sustentar decisões nesses recursos. Pacote, revisão nativa, contratação, execução real, commit e publicação não foram realizados por esta frente. A coordenação ainda consolida as três pesquisas antes da criação.
