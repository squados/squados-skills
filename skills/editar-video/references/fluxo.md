# Fluxo e contratos

prepare copia o bruto, mede mídia, cria PCM, transcreve em CPU e produz analysis.json.
Um arquivo sem fala/áudio recebe diagnóstico específico. O agente lê words/candidates e decide.
decisions.json: `removals` com candidate_id/start_us/end_us/reason/evidence;
retake com fala exige replacement_word_ids e semantic_preserved=true, conferidos contra áudio.
caption_corrections mapeia id de palavra para texto corrigido, sem mudar tempo.

apply valida decisões, monta A-roll CFR, remapeia palavras e normaliza áudio em duas passadas.
edit.json é a autoridade de tempo: segmentos mantidos com origem/saída e words remapeadas.
Não estimar tempos pelo texto nem usar relógio independente em motion.
storyboard.json rascunho precisa ser refinado pelo agente antes de compose.

compose compila assets locais, fontes e HTML determinístico; render produz preview/master.
qa decodifica inteiro, mede duração/LUFS/picos e produz pacote de frames/clips.
export só aceita fingerprint atual e QA técnico aprovado; separa revisão audiovisual pendente.
O aluno não edita JSON e não precisa aprovar essas etapas.

No screencast use --kind screencast. Em formato vertical, enquadramento contain preserva
informação por padrão; corte para preencher só quando área relevante puder ser preservada.
Sem fonte/asset essencial, corrigir antes do render. Sem máscara válida, embedded informa
fallback para foreground. Não apresentar fallback como segmentação feita.
