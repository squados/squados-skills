# Tipos e preservação

Use ao importar dados, editar um modelo existente ou reestruturar abas.

Inventarie recursos relevantes antes de salvar por outra ferramenta: fórmulas, nomes, tabelas, filtros, validações, proteção, links, gráficos, pivots, macros e conexões. O risco depende do recurso e da operação. Inserir linhas não garante atualização de todas as dependências; uma biblioteca pode preservar certos objetos e perder outros. Não prometa round-trip universal nem afirme que qualquer gráfico ou macro sempre desaparece. Prefira alteração estreita e compare o que foi afetado.

Leia fórmulas e resultados em vistas separadas quando necessário. Uma carga que retorna valores armazenados pode ocultar fórmulas; salvar esse objeto pode substituí-las por valores. Preserve o original até conferir a entrega. Em `.xlsm`, suporte a VBA e preservação dos objetos precisam ser avaliados concretamente; `.xlsx` não é recipiente equivalente.

Para CSV, confira delimitador, encoding, separador decimal e contrato do receptor. `00123` é um identificador, não a quantidade 123. `03/04/2026` pode ser ambíguo sem contexto. Aspas no CSV não garantem o tipo que o Excel escolherá por duplo clique. CSV representa uma tabela e não preserva abas, estilos ou recursos de workbook.

Limpeza precisa reconciliar linhas, entidades e totais. Dois registros iguais podem ser eventos legítimos; “manter o último” exige campo de ordenação e desempate. Quando possível, preserve origem ou registre transformações importantes. Não crie abas extras se uma nota suficiente resolve rastreabilidade.

Validações de entrada ajudam preenchimento, mas não verificam automaticamente valores existentes. Confira intervalos aplicados e comportamento no aplicativo. Proteção de folha evita edição acidental; não substitui criptografia ou controle de acesso. Se o formato solicitado não puder ser preservado, explique a limitação e escolha com a pessoa uma alternativa utilizável.
