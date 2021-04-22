pma = 0
pme = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: Kg'.format(c)))
    if c == 1:
        pma = peso
        pme = peso
    else:
        if peso>pma:
            pma = peso
        if peso<pme:
            pme = peso
print('O maior peso até agora foi {}Kg'.format((pma)))
print('O menor peso até agora foi {}Kg'.format(pme))