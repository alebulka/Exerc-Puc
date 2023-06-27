# Alessandra Bulka de Ramos
# Tecnologia em Análise e Desenvolvimento de Sistemas

import json

def exibir_menu_principal():
    print('------ MENU PRINCIPAL ------\n')
    print('(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matrículas\n(0) Sair\n')

def exibir_menu_secundario(option):
    print(f'Você escolheu a opção "Gerenciar {option}" \n \n\n ------ Menu de operações ------\n')
    print('(1) Incluir\n(2) Listar\n(3) Editar\n(4) Excluir\n(5) Salvar em arquivo\n(6) Recuperar de arquivo\n(0) Sair\n')

def incluir_item(lista, nome_item):
    id_item = int(input(f'Informe o ID do {nome_item}: '))
    nome_item = input(f'Informe o nome do {nome_item}: ')
    cpf_item = input(f'Informe o CPF do {nome_item}: ')
    item = {'ID': id_item, 'Nome': nome_item, 'CPF': cpf_item}
    lista.append(item)
    print(f'O {nome_item} com ID {id_item} foi incluído com sucesso.')

def listar_itens(lista, nome_item):
    if len(lista) == 0:
        print(f'Não há {nome_item.lower()}s cadastrados')
    else:
        print(f'Lista de {nome_item.lower()}s:')
        for item in lista:
            print(f"Código: {item['ID']}, Nome: {item['Nome']}, CPF: {item['CPF']}")

def editar_item(lista, nome_item):
    codigo_editar = int(input(f'Informe o código do {nome_item.lower()} que deseja editar: '))
    encontrado = False
    for item in lista:
        if item['ID'] == codigo_editar:
            print(f'Editando o {nome_item.lower()} com código {codigo_editar}:')
            item['ID'] = int(input(f'Informe o novo código do {nome_item.lower()}: '))
            item['Nome'] = input(f'Informe o novo nome do {nome_item.lower()}: ')
            item['CPF'] = input(f'Informe o novo CPF do {nome_item.lower()}: ')
            encontrado = True
            break
    if encontrado:
        print(f'O {nome_item.lower()} com código {codigo_editar} foi atualizado com sucesso.')
    else:
        print(f'Não foi encontrado nenhum {nome_item.lower()} com código {codigo_editar}.')

def excluir_item(lista, nome_item):
    codigo_excluir = int(input(f'Informe o código do {nome_item.lower()} que deseja excluir: '))
    encontrado = False
    for item in lista:
        if item['ID'] == codigo_excluir:
            lista.remove(item)
            encontrado = True
            print(f'O {nome_item.lower()} com código {codigo_excluir} foi removido com sucesso.')
            break
    if not encontrado:
        print(f'Não foi encontrado nenhum {nome_item.lower()} com código {codigo_excluir}.')

def salvar_itens(lista, nome_item, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)
    print(f'Lista de {nome_item.lower()}s salva com sucesso.')

def recuperar_itens(lista, nome_item, nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista = json.load(arquivo)
        print(f'Lista de {nome_item.lower()}s recuperada com sucesso.')
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} não encontrado. A lista de {nome_item.lower()}s não foi alterada.')

    return lista

