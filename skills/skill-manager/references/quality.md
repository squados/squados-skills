# Qualidade de uma skill de trabalho

Use esta referência ao escrever, revisar ou avaliar um pacote. Escolha verificações que mostrem se a pessoa recebe uma entrega útil; adapte sua profundidade ao trabalho e às consequências de um erro.

## Autoria e recursos

Defina uma unidade de trabalho reconhecível, que possa atender vários pedidos relacionados e conviver com outras skills. Descreva a intenção atendida em linguagem clara. Separe método reutilizável dos dados e preferências do trabalho atual; aproveite instruções e materiais já fornecidos.

Escreva um núcleo conciso, exemplos representativos e referências com indicação direta de quando consultá-las. Modelos de saída orientam sem substituir o formato solicitado. Recursos adicionais precisam justificar seu benefício: um script pode estabilizar uma conversão ou evitar reescrever cálculos; sua mera existência não melhora o pacote.

Nas skills geradas, trate dependências ausentes com explicação acessível e oferta de instalação; adapte a execução quando houver alternativa adequada. Ofereça melhorias concretas da versão utilizada quando o fluxo revelar uma preferência recorrente. A aceitação da pessoa ou seu pedido direto orienta a alteração; confira o trecho afetado sem transformar o episódio em regra universal.

## Avalie o que a pessoa recebe

| Trabalho | Evidência útil |
|---|---|
| Copy e documentos | Adequação ao público e objetivo, clareza, fatos e condições preservados, formato utilizável |
| Dados e planilhas | Valores e fórmulas conferidos, unidades/período definidos, premissas identificadas, conclusões sustentadas |
| Apresentações e materiais visuais | Conteúdo completo, renderização legível, gráficos compreensíveis, navegação quando pertinente |
| Processo ou plano | Ações realizáveis, dependências e responsáveis conhecidos, critérios de conclusão |

Use dados fornecidos ou fontes verificáveis; diferencie recomendações de decisões aprovadas e premissas de fatos. Exemplos públicos devem ser fictícios ou autorizados. Um arquivo que abre ou uma fórmula que calcula não comprova sozinho a qualidade da entrega.

Em uma nova skill ou mudança substancial, experimente pedidos representativos. Inclua variações e um pedido vizinho que exija outra competência. Observe seleção da skill, resultado e trajetória: perguntas, referências carregadas, ferramentas usadas e custo quando disponível. Compare com a execução sem a skill quando isso ajudar a demonstrar valor. Revisão humana ou comparação sem identificar a versão pode ajudar a avaliar aspectos criativos.

Registre resultados favoráveis e falhas. Corrija a causa observada e experimente outro caso para verificar generalização. Evite testes que apenas encontram títulos ou frases nas instruções. Poucas execuções não demonstram estabilidade estatística ou economia de tokens. Uma revisão pequena pode ser verificada no trecho afetado.

## Prepare um pacote que funcione no destino

Para este repositório, use `skills/<name>/SKILL.md` com `name` igual à pasta, identificador em inglês com minúsculas, números e hífen, descrição PT-BR de uma frase e `license`. O teto editorial é 120 caracteres; confira o limite real de criação do Hermes no destino e use o menor. A distribuição preparada consultada em 12/10/2026 exige até 60 caracteres na criação nativa. Documentação e comentários em PT-BR. A descrição deve comunicar capacidade e intenção, respeitando o limite editorial local.

Confira licença, links, arquivos e requisitos. A contratação atual do Studio aceita até 100 arquivos e 4 MiB de conteúdo UTF-8, sem binários; recursos em `references/`, `templates/`, `scripts/` ou `assets/`. Avisos legais na raiz têm tratamento próprio pelo adaptador; preserve-os e confira colisões. Leia AGENTS.md e CONTRIBUTING.md do repositório e o contrato vigente do consumidor antes de acrescentar um pacote ao índice.

Reutilize um validador de formato disponível quando houver. Essa verificação cobre estrutura, não comportamento. Confira ferramentas no runtime pretendido. Quando faltar algo, siga a oferta de instalação do núcleo, respeitando a autorização existente; a política atual de instalação extra da galeria é uma condição de distribuição a verificar separadamente.

Finalize com os arquivos, verificações efetivamente executadas e limitações. Validação estrutural, guard/proposta Hermes, contratação, instalação, uso real e publicação precisam de evidências próprias; mantenha os estados ainda não demonstrados explícitos.

Referências: [avaliação de resultados](https://agentskills.io/skill-creation/evaluating-skills) e [seleção por intenção](https://agentskills.io/skill-creation/optimizing-descriptions). Consulte quando precisar aprofundar a avaliação.
