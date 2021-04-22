from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando numeros....', end=' ')
    print(f'Pronto:')
    for c in range(0, 5):
        num = randint(1, 100)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.5)
    print()


def somapar(a):
    soma = 0
    for element in a:
        if element % 2 == 0:
            soma += element
    print(f"A soma dos números pares é igual a {soma}")


numeros = list()
sorteia(numeros)
somapar(numeros)
