##Sua função bubble_sort recebeu uma lista de números chamada a_list como parâmetro:
def bubble_sort(a_list):
    ##Dentro da função, você está obtendo o tamanho da lista, diminuindo 1 e salvando o resultado em list_lenght para controlar o número de iterações que seu algoritmo executará:
    list_length = len(a_list) - 1
    ##A função tem dois loops aninhados para você percorrer a lista e fazer comparação
    for i in range(list_length):
        for j in range(list_length):
            ##Dentro do loop "for" interno, você usou uma instrução if para comparar o número atual com número que vem depois dele, adicionando 1 ao índice do número atual.
            ##a_list[j] é o número atual
            ##a_list[j + 1] é o número seguinte da lista:
            if a_list[j] > a_list[j + 1]:
                ##Se o número atual for maior do que o número seguinte, você os trocará de posição.
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

##Todas as comparações do algoritmo ocorrem dentro do loop interno. O loop externo só existe para manter o algoritmo sendo executado por quantas trocas forem necessárias...
##para colocar a lista em ordem. Veja por exemplo, a lista do começo da seção:

##[32, 1, 9, 6]

##Após uma única iteração do loop interno, a lista ficou assim:

##[1, 9, 6, 32]

##Entretanto essa listão não está em ordem. Se você só tivesse o loop interno, o algoritmo terminaria prematuramente e a lista não ficaria em ordem.
##Por isso, você precisa do loop externo: para executar o loop interno do algoritmo desde início e repeti-lo até a lista estar em ordem.