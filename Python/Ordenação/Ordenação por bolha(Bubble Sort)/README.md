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

Como você pode ver, 32 flutuou para o fim da lista. No entanto, sua lista ainda não está em ordem porque 9 e 6 não estão nos locais corretos. Logo, o algoritmo começa do início novamente e compara 1 e 9.

[*1*, *9*, 6, 32]

Nada acontece porque 1 não é maior do que 9. Em seguida, ele compara 9 e 6:

[1, *9*, *6*, 32]

9 é maior do que 6, portanto você faz troca e a lista agora está em ordem:

[1, 6, 9, 32]

Em uma ordenação por bolha, o número maior passa para o fim da lista no final da primeira iteração do algoritmo, mas se o número menor estiver no fim, serão necessárias várias iterações para o algoritmo, mas se o número menor estiver no fim, serão necessáras variás iterações para o algoritmo movê-lo para o começo da lista. Nesse exemplo, 32 entrou no fim da lista após uma única iteração. Contudo, suponhamos que a lista começasse assim:

[32, 6, 9, 1]

Nesse caso, serão necessárias quatro iterações para mover 1 do final para ínicio da lista.

Pode ser útil você usar um visualizador de ordenação por bolha para entender melhor como esse algoritmo funciona.