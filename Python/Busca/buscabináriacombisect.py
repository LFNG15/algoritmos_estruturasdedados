from bisect import bisect_left

def busca_binaria(iteracao, alvo):
    indice = bisect_left(iteracao, alvo)
    if indice < len(iteracao) and iteracao[indice] == alvo:
        return True
    return False

iteracao = [1, 2, 3, 4]
alvo = 5
print(busca_binaria(iteracao, alvo))
iteracao = [1, 2, 3, 4]
alvo = 2
print(busca_binaria(iteracao, alvo))