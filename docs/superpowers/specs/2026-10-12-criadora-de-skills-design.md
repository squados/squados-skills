# Criadora de Skills de Trabalho — desenho

Data: 12/10/2026. Desenho aprovado na conversa com ajustes sobre scripts, instalação de dependências e melhoria da própria skill. Implementação pendente de revisão do plano e escolha de execução.

## Intenção e experiência

Criar e melhorar skills próprias do SquadOS para entregas reais de trabalho. O usuário pede naturalmente o que precisa; a Criadora identifica a intenção, a maturidade do material e o resultado esperado, escolhe a abordagem e carrega as referências pertinentes.

A preferência aprovada é liberdade de execução, roteamento automático e progressive disclosure. A skill ensina decisões que melhoram resultados e deixa o agente adaptar o método à tarefa. Perguntas servem para resolver informações que mudam a entrega; o contexto disponível pode resolvê-las. O usuário pode corrigir a abordagem ou determinar diretamente o resultado.

Exemplos de uso:

- “Crie uma skill de Copywriter com base nesta pesquisa”: aproveitar a pesquisa e concentrar o trabalho na autoria e avaliação.
- “Pesquise como fazer apresentações excelentes em HTML”: pesquisar e entregar a síntese solicitada; a criação do pacote pertence a uma etapa posterior neste projeto.
- “Melhore esta skill, ela pergunta demais”: investigar o atrito e fazer uma revisão proporcional, preservando o restante.
- “Este pacote serve para o Studio?”: inspecionar a compatibilidade e apresentar evidências.

O caminho escolhido é uma decisão interna do agente. A conversa usa a linguagem do trabalho e do resultado solicitado. Os exemplos orientam, sem constituir uma lista fechada de possibilidades.

## Organização mínima

Pacote previsto:

```text
skills/create-work-skills/
  SKILL.md
  references/
    research.md
    quality.md
```

`SKILL.md` contém propósito, interpretação do pedido, princípios de autoria, encaminhamento às referências e condições essenciais de entrega. Deve permanecer curto o suficiente para ser lido inteiro sem carregar a pesquisa detalhada.

Concisão é um critério de autoria: cada trecho deve acrescentar uma decisão útil, prevenir um erro concreto ou melhorar a entrega. Preservar o conhecimento necessário e retirar repetições, explicações básicas e conselhos genéricos. O tamanho acompanha o conteúdo que se mostrou útil; a orientação pública de até 500 linhas/5.000 tokens não é uma meta a preencher.

`references/research.md` orienta pesquisa profissional: fontes primárias, métodos, materiais e vídeos recentes quando relevantes, pacotes similares, atribuição e síntese aplicável. É carregado quando há pesquisa a fazer ou evidência a atualizar.

`references/quality.md` orienta avaliação do resultado e compatibilidade do pacote. É carregado quando há uma skill a criar, revisar ou verificar. Reúne exemplos de pedidos, avaliação de artefatos e verificações de distribuição no Studio.

Scripts entram quando acrescentam valor concreto ou economizam trabalho e tokens de LLM, especialmente em operações mecânicas repetidas. Critérios, raciocínio e criação continuam adaptáveis ao pedido. Modelos e recursos adicionais entram quando necessários. As referências são autorais e utilizáveis sem instalar skill-creator ou superpowers.

As referências também devem ser focadas e evitar duplicação. O núcleo indica diretamente quando carregar cada uma. Dossiês extensos de pesquisa permanecem como material de desenvolvimento; o pacote contém a síntese aplicável ao trabalho.

## Método e liberdade

O agente parte do pedido e do material existente. Pesquisa, síntese, autoria e avaliação são recursos que ele combina conforme o trabalho; a profundidade acompanha a novidade, a complexidade e as consequências da tarefa. Uma correção pequena aproveita o contexto existente, enquanto uma nova especialista exige entender seus pedidos reais e suas entregas.

De skill-creator, aproveitar escopo claro, conteúdo que acrescenta conhecimento útil e divulgação progressiva. De writing-skills, aproveitar avaliação observável e refinamento baseado em falhas demonstradas. Comparação com e sem a skill é especialmente útil para demonstrar o valor de instruções novas ou mudanças substanciais; seu uso deve justificar o esforço. A qualidade é julgada no resultado entregue, não pela reprodução de títulos ou frases.

As futuras especialistas seguem a mesma experiência: um Copywriter identifica se o pedido exige email, página ou carrossel e consulta a referência adequada. Uma especialista em apresentações reconhece audiência, propósito e conteúdo e escolhe como organizar o HTML. O usuário especifica o trabalho; o agente escolhe a execução.

