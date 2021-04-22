from datetime import date
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano nasceu a {}º pessoa? '.format(c)))
    dd = date.today().year - ano
    if dd >= 21:
        cont1 += 1
    else:
        cont2 += 1
if cont1 == 1:
    print('\033[1;35m{} pessoa atingiu a maioridade penal.\033[m'.format(cont1))
else:
    print('\033[1;35m{} pessoas atingiram a maioridade penal.\033[m'.format(cont1))
if cont2 == 1:
    print('\033[1;35m{} pessoa não atingiu a maioridade penal.\033[m'.format(cont2))
else:
    print('\033[1;35m{} pessoas não atingiram a maioridade penal.\033[m'.format(cont2))