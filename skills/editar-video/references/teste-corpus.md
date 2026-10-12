# Corpus anotado

Ferramenta para validar a distribuição, executada pelo agente/editor da skill.
`PYTHON scripts/check.py --suite all --e2e CORPUS` lê CORPUS/manifest.json.
Cada caso exige name e input relativo à pasta do manifesto. Pode incluir language,
model (base congelado ou diretório local), decisions (JSON anotado), storyboard (JSON
anotado) e expected_text (strings cuja presença é obrigatória na transcrição entregue).
transcript opcional injeta fixture conhecido; esse caso não valida ASR.
expected_error exige falha em prepare e substring do diagnóstico — útil para arquivos
sem áudio, silenciosos ou danificados. Não contar falha inesperada como sucesso.

O runner faz prepare/apply/compose/preview/final/qa/export pelo mesmo run.py da skill,
em pastas novas, e preserva logs/report.json. Sem storyboard anotado usa o starter;
esse caso testa motor e relógio, não a qualidade da direção criativa do agente.
Report editorial_approval=false permanece assim mesmo quando todas as métricas passam.
O corpus real de 12 casos, a escuta, os 30 minutos e o beta continuam gates separados.
