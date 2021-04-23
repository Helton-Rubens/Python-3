from random import randint
from time import sleep
from operator import itemgetter
print('JOGO DE DADOS:\n')
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
rank = list(sorted(jogo.items(), key=itemgetter(1), reverse=True))
for c, i in jogo.items():
    sleep(1)
    print(f'-> O {c} recebeu o valor {i} ao jogar o dado')
print()
print('-='*30)
print('RANKING:\n')
for k, j in enumerate(rank):
    sleep(1)
    print(f'   --> Em {k+1}º lugar: {j[0]} com valor {j[1]}')
