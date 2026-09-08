def calcular_comissao(valor_servico):
    """
    Calcula e exibe a comissão de 10% sobre um serviço.

    Parâmetro:
    valor_servico: valor do serviço realizado.

    Retorno:
    Exibe o valor da comissão.
    """

    comissao = valor_servico * 0.10

    print("Comissão do técnico: R$", comissao)


valor = float(input("Digite o valor do serviço: "))

calcular_comissao(valor)