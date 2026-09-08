valores = []

for i in range(7):
    numero = int(input(f"Digite o valor {i + 1}: "))
    valores.append(numero)

print("Valores na ordem inversa:")

for numero in reversed(valores):
    print(numero)