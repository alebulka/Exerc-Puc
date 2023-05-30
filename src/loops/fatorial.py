# inicializamos a variável fatorial com o valor 1. Esta variável será usada para armazenar o resultado do cálculo do fatorial.
fatorial = 1
# inicializamos a variável expressao com a string "Expressão: ". Ela será usada para construir e exibir a expressão matemática do fatorial.
expressao = "Expressão: "

num = int(input("Digite um número para o cálculo do fatorial: "))
# o algoritmo entra no laço for que itera de num até 1, decrementando 1 a cada iteração (range(num, 0, -1)) (esse terceiro valor -1 vai minimizar o valor total até o 0).
for i in range(num, 0, -1):
    # em cada iteração, multiplicamos o valor atual de fatorial pelo valor de i (índice da iteração) e atualizamos a variável fatorial com o resultado.
    fatorial *= i
    # adicionamos o valor de i convertido para string à variável expressao.
    expressao += str(i)
    if i > 1:
        expressao += " * "
print("O valor do fatorial de", num, "é", fatorial, expressao)