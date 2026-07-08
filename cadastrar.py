from auxilio_json import ler_dados, salvar_dados

def cadastrar_aluno():
    while True:
        nome = input("nome do aluno: ").strip().lower()

        if nome == "":
            print("campo vazio")
            continue

        if not nome.isalpha():
            print("nome inválido")
            continue

        break

    while True:
        print("opções de turma:")
        print("1 a 9")

        turma = input("turma: ")

        if turma in ["1","2","3","4","5","6","7","8","9"]:
            print("turma cadastrada!")
            break
        else:
            print("turma inválida")

    aluno = {
        "nome": nome,
        "turma": turma
    }

    alunos = ler_dados()

    alunos.append(aluno)

    salvar_dados(alunos)

    print("Aluno cadastrado com sucesso!")
