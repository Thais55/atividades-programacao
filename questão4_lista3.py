softwares = ["Windows", "Word", "Excel", "Chrome", "Python"]

print("Lista original:")
print(softwares)

novo = input("Digite o nome do novo software: ")
softwares.append(novo)

del softwares[1]

print("\nLista após as alterações:")
print(softwares)