É um algoritmo de ordenação recursivo que divide continuamente uma lista pela metade até existir uma ou mais listas contendo um único item e, em seguida, combina-as novamente em ordem correta. Primeiro usamos a recursão para dividir continuamente a lista pela metade até a lista original tonar-se uma ou mais sublistas contendo em único número.

      [6, 3, 9, 2]
    [6, 3] __ [9, 2]
[6] __ [3] __ [9] __ [2]

Listas que contêm um único item são consideradas ordenadas por definição. Quando você tiver listas ordenadas contendo um item cada uma, intercalará duas sublistas de cada vez comparando o primeiro item de cada lista. Intercalar listas significa combiná-las ordenadamente.

Primeiro, você intercalará [6] e [3] e, depois, [9] e [2]. Nesse caso, cada lista contém apenas um número, logo você comparará os dois números e inserirá o menor no começo da nova lista intercalada e o maior no fim. Agora você tem duas listas ordenadas:

[3, 6], [2, 9]
