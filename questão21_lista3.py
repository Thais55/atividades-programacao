gabarito = []

print("Digite o gabarito das 25 questões:")

for i in range(25):
    while True:
        resposta = input(f"Gabarito da questão {i + 1}: ").upper()

        if resposta in ["A", "B", "C", "D", "E"]:
            gabarito.append(resposta)
            break
        else:
            print("Resposta inválida! Digite A, B, C, D ou E.")


acertos = 0
erros = 0

print("\nDigite as respostas do estudante:")

for i in range(25):
    while True:
        resposta = input(f"Resposta da questão {i + 1}: ").upper()

        if resposta in ["A", "B", "C", "D", "E"]:
            break
        else:
            print("Resposta inválida! Digite A, B, C, D ou E.")

    if resposta == gabarito[i]:
        acertos += 1
    else:
        erros += 1


percentual = (acertos / 25) * 100

print("\n===== RESULTADO =====")
print("Quantidade de acertos:", acertos)
print("Quantidade de erros:", erros)
print(f"Percentual de aproveitamento: {percentual:.2f}%")
