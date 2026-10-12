# Agente de Propostas Comerciais — síntese da pesquisa

Consulta em 12/10/2026. Escopo aprovado: estruturar propostas com contexto do cliente, escopo, entregáveis e condições de negócio. Esta rodada prepara criação posterior, sem elaborar proposta real, enviar documento ou criar pacote.

## Fontes e alcance

- [Venda e serviços](2026-10-12-commercial-proposals-skills-sales.md): nove SKILL.md distintos lidos, sete principais e dois auxiliares, em sete repositórios; recursos decisivos e licenças.
- [Propostas estruturadas e QA](2026-10-12-commercial-proposals-skills-structured.md): treze SKILL.md completos de cinco origens, dezessete apoios e três fontes primárias de contexto.
- [Métodos profissionais](2026-10-12-commercial-proposals-methods.md): cinco materiais principais, catálogo Shipley 2026 complementar, duas páginas de vídeos 2025–2026 e webinar adicional sem data; três casos fictícios.

Total: **22 SKILL.md distintos de doze repositórios — vinte principais e dois auxiliares**. Não houve sobreposição de arquivos entre as duas frentes. As duas coleções Zubair possuem o mesmo autor; uma cópia RonManatee idêntica foi deduplicada. Quantidade de skills não representa quantidade de provas independentes de eficácia. SHA, autoria, licenças, datas e recursos lidos estão nos dossiês.

Nenhum vídeo foi assistido ou teve transcrição recuperada; páginas, embeds e limites de acesso estão registrados. APMP TV, BoK e alguns slides não ficaram acessíveis integralmente. Não houve créditos, contas, execução de pacotes ou resultado comercial demonstrado.

## Recomendação

Combinar **composição factual e fronteiras de escopo de B2BForce, concisão das propostas leves, rastreabilidade de requisitos das fontes RFP e ligação escopo→entrega→marco→pagamento das fontes SOW**. Profissionais Shipley/APMP ajudam a manter a proposta centrada no comprador e adequada à decisão, sem importar governança de grande licitação para um orçamento pequeno.

A skill identifica criar, revisar, comparar ou completar uma proposta pelo pedido. Aproveita conversa, anexos, template e condições fornecidas; escolhe extensão e formato sem exigir modo, CRM, workspace ou documento intermediário. Se a pessoa pedir rascunho, pode avançar com lacunas identificadas. Dados comerciais ausentes não devem ganhar preço, prazo, desconto ou capacidade inventados.

## Decisões por componente

| Componente | Fontes | Decisão e motivo |
|---|---|---|
| Cliente e decisão | B2BForce, SkillMedev, Shipley | **Aproveitar:** situação concreta e solução pertinente. **Descartar:** estimar dor sem base só para concluir o texto. |
| Clareza da oferta | phuryn value-proposition, consulting-proposal | **Adaptar sob demanda:** cliente, problema, mecanismo, mudança esperada e alternativas quando a oferta precisa ser esclarecida. Não abrir projeto de posicionamento para oferta já definida. |
| Escopo e fronteiras | B2BForce, OneWave, Meaningfy | **Aproveitar:** entregas verificáveis, quantidades/limites, exclusões, dependências e responsabilidades pertinentes. Texto e estimativa precisam vender o mesmo escopo. |
| Condições e números | ncklrs, Alireza deal-desk, orçamento dos métodos | **Adaptar:** unidade, total, recorrência, extras, parcelas e políticas reais. **Descartar:** três tiers, desconto, validade ou cobrança padrão universais. |
| Prova e benefícios | B2BForce, Gener8v, Alireza | **Aproveitar o princípio; corrigir os atalhos:** evidência aplicável à afirmação. Tag, número coincidente ou porte do fornecedor não comprovam capacidade. |
| RFP | Gener8v, Alireza, APMP | **Adaptar:** instruções, requisitos, resposta, fonte e estado. Matriz entra quando ajuda rastreabilidade; proposta espontânea não precisa de pipeline RFP. |
| Aceite e marcos | OneWave, fontes SOW | **Adaptar:** entrega, critério de conferência e pagamento coerentes com o acordo. **Descartar:** aceite por silêncio, SLA ou termos jurídicos genéricos preenchidos por template. |
| Revisão e formato | Peter, B2BForce, fornecedores de propostas | **Aproveitar:** conferir negócio após última edição e documento final legível. **Descartar:** score de vitória, checklist superficial ou comprimento como selo de qualidade. |
| Entrega e submissão | Peter receipt discipline | **Aproveitar conceito:** arquivo preparado, envio e recebimento têm evidências próprias. Recibo/checksum ajudam em submissão formal, sem infraestrutura obrigatória. |

## Achados decisivos

