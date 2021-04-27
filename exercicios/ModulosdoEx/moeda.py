def aumentar(valor=0, taxa=1, moeda = 'R$'):
    """
    Função que calcula e aumenta o valor do produto
    :param valor: preço do produto
    :param taxa: (Opcional) Taxa do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor + (valor * taxa / 100)
    return r


def diminuir(valor=0, taxa=1, moeda = 'R$'):
    """
    Função que calcula e diminui o valor do produto
    :param valor: preço do produto
    :param taxa: (Opcional) Taxa do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor - (valor * taxa / 100)
    return r


def dobro(valor=0, moeda = 'R$'):
    """
    Função que calcula e dobra o valor do produto
    :param valor: preço do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor * 2
    return r


def metade(valor=0, moeda = 'R$'):
    """
    Função que calcula e divide pela metade o valor do produto
    :param valor: preço do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor / 2
    return r


#A função "moeda" corresponde ao desafio do exercicio 109
def moeda(valor=0, moeda='R$'):
    """
    Função que retorna o valor da moeda formatado
    :param valor: valor
    :param moeda: A moeda de pagamento. Ex: R$, U$, €...
    :return: retorna a formatação
    """
    if moeda == 'R$':
        return f'{moeda}{valor}'.replace('.', ',')
    else:
        return f'{moeda}{valor}'
