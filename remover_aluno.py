from auxilio_json import ler_dados, salvar_dados
from cadastrar import cadastrar_aluno

def remover_aluno():

    alunos = ler_dados()


    if len(alunos) == 0:
        print("Não há alunos cadastrados")
        return


    print("Lista de alunos:")

    for aluno in alunos:
        print(
            "Matrícula:", aluno["matricula"],
            "| Nome:", aluno["nome"],
            "| Turma:", aluno["turma"]
        )


    matricula = int(input("Digite a matrícula do aluno que deseja remover: "))


    for aluno in alunos:

        if aluno["matricula"] == matricula:

            alunos.remove(aluno)

            salvar_dados(alunos)

            print("Aluno removido com sucesso!")
            return


    print("Matrícula não encontrada")