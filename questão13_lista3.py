continuar = "S"

while continuar.upper() == "S":
    print("\n1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")

    opcao = int(input("Escolha a conversão: "))
    temperatura = float(input("Digite a temperatura: "))

    if opcao == 1:
        resultado = temperatura * 9 / 5 + 32
        print("Resultado:", resultado, "°F")

    elif opcao == 2:
        resultado = temperatura + 273.15
        print("Resultado:", resultado, "K")

    elif opcao == 3:
        resultado = (temperatura - 32) * 5 / 9
        print("Resultado:", resultado, "°C")

    elif opcao == 4:
        resultado = (temperatura - 32) * 5 / 9 + 273.15
        print("Resultado:", resultado, "K")

    elif opcao == 5:
        resultado = temperatura - 273.15
        print("Resultado:", resultado, "°C")

    elif opcao == 6:
        resultado = (temperatura - 273.15) * 9 / 5 + 32
        print("Resultado:", resultado, "°F")

    else:
        print("Opção inválida.")

    continuar = input("Deseja realizar outra conversão? (S/N): ")