# squados-skills — instruções do repositório

Leia este arquivo e `CLAUDE.md` como um par, se o segundo existir. Consulte também
`README.md` e `CONTRIBUTING.md`. Antes de trabalhar em outro repositório, leia o par
de instruções dele; não transfira regras de implementação do Desktop automaticamente.

## Finalidade e limites

Este é o repositório público do catálogo curado de skills do SquadOS Studio e dos
pacotes próprios mantidos pelo SquadOS. Não é o código do aplicativo nem um espelho
de todos os repositórios de skills de terceiros.

- `gallery.json`: índice que o Studio consulta para mostrar a vitrine de agentes no RH.
- `skills/<nome>/`: conteúdo das skills próprias; o pacote pode incluir arquivos de apoio.
- `README.md`: funcionamento, formato, curadoria e exceções de distribuição.
- `CONTRIBUTING.md`: orientação para contribuir com o índice e os pacotes.
- `LICENSE`: licença deste repositório; não substitui as licenças de conteúdo externo.

**Curadoria SquadOS não significa autoria SquadOS.** O contrato atual aceita três
origens: `squados`, `hermes` e `github`. Skills externas permanecem em suas origens;
não devem ser copiadas para cá apenas para compor a vitrine. Informe a origem real,
preserve autoria e licença, e não apresente código de terceiros como próprio.

Em 12/10/2026, o índice contém 14 itens em seis áreas, todos de origem `hermes`.
Referências à Anthropic no README descrevem fontes permitidas e candidatos excluídos;
não representam skills Anthropic publicadas no índice. Confira o JSON antes de
reutilizar essa contagem. Tornar o catálogo exclusivo de skills próprias é uma mudança
de produto e de curadoria; não remova origens ou itens como uma limpeza documental.

## Integração com o Desktop

O consumidor é `../squados-desktop`. O Studio usa o harness Hermes por meio do
contrato `ComputerRuntime`; a interface e os serviços de skills pertencem ao Desktop.
As referências de implementação são:

- `src/shared/skills/gallery.ts`: URL pública, schemas, origens e parsing do índice.
- `src/main/services/skills/gallery-service.ts`: carregamento HTTP, busca e preparação.
- `src/main/services/skills/native-skills-service.ts`: invocação do adaptador Hermes.
- `resources/hermes/skills.py`: busca, download, verificação e proposta para revisão.
- `src/renderer/src/features/skills/GalleryBrowser.tsx`: vitrine, origens e mais resultados.

O Desktop lê `https://raw.githubusercontent.com/squados/squados-skills/main/gallery.json`.
Não usa este checkout local automaticamente. O serviço não mantém cache próprio;
faz a requisição sem credenciais, recusa redirecionamentos, usa timeout de 15 segundos
e rejeita um corpo acima de 1.000.000 bytes. O índice exige `version: 1`. Uma versão
incompatível torna a vitrine indisponível; itens inválidos são descartados individualmente.

O índice lista opções, sem instalar suas skills. Ao contratar, o adaptador resolve a
origem, verifica conteúdo com o guard do Hermes e prepara uma proposta nativa para a
pessoa revisar. A aprovação é uma etapa posterior. Resultados externos da busca são
separados da seleção editorial do JSON: excluir um item do índice não o remove
automaticamente de "Mais resultados".

## Contrato do catálogo

Confirme sempre o schema atual do Desktop antes de editar o índice:

- `id` e `area`: slugs em minúsculas, números e hífen, até 64 caracteres.
- Cada item pertence a uma área declarada; evite áreas vazias e IDs duplicados.
- Título de área até 60 caracteres; título de item até 80; descrição até 300.
- A curadoria exige `pt-BR` e `en`, texto de uma linha e linguagem de trabalho.
  O parser aceita ausência de `pt-BR`, mas isso não atende ao padrão editorial.
- `featured`, quando presente, é booleano e representa escolha editorial.
- `squados`: `{ "type": "squados", "path": "skills/<nome>" }`.
- `hermes`: caminho em `skills/...` ou `optional-skills/...` do acervo empacotado.
- `github`: identificador `<dono>/<repo>/<caminho>` somente de `openai/skills`,
  `anthropics/skills`, `huggingface/skills` ou `NVIDIA/skills`.

