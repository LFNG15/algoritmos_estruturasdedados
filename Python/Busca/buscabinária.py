def busca_binaria(lista, alvo):
    primeiro = 0
    último = len(lista) - 1
    while primeiro <= último:
        meio = (primeiro + último) // 2
        if lista[meio] == alvo:
            return meio
        else: 
            if alvo < lista[meio]:
                último = meio - 1
            else: 
                primeiro = meio + 1
    return False

lista = [1, 3, 5, 7, 9, 11]
alvo = 5
print(busca_binaria(lista, alvo)) 
alvo = 4
print(busca_binaria(lista, alvo)) 
alvo = 9
print(busca_binaria(lista, alvo))