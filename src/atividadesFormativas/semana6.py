# Alessandra Bulka de Ramos
# Tecnologia em Análise e Desenvolvimento de Sistemas

import sys


def exibir_menu_principal():
    print('------ MENU PRINCIPAL ------\n')
    print('(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matrículas\n(0) Sair\n')

def exibir_menu_estudantes():
    print('Você escolheu a opção "Gerenciar estudantes" \n \n\n ------ Menu de operações ------\n')
    print('(1) Incluir\n(2) Listar\n(3) Editar\n(0) Sair\n')

def incluir_estudantes():
    print('Você será redirecionado para a tela de inserção de dados. Aguarde um instante...')
    qtdNomes = int(input('Quantos alunos você quer incluir?'))
    alunosLista = []
    for _ in range(qtdNomes):
        id_aluno = int(input('Informe o ID do aluno: '))
        nome_aluno = input('Informe o nome do aluno: ')
        cpf_aluno = input('Informe o CPF do aluno: ')
        aluno = {'ID': id_aluno, 'Nome': nome_aluno, 'CPF': cpf_aluno}
        alunosLista.append(aluno)
    print(f'Aqui está a lista de estudantes atualizada:\n{alunosLista}')
    sys.exit()
    return alunosLista

def listar_estudantes(alunosLista):
    if len(alunosLista) == 0:
        print('Não há estudantes cadastrados')
    else:
        print('Lista de estudantes:')
        for aluno in alunosLista:
            print(f"Código: {aluno['ID']}, Nome: {aluno['Nome']}, CPF: {aluno['CPF']}")

def editar_estudante(alunosLista):
    codigo_editar = int(input('Informe o código do estudante que deseja editar: '))
    encontrado = False
    for aluno in alunosLista:
        if aluno['ID'] == codigo_editar:
            print(f'Editando o estudante com código {codigo_editar}:')
            aluno['ID'] = int(input('Informe o novo código do estudante: '))
            aluno['Nome'] = input('Informe o novo nome do estudante: ')
            aluno['CPF'] = input('Informe o novo CPF do estudante: ')
            encontrado = True
            break
    if encontrado:
        print(f'O estudante com código {codigo_editar} foi atualizado com sucesso.')
    else:
        print(f'Não foi encontrado nenhum estudante com código {codigo_editar}.')

def executar_programa():
    alunosLista = []

    exibir_menu_principal()

    while True:
        option = int(input('Informe a opção desejada: '))

        if option == 1:
            exibir_menu_estudantes()

            operations = int(input('Escolha a operação desejada:'))

            if operations == 1:
                alunosLista = incluir_estudantes()
                sys.exit()
            elif operations == 2:
                listar_estudantes(alunosLista)
                sys.exit()
            elif operations == 3:
                editar_estudante(alunosLista)
                sys.exit()
            elif operations == 0:
                print('Sair')
            else:
                print('Você digitou uma opção inválida')

        elif 0 < option < 6:
            print('Em desenvolvimento')
        elif option == 0:
            print('Sair')
            break
        else:
            print('Você digitou uma opção inválida')

executar_programa()
