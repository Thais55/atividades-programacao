estudantes = {
    "João": 8.5,
    "Maria": 6.0,
    "Ana": 7.0,
    "Pedro": 5.5
}

for nome, nota in estudantes.items():
    if nota >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("Nome:", nome)
    print("Nota:", nota)
    print("Situação:", situacao)
    print()