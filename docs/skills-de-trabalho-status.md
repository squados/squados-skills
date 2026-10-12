# Skills de trabalho — estado e continuação

Atualizado em 12/10/2026. Este documento é o ponto de retomada após compactação ou em uma nova sessão. Registra decisões, entregas e próximos passos; a lista definitiva está no catálogo aprovado.

## Objetivo e sequência acordada

Criar um catálogo público de skills próprias do SquadOS para o cotidiano de negócios, utilizável pelo Desktop/Studio com Hermes.

1. **Implementado e verificado localmente:** criar a skill que orienta criação, pesquisa, avaliação e melhoria das outras.
2. **Concluído:** catálogo aprovado e registrado: 33 skills em 14 áreas, de uso interno.
3. **Etapa atual:** pesquisar as escolhidas uma por uma, reunindo métodos profissionais, vídeos recentes, materiais e skills similares, com dossiês de fontes. Primeira pesquisa: Copywriter.
4. **Pendente:** após concluir as pesquisas, criar e verificar as skills uma por uma.
5. **Pendente:** publicar os pacotes neste repositório e coordenar galeria/espelho do Desktop ao final.

O usuário pediu a sequência acima. As 50 necessidades levantadas não significam 50 skills nem um ranking estatístico. Rodadas de Copywriter, Estrategista de Marketing, Criador de Conteúdo e Pesquisador de Mercado registradas e consolidadas, cada uma em três frentes paralelas autorizadas: duas de skills existentes e uma de métodos profissionais e materiais recentes. As demais 29 pesquisas e a criação dos pacotes continuam pendentes.

## Decisões aprovadas sobre o padrão

- Combinar skill-creator e writing-skills com adaptação ao nosso produto.
- Skills flexíveis: identificar intenção e escolher a abordagem automaticamente; a pessoa não precisa memorizar modos.
- Progressive disclosure: núcleo conciso e referências detalhadas carregadas conforme o pedido.
- Cada trecho deve acrescentar conhecimento útil, orientar decisões ou prevenir erros reais. Evitar repetição e conselhos genéricos.
- Perguntar pelo que altera materialmente a entrega e aproveitar o contexto existente.
- Scripts quando trouxerem benefício concreto ou economia de trabalho/tokens; preservar julgamento e criatividade.
- Dependência ausente: explicar o benefício e oferecer instalação simples, executada pelo agente quando autorizada. Comunicação adequada a pessoas não desenvolvedoras.
- Melhoria pelo uso: oferecer adaptar a própria versão da skill quando houver preferência recorrente ou atrito concreto; aplicar quando a pessoa aceitar ou pedir a alteração diretamente.
- Preferências de uma equipe não viram automaticamente padrões do pacote público.
- Avaliação proporcional, com entregas e comportamento observáveis; não montar infraestrutura sem necessidade.
- Pesquisa orientada prioritariamente pelas principais skills existentes: descobrir em diretórios, ler fontes originais e recursos pertinentes, comparar componentes e justificar o que aproveitar, adaptar ou descartar. Métodos profissionais ajudam a julgar e preencher lacunas. Popularidade não comprova eficácia; forks não são evidências independentes.
- Trabalhar na main, preservar WIP e fazer commits cirúrgicos. Publicação prevista para o final, ainda não realizada.

## O que já foi entregue

| Entrega | Arquivo | Estado |
|---|---|---|
| Levantamento de 50 necessidades e agrupamentos iniciais | [Pesquisa de necessidades](research/2026-10-12-necessidades-de-trabalho.md) | Referência histórica de pesquisa; seleção atual no catálogo aprovado |
| Pesquisa geral de autoria | [Boas práticas](research/2026-10-12-boas-praticas-de-skills.md) | 18 práticas e 15 fontes; aprovadas com os ajustes acima |
| Desenho da Criadora | [Desenho](superpowers/specs/2026-10-12-criadora-de-skills-design.md) | Aprovado e implementado |
| Plano do passo zero | [Plano](superpowers/plans/2026-10-12-criadora-de-skills.md) | Executado nativamente, com avaliações e revisão independentes |
| Pacote atual | [skill-manager](../skills/skill-manager/SKILL.md) | Três Markdown, sem scripts e sem dependências próprias |
| Catálogo escolhido | [33 skills por departamento](skills-de-trabalho-catalogo.md) | Aprovado pelo usuário em 12/10/2026; rodada de Copywriter registrada |
| Metodologia comparativa | [Atualização e validação](research/2026-10-12-skill-manager-research-validation.md) | skill-manager atualizada; revisão independente com caso sintético e checks locais |
| Pesquisa de Copywriter | [Síntese e dossiês](research/2026-10-12-copywriter.md) | Treze SKILL.md principais, doze fontes profissionais e sete vídeos identificados; acesso e lacunas discriminados |
| Pesquisa de Estrategista de Marketing | [Síntese e dossiês](research/2026-10-12-marketing-strategist.md) | Doze SKILL.md principais, nove fontes profissionais e quatro vídeos identificados; decisões, divergências e limites registrados |
| Pesquisa de Criador de Conteúdo | [Síntese e dossiês](research/2026-10-12-content-creator.md) | Dez SKILL.md principais distintos, nove fontes profissionais (sete novas) e quatro conteúdos de vídeo/webinar identificados; sobreposição contada uma vez |
| Pesquisa de Pesquisador de Mercado | [Síntese e dossiês](research/2026-10-12-market-researcher.md) | Dez SKILL.md principais, oito fontes profissionais e dois conteúdos de vídeo/podcast; transcrição recente parcial, lacunas de IBGE explícitas |
| Avaliações e limites | [Evidências](research/2026-10-12-criadora-de-skills-validation.md) | Cinco casos com/sem a nova skill, mais um caso novo; revisão independente sem achados |

