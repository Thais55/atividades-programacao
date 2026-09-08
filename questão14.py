preco = float(input("Digite o preço unitário: R$ "))
quantidade = int(input("Digite a quantidade: "))
desconto = float(input("Digite o desconto: R$ "))

total = (preco * quantidade) - desconto

print(f"Valor final da compra: R$ {total:.2f}")