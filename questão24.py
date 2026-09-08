valores_validos = []
for i in range(5):
    valor = float(input(f"Digite a medição {i+1}: "))
    if valor > 0 and valor < 1000 : 
        valores_validos.append(valor)
        if len(valores_validos) > 0 :
            media = sum(valores_validos) / len(valores_validos)
            print("Media das medições válidas : ", media)
        else:
            print("Nenhuma medição válida foi informada ")