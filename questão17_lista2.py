agenda = {}

for i in range(3):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")

    agenda[nome] = telefone

nome_procurado = input("Digite o nome que deseja procurar: ")

if nome_procurado in agenda:
    print("Telefone:", agenda[nome_procurado])
else:
    print("Contato não encontrado.")