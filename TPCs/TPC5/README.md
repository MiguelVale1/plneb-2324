# TPC5

Neste tpc foi pedido que terminássemos a estruturaçao dos títulos que aparecem se passarmos por cima de uma palavra presente no dicionário utilizado, apresentando a definição da palavra e a sua tradução em inglês.

## Programa

O programa em si, abre o ficheiro json dos conceitos (definições e traduções), juntamente com o ficheiro do ivro que se quer alterar. Foi criada uma lista de palavras a ignorar por causa da sua alta frequência.

Todos os conceitos foram transformados em minúsculas. Os termos \n e \f foram substituídos pelas suas versões em html e quealquer outra palavra passará pela função (etiquetador) de adição da sua definição e tradução.

A função etiquetador assume a palavra em questão, se a palavra não existe no dicionário de conceitos, este será retornado, senão, se esta estiver incluída no dicionário e não estiver no conjunto de palavras ignoradas, serão atribuídas as variáveis de definição e tradução ao seu valor incluído no ficheiro de conceitos dessa palavra. A etiqueta terá então a definição e a tradução, como title da palavra em si, em html e a palavra será retornada. 