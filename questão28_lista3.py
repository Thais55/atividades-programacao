dd_pesquisa = input("Digite o DD que deseja pesquisar: ")

encontrados = []

with open("agenda.txt", "r", encoding="utf-8") as arquivo:
    blocos = arquivo.read().strip().split("\n\n")

for bloco in blocos:
    linhas = bloco.split("\n")

    if len(linhas) >= 4:
        nome = linhas[0].replace("Nome: ", "")
        dd = linhas[2].replace("DD: ", "")

        if dd == dd_pesquisa:
            encontrados.append(nome)

print(f"\nQuantidade de pessoas com DD {dd_pesquisa}: {len(encontrados)}")

if encontrados:
    print("\nPessoas encontradas:")

    for nome in encontrados:
        print(nome)