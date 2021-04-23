from random import randint
tupla = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
count = 0
for numero in tupla:
    count = count + 1
    if count == 1:
        print(f'Os números sorteados foram: {numero}', end=' ')
    else:
        if numero == tupla[-1]:
            print(numero)
            break
        print(f'{numero}', end=' ')
print(f'O maior número foi: {max(tupla)}\nO menor valor foi: {min(tupla)}')
