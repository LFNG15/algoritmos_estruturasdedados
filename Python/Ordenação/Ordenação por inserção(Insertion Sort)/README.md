Uma ordenação por inserção é um algoritmo de ordenação no qual ordenamos os dados como ordenaríamos as cartas de um baralho. Primeiro, dividimos uma lista de números em duas metades: uma metade esquerda ordenada e uma metade direita não ordenada. Em seguida, classificamos a metade esquerda da mesma forma que ordenaríamos uma repleta de cartas. Por exemplo, quando ordenamos
uma mão com cinco cartas na ordem crescente, percorremos as cartas uma a uma, inserindo cada carta à direita das cartas menores que ela.

Veja como um algoritmo de ordenação por inserção funciona em uma lista com quatro elementos: 6, 5, 8 e 2. O algoritmo começa com o segundo item da lista, que é 5:

[6, 5, 8, 2]

Em seguida, você compara o item atual com o anterior da lista. Seia é maior do que 5, logo você os trocas de lugar:

[5, 6, 8, 2]

Agora, a metade esquerda da lista é ordenada, mas a metada direita não:

[5, 6, 8, 2]

Você passa, então, para o terceiro item da lista. Seis não é maior do que 8, portanto você não troca 8 e 6:

[5, 6, 8, 2]

Já que a metade esquerda da lista está ordenada, você não precisa comparar 8 e 5:

[5, 6, 8, 2]

Em seguida, você compara 8 e 2:

[5, 6, 8, 2]

Já que 8 é maior do que 2, você percorre cada item da metade esquerda ordenada da lista, comparando 2 com cada número até este chegar à posição inicial e a lista inteira estar ordenada:

[2, 5, 6, 8]