**Validador estrutural não verifica significado.** A coordenação conferiu o [validate-proposal.sh de B2BForce](https://github.com/b2bforce/b2bforce/blob/7682ed90c62190a0f3c09eb135596d08bd6890bc/scripts/validate-proposal.sh). Ele aceita três linhas de tabela e procura números por substring em registros de prova, sem ligar métrica, unidade, cliente ou período. Quote aprovada em um registro não confirma o texto contra o registro correto. Isso é triagem útil, sem prova semântica; não copiar a promessa de garantia.

**Capacidade provável não é capacidade comprovada.** A coordenação leu [requirements-mapper](https://github.com/gener8v/gener8v.claude-skills.rfp-response/blob/93373236bd76ecb223f4509bee6bc610778a6ffe/rfp-toolkit/requirements-mapper/SKILL.md) e [proposal-assembler](https://github.com/gener8v/gener8v.claude-skills.rfp-response/blob/93373236bd76ecb223f4509bee6bc610778a6ffe/rfp-toolkit/proposal-assembler/SKILL.md): o primeiro admite afirmações sem evidência direta; o segundo remove marcadores internos e mantém contagem/resumo para revisão humana. Esse fluxo pode perder a qualificação específica no texto. Preservar condições materiais até serem resolvidas; remover anotação interna não resolve a falta de prova. O drafter Alireza também usa tags/tipo como força da prova sem ler a fonte; resultado lexical é pista, não atendimento.

**Parser não substitui leitura da solicitação.** Cues apenas em inglês, classificação de linha ambígua e data sem hora/fuso podem perder obrigações e prazo real. Fonte, adendo e instruções atuais têm precedência; critérios de edital anterior não são automaticamente os critérios deste. Requisito atendido, parcial, pendente e não atendido precisam de justificativa, não de correspondência de palavras.

**Valor e ROI precisam de base explícita.** Em exemplo ncklrs, US$ 24 mil por trimestre totalizam US$ 96 mil contra US$ 84 mil anuais: adicional de 14,29%, e não 10%. Benefício bruto/preço é diferente de ROI líquido. A conta do exemplo não valida sua projeção. ROI, quando pertinente, usa premissas e horizonte rastreáveis, inclusive possibilidade negativa; não deve ser positivo por construção.

**Precisão não depende de extensão.** Há modelos que exigem páginas, 16 seções, centenas de linhas, três opções ou seis emails. Preservar somente componentes que ajudam a entender a oferta e decidir. Opções reais podem ser comparadas quando o pedido justificar; acompanhamento é uma entrega adicional, sem fabricação de popularidade ou pressão automática.

**Estado documental não determina sozinho efeito jurídico.** A coordenação consultou o [Código Civil brasileiro, art. 427](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm): proposta contratual pode vincular conforme termos e circunstâncias. Não afirmar que o título “proposta” ou ausência de assinatura torna o documento universalmente sem efeito. Aqui a distinção rascunho/enviado/assinado serve à operação; nenhuma cláusula ou proposta concreta recebeu análise jurídica. Preservar termos fornecidos e tratar lacunas de contexto/jurisdição quando uma revisão jurídica for realmente solicitada.

## Casos e avaliação posterior

Os [casos fictícios](2026-10-12-commercial-proposals-methods.md) cobrem negócios distintos; a coordenação conferiu a aritmética com Decimal e soma de parcelas:

| Caso | Gabarito | Falhas críticas |
|---|---|---|
| Treinamento | Duas sessões + preparação = R$ 8.200; 40%/60% = R$ 3.280/R$ 4.920 | Omite preparo, amplia participantes/revisões, promete automação/economia, inventa multa |
| Produtos | 12 kits + 8 cadernos + frete = R$ 3.054,80; parcelas 1.018,27 + 1.018,27 + 1.018,26 | Frete multiplicado, três parcelas arredondadas para cima, desconto ou prazo inventado |
| RFP | Componentes ofertados R$ 30.000; presença local não atendida, acesso condicionado, prazo de relatório pendente | Conformidade integral presumida, fornecedor/parceiro inventado, requisito omitido |

Avaliação prática futura: preço corresponde à unidade/escopo; parcelas fecham; marcos existem; prazo respeita dependências; exclusões não reaparecem como inclusões; prova sustenta a afirmação; formato pedido preserva conteúdo. Uma matriz deve continuar correta após revisão, sem sumário ou páginas estimadas tratados como finais.

Os scripts examinados não foram executados e nenhum desses casos virou proposta real. A revisão deve verificar o resultado utilizável, não apenas frases no SKILL.md ou um status PASS. Alegações de winrate, probabilidade ou conversão dos pacotes não foram calibradas/comprovadas nesta pesquisa.

## Núcleo e referências

Núcleo futuro: aproveitar contexto/modelo, reconhecer intenção, perguntar por lacuna material, redigir oferta proporcional, conferir coerência e números e devolver no formato solicitado. Referências sob demanda: clareza da oferta; serviços/escopo/aceite; orçamento e condições; provas e lacunas; respostas RFP; qualidade documental. Dossiês extensos e bibliografia ficam fora da skill executável.

Scripts só para mecânica com ganho concreto, como tabela volumosa ou conferência repetida. Não impor Bash, CRM, renderer PDF, Pandoc ou pipeline de várias skills para proposta curta. Dependência de exportação ausente: explicar benefício e oferecer preparação simples ou alternativa disponível. Dependências do serviço vendido são diferentes das ferramentas da skill.

Quando preferência recorrente ou atrito justificar, oferecer adaptar a própria versão: terminologia, modelo, tabela ou política fornecida. Aplicar com aceitação/pedido; condições de cliente e promessa comercial não viram regra pública. Uma adaptação pode melhorar redação e revisão sem criar nova governança, modos ou armazenamento.

## Licenças e limites

Várias origens têm MIT lida; ncklrs e Gener8v declararam MIT no README sem aviso completo verificável encontrado. Meaningfy declara Apache no frontmatter, com arquivos legais ainda não auditados. Peter reconhece métodos derivados cuja cadeia deve ser conferida antes de cópia substancial. Materiais Shipley/APMP/Proposify não foram redistribuídos; acesso público não significa licença de templates, formulários ou imagens. Fonte, licença e atribuição permanecem requisitos da reutilização concreta, sem transformar curadoria em autoria SquadOS.

Pesquisa documental registrada, ainda sem pacote, proposta real, instalação, proposta Hermes, contratação, execução no Studio, envio ou publicação. Nenhuma conta, chave ou serviço pago foi usado. Nenhuma mudança de allowlist, índice ou espelho do Desktop ocorreu. Temporários de rodadas anteriores permanecem fora dos commits após rejeição automática de remoção já registrada.
