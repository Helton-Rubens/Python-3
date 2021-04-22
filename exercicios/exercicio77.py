from time import sleep
sleep(2)
print('\033[37m=\033[m'*50)
print(f'\n{"Verificador de vogais":^50}\n')
print('\033[37m=\033[m'*50)
sleep(2)
vog = (str(input('\nDigite uma palavra: ')).strip().lower(), str(input('Digite outra palavra: ').strip().lower()),
       str(input('Digite outra palavra: ').strip().lower()),  str(input('Digite outra palavra: ').strip().lower()),
       str(input('Digite outra palavra: ').strip().lower()),  str(input('Digite outra palavra: ').strip().lower()),
       str(input('Digite outra palavra: ').strip().lower()),  str(input('Digite outra palavra: ').strip().lower()),
       str(input('Digite outra palavra: ').strip().lower()),  str(input('Digite outra palavra: ').strip().lower()),
       str(input('Digite outra palavra: ').strip().lower()),  str(input('Digite outra palavra: ').strip().lower()))
print('\033[1;37m=\033[m'*50, end='\n')
for vogal in vog:
    print(f'\nNa palavra "\033[1;34m{vogal}\033[m" há as vogais: ', end='')
    for i in vogal:
        if i in 'AaEeIiOoUu':
            print(f'\033[31m{i}\033[m', end=' ')
