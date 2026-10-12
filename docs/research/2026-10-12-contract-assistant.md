# Assistente de Contratos — síntese da pesquisa

Rodada 29 do catálogo aprovado, consultada em 12/10/2026. Futura skill de uso interno para entender, revisar, comparar, preparar minutas e acompanhar obrigações. Pesquisa não equivale a avaliação de um contrato real, assinatura, comunicação à contraparte ou pacote executado.

## Alcance e recomendação

- [Revisão e negociação textual](2026-10-12-contract-assistant-skills-review.md): dez SKILL completos de sete repositórios, com recursos pertinentes e oito candidatas somente triadas.
- [Minutas e ciclo de vida](2026-10-12-contract-assistant-skills-lifecycle.md): cinco SKILL completos de quatro repositórios, três recursos operacionais, licenciamento e metadados de modelos.
- [Métodos e casos](2026-10-12-contract-assistant-methods.md): dezesseis registros, com conteúdo público, vídeo apenas por metadados e um acórdão não recuperado; três casos autorais.

São **quinze SKILL distintos em dez repositórios**. Anthropic comercial aparece nas duas frentes, mas com seis arquivos diferentes. Os componentes institucionais e a provável mesma abordagem histórica Kromer não são evidências independentes de eficácia; a semelhança não comprova fork formal. Pins, licenças, acesso e alcance de recursos estão nos dossiês. O 404 de um caminho antigo e a existência do novo repositório não demonstram histórico de migração.

