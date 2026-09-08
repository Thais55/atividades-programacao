from  import (
soma,
subtracao,
multiplicacao,
divisao,
potencia,
resto
)

print("===== CALCULADORA =====")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Resto da divisão")

opcao = int(input("Escolha uma operação: "))

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = soma(a, b)
elif opcao == 2:
    resultado = subtracao(a, b)
elif opcao == 3:
    resultado = multiplicacao(a, b)
elif opcao == 4:
    if b != 0:
        resultado = divisao(a, b)
    else:
        resultado = "Não é possível dividir por zero."
elif opcao == 5:
    resultado = potencia(a, b)
elif opcao == 6:
    if b != 0:
        resultado = resto(a, b)
    else:
        resultado = "Não é possível dividir por zero."
else:
    resultado = "Opção inválida."

print("Resultado:", resultado)