numbers = []
while True:
    numbers.append(int(input('Digite um valor: ')))
    dec = str(input('Quer continuar[Sim/Não]? ')).strip().lower()
    if dec[0] in 'Nn':
        print('=+'*30)
        break
    while dec[0] not in 'SsNn':
        print('Digite uma das duas opções!')
        dec = str(input('Quer continuar[Sim/Não]? '))
        if dec[0] in 'Nn':
            break
numbers.sort(reverse=True)
print(f'Você digitou {len(numbers)} elementos!')
print(f'Os valores em ordem decrescente são {numbers}')
if 5 in numbers:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista...')