A lista de fontes permitidas não garante licença adequada, compatibilidade ou qualidade
de cada pacote. Leia a skill inteira e seus recursos antes de incluí-la. Não altere
`version` sem uma mudança coordenada no consumidor. O parser limita a saída a 50 áreas
e 500 itens; não conte com esse truncamento para organizar o catálogo.

## Pacotes próprios e compatibilidade

Use `skills/<nome>/SKILL.md` com frontmatter que declare `name`, `description` e `license`.
O nome deve coincidir com a pasta. Preserve scripts, referências, templates, assets,
licenças e versões de dependências necessários à execução. Não prometa que copiar
apenas o Markdown instala um pacote que depende de outros arquivos.

Para contratação pela galeria, o adaptador atual aceita até 100 arquivos e 4 MiB de
conteúdo UTF-8, sem binários. Além de `SKILL.md`, os recursos devem estar em
`references/`, `templates/`, `scripts/` ou `assets/`. Arquivos de licença `LICENSE*`,
`LICENCE*`, `NOTICE*` e `COPYING*` na raiz são movidos para `references/` pelo adaptador,
desde que não haja colisão. Outros arquivos soltos ou pastas não aceitas impedem a
preparação. Confira também os limites e validações nativos do Hermes.

O adaptador e seu teste de integração são a referência para essas regras. Não remova
avisos legais para contornar restrições de empacotamento.

Um pacote pode existir neste repositório sem estar apto à galeria. É o caso de
`skills/editar-video`: versão de desenvolvimento 0.1.0, com binários e estrutura própria,
Python 3.11–3.12, Node 22+, FFmpeg e dependências adicionais. Mantenha-o fora do índice
até que sua compatibilidade seja demonstrada. Leia o README e as referências de
instalação do pacote antes de executá-lo. Existência local não significa publicação.

Não assuma que uma dependência mencionada por uma skill está instalada. O Desktop
atual possui bibliotecas Python de documentos instaladas sob demanda; confirme seu
perfil, locks e rotina de preparação antes de dizer que "o Studio já traz" uma biblioteca.

## Validação e entrega

Credenciais de provedores, incluindo OpenRouter, ficam na configuração local do
agente que executa a skill, fora deste repositório. Não coloque chaves em SKILL.md,
scripts, exemplos, projetos gerados, logs ou commits. A skill de vídeo usa o agente
já configurado e não exige uma chave própria de LLM. Arquivos `.env` locais são
ignorados; arquivos `.env.example` públicos só podem conter valores fictícios.
O `.gitignore` não remove segredos já rastreados nem protege contra `git add -f`:
confira o diff antes de cada commit. Se uma chave for publicada, revogue-a e
substitua-a; apagar o arquivo em um novo commit não apaga o histórico.

Este repositório não possui um runner de testes ou CI próprio na raiz. Não invente
comandos `npm test` aqui. Pacotes independentes têm seus próprios checks.

Para o catálogo, valide JSON, campos, traduções, unicidade, referências de área,
caminhos e licenças. Compare com `../squados-desktop/docs/squados-skills/gallery.json`:
o teste `gallery-content.test.ts` lê esse espelho, não este repositório. Se houver uma
mudança no índice, o espelho precisa ser reconciliado na entrega coordenada do Desktop;
um teste verde sobre o espelho antigo não valida o novo índice.

No Desktop, use o script nomeado e um escopo focado:

```powershell
npm test -- src/shared/skills/gallery.test.ts src/shared/skills/gallery-content.test.ts src/main/services/skills/gallery-service.test.ts src/runtime/hermes/skills-gallery.integration.test.ts src/main/ipc/gallery.test.ts src/renderer/src/features/skills/GalleryBrowser.test.tsx
```

Os testes de conteúdo Hermes e integração podem ser pulados quando o source/runtime
preparado não existe. Verifique o resumo e declare skips como pendentes. Não prepare
dependências nem abra a aplicação apenas para validar uma edição documental.

Separe as evidências: contrato válido, pacote verificável, proposta revisável,
aprovação/instalação e execução de um pedido real são etapas diferentes. Não declare
"100% funcional" apenas porque o JSON carrega ou os testes passam.

Trabalhe na branch principal, preserve WIP de outras sessões e faça commits cirúrgicos
dos próprios arquivos após validação. Use PowerShell 7 no Windows. Documentação e
comentários em PT-BR; identificadores novos em inglês. Não acrescente infraestrutura
ou copie dependências sem uma necessidade concreta. Push e publicação dependem de
pedido explícito; registre como estado quando ainda não ocorreram.
