# Instalação

Copie/descompacte a pasta inteira editar-video no diretório de skills do agente.
Codex: `~/.agents/skills/editar-video`; Claude Code: `~/.claude/skills/editar-video`;
Hermes: `$HERMES_HOME/skills/editar-video` ou `~/.hermes/skills/editar-video`.
`scripts/install.py --host codex|claude|hermes --destination PATH` copia o pacote completo
para o destino informado, sem sobrescrever pasta existente. O agente faz esta operação.

No primeiro uso, rode `python scripts/setup.py` da pasta real da skill.
Precisará de Python 3.11–3.12, Node 22+, FFmpeg com ffprobe e uv.
Se faltarem, o agente usa o gerenciador apropriado do host sob suas permissões;
no Windows, winget; no macOS, Homebrew; Linux, gerenciador da distribuição.
Não execute instaladores remotos não examinados. Se a instalação exigir aprovação real
do host, explique qual ferramenta está faltando e siga o mecanismo de aprovação do host.
Depois `python scripts/setup.py --install` restaura uv.lock e package-lock.json.
Não instalar CUDA. O modelo base roda em CPU INT8. Primeiro download exige internet.

Node encontra dependências na própria skill. A variável opcional EDITAR_VIDEO_NODE_HOME
permite ambiente de desenvolvimento isolado; não é necessária ao aluno.
O modelo padrão usa snapshot congelado; `--model PATH` admite modelo local preexistente.
Use CPU para o caminho padrão; o compositor usa SwiftShader sem GPU física. Opcionalmente,
EDITAR_VIDEO_BROWSER_GPU=1 habilita a aceleração de navegador quando o host a oferece.
“Local” não promete que as chamadas do agente ficam offline.

Distribuição pública ainda depende do relatório de aceite: beta, máquina limpa e plataformas.


Wrappers de cópia: install.ps1 -HostName HOST -Destination PATH no PowerShell;
sh install.sh --host HOST --destination PATH no shell POSIX. O agente executa o wrapper
adequado; ele usa o mesmo scripts/install.py, não outro instalador por plataforma.
Testes de corpus anotado: PYTHON scripts/check.py --suite all --e2e CORPUS, que lê
manifest.json e executa a CLI compartilhada para cada caso. Os resultados não aprovam
revisão editorial automaticamente. Consulte [teste-corpus.md](teste-corpus.md).
