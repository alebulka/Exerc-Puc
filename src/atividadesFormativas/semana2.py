# Menu principal
print('------ MENU PRINCIPAL ------\n')
print('(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matrículas\n(0) Sair\n')
option = int(input('Informe a opção desejada: '))

while True:
    try:
        if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
            print(f'Você escolheu a opção {option} \n \n\n ------ Menu de operações ------\n')
            print('(1) Incluir\n(2) Listar\n(3) Atualizar\n(4) Excluir\n(0) Sair\n')
            operations = int(input('Escolha a operação desejada:'))

            if operations == 1:
                # Opção Incluir
                print('Você será redirecionado para a tela de inserção de dados. Aguarde um instante...')
            elif operations == 2:
                # Opção Listar
                print('Aguarde um instante...')
            elif operations == 3:
                # Opção Atualizar
                print('Você será redirecionado para a tela de atualização de dados. Aguarde um instante...')
            elif operations == 4:
                # Opção Excluir
                print('Você tem certeza disso?\n(Sim)     (Não)')
            elif operations == 0:
                # Opção Sair
                print('Sair')
            else:
                print('Você digitou uma opção inválida')
        elif option == 0:
            print('Sair')
    except ValueError:
        print('Você digitou uma opção inválida')