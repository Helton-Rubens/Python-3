numero = int(input('Digite um número inteiro para fazer sua tabuada de múltiplicação: '))
for c in range(0, 11):
    print('{} * {} = {}'.format(numero, c, numero*c))