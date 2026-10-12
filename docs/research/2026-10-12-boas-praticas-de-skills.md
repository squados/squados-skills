# Boas práticas de autoria de skills de trabalho

Consulta: 12/10/2026. Pesquisa complementar ao desenho da Criadora. Fontes primárias: documentação de autoria e estudos dos próprios pesquisadores. As aplicações ao SquadOS são recomendações editoriais, ainda sem avaliação no Studio.

## Conclusões aplicáveis

| Prática | Aplicação no nosso padrão | Fonte |
|---|---|---|
| Acrescentar conhecimento que muda decisões | Selecionar métodos e detalhes úteis; retirar explicações básicas e conselhos genéricos | [1], [2] |
| Concisão em toda a árvore de recursos | Entrada curta e referências focadas; carregar detalhes apenas quando pertinentes | [1], [2] |
| Indicar quando consultar cada referência | Rotear pelo pedido: emails, carrosséis, análise ou apresentação; manter links diretos e claros | [2] |
| Preferir um caminho padrão adaptável | O agente escolhe a execução; o usuário pede o resultado em linguagem natural | [1] |
| Preservar detalhes que evitam erros reais | Manter convenções de saída e problemas recorrentes que o agente não reconheceria sozinho | [1] |
| Usar exemplos representativos | Exemplos concretos ensinam o padrão; modelos de artefato permanecem adaptáveis | [2] |
| Verificar seleção e qualidade separadamente | Um pedido pode carregar a skill certa e ainda gerar um resultado ruim; avaliar ambas as coisas | [3], [4] |
| Avaliar eficiência além do resultado | Observar perguntas, leituras, tempo e tokens quando disponíveis; remover trabalho sem ganho demonstrável | [4] |

## Concisão e progressive disclosure

O corpo da skill ocupa contexto quando é carregado. A documentação recomenda até 500 linhas e cerca de 5.000 tokens como orientação de organização, não como tamanho ideal a preencher [1]. Esses números não são uma meta editorial para o catálogo.

Nossa síntese: escrever a menor instrução que preserva qualidade, decisões úteis e verificações necessárias. Uma pesquisa extensa pode fundamentar uma skill curta. A bibliografia e o histórico de desenvolvimento ficam nos dossiês; o pacote executável recebe o conhecimento que ajuda a realizar a tarefa e referências pertinentes.

Exemplo autoral para uma referência de copywriting: “Para emails, consulte `references/email.md`; para carrosséis, consulte `references/carousel.md`.” O roteamento deve resolver o pedido automaticamente. A referência de email deve acrescentar decisões e exemplos do formato, sem repetir todo o núcleo da skill.

A revisão pode perguntar: este trecho muda uma decisão, previne um erro concreto ou melhora a entrega? Se seu valor for incerto, comparar a execução com e sem ele pode ajudar. Concisão preserva detalhes necessários; textos vagos também provocam tentativas, perguntas e consumo de contexto.

## Evidência empírica e limites

O artigo de lançamento do SkillsBench relata maior ganho para skills compactas do que para documentação abrangente nos experimentos do snapshot histórico paper-v1 [5]. Também relata tarefas prejudicadas pelo uso de skills. É evidência a favor de concisão e avaliação por tarefa, não demonstração de que toda skill curta é melhor, nem regra de quantidade de skills. O próprio texto apresenta contagens de tarefas com efeitos negativos que divergem entre legenda e corpo; não reutilizamos essas contagens como resultado consolidado.

SkillJuror compara organização com conhecimento controlado em 82 tarefas, com 410 tentativas pareadas. Relata 17 aprovações adicionais com progressive disclosure, com benefício dependente da tarefa [6]. A organização altera o uso de recursos, mas não garante economia de tokens ou ganho de qualidade em todos os trabalhos. Devemos observar quais arquivos são efetivamente lidos e se ajudam a entrega.

## O que aproveitamos com adaptação

A recomendação de tornar descrições mais insistentes [3] precisa de precisão: no nosso catálogo, descrever a intenção em uma frase discriminante e testar pedidos próximos ajuda a evitar especialistas concorrendo pelo mesmo trabalho. A preferência local de descrição até 120 caracteres permanece uma convenção editorial, diferente do máximo de 1.024 da especificação.

Checklists, scripts e validações de sequência são úteis em tarefas cuja correção depende deles. A escolha de usá-los deve nascer do problema concreto. Para escrita e criação visual, oferecer critérios e exemplos com espaço para julgamento combina melhor com a experiência aprovada.

A avaliação sugerida pela documentação inclui resultados, tempo e tokens [4]. Usaremos os dados disponíveis no ambiente, declarando ausências. Estatísticas de poucas execuções não demonstram ganho generalizável; uma inspeção proporcional pode bastar para corrigir um problema pequeno.

## Fontes consultadas

1. [Agent Skills — Best practices for skill creators](https://agentskills.io/skill-creation/best-practices): conteúdo útil, escopo, controle proporcional e padrões adaptáveis. Página sem data de publicação explicitada na leitura.
2. [Anthropic — Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): custo de contexto, graus de liberdade, exemplos e referências diretas. Orientações para Claude; aplicação ao Hermes precisa de verificação no destino.
3. [Agent Skills — Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions): intenção, descrições concisas e avaliação de ativação, inclusive pedidos próximos.
4. [Agent Skills — Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills): avaliação de artefatos, comparação de configurações e custo/benefício.
5. [SkillsBench — Introducing SkillsBench](https://www.skillsbench.ai/blogs/introducing-skillsbench): publicação dos autores sobre experimentos de concisão, recursos e efeitos dependentes de domínio; a página distingue o snapshot histórico do registro atual.
6. [SkillJuror — Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/abs/2606.11543): resumo e resultados declarados pelos autores consultados; não reproduzimos os experimentos.

## Estado

Pesquisa incorporada ao desenho da Criadora como orientações de concisão e eficiência. Nenhuma skill foi implementada, nenhum teste de comportamento executado e nenhuma economia de tokens medida nesta etapa.
