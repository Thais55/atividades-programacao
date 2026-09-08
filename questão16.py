tensao = float(input("Digite a tensão em volts: "))
corrente = float(input("Digite a corrente em ampères: "))

resistencia = tensao / corrente

print(f"Resistência elétrica: {resistencia:.2f} Ω")