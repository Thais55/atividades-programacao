tensao = float(input("Digite a tensão em volts: "))
resistencia = float(input("Digite a resistência em ohms: "))

corrente = tensao / resistencia

print(f"Corrente elétrica: {corrente:.2f} A")