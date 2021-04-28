def leiaValor(a):
    """
    Essa função lê um valor e faz uma validação.
    :param a: Uma mensagem do tipo string que será usada como um input,
    que será lido pelo usuário.
    :return: No final do programa, se o valor digitado pelo usuário for aceito,
     retorna  o valor para a variável.
    """
    valida = False
    while not valida:
        entrada = str(input(a).strip().replace(',', '.'))
        if entrada.isalpha() or entrada.strip() == "":
            print(f'Erro! "{entrada}" não é um valor.')
        else:
            valida = True
            return float(entrada)

