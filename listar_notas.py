from auxilio_json import ler_dados
from cadastrar import cadastrar_aluno

def listar_notas():

    alunos = ler_dados()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return


    for aluno in alunos:

        notas = aluno["notas"]

        soma = 0

        for nota in notas:
            soma = soma + nota

        media = soma / len(notas)


        if media >= 7:
            situacao = "Aprovado"

        elif media >= 5:
            situacao = "Recuperação"

        else:
            situacao = "Reprovado"


        print("----------------------")
        print("Matrícula:", aluno["matricula"])
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Turma:", aluno["turma"])
        print("Notas:", notas)
        print("Média:", media)
        print("Situação:", situacao)