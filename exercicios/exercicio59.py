from time import sleep
valor1 = int(input('\033[1;32mDigite o primeiro valor:\033[m '))
valor2 = int(input('\033[1;32mDigite o segundo valor:\033[m '))
sleep(2)
numeromaior = valor1
dec = 0
la = 0
while dec != 5:
    print('''\033[1;36mQual das opções você deseja?\033[m
    \033[1;32m[1]\033[m \033[1;34mSomar\033[m
    \033[1;32m[2]\033[m \033[1;34mMultiplicar\033[m
    \033[1;32m[3]\033[m \033[1;34mVerificar qual é o Maior\033[m
    \033[1;32m[4]\033[m \033[1;34mNovos números\033[m
    \033[1;32m[5]\033[m \033[1;31mSair do Programa\033[m''')
    dec = int(input('\n\033[36mDigite sua escolha:\033[m '))
    if dec == 1:
        print('Você escolheu a soma dos algarismos {} e {}.'
              ' \n{} + {} é igual a {}.'.format(valor1, valor2, valor1, valor2, valor1 + valor2))
    elif dec == 2:
        print('Você escolheu a multiplicação dos algarismos {} e {}.'
              ' \n{} X {} é igual a {}.'.format(valor1, valor2, valor1, valor2, valor1 * valor2))
    elif dec == 3:
        if valor2 > numeromaior:
            numeromaior = valor2
            print('O maior numero entre {} e {} é {}.'.format(valor1, valor2, numeromaior))
        elif valor1 > numeromaior:
            numeromaior = valor1
            print('O maior numero entre {} e {} é {}.'.format(valor1, valor2, numeromaior))
        elif valor1 == valor2:
            print('\033[35mAmbos os valores são iguais. Não há maior e nem menor.\033[m')
    elif dec == 4:
        valor1 = int(input('\033[1;30mDigite o primeiro valor:\033[m '))
        valor2 = int(input('\033[1;30mDigite o segundo valor:\033[m '))
    elif dec == 5:
        print('\033[4;34mFinalizando...')
        sleep(2)
    else:
        print('''\033[1;31mAlerta de Erro:
Você não escolheu nenhuma opção.\033[m''')
    print('\033[1;36m=+\033[m'*10)
print('\033[4;35mPrograma encerrado.\033[m')
