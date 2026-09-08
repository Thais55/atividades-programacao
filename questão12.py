total = 0

for i in range(1, 5):
    quantidade = int(input(f"Digite a quantidade recebida pelo setor {i}: "))
    total += quantidade

print(f"Total de produtos recebidos: {total}")