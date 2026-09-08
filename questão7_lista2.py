notas = []

quantidade = int(input("Quantas notas deseja informar? "))

for i in range(quantidade):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

try:
    media = sum(notas) / len(notas)
    print("Média:", media)

except ZeroDivisionError:
    print("A lista está vazia. Não é possível calcular a média.")