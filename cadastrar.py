from auxilio_json import ler_dados, salvar_dados


def cadastrar_aluno():

    while True:
        nome = input("Nome do aluno: ").strip().lower()

        if nome == "":
            print("Campo vazio")
            continue

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido")
            continue

        break


    while True:
        idade = input("Qual sua idade: ")

        if idade.isdigit():
            idade = int(idade)

            if 0 < idade <= 120:
                break

        print("Idade inválida")


    while True:
        print("Opções de turma: 1 a 9")

        turma = input("Turma: ")

        if turma in ["1","2","3","4","5","6","7","8","9"]:
            break

        print("Turma inválida")


    while True:
        try:
            nota1 = float(input("Nota 1 (0-10): "))

            if 0 <= nota1 <= 10:
                break

            print("Nota inválida")

        except:
            print("Digite um número válido")


    while True:
        try:
            nota2 = float(input("Nota 2 (0-10): "))

            if 0 <= nota2 <= 10:
                break

            print("Nota inválida")

        except:
            print("Digite um número válido")


    alunos = ler_dados()


    if len(alunos) == 0:
        matricula = 1
    else:
        matricula = alunos[-1]["matricula"] + 1


    aluno = {
        "matricula": matricula,
        "nome": nome,
        "idade": idade,
        "turma": turma,
        "notas": [nota1, nota2]
    }


    alunos.append(aluno)

    salvar_dados(alunos)


    print("Aluno cadastrado com sucesso!")
    print(f"Matrícula: {matricula}")