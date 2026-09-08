soma = 0
adequados = 0
superior = 0
maior = 0

for i in range(10):
    latencia = float(input(f"Digite a latência do teste {i + 1}: "))

    soma += latencia

    if latencia <= 100:
        adequados += 1
    else:
        superior += 1

    if i == 0 or latencia > maior:
        maior = latencia

media = soma / 10

print("\nTestes com latência menor ou igual a 100:", adequados)
print("Testes com latência superior a 100:", superior)
print("Média das latências:", media)
print("Maior latência:", maior)