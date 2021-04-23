print('\033[37m===\033[m'*15)
print('{:>50}'.format('\033[1;33mCampeonato \033[1;32mBrasileiro \033[1;34mFutebol\033[m'))
print('\033[37m===\033[m'*15)
times = ('São Paulo', 'Internacional', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'Santos',
         'Corinthias', 'Athletico - PB', 'Ceará SC', 'Bragantino', 'Atlético - GO', 'SPORT Recife', 'Vasco da Gama',
         'Fortaleza', 'Bahia', 'Goiás', 'Coritiba', 'Botafogo')
for c in times[0:5]:
    if c == times[0]:
        print(f'Os cinco primeiro colocados são {c}', end=', ')
    else:
        if c == times[4]:
            print(f'{c}.')
            break
        print(f'{c}',end=', ')
print('\033[37m---\033[m'*15)
for c in times[-4:]:
    if c == times[-4]:
        print(f'Os últimos quatro colocados são {c}', end=', ')
    else:
        if c == times[-1]:
            print(f'{c}.')
            break
        print(f'{c}',end=', ')
print('\033[37m---\033[m' * 15)
cont = 0
for c in sorted(times):
    cont = cont + 1
    if cont == 1:
        print(f'A lista em ordem alfabetica é {c}', end=', ')
    else:
        if cont == 20:
            print(f'e {c}.')
            break
        print(f'{c}',end=', ')
print('\033[37m---\033[m' * 15)
print('O time da Chapecoense não se encontra nessa lista...')