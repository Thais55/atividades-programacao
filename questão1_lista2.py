soma = 0
contador = 0

while contador < 10:
    numero = int(input("Digite um número divisível por 6: "))

    if numero % 6 == 0:
        soma += numero
        contador += 1
    else:
        print("Número inválido. Digite um número divisível por 6.")

print("Soma dos 10 números:", soma)