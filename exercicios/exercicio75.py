valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')),
           int(input('Digite outro valor: ')))
nine = 0
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)}')
else:
    print('O valor 9 não apareceu nenhuma vez.')
if 3 in valores:
    print(f'O valor 3 foi encontrado na {valores.index(3)+1}ª posição!')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
par = 0
for cont in valores:
    if cont % 2 == 0:
        par = par + 1
        if par == 1:
            print(f'Os valores pares digitados foram: {cont} ', end='')
        else:
            print(f'{cont} ', end='')
