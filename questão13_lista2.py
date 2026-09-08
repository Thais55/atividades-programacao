disciplina = {
    "nome": "Programação",
    "professor": "Professor Carlos",
    "carga_horaria": 60,
    "periodo": 2
}

chave = input("Digite o nome da chave: ")

if chave in disciplina:
    print("A chave existe.")
else:
    print("A chave não foi encontrada.")