Quando o uso revelar uma preferência recorrente ou uma melhoria concreta de fluxo, a skill oferece incorporar esse aprendizado na própria versão utilizada pela pessoa. A proposta explica a mudança e o benefício em linguagem simples; se a pessoa aceitar, o agente aplica a alteração pontual e verifica o trecho afetado. Aprender com uma equipe não transforma seu caso particular em regra para todas as outras. A alteração da cópia utilizada e a publicação de uma mudança no pacote público são entregas diferentes.

## Pesquisa, qualidade e compatibilidade

A pesquisa registra fontes e o que foi efetivamente consultado, distinguindo páginas, transcrições e conteúdo audiovisual. Recursos de terceiros exigem licença e atribuição adequadas. A síntese deve ajudar a fazer o trabalho; quantidade de links não é critério suficiente.

As avaliações usam pedidos representativos e critérios próprios do artefato: texto adequado ao contexto, números verificáveis, apresentação legível, recursos acessíveis e comportamento que preserva a intenção. Incluir situações incompletas e pedidos próximos ajuda a avaliar perguntas e roteamento. Se faltar ferramenta ou dado essencial, esclarecer a limitação e entregar o que puder ser sustentado.

Quando faltar uma dependência, explicar o que ela permite fazer e oferecer uma instalação simples, executada pelo agente quando autorizada. A conversa deve ser adequada a pessoas não desenvolvedoras: explicar benefício e impacto relevantes, usando nomes técnicos apenas quando ajudam a decidir. Conferir a disponibilidade após instalar e retomar o pedido. Na ausência de acesso ou autorização, explicitar o que ainda pode ser entregue. Esse comportamento se aplica às futuras skills; o critério atual da galeria sobre instalação extra continua sendo uma condição de elegibilidade a verificar, sem prometer inclusão automática de pacotes que não o atendam.

Observar também o custo da execução: perguntas desnecessárias, leituras irrelevantes, tempo e tokens quando mensuráveis. Avaliar seleção da skill e qualidade da entrega separadamente. Refinar conteúdo a partir de resultados e trajetórias observados, mantendo exemplos e detalhes que demonstram valor.

No pacote, aplicar as regras do repositório: identificador em inglês igual à pasta, descrição breve e documentação em PT-BR, licença declarada e recursos UTF-8 nas pastas aceitas. O adaptador admite até 100 arquivos e 4 MiB, sem binários. A publicação no catálogo exige conferir o contrato atual do Desktop e coordenar o espelho. Essas exigências são de distribuição, não um roteiro de interação imposto a toda tarefa.

## Aceitação

- [ ] Pedidos naturais encaminham o trabalho sem exigir que a pessoa conheça modos.
- [ ] A skill usa o contexto existente e faz perguntas quando a resposta altera materialmente a entrega.
- [ ] Referências detalhadas são carregadas conforme a necessidade do pedido.
- [ ] Núcleo e referências são concisos e acrescentam conhecimento útil sem duplicação desnecessária.
- [ ] Um pedido de pesquisa gera pesquisa; uma revisão pequena recebe uma revisão proporcional.
- [ ] A avaliação examina entregas e falhas observáveis, com esforço justificado pelo trabalho.
- [ ] Scripts propostos têm benefício concreto ou economia de tokens, preservando flexibilidade no trabalho.
- [ ] Dependência ausente gera uma explicação simples e oferta de instalação; instalação executada é verificada.
- [ ] Melhorias de fluxo identificadas podem ser propostas e incorporadas à própria skill com a aceitação da pessoa.
- [ ] O pacote é autoral, autocontido e verificável contra as regras de contratação do Studio.
- [ ] O relatório distingue verificações executadas de evidências ainda pendentes.

## Entrega e sequência

Footprint da implementação: `skills/create-work-skills/` e evidências de pesquisa/avaliação em `docs/` quando necessárias. Este passo estabelece a Criadora. A escolha definitiva do catálogo e a pesquisa das demais especialistas seguem a sequência solicitada pelo usuário. Publicação prevista ao final; ainda não realizada.

Referências: [skill-creator da Anthropic](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md), [writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md), [Agent Skills](https://agentskills.io/specification), versões locais lidas na sessão e contrato descrito em AGENTS.md/CONTRIBUTING.md deste repositório.

Pesquisa complementar: [boas práticas de autoria](../../research/2026-10-12-boas-praticas-de-skills.md), com fontes de concisão, roteamento, avaliação e estudos sobre organização dos recursos, consultadas em 12/10/2026.
