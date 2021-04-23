num = int(input('Digite um número inteiro: '))
print('+='*10)
print('''\nEscolha uma das bases para conversão:

[\033[1;34m1\033[m] Converter para \033[4;35mBINÁRIO\033[m
[\033[1;34m2\033[m] Converter para \033[4;35mOCTAL\033[m
[\033[1;34m3\033[m] Converter para \033[4;35mHEXADECIMAL\033[m\n''')
opc = int(input('Sua opção: '))
if opc == 1:
    print('O número {} convertido para \033[1;34mbinário\033[m é: {}.'.format(num, bin(num) [2:]))
elif opc == 2:
    print('O número {} convertido para \033[1;34moctal\033[m é: {}.'.format(num, oct(num) [2:]))
elif opc == 3:
    print('O número {} convertido para \033[1;34mhexadecimal\033[m é: {}'.format(num, hex(num) [2:]))
else:
    print('\033[1;31mAlerta!\033[m \n\033[1;31mOpção inválida. \nTente novamente.\033[m')