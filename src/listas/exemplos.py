# Elabore um programa que solicite ao usuário cinco números, armazene-os em uma lista e exiba como resultado os dados obtidos.
""" nums = [0, 0, 0, 0, 0]
for i in range(5):
    num = int(input("Digite um número: "))
    nums[i] = num
print(nums) """

# usando método append
""" nums = [] # quantidade de valores indeterminados
for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)
print(nums) """

# Elabore um programa que solicite ao usuário cinco números e exiba duas listas separadas: uma contendo somente números pares e outra contendo somente números ímpares. 
""" pares = []
impares = []
for i in range(5):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Números pares:", pares, "- Números ímpares:", impares) """

# Dada a lista de dados nums = [1, 4, 23, 11, 8], corra a lista usando um objeto range e imprima cada elemento em uma linha.
""" nums = [1, 4, 23, 11, 8]
for i in range(len(nums)):
    print(nums[i]) """

""" # ordenação de números
# Dada a lista de dados nums = [17, 33, 23, 11, 8, 15, 9], ordene-a e mostre o resultado ao usuário.
nums = [17, 33, 23, 11, 8, 15, 9]
aux = 0
for _ in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            aux = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = aux
print(nums)
# É importante observar na linha 03 que, se a variável contadora não for utilizada dentro do bloco de códigos do laço, não será necessário declará-la, fazendo uso do símbolo de underscore (_). """

""" # Matriz [[numeros], [numeros], [numeros]]
# Solicite ao usuário que digite três coordenadas (x, y), armazenando-as em uma matriz bidimensional.

# Começamos criando uma lista vazia chamada coordenadas, que servirá para armazenar as coordenadas fornecidas pelo usuário
coordenadas = []
# Em seguida, entramos em um laço "for" que será executado três vezes (de 0 a 2).
for i in range(3):
    x = int(input("Insira um valor de x: "))
    y = int(input("Insira um valor de y: "))
    # Depois, adicionamos um par de coordenadas, que é uma lista contendo x e y, à lista coordenadas.
    coordenadas.append([x, y])
print(coordenadas) """

# métodos
# nums = [17, 33, 8, 11, 8, 15, 9]
# append() -> Adiciona um elemento ao fim da lista.
""" nums.append(10)
print(nums) """

# extend() -> Adiciona todos os elementos de uma lista em outra.
""" num2 = [3, 7]
nums.extend(num2)
print(nums) """
#insert() -> Insere um elemento em determinado índice da lista. (elemento 0 na posição 2)
""" nums.insert(2, 0)
print(nums) """
# remove() -> Remove um elemento da lista. (Elemento 11)
""" nums.remove(11)
print(nums) """
# pop() ->	Remove e retorna determinado elemento de um índice da lista.(remove e retorna o elemento na posição 7)
""" print(nums.pop(7))
print(nums) """
# clear() -> remove todos os elementos da lista
""" nums.clear()
print(nums) """
#copy() -> Retorna uma cópia da lista.
# cria uma cópia da nums em numsCpy
""" numsCpy = nums.copy()
print(numsCpy) """
# count() -> Retorna a quantidade de um elemento na lista passado como argumento.
# conta quantos elementos 8 existem na lista
""" nums = numsCpy.copy()
print(nums.count(8)) """
# ordena os elementos de uma lista em ordem ascendente
""" nums.sort()
print(nums) """
# reverse() ->	Inverte a ordem dos elementos de uma lista.
""" nums.reverse()
print(nums) """

# A função max retorna o maior valor dentro de uma lista.
""" nums = [17, 33, 8, 11, 8, 15, 9]
print(max(nums)) """# isto mostrará o valor "33"
#Caso os elementos da lista sejam strings, a comparação é feita tomando por base a ordem alfabética.
""" herois = ["Zorro", "Capitão América", "Hulk", "Super-Homem"]
print(max(herois)) """# isto mostrará o valor "Zorro"

# A função min retorna o menor valor dentro de uma lista.
""" nums = [17, 33, 8, 11, 8, 15, 9]
print(min(nums)) """# isto mostrará o valor "8"
# Da mesma forma que a função max, caso os elementos da lista sejam strings, a função min efetua a comparação tomando por base a ordem alfabética.
""" herois = ["Zorro", "Capitão América", "Hulk", "Super-Homem"]
print(min(herois)) """# isto mostrará o valor "Capitão América"


# A função sorted retorna a lista passada em ordem crescente.
""" nums = [17, 33, 8, 11, 8, 15, 9]
sorted(nums) """# isto resultará em [8, 8, 9, 11, 15, 17, 33]
# Também é possível fazer a ordenaçã em ordem decrescente, por meio do parâmetro reverse.
""" nums = [17, 33, 8, 11, 8, 15, 9]
sorted(nums, reverse=True) """# isto resultará em [33, 17, 15, 11, 9, 8, 8]
# Ainda, pode-se aplicar a função sorted sobre uma string, retornando uma lista não editável, no caso, uma tupla, como será visto na próxima unidade.
""" nome = "José dos Santos"
sorted(nome) """
# isto resultará em [' ', ' ', 'J', 'S', 'a', 'd', 'n', 'o', 'o', 'o', 's', 's', 's', 't', 'é']

# A função sum retorna a soma de todos os elementos de uma lista.
""" nums = [17, 33, 8, 11, 8, 15, 9]
print(sum(nums)) """# isto resultará em "101"