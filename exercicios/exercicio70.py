c = count = total = barato = 0
dec = produtobarato = produto = ''
print('{:-^40}'.format('\033[1;4;32;40mLoja Santana\033[m'))
while dec != 'N':
    c = c + 1
    print('\033[36m===\033[m'*5)
    produto = str(input('\033[1;33mNome do produto que você deseja comprar: ').strip().capitalize())
    valor = float(input('\033[1;33mDigite o valor do produto: \033[1;32mR$\033[m'))
    if c == 1:
        barato = valor
    else:
        if valor < barato:
            barato = valor
            produtobarato = produto
    if valor >= 1000.00:
        count = count + 1
    total = total + valor
    dec = str(input('Quer continuar[S/N]? ').strip().upper())
    while dec != 'S' and dec != 'N':
        print("\033[1;31;40mINVÁLIDO\033[m\n\033[1;31;40mDigite uma das duas opções!\033[m")
        dec = str(input('Quer continuar[S/N]? ').strip().upper())
print('{:-^40}'.format('\033[1;4;32;40mPROGRAMA FINALIZADO\033[m'))
print('\033[1;32mR${:.2f}\033[1;36m no total.'.format(total))
print('Foram {:.2f} produtos com mais de \033[1;32mR$1000.00\033[m\033[1;36m.'.format(count))
print('O nome do produto mais barato é {} e custa \033[1;32mR${:.2f}\033[1;36m!'.format(produtobarato, barato))
