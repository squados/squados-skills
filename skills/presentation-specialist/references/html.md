# Produção e verificação do HTML

Use ao implementar a apresentação e preparar o pacote de entrega.

Um arquivo HTML autossuficiente costuma ser suficiente para texto, formas, tabelas e gráficos simples. Se houver imagens ou outros recursos separados, entregue a pasta completa com caminhos relativos válidos. Fontes do sistema evitam downloads; recursos remotos devem ser declarados. Dados embutidos com bibliotecas de CDN ainda exigem rede. Alegue offline somente após conferir todos os recursos e o funcionamento sem rede.

Use elementos semânticos, títulos reconhecíveis e controles com nomes acessíveis. Em slides, mantenha apenas a tela atual disponível para interação; elementos de telas ocultas não devem capturar foco. Botões anterior/próximo e indicação de posição ajudam a orientação. Setas, Home e End podem complementar os controles, sem interceptar digitação em campos. Evite prender a pessoa em tela cheia; mantenha saída e retorno previsíveis. Animações devem respeitar redução de movimento e continuar compreensíveis sem efeito.

Confirme primeira e última telas, estado dos controles nos extremos, foco visível, links e recursos. Inspecione telas de conteúdo denso no tamanho de uso; ausência de overflow não demonstra texto legível. Gráficos precisam de rótulos e alternativa textual ou tabela quando os valores importarem. Em telas pequenas, recomposição ou leitura contínua pode ser mais útil que encolher um palco inteiro.

Para impressão, use `@media print` para mostrar todo o conteúdo, remover controles e evitar que altura fixa corte texto. Configure quebras por tela quando apropriado e examine a saída real. Fundos, margens, fontes e quebras variam no navegador; PDF pede verificação própria. HTML, PDF e PPTX têm capacidades diferentes: conversão pode perder navegação ou editabilidade. Entregue instrução curta de abertura e declare dependências e exportações realmente verificadas.
