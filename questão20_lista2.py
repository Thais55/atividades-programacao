def exibir_nome_do_programa():
    """Exibe o nome do programa."""
    print("===== SISTEMA DE GERENCIAMENTO ACADÊMICO =====")


def exibir_menu():
    """Exibe as opções disponíveis no sistema."""
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Alterar situação")
    print("0 - Sair")


def cadastrar_estudante():
    """Exibe a mensagem da opção cadastrar estudante."""
    print("Opção Cadastrar estudante selecionada.")


def listar_estudantes():
    """Exibe a mensagem da opção listar estudantes."""
    print("Opção Listar estudantes selecionada.")


def alterar_situacao_estudante():
    """Exibe a mensagem da opção alterar situação."""
    print("Opção Alterar situação selecionada.")


def opcao_invalida():
    """Informa que a opção escolhida não existe."""
    print("Opção inválida.")


def finalizar_programa():
    """Informa que o sistema está sendo encerrado."""
    print("Sistema sendo encerrado.")


def main():
    """Coordena a execução do Sistema Acadêmico."""

    exibir_nome_do_programa()
    exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_estudante()
    elif opcao == 2:
        listar_estudantes()
    elif opcao == 3:
        alterar_situacao_estudante()
    elif opcao == 0:
        finalizar_programa()
    else:
        opcao_invalida()


main()