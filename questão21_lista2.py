programacao = float(input("Horas de estudo de Programação: "))
banco_dados = float(input("Horas de estudo de Banco de Dados: "))
redes = float(input("Horas de estudo de Redes de Computadores: "))

if programacao < 0 or banco_dados < 0 or redes < 0:
    print("Os valores são inválidos.")
else:
    total = programacao + banco_dados + redes
    print("Carga horária total planejada:", total, "horas")