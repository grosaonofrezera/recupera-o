import json

def ler_dados():
    with open("dados.json", "r") as arquivo:
        alunos = json.load(arquivo)
    return alunos

def salvar_dados(alunos):
    with open("dados.json", "w") as arquivo:
        json.dump(alunos, arquivo, indent=4)