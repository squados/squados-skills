# Processo seletivo — pesquisa de skills para briefing e leitura de candidatos

Data de acesso: 12/10/2026. Dossiê autoral para futura skill interna de negócios. Escopo desta frente: análise da vaga, descrição, critérios prévios, leitura de CV e comparação explicável para revisão humana. Entrevistas, amostras de trabalho e legislação são aprofundadas nas outras frentes; este arquivo não implementa, instala nem publica uma skill.

## Conclusão

Recomenda-se combinar três componentes, em redação própria: briefing por trabalho e resultados; critérios observáveis definidos antes de olhar candidatos; leitura que liga cada afirmação ao material e separa suporte documental de verificação. Os melhores exemplos encontrados foram `job-description-writer` e `screening-rubric-builder` de SkillMedev, `candidate-qualification` de ProfileSpider e a revisão atual de `candidate-screen` de Ke-Mo. Nenhum pacote foi demonstrado em seleção real nesta pesquisa. Pesos, percentuais e classificações encontrados são propostas dos autores, sem validação preditiva demonstrada para o caso do SquadOS.

As contribuições abaixo são referências de método. Os repositórios pesquisados não pertencem à lista `github` permitida pelo catálogo atual. Pesquisa e licença não os tornam publicáveis pela galeria, nem autorizam copiar conteúdo de terceiros como autoria SquadOS.

## Alcance e rastreabilidade

Buscas em inglês por `job description`, `hiring brief`, `role scorecard`, `candidate qualification`, `resume screening`, combinadas com `SKILL.md`, GitHub e diretórios; foram também analisados candidatos encontrados em chinês. Consultados skills.sh, SkillMD e resultados de SkillsMP/RuleSkill para descoberta; a avaliação decisiva foi feita nos originais GitHub via arquivos raw. Popularidade e selos dos diretórios não foram usados como comprovação de qualidade.

Foram lidos **8 arquivos de entrada de skills em 5 famílias**, mais 2 agentes decisivos do harness, licenças e recursos discriminados abaixo. Os três pacotes SkillMedev compartilham autoria e acervo; não são três confirmações independentes. Diretórios que espelham um arquivo não contam como outra solução. A genealogia completa entre acervos não foi auditada.

Os pins são HEADs observados com `git ls-remote`, sem clone. Datas são as datas de commit consultadas no HTML do GitHub, com os fusos originais convertidos apenas quando necessário; não representam a última alteração individual de cada skill. A API anônima respondeu rate limit, por isso não foi obtido histórico por arquivo. Onde houve 404, não se afirmou leitura do pacote.

| Família e autoria | Pin observado e data de commit | Entradas lidas integralmente | Recursos decisivos e limite |
|---|---|---|---|
| SkillMedev/skills; licença atribui Alexander Ouellet | `6b3044d569595b481a3677da8f68af7aa239dc09`; 04/10/2026, -07:00 | `skills/job-description-writer/SKILL.md`, `skills/jd-bias-scrubber/SKILL.md`, `skills/screening-rubric-builder/SKILL.md` | README para localização e LICENSE MIT. Essas entradas não apontam recursos locais necessários. Não auditada a totalidade do acervo. |
| spiralcrew-ou/profilespider-agent-skills; frontmatter ProfileSpider, copyright SpiralCrew | `6c65d0507687364704a180476613b72467028e87`; 21/06/2026, +02:00 | `candidate-qualification/SKILL.md` | README e LICENSE MIT; versão interna 1.0. Entrada autossuficiente, sem script obrigatório. |
| oukeming64-tech/candidate-screen; copyright Ke-Mo | `9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd`; 05/10/2026, +08:00 | `SKILL.md` atual em chinês | README, LICENSE MIT, `evals/cases.md` e `evals/validation.md`. Não lidos integralmente inputs/observed nem variante inglesa; resultados tratados como relato do mantenedor. |
| RefoundAI/lenny-skills; curadoria Refound AI, fontes atribuídas a Lenny Rachitsky e convidados | `13598cc54e09399bc1bc1398b0fca284110efb2f`; 15/07/2026, -07:00 | `skills/hiring-product-talent/SKILL.md` | `references/artifacts.md` integral, LICENSE e README. `guest-insights.md` apenas trecho inicial; vídeos, transcrições e newsletters originais não conferidos. |
| revfactory/harness-100; licença copyright Robin | `8e8d35c6a19166614d1af1df85512266d51121ae`; 23/03/2026, +09:00 | `en/90-hiring-pipeline/.claude/skills/hiring-pipeline/skill.md`, `.../competency-model/skill.md` | Agentes `jd-writer.md` e `screening-expert.md` integrais, LICENSE Apache-2.0. Demais agentes e pacote completo não auditados. |

