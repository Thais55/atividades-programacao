usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

usuario_correto = "Fesor"
senha_correta = "D0m1No"

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso autorizado.")
else:
    print("Usuário ou senha inválidos.")  