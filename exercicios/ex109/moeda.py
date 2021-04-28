def aumentar(valor=0, taxa=0, formato=False):
    """
    Função que calcula e aumenta o valor do produto
    :param formato: formata o valor do resultado
    :param valor: preço do produto
    :param taxa: (Opcional) Taxa do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor + (valor * taxa / 100)
    if not formato:
        return r
    else:
        return moeda(r)


def diminuir(valor=0, taxa=0, formato=False):
    """
    Função que calcula e diminui o valor do produto
    :param formato: formata o valor do resultado
    :param valor: preço do produto
    :param taxa: (Opcional) Taxa do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor - (valor * taxa / 100)
    if not formato:
        return r
    else:
        return moeda(r)


def dobro(valor=0, formato=False):
    """
    Função que calcula e dobra o valor do produto
    :param formato: Formatado para
    :param valor: preço do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor * 2
    if not formato:
        return r
    else:
        return moeda(r)


def metade(valor=0, formato=False):
    """
    Função que calcula e divide pela metade o valor do produto
    :param formato: Formata o valor
    :param valor: preço do produto
    :return: retorna o valor do cálculo para a variável
    """
    r = valor / 2
    if not formato:
        return r
    else:
        return moeda(r)

# A função "moeda" corresponde ao desafio do exercicio 109
def moeda(valor=0, simbolmoeda='R$'):
    """

    :param valor: valor
    :param simbolmoeda: A moeda de pagamento. Ex: R$, U$, €...
    :return: retorna a formatação
    """
    if simbolmoeda == 'R$':
        return f'{simbolmoeda}{valor:.2f}'.replace('.', ',')
    else:
        return f'{simbolmoeda}{valor:.2f}'

