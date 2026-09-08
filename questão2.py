tempo_horas = float(input("Digite o tempo de deslocamento em horas : "))
velocidade = 30 
tempo_segundos = tempo_horas *3600
distancia_km = velocidade * tempo_segundos
distancia_metros = distancia_km * 1000
print("Distância percorrida : ", distancia_metros, "metros")