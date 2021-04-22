valor = int(input('\033[1;30mDigite um valor:\033[m '))
print ('\n\033[32m>>>\033[m \033[31mO dobro do número é:\033[m \033[32m{}\033[m '
       '\n \033[32m>>>\033[m \033[31mO triplo é:\033[31m \033[32m{}\033[m '
       '\n \033[32m>>>\033[m \033[31mE a raiz quadrada do número é:\033[m'
       ' \033[31m{:.3f}\033[m\033[32m.'.format ( valor*2, valor*3, valor**(1/2)))