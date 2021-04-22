from time import sleep
from datetime import date
print("\033[4;36m+=+\033[m"*10)
print('\033[1;35midentificação de categoria para atletas!\033[m')
print("\033[4;36m+=+\033[m"*10)
sleep(1)
idade = int(input('Digite o ano de nascimento do atleta: '))
calculo = date.today().year - idade
print('Quem nasceu no ano de {} tem {} anos,'.format(idade, calculo))
sleep(1)
print('portanto...')
sleep(1)
if calculo <= 9:
    print('O atleta pertence a categoria \033[1;35mmirim\033[m.')
elif calculo <= 14:
    print('O atleta pertence a categoria \033[1;35minfantil\033[m.')
elif calculo <= 19:
    print('O atleta pertence a categoria \033[1;35mjunior\033[m.')
elif calculo == 20:
    print('O atleta pertence a categoria \033[1;35msênior\033[m.')
else:
    print('O atleta pertence a categoria \033[1;4;36mMASTER\033[m.')