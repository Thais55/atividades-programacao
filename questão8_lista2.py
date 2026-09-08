notas = [7.5, 6.0, 8.2, 9.0, 4.5, 7.0, 10.0, 5.8, 6.5, 8.0]

aprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1

print("Quantidade de estudantes aprovados:", aprovados)