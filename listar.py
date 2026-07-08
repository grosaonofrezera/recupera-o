from auxilio_json import ler_dados

def listar_alunos():

    dados = ler_dados()

    if len(dados) == 0:
        print("nenhum aluno cadastrado")

    else:

        print("\n=== lista de alunos ===")

        for aluno in dados:

            print("nome:", aluno["nome"])
            print("turma:", aluno["turma"])
            print()