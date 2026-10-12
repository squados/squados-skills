# Skill-manager — metodologia de pesquisa comparativa

Atualização de 12/10/2026 solicitada pelo usuário: priorizar as principais skills existentes e consolidar seus melhores componentes em futuras pesquisas. Alteração autorizada diretamente; mantém os padrões já aprovados de flexibilidade e progressive disclosure.

## Lacuna e alteração

A versão anterior de `references/research.md` já orientava ler pacotes similares, recursos, origem e licença. A inspeção do conteúdo mostrou que faltava explicitar a prioridade dessa comparação, a descoberta dos candidatos e a rastreabilidade das decisões por componente. Isso é uma lacuna documental identificada, não um teste comportamental com falha observado em produção.

O núcleo permanece com 38 linhas. Uma linha de encaminhamento agora reconhece pesquisas de especialidades e consolidação de skills. A referência tem 49 linhas e acrescenta descoberta em diretórios/fontes originais, seleção por relevância e diversidade, comparação de componentes, decisões de aproveitamento/adaptação/descarte e consolidação proporcional. Nenhum script, dependência ou comando de modo foi acrescentado.

## Verificação local

- Validador existente: `python -X utf8` com `quick_validate.py` de skill-creator retornou `Skill is valid!`.
- Três Markdown, UTF-8 estrito, sem NUL; links relativos do pacote existentes.
- Descrição de uma frase dentro de 120 caracteres; nome e pasta preservados.
- Arquivos e tamanho dentro dos limites locais de distribuição.
- Diff revisado: alteração restrita ao encaminhamento e à referência de pesquisa; qualidade, instalação e adaptação pelo uso preservadas.

## Aplicação e limites

Um avaliador independente aplicou a referência a um caso sintético de propostas comerciais, limitado aos dados de três candidatas: original MIT sem teste publicado, fork idêntico com mais estrelas e dependências extras, e template sem licença informada/scripts consultados. A resposta distinguiu a linhagem do fork, registrou decisões por componente e tratou licença, leitura parcial e eficácia como limites; não criou ou instalou pacote. Não houve comparação controlada com a versão anterior.

A revisão não encontrou lacuna bloqueante. Duas ambiguidades pequenas foram ajustadas no texto: comparação restrita ao material fornecido permanece preliminar; fontes profissionais adicionais entram quando ajudam a julgar componentes ou resolver lacunas materiais. A conferência após a mudança foi documental/estrutural; o exercício não foi repetido.

A pesquisa de Copywriter usa três frentes autorizadas, duas dedicadas às skills existentes e uma a métodos profissionais/materiais recentes. Os dossiês dessa pesquisa registram as fontes e decisões. Essa aplicação não é um experimento controlado de melhoria do modelo.

A validação acima cobre estrutura e revisão documental. Não demonstra reconhecimento implícito de intenção no Studio, economia de tokens, eficácia dos pacotes pesquisados, contratação, instalação ou execução autenticada. Nenhum push/publicação acompanha esta atualização.
