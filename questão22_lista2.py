def cadastrar_estudante():
    """
    Solicita os dados de um estudante e confirma o cadastro.

    A função solicita o nome, a matrícula e o curso do estudante.
    Não recebe parâmetros e não retorna valores.
    """

    nome = input("Digite o nome do estudante: ")
    matricula = input("Digite a matrícula: ")
    curso = input("Digite o curso: ")

    print("\nCadastro realizado com sucesso!")
    print("Nome:", nome)
    print("Matrícula:", matricula)
    print("Curso:", curso)


cadastrar_estudante()