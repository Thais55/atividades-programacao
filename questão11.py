valor = float(input("Digite o valor do empréstimo: R$ "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite a quantidade de meses: "))

juros = valor * (taxa / 100) * meses
montante = valor + juros

print(f"Juros pagos: R$ {juros:.2f}")
print(f"Montante total: R$ {montante:.2f}")