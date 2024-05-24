from bisect import bisect_left

sorted_fruits = ['apple', 'banana', 'orange', 'plun']
position = bisect_left(sorted_fruits, 'banana')
print(position)

##Nesse caso, bisect_left retonrou 1 porque 'banana' está no índice 1 em sorted_fruits.

##Se o item que você está procurando não estiver em iterável ordenado, bisect_left retornará onde ele estaria se estivesse presente.

sorted_fruits = ['apple', 'banana', 'orange', 'plun']
position1 = bisect_left(sorted_fruits,'kiwi')
print(position1)

##Como você pode ver, 'kiwi' não está em seu iterável ordenado, mas se estivesse, ocuparia o índice 2.
##Já que bisect_left informa onde um item deveria estar caso não esteja presente para verificar se um item se encontra em um iterável, você precisa ver se o índice existe dentro do iterável
##e se o item do índice retornado por bisect_left é o valor procurado. Veja a seguir no codigo de busca binária com bisect_left