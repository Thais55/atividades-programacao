numero = int(input("Digite um número entre 1 e 10: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")