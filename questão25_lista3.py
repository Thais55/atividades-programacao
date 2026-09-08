matriz = []

for i in range(4):
    linha = []

    for j in range(3):
        valor = float(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)

    matriz.append(linha)

valores = []

for linha in matriz:
    for valor in linha:
        valores.append(valor)

if len(valores) != len(set(valores)):
    print("Existem valores repetidos na matriz.")
else:
    print("Não existem valores repetidos na matriz.")