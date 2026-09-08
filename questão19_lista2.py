alunos = {
    "João": {
        "Nota1": 8.0,
        "Nota2": 7.5,
        "Média": 7.75
    },

    "Maria": {
        "Nota1": 5.0,
        "Nota2": 6.0,
        "Média": 5.5
    }
}

for nome, notas in alunos.items():
    print("Aluno:", nome)
    print("Nota 1:", notas["Nota1"])
    print("Nota 2:", notas["Nota2"])
    print("Média:", notas["Média"])

    if notas["Média"] >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

    print()