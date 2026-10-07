# Como contribuir

Há dois tipos de pull request.

## 1. Acrescentar um item ao índice

Edite `gallery.json` e acrescente um item (formato no [README](README.md)) apontando para:

- uma skill deste repositório (`"type": "squados"`);
- uma skill de `openai/skills`, `anthropics/skills`, `huggingface/skills` ou `NVIDIA/skills` (`"type": "github"`). Outro repositório não entra: o Studio descarta o item;
- uma skill do acervo do Hermes que o Studio já empacota (`"type": "hermes"`).

Antes de abrir o pull request:

- `title` e `description` em `pt-BR` e `en`, uma linha cada, na palavra que a pessoa usa no trabalho;
- abra a skill e confirme que ela não pede conta, chave nem instalação extra;
- confirme que todo arquivo além de `SKILL.md` está em `references/`, `templates/`, `scripts/` ou `assets/`, sem binário. Skill com `LICENSE.txt` na raiz, por exemplo, não é aceita na contratação.

## 2. Acrescentar uma skill nossa

Crie `skills/<nome>/SKILL.md`:

- `name` igual ao nome da pasta (minúsculas, números e hífen);
- `description` de uma linha;
- `license` no frontmatter;
- somente texto, sem conta nem chave; arquivos de apoio só em `references/`, `templates/`, `scripts/` ou `assets/`.

Depois acrescente o item correspondente em `gallery.json`, com `"source": { "type": "squados", "path": "skills/<nome>" }`.

## O que o Studio faz com o seu pull request

O Studio nunca instala uma skill direto: toda skill passa pelo verificador do Hermes
(`tools/skills_guard.py`) antes de chegar à pessoa, e a pessoa revisa o que será contratado.
Uma skill barrada pelo verificador não é contratada e a pessoa vê o motivo.
