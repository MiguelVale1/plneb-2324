# TPC2

Neste TPC foi proposta a resolução de uma ficha com problemas de expressões regulares, com a utilização de funções do módulo re, de regex.
##Exercício 1

Para alcançar os objetivos pretendidos em cada exercício for criada em cada uma das alíneas, uma função que implementa funções de regex sobre a procura, manipulação, substituiçao, divisão, etc, de zonas de texto que se pretendem encontrar, esta função tem como parâmetro(s) a frase em questão e no caso de funções de substituição a string que se pretenda substituir. Finalmente esta aplica as alterações pretendidas e retorna os resultados, sendo que, nos casos de procura, apresenta 'True' se a string foi encontrada na frase e None se não foi encontrada.

## 1.1

Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece no início da linha.

Neste exercício foi aplicada a função re.match(), para procurar pela palavra 'hello' no início da frase. Para a expressão regular foi escrito 'hello\b', para ter a certeza que não se incluí possíveis palavras iniciadas por hello.

## 1.2

Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece em qualquer posição da linha.

Neste exercício foi aplicada a função re.search(), para procurar pela palavra 'hello' pela frase toda. Para a expressão regular foi escrito '\bhello\b', para ter a certeza de que a string em questão não seja parte de uma outra diferente.

## 1.3

Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, admitindo que a palavra seja escrita com maiúsculas ou minúsculas.

Neste exercício foi aplicada a função re.findall(), para procurar pela palavra 'hello' pela frase toda e incluí-la numa lista. Para a expressão regular foi escrito '\bhello\b', para ter a certeza de que a string em questão não seja parte de uma outra diferente e como flag usou-se re.I, para na busca se incluir tanto minúsculas como maiúsculas.

Na função é verificado se o tamanho da lista resultante for diferente de 0 retorna esta, senão retorna None.

## 1.4

Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha, substituindo cada uma por "*YEP*".

Neste exercício foi aplicada a função re.sub(), para procurar pela palavra 'hello' pela frase toda e substituí-la por "*YEP*". Para a expressão regular foi escrito '\bhello\b', para ter a certeza de que a string em questão não seja parte de uma outra diferente e como segundo parâmetro incluiu-se a string de substituição "*YEP*".

## 1.5

Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada parte da linha por esse caracter.

Neste exercício foi aplicada a função re.split(), para procurar pela string ',' e devolver uma lista da frase com a string "," como string de separação dos items da lista. Para a expressão regular foi escrito ','.

## 2

Define a função palavra_magica que recebe uma frase e determina se a mesma termina com a expressão "por favor", seguida de um sinal válido de pontuação.

Neste exercício foi aplicada a função re.search(), para procurar pela string 'por favor' pela frase toda. Para a expressão regular foi escrito '\bpor favor[.!?]$', para ter a certeza de que a palavra 'por' não seja o final de outra palavra, também foi usado "[.!?]" para todos os sinais de final de frase e finalmente "$" para ter a certeza de que esta string está no final da frase.

## 3

Define a função narcissismo que calcula quantas vezes a palavra "eu" aparece numa string.

Neste exercício foi aplicada a função re.findall(), para procurar pela string 'eu' pela frase toda e retornar uma lista de todas as instâncias desta string. Para a expressão regular foi escrito '\beu\b', para ter a certeza de que a palavra 'eu' não seja parte de outra que a incluí.

Para saber o número de vezes que a string 'eu' aparece usou-se a função len() para saber quantas vezes a função encontrou a palavra na frase.

## 4

Define a função troca_de_curso que substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.

Neste exercício foi aplicada a função re.sub(), para procurar pela string 'LEI' pela frase toda e substituí-la pela palavra que se queira substituir. Para a expressão regular foi escrito 'LEI'.

## 5

Define a função soma_string que recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e devolve a soma destes números.

Neste exercício foi aplicada a função re.split(), para procurar pela string ',' e devolver uma lista dos números com a string "," como string de separação dos números da lista. Para a expressão regular foi escrito ','.

Para obter o somatório dos números usou-se a função sum() onde se incluíu uma lista de compreensão em que se incluí os valores numéricos dos números que estavam guardados em string.

## 6

Define a função pronomes que encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu", "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas.

Neste exercício foi aplicada a função re.findall(), para procurar pelos pronomes pessoais pela frase toda e incluí-la numa lista. Para a expressão regular foi escrito '\b(eu|tu|eles?|elas?|nós|vós)\b', para ter a certeza de que os pronomes pessoais em questão não sejam parte de uma outra palavra diferente e um grupo em que todas as possibilidades estão descritas com o símbolo ? para a existência ou não do plural de ele ou ela, finalmente como flag usou-se re.I, para na busca se incluir tanto minúsculas como maiúsculas.

## 7

Define a função variavel_valida que recebe uma string e determina se a mesma é um nome válido para uma variável, ou seja, se começa por uma letra e apenas contém letras, números ou underscores.

Neste exercício foi aplicada a função re.match(), para procurar pela palavra da variável, visto que esta é a única palavra existente na string. Para a expressão regular foi escrito '^[a-z]\w*$', o primeiro caracter é uma letra, e os seguintes tanto possam ser letras, como números, como underscores e finalmente ^ e $ para ter a certeza que esta seja a única palavra que exista na string. Como flag foi usado re.I para que as letras possam ser tanto minúsculas como maiúsculas.

## 8

Define a função inteiros que devolve todos os números inteiros presentes numa string. Um número inteiro pode conter um ou mais dígitos e pode ser positivo ou negativo.

Neste exercício foi aplicada a função re.findall(), para procurar por todos os números na string. Para a expressão regular foi escrito '-?\d+[.,]?\d*', para ter a certeza de que a string possa ser tanto positiva como negativa, descrito pela presença ou não do símbolo "-", seguida de um ou mais números, com um ponto ou vírgula para descrever um possível decimal e nesse caso no final mais números. 

Após esta procura, esta é aplicada num ciclo dentro de uma lista de compreensão em que se cada número em formato de string não tiver um símbolo de decimal será transformada num número e este será adicionado a uma lista que será retornada. 

## 9

Define a função underscores que substitui todos os espaços numa string por underscores. Se aparecerem vários espaços seguidos, devem ser substituídos por apenas um underscore.

Neste exercício foi aplicada a função re.sub(), para procurar pela string ' ', pela frase toda e substituí-la por "_". Para a expressão regular foi escrito ' +', para ter a certeza de que a string em questão seja um ou mais espaços.

## 10

Define a função codigos_postais que recebe uma lista de códigos postais válidos e divide-os com base no hífen. A função deve devolver uma lista de pares.

Neste exercício foi aplicada a função re.split(), para procurar pela string '-' e devolver uma lista dos pares de números com a string "-" como string de separação dos items da lista. Para a expressão regular foi escrito '-'.

A função cria uma lista vazia onde serão adicionados os pares de números. Após isto, é criado um ciclo que itera por cada string da lista fornecida e será feito o split desta e adicionada à nova lista, que será retornada.
