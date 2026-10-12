# Treinador de Vendedores: skills de simulação, objeções e prática

Pesquisa em 12/10/2026. Frente da pesquisa 12/33, com responsabilidade exclusiva por este arquivo. Consulta de fontes públicas e leitura de instruções; nenhuma skill instalada ou executada. Este dossiê orienta a criação posterior e não é um pacote executável.

## Resultado recomendado

O melhor reaproveitamento é combinar **a separação entre cliente e treinador de `rpg-persona`**, **o cenário coerente e a revelação progressiva de `ttai-agent`**, **o ciclo ensaiar → feedback específico → repetir de `sales-coaching`**, e **o foco em uma mudança observável de Dialfyne**. Não copiar integralmente nenhum desses fluxos: há interrupções excessivas, notas compulsórias, acesso automático a contas privadas, notas arbitrárias e exigência de urgência que conflitam com o destino.

O treinador deve reconhecer o pedido: ensaiar uma abordagem, responder a uma objeção, melhorar uma fala ou revisar um trecho. Aproveitar o contexto já fornecido; perguntar apenas o que muda a prática. Uma simulação pode começar com uma descrição curta do cliente e uma fala dele, sem menu de modos, escolha de dificuldade ou formulário completo. O vendedor responde; o agente reage de modo plausível; no ponto útil, devolve um acerto, um ajuste e uma nova tentativa. Um cliente pode concordar, pedir informação, adiar ou recusar. Comprar não é a única conclusão satisfatória.

## Alcance, busca e contagens

Foram usadas buscas em inglês e português por profissão, `sales coach`, `sales trainer`, `roleplay`, `objection handling`, prática e `SKILL.md`, em pesquisa web, skills.sh e diretórios. A skill local find-skills orientou descoberta por sinônimos e consulta à origem. Não foi usado `npx`: a pesquisa web bastou, sem instalação de CLI ou pacotes.

**12 registros de descoberta**, correspondentes a **11 linhagens candidatas** após unir o nome antigo `scenario-creator` à linhagem atual Tough Tongue. **6 fontes originais avaliadas com leitura integral do arquivo principal**: alamops, Tough Tongue, jbalbu01, revfactory, Demodesk e Dialfyne. **3 referências decisivas adicionais** de Tough Tongue lidas integralmente: `sales-roleplay.md`, `authoring.md`, `rubric.md`. Licenças integrais foram lidas em quatro repositórios GitHub. Nos dois sites sem repositório/commit identificado, não se verificou licença de redistribuição.

As 6 fontes restantes são descobertas com acesso insuficiente ou fora do escopo; não contam como skills integralmente avaliadas. Repetições do mesmo pacote em SkillMD, SkillsMP, agentescli e ClaudePluginHub não contam como evidência independente. Não se verificou genealogia textual de todos os forks possíveis; a deduplicação cobre os nomes e origens encontrados.

Não se afirma cobertura de toda a internet. A busca parou quando havia componentes suficientes para resolver contexto mínimo, encenação, objeção, feedback, repetição, diversidade B2B/B2C, ferramentas e limites de autoria.

## Registro das fontes originais

O SHA abaixo é o **commit de snapshot consultado**. A data por arquivo, quando disponível, vem do último commit que modificou o arquivo principal ou a receita indicada; não confundir com atualização de outro arquivo do repositório.

