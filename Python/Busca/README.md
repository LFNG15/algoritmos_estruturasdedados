A busca binária é algoritmo mais rápido para a busca de um número em uma lista. No entanto, você não pode usá-la em qualquer conjunto de dados porque ela só funciona quando os dados estão ORDENADOS.

Uma busca binária busca um elemento em uma lista, divindindo-a em metades. Suponhamos que você tivesse a lista de números ordenada (do número mais baixo ao mais alto) como essa aqui:

10/12/13/14/15/18/19

A primeira etapa de uma busca binária é localizar o número do meio. Há sete itens nessa lista, logo o número do meio é 14.

10/12/13/    14    /15/18/19

Já que o 14 não é número procurado, você dá prosseguimentos. A próxima etapa é determinar se o número que você está procurando é maior ou menor do que o número do meio. O número procurado, 19, é maior do que 14, portanto não é necessário pesquisar a metade inferior da lista. Você pode descartá-la. Dessa forma, só sobrou a metade superior com três números para serem pesquisados.

15/18/19

Em seguida você repete o processo localizando o número do meio novamente que agora é 18.

15/  18  /19

Já que 18 não é número procurado, você determina novamente se deve manter a parter inferior ou superior da lista. Como 19 é maior do que 18, você mantém a metade superior e descartar a inferior. Assim deixa sobrando um número, 19, que é você está procurando. Se o número sobrado não fosse 19, você saberia que ele não está na lista.

Em BUSCA LINEAR, teríamos levado 7 etapas para encontrar o número 19. Enquanto em BUSCA BINÁRIA, levamos apenas 3 etapas para encontrar.

Pseudocodigo exemplo:

função busca binária(lista, numero):
primeiro = 0
último = tamanho(lista) - 1
enquanto último >= primeiro:
    meio = (primeiro + último) // 2
    se lista(meio) == numero:
        retorna verdadeiro
    se não:
        se numero < lista(meio):
            último = meio - 1
        se não:
            primeiro = meio + 1
    retorna falso