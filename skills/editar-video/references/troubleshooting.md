# Problemas comuns

1. Skill apareceu mas script não existe: reinstalar pasta/ZIP completo; não só SKILL.md.
2. Hermes usa outro backend: copiar pacote e vídeo para o filesystem do terminal autorizado.
3. Python incompatível: usar 3.11–3.12 e uv.lock; não misturar venv de outro projeto.
4. Node antigo: preparar Node 22+; executar setup novamente.
5. FFmpeg/ffprobe ausente: agente instala pelo gerenciador do host e confere PATH.
6. Sem fala: inspecionar áudio/channel_scores; arquivo mudo precisa de áudio fornecido.
7. Nome/preço errado: confrontar áudio, retranscrever trecho via modelo local melhor disponível
   ou corrigir caption_text por id com evidência; nunca inferir preço pelo contexto.
8. Render falhou: ler primeira causa em render-*.log; captura experimental desativada por padrão.
9. QA stale: revisão mudou assets/configuração; compose/render/qa antes de export.
10. Máscara rejeitada: foreground mantém legenda, resumo informa fallback; não fingir embedded.
11. Fonte ausente: copiar fonte/licença para o projeto e configurar style.custom_fonts.
12. Sem playback: revisão de áudio pendente e retakes de fala conservados.
