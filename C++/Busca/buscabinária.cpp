#include <iostream>
#include <vector>

int busca_binaria(std::vector<int> lista, int alvo) {
    int primeiro = 0;
    int último = lista.size() - 1;
    while (primeiro <= último) {
        int meio = (primeiro + último) / 2;
        if (lista[meio] == alvo) {
            return meio;
        } else if (alvo < lista[meio]) {
            último = meio - 1;
        } else {
            primeiro = meio + 1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> lista = {1, 3, 5, 7, 9, 11};
    int alvo = 5;
    std::cout << busca_binaria(lista, alvo) << std::endl; 
    alvo = 4;
    std::cout << busca_binaria(lista, alvo) << std::endl;
    alvo = 9;
    std::cout << busca_binaria(lista, alvo) << std::endl;
    return 0;
}
