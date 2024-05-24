#Função
##Sua função binary_search recebeu 2 argumentos a_list e n (o número alvo):
def binary_search(a_list, n):
    ##Variaveis "first" e " last" para registrar o começo e o fim da lista que está pesquisando. Inicialmente, atribuiu o valor 0 à variável "first".
    ##Em seguida, atribuiu o tamanho da lista menos 1 à variável "last". Você alterará o valor dessas variáveis ao dividir "a_list" em segmentos que diminuirão cada vez mais:
    first = 0
    last = len(a_list) - 1
    ##O loop do seu algoritmo continuará sendo executado enquanto existerem itens na lista:
    while last >= first:
        ##Dentro do loop, você localizou o ponto intermediário de "a_list" somando "first" e "last" e dividindo por 2:
        mid = (first + last) // 2
        ##Em seguida, você usou uma instrução condicional para verificar se o elemento do ponto intermediário da lista é procurado.
        ##Se for, você retornará True porque encontrou o número que está procurando:
        if a_list[mid] == n:
            return True
        else:
            ##Se o item do ponto intermediário de sua lista não for o item-alvo, você verificará se o item-alvo é maior ou menor do que o valor do ponto intermediário.
            ##Se o item-alvo for menor do que o valor do ponto intermediário, você atribuirá à variável "last" o valor do ponto intermediário menos 1, descartando a metade superior
            ##...da lista de processamento posterior
            if n < a_list[mid]:
                last = mid - 1
            ##Se o item-alvo for maior do que o valor do ponto intermediário, você configurará o valor do "first" com o ponto intermediário mais um, descartando a metade inferior...
            ##da lista do processamento posterior:
            else:
                first = mid + 1
            ##Posteriormente seu loop será, então, repetido em um segmento menor da lista que você criou usando as variáveis "first" e "last"
            ## mid = (first + last) // 2
    ##Quando o loop terminar, a função retornará "False" porque se você for até o fim da função, o número não faz parte do argumento iterável a_list
    return False