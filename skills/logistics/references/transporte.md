# Transporte e capacidade

Use para comparar cotação, planejar carga, rota ou capacidade operacional.

Primeiro confira quais alternativas atendem origem/destino, serviço, corte, prazo e restrições da carga. Um preço de coleta após o corte não é equivalente ao que atende o pedido. Verifique peso, volume, dimensões, empilhamento e compatibilidade quando afetarem a opção. Capacidade em kg não demonstra capacidade em m³ ou encaixe físico.

Peso tarifável depende da regra da cotação: modal, região, divisor, arredondamento e mínimos. Não transfira o divisor de um serviço para todos os demais. Distinga peso físico e base de cobrança. Compare frete, adicionais, impostos pertinentes, embalagem, espera, coleta, retorno e transição na mesma unidade. Custos comuns não devem ser duplicados ao comparar alternativas; preço anunciado não é gasto confirmado.

Para rota, use endereços e matriz de tempos/distâncias com origem conhecida. Distância geométrica em coordenadas não é distância viária nem trânsito atual. Inclua janela, duração de serviço, capacidade, depósitos, retorno e jornada relevantes. Se os dados não permitirem uma rota operacional, entregue sequência candidata e lacunas explícitas.

Uma carga individual maior que a capacidade pede outra opção ou divisão permitida; não deve deixar o algoritmo tentando indefinidamente. Alterações de rota exigem checar capacidade e janelas novamente. Registre pedidos não atendidos e razão. Um solver pode provar ótimo apenas para seu modelo e condição de busca, sem validar endereço, tarifa ou tráfego reais.

Em filas e capacidade, encontre o gargalo pertinente: separação pode suportar o volume enquanto embalagem não. Use ritmo, disponibilidade, espera e variabilidade conhecidos. Não prometa ganho obtido apenas por comparar cenários; indique condição e evidência necessária para implementá-los.
