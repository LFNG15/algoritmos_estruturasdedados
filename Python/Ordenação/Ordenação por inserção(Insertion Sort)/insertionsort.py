def ordenacao_por_insercao(lista):
    for i in range(1, len(lista)):
        value = lista[i]
        while i > 0 and lista[i - 1] > value:
            lista[i] = lista[i - 1]
            i = i - 1
            lista[i] = value
        return lista
    
lista = input("Insira os números separados por espaços: ").split()
lista = [int(num) for num in lista if num.isdigit()]
lista_ordenada = ordenacao_por_insercao(lista)
print("Lista ordenada:", lista_ordenada)