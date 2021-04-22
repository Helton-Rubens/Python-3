nu1 = int(input('Digite o primeiro valor: '))
nu2 =  int(input('Digite o segundo valor: '))
if nu1 > nu2:
    print('\033[1;32mO primeiro valor ({}) é maior que o segundo valor ({}).'.format(nu1, nu2))
elif nu2 > nu1:
    print('\033[1;32mO segundo valor ({}) é maior que o primeiro valor ({}).\033[m'. format(nu2, nu1))
else:
    print('\033[1;31mNão existe valor maior ou menor, ambos são iguais.')