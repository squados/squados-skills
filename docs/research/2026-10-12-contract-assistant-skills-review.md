# Assistente de Contratos — revisão, comparação e negociação textual

Pesquisa consultada em **12/10/2026**, para apoiar a criação posterior de uma skill interna de negócios em PT-BR. Esta frente cobre revisão de NDA/MSA/serviços/SaaS, comparação de versões e preparação de alterações; a frente de minutas/obrigações/renovações e a de fontes jurídicas brasileiras têm documentos próprios.

## Recomendação

Criar uma síntese autoral: posição da empresa, leitura completa, achados localizáveis, consequência comercial, comparação com política realmente fornecida e alteração mínima coerente com o contrato. Usar referências sob demanda por pedido. A evidência mais útil é o conjunto comercial atual da Anthropic, complementado pela disciplina de extração de Ananya e pela organização de evidências de nwwfewx. Não importar seus defaults estrangeiros, seus fluxos de CLM/assinatura ou seus formatos fixos.

O objetivo é preparar trabalho revisável para a empresa: explicar uma cláusula, apontar lacunas, comparar a contraproposta, sugerir redação ou montar uma pauta de negociação. Autoridade para aceitar riscos, validade jurídica e assinatura são decisões distintas. Uma cor ou pontuação não representa autorização.

## Alcance e rastreabilidade

Busca em inglês e português, por `contract-review`, `contract-comparison`, `redline`, `NDA`, `MSA`, `negotiation`, `SKILL.md`. Diretórios e resultados de busca serviram à descoberta; as conclusões abaixo vêm dos originais. A página dinâmica `skills.sh/?q=contract` não foi acessível pelo navegador de pesquisa. Não usei popularidade como validação. A API anônima do GitHub retornou rate limit; os pins foram obtidos com `git ls-remote HEAD`, sem clone. Leitura de texto remoto ocorreu em memória; nenhum pacote foi instalado ou executado.

Contagens desta frente: **7 repositórios aprofundados**, **10 SKILL.md completos lidos**: quatro do novo pacote comercial Anthropic, um SMB Anthropic, SaarthiOS, Ananya, nwwfewx, Kromer e comparação zubair. **8 candidatas adicionais apenas triadas**: hc938456, event4u-app, avSercanKoc, evolsb, seb1n, borghei, kesslernity e agentcounsel. Não contam como oito soluções demonstradas. O aprofundamento dos quatro módulos Anthropic é uma família, não quatro evidências independentes.

As datas abaixo são datas de consulta e pins, não datas de criação. Não consegui confirmar datas dos commits remotos pela API; quando a skill não declara versão/data, isso permanece desconhecido. SHA identifica revisão, não auditoria do repositório completo.

