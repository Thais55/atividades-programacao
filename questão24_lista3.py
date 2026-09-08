import csv

estudantes = []

for i in range(10):
    print(f"\nEstudante {i + 1}")

    nome = input("Nome: ")
    nota1 = float(input("Nota da avaliação 1: "))
    nota2 = float(input("Nota da avaliação 2: "))
    nota3 = float(input("Nota da avaliação 3: "))

    media = (nota1 * 3 + nota2 * 4 + nota3 * 3) / 10

    estudantes.append({
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    })

maior = max(estudantes, key=lambda estudante: estudante["media"])

print("\n===== RESULTADO =====")

for estudante in estudantes:
    print(f"Nome: {estudante['nome']}")
    print(f"Notas: {estudante['nota1']}, "
          f"{estudante['nota2']}, "
          f"{estudante['nota3']}")
    print(f"Média: {estudante['media']:.2f}")
    print()

print(f"Maior média: {maior['nome']} - {maior['media']:.2f}")

with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota 1", "Nota 2", "Nota 3", "Média"])

    for estudante in estudantes:
        escritor.writerow([
            estudante["nome"],
            estudante["nota1"],
            estudante["nota2"],
            estudante["nota3"],
            estudante["media"]
        ])