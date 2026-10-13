---
name: spreadsheet-specialist
description: Cria e edita planilhas com cálculos conferíveis.
license: MIT
---

# Especialista em Planilhas

Produza ou altere o arquivo de planilha quando ele for o objeto do pedido. Aproveite template, regras e contexto existentes. Escolha a estrutura mais simples que permita preencher, consultar e atualizar os cálculos; um controle pequeno não precisa de capa ou dashboard. Diferencie entradas, cálculos e saídas de forma legível, respeitando convenções úteis já adotadas.

Antes de editar, inspecione abas, fórmulas, tabelas, nomes, validações e recursos que possam ser afetados. Faça alterações localizadas e preserve o restante. Para importação e workbooks existentes, leia [Tipos e preservação](references/preservacao.md). Arquivos com macros, conexões ou objetos avançados exigem uma ferramenta compatível e conferência dos recursos presentes; trocar a extensão não realiza conversão segura.

Defina tipos por significado da coluna. Identificadores e zeros à esquerda permanecem texto; moeda, percentuais e quantidades calculáveis ficam numéricos. Distinga branco, zero e desconhecido. Confirme separadores e datas ambíguas quando mudarem o resultado. Duplicatas requerem chave de negócio e regra de conservação, sem remoção automática por aparência.

Use fórmulas quando a pessoa precisa alterar entradas e atualizar resultados. Deixe taxas e premissas de negócio identificadas. Não esconda referências quebradas com zero nem invente regra de comissão, saldo ou elegibilidade. Use [Fórmulas e conferência](references/calculos.md) para compatibilidade, recálculo e testes pertinentes. Respeite a plataforma de destino; uma função disponível no Excel atual pode faltar no motor disponível.

Confira dados e totais antes/depois; teste casos de borda da regra e uma alteração de entrada quando pertinente. Fórmula gravada, cache lido e cálculo realizado são evidências diferentes. Bibliotecas que escrevem fórmulas podem não avaliá-las. Se faltar motor de cálculo, declare o recálculo pendente, sem fabricar cache para simular verificação.

Ajuste cabeçalhos, formatos, filtros, largura e impressão ao uso. Cor ajuda, mas não deve carregar sozinha uma condição. Reabra o arquivo final e confira alterações e preservação relevante. Entregue link para o arquivo, orientação breve sobre onde preencher e limites reais da validação.

Se uma ferramenta necessária faltar, explique o benefício e ofereça instalá-la e continuar, respeitando autorização já dada. Uma alternativa deve preservar a entrega necessária ou explicitar sua diferença. Se padrão recorrente de colunas ou preenchimento justificar, proponha adaptar a versão usada pela pessoa; aplique com aceitação, mantendo regras particulares fora do pacote público.
