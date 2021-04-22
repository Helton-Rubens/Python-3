print('\033[37m=\033[m'*30)
print('{:^40}'.format('\033[1;4;35mBanco HR\033[m'))
print('\033[37m=\033[m'*30)
valor = int(input('\033[1;33mQual valor você deseja sacar?\033[m \033[1;32mR$\033[m'))
tot = valor
cedula = 200
totcedu = 0
while True:
    if totcedu > 0:
        print(f'{totcedu} cedulas de R${cedula}!')
    if tot >= cedula:
        tot = tot - cedula
        totcedu += 1
    else:
        if tot == 200:
            cedula = 100
        elif tot == 100:
            cedula = 50
        elif tot == 50:
            cedula = 20
        elif tot == 20:
            cedula = 10
        elif tot == 10:
            cedula = 5
        elif tot == 5:
            cedula = 2
        elif tot == 2:
            cedula = 1
        totcedu = 0
        if tot == 0:
            break
print('Volte sempre!')
