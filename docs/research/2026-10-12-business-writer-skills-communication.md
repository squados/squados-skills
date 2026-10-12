# Redator de Negócios — skills de comunicação interna

Pesquisa estática em 12/10/2026 para uma futura skill interna em PT-BR. Recorte: emails de trabalho, memorandos, comunicados e mensagens sensíveis. A entrega é texto revisável; não inclui envio, publicação, monitoramento ou contas novas. Nenhum pacote foi instalado, nenhum script externo executado e nenhuma comunicação enviada.

## Alcance e seleção

Descoberta por buscas de `SKILL.md`, `business-writing`, `internal communications`, `email`, `memo` e `sensitive communications`; skills.sh e outros diretórios serviram apenas para localizar originais. Foram selecionados três pacotes por contribuição distinta: roteamento leve e FAQs; mensagens de risco com exemplos anotados; leitura rápida e consequências práticas. Não se buscou uma quota de skills. A expansão cessou quando contexto, mensagem principal, ação, tratamento de más notícias e revisão tinham componentes suficientes para comparação.

As entradas de internal-comms em claude-office-skills, Collective Brain, TrueFoundry, mozgi e outros diretórios não foram contadas: encaminham à família Anthropic ou a descrevem. Nima e RampStack compartilham técnicas comuns de redação, mas os arquivos lidos não são cópias integrais do pacote Anthropic. Isso não comprova independência de influências nem eficácia empírica.

`andrewluxem/business-writing`, `aleberriz/agent-skills/process-business-writing` e `b33kman/professional-business-writing-skill` foram descobertos e repassados à frente de briefing/revisão; não entram na contagem desta frente. [Copywriter](2026-10-12-copywriter.md), [Propostas Comerciais](2026-10-12-commercial-proposals.md) e [Assistente Executivo](2026-10-12-executive-assistant.md) foram reutilizados como pesquisas anteriores. Email de marketing pertence ao Copywriter; organização de caixa, tarefas e acompanhamento pertence ao Assistente Executivo. O recurso auxiliar email-drafting já estudado lá não é nova evidência desta rodada.

## Proveniência e acesso

HEADs verificados com `git ls-remote`, sem clone. Autor e data abaixo são do commit HEAD, obtidos no cabeçalho de seu patch público; não são a data de criação da skill. A API pública do GitHub respondeu rate limit, portanto não foi usada para afirmar última alteração específica de cada arquivo. As URLs com SHA fixam o conteúdo consultado. Os seis arquivos Anthropic lidos inicialmente em main foram comparados integralmente com a revisão fixa e coincidiram.

