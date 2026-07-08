from cadastrar import cadastrar_aluno
from listar import listar_alunos

def menu():

    while True:

        print("=== MENU MAIS FODA DA HISTORIA ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Editar aluno")
        print("4 - Remover aluno")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            editar_aluno()

        elif opcao == "4":
            remover_aluno()

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

menu()