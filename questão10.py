valor = float(input("Digite o valor financiado : "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
meses = int(input("Digite a quantidade de meses : "))
juros = valor * (taxa / 100) * meses 
montante = valor * juros
print("Juros acumulados : ")
print(" Montante total : ",montante )
