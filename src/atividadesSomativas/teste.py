# Alessandra Bulka de Ramos
# Tecnologia em Análise e Desenvolvimento de Sistemas

import json

class Gerenciador:
    def __init__(self):
        self.alunosLista = []
        self.professoresLista = []

    def exibir_menu_principal(self):
        print('------ MENU PRINCIPAL ------\n')
        print('(1) Gerenciar estudantes\n(2) Gerenciar professores\n(3) Gerenciar disciplinas\n(4) Gerenciar turmas\n(5) Gerenciar matrículas\n(0) Sair\n')

    def exibir_menu_secundario(self, option):
        print(f'Você escolheu a opção "Gerenciar {option}" \n \n\n ------ Menu de operações ------\n')
        print('(1) Incluir\n(2) Listar\n(3) Editar\n(4) Excluir\n(5) Salvar em arquivo\n(6) Recuperar de arquivo\n(0) Sair\n')

    def incluir_item(self, lista, item):
        id_item = int(input(f'Informe o ID do {item.lower()}: '))
        nome_item = input(f'Informe o nome do {item.lower()}: ')
        # ... Coletar outras informações relevantes
        novo_item = {'ID': id_item, 'Nome': nome_item}
        lista.append(novo_item)
        print(f'O {item.lower()} com ID {id_item} foi incluído com sucesso.')

    def listar_itens(self, lista, item):
        if len(lista) == 0:
            print(f'Não há {item.lower()} cadastrados')
        else:
            print(f'Lista de {item.lower()}s:')
            for elemento in lista:
                print(f"Código: {elemento['ID']}, Nome: {elemento['Nome']}")
            print()

    def editar_item(self, lista, item):
        codigo_editar = int(input(f'Informe o código do {item.lower()} que deseja editar: '))
        encontrado = False
        for elemento in lista:
            if elemento['ID'] == codigo_editar:
                print(f'Editando o {item.lower()} com código {codigo_editar}:')
                elemento['ID'] = int(input(f'Informe o novo código do {item.lower()}: '))
                elemento['Nome'] = input(f'Informe o novo nome do {item.lower()}: ')
                encontrado = True
                break
        if encontrado:
            print(f'O {item.lower()} com código {codigo_editar} foi atualizado com sucesso.')
        else:
            print(f'Não foi encontrado nenhum {item.lower()} com código {codigo_editar}.')

    def excluir_item(self, lista, item):
        codigo_excluir = int(input(f'Informe o código do {item.lower()} que deseja excluir: '))
        encontrado = False
        for elemento in lista:
            if elemento['ID'] == codigo_excluir:
                lista.remove(elemento)
                encontrado = True
                print(f'O {item.lower()} com código {codigo_excluir} foi excluído com sucesso.')
                break
        if not encontrado:
            print(f'Não foi encontrado nenhum {item.lower()} com código {codigo_excluir}.')

    def salvar_itens(self, lista, item, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(lista, arquivo)
        print(f'Lista de {item.lower()}s salva com sucesso.')

    def recuperar_itens(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                lista = json.load(arquivo)
        except FileNotFoundError:
            print(f'Arquivo {nome_arquivo} não encontrado. Criando um novo arquivo...')
            lista = []
        return lista

    def executar_programa(self):
        while True:
            self.exibir_menu_principal()
            option = int(input('Informe a opção desejada: '))

            if option == 1:
                self.exibir_menu_secundario('estudantes')

                while True:
                    operations = int(input('Escolha a operação desejada: '))

                    if operations == 1:
                        self.incluir_item(self.alunosLista, 'Estudante')
                    elif operations == 2:
                        self.listar_itens(self.alunosLista, 'Estudante')
                    elif operations == 3:
                        self.editar_item(self.alunosLista, 'Estudante')
                    elif operations == 4:
                        self.excluir_item(self.alunosLista, 'Estudante')
                    elif operations == 5:
                        self.salvar_itens(self.alunosLista, 'Estudante', 'alunos.json')
                    elif operations == 6:
                        self.alunosLista = self.recuperar_itens('alunos.json')
                    elif operations == 0:
                        print('Sair')
                        break
                    else:
                        print('Você digitou uma opção inválida')

            elif option == 2:
                self.exibir_menu_secundario('professores')

                while True:
                    operations = int(input('Escolha a operação desejada: '))

                    if operations == 1:
                        self.incluir_item(self.professoresLista, 'Professor')
                    elif operations == 2:
                        self.listar_itens(self.professoresLista, 'Professor')
                    elif operations == 3:
                        self.editar_item(self.professoresLista, 'Professor')
                    elif operations == 4:
                        self.excluir_item(self.professoresLista, 'Professor')
                    elif operations == 5:
                        self.salvar_itens(self.professoresLista, 'Professor', 'professores.json')
                    elif operations == 6:
                        self.professoresLista = self.recuperar_itens('professores.json')
                    elif operations == 0:
                        print('Sair')
                        break
                    else:
                        print('Você digitou uma opção inválida')

            # Repetir o mesmo padrão para as demais opções

    executar_programa(self)