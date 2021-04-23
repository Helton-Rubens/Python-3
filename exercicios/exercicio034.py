salario = float(input('\033[30mDigite o salário do funcionario: R$'))
if salario > 1250:
    print('\033[37mO salário é superior a \033[32mR$1250.00\033[m \033[37me receberá um aumento de 10%.')
    print('\033[37mGanhará \033[2;32m{:.2f}\033[m \033[37mreais a mais.'.format((salario*10)/100))
    print('\033[37mO salário será de \033[4;32mR${}!'.format(salario+(salario*10)/100))
else:
    print('\033[37mO salário é igual ou inferior a \033[32mR$1250.00\033[m \033[37me receberá um aumento de 15%.')
    print('\033[37mTerá \033[2;32m{:.2f}\033[m \033[37mreais a mais.'.format((salario*15)/100))
    print('\033[37mE o seu novo salário será de \033[4;32mR${:.2f}!'.format(salario+(salario*15)/100))