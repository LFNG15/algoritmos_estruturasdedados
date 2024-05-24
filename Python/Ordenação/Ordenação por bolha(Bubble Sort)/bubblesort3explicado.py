##Você também pode tornar uma ordenação por bolha mais eficiente do que o 2, adicionando uma variável que registre se seu algoritmo fez alguma troca no loop interno.
##Se você percorrer um loop interno sem trocas, sua lista estará ordenada e será possível sair do loop e retornar a lista sem nenhum processamento adicional.

def bubble_sort(a_list):
    list_length = len(a_list) - 1
    for i in range (list_length):
        no_swaps = True
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
            if no_swaps:
                return a_list
            return a_list
        
##Nesse caso, você adicionou uma variável chamada no_swaps que começa como True no inicio do loop interno.
##Se você trocar dois números de lugar dentro do loop interno, ela terá o valor False.
##Se percorrer o loop interno e no_swaps continuar sendo Ture, a lista estará ordenada e você poderá encerrar seu algoritmo.