| Fonte | Autoria e licença verificadas | Snapshot e data | Arquivos efetivamente lidos |
|---|---|---|---|
| [alamops/skills — rpg-persona](https://github.com/alamops/skills/tree/c88eb23094299c3969360339dc63756bdebb38be/skills/rpg-persona) | Perfil alamops; LICENSE: Alamo Saravali, 2026, MIT | SHA `c88eb23094299c3969360339dc63756bdebb38be`; snapshot 29/09/2026. Última mudança de SKILL: 08/05/2026, commit `7c8b5673cf8876a41b2102b30ca6761b140424d8` | `skills/rpg-persona/SKILL.md` inteiro; `LICENSE` inteiro. A pasta da skill contém só SKILL.md no snapshot. |
| [Tough Tongue — ttai-agent](https://github.com/tough-tongue/toughtongue-skills/tree/47d9df1e80e7138cace77b1acae16f1c8a8e861b/skills/ttai-agent) | Tough Tongue AI, LICENSE MIT, 2026; receita com commit de Mayank Raj | SHA `47d9df1e80e7138cace77b1acae16f1c8a8e861b`; snapshot 02/10/2026. Receita sales-roleplay: 02/10/2026, commit `6ff9052722e010c79d2079e585ac29def2a68354` | SKILL inteiro; `references/recipes/sales-roleplay.md`, `references/scenario/authoring.md`, `references/scenario/rubric.md`, todos inteiros; LICENSE inteiro; árvore do repo. Demais referências e configuração de conta/runtime não auditadas. |
| [jbalbu01 — sales-coaching](https://github.com/jbalbu01/sales-enablement-plugin/tree/bb31753931f74f6b9e26e46ead4165f5e3f49d75/skills/sales-coaching) | Jose Balbuena no commit do arquivo; LICENSE MIT, copyright 2026 sem nome | SHA `bb31753931f74f6b9e26e46ead4165f5e3f49d75`; snapshot 22/02/2026. SKILL: 12/02/2026, commit `5a7078032f09abec1ae51f51e9b20dc3027aba79` | SKILL inteiro; LICENSE inteiro. Pasta da skill só contém SKILL.md no snapshot; plugin e integração MCP não executados/auditados integralmente. |
| [revfactory — objection-handler](https://github.com/revfactory/harness-100/blob/8e8d35c6a19166614d1af1df85512266d51121ae/en/48-sales-enablement/.claude/skills/objection-handler/skill.md) | revfactory no commit; LICENSE Apache-2.0, copyright 2026 Robin | SHA `8e8d35c6a19166614d1af1df85512266d51121ae`; 22/03/2026 | `en/48-sales-enablement/.claude/skills/objection-handler/skill.md` inteiro, LICENSE inteiro, árvore de paths. Versão coreana é variante da mesma linhagem e não outra evidência. |
| [Demodesk — Objection Handling](https://marketplace.demodesk.ai/skills/objection-handling) | Demodesk na página; nenhuma licença explícita encontrada no SKILL/página consultados | Página declara v2.7.3, atualização 15/03/2026. SHA Git não disponível | [SKILL.md raw](https://marketplace.demodesk.ai/skills/objection-handling/SKILL.md), 299 linhas, inteiro, e página de apresentação. |
| [Dialfyne — roleplay-coaching](https://dialfyne.com/tools/roleplay-coaching-guide) | Dialfyne; guia público/gratuito, sem licença explícita identificada no arquivo/página | Sem SHA Git, versão ou data editorial verificável no material lido; consulta em 12/10/2026 | SKILL inteiro embutido na página, 185 linhas aproximadamente, e [link raw disponibilizado](https://dialfyne.com/skills/roleplay-coaching/SKILL.md). Não há recurso de execução necessário indicado para o guia textual. |

Os dois arquivos de site foram obtidos por HTTP: o leitor web recusou o tipo `text/markdown`, mas as respostas públicas foram lidas por PowerShell. Isso não indica problema de execução da skill.

## Comparação de componentes

| Fonte/arquivo → componente | Decisão | Contribuição concreta e motivo |
|---|---|---|
| alamops SKILL → cliente e treinador com vozes separadas | Aproveitar | Preserva a encenação; comentário técnico não aparece como fala do comprador. Quando o vendedor pede pausa, responder só como treinador e retomar depois. |
| alamops SKILL → feedback em cada turno, seis campos fixos | Adaptar | O conteúdo específico ajuda, mas seis campos a cada frase quebram o ensaio e sobrecarregam. Usar poucas observações no momento útil ou a pedido. |
| alamops SKILL → persona mais cética e confirmação obrigatória | Adaptar | Aproveitar contexto/perfil existente e limitações plausíveis. Não selecionar automaticamente o cliente mais hostil nem exigir confirmação de uma hipótese simples antes de todo treino. |
| alamops SKILL → preço, alternativa, prazo, autoridade e prova | Aproveitar com contexto | São pressões comerciais úteis, desde que correspondam à oferta real. A própria fonte inclui B2C: hábito, cancelamento, privacidade, preço e expectativa criada por anúncio. |
| alamops SKILL → compra após três de seis critérios | Descartar como regra universal | Compra artificial por checklist ensina a passar no jogo. Decisão depende do caso; não ter encaixe ou orçamento continua válido mesmo com ótima fala. |
| alamops SKILL → arquivo completo de notas obrigatório | Descartar do núcleo | Uma prática breve não precisa persistir transcrição, sobretudo dados sensíveis. Gerar resumo/arquivo quando solicitado. |
| Tough Tongue authoring → cenário como ambiente de decisão | Aproveitar | Define papel, fatos, incógnitas, resistência coerente e evidência que muda a decisão; mais útil que decorar um script. |
| Tough Tongue sales-roleplay → divulgação progressiva | Adaptar | Cliente responde ao que foi perguntado e não entrega contexto todo de início. Não esconder sempre informação nem produzir incerteza artificial em todo turno. |
| Tough Tongue sales-roleplay → aceitar boa resposta, uma preocupação por vez | Aproveitar | Evita cliente eternamente resistente e mistura de dez objeções. Usar pergunta de esclarecimento quando a resposta vaga não atende à preocupação. |
| Tough Tongue sales-roleplay → números fixos de follow-ups/objeções | Descartar como exigência | Duas ou três perguntas por objeção e cinco a sete objeções totais são uma receita particular; adaptar ao pedido e duração. |
| Tough Tongue authoring → dificuldade por contexto | Aproveitar | Pressão de tempo, evidência, ambiguidade e disponibilidade de informação são mais realistas que agressividade aleatória. Calibrar pela tentativa, sem pedir ao usuário nível no menu. |
| Tough Tongue sales-roleplay → urgência obrigatória e três resultados fechados | Descartar | Não há razão universal para forçar desconto, evento ou pressão competitiva. Resultados podem ser informação, proposta condicionada, próximo passo, recusa ou adiamento. |
| Tough Tongue rubric → critérios observáveis | Adaptar | Avaliar fala/ação demonstrada e distinguir o que não houve oportunidade de observar. A plataforma exige notas ponderadas; o nosso padrão pode ser feedback qualitativo. |
| Tough Tongue SKILL → roteador para referências só quando úteis | Aproveitar a organização | Papel e intenção encaminham ao arquivo necessário; não carregar configuração técnica, telefone, conta e análises de sessões em uma prática textual. |
| Tough Tongue SKILL → MCP, voz, chamadas SIP, bots e saldo | Descartar da proposta atual | Produto externo e conta; não são dependências necessárias para treino em chat. Não testar chamadas, bots ou criar cenários no serviço. |
| jbalbu01 SKILL → tentativa, debrief específico, repetição | Aproveitar | Pequeno ciclo de prática útil ao vendedor individual; reconhecer tanto acerto quanto ajuste com base na tentativa. |
| jbalbu01 SKILL → calibrar pelo repertório observado | Adaptar | Começar com situação plausível; aprofundar se a tentativa justificar. Não presumir senioridade, produtividade, motivação ou personalidade. |
| jbalbu01 SKILL → auto-pull Gong/CRM/Slack antes de perguntar | Descartar | A presença de ferramentas não autoriza ler todas as conversas, performance da equipe ou feedback privado. Não precisa desses dados para ensaio. |
| jbalbu01 SKILL → score global, coachability e memória da pessoa | Descartar | Notas e persistência automática excedem evidência e intenção. Não diagnosticar pessoa; apontar comportamento local. |
| revfactory skill → LAER: escutar, reconhecer, explorar, responder | Adaptar | Estrutura útil para dúvida específica; esclarecer a preocupação antes de contra-argumentar, com linguagem natural. A classificação serve internamente, não como formulário obrigatório. |
| revfactory skill → gravidade/encaixe | Adaptar | Separar falta de informação de restrição de prazo/processo e incompatibilidade real; às vezes encerrar a oportunidade é correto. Sem semáforo obrigatório na conversa. |
| revfactory skill → FAQ com ISO/SOC2, integrações e retenção fictícios | Descartar | Respostas pré-escritas contêm alegações concretas sem evidência da oferta. Certificações, integração, política e prazo só podem vir do material confirmado. |
| Demodesk raw → objeção/contexto/prova/pergunta | Adaptar | Preparar resposta usando a preocupação ouvida e prova real; esclarecer antes de reenquadrar. Não transformar atraso em evasão certa, não forçar urgência e não impor 1–5. |
| Dialfyne SKILL → uma mudança, ensaio repetido e conferência de transferência | Adaptar | Conectar o treino ao trecho observado, e comparar aplicação posterior se trouxerem material. Sem agenda semanal obrigatória, três repetições fixas, notas fixas ou exigência de gravações. |
| Dialfyne SKILL → não inventar ganhos e preferir evidência | Aproveitar | Melhor fala não prova aumento de vendas. Manter resultado esperado como hipótese até existir aplicação observada. |

## Conflitos que precisam de decisão

1. **Interrupção versus fluência.** Alamops impõe coaching a cada turno; Tough Tongue mantém personagem e analisa depois; jbalbu01 ensaia e faz debrief. Para uma objeção curta, comentar a tentativa imediatamente ajuda. Em ensaio de conversa, deixar o cliente reagir e comentar na pausa ou conclusão preserva fluência. A pessoa pode pedir ajuda/recomeço a qualquer hora; não exigir que escolha um modo antes.

2. **Comprador difícil versus caricatura.** As receitas de resistência melhoram o teste contra concordância fácil do LLM, mas um cliente sempre desconfiado ou vago distorce a prática. Interesse genuíno, boa resposta e falta real de encaixe precisam afetar a reação. O treinamento não deve premiar pressão por insistência.

3. **Urgência versus verdade.** Em Tough Tongue, `authoring.md` proíbe urgência fabricada e garantias sem suporte, enquanto `sales-roleplay.md` condiciona receptividade a urgência e enumera descontos/prazos. Preservar a primeira regra; usar prazo apenas se existente no caso. Alamops já distingue prazo do cliente de urgência produzida pelo vendedor.

4. **Pontuação versus aprendizado.** As fontes usam 1–5, 1–10 ponderado, três rótulos ou critérios para fechar. Não são métricas intercambiáveis e não demonstram validade preditiva. Padrão recomendado: observação apoiada na tentativa, efeito provável com limite explícito, frase alternativa e nova tentativa. Rubrica existente da empresa entra quando fornecida; nota pedida precisa critérios claros e sem avaliação de traços da pessoa.

5. **Exploração versus leitura da mente.** Objeção pode refletir dúvida, limite real, falta de prioridade ou recusa. Tratar motivo oculto como hipótese testável, sem presumir evasão e sem classificar psicologicamente o comprador. Se não desejar explicar, respeitar a decisão.

6. **Ensaio hipotético versus material real.** Se o usuário trouxer conversa, usar seus fatos e preocupações; se pedir ensaio sem histórico, criar caso fictício explícito. Não exigir pior gravação da semana, dados de pipeline ou cliente identificável para poder praticar.

## Proposta de núcleo e referências sob demanda

**Núcleo curto:** reconhecer intenção e usar material recebido; definir objetivo e cliente com contexto mínimo; encenar um turno por vez; preservar fatos da oferta e indicar hipóteses; aceitar pausas/correção; devolver feedback específico sobre o que a pessoa disse; praticar novamente um ajuste; concluir com poucas mudanças úteis e próximo ensaio quando pertinente. Nenhuma ferramenta especial é necessária para esse núcleo.

**Referências carregadas quando o pedido exigir:** exemplos por canal e negócio; técnicas para esclarecer objeções e responder com evidência; critérios de observação de abertura, escuta, descoberta, proposta e próximo passo; desenho de treino de equipe/transferência; modelos de resumo solicitado. A bibliografia, commits e histórico permanecem neste dossiê, fora da skill executável.

Exemplos que devem orientar casos posteriores, sem virar um banco obrigatório: comércio local com preocupação de preço/prazo; serviço profissional com escopo e expectativa; venda industrial com especificação/entrega; distribuição com estoque e margem; assinatura B2C com cancelamento/hábito; B2B com outras pessoas na decisão. Nenhum pressupõe SaaS, CFO, demo ou contratação enterprise.

**Scripts e dependências:** os componentes escolhidos são instruções textuais. Não há necessidade concreta de script para ensaio ou feedback. Contagem de palavras não mede escuta, tom ou competência. Se posteriormente pedirem processamento em lote, transcrição ou gravação, avaliar benefício e dependências naquela entrega e oferecer preparação ao usuário; não instalar por iniciativa nem introduzir ferramentas de desenvolvedor na experiência.

**Melhoria da própria skill:** quando uma falha repetida mostrar lacuna concreta, oferecer um ajuste conciso e explicar o benefício. Alteração de versão/conteúdo só após pedido ou aceitação; essa oferta não substitui resolver o treino atual.

## Descobertas não promovidas a avaliação integral

| Registro e fonte | Situação e motivo |
|---|---|
| [sales-skills/sales — sales-coaching, via SkillsMP](https://skillsmp.com/skills/sales-skills-sales-skills-sales-coaching-skill-md) | Snapshot de diretório declara MIT e programa de coaching. Repo original/API/raw retornaram 404 na consulta; referências não acessíveis. Não afirmar licença atual, SHA, conteúdo integral ou redistribuição aprovada. A URL raw sugerida pelo próprio snapshot está indisponível. |
| sales-skills/sales — sales-objection-handling | Tentativa raw na origem retornou 404; existência/conteúdo atual não confirmados. Candidato de busca, sem componente extraído. |
| [scenario-creator, diretório agentscli](https://marketplace.agentscli.com/items/tough-tongue-toughtongue-skills-scenario-creator) | Nome/path antigo não existe na árvore atual. Avaliação feita no `ttai-agent` atual e receita sales-roleplay da mesma origem; não contar duas skills independentes. |
| [Agensi — Sales Call Coach Bundle](https://www.agensi.io/skills/sales-call-coach-bundle) | Página pública descreve treino, preparação e debrief, mas pacote pago não foi obtido. Apenas descoberta; autor, licença, SHA e execução não verificados. Nenhuma compra. |
| [myclaude-sh/jeremy-miner](https://github.com/myclaude-sh/jeremy-miner) | README público anuncia arquitetura/persona e pacote pago. Não foi comprado, instalado nem lido o corpus integral; não reaproveitar promessa de fidelidade, números psicológicos ou personificação de profissional. |
| [lyndonkl/claude — role-switch](https://github.com/lyndonkl/claude/blob/main/skills/role-switch/SKILL.md) | Análise de perspectivas e alinhamento, não prática comercial específica. Descoberta descartada por escopo; recursos não auditados. |

Também apareceram [eol-internal-enablement](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/eol-internal-enablement/SKILL.md), material de enablement e agentes Sales Coach. Foram encaminhados como contexto para as frentes de material/método, sem aumentar as contagens desta seleção.

## Limites e estado de entrega

- Leitura demonstra instruções e desenho, não eficácia pedagógica, melhora de conversão, segurança integral ou compatibilidade funcional no Studio.
- Os quatro repositórios MIT/Apache permitem estudar/adaptar sob suas condições, mas nenhuma cópia foi incorporada. Se houver adaptação textual substancial posterior, preservar licença e atribuição; Apache também exige avisos de alteração e NOTICE aplicável. Demodesk/Dialfyne são referências conceituais, sem permissão de redistribuição verificada.
- Nenhuma das seis fontes é um dos quatro repositórios GitHub permitidos no índice atual. Aprovação deste catálogo/profissão não altera a allowlist técnica nem converte autoria externa em SquadOS.
- Nenhuma skill foi instalada ou executada; nenhum treino real foi realizado; não houve mensagem a leads, acesso a CRM/conta privada, gravação, compra ou chamada de API comercial.
- Nenhum pacote novo, alteração de gallery.json, mirror Desktop, commit ou push nesta frente. O único entregável é este Markdown.
- Pesquisa documental da frente concluída; criação posterior e eventual validação de um pedido real permanecem etapas distintas sob a coordenação.
