soma = 0
num = -1
while True:
    try:
        num = int(input("Digite um número para somar (0 finaliza): "))
        if num == 0:
            break
        soma += num
    except ValueError:
        print("Valor inválido")
print("A soma dos números é ", soma)
