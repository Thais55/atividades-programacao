def filtrar_tempos(tempos, limite_inferior, limite_superior):
    """
    Recebe uma lista de tempos e retorna os valores
    dentro do intervalo informado.
    """

    sublista = []

    for tempo in tempos:
        if limite_inferior <= tempo <= limite_superior:
            sublista.append(tempo)

    print("Tempos encontrados:", sublista)


tempos = [15, 22, 35, 48, 60, 75, 90, 120]

filtrar_tempos(tempos, 35, 75)