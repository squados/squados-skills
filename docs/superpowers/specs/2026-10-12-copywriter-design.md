# Copywriter — proposta de desenho

Data: 12/10/2026. Estado: desenho aprovado pelo usuário com “sim”, implementado e verificado localmente. O catálogo e o padrão de autoria estão aprovados; este documento concretiza o primeiro pacote da próxima etapa. As 33 pesquisas do catálogo estão consolidadas; Copywriter foi implementado e avaliado localmente; criação dos outros pacotes e publicação permanecem posteriores.

## Resultado pretendido

Uma especialista de redação de marketing, em PT-BR, para colaboradores e equipes: emails, páginas de vendas, anúncios, peças estáticas, carrosséis e outros textos relacionados. A pessoa descreve o trabalho; a skill reconhece criação, revisão ou adaptação e o formato pertinente. Não precisa escolher modos ou conhecer frameworks.

A especialista entrega texto utilizável, adequado ao público, oferta, canal e voz. Pergunta quando uma informação ausente muda a entrega; aproveita conversa, briefing e materiais existentes. Uma revisão restrita preserva condições e trechos aprovados. A falta de uma prova não autoriza inventar resultado, testemunho, garantia, escassez ou prazo.

## Referências e escolhas

Base: [síntese de Copywriter](../../research/2026-10-12-copywriter.md), com treze SKILL principais e três dossiês de origem. Autoria seguirá a [skill-manager](../../../skills/skill-manager/SKILL.md) e o [padrão aprovado](../../skills-de-trabalho-status.md).

| Referência comparada | Contribuição adotada | Corte ou adaptação |
|---|---|---|
| Corey Haines: copywriting/copy-editing/emails | Contexto, ação, oferta e prova; campos úteis para escrita de emails | Estruturas como opções; sem sete passagens, painel de personas ou benchmarks obrigatórios |
| Forjd: better-writing | Revisão proporcional e preservação de fatos e voz | Sem transportar limiares e regras de pontuação em inglês |
| Swan/Tanyo: email-sequence | Função de cada contato, relacionamento e gatilho conhecido | Pedido de texto não exige desenhar automação; sem cadência universal |
| ECC e Tribe AI: voz | Amostras sustentam atributos; tom acompanha contexto | Sem estilo pessoal do mantenedor, bans universais ou guia formal obrigatório |
| Sanket Dongre: direct-response-copy | Coerência entre promessa, prova e oferta | Sem exigir mecanismo proprietário ou oito partes em qualquer peça |
| Sergey Bulaev: carrosséis | Texto da arte, ordem de leitura e legenda separados | Quantidade pela substância; sem claims de algoritmo e publicação acoplada |

As revisões, links de arquivos, autoria e licenças estão nos dossiês. O pacote será autoral; a consulta não implica copiar recursos nem incluir fontes externas no índice.

## Alternativas consideradas

| Caminho | Vantagem | Custo ou limitação |
|---|---|---|
| **Núcleo curto com referências por formato — recomendado** | Encaminhamento natural e detalhes úteis só quando necessários; permite atender o escopo escolhido | Exige indicação clara de quando consultar cada referência e evitar repetição |
| Apenas um SKILL.md curto | Menos arquivos e leitura simples | Ou perde distinções importantes entre formatos, ou carrega tudo em cada pedido |
| Especialistas e scripts separados para cada formato | Mais isolamento para fluxos complexos recorrentes | Fragmenta um trabalho já escolhido como uma skill e cria coordenação sem necessidade demonstrada |

## Pacote proposto

```text
skills/copywriter/
  SKILL.md
  references/
    pages-and-offers.md
    emails.md
    ads-and-social.md
```

Frontmatter: `name: copywriter`, `license: MIT`; descrição PT-BR de uma frase até 120 caracteres. Exemplo de descrição: “Escreve e revisa textos de marketing com voz, argumentos e ofertas coerentes com o público.”

O núcleo orienta contexto, escolha de abordagem, voz, fatos, revisão e entrega. As três referências ajudam, respectivamente, em páginas e argumentos de oferta; emails e sequências; anúncios, estáticos, carrosséis e roteiros. Voz e revisão comuns ficam no núcleo; detalhes exclusivos de um formato ficam na referência. A quantidade de arquivos só aumenta se surgir conteúdo útil que não caiba nessa organização.

Bibliografia extensa, comparação, histórico e avaliações ficam em `docs/`, fora do pacote executável. Não criar scripts, dependências, menus, modelos fixos de briefing ou integração de campanha nesta unidade. Texto não exige instalação. Caso um pedido posterior precise de outra ferramenta, explicar benefício, conferir disponibilidade e aproveitar autorização existente.

## Comportamento e entrega

