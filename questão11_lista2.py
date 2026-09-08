estudante = {
    "nome": "Thais",
    "matricula": "20250001",
    "idade": 20,
    "curso": "Licenciatura em Ciência da Computação",
    "semestre": 3,
}

estudante["semestre"] = 3
estudante["email"] = "thais@ifbaiano.edu.br"

del estudante["idade"]

print(estudante)