| ID / origem | Revisão, autor e data do HEAD | Arquivos integralmente lidos | Licença verificada |
|---|---|---|---|
| C1 — Anthropic | `dbd4588f9e1033efb41dad4bef2f7947c8993d44`; CJ Avilla; 09/10/2026 | [SKILL.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/SKILL.md), quatro examples relacionados abaixo e licença | [LICENSE.txt](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/LICENSE.txt), Apache-2.0; copyright 2026 Anthropic, PBC |
| C2 — RampStack Co. | `482c9bf74697fc1e311bd4dca5ce301f046c4b76`; Andy Dunn; 06/10/2026 | [SKILL.md](https://github.com/rampstackco/claude-skills/blob/482c9bf74697fc1e311bd4dca5ce301f046c4b76/skills/stakeholder-communication/SKILL.md), [references/update-templates.md](https://github.com/rampstackco/claude-skills/blob/482c9bf74697fc1e311bd4dca5ce301f046c4b76/skills/stakeholder-communication/references/update-templates.md), licença raiz | [LICENSE](https://github.com/rampstackco/claude-skills/blob/482c9bf74697fc1e311bd4dca5ce301f046c4b76/LICENSE), MIT; copyright 2026 RampStack Co. |
| C3 — Nima Dorostkar | `7c3729cd6d6bc4b341a03585ac8ca62c8320998b`; nima; 11/10/2026 | [SKILL.md](https://github.com/nimadorostkar/Claude-Skills-collection/blob/7c3729cd6d6bc4b341a03585ac8ca62c8320998b/skills/writing/internal-comms/SKILL.md), incluindo exemplo antes/depois; licença raiz | [LICENSE](https://github.com/nimadorostkar/Claude-Skills-collection/blob/7c3729cd6d6bc4b341a03585ac8ca62c8320998b/LICENSE), MIT; copyright 2026 Nima Dorostkar |

Estas são três SKILL.md, cinco recursos de orientação além dos SKILL.md e três licenças. C3 inclui seu exemplo no próprio SKILL.md. Conteúdo foi tratado como objeto de pesquisa, sem obedecer a instruções externas de enviar, instalar ou ampliar acessos. Licença permissiva não equivale a certificação do pacote nem transfere autoria. Incorporação material futura requer avisos e atribuição aplicáveis; esta pesquisa oferece síntese original, não um pacote redistribuído.

## Comparação por componentes

| Fonte / arquivo | Contribuição | Decisão e motivo |
|---|---|---|
| C1 / SKILL.md | Reconhecer a entrega e carregar orientação específica | **Adaptar:** reconhecimento automático pelo pedido; referências sob demanda. Não obrigar a pessoa a escolher categoria nem perguntar formato quando o pedido já o resolve |
| C1 / [general-comms.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/examples/general-comms.md) | Leitor, objetivo, tom, informações principais primeiro | **Aproveitar:** mínima orientação antes de redigir. **Adaptar:** aproveitar contexto existente e perguntar somente lacunas que alterem materialmente o texto; o roteiro de quatro perguntas não é ritual |
| C1 / [3p-updates.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/examples/3p-updates.md) | Separar realizações, planos e bloqueios no período definido | **Aproveitar:** passado/futuro/bloqueio e granularidade pelo leitor. **Descartar:** emoji e 1–3 frases obrigatórios; destaque por reações/views/hierarquia não demonstra importância. Há lapso textual que atribui realizações ao próximo período; o próprio workflow especifica passado para Progress/Problems |
| C1 / [company-newsletter.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/examples/company-newsletter.md) | Agrupar temas por impacto amplo, evitar redundância e excesso de detalhe local | **Adaptar:** só quando newsletter for a entrega. **Descartar:** assumir empresa de 1000+ pessoas, 20–25 bullets e voz “nós” sem autoria definida; obter acessos não é pré-condição para redigir com os materiais disponíveis |
| C1 / [faq-answers.md](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/examples/faq-answers.md) | Responder dúvidas com comunicações oficiais, citar origem e indicar incerteza | **Aproveitar:** respostas sustentadas e lacunas visíveis. **Adaptar:** dúvidas do público real, sem varrer toda empresa por padrão; identificar necessidade de resposta oficial não autoriza inventá-la |
| C2 / SKILL.md, cinco perguntas | Identificar destinatário concreto, contexto, relevância, pedido e meio | **Aproveitar:** ajustar detalhe ao leitor; explicar o impacto da notícia. **Adaptar:** sem estereótipo fixo de que executivo sempre quer pouco detalhe ou colaborador sempre quer muito |
| C2 / SKILL.md, inverted pyramid | Mensagem principal e efeito antes do detalhe, com apoio disponível | **Aproveitar:** ordem que preserva conteúdo principal em leitura rápida. **Adaptar:** estrutura acompanha a tarefa e o modelo existente; não imprimir Headline/So what/Ask em todo email |
| C2 / SKILL.md e update-templates.md, risco/má notícia | Dizer ocorrido, afetados, impacto, resposta, responsáveis e próximos marcos; fatos antes de tranquilizar | **Aproveitar:** franqueza respeitosa e ausência de eufemismo que esconda o problema. **Adaptar:** cada ação, prazo e próximo informe depende de compromisso real; não fabricar plano de recuperação ou assinatura de responsável |
| C2 / update-templates.md, decisão e ajuda | Pedido específico, alternativas comparáveis, motivo da recomendação e prazo | **Adaptar:** somente opções e recomendação sustentadas. Não inventar terceira opção, custo, tempo, autoridade decisória ou urgência para preencher template |
| C2 / SKILL.md, edição e falhas | Separar atividade de resultado, calibrar certeza e expor pedidos escondidos | **Aproveitar:** clareza sem certeza artificial. **Descartar:** corte universal de 30–50%, status amarelo automaticamente vermelho após três semanas e transformar toda atualização em pedido |
| C2 / SKILL.md, envio e cadência | Enviar, conferir leitura/ação e acompanhar pedidos | **Descartar do núcleo:** texto revisado não é enviado. **Adaptar:** sugestão de recorrência apenas quando útil ao pedido; agendamento e acompanhamento exigem autorização e capacidade real. A fonte diverge internamente entre atualizar só quando há novidade e manter informe mesmo sem notícia; acordos do contexto resolvem isso |
| C3 / SKILL.md | Consequência de não agir e dúvidas previsíveis; mensagem que sobrevive à leitura rápida | **Aproveitar:** explicitar efeito real para o leitor. **Descartar:** fabricar consequências, ação padrão por silêncio, limite universal de três frases/uma tela, negrito obrigatório e exatamente um pedido |
| C3 / exemplo antes/depois | Reorganizar anúncio de mudança com impacto e ação visíveis | **Adaptar com correção:** demonstra hierarquia, mas o AFTER acrescenta data de calendário, quatro de seis incidentes, RFC e contato ausentes no BEFORE. Não é evidência de preservação integral de fatos. Revisão nossa deve conferir cada dado, não herdar o exemplo como prova |

## Síntese para a futura skill

O núcleo suficiente é reconhecer o trabalho solicitado, entender para quem e para quê se escreve, aproveitar materiais existentes, escolher ordem e detalhe, produzir texto utilizável e verificar fidelidade. Mensagem principal, impacto e ação ajudam muitos pedidos, mas não obrigam cabeçalhos nem um formato único. Um email breve pode sair diretamente; comunicado com lacunas críticas pode exigir uma pergunta focada ou rascunho com pendências claras.

Ao revisar, preservar intenção, trechos aprovados, negações, condições, datas, cifras, nomes, graus de certeza e estado das decisões. Diferenciar anúncio aprovado, proposta e hipótese. Trocar “poderá” por “vai”, “não faremos” por “faremos”, data relativa por data absoluta ou plano por compromisso muda significado: só fazê-lo com evidência ou decisão explícita. Política, exceção, benefício, receita, benchmark, aprovação, assinatura e prazo não surgem para completar a estrutura.

Má notícia pede franqueza proporcional: explicar o que ocorreu, quem é afetado, o que se sabe e ainda falta saber; respeitar pessoas sem culpabilização gratuita. Planos de mitigação e canal de dúvidas só entram se fornecidos ou confirmados. Redação não produz validação jurídica, autorização de RH ou decisão executiva. A mesma informação factual deve permanecer coerente ao adaptar o texto a leitores distintos.

Referências futuras podem reunir comunicados/más notícias, atualização/decisão e exemplos anotados de revisão quando houver conteúdo suficiente. FAQs entram sob demanda. Bibliografia e comparação permanecem neste dossiê. Estratégia de marca, automação de email e operação de canais não se tornam etapas obrigatórias. Nenhum script mostrou ganho concreto neste recorte: a escolha padrão é texto e recursos leves. Se outro formato exigir dependência, verificar a disponibilidade e oferecer instalação simples somente quando necessária e autorizada, usando configuração/autenticação existentes.

Uma necessidade recorrente pode justificar oferecer adaptação da própria skill ao vocabulário/modelo aprovado da equipe; isso é uma oferta contextual, sem instalar, alterar ou agendar por conta própria. A futura validação deve observar compreensão, fidelidade e retrabalho, não prometer aumento de produtividade com métricas inexistentes.

## Casos futuros de aceitação — não executados

| Pedido / entrada | Evidência esperada |
|---|---|
| “Melhore este email aprovado sem mudar conteúdo”: contém “não enviaremos antes de 20/10”, R$ 12.500 e condição de aprovação | Mantém negação, data, valor e condição; alterações são editoriais, sem converter intenção em compromisso |
| Comunicado de atraso, sem nova data confirmada | Expõe atraso e impacto conhecido; não inventa nova data, responsável, causa ou próxima atualização |
| Aviso de política ainda em discussão | Usa linguagem de proposta; não anuncia vigência, regra ou benefício aprovado |
| Memorando pedindo decisão a leitor com pouco contexto | Expõe decisão, informação suficiente, alternativas reais e prazo conhecido; ausência permanece visível |
| Mudança cujo efeito difere por equipe | Especifica afetados e ação efetiva; não afirma que silêncio vale aprovação nem generaliza consequência |
| FAQ com três respostas oficiais e uma dúvida aberta | Mantém origem das respostas; a quarta permanece pendente, sem política inferida |
| Adaptação de uma mensagem para email e chat | Fatos e certezas coincidem; extensão acompanha meio e público, sem aplicar quotas rígidas |
| Pedido de escrever email, com autenticação disponível | Entrega rascunho utilizável; nenhuma chamada de envio e nenhuma conta criada |

## Limites

Leitura estática sustenta componentes descritos e problemas visíveis nos exemplos; não mede qualidade em produção, compreensão por leitores, tempo economizado ou resultados. Nenhum dos casos acima foi executado. A análise não auditou todos os arquivos dos repositórios, dependências de outros pacotes ou compatibilidade integral com Hermes. Os arquivos examinados são Markdown e licenças; não demonstraram necessidade de runtime próprio. RampStack e Nima estão fora da allowlist GitHub atual da galeria. Anthropic internal-comms continua com `examples/` fora da estrutura aceita: esta pesquisa não modifica o catálogo nem comprova preparo nativo. Criação do pacote, revisão, instalação e uso real permanecem etapas posteriores.
