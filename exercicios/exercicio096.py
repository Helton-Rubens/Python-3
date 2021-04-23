jogador = dict()
jogadores = list()
dec = ' '
while dec not in 'Nn':
    jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().title()
    i = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for i in range(1, i+1):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez no {i}º jogo? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    dec = str(input('Quer continuar?[S/N] '))[0]
    while dec[0] not in 'SsNn':
        print('Erro! Digite apenas "Sim" ou "Não"')
        dec = str(input('Quer continuar?[S/N] '))[0]
print('-='*40)
print(f'{"Cod":>3} {"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-='*40)
for n, i in enumerate(jogadores):
    print(f'{n:>3}', end=' ')
    for u in i.values():
        print(f'{str(u):<15}', end='')
    print()
print()
while True:
    print('--'*30)
    busca = int(input('Deseja buscar os dados de qual jogador?(999 para parar) '))
    while busca > len(jogadores) or busca < 0:
        print(f'Inválido. Não existe jogador com código {busca}!')
        print('--'*30)
        busca = int(input('Deseja buscar os dados de qual jogador?(999 para parar)'))
    if busca == 999:
        break
    else:
        print(f'levantamento do jogador {jogadores[busca]["nome"]}')
        for i, c in enumerate(jogadores[busca]['gols']):
            print(f'    No {i+1}º jogo, {jogadores[busca]["nome"]}, fez {c} gols.')
