from time import sleep
from datetime import date
idade = int(input('Em qual ano você nasceu? '))
anoatual = date.today().year
if anoatual - idade < 18:
    print('Você ainda irá se alistar no exército.')
    print('Falta \033[1;32m{}\033[m anos para você se alistar.'.format(18 - (anoatual - idade)))
elif anoatual - idade > 18:
    print('Você já passou do tempo de se alistar no exército.')
    sleep(2)
    print('\033[1;31mE já pode ser preso. Huehuehueheuhue!\033[m')
    print('você deveria ter se alistado há \033[1;32m{}\033[m anos atrás.'.format((anoatual - idade) - 18))
else:
    print('Você está no tempo de se alistar no exército.')
    sleep(2)
    print('\033[1;31mE já pode ser preso. Huehuehueheuhue!\033[m')
