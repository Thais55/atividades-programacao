contatos = []

while True:
    print("\n===== CADASTRO =====")

    nome = input("Nome: ")
    endereco = input("Endereço: ")
    dd = input("DD: ")
    telefone = input("Telefone: ")

    contatos.append({
        "nome": nome,
        "endereco": endereco,
        "dd": dd,
        "telefone": telefone
    })

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()

    if continuar != "s":
        break

print("\n===== CONTATOS =====")

for contato in contatos:
    print(f"\nNome: {contato['nome']}")
    print(f"Endereço: {contato['endereco']}")
    print(f"DD: {contato['dd']}")
    print(f"Telefone: {contato['telefone']}")

with open("agenda.txt", "w", encoding="utf-8") as arquivo:
    for contato in contatos:
        arquivo.write(f"Nome: {contato['nome']}\n")
        arquivo.write(f"Endereço: {contato['endereco']}\n")
        arquivo.write(f"DD: {contato['dd']}\n")
        arquivo.write(f"Telefone: {contato['telefone']}\n\n")

pesquisa = input("\nDigite o nome para pesquisar: ")

encontrado = None

for contato in contatos:
    if contato["nome"].lower() == pesquisa.lower():
        encontrado = contato
        break

if encontrado:
    print(f"\nDD: {encontrado['dd']}")
    print(f"Telefone: {encontrado['telefone']}")
else:
    print("Contato não encontrado.")