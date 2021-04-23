numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
dig = int(input('Digite um número entre 0 e 20: '))
while dig < 0 or dig > 20:
    dig = int(input('\033[1;4;31mDigito inválido.\033[m\nDigite um número entre 0 e 20: '))
print(f'Você digitou o número {numero[dig]}.')
dec = str(input('Você deseja continuar? ').strip().upper())
while dec[0] not in 'Nn':
    dig = int(input('Digite um número entre 0 e 20: '))
    while dig < 0 or dig > 20:
        dig = int(input('\033[1;4;31mDigito inválido.\033[m\nDigite um número entre 0 e 20: '))
    print(f'Você digitou o número {numero[dig]}.')
    dec = str(input('Você deseja continuar? ').strip().upper())
print('Fim.')
