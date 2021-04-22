casa = float(input('Digite o valor da casa: \033[1;32mR$\033[m'))
salario = float(input('Digite o salário do comprador: \033[1;32mR$\033[m'))
anos = float(input('Quantos anos de financiamento? '))
parcela = (casa) / (anos*12)
print( 'O valor da parcela vai ser de \033[1;32m{:.2f} reais\033[m por mês durante \033[1;32m{:.0f}\033[m anos.'.format(parcela, anos))
if parcela > (((salario)*30)//100):
    print('Você não pode financiar essa casa.')
else:
    print('Você pode financiar essa casa.')
    decisao = str(input('Deseja fechar o negócio? ')).strip()
    if 'Sim' or 'sim' or 's' or 'ss':
        print('Então entre em contato com o vendedor dessa casa.')
    elif 'Não' or 'não' or 'n' or 'nn':
        print('Okay.')