inventario = {
    "001": {
        "equipamento": "Computador",
        "marca": "Dell",
        "situacao": "Funcionando"
    },

    "002": {
        "equipamento": "Notebook",
        "marca": "Lenovo",
        "situacao": "Em manutenção"
    }
}

for patrimonio, informacoes in inventario.items():
    print("Patrimônio:", patrimonio)

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

    print()