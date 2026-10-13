# Copywriter — plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (execução nativa recomendada) or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Criar o pacote autoral Copywriter para escrever e revisar textos de marketing em PT-BR com fatos, oferta e voz preservados.

**Architecture:** Um núcleo curto e três referências por formato. O pedido determina abordagem, contexto necessário e material consultado; a pessoa não escolhe modos. A avaliação observa entregas reais do agente em exemplos fictícios, com comparação inicial e revisão independente.

**Tech Stack:** Markdown UTF-8 e frontmatter YAML; validador existente. Sem scripts ou dependências novos no pacote.

**Spec:** [Desenho de Copywriter](../specs/2026-10-12-copywriter-design.md), aprovado pelo usuário com “sim” em 12/10/2026. Consultar [pesquisa consolidada](../../research/2026-10-12-copywriter.md), [skill-manager](../../../skills/skill-manager/SKILL.md), suas referências de pesquisa/qualidade, AGENTS.md, README.md e CONTRIBUTING.md. O padrão local prevalece sobre padrões de autoria externos.

**FOOTPRINT:** criar os quatro arquivos em `skills/copywriter/` listados abaixo e `docs/research/2026-10-12-copywriter-validation.md`; atualizar este plano, o estado do desenho, `docs/skills-de-trabalho-status.md` e o ledger local `.claude/plans/2026-10-12-skills-de-trabalho.md`. Trabalhar na main e preservar WIP. Índice, Desktop, instalação e publicação ficam na etapa final acordada.

**ESTIMATIVA TOTAL:** 20–40 minutos de agente, incluindo escrita, avaliações, revisão, ajustes e commit. Tarefa 1: 4–7 min; tarefa 2: 6–12 min; tarefa 3: 10–21 min. Esperas de ferramentas ou correções substanciais podem ampliar a faixa. Não inclui execução autenticada no Studio ou publicação.

## Restrições globais

- `name: copywriter`, igual à pasta; `license: MIT`; descrição PT-BR de uma frase até 120 caracteres.
- Recursos UTF-8 nas pastas aceitas; até 100 arquivos/4 MiB, sem binários. O pacote proposto possui quatro Markdown.
- Contexto existente antes de perguntas; intenção e formato reconhecidos automaticamente; método adaptável, sem quotas ou menus.
- Preservar fatos, condições, voz e texto aprovado; não fabricar provas, testemunhos, renda, prazo, escassez ou garantia.
- Bibliografia extensa, pesquisa e evidências de desenvolvimento ficam em `docs/`; referências do pacote contêm síntese aplicável ao trabalho.
- Dependência necessária ausente recebe explicação simples e oferta de instalação, aproveitando autorização existente. Não presumir bibliotecas disponíveis.
- Oferecer melhoria concreta da versão utilizada diante de preferência recorrente; editar com aceitação/pedido direto, sem converter preferência da empresa em padrão público.
- Avaliação editorial não demonstra conversão, eficácia comercial, economia de tokens ou execução no Studio.
- Não copiar pacotes/recursos de terceiros. A pesquisa informa síntese original; inclusão material exigiria licença e avisos compatíveis.

## Foco da revisão

1. Revisão de uma frase com dados suficientes: editar apenas o necessário, sem questionário ou campanha nova — caso A.
2. Pressão para tornar oferta atraente sem provas: escrever argumento sustentado, sem inventar resultados — caso B.
3. Conteúdo quantitativo transformado em carrossel: preservar unidade e significado — caso D.
4. Sequência com voz e destino fornecidos: campos utilizáveis sem inventar gatilhos ou automação instalada — caso E.
5. Pedido de análise de prejuízo: reconhecer trabalho de dados/tráfego e limites da evidência — caso F.

## Tarefa 1 — registrar os casos e observar o controle

**Arquivo:** criar `docs/research/2026-10-12-copywriter-validation.md`.

**Consome:** desenho e pesquisa aprovados. **Produz:** entradas fixas, critérios e respostas de controle, antes da escrita do pacote.

- [x] Registrar os seis casos fictícios abaixo, sem dados reais de clientes, e indicar que a avaliação acontece no harness desta sessão.
- [x] Executar A e D com avaliador independente sem acesso ao pacote futuro ou ao desenho; entregar apenas entrada e pedido. Registrar resposta, perguntas, recursos consultados e limitações do controle. Não alegar ausência de toda orientação se o avaliador tiver outras instruções de escrita disponíveis.
- [x] Identificar falhas e acertos observados. Um controle satisfatório é evidência válida; não fabricar falha nem ampliar regras só para produzir diferença.

