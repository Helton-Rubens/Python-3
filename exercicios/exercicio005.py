numero = int(input('\033[37mDigite um número para descobrir seu sucessor e antecessor: \033[m'))
print('\033[34mO sucessor do número {} é:\033[m \033[32m{}\033[m'.format(numero, numero+1))
print('\033[34mO antecessor do número {} é: \033[32m{}\033[m'.format(numero, numero-1))