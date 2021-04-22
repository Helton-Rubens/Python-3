numeros = []
pomax = []
pomin = []
for contagem in range(0, 5):
    if contagem == 0:
        numeros.append(int(input('\033[37mDigite um numero:\033[m ')))
    else:
        numeros.append(int(input('\033[37mDigite outro numero:\033[m ')))
print(f'Você digitou os valores: \033[32m{numeros}\033[m')
for chave, item in enumerate(numeros):
    if max(numeros) == item:
        pomax.append(chave+1)
    if min(numeros) == item:
        pomin.append(chave+1)
print(f'O maior numero foi {max(numeros)} encontrado na posição: ', end='')
for item in pomax:
    if item == pomax[-1]:
        print(f'{item}!')
        break
    print(f'{item}', end='..')
if pomin == pomax:
    print(f'O menor numero também foi {min(numeros)} encontrado na posição: ', end='')
else:
    print(f'O menor numero foi {min(numeros)} encontrado na posição: ', end='')
for item in pomin:
    if item == pomin[-1]:
        print(f'{item}!')
        break
    print(item, end='..')
