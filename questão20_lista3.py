medicoes = []

for i in range(5):
    memoria = float(input(f"Digite a medição {i + 1}: "))
    medicoes.append(memoria)

soma = sum(medicoes)

print("Soma das medições:", soma) 