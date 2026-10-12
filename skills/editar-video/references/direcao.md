# Direção e motion

Quatro direções: criador (alto contraste/pop), editorial (serif/ritmo calmo), tecnologia
(mono/diagramas), aula (clareza/etapas). Até três famílias por vídeo, papéis base/emphasis/contrast.
Todo beat referencia word_ids e anchor_word_id reais, start_us/end_us derivados das palavras,
intent, effect, data, region, caption, font_role e reason. Cobertura exata: cada palavra em um beat.
Cada ideia tem uma decisão; hold é apropriado quando leitura/rosto precisam de espaço.

18 efeitos executáveis e seus dados:
- emphasis: text; counter: value numérico/unit; comparison: before/after.
- checklist, steps, flow, timeline: items.
- chart: values/labels, valores explicitamente presentes na fala/dados fornecidos.
- quote: quote/author; definition: title/text; problem-solution: before/after.
- callout: text; interface: title/items; morph: text.
- concept-map: title/items; media-reveal: src local em assets/title.
- lower-third: name/role; recap: title/items.

Cards podem resumir; captions permanecem fiéis à fala. Não invente métricas, nomes ou afirmações.
Use gesto visual por função: quantidade→counter, contraste→comparison, sequência→steps/flow,
definição→definition, estrutura→concept-map. Varie efeito conforme ideias, sem rotação aleatória.
Reservar zona de caption e não cobrir rosto/slide. Motion não compete com legenda a cada palavra.

Seis transições: cut, dissolve, match-graphic, wipe, slide, zoom-bridge. Declare at_us,
duration_us e handles.before_us/after_us medidos. Sem handles, corte seco informado.
Transições gráficas sobre composição mantêm áudio contínuo; não criam crossfade de tomadas.


## Imagem e enquadramento

request.json aceita color {brightness, contrast, saturation} com ajustes leves delimitados,
e face_zoom entre 1 e 1.08. Faça esses ajustes antes de apply, com motivo visual registrado.
Aspectos 9:16/16:9 usam crop estável quando uma pessoa foi detectada e todos os rostos
amostrados cabem no recorte com margem. Sem essa evidência, usa contain. Screencast mantém
a tela inteira. Não promete tracking contínuo: amostras são obtidas a cada dois segundos;
revise o preview se a pessoa se move rapidamente. HDR usa tonemap para SDR.


request.json também aceita denoise=true quando o áudio possui ruído contínuo confirmado.
O tratamento aplica redução leve (6 dB), EQ, compressão moderada e loudness em duas passadas.
Não tenta reconstruir fala saturada. Cada segmento usa fades de 4 ms nas bordas; a escuta
continua obrigatória para aprovar a emenda. analysis_track/analysis_channel são usados também
no áudio final, para que o canal escolhido na análise seja o canal efetivamente entregue.
