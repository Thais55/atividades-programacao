notas = []

for i in range(5):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Entrada inválida. Digite um número.")

print("Todas as notas:", notas)
print("Média:", sum(notas) / len(notas))
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))