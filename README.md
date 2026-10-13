# squados-skills

Vitrine de agentes prontos do SquadOS Studio: um índice curado (`gallery.json`) de skills
que a pessoa contrata com um clique no RH. O repositório guarda o índice e, quando for o
caso, skills nossas em `skills/<nome>/SKILL.md`. As skills de outros repositórios ficam
onde estão e são baixadas só na hora da contratação.

## Skills próprias de trabalho

Os [33 especialistas por departamento](docs/skills-de-trabalho-pacotes.md) e a
[skill-manager](skills/skill-manager/SKILL.md) estão implementados neste checkout,
com referências sob demanda, instruções em PT-BR e licença MIT. A manager orienta
pesquisa comparativa, criação e melhoria pelo uso. Não há modos para memorizar.

O índice local reúne 48 itens em 15 áreas: preserva os 14 itens Hermes e acrescenta
34 pacotes próprios. Estrutura, guard e preparação de propostas foram conferidos
localmente; instalação e uso real no Studio têm evidências próprias. Consulte o
[estado de entrega](docs/skills-de-trabalho-status.md) para publicação e limites.

## Como o Studio lê

O Studio baixa `gallery.json` da branch `main`, sem cache:

```
https://raw.githubusercontent.com/squados/squados-skills/main/gallery.json
```

O arquivo tem teto de 1 MB e começa com `"version": 1`. Versão diferente de 1 faz a vitrine
aparecer como indisponível. Um item malformado, ou de uma fonte que não é confiável, some
sozinho: os demais continuam na vitrine.

## Formato

```json
{
  "version": 1,
  "areas": [{ "id": "finance", "title": { "pt-BR": "Financeiro", "en": "Finance" } }],
  "items": [
    {
      "id": "three-statement-model",
      "area": "finance",
      "title": { "pt-BR": "...", "en": "..." },
      "description": { "pt-BR": "...", "en": "..." },
      "source": { "type": "hermes", "path": "optional-skills/finance/3-statement-model" }
    }
  ]
}
```

- `id` e `area`: minúsculas, números e hífen. Todo item aponta para uma área declarada em `areas`.
- `title` (até 80 caracteres) e `description` (até 300): em `pt-BR` e `en`, uma linha, na palavra de trabalho, sem jargão.
- `source` tem três formas:
  - `{ "type": "squados", "path": "skills/<nome>" }`: skill deste repositório.
  - `{ "type": "github", "identifier": "<dono>/<repo>/<caminho>" }`: só `openai/skills`, `anthropics/skills`, `huggingface/skills` e `NVIDIA/skills`.
  - `{ "type": "hermes", "path": "skills/..." | "optional-skills/..." }`: acervo do Hermes empacotado no Studio.

## Critério da lista

Pedido comum de escritório, sem conta, sem chave e sem instalação extra. Toda skill passa
pelo verificador do Hermes na contratação, e a encenação só aceita arquivos de apoio nas
pastas `references/`, `templates/`, `scripts/` e `assets/` (um `LICENSE*`, `NOTICE*` ou
`COPYING*` na raiz da pasta vai para `references/`), sem binário, até 100 arquivos e 4 MB. O teste `src/shared/skills/gallery-content.test.ts`, no repositório do Studio, confere
isso para os itens do Hermes.

### Acervo Hermes preservado

| Item | Área | Origem | Por que entrou |
|---|---|---|---|
| `three-statement-model` | Financeiro | Hermes | Resultado, balanço e fluxo de caixa ligados; só planilha |
| `comps-analysis` | Financeiro | Hermes | Valuation por comparáveis; só planilha |
| `excel-author` | Financeiro | Hermes | Convenções de planilha auditável; usa `openpyxl`, cuja disponibilidade precisa ser conferida no ambiente |
| `lbo-model` | Financeiro | Hermes | Compra alavancada com TIR e múltiplo; só planilha |
| `claude-design` | Marketing | Hermes | Páginas e apresentações em HTML, sem ferramenta extra |
| `popular-web-designs` | Marketing | Hermes | 54 estilos de sites conhecidos, todos em `templates/` |
| `sketch` | Marketing | Hermes | Variações rápidas de uma tela em HTML |
| `reddit-reading` | Marketing | Hermes | Leitura anônima, sem conta nem chave (as credenciais são um extra opcional) |
| `competitor-news` | Vendas | Hermes | Resumo de notícias com fontes, usando a pesquisa na web |
| `price-monitor` | Vendas | Hermes | Vigia preços com a pesquisa na web |
| `simple-english` | Pessoas | Hermes | Texto claro e sem ambiguidade; só texto |
| `llm-wiki` | Operações | Hermes | Base de notas em Markdown; a sincronização com Obsidian é um anexo opcional |
| `arxiv` | Pesquisa | Hermes | API aberta, sem chave |
| `rss-feeds` | Pesquisa | Hermes | Feeds abertos, sem chave |

Ressalvas: `three-statement-model`, `comps-analysis`, `lbo-model` e `excel-author` indicam um
passo de recálculo com LibreOffice quando ele estiver instalado; o restante do trabalho usa
só `openpyxl`.

### Fora da lista

| Candidato | Origem | Motivo |
|---|---|---|
| `dcf-model` | Hermes | `requirements.txt` (instalação de pacote) e `TROUBLESHOOTING.md` fora das pastas aceitas |
| `article-illustrator` (`baoyu-article-illustrator`) | Hermes | `PORT_NOTES.md` e `prompts/` fora das pastas aceitas |
| `mono-color` | Hermes | `design-system/` fora das pastas aceitas |
| `flashcards` (`memento-flashcards`) | Hermes | Declara só macOS e Linux, e o Studio roda no Windows |
| `doc-coauthoring` | `anthropics/skills` | Não declara licença e o repositório não tem licença única na raiz; sem base clara para distribuir |
| `email-triage` (`email-inbox-triage`) | Hermes | Só orquestra: manda carregar `himalaya` (CLI a instalar) ou `google-workspace` (conta) para ler a caixa |
| `internal-comms` | `anthropics/skills` | `examples/` fora das pastas aceitas |
| `docx`, `pdf`, `pptx`, `xlsx` | `anthropics/skills` | Source-available, não open source; o Studio já traz as suas versões |
| demais skills de `anthropics/skills` | `anthropics/skills` | Não avaliadas item a item para esta lista; aparecem em "Mais resultados" da busca |
| `grill-me` | Hermes | Entrevista sobre plano de implementação, de `software-development`: desenvolvimento fica fora da curadoria |

Os candidatos reprovados foram trocados por `lbo-model` e `popular-web-designs`, que passam no
teste; `grill-me` saiu sem substituto. `email-triage` saiu sem substituto e, com ele, a área Atendimento (nenhum
outro item do acervo passa nos critérios); ela volta ao índice quando houver um item.

## Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md). Licença: [MIT](LICENSE).

## Skill de edição de vídeo

O pacote [Editor de Vídeos](skills/editor-de-videos/SKILL.md) está em `skills/editor-de-videos/`,
com scripts, referências, templates, fontes, modelos, licenças e locks de dependências.
Copie a pasta inteira; apenas o `SKILL.md` não funciona. Consulte as
[instruções de instalação](skills/editor-de-videos/references/instalacao.md).

Essa skill fica fora de `gallery.json`: exige Python 3.11–3.12, Node 22+, FFmpeg e
instalação de dependências, inclui recursos binários e tem 241 arquivos, cerca de 4,7 MB,
com pastas além das aceitas na contratação do Studio. O pacote é uma versão de
desenvolvimento 0.1.0; a validação estrutural não equivale à aprovação para distribuição
aos alunos.
