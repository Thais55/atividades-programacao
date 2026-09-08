arquivo_nome = input("Digite o nome do arquivo: ")

try:
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read().lower()

    contagem = {}

    for caractere in texto:
        if caractere.isalpha():
            if caractere in contagem:
                contagem[caractere] += 1
            else:
                contagem[caractere] = 1

    for letra in sorted(contagem):
        print(letra, ":", contagem[letra])

except FileNotFoundError:
    print("Arquivo não encontrado.")