# Verificação integrada do catálogo de trabalho

Início em 12/10/2026; conclusão das conferências em 13/10/2026. Autorização contínua do usuário para criar todos os especialistas e depois testar/melhorar. As 33 sínteses e 99 dossiês precedem a autoria; esta etapa reutilizou decisões por componente, com desenhos registrados por frente. Nenhum pacote externo foi incorporado: instruções originais MIT, sem scripts, instrumentos ou assets copiados.

## Pacotes e preparação nativa

34 pacotes: 33 especialistas aprovados mais skill-manager. São 111 arquivos Markdown e 263.246 bytes no snapshot conferido. As 32 novas skills têm núcleos de aproximadamente 350–435 palavras; detalhes pertinentes ficam em referências diretas. Não há scripts, dependências próprias ou modos que a pessoa precise memorizar.

O gate nativo inicialmente recusou recruitment: o limite de descrição de criação do Hermes preparado é 60, menor que o teto editorial 120 e o quick_validate. Diagnóstico em preview_payload identificou a causa; descrições dos 34 pacotes foram ajustadas sem alterar o Desktop. A referência de qualidade da manager ensina conferir o menor limite vigente. Falha e correção estão no [registro da coordenação](2026-10-12-work-skills-coordination-implementation.md).

[Evidência nativa por pacote](2026-10-12-work-skills-native-validation.json): UTF-8 estrito, nome/pasta, licença, descrição, estrutura, links, limites e _validate_frontmatter(new_skill=True) conferidos. Guard skills-guard-v10: 34 safe/allowed; a manager tem um achado low agent_config_ref por citar instruções do repositório, aceito pela política nativa, sem ocorrência bloqueante. Hashes dos arquivos de guard/adaptador consultados estão no JSON; isso não certifica versões futuras.

gallery_stage e pending reais prepararam 34 propostas com origem studio-gallery, source preservado e conteúdo de todas as referências igual ao disco. Perfil isolado em .scratch/work-skills-contract/home; provedor de download substituído por arquivos locais do repo. Nenhuma rede autenticada, aprovação ou instalação no perfil da pessoa. Esse ensaio demonstra preparação/preview no snapshot local; não demonstra download da main pública nem integração de interface/instalação em produção.

## Pedidos de trabalho

[Inputs](2026-10-12-work-skills-evaluation-inputs.md) e respostas integrais: [Marketing/RH](2026-10-12-work-skills-marketing-evaluation.md), [Comercial/finanças](2026-10-12-work-skills-commercial-evaluation.md), [Operações/pessoas](2026-10-12-work-skills-operations-evaluation.md).

Os 32 novos pacotes receberam um pedido sintético cada em três agentes que não participaram da autoria, com leitura explícita do núcleo e referências pertinentes. Há duas variações adicionais, porque os casos originais de recruitment e training-specialist coincidiram com exemplos das referências. As variações mudam domínio/números e continuam no mesmo contexto; não são ensaios virgens. Copywriter mantém sua [avaliação anterior](2026-10-12-copywriter-validation.md), sete pedidos e dois controles, com limites registrados; a alteração atual foi na descrição.

A coordenação leu as entregas e conferiu adequação e contas: pedidos com receita incompleta separados; competência/caixa e risco no caminho; parcelas, GRR/NRR sem novos clientes; NPS/deduplicação; compra mínima/prazo; disponível/posição/ponto de reposição; atraso de pedidos em trânsito; decisões e compromissos condicionais; população de treinamento e capacidade. O coach entregou abertura e aguardou, conforme pedido; não houve treino completo de pessoa. Especificação de planilha foi o formato pedido, sem XLSX ou recálculo alegado.

Contextos agrupados, seleção explícita e uma execução por pacote limitam esta evidência. Nenhum ganho causal, estabilidade estatística, economia medida de tokens, eficácia comercial ou ativação implícita foi demonstrado. Dados, pessoas e empresas são fictícios; não ocorreram contatos, pagamentos, compras ou alterações em sistemas reais. Autoavaliação dos executores não substitui revisão da coordenação e o revisor final independente.

## Apresentação HTML

[Amostra real de quatro telas](evaluation-artifacts/2026-10-12-presentation-sample.html), com conteúdo, CSS e JavaScript locais. O executor declarou corretamente que seu DOM simulado não verificava renderização. A coordenação complementou com Chromium real headless já disponível no repo vizinho, sem instalação, servidor ou janela visível.

[Prova de navegador](2026-10-12-work-skills-presentation-render-validation.json): quatro telas em 1440×1000 e 390×844, botões/setas/Home/End, extremos desabilitados, uma tela ativa, ausência de overflow horizontal, erros de console e requisições remotas. Screenshots desktop das telas 1/4 e mobile4 inspecionadas: conteúdo legível, hierarquia e condições preservados; no celular há rolagem vertical normal. Impressão/PPTX/leitor de tela e outros conteúdos/marcas não foram testados. Prints temporários ficaram fora dos pacotes/commits.

## Galeria

[Prova do parser atual](2026-10-12-work-skills-gallery-validation.json): gallery.ts real do Desktop compilado com esbuild existente, sem modificar consumidor. Índice local version1, 48 itens/15 áreas/25.225 bytes; todos passaram no schema real, unicidade, traduções, caminhos e referências de áreas. Preservados integralmente os 14 itens e seis áreas anteriores; 34 novas fontes squados. Destaques existentes preservados.

O espelho docs/squados-skills/gallery.json do Desktop ainda tem14 itens e não foi alterado. Portanto teste de conteúdo sobre esse espelho não valida o índice novo. A preparação usa o parser real sobre este JSON; entrega coordenada do espelho e gates nomeados do Desktop são etapas posteriores. Nenhuma biblioteca do Desktop foi instalada, nenhuma aplicação foi iniciada.

## Pesquisa complementar e limites

Conferidos [OPM — entrevistas estruturadas](https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/structured-interviews/), [CDC — padrões de treinamento](https://www.cdc.gov/training-development/php/qts/index.html) e [Agent Skills — especificação](https://agentskills.io/specification). A rota CDC inicial retornou erro, resolvido com a rota correta; não fingir leitura onde houve erro. Fontes/regulação/plataformas mutáveis devem ser pesquisadas quando o pedido real depender delas.

Não houve novas transcrições pagas, auditoria jurídica exaustiva de similaridade autoral nem leitura de todos os vídeos identificados na pesquisa. Bases e direitos externos continuam com seus limites nos dossiês. A síntese original não redistribui seus arquivos.

## Estado de entrega e revisão

Autoria e verificações locais integradas à main. [Revisão final independente](2026-10-12-work-skills-final-review.md): APPROVE, zero Critical/Important/Minor após leitura integral dos 34 pacotes; nenhuma correção necessária. A coordenação aceitou o parecer no escopo local, preservando os limites acima. Nenhum push, publicação, aprovação/instalação no perfil real ou pedido real no Studio. A próxima prova solicitada pelo usuário é testar os pacotes no seu fluxo e então aprimorar.
