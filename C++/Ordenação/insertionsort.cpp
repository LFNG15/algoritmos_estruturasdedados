#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

std::vector<int> ordenacao_por_insercao(std::vector<int> lista) {
    for (int i = 1; i < lista.size(); i++) {
        int value = lista[i];
        while (i > 0 && lista[i - 1] > value) {
            lista[i] = lista[i - 1];
            i--;
            lista[i] = value;
        }
    }
    return lista;
}

int main() {
    std::string input;
    std::cout << "Insira os números separados por espaços: ";
    std::getline(std::cin, input);

    std::vector<int> lista;
    std::stringstream ss(input);
    std::string num;
    while (std::getline(ss, num, ' ')) {
        if (std::all_of(num.begin(), num.end(), ::isdigit)) {
            lista.push_back(std::stoi(num));
        }
    }

    std::vector<int> lista_ordenada = ordenacao_por_insercao(lista);

    std::cout << "Lista ordenada: ";
    for (int num : lista_ordenada) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

