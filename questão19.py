potencia = float(input("Digite a potência em watts: "))
tensao = float(input("Digite a tensão em volts: "))

corrente = potencia / tensao

print(f"Corrente elétrica: {corrente:.2f} A")