# Copywriter — evidências de avaliação local

Data: 12/10/2026. Execução nativa aprovada pelo usuário com “ok”. [Desenho](../superpowers/specs/2026-10-12-copywriter-design.md) e [plano com entradas A–F](../superpowers/plans/2026-10-12-copywriter.md) definem o pacote e os critérios. Todos os dados e destinos dos casos são fictícios.

## Método e limites

Avaliação no harness Codex desta sessão, com subagentes de contexto novo, modelo herdado e instruções gerais do ambiente. Não é execução no Hermes/Studio. Controle recebe apenas os pedidos A/D, sem leitura de pacote, desenho ou pesquisa; tratamento terá acesso explícito ao SKILL e às referências escolhidas. Isso observa encaminhamento após carregamento, sem demonstrar descoberta implícita.

Respostas são julgadas por fatos, condições, voz, utilidade e proporcionalidade, sem nota de conversão. Não há cegamento, aleatorização, amostra estatística, medição de tokens ou dados comerciais reais. Outras orientações gerais do ambiente podem influenciar o controle; ele não representa um modelo sem instruções.

## Tarefa 1 — controle observado antes da autoria

Agente `copywriter_control`, sem herança de conversa, recebeu os dois pedidos exatos. Foi orientado a não consultar arquivos/skills nem usar ferramentas; declarou uso exclusivo do texto fornecido. Nenhuma pergunta feita. O pacote ainda não existia.

### Resposta A

> Olá, Joana.
>
> Passando aqui para te lembrar que as inscrições para a nossa oficina de planilhas estão abertas até 20/10.
>
> O valor é R$ 490, e a turma começa em 27/10. Serão quatro encontros ao vivo para praticar fórmulas e organizar relatórios.
>
> Se quiser participar, você pode se inscrever em https://example.com/oficina.
>
> Um abraço, Equipe Farol.

**Conferência:** preservou preço, datas, quatro encontros, conteúdo, destino e tom. A edição foi localizada, sem perguntas ou novo escopo. Resultado satisfatório no critério do caso; nenhuma falha fabricada para justificar a skill.

### Resposta D

| Slide | Texto observado |
|---|---|
| 1 | Está no estoque. Mas está disponível? Antes de prometer uma entrega, confira os dois saldos. |
| 2 | Saldo físico. É a quantidade de produtos que está fisicamente no estoque. |
| 3 | Saldo disponível. Considera as unidades reservadas e outras restrições que possam impedir a venda. Um produto reservado pode continuar no estoque físico. |
| 4 | Na prática: 100 unidades físicas − 20 unidades reservadas = 80 unidades disponíveis. Isso se não houver outras restrições. |
| 5 | Reserva não significa saída física. Antes de prometer a entrega ao cliente, confira quanto está disponível. |

Legenda observada: “Ter 100 unidades no estoque físico não significa ter 100 unidades disponíveis para vender. Se 20 estiverem reservadas, a disponibilidade será de 80 unidades, desde que não haja outras restrições. As unidades reservadas podem continuar fisicamente no estoque. Antes de prometer uma entrega, confira o saldo disponível.”

**Conferência:** cálculo, unidades, condição e reserva/saída preservados. Texto por slide e legenda utilizáveis, sem número imposto pelo pedido. Resultado satisfatório. O controle já resolve esses dois pedidos; a avaliação posterior pode mostrar manutenção de qualidade, sem alegar melhoria causal.

## Estado desta unidade

Controle A/D registrado antes da escrita. Autoria, avaliações com pacote, revisão independente e checks estruturais ainda não ocorreram neste marco. Instalação, guard/proposta Hermes, uso real e publicação permanecem posteriores.
