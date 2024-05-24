##Você começou definindo uma função insertion_sort que recebe uma lista de números como entrada:
def insertion_sort(a_list):
    ##A função usa um loop "for" para percorrer cada item da lista. Em seguida, usa um loop "while" para as comparações que o algoritmo faz quando da inclusão de um novo número...
    ##no lado esquerdo classificado da lista:
    ##A função "for" começa com o segundo item da lista (índice 1). Dentro do loop, você está registrando o número atual na variável value:
    for i in range (1, len(a_list)):
        value = a_list[i]
        ##O loop "while" move os itens da metade direita não ordenada da lista para metade esquerda ordenada.
        ##Continuará fazendo isso enquanto duas condições forem verdadeiras: i deve ser maior do que 0 e o item anterior deve ser maior do que o item que vem depois dele.
        ##A variável i deve ser maior do que 0 porque o loop "while" compara dois números. Se i for 0, isso significará que o algoritmo está no primeiro item da lista e não haverá um número anterior com o qual comparar:
        ##Seu loop "while" só será executada se o número de "value" for menor do que o item anterior da lista. Dentro do loop "while", você está movendo o valor maior para a direita na lista.
        ##Em seguida, o algoritmo tenta descobrir onde deve colocar o valor menor na metade esquerda ordenada. Você decrementou i para que o loop possa fazer outra comparação e ver se o número menor precisa ser deslocado ainda mais para esquerda
        while i > 0 and a_list[i - 1] > value:
            ##Quando o loop "while" terminar, você inserirá o número atual do value na posição correta da metade esquerda ordenada na lista
            a_list[i] = a_list[i - 1]
            i = i - 1
            a_list[i] = value
        return a_list
    
    ##Examinaremos como seu algoritmo de ordenação por inserção funciona com a lista a seguir:

    ##[6, 5, 8, 2]

    ##Na primeira iteração do loop "for", i é 1 e value é 5
    ##for i in range(1, len(a_list)):
    ## value = a_list[i]

    ##O codigo destacado a seguir é Ture porque i > 0 e 6 > 5, logo o loop "while" será executado:
    ##WHILE I > 0 AND A_LIST[I - 1] > VALUE:
    ## a_list[i] = a_list[i - 1]
    ##  i = i - 1
    ##  a_list[i] = value