num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, * ou /): ")

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Não é possível dividir por zero.")
        resultado = None

else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)