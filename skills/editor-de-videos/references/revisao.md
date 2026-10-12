# Revisão e QA

Leia qa.json e review/packet.json, frames por beat e clips de cada emenda.
Confirme texto/números/negações, fonte, legibilidade em celular, posição, gráfico, cor,
ritmo, sincronia labial e voz sem fonema comido. Assista/escute preview completo se o host permite.
Métrica de duração e ASR não provam sincronia de cada palavra ou fidelidade semântica.

review.json: fingerprint e master_sha256 atuais (qa.json), visual/audio='passed' somente após revisão real,
evidence com paths/timestamps/ferramenta e notes. Sem ferramenta de escuta, audio='pending'.
Reexecute qa depois de registrar. technical_passed pode ser verdadeiro com review_pending;
o resumo deve explicitar essa diferença. Não inventar aprovação.

Até duas rodadas de reparo; falha grave técnica bloqueia export. Remova efeito quebrado
com motivo registrado quando fallback conserva conteúdo. Não ocultar ausência de modelo/máscara.

Revisão do aluno: patch.json permite caption_text {word_id:text}, removals (lista final),
style (fonts/accent/background), beats (lista final), transitions (lista final), music
(path local no projeto ou null para remover) e sfx (lista final; [] para remover).
Também aceita aspect, face_zoom, color e denoise; esses campos refazem o A-roll e
o plano de imagem sem retranscrever. Use face_zoom=1 para retirar zoom de rosto.
Uma correção textual redefine o motion da ideia afetada para texto fiel; reconstrua
contador/gráfico com os dados corrigidos antes de compor, se necessário.
CLI revise cria nova pasta sem master stale; depois compose/render/qa/export.
Restaurar pausa usa lista removals sem aquela retirada. Mudança de corte refaz storyboard
e A-roll; corrigir fonte não retranscreve. FCPXML experimental exporta somente montagem.
