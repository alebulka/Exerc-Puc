# Exemplo de aplicação 4: Elabore um programa que solicite ao usuário o cadastro de endereços para entrega de produtos de uma loja.
""" 
enderecos = []
print("Cadastro de Endereços de Entrega")
while True:
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradouro, numero, bairro, cidade, estado)
    enderecos.append(novo_endereco)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
print("Os endereços cadastrados são:")
for i in range(0, len(enderecos)):
    endereco = enderecos[i]
    print(f"{i}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")

 """

 # Exemplo de aplicação 5: Elabore um programa que crie uma tupla contendo duas listas com dados, altere os dados da primeira lista e verifique se ocorre mudança de dados da tupla.
""" tupla_com_lista = ([1, 2, 3], [4, 5, 6])
print(id(tupla_com_lista[0]))
tupla_com_lista[0].append(9)
print(tupla_com_lista)
print(id(tupla_com_lista[0])) """

# Concatenação de tuplas
# Exemplo de aplicação 6: Elabore um programa que concatene tuplas.
""" endereco_puc = ("Rua Imaculada Conceição", 1555, "Prado Velho", "Curitiba", "PR")
print(id(endereco_puc))
endereco_puc += ("Brazil",)
print(endereco_puc)
print(id(endereco_puc)) """

# No exemplo acima é possível verificar que, embora seja usado o operador “+=”, pela análise dos endereços de memória foi criada uma tupla, e esta tupla foi atribuída à variável endereco_puc. Outro ponto a destacar está na linha 03, em que se pode ver que uma tupla com um único dado deve ser declarada com uma vírgula no fim; caso contrário, o Python se confundirá e não entenderá que isto se trata de uma tupla. O próximo exemplo demonstrará isto para você. Testemos:

# Exemplo de aplicação 7: Elabore um aplicativo que demonstre a necessidade de finalizar uma tupla de um único elemento com uma vírgula no fim.
""" tupla1 = ("Brasil")
print(type(tupla1))
tupla2 = ("Brasil",)
print(type(tupla2)) """

# A função namedtuple() permite nomear tanto tuplas quanto seus dados, o que resulta em um código muito mais legível. Segue sua sintaxe:
# collections.namedtuple(typename, field_names)
# é necessário importar a função
# from collections import namedtuple