1. Identificar o trabalho, a ação desejada e o material disponível. O formato solicitado prevalece; não criar campanha inteira a partir de uma revisão de linha.
2. Extrair público, oferta, condições, provas, objeções e voz pertinentes ao pedido. Se faltar algo decisivo, perguntar de forma breve. Uma lacuna menor pode permanecer como pressuposto explícito no rascunho.
3. Escolher argumento, sequência e tom pelo contexto. Frameworks são recursos, sem obrigação de nomeá-los ou encaixar toda entrega na mesma estrutura.
4. Escrever o texto. Separar elementos necessários à produção: texto na arte e legenda; assunto, preview, corpo e destino; seções de página, quando pertinentes.
5. Conferir fatos, condições, coerência da promessa, voz, leitura e próximo passo. Preservar trechos aprovados e manter alterações dentro do pedido.
6. Entregar o artefato primeiro; explicar mudanças ou lacunas relevantes de forma concisa. Variações surgem quando pedidas ou quando ajudam uma decisão concreta, com diferença reconhecível entre elas.

Provas ilustrativas de terceiros não viram resultados do cliente. Uma hipótese de teste editorial não é performance medida. Se a peça exigir informação atual, a pesquisa precisa de fontes; não pesquisar por rotina a cada edição simples. Análise de campanhas pertence à especialista de Marketing e Tráfego; produção de imagens pertence ao trabalho visual pertinente.

Quando uma preferência recorrente ajudar o fluxo, oferecer ajustar a versão utilizada da skill. Aplicar com aceitação ou pedido direto, preservando o restante. A voz de uma empresa não vira padrão público para todas.

## Avaliação proposta

Usar exemplos fictícios identificados. Observar entregas e decisões, sem exigir títulos ou frases literais do pacote. Um conjunto inicial pequeno cobre os principais riscos; incluir um caso novo depois de qualquer correção substancial.

| Pedido | Entrada fictícia | Evidência esperada |
|---|---|---|
| Revisão limitada | Email aprovado: oferta R$ 490, inscrições até 20/10, turma em 27/10; pedido apenas de clareza | Condições e promessa preservadas; edição proporcional, sem redesenhar oferta |
| Página com prova incompleta | Curso de planilhas, quatro encontros, sem depoimentos ou resultado de renda; público administrativo | Argumento coerente com o conteúdo; lacunas visíveis, sem testemunhos, renda ou garantia inventados |
| Anúncios distintos | Serviço de gestão de estoque; provas apenas de funções de produto; pedido de três ângulos | Ângulos reconhecíveis, claims sustentados e ligação com ação/página, sem notas fingindo conversão |
| Carrossel a partir de material | Nota fornecida distingue estoque físico de disponível e traz exemplo de 100 unidades, vinte reservadas | Preserva distinção e exemplo; texto por slide e legenda utilizáveis, sem quantidade artificial de slides |
| Sequência e voz | Dois emails para participantes de evento fictício; amostras de voz diretas, sem gírias; destino já informado | Função por contato, assunto/preview/corpo/CTA; sem inventar eventos, automação instalada ou voz caricata |
| Pedido vizinho | “Essas campanhas perderam dinheiro? Aqui estão os custos.” | Reconhece análise financeira/de tráfego, sem substituir evidência por julgamento de copy |

Comparar um pedido de revisão e um multiformato com execução de controle, quando isso ajudar a identificar contribuição do pacote. Referências carregadas e perguntas feitas podem ser observadas; economia de tokens só pode ser declarada se medida. Avaliação editorial não demonstra ganho comercial.

## Critérios de aceitação e limites

- Pacote autoral com metadados válidos, descrição no limite, links locais resolvidos e arquivos UTF-8 nas pastas aceitas.
- Intenção e formato reconhecidos pelo pedido, sem apresentação obrigatória de modos ou briefing repetido.
- Texto com fatos e condições preservados, argumentos sustentados e voz adequada; produção não precisa reconstruir os campos essenciais.
- Conteúdo detalhado encaminhado por necessidade; núcleo sem bibliografia extensa, repetição ou dependência desnecessária.
- Casos observados e revisão independente registrados com falhas e limitações; correções conferidas em caso novo quando pertinente.

Validador e avaliações locais não provam ativação implícita, guard/proposta Hermes, instalação, execução no Studio ou conversão comercial. Esses estados precisam de evidência própria. Galeria, espelho do Desktop e publicação permanecem na etapa final do catálogo.

## Footprint e estimativa da próxima unidade

Criação posterior: `skills/copywriter/**`, documento de evidência em `docs/research/`, estado canônico e ledger. Não alterar catálogo ou consumidor nessa unidade.

Estimativa de agente: **20–40 minutos** para autoria, avaliação local, correções, verificação e commit; acesso a ferramentas ou falhas podem ampliar a faixa. Não inclui execução autenticada no Studio ou publicação. A implementação é sequencial; **▶ avaliações independentes** de casos disjuntos podem ocorrer em paralelo depois que o pacote estiver escrito, sem edição concorrente do núcleo.

O [pacote Copywriter](../../../skills/copywriter/SKILL.md) foi escrito e verificado localmente conforme o [plano de execução](../plans/2026-10-12-copywriter.md). A [avaliação](../../research/2026-10-12-copywriter-validation.md) registra respostas, correção, revisão e limites. Instalação, uso no Studio e publicação permanecem posteriores.
