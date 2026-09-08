equipamentos = []
LIMITE = 100
continuar = "S"

while continuar == "S" and len(equipamentos) < LIMITE:
    print("\nCADASTRO DE EQUIPAMENTO")

    patrimonio = input("Número de patrimônio: ")
    modelo = input("Modelo: ")
    ano = input("Ano de fabricação: ")
    situacao = input(
        "Situação (ATIVO, MANUTENÇÃO, EMPRÉSTIMO OU BAIXADO): "
    ).upper()
    setor = input("Setor onde está instalado: ")

    equipamento = {
        "patrimonio": patrimonio,
        "modelo": modelo,
        "ano": ano,
        "situacao": situacao,
        "setor": setor
    }

    equipamentos.append(equipamento)

    continuar = input(
        "\nDeseja cadastrar um novo equipamento? (S/N): "
    ).upper()

print("\nEQUIPAMENTOS CADASTRADOS")

if len(equipamentos) == 0:
    print("Nenhum equipamento foi cadastrado.")
else:
    for equipamento in equipamentos:
        print("\nNúmero do patrimônio:", equipamento["patrimonio"])
        print("Modelo:", equipamento["modelo"])
        print("Ano de fabricação:", equipamento["ano"])
        print("Situação:", equipamento["situacao"])
        print("Setor:", equipamento["setor"])

    # Pesquisa por situação
    situacao_pesquisa = input(
        "\nDigite a situação que deseja pesquisar: "
    ).upper()

    quantidade = 0

    for equipamento in equipamentos:
        if equipamento["situacao"] == situacao_pesquisa:
            print("\nNúmero do patrimônio:", equipamento["patrimonio"])
            print("Modelo:", equipamento["modelo"])
            print("Ano de fabricação:", equipamento["ano"])
            print("Situação:", equipamento["situacao"])
            print("Setor:", equipamento["setor"])
            quantidade += 1

    print(f"\nQuantidade de equipamentos encontrados: {quantidade}")

    # Salvar dados no arquivo
    with open("equipamentos.txt", "w", encoding="utf-8") as arquivo:
        for equipamento in equipamentos:
            arquivo.write(f"Patrimônio: {equipamento['patrimonio']}\n")
            arquivo.write(f"Modelo: {equipamento['modelo']}\n")
            arquivo.write(f"Ano de fabricação: {equipamento['ano']}\n")
            arquivo.write(f"Situação: {equipamento['situacao']}\n")
            arquivo.write(f"Setor: {equipamento['setor']}\n")
            arquivo.write("------------------------------\n")

    print("\nDados salvos com sucesso no arquivo equipamentos.txt.")
