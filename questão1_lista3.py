for ciclo in range(10):
    if ciclo == 0:
        anterior = 0
    else:
        anterior = ciclo - 1

    soma = ciclo + anterior

    print("Ciclo atual:", ciclo)
    print("Ciclo anterior:", anterior)
    print("Soma:", soma)
    print()