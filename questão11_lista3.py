maior = None

for i in range(15):
    valor = float(input(f"Digite o valor {i + 1}: "))

    if maior is None or valor > maior:
        maior = valor

print("Maior valor registrado:", maior)