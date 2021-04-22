pessoas = []
rar = []
lev = pes = 0
while True:
    rar.append(str(input('Nome: ')))
    rar.append(float(input("peso: Kg's ")))
    if len(pessoas) == 0:
        lev = pes = rar[1]
    else:
        if rar[1] > pes:
            pes = rar[1]
        elif rar[1] < lev:
            lev = rar[1]
    pessoas.append(rar[:])
    rar.clear()
    dec = str(input('Quer continuar[S/N]? ')).strip().lower()
    if dec[0] in 'NnSs':
        if dec[0] in 'Nn':
            break
    else:
        while dec[0] not in 'NnSs':
            print('Digito inválido. Digite apenas "Sim" ou "não"')
            dec = str(input('Quer continuar[S/N]? '))
print('=-'*30)
print(f"""Ao todo foram cadastradas {len(pessoas)} pessoas""")
print(f"O maior peso foi de {lev} Kg's. Foi o peso de: ", end='')
for i in pessoas:
    if i[1] == lev:
        print(f'{i[0]}', end=' ')
print(f'\nO menor peso foi {pes}. Foi o peso de: ', end='')
for i in pessoas:
    if i[1] == pes:
        print(f'{i[0]}', end=' ')
