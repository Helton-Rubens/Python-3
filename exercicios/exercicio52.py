numero = int(input('Digite um número: '))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[1;34m', end='')
        cont = cont + 1
    else:
        print('\033[1;33m', end='')
    print('{}\033[m'.format(c), end=' ')
if cont > 2:
    print('\nO número {} não é primo, pois foi divisível por {} numeros além do 1 e ele mesmo.'.format(numero, cont))
else:
    print('\nO número {} é primo, pois foi divisível por {} numeros: o número 1, e ele mesmo.'.format(numero, cont))