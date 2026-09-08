import csv

estudantes = []
aprovados = 0
reprovados = 0

for i in range(10):
    print(f"\nEstudante {i + 1}")

    nome = input("Nome: ")
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 6:
        situacao = "APROVADO"
        aprovados += 1
    else:
        situacao = "REPROVADO"
        reprovados += 1

    estudantes.append([
        nome,
        nota1,
        nota2,
        media,
        situacao
    ])

print("\n===== RELATÓRIO =====")

for estudante in estudantes:
    print(f"Nome: {estudante[0]}")
    print(f"Nota 1: {estudante[1]:.2f}")
    print(f"Nota 2: {estudante[2]:.2f}")
    print(f"Média: {estudante[3]:.2f}")
    print(f"Situação: {estudante[4]}")
    print()

print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

with open("notas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "Nome",
        "Nota 1",
        "Nota 2",
        "Média",
        "Situação"
    ])

    escritor.writerows(estudantes)