| Original / autoria atribuível | Revisão consultada | Licença efetivamente encontrada | Limite |
|---|---|---|---|
| [Anthropic — claude-for-legal](https://github.com/anthropics/claude-for-legal/tree/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills) | `4a6c651889c97cc9140580363c73e0eb17379c2b` | [LICENSE raiz Apache-2.0](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/LICENSE) | Autoria institucional; não atribuir autor individual sem evidência; config global referenciada não auditada inteira |
| [Anthropic — SMB contract-review](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/small-business/skills/contract-review/SKILL.md) | `02ffa99ff00ce4d3046ccebabb8357cb39f3ab06` | [LICENSE raiz contém Apache-2.0](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/LICENSE) | Texto adicional atípico ao fim da licença; não assumir inventário legal de todas as subpastas |
| [SaarthiOS](https://github.com/SaarthiOS/contract-review/tree/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review) | `1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd` | `Proprietary` no frontmatter | Ler não autoriza copiar; não portar código/templates |
| [Ananya / AI with Ananya](https://github.com/aiwithananya/contract-review-agent/tree/8d1a5f4014626b89cdf4ab3a92dd99826a5e8af7) | `8d1a5f4014626b89cdf4ab3a92dd99826a5e8af7` | [MIT, copyright 2026 Ananya](https://github.com/aiwithananya/contract-review-agent/blob/8d1a5f4014626b89cdf4ab3a92dd99826a5e8af7/LICENSE) | Somente SKILL + fallback aprofundados; demais referências listadas, sem auditoria integral |
| [nwwfewx](https://github.com/nwwfewx/contract-review/tree/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd) | `ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd` | [MIT, copyright 2026 nwwfewx](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/LICENSE) | SKILL, mapa, intake, restrições e saída lidos; checklists de asset management não auditados |
| [Kromer-Group / Claude-Legal](https://github.com/Kromer-Group/Claude-Legal/blob/9409580cdd4245c3fe8219548e133a4e90c1b366/skills/contract-review/SKILL.md) | `9409580cdd4245c3fe8219548e133a4e90c1b366` | [Apache-2.0 na raiz](https://github.com/Kromer-Group/Claude-Legal/blob/9409580cdd4245c3fe8219548e133a4e90c1b366/LICENSE) | Conteúdo muito semelhante à família histórica Anthropic; proveniência individual não comprovada |
| [zubair-trabzada / ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude/blob/19ece98df260c4c645bdd750f6e2eb48af2bd6c4/skills/legal-compare/SKILL.md) | `19ece98df260c4c645bdd750f6e2eb48af2bd6c4` | Não localizada: `LICENSE` raiz retornou 404; frontmatter sem licença | Consulta como referência; nenhum texto copiado para pacote |

O caminho antigo `anthropics/knowledge-work-plugins/legal/skills/contract-review/SKILL.md` retornou 404 em 12/10. O novo repositório existe; **não foi verificado o histórico que permitiria afirmar uma migração formal**. A issue antiga de publicação em diretório não valida o estado atual. Nenhum desses repositórios externos é automaticamente origem elegível no catálogo: a allowlist do consumidor cita `anthropics/skills`, não todos os repos da organização.

## Componentes: aproveitar, adaptar ou descartar

### Anthropic comercial atual — quatro módulos completos

Fontes: [review](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/review/SKILL.md), [vendor-agreement-review](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/vendor-agreement-review/SKILL.md), [nda-review](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/nda-review/SKILL.md), [saas-msa-review](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/saas-msa-review/SKILL.md).

| Arquivo/componente | Contribuição | Decisão e motivo |
|---|---|---|
| `review/SKILL.md` → estrutura documental | Encaminha conforme documento principal e anexos | Adaptar: estrutura é pista; conteúdo operativo confirma a rota; reconhecimento silencioso no caso claro |
| `vendor-agreement-review` → cap de responsabilidade | Separa base, dano direto/indireto, exceções e política da parte | Aproveitar como perguntas analíticas, sem aceitar um múltiplo universal |
| `vendor-agreement-review` → anexos/valor | Distingue DPA não lido de inexistente; exige valor antes de alçada monetária | Aproveitar distinção; suspender só a conclusão dependente da lacuna |
| `vendor-agreement-review` → redline mínimo | Alteração menor antes de substituir cláusula inteira | Aproveitar; preserva negociação e facilita conferência |
| `nda-review` → escopo escondido | Identifica obrigações além de confidencialidade e diferencia unilateral/mútuo | Adaptar: examinar quem divulga/recebe, não presumir mutualidade ideal |
| `nda-review` / `saas-msa-review` → thresholds | Usa posições da organização em vez de números fixos | Aproveitar; ausência de política não equivale a aprovação |
| `saas-msa-review` → AI/dados | Examina direitos explícitos, políticas incorporadas e definições | Adaptar ao uso real; sem checklist obrigatório em contrato sem esse tema |
| Config obrigatória, US provisional, CLM/DocuSign, privilege | Acoplamento a outro produto/jurisdição | Descartar defaults e automações; nunca presumir privilégio por cabeçalho |

A família diferencia risco jurídico e fricção de negócios. Usar essa distinção para explicar efeitos concretos; não repetir dois semáforos para cada frase. Há contradição operacional: uma seção manda parar no deal-breaker; outra admite revisão detalhada. A futura skill deve resolver pelo pedido, destacando impedimento cedo e continuando o trabalho autorizado quando útil.

### Anthropic SMB

Fontes: [SKILL completo](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/small-business/skills/contract-review/SKILL.md), [gotchas completo](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/small-business/skills/contract-review/reference/gotchas.md). Demais conectores e exemplo SaaS não aprofundados.

| Componente | Contribuição | Decisão |
|---|---|---|
| Documento já fornecido primeiro | Evita procurar arquivo em contas | Aproveitar |
| Leitura completa e poder de barganha | Inclui anexos e viabilidade da contraproposta | Aproveitar |
| Categorias pagamento/escopo/saída | Linguagem de negócio acessível | Adaptar conforme pedido e lado |
| Net-30 padrão, 2–3 anos confidencialidade, uncapped sempre vermelho | Defaults sem base contextual | Descartar como regra e como fonte jurídica |
| Redline com tachado/sublinhado | Representação legível | Adaptar: não chamar formatação visual de Track Changes nativo |
| HTML obrigatório e ofertas de conectores | Custo e ações alheios ao pedido | Descartar |

O exemplo de lacuna de liability em `gotchas.md` afirma efeito da lei padrão sem jurisdição. É um exemplo de por que linguagem simples não basta para qualidade jurídica. A omissão deve ser descrita como evidência textual e efeito potencial, com verificação específica quando necessária.

### Ananya

Fontes: [SKILL](https://github.com/aiwithananya/contract-review-agent/blob/8d1a5f4014626b89cdf4ab3a92dd99826a5e8af7/SKILL.md), [fallback-positions](https://github.com/aiwithananya/contract-review-agent/blob/8d1a5f4014626b89cdf4ab3a92dd99826a5e8af7/references/fallback-positions.md), ambos completos.

| Componente | Contribuição | Decisão |
|---|---|---|
| Intake por lado, valor, prazo e barganha | Calibra materialidade | Adaptar: aproveitar contexto, perguntar só lacuna relevante |
| Extraído/inferido + conflitos explícitos | Evidência sem inventar preenchimento | Aproveitar; ausência pode ser “não identificado”, sem falso vazio conclusivo |
| Preferido/fallback/troca | Negociação pronta para trabalhar | Adaptar: limites pertencem à empresa; sugestões ainda não são concessões aprovadas |
| Mesmo termo definido/numeração e correções cruzadas | Evita texto incompatível | Aproveitar |
| Thresholds fixos, rupees/dollars, caminhos `/mnt`, subagente sempre | Acoplamento e custo | Descartar obrigatoriedade |
| Escrever learnings automaticamente | Muda política durável sem revisão | Descartar como padrão |

O pacote exclui NDA; não inferir cobertura universal. A escada de fallback ajuda negociação real, mas não deve fabricar um piso de aceitação. Seus números de pagamento/incidente/renovação são propostas da fonte, não recomendações brasileiras verificadas.

### nwwfewx

Fontes completas: [SKILL](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/SKILL.md), [loading map](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/references/loading_map_and_dependencies.md), [input schema](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/references/input_schema.md), [hard constraints](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/protocols/hard_constraints.md), [output requirements](https://github.com/nwwfewx/contract-review/blob/ea38a8c97a38d86b1ad48e774f85d94f2c7ef2bd/references/output_requirements.md).

| Componente | Contribuição | Decisão |
|---|---|---|
| Arquivo/localização, consequência, redação e condição | Achado verificável e utilizável | Aproveitar estrutura conceitual |
| Mapa por gatilho | Carrega somente referências pertinentes | Adaptar; sem máquina formal de fases |
| Salvar como nova cópia em layout-lock | Preserva baseline visual | Adaptar quando pedido e ferramenta disponível |
| Falha de localização → não editar | Evita alterar trecho errado | Aproveitar |
| Assets financeiros/China e checklist universal de segregação | Especialização fora do alvo | Descartar do núcleo |
| Autor de revisões fixo `WynnSing` | Atribuição incorreta ao transplantar | Descartar; autoria explicitamente definida |
| `checklists/`, `protocols/`, `GOTCHAS.md` solto | Estrutura incompatível com galeria atual | Não contratar pacote como está |

A tabela fixa esconde a base/prioridade em apêndice salvo pedido, enquanto o núcleo pede evidência e prioridade sempre. Adaptar para manter fundamentação perto do achado. Intake não deve confundir “quem enviou o documento” com papel econômico da parte.

### SaarthiOS — análise e código estáticos, sem execução

Fontes completas: [SKILL](https://github.com/SaarthiOS/contract-review/blob/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review/SKILL.md), [clause-playbook](https://github.com/SaarthiOS/contract-review/blob/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review/references/clause-playbook.md), [scoring-rubric](https://github.com/SaarthiOS/contract-review/blob/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review/references/scoring-rubric.md), [apply_decisions.py](https://github.com/SaarthiOS/contract-review/blob/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review/scripts/apply_decisions.py). `ooxml.py`, builders, widget e demais schemas não auditados; compatibilidade geral não demonstrada.

| Componente | Contribuição | Decisão |
|---|---|---|
| Separar achado, proposta e decisão | Pessoa controla alterações | Aproveitar conceito, sem UI compulsória |
| Preservar comentários e revisões | Histórico negocial importa | Adaptar ao ambiente disponível |
| Nota 0–10 e “ready to sign” | Falsa precisão de aprovação | Descartar |
| Playbook com common law/India e “mercado” | Regra estrangeira sem contexto | Descartar transplante |
| Script de aplicação | Mostra dificuldades de OOXML | Não portar: proprietário e riscos estáticos abaixo |

Em `apply_decisions.py`, o matching escolhe a primeira ocorrência de substring, sem unicidade por cláusula. O fallback normalizado substitui o run inteiro, podendo apagar texto adjacente. `author` entra em atributo XML sem escaping. A resolução de thread ocorre antes de comprovar alteração aplicada. Há risco de mudar local errado, XML inválido ou encerrar discussão sem correção. São achados estáticos, não falhas reproduzidas. Nenhum resultado confirma preservação visual ou tratamento de outros stories do DOCX. Copiar o motor seria inadequado independentemente da licença.

### Comparação zubair e família Kromer

Fontes completas: [legal-compare](https://github.com/zubair-trabzada/ai-legal-claude/blob/19ece98df260c4c645bdd750f6e2eb48af2bd6c4/skills/legal-compare/SKILL.md) e [Kromer contract-review](https://github.com/Kromer-Group/Claude-Legal/blob/9409580cdd4245c3fe8219548e133a4e90c1b366/skills/contract-review/SKILL.md).

| Fonte/componente | Contribuição | Decisão |
|---|---|---|
| zubair → identidade A/B e versão anterior/posterior | Distingue diff de versões de comparação entre contratos | Aproveitar |
| zubair → estrutural/substantivo/cosmético | Facilita leitura das mudanças | Adaptar; número/data aparentemente cosmético pode alterar efeito |
| zubair → antes/depois e favorabilidade | Confere texto e consequência para parte | Aproveitar, sem proclamar versão melhor sem objetivo |
| zubair → resumo global obrigatório/arquivo fixo | Força decisão e pode sobrescrever | Descartar |
| Kromer → playbook e alternativa específica | Padrão útil, mas semelhante à família conhecida | Deduplicar como abordagem; não evidência independente |
| Kromer → defaults estrangeiros/market standard | Base sem fonte específica | Descartar transferência jurídica |

Semelhança de Kromer com o playbook histórico não prova autoria/fork formal. Registro como provável mesma família metodológica; conferir histórico se houver intenção de redistribuir. A busca também encontrou múltiplos nomes “contract-review” que não são necessariamente duplicatas. Não contar títulos como soluções únicas.

## Síntese autoral para orientar a futura skill

O núcleo deve reconhecer o pedido e produzir o menor resultado útil. Ler os materiais existentes antes de intake; distinguir contrato inteiro de trecho enviado, minuta de assinado, baseline aprovado de versão da contraparte. Para uma explicação localizada, não exigir diagnóstico de todo o negócio. Para revisão integral, declarar cobertura de páginas, anexos, políticas incorporadas, aditivos e qualidade da extração.

Contexto relevante: qual entidade e lado se protege; papel concreto no NDA; objeto e objetivo; versão e estado; lei escolhida e conexões reais; materiais incorporados; preço/prazo/entregáveis; capacidade operacional; políticas e cláusulas aprovadas disponíveis; histórico de concessões; quem pode aceitar mudanças. Não preencher com país inferido pelo idioma. Não presumir que um contrato chamado MSA seja só serviços.

No caso claro, escolher a rota sem oferecer menu: explicar, revisar, comparar, alterar, negociar. Conteúdo determina referências complementares. NDA não vira revisão SaaS porque aparece “dados”; MSA com SLA/DPA pede análise conjunta das interações pertinentes. Não perguntar confirmação de rota só porque a fonte estrangeira exige.

Uma entrega curta pode conter resumo executivo e tabela: localização/trecho, efeito para nossa parte, evidência/base, sugestão mínima, pendência e prioridade contextual. Separar: texto extraído; fato informado; inferência explicada; posição interna documentada; fundamento externo verificado; matéria não resolvida. “Não identificado nos materiais recebidos” difere de “o contrato não contém”.

Prioridade acompanha exposição e política: efeito, gatilho, capacidade de controlar, consequência plausível, mitigação já presente, interação com anexos e limiar aprovado. Não inventar cálculo de risco ou “red flag universal”. Nada de multiplicar severidade × probabilidade com números sem dados. Ausência de cap pode beneficiar quem demanda indenização; uma cláusula unilateral pode servir corretamente à divulgação unilateral. Parte protegida e cenário devem vir antes do juízo.

Comparação: fixar identidade, ordem e versões; alinhar cláusulas mesmo renumeradas; conferir definições e anexos; agrupar alterações correlatas; mostrar antes/depois e mudança de efeito. Não confundir paráfrase com citação. Distinguir reversão de mudança previamente aprovada, novo pedido e modificação silenciosa. Um diff textual pode auxiliar, mas não prova equivalência jurídica.

Redação: conservar termos definidos, remissões, numeração, tempo verbal e obrigações correlatas. Indicar ponto exato de inserção e ajustes dependentes. Produzir minuta/proposta autoral com lacunas visíveis, sem reproduzir bibliotecas protegidas. Cláusula aprovada fornecida tem proveniência, versão e âmbito; não modificar silenciosamente nem tratar aprovação antiga como política universal.

Negociação: pauta priorizada, pedido preferido, justificativa comercial, alternativa possível e informação necessária. Piso de aceitação e trocas exigem política ou decisão da empresa; se ausentes, apresentar opções e efeitos, sem declarar concessão aceita. Ajustar tom a barganha, relação e custo de saída; um contrato fechado pode pedir mitigação operacional em vez de redline extensa. Preparar texto para a pessoa usar não inclui enviar à contraparte.

Pesquisa jurídica: quando o pedido realmente depende de validade, efeito de lei ou jurisprudência, consultar fonte primária atual e aplicável. Se não houver base, entregar análise textual/comercial e delimitar conclusão dependente. Não herdar GDPR, DPDP, US statutes, common-law penalties ou privilege como regra BR. Referências brasileiras são responsabilidade da outra frente; esta pesquisa não emite conclusão de eficácia jurídica.

## Organização proposta, sem criar o pacote

`SKILL.md` conciso: objetivo, reconhecimento do pedido, contexto mínimo, evidência, prioridade contextual, preservação documental e entrega. Referências pequenas sob demanda: `references/revisao.md`, `references/comparacao.md`, `references/negociacao.md`, `references/formatos-e-revisoes.md`. Se métodos coincidem, manter uma regra no núcleo, não repetir em cada arquivo. A bibliografia longa permanece neste dossiê.

Sem script inicial só para automatizar o raciocínio. Um script determinístico de comparação/validação de anchors pode valer quando um caso real demonstrar ganho; um motor OOXML próprio não é requisito da skill. Reusar capacidades documentais verificadas no ambiente. Não prometer que biblioteca, Word, LibreOffice, pandoc, OCR ou visualizador estejam disponíveis. Se faltar formato pedido, entregar alternativa revisável e explicitar limite. Preservar original; controle de alterações nativo e marcação visual são formatos distintos.

## Validação futura e limites atuais

Critérios de casos reais: inverter fornecedor/cliente muda consequências; NDA unilateral apropriado não é reprovado automaticamente; política ausente não gera aprovação; anexo não recebido não vira inexistente; contrato assinado não é silenciosamente reescrito; duas ocorrências iguais não recebem alteração por matching ambíguo; contraproposta mantém remissões; conflito de versões é mostrado; confidencialidade e autoria permanecem corretas; achados citam o texto certo; lacuna de lei não vira certeza; resumo adequado ao pedido.

Somente pesquisa e análise estática realizadas. Não houve instalação, geração/aplicação de redline real, teste com contrato, validação do guard Hermes, conexão de contas, transação, envio, assinatura, commit ou publicação. Atestar JSON/empacotamento, proposta revisável, aprovação/instalação e execução real exige evidências próprias. Licenças observadas aqui não equivalem a revisão de todos os recursos nem autorizam misturar conteúdo proprietário.
