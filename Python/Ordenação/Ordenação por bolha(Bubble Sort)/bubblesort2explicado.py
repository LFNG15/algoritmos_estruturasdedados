##Você pode melhorar a eficiência da ordenação por bolha incluindo - i no segundo loop for. Desta forma, o loop interno não comparará os dois últimos números na primeira passagem
##na segunda passagem, não comparará os três últimos números e assim por diante.

def bubble_sorte(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        ##Adicionando o - i
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

##Você não precisa fazer essas comparações porque os números mais altos flutuam para o fim da lista. No exemplo do começo, você viu que 32 flutuou para o fim da lista.
#Isso significa que o número maior estará no fim da lista após primeira iteração, o segundo número maior estará na penúltima posição após a segunda iteração etc.,
##ou seja, você não precisa comparar os outros números com eles e pode encerrar seu loop mais cedo.
##Por exemplo, examine a lista do começo:

##[32, 1, 9, 6]

##Após iteração completa do loop interno, ela ficará assim:

##[1, 9, 6, 32]

##Após uma iteração, o número maior passou para o fim da lista, logo você não precisa comparar os números com 32, porque sabe que ele é o maior número da lista.

##Na segunda iteração do loop interno, o segundo valor maior passará para sua posição final como penúltimo etc.

##[1, 6, 9, 32]

##Portanto, a cada iteração do loop interno, o loop terminará mais cedo.

