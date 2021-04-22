from time import sleep
from random import randint
print('+='*27)
print('{:^50}'.format('jogo da mega sena'.title()))
print('+='*27)
dec = int(input('Quantos jogos você quer que eu sorteie? '))
sorteio = []
temp = []
print()
for c in range(1, dec+1):
    for i in range(1, 7):
        n = randint(1, 61)
        if n not in temp:
            temp.append(n)
        else:
            while n in temp:
                n = randint(1, 61)
            temp.append(n)
    temp.sort()
    sorteio.append(temp[:])
    temp.clear()
    print(f'Jogo {c}: {sorteio[c-1]}')
    sleep(1)
print(f'{" boa sorte! ":-^40}')
