# Identidade, atributos e variantes

Mantenha relação entre família, produto, variante e oferta. SKU identifica no escopo da operação; GTIN identifica artigo comercial; código do fabricante tem contexto próprio. Formato ou checksum válido não prova atribuição ao item. Deduplicar por título ou exigir unicidade global sem escopo pode apagar ofertas válidas.

Registre fonte e abrangência de cada atributo material. Aço 304 confirmado em garrafa azul de 500 mL não autoriza herdar esse grau para preta de 750 mL. Um pai com descrição genérica precisa evidência de universalidade antes de distribuir o fato. Conflitos devem ficar visíveis, sem escolher silenciosamente o valor mais conveniente.

Use tipo pertinente: seleção com vocabulário, número/unidade, booleano ou texto. Não converta ausência em false/zero. Estoque zero confirmado informa indisponibilidade; estoque desconhecido não. Preserve IDs e overrides. Uma matriz de duas cores por três tamanhos pode ter apenas quatro combinações ofertadas; não publique as duas restantes por preenchimento automático.

Converta unidades rastreavelmente quando fizer sentido. Duas peças de 0,35 L são duas de 350 mL, não um item de 700 mL. Peso bruto de 0,84 kg corresponde a 840 g bruto, sem virar líquido. Altura 12 sem unidade fica pendente. Números com vírgula/ponto exigem locale e campo antes de transformação.

Separe taxonomia interna, categoria oficial de destino, tags e coleção. “Presentes” pode ser agrupamento comercial, sem equivaler a código de canal. Mapeamento incerto é proposta com motivo; consulte o vocabulário atual do destino quando necessário.

Para arquivo final, confirme colunas, tipos e preservação de códigos ao reabrir. Uma exportação que transforma GTIN em número científico falha mesmo que as descrições estejam boas.
