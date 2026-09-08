menor = None

for i in range(10):
    latencia = float(input(f"Digite a latência {i + 1}: "))

    if menor is None or latencia < menor:
        menor = latencia

print("Menor latência:", menor, "ms")