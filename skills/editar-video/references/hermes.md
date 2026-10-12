# Hermes Agent

Mesmo SKILL.md, Python e Node do Codex/Claude Code; nenhum adaptador de API.
Instale a pasta completa em `$HERMES_HOME/skills/editar-video` (perfil padrão: `~/.hermes/skills`).
Use `skill_view(name="editar-video")` ou `/editar-video` para carregar. A ativação informa
`skill_dir`; caminhos dos scripts usam essa pasta, não o diretório de trabalho do terminal.
`terminal` executa a CLI. `read_file` lê JSON/referências; use os recursos de imagem/áudio
disponíveis para revisão. Não presuma que terminal implica capacidade de ouvir.

Backend local/container/SSH: input, pacote, dependências, modelos e outputs devem existir
no mesmo filesystem do terminal. Path `D:\...` não existe automaticamente em Linux remoto.
Preserve o arquivo e transfira apenas para o backend autorizado pelo aluno quando necessário.
Faça stdout curto em cada etapa, leia logs só na falha e guarde o estado do projeto entre turnos.
Operações demoradas usam recursos de processo/background reais do Hermes e acompanhamento
até conclusão; timeout do chat não significa sucesso do render.

Gateway: anexe paths entregáveis reconhecidos pelo canal; `[[as_document]]` evita compressão
de mídia quando suportado. Canal sem acesso aos arquivos: informe o path no backend e o
meio de download disponível, sem inventar URL pública.

O pacote completo é obrigatório. Não usar instalação remota que copie somente referências
Markdown e omita engine/runtime/lock/fontes. O instalador local incluído copia todos os arquivos
reais e valida antes de concluir. Não ativar inline_shell nem alterar configuração do Hermes.

Referências oficiais verificadas em 2026-10-11:
- https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills/
- https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/

Compatibilidade não equivale a suporte de plataforma validado: consultar relatório de release.