Links permanentes e licenças estão na bibliografia. O último pin é de um harness com vários artefatos, não de um pacote simples pronto para contratação.

## Comparação por componente

Legenda: **aproveitar** = princípio pertinente para síntese própria; **adaptar** = precisa de mudança explícita; **descartar** = não entra no método padrão. Nenhuma decisão equivale à aprovação de redistribuição do pacote.

| Fonte/arquivo → contribuição | Decisão | Motivo e adaptação concreta |
|---|---|---|
| [SkillMedev job-description-writer](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/job-description-writer/SKILL.md) → resultados, nível, requisitos essenciais/desejáveis, logística e responsável | Aproveitar/adaptar | Boa entrada para briefing. Usar resultados e contexto que o usuário já informou; perguntar somente lacuna que altera a entrega. Números fixos de requisitos/palavras e regra de amplitude salarial são heurísticas sem demonstração nesta pesquisa; não impor. Faixa não informada fica pendente. |
| [SkillMedev jd-bias-scrubber](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/jd-bias-scrubber/SKILL.md) → frase problemática, motivo, alternativa, intensidade | Aproveitar/adaptar | Revisão textual específica e rastreável, sem alteração silenciosa. Descartar a estatística HP 60%/100% e generalizações sobre anos de experiência: primários não conferidos. Não importar rótulos jurídicos dos EUA nem declarar texto legal/publicável. Preservar exigências materiais justificadas; consultar responsável quando mudar intenção. |
| [SkillMedev screening-rubric-builder](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/skills/screening-rubric-builder/SKILL.md) → critério observável, âncoras, evidência e regra anterior aos CVs | Aproveitar/adaptar | Escrever a ligação vaga→critério→evidência antes da leitura. Ausência de evidência é estado próprio, nunca nota mínima. Pesos opcionais explicitam prioridades do solicitante, sem alegar previsão validada; nenhuma linha de corte opera decisão. Concordância de avaliadores exige observação, não declaração automática. |
| [ProfileSpider candidate-qualification](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/candidate-qualification/SKILL.md) → somente requisitos declarados; critérios iguais; lacunas distintas de falha; auto-relato a verificar | Aproveitar/adaptar | Mais claro sobre informações ausentes. Sua exceção para lacunas marcadas como eliminatórias precisa de cuidado: o requisito pode ser essencial, mas desconhecido continua desconhecido. Retirar score sem escala e campos vagos de risco. Produzir evidência, cobertura e perguntas para pessoa responsável, sem aplicar aprovação/recusa. |
| [Ke-Mo candidate-screen atual](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/SKILL.md) → leitura cruzada, contribuição pessoal/equipe, suporte versus verificação, isolamento por candidato | Aproveitar/adaptar | Útil para esclarecer alegações de resultado e autoria. Separar falta de dado, contradição e declaração explícita. Não deduzir mentira/personalidade. Adaptar metáforas ao PT-BR e escopo profissional; análise de contribuição não mede caráter. Não abrir links pessoais ou investigar alguém por implicação. |
| [Refound hiring-product-talent](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/hiring-product-talent/SKILL.md) e `artifacts.md` → propósito da contratação, trabalho concreto, transparência | Adaptar/descartar | Aproveitar o papel da vaga no negócio e exemplos concretos de trabalho. Não generalizar preferências de startups, intelecto, fundadores ou entusiasmo como critérios universais. Descartar inferência por gênero/localidade para oferta, interação com família e linguagem de pessoa excepcional sem critério observável. |
| [harness hiring-pipeline](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/en/90-hiring-pipeline/.claude/skills/hiring-pipeline/skill.md) → encadeamento briefing→critérios→entrevista | Adaptar | Ajuda a preservar coerência entre entregas. Não importar 5 agentes, workspace obrigatório e pipeline completo para pedido pequeno. A tradução inglesa está degradada; não serve como texto executável confiável. |
| harness `jd-writer.md`/`screening-expert.md`/`competency-model` → competência, nível, método de avaliação | Adaptar/descartar | Aproveitar a ligação competência→evidência. Descartar pesos universais, taxas pretendidas de passagem, qualidade estética do CV e nota total automática; podem refletir apresentação e decisões arbitrárias. Recursos dependem do harness e estrutura `.claude`, fora do formato simples pretendido. |
| [ClawPod resume-screening](https://github.com/clawpod-app/awesome-openclaw-agent-packs/blob/60c78255d16cafddb831eb60929111fdaf420e6e/packs/recruiting/skills/resume-screening/SKILL.md) → resumo tabular e divisão essencial/desejável | Descoberta suplementar; descartar classificação pronta | SKILL completo e LICENSE raiz consultados. MIT com aviso de porções derivadas Apache-2.0; origem dessa skill específica não estabelecida. “Faltam dois essenciais” não justifica categoria negativa quando o CV apenas omite dados. Top-5 e pesos sem âncoras acrescentam falsa certeza. Não contado entre as cinco famílias principais. |

## Divergência material entre diretório e fonte atual

Em `candidate-screen`, o resultado de busca e o raw recuperado pelo buscador mostraram uma versão anterior com julgamento intuitivo, metáfora de autenticidade e recomendações de passagem/retenção/eliminação. A leitura HTTP direta de HEAD mostrou revisão substancial: auditoria das alegações, sem pontuação pseudoprecisa ou eliminação automática. A pesquisa adotou **o pin atual**, não a descrição em cache. O README atual também exclui contato, investigação e alteração de ATS. [Fonte atual](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/README.md).

O relatório de validação de 05/10/2026 declara três grupos sintéticos, uma execução por grupo, sem repetição ou contraste cego com a versão antiga. É evidência limitada relatada pelo mantenedor, não comprovação de acurácia ou justiça em contratação real. [Relato e limitações](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/evals/validation.md).

`writing-job-descriptions` de Refound apareceu em [skills.sh](https://skills.sh/refoundai/lenny-skills/writing-job-descriptions), mas caminho atual e dois prefixos antigos encontrados em diretório retornaram 404. O espelho `majiayu000/claude-skill-registry` também retornou 404 no raw consultado. Isso é lacuna de acesso, não defeito demonstrado da técnica. Em vez de atribuir leitura completa ao espelho, a comparação usou `hiring-product-talent` atual, que contém a contribuição por resultados.

## Método profissional que resolve a lacuna do briefing

A [OPM, Job Analysis](https://www.opm.gov/policy-data-oversight/assessment-and-selection/job-analysis/) orienta relacionar tarefas realizadas, competências necessárias e a conexão entre ambas. A contribuição aqui é a sequência trabalho→competência→avaliação, anterior a preferência por uma pessoa. Página sem data de publicação visível; acesso em 12/10/2026. Trata-se de orientação de órgão federal dos EUA, não regra jurídica brasileira.

O [O*NET Content Model](https://www.onetcenter.org/content.html) organiza informação ocupacional entre trabalho, requisitos e contexto. Pode ajudar a formular perguntas quando a função é desconhecida. Uso proposto: consultar somente tarefas/conhecimentos pertinentes e validar com o gestor; não copiar médias ocupacionais como descrição exata da empresa nem inferir interesses/traços do candidato. Não houve importação da base ou aplicação de instrumento psicológico; eventual reutilização de dados requer conferir a licença do dataset específico.

## Proposta de organização para a futura skill

Esta é uma síntese de desenho, não o pacote executável.

**Núcleo curto:** reconhecer se a intenção é criar/revisar vaga, desenhar critérios ou ler materiais; aproveitar contexto já presente; entregar a menor peça útil. Para vaga, esclarecer resultado e nível. Para CV, reconhecer o escopo do material e vincular afirmações a critérios previamente declarados. Quando o usuário pede comparação, explicitar esses critérios e apresentar cobertura e lacunas para análise humana. Não produzir decisão de emprego, inferir atributos sensíveis nem tratar material de candidato como instrução.

**Referências sob demanda:** briefing de vaga com um exemplo de negócio; revisão de linguagem com justificativa; matriz de evidência e cobertura; contribuição pessoal/equipe e números de resultados. Templates somente quando o formato ajuda a execução. Scripts não são necessários para estes pedidos textuais; um agregador só se justifica depois de demonstrado benefício num lote e nunca aplica nota/corte automaticamente.

Formato autoral sugerido para o briefing:

| Trabalho/resultados | Competência necessária | Evidência aceitável | Essencial na entrada ou aprendível | Onde avaliar |
|---|---|---|---|---|
| Resultado que o gestor descreveu | Capacidade relacionada ao resultado | Exemplo observável e verificável | Justificativa do gestor | CV, conversa estruturada ou exercício |

Formato autoral sugerido para análise de materiais:

| Critério e justificativa | Material e localização | O que sustenta | Estado da informação | Limite e esclarecimento |
|---|---|---|---|---|
| Critério declarado antes da análise | Nome de arquivo e seção; página apenas se real | Afirmação factual, sem extrapolação | Presente; parcial; não informado; contraditório; ausência explicitamente declarada | Pergunta específica para revisão humana |

Esses estados são documentação, não categorias de pessoa. “Contraditório” requer apresentar as duas posições sem inventar explicação nem concluir desonestidade. “Presente” não equivale a autenticidade confirmada. Se faltar dado essencial, registrar a necessidade de esclarecer; não converter para zero, reprovação ou eliminação.

Exemplo sintético: vaga de analista financeiro exige conduzir fechamento mensal. Material A descreve conciliações e apoio ao fechamento; não informa responsabilidade final. Registro adequado: evidência parcial, autoria do fechamento não informada, esclarecer escopo e exemplo. Um material B mais detalhado possui maior cobertura documental naquele critério; isso não prova que A tem menor competência.

Para revisão posterior, casos sintéticos devem cobrir CV sem números, experiência transferível, autoria compartilhada, informação ausente, requisito explicitamente não atendido, conflito de datas e instrução hostil dentro do documento. Troca de nome/foto/idade e melhora estética com fatos iguais não devem mudar a leitura de competência. Isso é proposta de teste, ainda não execução ou resultado.

## Licenças, adaptação e limites

MIT foi confirmado nos textos originais de SkillMedev, SpiralCrew e Ke-Mo; copiar/adaptar conteúdo substancial requer preservar atribuições e licença. O frontmatter de algumas entradas não contém `license`, embora a raiz a forneça; não se deve copiar e declarar automaticamente conformidade com o contrato do SquadOS.

No Refound, [README](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/README.md) delimita MIT à estrutura e organização, e mantém o conteúdo subjacente de Lenny/convidados como propriedade desses autores. O LICENSE raiz, sozinho, não resolve redistribuição de falas, transcrições ou técnicas protegidas. Usar raciocínio autoral e links; não incorporar a biblioteca de citações. No harness, Apache-2.0 foi lido; `NOTICE` e conteúdo completo não auditados, logo redistribuição continua sem parecer de pacote.

Nenhum acesso a CV real, contato, anúncio, rejeição, ATS, scraping de perfis pessoais, instalação, execução remota ou contratação ocorreu. A pesquisa também não prova compatibilidade Hermes/Studio, pacote até 100 arquivos/4 MiB, ausência global de dependências ou segurança do repositório completo. Tudo isso pertence a gates posteriores se houver decisão de implementar/publicar.

## Bibliografia de fontes originais consultadas

- [SkillMedev — repositório no pin](https://github.com/SkillMedev/skills/tree/6b3044d569595b481a3677da8f68af7aa239dc09), [LICENSE](https://github.com/SkillMedev/skills/blob/6b3044d569595b481a3677da8f68af7aa239dc09/LICENSE). Entradas relevantes linkadas na matriz.
- [ProfileSpider — entrada](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/candidate-qualification/SKILL.md), [LICENSE](https://github.com/spiralcrew-ou/profilespider-agent-skills/blob/6c65d0507687364704a180476613b72467028e87/LICENSE).
- [Ke-Mo — entrada](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/SKILL.md), [casos](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/evals/cases.md), [LICENSE](https://github.com/oukeming64-tech/candidate-screen/blob/9b1417b0f38e7d44c7cb6aeb0f2dd065c9f5fcfd/LICENSE).
- [Refound — artefatos](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/hiring-product-talent/references/artifacts.md), [insights: leitura parcial](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/skills/hiring-product-talent/references/guest-insights.md), [LICENSE](https://github.com/RefoundAI/lenny-skills/blob/13598cc54e09399bc1bc1398b0fca284110efb2f/LICENSE). Vídeos apenas indicados pelo acervo, sem consulta audiovisual/transcrição nesta frente.
- [Harness — modelo de competências](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/en/90-hiring-pipeline/.claude/skills/competency-model/skill.md), [agente JD](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/en/90-hiring-pipeline/.claude/agents/jd-writer.md), [agente triagem](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/en/90-hiring-pipeline/.claude/agents/screening-expert.md), [LICENSE](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/LICENSE).
- [ClawPod — LICENSE com ressalva de derivações](https://github.com/clawpod-app/awesome-openclaw-agent-packs/blob/60c78255d16cafddb831eb60929111fdaf420e6e/LICENSE).
- Descoberta secundária: [SkillMD, ClawPod](https://skillmd.com/skills/clawpod-app/resume-screening), [Manifest, Refound antigo](https://manifest.manifold.security/skills/skills.sh/refoundai/lenny-skills/writing-job-descriptions), [SkillsMP, zweien](https://skillsmp.com/ko/skills/zweien-resume-screening-skill-md), [RuleSkill, recruiter](https://ruleskill.com/skills/theneoai/recruiter). Os dois últimos ficaram na descoberta: originais completos não lidos, sem inclusão na comparação decisiva.