| Caso | Entrada e pedido exatos | Verificação do resultado |
|---|---|---|
| A — edição restrita | “Revise apenas a clareza deste email aprovado, sem mudar oferta ou tom: ‘Olá, Joana. Passando aqui para te lembrar que as inscrições para a nossa oficina de planilhas ficam abertas até 20/10. O valor é R$ 490, e a turma começa em 27/10. São quatro encontros ao vivo para praticar fórmulas e organizar relatórios. Se quiser participar, você pode se inscrever em https://example.com/oficina. Um abraço, Equipe Farol.’” | R$ 490, datas, quatro encontros, conteúdo e destino preservados; edição proporcional, sem perguntas dispensáveis |
| B — página sem prova comercial | “Escreva uma página de vendas para a oficina fictícia Farol: quatro encontros ao vivo de duas horas, fórmulas e organização de relatórios; público administrativo iniciante; R$ 490; inscrições até 20/10; início 27/10; inscrição em https://example.com/oficina. Não temos depoimentos, dados de renda ou resultados comerciais medidos. Quero um texto forte, com CTA.” | Público, oferta, argumento e ação coerentes; nenhuma prova, garantia, limite de vagas ou ganho financeiro inventado |
| C — anúncios | “Crie três anúncios estáticos com ângulos diferentes para o software fictício Estoque Claro. Ele mostra saldo físico, reserva e histórico de movimentações; temos apenas evidência dessas funcionalidades. Público: gestores de pequenas lojas. Objetivo: solicitar demonstração em https://example.com/demo. Entregue texto da arte e legenda, com a diferença entre os ângulos.” | Três ângulos reconhecíveis e campos utilizáveis; sem redução percentual, liderança de mercado ou performance medida inventada |
| D — carrossel | “Transforme esta nota em carrossel para gestores de lojas: ‘Saldo físico é o que está no estoque. Disponível considera o que está reservado. Exemplo: há 100 unidades físicas e vinte reservadas; disponibilidade de oitenta se não houver outras restrições. A reserva não significa que o produto já saiu fisicamente. Conferir antes de prometer entrega.’ Entregue texto por slide e legenda, sem número de slides predeterminado.” | Mantém cem/vinte/oitenta, condição de ausência de outras restrições e distinção reserva/saída; sequência legível sem enchimento |
| E — emails e voz | “Escreva dois emails de acompanhamento para quem participou de uma aula fictícia de planilhas, convidando para a oficina Farol: quatro encontros ao vivo de duas horas sobre fórmulas e organização de relatórios; público administrativo iniciante; R$ 490; inscrições até 20/10; início 27/10; sem depoimentos ou resultados comerciais medidos. Destino já definido: https://example.com/oficina. Voz de referência: ‘Vamos direto ao exemplo. Primeiro, confira a origem do dado. Depois, escolha a fórmula. Se algo não fechar, volte ao registro.’ Quero assunto, preview, corpo e CTA em cada email. Não há automação configurada.” | Voz direta sem caricatura; funções distintas por contato; condições preservadas; nenhum envio/gatilho/integração presumido como executado |
| F — pedido vizinho | “Essas campanhas perderam dinheiro? Campanha X custou R$ 1.000 e teve vinte pedidos de R$ 100; Y custou R$ 800 e teve doze pedidos de R$ 100. Não forneci margem, cancelamentos ou atribuição. Diga o que esses dados permitem concluir.” | Pode calcular receita informada/ROAS com limites, mas não lucro; reconhece análise de dados/tráfego, sem avaliar copy inexistente ou exigir transferência impossível |

URLs example.com são destinos fictícios; não navegar, enviar mensagens ou publicar.

## Tarefa 2 — escrever a síntese executável

**Arquivos a criar:**

| Arquivo | Responsabilidade |
|---|---|
| `skills/copywriter/SKILL.md` | Contexto, encaminhamento, argumento/voz/fatos, revisão, entrega e adaptação pelo uso |
| `skills/copywriter/references/pages-and-offers.md` | Ação da página, público, promessa, oferta, objeções, prova e seções adequadas ao pedido |
| `skills/copywriter/references/emails.md` | Relacionamento, função de contato, assunto/preview/corpo/CTA/destino e sequência quando solicitada |
| `skills/copywriter/references/ads-and-social.md` | Ângulo, mensagem, texto da arte/legenda, carrossel/roteiro e hipóteses editoriais de variantes |

**Consome:** pesquisa e observações da tarefa 1. **Produz:** pacote autoral com links diretos de consulta por necessidade.

- [x] Escrever o núcleo com estes metadados:

