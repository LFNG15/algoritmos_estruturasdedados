##Esse é algoritmo mais eficiente e ele ordena por completo

def ordenacao_por_bolha(lista):
    lista_length = len(lista)
    for i in range(lista_length):
        for j in range(lista_length - i - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = input("Insira os números separados por espaços: ").split()
lista = [int(num) for num in lista]
lista_ordenada = ordenacao_por_bolha(lista)
print("Lista ordenada:", lista_ordenada)
        