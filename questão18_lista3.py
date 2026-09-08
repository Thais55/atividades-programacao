equipamentos = []

for i in range(5):
    nome = input("Digite o nome do equipamento: ")
    preco = float(input("Digite o preço: "))

    equipamentos.append({
        "nome": nome,
        "preco": preco
    })

print("\nEquipamentos cadastrados:")

for equipamento in equipamentos:
    print(equipamento["nome"], "- R$", equipamento["preco"])

mais_caro = equipamentos[0]

for equipamento in equipamentos:
    if equipamento["preco"] > mais_caro["preco"]:
        mais_caro = equipamento

print("\nEquipamento mais caro:")
print(mais_caro["nome"], "- R$", mais_caro["preco"])