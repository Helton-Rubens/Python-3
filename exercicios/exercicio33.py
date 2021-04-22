n1 = int(input('Digite o primeiro valor: ').strip())
n2 = int(input('Digite o segundo valor: ').strip())
n3 = int(input('Digite o terceiro valor: ').strip())
numeros = [n1, n2, n3]
print('O menor valor digitado foi {}.'.format(min(numeros)))
print('e o maior número digitado foi {}.'.format(max(numeros)))