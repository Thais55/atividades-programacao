aluno_a = set()
aluno_b = set()

print("Digite as linguagens do Aluno A.")
print("Digite 'fim' para encerrar.")

while True:
    linguagem = input("Linguagem: ")

    if linguagem.lower() == "fim":
        break

    aluno_a.add(linguagem)

print("\nDigite as linguagens do Aluno B.")
print("Digite 'fim' para encerrar.")

while True:
    linguagem = input("Linguagem: ")

    if linguagem.lower() == "fim":
        break

    aluno_b.add(linguagem)

print("\nLinguagens do Aluno A:")
print(aluno_a)

print("\nLinguagens do Aluno B:")
print(aluno_b)

print("\nConhecidas por ambos:")
print(aluno_a & aluno_b)

print("\nConhecidas por pelo menos um:")
print(aluno_a | aluno_b)

print("\nConhecidas apenas pelo Aluno A:")
print(aluno_a - aluno_b)

print("\nConhecidas apenas pelo Aluno B:")
print(aluno_b - aluno_a)

print("\nQuantidade de linguagens diferentes:")
print(len(aluno_a | aluno_b))