#include <iostream>
#include <vector>
#include <string>
#include <sstream>

std::vector<int> bubble_sort(std::vector<int> list) {
    int list_length = list.size();
    for (int i = 0; i < list_length; i++) {
        for (int j = 0; j < list_length - i - 1; j++) {
            if (list[j] > list[j + 1]) {
                std::swap(list[j], list[j + 1]);
            }
        }
    }
    return list;
}

int main() {
    std::string input;
    std::cout << "Enter numbers separated by spaces: ";
    std::getline(std::cin, input);

    std::vector<int> list;
    std::stringstream ss(input);
    std::string num;
    while (std::getline(ss, num, ' ')) {
        list.push_back(std::stoi(num));
    }

    std::vector<int> sorted_list = bubble_sort(list);

    std::cout << "Sorted list: ";
    for (int num : sorted_list) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

