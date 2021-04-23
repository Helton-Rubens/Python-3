soma = 0
conta = 0
for c in range (1, 7):
    numero = int(input('Digite o {} valor: '.format(c)))
    if numero%2 == 0:
        conta = conta + 1
        soma = soma + numero
print('''A soma entre todos algarismos pares escritos é igual a {}.
Você informou {} algarismos pares!'''.format(soma, conta))