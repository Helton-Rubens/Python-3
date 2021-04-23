from time import sleep
from random import randint
computador = randint(1, 10)
sleep(2)
print('''\033[1;31mComputador:\033[m \033[1;33mOlá jogador, que tal jogarmos um jogo?
Você consegue adivinhar em qual número eu estou pensando?\033[m''')
sleep(3)
print('\033[1;34m-=-\033[m'*10)
print('\033[1;35mJOGO DA ADIVINHAÇÃO\033[m')
print('\033[1;34m-=-\033[m'''*10)
sleep(2)
print('''\033[1;31mComputador:\033[m \033[1;33m Vamos tentar descobrir se você consegue acertar
o número que eu pensei! Se você acertar, você ganhou o jogo.\033[m''')
sleep(3)
print('''\033[1;31mComputador:\033[m \033[1;33m Se você errar, perguntarei novamente até você acertar.
No final mostrarei a quantidade de tentativas que você fez até acertar.\033[m''')
sleep(4)
print('\033[1;31mComputador:\033[m \033[1;33mDeixei me pensar...\033[m')
sleep(2)
print('\033[1;31mComputador:\033[m \033[1;33mPronto...\033[m')
sleep(1)
print('\033[1;31mComputador:\033[m \033[1;33mQual número de 1 a 10 eu estou pensando agora?\033[m')
sleep(3)
jogador = int(input('\033[1;37mJogador:\033[m '))
tentativa = 0
while jogador != computador:
    sleep(1)
    print('\033[1;32mVocê errou!\033[m')
    sleep(1)
    if jogador < computador:
        jogador = int(input('\033[36mMais... Tente novamente\033[m \n\033[1;37mJogador: \033'))
    elif jogador > computador:
        jogador = int(input('\033[36mMenos... Tente novamente\033[m \n\033[1;37mJogador: \033'))
    tentativa = tentativa + 1
print('\033[1;31mComputador:\033[m \033[1;33mParabéns,Você acertou e o total de tentativas foram {}.\033[m'.format(tentativa))