from auxilio_json import ler_dados, salvar_dados

def editar_aluno():

    matricula_aluno = int(input("digite a matricula do aluno: "))

    print("1 - atualizar nome")
    print("2 - atualizar turma")

    escolha = input("escolha: ")

    dados = ler_dados()

    if escolha == "1":

        novo_nome = input("novo nome: ")

        for aluno in dados:
            if aluno["matricula"] == matricula_aluno:
                aluno["nome"] = novo_nome
                break

        salvar_dados(dados)

        print("nome atualizado!")

    elif escolha == "2":

        nova_turma = input("nova turma: ")

        for aluno in dados:
            if aluno["matricula"] == matricula_aluno:
                aluno["turma"] = nova_turma
                break

        salvar_dados(dados)

        print("turma atualizada!")

    else:
        print("opção inválida")