A coordenação leu os três dossiês integralmente. Conferiu renewal-tracker completo e trechos decisivos do motor de redline Saarthi, sem execução. Foram acrescentadas três consultas primárias: [notícia STJ de 18/03/2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/18032026-Terceira-Turma-valida-emprestimo-digital-com-assinatura-em-plataforma-nao-certificada-pela-ICP-Brasil.aspx), corpo integral; [VALIDAR ITI](https://validar.iti.gov.br/), página inicial; [FAQ ITI](https://validar.iti.gov.br/duvidas.html), seções gerais e validação. São **dezenove registros contando essas consultas**, com níveis distintos, não dezenove materiais integralmente lidos. Nenhum documento foi submetido ao serviço.

## Componentes escolhidos

| Trabalho e referência | Adaptação recomendada | Ganho concreto |
|---|---|---|
| Anthropic atual: lado, política e alteração mínima | Contexto existente antes de perguntas; critérios da empresa realmente fornecidos | Risco e favorabilidade dependem da parte; semáforo não autoriza aceitação |
| Ananya: extraído/inferido, preferido/fallback | Fonte por achado e opções comerciais condicionadas | Sugestão não vira concessão aceita ou política inventada |
| nwwfewx e comparação zubair | Identidade A/B, localização, mudança de sentido e referências | Não confundir renumeração com equivalência nem editar ocorrência ambígua |
| Anthropic amendment-history | Cadeia base/aditivos, status e alcance específico | Minuta recente não substitui automaticamente documento vigente |
| Renewal-tracker e CS renewal review | Condição, envio/recebimento, data-base e evidência | Prazo não se calcula com evento ausente ou calendário presumido |
| OpenAgreements | Fatos e campos pertinentes, instrumento e conteúdo incorporado | Modelo ou capa não dispensa consultar termos; defaults estrangeiros não são decisões da empresa |
| GOV.UK e WorldCC | Obrigações com responsável, gatilho, prova e prioridade | Extrair lista é diferente de acompanhar execução; cláusulas interagem |
| Contract Design e ABA | Texto orientado à tarefa e negociação rastreável | Resumo acessível mantém ligação com o instrumento e não o substitui |

A pessoa pede uma explicação, comparação, minuta ou agenda; a skill reconhece a abordagem e entrega somente o necessário. Um pedido localizado não exige revisão integral. Uma revisão ampla declara documentos/anexos realmente cobertos. “Não localizado nos materiais” não equivale a inexistência contratual. Cláusulas fornecidas e aprovadas mantêm proveniência, âmbito e versão.

## Divergências e descartes

O [renewal-tracker Anthropic](https://github.com/anthropics/claude-for-legal/blob/4a6c651889c97cc9140580363c73e0eb17379c2b/commercial-legal/skills/renewal-tracker/SKILL.md) oferece campos úteis, mas mistura prazo inicial/corrente e envio/recebimento. Descartar rollback universal, calendário estrangeiro placeholder e trânsito presumido. Data calculada precisa da cláusula e premissas; lembrete antecipado não é deadline jurídico. Janela vencida sem registro não comprova renovação consumada.

O [motor Saarthi](https://github.com/SaarthiOS/contract-review/blob/1dc54794922a6c45a6d5ae9e007e0cc7e9d445dd/plugins/contract-review/skills/contract-review/scripts/apply_decisions.py) seleciona a primeira ocorrência, amplia um fallback ao run inteiro e interpola autoria em XML sem escaping; também resolve thread antes de confirmar alteração. A coordenação conferiu esses trechos. Constatação estática e licença proprietária impedem apresentá-lo como motor pronto; nenhum DOCX foi modificado nesta pesquisa.

Descartar padrões universais de multa, net-30, confidencialidade, responsabilidade, foro, pontuação de risco ou cláusula “de mercado” sem base pertinente. Não herdar CNPJ, assinatura, privilégio, dados de partes, lei estrangeira ou automação de conta. Tachar/sublinhar é marcação visual; não prova Track Changes nativo. Redline sugerida, aplicada e verificada são estados distintos.

## Fontes jurídicas e limites específicos

O dossiê profissional verificou [Código Civil](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm) em trechos de forma, interpretação, representação, prazo e formação; e [CPC arts. 783/784 §4º](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm). Validade do negócio, autoria/integridade e executividade exigem análises distintas. Não presumir contagem processual de dias úteis para obrigação contratual nem invalidade automática por ausência de assinatura.

A notícia STJ de março/2026 trata empréstimo e evidência de manifestação de vontade, não validade de todo contrato digital. Seu acórdão não foi consultado pela coordenação. O [ITI](https://validar.iti.gov.br/) limita o resultado à identificação do titular e integridade: não comprova alçada, equilíbrio das cláusulas ou cumprimento. A FAQ distingue assinatura digitalizada e eletrônica e admite resultado indeterminado; a home atual também menciona reconhecimento internacional. Não transformar falha de ferramenta em nulidade do negócio.

Quando uma decisão depender de efeito jurídico específico, consultar fonte primária atual aplicável e identificar a questão/documentos necessários. Trabalho textual ou comercial pode avançar independentemente. Não exigir parecer especializado para toda entrega nem improvisar conclusão sobre obrigação contestada, representação ou regime especial. Métodos estrangeiros e relatos de precedentes permanecem no contexto verificado.

## Pacote posterior e avaliação

Núcleo conciso: intenção, parte, cobertura, fatos/propostas, referência e entrega. Recursos sob demanda podem tratar comparação/redação, negociação e obrigações/datas. Bibliografia e histórico ficam nos dossiês. Nenhum script ou CLM foi necessário ao fluxo-base; ferramentas de formato precisam ser verificadas no ambiente. Dependência ausente recebe explicação simples e oferta de instalação com autorização; preferência recorrente pode motivar oferta de adaptar a própria skill.

Os [três casos autorais](2026-10-12-contract-assistant-methods.md) são fictícios e ainda não foram executados contra uma skill. Python local próprio conferiu:

1. Cenário de multa: R$400 única versus R$2.000 diária limitada; responsabilidade R$120.000 versus R$60.000, mantendo exceção. Negação equivalente não é inclusão geral de responsabilidade. Cálculo não valida a penalidade.
2. Calendário fornecido: prévia vence 15/10, resposta 14/10 e pagamento 20/10; na data solicitada 13/10 não há vencido nesses itens. Último gatilho do pagamento é a nota correta, e ausência de prova não significa descumprimento.
3. Contrato v1 e fatos cumpridos continuam referenciados; v2 expressamente minuta/condicionada permanece proposta. “15 dias” exige evento/unidade antes de fechar aquela cláusula, sem bloquear o restante do aditivo.

## Proveniência e estados pendentes

Licenças observadas MIT/Apache, titular não identificado, licença desconhecida e conteúdo proprietário estão separados por fonte. WorldCC restringe exemplos; OpenAgreements distingue código, capa e minuta. A licença do repositório não relicencia conteúdo externo. Nenhum template protegido ou pacote foi copiado.

Ainda faltam desenho final, criação, avaliação com agente/documentos autorizados, guard/proposta Hermes, instalação e uso real. Vídeo fechado, guia integral, acórdão e recursos não consultados permanecem lacunas. Sem contas, envio, assinatura, push, alteração de galeria/espelho ou chamada paga vidIQ.
