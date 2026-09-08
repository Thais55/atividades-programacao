import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não há raízes reais.")

elif delta == 0:
    x = -b / (2 * a)
    print("A única raiz real é:", x)

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print("Primeira raiz:", x1)
    print("Segunda raiz:", x2)