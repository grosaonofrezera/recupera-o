from auxilio_json import ler_dados, salvar_dados
from cadastrar import cadastrar_aluno
while True:
    try:
        nota1 = float(input("nota 1 (0-10): "))
        if nota1 < 0 or nota1 > 10:
            print("nota inválida")
            continue
        break
    except:
        print("digite um número válido")

while True:
    try:
        nota2 = float(input("nota 2 (0-10): "))
        if nota2 < 0 or nota2 > 10:
            print("nota inválida")
            continue
        break
    except:
        print("digite um número válido")

for aluno in dados:
    if aluno["matricula"] == matricula_aluno:
        aluno["notas"] = [nota1, nota2]
        break

    salvar_dados(dados)

    print("notas registradas com sucesso!")