lista = ('lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('----'*10)
print('{:^40}'.format('Listagem de Preços!'))
print('----'*10)
for item in lista:
    if type(item) == str:
        print('{:.<20}'.format(item), end='')
    if type(item) == float:
        print(f'\033[1;32mR${item:.2f}\033[m')
