# Especialista em CS — skills de onboarding, adoção, planos e revisões de resultados

Pesquisa da rodada 15/33, consultada em 12/10/2026. Frente: apoio **interno** à equipe de Customer Success. Este documento compara pacotes existentes e orienta uma futura skill; não cria, instala nem executa o pacote. Atendimento, envio de mensagens, realização de reuniões, escrita em contas externas e análise temática de Voz do Cliente estão fora desta frente.

## Recomendação

Usar **Stephen Rogan** como referência principal dos artefatos de trabalho; **Magnus Hedemark** para diagnóstico de adoção, contextos não-SaaS e organização sob demanda; **SuccessCOACHING/t0ddc3by** para rastreabilidade, critérios de sucesso confirmados e continuidade entre revisões. Aproveitar a passagem vendas→entrega de **Eric Risco** como checklist interno. Nenhum pacote merece adoção integral: existem benchmarks sem fonte, rotinas externas fora do escopo e inconsistências concretas.

A futura especialista deve reconhecer o pedido — preparar onboarding, revisar adoção, montar um plano, organizar uma revisão de resultados ou produzir uma atualização interna — e entregar somente o necessário. A estrutura comum é **objetivo conhecido → evidência disponível → lacuna ou barreira → próxima ação proposta → responsável/prazo confirmados ou pendentes**. Não exigir um formulário inicial inteiro, nem transformar toda solicitação em implantação de software recorrente.

## Alcance e contagens

- **14 SKILL.md lidos integralmente**, em **5 repositórios de origem distintos**: 8 Stephen Rogan, 3 SuccessCOACHING/t0ddc3by, 1 Magnus, 1 Eric Risco e 1 astDeniss.
- **12 recursos decisivos de referência/template lidos integralmente**: 8 do `product-adoption`, 3 reasoning blueprints do t0ddc3by e 1 onboarding playbook do Risco. Também consultadas seções de dois arquivos de configuração e do modelo de domínio compartilhado do t0ddc3by; não contar essas leituras parciais como revisão integral.
- **7 registros adicionais triados na descoberta**, sem revisão integral: louisblythe/customer-onboarding, KunanonJ/qbr-preparation, indranilbanerjee/qbr-plan, jshsakura/customer-success-manager, majiayu000/customer-success, Wicked Growth/qbr-builder e Argo/onboarding template.
- Diretórios consultados na descoberta: SkillMD, SkillsMP, RuleSkill, ClaudSkills e TrueFoundry Skills Registry. Consultas a skills.sh não produziram candidatos adicionais verificáveis nesta passada.
- Diretório e original não são duas evidências independentes. SkillsMP→Stephen, RuleSkill→Risco e SkillMD→candidatos originais foram deduplicados. O registro `majiayu000/claude-skill-registry` foi tratado como agregação, não como autoria independente. Não contar as dezenas de skills anunciadas pelos READMEs como lidas.
- A consulta à API pública GitHub recebeu HTTP 403 por quota; os originais foram consultados por raw e os SHAs por `git ls-remote`, sem clone, instalação, pacote remoto ou scratch. Isso preserva conteúdo e revisão, mas **não comprova a genealogia completa de forks/cópias**. Não apareceu duplicação integral entre os 14 arquivos lidos; parentesco não identificado permanece desconhecido.

As buscas combinaram profissão e entregas: customer success, onboarding, adoption, activation, success plan, QBR, EBR e internal updates, com `SKILL.md`. O objetivo foi cobrir componentes diferentes, não maximizar quantidade. A pesquisa parou ao resolver onboarding, diagnóstico, plano, revisão e material interno; retenção/saúde e métodos/vídeos são frentes coordenadas separadas.

## Origem, revisão, autoria e licença

SHAs são o HEAD observado; as datas abaixo são do **commit do repositório**, obtidas na página do commit, não datas de publicação individual de cada skill. Todas as leituras decisivas abaixo usam esse SHA, evitando depender de `main` mutável.

