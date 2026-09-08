num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

inicio = min(num1, num2)
fim = max(num1, num2)

for numero in range(inicio, fim + 1):
    print(numero)