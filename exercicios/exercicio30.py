from time import sleep
numero = int(input('Digite um número: '))
print('Analisando...')
sleep(2)
if numero%2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))