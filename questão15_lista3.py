soma = 0
quantidade = 0

for numero in range(1, 20):
    if numero % 2 == 0:
        soma += numero
        quantidade += 1

media = soma / quantidade

print("Média dos identificadores:", media)