| Origem | SHA observado e data do commit | Autoria verificável | Licença e limite |
|---|---|---|---|
| [stephenrogan/csm-skills](https://github.com/stephenrogan/csm-skills/tree/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2) | `a080002b0c8d064793afdcdd9aa8e9bfb2170ba2`; 31/07/2026, 23:29:18 +01:00 | Stephen Rogan no frontmatter; copyright 2026 Stephen Rogan | [MIT integral consultada](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/LICENSE). Preservar copyright/licença se houver cópia ou derivação substancial. Skills selecionadas versão 1.0.0, standalone. |
| [magnus919/agent-skills](https://github.com/magnus919/agent-skills/tree/dcfba034d1b6f9692a882ff76f028b0073d009af) | `dcfba034d1b6f9692a882ff76f028b0073d009af`; 12/10/2026, 15:54:23 −04:00 | Magnus Hedemark, copyright; perfil magnus919 | [LICENSE.md MIT integral consultada](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/LICENSE.md); skill declara MIT. Não foram revisadas todas as skills irmãs. |
| [t0ddc3by/claude-for-customer-success](https://github.com/t0ddc3by/claude-for-customer-success/tree/7c10e6dbe345dbf33fbe1305362330020cebea26) | `7c10e6dbe345dbf33fbe1305362330020cebea26`; 28/09/2026, 10:46:12 −07:00 | Mantenedor t0ddc3by; copyright 2026 SuccessCOACHING | [Apache-2.0 integral consultada](https://github.com/t0ddc3by/claude-for-customer-success/blob/7c10e6dbe345dbf33fbe1305362330020cebea26/LICENSE). Preservar licença, avisos aplicáveis e registrar modificações se derivar. Não declarar auditado o pacote completo/NOTICE. Três skills versão 1.0.0, marcadas PROPOSED. |
| [ericrisco/rsc-harness](https://github.com/ericrisco/rsc-harness/tree/5343ea565c39c00d329793606e8d609da2faa004) | `5343ea565c39c00d329793606e8d609da2faa004`; 11/10/2026, 21:16:05 UTC | Eric Risco no copyright; origin `risco` | [MIT integral consultada](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/LICENSE). Frontmatter da skill não declara licença própria; a raiz cobre a consulta. |
| [astDeniss/business-skills](https://github.com/astDeniss/business-skills/tree/208245b7066f1101b09fbfd728a53717a47837d4) | `208245b7066f1101b09fbfd728a53717a47837d4`; 09/07/2026, 13:50:05 +08:00 | Conta mantenedora astDeniss; autor individual não confirmado | Sem licença no frontmatter; `LICENSE` e `LICENSE.md` retornaram 404. **Licença não confirmada**; consultar como contraste e não copiar/redistribuir texto ou templates. Não afirmar inexistência de licença em todo o repositório. |

## Inventário de leitura e contribuição

Os links apontam aos SKILL.md efetivamente lidos. O julgamento é sobre conteúdo documental; **runtime não testado em todos os casos**.

| Skill original | Contribuição concreta | Limite decisivo |
|---|---|---|
| [Rogan — onboarding-plan-builder](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/onboarding-plan-builder/SKILL.md) | Fases, marcos observáveis, responsabilidades, critérios de saída e risco de escopo | Dias e segmentos SaaS pré-fixados; >50% de usuários como critério universal; treinamento pode virar mandato. |
| [Rogan — success-plan-creator](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/success-plan-creator/SKILL.md) | Objetivo/medida/baseline/meta/prazo/dono; marcos; revisões; dependências | Exemplo de ROI 3x e percentuais ilustrativos não são metas reais; documento não se torna mútuo só por ter duas colunas. |
| [Rogan — qbr-content-assembler](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/qbr-content-assembler/SKILL.md) | Plano versus realizado, tendência e roteiro de apresentação; recomendação estratégica pode permanecer lacuna | Aceita valor estimado sem método obrigatório; exemplo mostra score de saúde apesar da regra de excluí-lo do material externo. |
| [Rogan — business-review-framework](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/business-review-framework/SKILL.md) | Revisão proporcional, uma discussão prioritária, resultado e próximos passos | ARR europeu decide formato; call/vídeo/email são execução externa fora desta frente. |
| [Rogan — qbr-action-tracker](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/qbr-action-tracker/SKILL.md) | Compromissos bilaterais, origem, dono, data, bloqueio, evidência e histórico sem apagar pendências | Cadência T+3/T+14 e escalar depois de três revisões são escolhas do autor; não enviar lembretes. |
| [Rogan — change-management-advisor](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/change-management-advisor/SKILL.md) | Diferencia conhecimento, relevância, capacidade, motivação e sustentação; conecta intervenção à barreira | Afirma que problema raramente é produto e depois que adoção não é problema de produto: hipótese inadequada como regra. |
| [Rogan — internal-debrief-writer](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/internal-debrief-writer/SKILL.md) | Resumo interno para sucessor, mudanças relevantes, pedido de ajuda e audiência | Inferir intenção pelo que alguém “quis dizer”, silêncio ou linguagem corporal pode fabricar estado da conta; componente descartado. |
| [Rogan — internal-status-update-writer](https://github.com/stephenrogan/csm-skills/blob/a080002b0c8d064793afdcdd9aa8e9bfb2170ba2/skills/internal-status-update-writer/SKILL.md) | Atualização por destinatário, mudanças relevantes e decisões/recursos necessários | Portfólio e números só se fornecidos; não criar saúde, NRR, forecast ou pipeline para preencher template. |
| [Magnus — product-adoption](https://github.com/magnus919/agent-skills/blob/dcfba034d1b6f9692a882ff76f028b0073d009af/product-adoption/SKILL.md) | Núcleo curto com mapa de recursos; distingue ativação, hábito e continuidade; quatro contextos além de SaaS | Gates 2x, 50% e duas tentativas sem calibração; referências a skills “não implementadas” não são capacidades disponíveis. |
| [SuccessCOACHING — success-plan-builder](https://github.com/t0ddc3by/claude-for-customer-success/blob/7c10e6dbe345dbf33fbe1305362330020cebea26/csm/skills/success-plan-builder/SKILL.md) | Fonte do objetivo, evidência de critério, revisão específica, histórico e acordo confirmado | Setup de perfil, flags e dependência de outras skills; escrita em armazenamento externo prevista; não assumir instalado. |
| [SuccessCOACHING — onboarding-plan](https://github.com/t0ddc3by/claude-for-customer-success/blob/7c10e6dbe345dbf33fbe1305362330020cebea26/onboarding/skills/onboarding-plan/SKILL.md) | Atualização preserva histórico; adapta papéis para implantação/parceiro/autonomia; prazo como alvo versus compromisso | Âncora contrato sempre, marcos M1–M5 rígidos e definição de TtV inconsistente com domínio compartilhado. |
| [SuccessCOACHING — qbr-builder](https://github.com/t0ddc3by/claude-for-customer-success/blob/7c10e6dbe345dbf33fbe1305362330020cebea26/csm/skills/qbr-builder/SKILL.md) | Revisa compromissos anteriores, objetivo versus resultado, fonte/data e decisão executiva | Prazos de frescor divergentes; no-config bloqueia; obriga desafio real e checklist afirma toda revisão tem desafio — isso não pode inventar problema. |
| [Risco — client-onboarding](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/client-onboarding/SKILL.md) | Handoff recupera promessa/escopo/contexto; primeiro resultado verificável; saída e dono seguinte | Percentuais de conversão/churn sem fonte e classificação por ACV; contato e acesso a contas não autorizados. |
| [astDeniss — customer-onboarding](https://github.com/astDeniss/business-skills/blob/208245b7066f1101b09fbfd728a53717a47837d4/customer-onboarding/SKILL.md) | Contraste: remover/deferir/assistir etapa de fricção, resultado versus checklist | Defaults inventam trial 14 dias, tooling e motion; checklist exige zero placeholders, incentivando preencher lacunas. Licença não confirmada. |

## Recursos decisivos consultados

Na raiz pinada de [Magnus/product-adoption](https://github.com/magnus919/agent-skills/tree/dcfba034d1b6f9692a882ff76f028b0073d009af/product-adoption), foram lidos os oito recursos referidos pelo núcleo:

1. `references/discovery-brief.md`: fronteiras e inventário; a afirmação de ausência de alternativas é descoberta do autor, não resultado desta pesquisa.
2. `references/adoption-lifecycle-concepts.md`: distinções de estágio; causalidade “adoção quase sempre precede churn” não transferida como certeza.
3. `references/non-saas-adoption-contexts.md`: serviço público, ferramentas internas, consumidor e B2B sem assinatura.
4. `references/behavior-change-and-education.md`: capacidade/oportunidade/motivação, orientação no momento de necessidade, acessibilidade; inclui explicitamente descartar falta de valor/UX/ambiente antes de prescrever treinamento.
5. `templates/adoption-plan.md`: resultado, intervenção e evidência de decisão; dez seções não obrigatórias.
6. `templates/activation-time-to-value-diagnostic.md`: sintoma, fonte/período, hipótese, evidência a favor/contra e como verificar.
7. `templates/segmentation-and-rollout-record.md`: definição de grupos comparáveis e progresso por grupo; limiares ilustrativos não são benchmarks.
8. `templates/sustained-use-review.md`: diferença entre primeira realização e repetição; janelas 30/60/90 não universais.

No [t0ddc3by](https://github.com/t0ddc3by/claude-for-customer-success/tree/7c10e6dbe345dbf33fbe1305362330020cebea26), lidos integralmente:

- `csm/skills/qbr-builder/references/reasoning-blueprint.md`: continuar revisão começa pelas promessas anteriores; explicar relevância do indicador; roadmap somente verificado. Não adotar regra “<2 fontes = draft” ou mudança >15% universal.
- `csm/skills/success-plan-builder/references/reasoning-blueprint.md`: revisão de meta, recalibração versus mudança de objetivo, meta sem baseline vira lacuna. Não comprometer estabelecer baseline em 30 dias por conta própria.
- `onboarding/skills/onboarding-plan/references/reasoning-blueprint.md`: preservar histórico e propagar efeitos de prazo; não exigir flags, perfil permanente ou five-milestone protocol.

Consultas parciais a `csm/CLAUDE.md`, `onboarding/CLAUDE.md` e `shared/cs-domain-model.md` esclareceram dependências, atribuição e TtV. Os guardrails não podem ser tratados como nomes autoexplicativos: o significado dos códigos difere entre arquivos.

No [Risco/onboarding-playbook](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/client-onboarding/references/onboarding-playbook.md), lido integralmente: handoff, packet, agenda, RACI, plano, sequência e saída. Aproveitar contexto transferido e responsável; comunicação externa e sequência de nudges ficam fora. RACI só quando a ambiguidade de execução pedir; uma coluna de responsável basta nos casos simples.

## Decisões por componente

| Fonte/arquivo → componente | Decisão | Motivo e adaptação concreta |
|---|---|---|
| Rogan `onboarding-plan-builder` + Risco `onboarding-playbook` → handoff e saída | **Adaptar** | Recuperar o vendido, escopo, restrições e objetivos já documentados. Definir saída por resultado verificável e pessoa que assume; sem executar setup, kickoff ou convite. |
| Rogan `success-plan-creator` → objetivo/medida/baseline/meta/marcos | **Aproveitar método; adaptar entrega** | Fornecer rascunho interno com campos realmente conhecidos. Meta proposta não é meta acordada; dono sugerido não é compromisso assumido. Plano só chamado mútuo quando houver evidência de aceite. |
| t0dd `success-plan-builder` + blueprint → rastrear objetivo e revisar lacunas | **Aproveitar** | Preferir material do cliente já fornecido à inferência por features; avaliar se medida pode ser verificada. Registrar fonte, data, pendência e revisão exata, sem exigir instalação de outra skill. |
| Magnus diagnostic + behavior-change → barreiras e intervenções | **Adaptar** | Testar produto, tarefa, ambiente, acesso, habilidade e relevância antes de educação. Uma hipótese com evidência insuficiente continua hipótese; não criar um programa completo para resolver uma barreira pequena. |
| Magnus non-SaaS → critérios por contexto | **Adaptar** | Consultoria/projeto pode pedir entrega e continuidade de processo; formação, aplicação do aprendizado; ferramentas internas, conclusão de tarefa; serviço público, acesso/conclusão/equidade. Métrica válida depende do objetivo e dados reais. |
| Rogan `change-management-advisor` → presumir raiz organizacional | **Descartar premissa; adaptar perguntas** | Pode haver UX, bug ou proposta sem valor. Não converter falta de uso em falta de vontade, nem rotular pessoas resistentes por inferência. |
| Magnus rollout → comparar segmentos/coortes | **Adaptar** | Usar se comportamento difere por papel, caso de uso, acesso ou período. Não forçar coortes, piloto ou implantação em ondas em toda conta. Critérios para avançar/pausar vêm do caso. |
| Rogan QBR + t0dd QBR blueprint → resultados e relevância | **Adaptar** | Preparação interna liga objetivo→baseline/meta→resultado→fonte/período→implicação→decisão necessária. Pode ser pauta, briefing ou conteúdo de slides para revisão humana; não agenda/realiza a reunião. |
| Rogan `business-review-framework` → revisão breve | **Aproveitar princípio** | Tamanho acompanha audiência, propósito, complexidade e informações, não ARR ou quantidade fixa de slides. Revisão executiva prioriza consequência/decisão; operacional, bloqueio/próxima etapa. |
| Rogan `qbr-action-tracker` + t0dd continuation QBR → continuidade | **Adaptar** | Reter compromisso confirmado, origem, prazo e evidência de conclusão; manter parcial/perdido/bloqueado visível. Proposta de ação separada de compromisso. Sem lembretes enviados ou status presumidos. |
| t0dd onboarding-plan → revisar somente mudança relevante | **Aproveitar** | Não apagar evidência histórica ao ajustar cronograma; indicar efeito em dependências. Data de referência pode ser início de projeto/kickoff/entrega, conforme contrato e contexto. |
| Rogan internal-status → atualização por audiência | **Aproveitar** | Mudança, impacto conhecido e pedido de decisão/recurso. Omitir seção sem relevância; dado ausente não significa ausência de risco. |
| Rogan internal-debrief → leitura de intenções/política | **Descartar** | Não inferir mente, intenção, saúde ou fidelidade a partir de silêncio/tom. Registro factual e hipótese explícita bastam; análise textual de VOC fica para a próxima especialidade. |
| astDeniss → defaults e programa completo obrigatório | **Descartar** | Não presumir trial, software recorrente, ACV, ferramenta ou metas. Licença não confirmada impede copiar recursos; a comparação informa crítica autoral. |
| Todas → benchmarks, ROI e pontuações prontas | **Descartar como padrão** | Número ilustrativo não demonstra causalidade nem resultado. ROI exige método, baseline, custos, período, limites e dados; evidência de uso isolada não prova dinheiro economizado. |
| t0dd → setup perfil + flags + dependências + exportação | **Descartar nesta entrega** | Contexto da conversa e arquivos fornecidos podem resolver pedido. Infere intenção, pergunta lacuna material, entrega interno; não exige modos/configuração, conectores ou publicação externa. |

## Divergências concretas que impedem transplante integral

**TtV não significa o mesmo em dois arquivos t0dd.** `shared/cs-domain-model.md` seção 5 mede contrato→M4 (primeiro valor), explicitamente distingue M5 (graduação). `onboarding-plan/SKILL.md` seção 7 calcula projeção com M5−contrato. A proposta separa primeiro resultado, graduação e tempo estimado até cada um; não reutiliza a fórmula conflitante.

**Guardrails G não têm contrato uniforme.** `qbr-builder` chama G1 frescor, G4 claims e G7 separação; o modelo compartilhado chama G1 saúde e G4 triagem. Os códigos dependem de configuração adicional. A futura skill terá linguagem explícita e curta, sem referências de códigos que possam trocar de significado.

**Frescor e confiança precisam do caso.** t0dd menciona 72 horas, 7 dias CRM, 3 dias CS, 14 dias calls e 30 dias em success plan. Uma exportação de trimestre encerrado não perde validade por envelhecer 72 horas; um bloqueio operacional pode ficar obsoleto antes. Registrar período da observação e data da fonte; perguntar atualização apenas quando altera decisão. Relato fornecido pela equipe não recebe automaticamente “baixa confiança” só por não vir de conector; corroborabilidade e precisão importam.

**QBR não exige dramatizar nem monetizar.** Rogan pede número em toda afirmação, aceita estimativas e possui exemplos incompatíveis com regras de sigilo. t0dd pede ao menos um desafio real, mas também admite nenhum obstáculo material. A síntese permite marcos qualitativos verificáveis e ausência de problemas **quando evidenciada**; não transforma desconhecimento em “está tudo bem”, nem inventa um desafio para satisfazer checklist.

**Onboarding é compatível com múltiplos contextos.** ARR, seats, trial e 30/60/90 podem servir a uma implantação SaaS específica; não definem a profissão. Um serviço recorrente, consultoria, projeto, formação ou implantação por parceiro pede objetivos, cadência e critérios próprios. Não confundir aluno que acessa conteúdo com quem aplica aprendizado, projeto provisionado com resultado realizado ou feature usada com objetivo alcançado.

## Conferência pontual com métodos primários

Não é revisão exaustiva de métodos; serve para julgar componentes decisivos e complementar a frente de métodos.

- **BJ Fogg**, [Fogg Behavior Model](https://www.behaviormodel.org/home), página do autor, sem data de publicação visível: motivação, capacidade e prompt convergem para o comportamento. Magnus escreve uma soma informal; o original não é fórmula numérica de scoring. Aproveitar diagnóstico de facilidade e sinal oportuno, sem pontuar motivação do cliente ou prometer ganho percentual.
- **Gainsight**, [guia de QBR](https://www.gainsight.com/essential-guide/quarterly-business-reviews-qbrs/), sem data visível no conteúdo consultado: comparação com objetivos anteriores, alinhamento e próximos passos. Apoia revisão orientada a resultado. Material de fornecedor; alegações de impacto comercial não foram usadas como prova nem benchmarks. O guia admite health update externo, enquanto t0dd o proíbe: para nosso escopo interno essa divergência não exige criar exportação nem regra universal.
- **Gainsight**, [Executive Business Review](https://www.gainsight.com/blog/executive-business-review/), página mostra 06/12/2022 e conteúdo referencia 2025 — indicar provável atualização sem data específica confirmada: audiência executiva e visão estratégica alteram a narrativa. Usar propósito/audiência para diferenciar EBR/QBR; não exigir calendário trimestral de todas empresas.
- **Gainsight Support**, [Success Plan FAQs](https://support.gainsight.com/gainsight_nxt/Success_Plans/FAQs/Success_Plan_FAQs), documento de produto, sem data individual confirmada: objetivos do cliente e alinhamento são relacionados, mas distintos de metas internas da empresa. Apoia manter rascunho de equipe separado de aceite mútuo; não recomenda adquirir nem implantar Gainsight.

## Proposta de núcleo e referências sob demanda

**Núcleo curto:** reconhecer entrega e aproveitar materiais; estabelecer objetivo/período/quem usará; comparar evidência com critério aplicável; identificar lacuna/barreira antes de prescrever; produzir o menor artefato útil; conferir fatos, cálculos, acordos e próximos passos. Isso funciona sem enumerar “modos” para a pessoa escolher. Uma pergunta sobre objetivo desconhecido pode ser necessária; perguntas já respondidas em contrato/notas não se repetem.

**Referências autorais futuras**, carregadas quando a tarefa precisar:

| Referência proposta | Quando ajuda | Conteúdo a sintetizar |
|---|---|---|
| `references/onboarding-and-handoff.md` | Nova relação/projeto ou falha na passagem de contexto | Escopo vendido, resultados esperados, dependências, marco inicial/saída e responsabilidade; exemplos SaaS/serviço/formação. |
| `references/adoption-diagnostics.md` | Primeiro resultado ou uso sustentado não acontece | Hipóteses com evidência a favor/contra; barreira de produto/acesso/ambiente/capacidade; intervenção proporcional e verificação. |
| `references/success-plans.md` | Criar, revisar ou corrigir plano | Objetivo→medida→baseline/meta conhecida→marco; compromisso confirmado versus proposta; histórico e recalibração. |
| `references/business-reviews.md` | Preparar QBR, EBR ou revisão breve | Objetivo e resultado, pendências anteriores, implicação e decisão; fontes/limites; agenda ou narrativa adaptável. |
| `references/internal-updates.md` | Reportar avanço/bloqueio ou pedir ajuda | Mudança relevante, evidência, impacto conhecido e necessidade; granularidade por audiência. |

Esses nomes são organização sugerida, não arquivos criados. Referências não devem reproduzir todos os templates examinados. Bibliografia, história e inventário de pesquisa ficam neste dossiê, fora do núcleo executável. Scripts só entram quando há cálculo repetitivo real e benefício demonstrado; texto/Markdown/tabelas resolvem a maior parte destes pedidos.

Se um formato exigir recurso ausente, explicar o benefício em termos de entrega e oferecer preparação simples: “Para entregar a planilha editável com fórmulas, preciso preparar esse recurso; posso cuidar disso.” Não pressupor biblioteca instalada, expor instruções de terminal ou exigir chave. Diante de recorrência e aceite, oferecer adaptação da própria skill ao modelo da equipe; não persistir regras silenciosamente.

## Casos de qualidade para futura validação

São critérios de avaliação, **não execuções realizadas**:

1. “Monte onboarding desta consultoria”: recupera escopo contratado e entrega por marcos; não pede seats/ARR/trial.
2. “Treinamos todos e ninguém usa”: diferencia treinamento realizado de capacidade/necessidade/acesso; considera defeito/UX/ambiente antes de culpar resistência.
3. “Plano com meta de 80%, baseline desconhecido”: marca baseline ausente e meta como proposta salvo evidência de acordo; não inventa uso inicial.
4. “EBR sem ROI medido”: apresenta resultado observável e limite; não converte execuções em horas/dinheiro sem método.
5. “Prepare próxima revisão, três pendências anteriores”: preserva todos os compromissos anteriores e sua evidência, sem status novo por adivinhação.
6. “Mudou a data de uma integração”: atualiza trecho afetado, dependências e histórico; não apaga o ocorrido nem promete nova data pelo cliente.
7. “Atualize liderança”: oferece documento interno proporcional e pedido concreto, usando somente estados fornecidos ou comprovados; não envia.
8. “Gere DOCX, recurso não preparado”: explica benefício e oferece preparação; núcleo de conteúdo continua útil sem executar instalação automaticamente nesta pesquisa.

## Candidatos triados sem aprofundar

| Registro de descoberta | Decisão de pesquisa |
|---|---|
| [louisblythe/customer-onboarding — SkillMD](https://skillmd.com/skills/louisblythe/customer-onboarding) | Sobreposição com onboarding lido; original e licença não confirmados nesta frente. Não usar texto do diretório como revisão do original. |
| [KunanonJ/qbr-preparation — ClaudSkills](https://claudskills.com/skills/qbr-preparation/) | Outra montagem de QBR; componentes já resolvidos por dois originais lidos. Sem avaliação integral/licença. |
| [indranilbanerjee/qbr-plan — TrueFoundry](https://www.truefoundry.com/skills-registry/skill/indranilbanerjee-digital-marketing-pro-qbr-plan) | Contexto de marketing e estratégia de cliente; não adiciona componente essencial frente aos QBRs lidos. |
| [jshsakura/customer-success-manager — SkillMD](https://skillmd.com/skills/jshsakura/customer-success-manager) | Perfil ligado a engenharia, suporte e risco; mais pertinente à frente saúde/retenção, sem leitura integral aqui. |
| [majiayu000/customer-success — GitHub](https://github.com/majiayu000/claude-skill-registry/blob/main/skills/data/customer-success/SKILL.md) | Registro agregador, origem autoral não estabelecida; não tratar como fonte independente. |
| [Wicked Growth/qbr-builder](https://www.getwickedgrowth.com/skills/qbr-builder/) | Página publica corpo de skill, mas autoria/licença de redistribuição e revisão versionada não fechadas; QBR já resolvido. |
| [Argo SaaS onboarding](https://www.try-argo.com/solutions/runtime/codex-saas-customer-onboarding-skill-template) | Starter comercial amarrado ao runtime e saída própria; não substitui pacote profissional original revisado e acrescenta dependência sem necessidade. |

## Estado de evidência e limite de entrega

Pesquisa documental verificada nos arquivos e revisões citados; textos completos das 14 skills e 12 recursos decisivos consultados. As licenças verificadas cobrem as origens indicadas, sem auditoria de todo recurso e dependência de cada repositório. Algumas configurações foram lidas por seção, como declarado. Nenhuma skill foi instalada/executada, nenhuma conta foi conectada, nenhum código remoto foi rodado, nenhum material foi enviado e nenhum dado de cliente foi fabricado.

Não há alteração de `gallery.json`, de pacote executável ou de consumidor Desktop. A proposta continua pesquisa de composição autoral: implementação futura, contratação pelo Hermes, revisão/aprovação e execução de pedido real são evidências posteriores. Origens Magnus e t0dd são compartilhadas com a frente de retenção e devem ser contadas **uma vez por repositório** na consolidação; aqui os arquivos de adoção são distintos. Push/publicação não realizados.
