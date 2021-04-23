from time import sleep
from random import choice
comp = choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[1;34m+=\033[m'*20)
print('\033[1;32mThe Jokenpô Game\033[m')
print('\033[1;34m+=\033[m'*20)
print('\nVamos jogar?')
jogador = int(input('''Escolha Pedra
Papel
Tesoura
Opção: ''').strip().capitalize())
print('A escolha do computador foi: {}'.format(comp))
sleep(1)
print('\033[32mVerificando...\033[m')
sleep(1)
if jogador == comp:
    print('Empate! O computador também escolheu {}'.format(comp))
elif jogador != comp:
    if comp == 'Pedra' and jogador == 'Tesoura':
        print('\033[1;31mO computador venceu!\033[m')
    elif comp == 'Papel' and jogador == 'Pedra':
        print('\033[1;31mComputador venceu!\033[m')
    elif comp == 'Tesoura' and jogador == 'Papel':
        print('\033[1;31mO computador venceu!\033[m')
    elif comp == 'Tesoura' and jogador == 'Pedra':
        print('\033[1;35mParabéns. Você venceu!\033[m')
    elif comp == 'Pedra' and jogador == 'Papel':
        print('\033[1;35mParabéns. Você venceu!\033[m')
    elif comp == 'Papel' and jogador == 'Tesoura':
        print('\033[1;35mParabéns. Você venceu!\033[m')
    else:
        print('\033[1;31m Você não escolheu nenhuma das opções!\033[m')