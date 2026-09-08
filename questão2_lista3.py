def calcular(a, b):
    produto = a * b

    if produto <= 1000:
        return produto
    else:
        return a + b


a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

resultado = calcular(a, b)

print("Resultado:", resultado)