from time import sleep
from random import randint
from emoji import emojize
sleep(2)
print('\033[1;34m-=-\033[m'*10)
print('\033[0;33mJOGO DA ADIVINHAÇÃO\033[m')
print('\033[1;34m-=-\033[m'''*10)
sleep(3)
print('''\033[30mVamos tentar descobrir 
se você consegue acertar
o número que eu pensei!
Se você acertar, você ganhou o jogo\033[m.
\033[4;31mCaso contrário, você perde!\033[m\n''')
sleep(2)
print('\033[30mDeixe me pensar...', end= ' ')
sleep(1)
print('\033[30mProntinho!\n')
sleep(1)
numero = int(input('\033[30mEm qual número (de 1 a 2) eu pensei? ')) #jogador tenta adivinhar
comput = randint(1, 2) #faz o computador "pensar"
sleep(1)
print('\033[30mVerificando...')
sleep(3)
if numero == comput:
    print(emojize('\033[1;30mPARABÉNS, VOCÊ GANHOU! :blush:', use_aliases=True))
    print(emojize('\033[30mEu pensei no número {}! :alien:'.format(comput), use_aliases=True))
else:
    print(emojize('\033[mQue pena, não foi dessa vez... :sunglasses:', use_aliases=True))
    print(emojize('Eu pensei no número {}! :laughing:'.format(comput), use_aliases=True))