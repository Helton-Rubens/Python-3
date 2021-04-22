dec = ' '
jogadores = list()
jogador = dict()
while dec[0] not in 'Nn':
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
print(f'{"Cod"} {"Nome":<15}{"Gols"}{"Total":>15}')
