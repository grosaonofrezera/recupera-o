import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "ativo": True,
    "habilidades": ["Python", "JavaScript"]
}

# Salvando em um arquivo JSON
with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)