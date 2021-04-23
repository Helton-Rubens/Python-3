numero = int(input('Digite um número inteiro: '))
dec = str(input('Deseja continuar [S/N]? ').strip().lower())
while dec != 's' and dec != 'n':
    print('\033[1;31mDígito inválido. Digite "s" ou "n".\033[m')
    dec = str(input('Deseja continuar [S/N]? '))
soma = 0 + numero
numeromenor = numero
numeromaior = numero
cont = 1
while dec != 'n':
    cont = cont + 1
    numero = int(input('Digite um número inteiro: '))
    soma = soma + numero
    if cont >= 2:
        if numero > numeromaior:
            numeromaior = numero
        if numero < numeromenor:
            numeromenor = numero
    dec = str(input('Deseja continuar [S/N]? ').strip().lower())
    while dec != 's' and dec != 'n':
        print('\033[1;31mDígito inválido. Digite "s" ou "n".\033[m')
        dec = str(input('Deseja continuar [S/N]? '))
print(f'A soma dos números é {soma}.')
print('''A média dos números foi {:.2f}.
O maior valor digitado foi {}, e o menor foi {}.'''.format(soma / cont, numeromaior, numeromenor))
