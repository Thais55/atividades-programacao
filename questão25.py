horas = int(input("Digite a quantidade de horas de estudo : "))
if horas < 10 :
    print("quantidade de horas muito baixa ")
elif horas > 40 :
    print("Quantidade muito alta ")
else:
    print(f"Plano configurado com {horas} horas . ")
    