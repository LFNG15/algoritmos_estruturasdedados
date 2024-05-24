A ordenação por bolha é um algoritmo de ordenação no qual percorremos uma lista de números, comparamos cada número com o número seguinte e os trocamos se estiverem fora de ordem.
Os cientistas da computação a chamam de ordenação por bolha porque os números de valores mais alto flutuam para o fim da lista e os números de valores mais baixos passam para o início da lista à medida que o algoritmo avança

Digamos que você tivesse a lista a seguir:
[32, 1, 9, 6]

Primeiro, você compara 32 e 1:
[*32*, *1*, 9, 6]

32 é maior, logo você faz troca:
[1, 32, 9, 6]

Em seguida, você compara 32 e 9:
[1, *32*, *9*, 6]

32 é maior, então você faz troca novamente:
[1, 9, 32, 6]

Para concluir, você compara 32 e 6:
[1, 9, *32*, *6*]

Mais uma vez, você faz troca:
[1, 9, 6, 32]

Como você pode ver, 32 flutuou para o fim da lista. No entanto, sua lista ainda não está em ordem porque 9 e 6 não estão