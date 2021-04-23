from random import randint
print('\033[1;4;33;40mPar ou Ímpar, The Game!\033[m')
count = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número de 1 a 10: '))
    while jogador > 10 or jogador < 0:
        print('\033[1;31mOpção Inválida. Digite o valor correto.\033[m')
        jogador = int(input('Digite um número de 1 a 10: '))
    dec = str(input('ímpar ou Par[I/P]? ').upper().strip())
    print('-'*30)
    while dec != 'P' and dec != 'I':
        print('\033[1;31mOpção Inválida. Digite o valor correto.\033[m')
        dec = str(input('ímpar ou Par[I/P]? ').upper().strip())
    print(f'Computador escolheu {computador}')
    result = computador + jogador
    if result % 2 == 0:
        print('{} + {} é igual {}, portanto é um número par'.format(jogador, computador, result))
        result = 'P'
        if dec == result:
            print('\033[1;35;40mVocê ganhou\033[m')
            print('~~' * 10)
            print('\033[1;32mVamos jogar mais uma vez...\033[m')
            print('~~' * 10)
            count = count + 1
        else:
            print('Você perdeu!')
            break
    else:
        print(f'{jogador} + {computador} é igual {result}, portanto é um número ímpar')
        result = 'I'
        if dec == result:
            print('\033[1;35;40mVocê ganhou\033[m')
            print('~~' * 10)
            print('\033[1;32mVamos jogar mais uma vez...\033[m')
            print('~~'*10)
            count = count + 1
        else:
            print('Você perdeu!')
            break
print('\033[1;31;40mGame over!\033[m\nVenceu {} vezes!'.format(count))
