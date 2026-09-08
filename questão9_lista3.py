inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o último número: "))

soma = 0
quantidade = 0

for numero in range(inicio, fim + 1):
    soma += numero
    quantidade += 1

media = soma / quantidade

print("Média dos números:", media)