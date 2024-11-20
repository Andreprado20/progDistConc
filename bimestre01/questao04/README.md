Questão 04
Um problema simples que pode ser resolvido com threads é o cálculo da soma de um vetor grande de
números inteiros.
Suponha que temos um vetor de 1 milhão de números inteiros e queremos calcular a soma de todos eles.
Podemos resolver esse problema de forma sequencial, percorrendo o vetor e somando cada número, mas
isso pode ser muito lento. Uma abordagem mais eficiente é dividir o vetor em várias partes e calcular a soma
de cada parte em uma thread separada, para aproveitar o poder de processamento de máquinas com vários
núcleos.
Para isso, podemos criar uma classe SomaThread que implementa a interface Runnable e recebe como
parâmetros o vetor de números inteiros, o índice do início e do fim da parte do vetor que será somada, e um
objeto AtomicInteger para armazenar o resultado parcial da soma.