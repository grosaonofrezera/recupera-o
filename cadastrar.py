import json

def cadastrar_aluno():
    while True:
        nome = input("Nome do aluno: ").strip().lower()

        if nome == "":
            print("Campo vazio.")
            continue

        if not nome.isalpha():
            print("Nome inválido.")
            continue

        break

    while True:
        print("Opções de turma:")
        print("1 a 9")

        turma = input("Turma: ")

        if turma in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            break
        else:
            print("Turma inválida.")

    aluno = {
        "nome": nome,
        "turma": turma
    }

    try:
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)
    except FileNotFoundError:
        alunos = []

    alunos.append(aluno)

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

    print("Aluno cadastrado com sucesso!")

cadastrar_aluno()