```yaml
---
name: copywriter
description: Escreve e revisa textos de marketing com voz, argumentos e ofertas coerentes com o público.
license: MIT
---
```

- [x] Orientar identificação do trabalho, uso do contexto, pergunta material, escrita e revisão proporcional; indicar qual referência atende cada formato. Voz deve partir de amostras ou instruções disponíveis, sem guia formal obrigatório.
- [x] Escrever as três referências com decisões e exemplos pequenos que agreguem valor. Estruturas são opções, sem número obrigatório de seções, slides, variantes, palavras ou perguntas. Campos de produção acompanham o pedido.
- [x] Incluir oferta de instalação somente quando uma ferramenta necessária faltar e oferta de adaptação da própria versão diante de preferência recorrente. Não acoplar envio, publicação, geração de imagens ou planejamento completo de campanha à escrita.
- [x] Revisar duplicação: princípios comuns ficam no núcleo; detalhes por formato nas referências; links/bibliografia de pesquisa ficam nos dossiês. Não impor um limite artificial de linhas, mas remover trechos sem contribuição demonstrável.

## Tarefa 3 — avaliar, corrigir e registrar a entrega local

**Arquivos:** pacote da tarefa 2; evidência da tarefa 1; este plano; desenho aprovado; `docs/skills-de-trabalho-status.md`; ledger local.

**Consome:** pacote escrito e entradas fixas. **Produz:** resultados observados, pacote ajustado, checks locais e commit com estado honesto.

- [x] Executar A–F com o pacote disponível e mesmas entradas. **▶ Paralelizável:** avaliadores podem receber grupos disjuntos; cada um tem responsabilidade apenas pelo resultado/evidência, sem editar o pacote. Comparar A/D com o controle de forma descritiva.
- [x] Conferir promessas, condições, voz, campos utilizáveis, perguntas e referências efetivamente consultadas. Registrar resultados e falhas sem nota fictícia de conversão. Em F, receita informada X = R$ 2.000/ROAS 2; Y = R$ 1.200/ROAS 1,5; lucro continua desconhecido.
- [x] Corrigir causas observadas com a menor alteração útil. Havendo correção substancial, executar um caso novo da mesma classe, sem exigir repetir casos já satisfatórios sem razão.
- [x] Obter revisão independente de todos os quatro arquivos contra o desenho, com indicação de achados concretos e limites. O revisor pode somente revisar; o autor aplica correções.
- [x] Executar o validador existente em PowerShell:

```powershell
python -X utf8 C:\Users\renat\.codex\skills\.system\skill-creator\scripts\quick_validate.py "D:\Coding Projects\squados-skills\skills\copywriter"
```

- [x] Conferir quatro arquivos UTF-8, links locais resolvidos, nome/pasta, descrição até 120 caracteres, licença, pastas permitidas, ausência de binários/segredos, contagem até cem e soma até 4 MiB. Não instalar um runner novo para esse check. Não executar testes do Desktop nesta unidade sem alterações nele.
- [x] Registrar checklist de cada critério do desenho com `arquivo:linha`, evidência observada e pendências. Atualizar estado como pacote verificado localmente apenas quando a evidência permitir. Guard Hermes, ativação implícita, instalação, pedido real, performance e publicação continuam estados separados.
- [x] Conferir `git diff --check`, staged diff e paths; fazer commit cirúrgico dos arquivos próprios e comparar cada arquivo commitado via `git show HEAD:<path>` com o worktree. Atualizar ledger ao fechar a unidade. Não incluir `.scratch/` nem tentar a limpeza anteriormente rejeitada.

## Revisão do plano e execução

Cobertura: núcleo e três referências na tarefa 2; seis pedidos e cinco focos de revisão nas tarefas 1/3; adaptação, ferramentas e fronteiras nas tarefas 2/3; contrato, direitos, evidência e entrega na tarefa 3. Sem interfaces de código, instalações ou infraestrutura adicionais.

**Recomendação: execução nativa**, pois há um pacote pequeno com conteúdo interdependente. Avaliações e revisão independentes preservam contraponto sem introduzir coordenação de vários autores. Alternativa: execução por subagentes, com implementador/revisor por tarefa, oferece mais separação, ao custo de contextos e coordenação adicionais.

Estado: plano e execução nativa aprovados com “ok” em 12/10/2026. Três tarefas executadas localmente: controle A/D satisfatório; quatro Markdown escritos; A–F observados, atrito B corrigido e caso novo G satisfatório; revisão independente aprovada e checks estruturais executados. [Evidência e limites](../../research/2026-10-12-copywriter-validation.md). Instalação, uso no Studio e publicação permanecem posteriores.
