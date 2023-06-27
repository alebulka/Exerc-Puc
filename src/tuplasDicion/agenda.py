# Exemplo de aplicação 1: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda, exibindo, ao final, o dicionário.
""" agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
print(agenda) """

""" Vamos entender o que cada linha faz:

    Linha 01: Criamos um dicionário vazio com o nome de agenda. Sabemos disso porque abrimos e fechamos as chaves (“{}”) sem nada dentro. Este dicionário será usado para armazenar pares de chave-valor, onde a chave é o nome do contato e o valor é o número de telefone do contato.
    Linha 02: Exibimos a mensagem "*** Cadastro de telefones ***".
    Linha 03: Iniciamos um laço de repetição infinito, que só será interrompido quando o usuário decidir.
        Linhas 04 e 05: Solicitamos ao usuário para que insira o nome e o número de telefone do contato. Guardamos estas informações nas variáveis chamadas contato e telefone, respectivamente.
        Linha 06: Adicionamos o telefone no dicionário agenda. A chave para encontrarmos o telefone será o contato.
    Linhas 07 e 08: Perguntamos ao usuário se ele deseja cadastrar um novo contato. Se o usuário digitar "n", o laço é interrompido.

    Linhas 09: Mostramos o dicionário agenda, mostrando todos os contatos e seus respectivos números de telefone que foram cadastrados. """



# Exemplo de aplicação 2: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda. Caso seja informado um nome já existente, deve perguntar se deseja alterar os dados existentes. Caso seja um telefone já existente, deve informar que esse telefone já está cadastrado em outro contato, não podendo ser efetuada a inclusão. Ao final, deve exibir o dicionário.

""" agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já cadastrado com o número {agenda[contato]}. Deseja alterar? (s/n) ") == "n":
            continue
    if telefone in agenda.values():
        print("Telefone já cadastrado para outro contato")
        continue
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
print(agenda) """

# Exemplo de aplicação 3: Elabore um programa que exemplifique a remoção de itens de um dicionário usando o método pop().

""" agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789"}
print(agenda)
print(agenda.pop("Maria", "Contato com nome Maria localizado"))
print(agenda) """
""" print(agenda.pop("José", "Contato com nome José não localizado")) """