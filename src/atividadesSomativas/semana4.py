# Alessandra Bulka de Ramos
# Tecnologia em Análise e Desenvolvimento de Sistemas

print('------ MENU PRINCIPAL ------\n')
print('(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matrículas\n(0) Sair\n')
option = int(input('Informe a opção desejada: '))

if option == 1 :
    print('Você escolheu a opção "Gerenciar estudantes" \n \n\n ------ Menu de operações ------\n')
    print('(1) Incluir\n(2) Listar\n(3) Atualizar\n(4) Excluir\n(0) Sair\n')
    operations = int(input('Escolha a operação desejada:'))

    if operations == 1:
        # Opção incluir
        print('Você será redirecionado para a tela de inserção de dados. Aguarde um instante...')
        qtdNomes = int(input('Quantos alunos você quer incluir?'))
        nomesLista = []
        for i in range(qtdNomes):
            nomes = input('Escreva o nome do aluno: ')
            nomesLista.append(nomes)
        print(f'Aqui está a lista de estudantes atualizada:\n{nomesLista}')
    elif operations == 2:
        # Opção listar
        print('Não há estudantes cadastrados')
    elif operations == 3 or operations == 4:
        # Opções atualizar e excluir
        print('Em desenvolvimento')
    elif operations == 0:
        # Opção Sair
        print('Sair')
    else:
        print('Você digitou uma opção inválida')
elif option == 2 or option == 3 or option == 4 or option == 5:
     print('Em desenvolvimento')
elif option == 0:
    print('Sair')
else:
    print('Você digitou uma opção inválida')