O pacote foi criado como `create-work-skills` no commit `a2a92b2` e depois renomeado para `skill-manager` no commit `891709f`. As instruções mantiveram o conteúdo; nome/pasta foram atualizados. Os documentos históricos de desenho, plano e avaliação ainda usam o nome de criação. **O caminho atual para utilização é `skills/skill-manager/SKILL.md`; não recriar a pasta antiga.**

Validação: metadados, UTF-8, links, limites de arquivos/tamanho e revisão do conteúdo. No Windows, o validador existente foi executado com `python -X utf8`. As respostas observadas reforçaram ofertas de instalação e adaptação; revisão e pesquisa já eram satisfatórias no controle. O controle também consultou outra skill de autoria, portanto não representa um modelo sem orientação.

**Ainda sem prova:** ativação implícita pelo Studio, carregamento mínimo por pedido isolado, estabilidade estatística, economia de tokens, guard/proposta Hermes, contratação, instalação e uso real autenticado no Studio. Índice e espelho do Desktop não foram alterados por esta unidade. Nenhum push ou publicação foi executado nesta conversa.

## Catálogo aprovado e próximo passo

A lista atual está em [Catálogo aprovado](skills-de-trabalho-catalogo.md): 33 skills em 14 departamentos/áreas, para uso interno. O agrupamento em Operações mantém Dados, Apresentações e Planilhas. Customer Success apoia internamente a equipe com análise, planejamento e materiais. Os nomes e a seleção foram aprovados; fronteiras e ferramentas serão detalhadas na pesquisa.

O arquivo [Candidatas por departamento](skills-de-trabalho-candidatas.md) preserva a origem dos agrupamentos já ajustados à escolha. Os levantamentos iniciais continuam como histórico, não como listas de produção.

Quatro rodadas estão registradas nas sínteses acima, com três dossiês de fontes cada. O usuário aprovou o piloto Copywriter e autorizou prosseguir. O roteiro de [Pesquisa](../skills/skill-manager/references/research.md) prioriza comparar skills existentes e consolidar seus melhores componentes com rastreabilidade. O encaminhamento nas instruções reconhece a intenção automaticamente; ativação implícita pelo Studio segue não demonstrada. Nenhum modo precisa ser memorizado. Seguir uma skill por vez, usando frentes paralelas dentro dela quando úteis e autorizadas. Lacunas de vídeos/PT-BR e execução estão registradas. Próxima especialidade prevista: Especialista em SEO. Depois de concluir as pesquisas, criar e verificar os pacotes individualmente e publicar ao final.

Durante a terceira rodada, foram apresentadas duas perguntas opcionais: ritmo de revisão (seguir marcos ou revisar cada dossiê) e uso de até 50 créditos vidIQ para transcrições. Sem resposta até a quarta rodada; seguir pesquisa gratuita sequencial e registrar marcos é a hipótese de ritmo. Nenhuma chamada paga vidIQ foi feita; transcrições pagas dependem da resposta. A ausência de resposta não autoriza consumo de créditos.

Setor e porte das empresas ainda podem orientar os exemplos e a profundidade; o escopo de uso interno está fechado. Mudanças de nome, consolidação ou expansão do catálogo precisam de decisão do usuário.

## Como retomar

Leia este arquivo, as instruções globais e o par AGENTS.md/CLAUDE.md quando existir. Confira o estado atual do Git e os caminhos antes de editar. Para a próxima etapa, consulte o pacote skill-manager e o levantamento de necessidades. Atualize este documento ao fechar cada marco; preserve aqui as escolhas de catálogo quando aprovadas e links para os novos dossiês.
