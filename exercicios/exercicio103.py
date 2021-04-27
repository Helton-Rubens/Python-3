from time import sleep


def fatorial(n, show=False):
    """
    Função que calcula o fatorial de um número
    :param n: Um número inteiro a ser calculado
    :param show: (opcional) Retorna o cálculo
    :return: O valor fatorial de um número n
    """
    f = 1
    print('--'*10)
    for c in range(n, 0, -1):
        f *= c
    if show:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            if c == 1:
                print(f'{c} = ', end='')
                return f
            print(f'{c} x', end=' ')
    return f


num = int(input('Qual número você deseja calcular o fatorial? '))
dec = str(input('Você deseja que o calculo seja mostrado também [S/N]?').strip().upper()[0])
print('Mostrando o resultado', end='')
for c in range(1, 4):
    sleep(0.5)
    print('.', end='')
print()
if dec[0] in 'Nn':
    print(fatorial(num))
elif dec[0] in 'Ss':
    print(fatorial(num, show=True))
