codigos = []
for i in range(10):
    codigo = int(input(f"Digite o {i + 1} código: "))
    codigos.append(codigo)
    
verificados = []

print("\nQuantidade de ocorrências:")

for codigo in codigos:
    if codigo not in verificados:
        quantidade = codigos.count(codigo)

        print(f"Código {codigo}: {quantidade} vez(es)")

        verificados.append(codigo)