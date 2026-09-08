import math
print("1 - Calcular a hipotenusa")
print("2 - Calcular um cateto")
opcao = int(input("Escolha uma opção : "))
if opcao == 1:
    cateto1 = float(input("Digite o primeiro cateto : "))
    cateto2 = float(input("Digite o segundo cateto"))
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2 )
    print("Hipotenusa : ",hipotenusa)
elif opcao == 2 :
    hipotenusa = float(input("Digite a hipotenusa : "))
    cateto = float(input("Digite o outro cateto : "))
    outro_cateto = math.sqrt(hipotenusa ** 2 - cateto ** 2)
    print("Cateto : " , outro_cateto)
else:
    print("Opção invalida")