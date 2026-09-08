idade = int(input("Digite a idade: "))

if idade < 0:
    print("Idade inválida.")

elif idade <= 12:
    print("Criança.")

elif idade <= 18:
    print("Adolescente.")

else:
    print("Adulto.")