nome = input("Digite o nome : ")
idade = int(input("Digite a idade : "))
acompanhado = input("Está acompanhado por um responsável ? (sim/não): ")
if idade >= 18:
    print(nome , "pode entrar ")
elif acompanhado.lower() == "sim":
    print(nome , "pode entrar acompanhado por um responsável ")
else:
    print(nome, " não pode entrar ")