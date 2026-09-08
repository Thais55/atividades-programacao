vogais = 0
consoantes = 0

for i in range(10):
    letra = input(f"Digite a letra {i + 1}: ").lower()

    if letra in "aeiou":
        vogais += 1
    else:
        consoantes += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)