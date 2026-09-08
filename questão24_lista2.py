convidados = ["Ana", "João", "Maria", "Pedro", "Lucas"]

# Convites iniciais
for pessoa in convidados:
    print(f"{pessoa}, você está convidado(a) para o jantar!")

# Um convidado não poderá ir
print("\nMaria não poderá comparecer.")
indice = convidados.index("Maria")
convidados[indice] = "Carla"

print("\nNovos convites:")
for pessoa in convidados:
    print(f"{pessoa}, você está convidado(a) para o jantar!")

# Adicionando três pessoas
convidados.insert(0, "Paulo")
convidados.insert(len(convidados) // 2, "Julia")
convidados.append("Rafael")

print("\nLista com mais convidados:")
print(convidados)

# Removendo até restarem duas pessoas
print("\nA mesa não chegará a tempo. Apenas duas pessoas poderão participar.")

while len(convidados) > 2:
    removido = convidados.pop()
    print(f"{removido}, infelizmente você não poderá participar.")

# Confirmando os dois convidados restantes
print("\nConvidados restantes:")
for pessoa in convidados:
    print(f"{pessoa}, seu convite está confirmado!")

# Esvaziando a lista
convidados.pop()
convidados.pop()

print("\nLista final:", convidados)