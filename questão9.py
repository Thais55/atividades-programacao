L1 = float(input("Digite o primeiro lado: "))
L2 = float(input("Digite o segundo lado: "))
L3 = float(input("Digite o terceiro lado: "))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print("Os valores formam um triângulo.")

    if L1 == L2 == L3:
        print("O triângulo é equilátero.")
    elif L1 != L2 and L1 != L3 and L2 != L3:
        print("O triângulo é escaleno.")

else:
    print("Os valores não formam um triângulo.")