def executar_programa():
    alunosLista = []
    professoresLista = []
    disciplinasLista = []
    turmasLista = []
    matriculasLista = []

    while True:
        exibir_menu_principal()
        option = int(input('Informe a opção desejada: '))

        if option == 1:
            exibir_menu_secundario('estudantes')
            operations = int(input('Escolha a operação desejada: '))

            if operations == 1:
                incluir_item(alunosLista, "Estudante")
            elif operations == 2:
                listar_itens(alunosLista, "Estudante")
            elif operations == 3:
                editar_item(alunosLista, "Estudante")
            elif operations == 4:
                excluir_item(alunosLista, "Estudante")
            elif operations == 5:
                nome_arquivo = input('Informe o nome do arquivo para salvar os estudantes: ')
                salvar_itens(alunosLista, "Estudante", nome_arquivo)
            elif operations == 6:
                nome_arquivo = input('Informe o nome do arquivo para recuperar os estudantes: ')
                alunosLista = recuperar_itens(alunosLista, "Estudante", nome_arquivo)
            elif operations == 0:
                print('Sair')
                break
            else:
                print('Você digitou uma opção inválida')

        elif option == 2:
            exibir_menu_secundario('professores')
            operations = int(input('Escolha a operação desejada: '))

            if operations == 1:
                incluir_item(professoresLista, "Professor")
            elif operations == 2:
                listar_itens(professoresLista, "Professor")
            elif operations == 3:
                editar_item(professoresLista, "Professor")
            elif operations == 4:
                excluir_item(professoresLista, "Professor")
            elif operations == 5:
                nome_arquivo = input('Informe o nome do arquivo para salvar os professores: ')
                salvar_itens(professoresLista, "Professor", nome_arquivo)
            elif operations == 6:
                nome_arquivo = input('Informe o nome do arquivo para recuperar os professores: ')
                professoresLista = recuperar_itens(professoresLista, "Professor", nome_arquivo)
            elif operations == 0:
                print('Sair')
                break
            else:
                print('Você digitou uma opção inválida')

        elif option == 3:
            exibir_menu_secundario('disciplinas')
            operations = int(input('Escolha a operação desejada: '))

            if operations == 1:
                incluir_item(disciplinasLista, "Disciplina")
            elif operations == 2:
                listar_itens(disciplinasLista, "Disciplina")
            elif operations == 3:
                editar_item(disciplinasLista, "Disciplina")
            elif operations == 4:
                excluir_item(disciplinasLista, "Disciplina")
            elif operations == 5:
                nome_arquivo = input('Informe o nome do arquivo para salvar as disciplinas: ')
                salvar_itens(disciplinasLista, "Disciplina", nome_arquivo)
            elif operations == 6:
                nome_arquivo = input('Informe o nome do arquivo para recuperar as disciplinas: ')
                disciplinasLista = recuperar_itens(disciplinasLista, "Disciplina", nome_arquivo)
            elif operations == 0:
                print('Sair')
                break
            else:
                print('Você digitou uma opção inválida')

        elif option == 4:
            exibir_menu_secundario('turmas')
            operations = int(input('Escolha a operação desejada: '))

            if operations == 1:
                incluir_item(turmasLista, "Turma")
            elif operations == 2:
                listar_itens(turmasLista, "Turma")
            elif operations == 3:
                editar_item(turmasLista, "Turma")
            elif operations == 4:
                excluir_item(turmasLista, "Turma")
            elif operations == 5:
                nome_arquivo = input('Informe o nome do arquivo para salvar as turmas: ')
                salvar_itens(turmasLista, "Turma", nome_arquivo)
            elif operations == 6:
                nome_arquivo = input('Informe o nome do arquivo para recuperar as turmas: ')
                turmasLista = recuperar_itens(turmasLista, "Turma", nome_arquivo)
            elif operations == 0:
                print('Sair')
                break
            else:
                print('Você digitou uma opção inválida')

        elif option == 5:
            exibir_menu_secundario('matrículas')
            operations = int(input('Escolha a operação desejada: '))

            if operations == 1:
                incluir_item(matriculasLista, "Matrícula")
            elif operations == 2:
                listar_itens(matriculasLista, "Matrícula")
            elif operations == 3:
                editar_item(matriculasLista, "Matrícula")
            elif operations == 4:
                excluir_item(matriculasLista, "Matrícula")
            elif operations == 5:
                nome_arquivo = input('Informe o nome do arquivo para salvar as matrículas: ')
                salvar_itens(matriculasLista, "Matrícula", nome_arquivo)
            elif operations == 6:
                nome_arquivo = input('Informe o nome do arquivo para recuperar as matrículas: ')
                matriculasLista = recuperar_itens(matriculasLista, "Matrícula", nome_arquivo)
            elif operations == 0:
                print('Sair')
                break
            else:
                print('Você digitou uma opção inválida')

        elif option == 0:
            print('Sair')
            break
        else:
            print('Você digitou uma opção inválida')

executar_programa()
