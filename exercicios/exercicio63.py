numero = int(input('Digite o número de termos da sequência de Fibonacci: '))
print('~~'*10)
print('Sequência de Fibonacci')
print('~~'*10)
f1 = 0
f2 = 1
print('{}-{}'.format(f1, f2), end='-')
cont = 2
while cont != numero:
    f3 = f1 + f2
    print('{}'.format(f3), end='-')
    f1 = f2
    f2 = f3
    cont = cont + 1
print('Fim')