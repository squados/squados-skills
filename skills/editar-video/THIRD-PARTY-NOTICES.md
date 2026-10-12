# Dependências e assets

Código autoral deste pacote: MIT. Isso não altera a licença das dependências.

- HyperFrames 0.8.147: Apache-2.0, https://github.com/heygen-com/hyperframes .
- GSAP 3.15.0: licença própria Standard No Charge, https://gsap.com/community/standard-license/ .
  Não rotular como MIT. Sua licença permite código gerado por IA; termos próprios continuam válidos.
- faster-whisper 1.2.1: MIT, https://github.com/SYSTRAN/faster-whisper .
- Whisper/modelos derivados: verificar notices da distribuição exata antes do release.
- Silero VAD incluído por faster-whisper: MIT, https://github.com/snakers4/silero-vad .
- MediaPipe 0.10.21 e modelos incluídos no wheel: Apache-2.0,
  https://github.com/google-ai-edge/mediapipe/blob/v0.10.21/LICENSE .
  SHA256 do modelo runtime conferido contra assets/manifest.json. OpenCV contrib 4.11.0.86:
  licença Apache-2.0 e notices do wheel, https://github.com/opencv/opencv/blob/4.11.0/LICENSE .
- NumPy/PyYAML/CTranslate2/AV e demais dependências: versões travadas em uv.lock;
  a auditoria transitiva e notices completos constam do gate de pacote, não presumir MIT uniforme.
- FFmpeg é instalado pelo aluno/agente, não redistribuído neste ZIP. Licença depende do build:
  https://ffmpeg.org/legal.html .
- Seis famílias Google Fonts: OFL-1.1; OFL.txt junto a cada fonte e paths/SHA256/source/commit
  em assets/manifest.json. Não substituir os avisos pelas condições do código.

Nenhum meme, stock, música de terceiro, fonte sem licença ou asset interno incluído.
Publicação exige auditoria transitiva e de modelos concluída no relatório de release.


Inventários: assets/licenses/python-dependencies.json (46 distribuições) e
assets/licenses/npm-dependencies.json (77 entradas instaladas nesta plataforma).
Notices dos wheels e dos fontes exatos preservados. Brotli/dfa/fontkit declaram MIT,
mas não têm texto de licença independente no snapshot exato: README e metadata
foram preservados; confirmação desse detalhe permanece gate de release.
ASR base é baixado no primeiro uso; pesos não são redistribuídos neste ZIP.
