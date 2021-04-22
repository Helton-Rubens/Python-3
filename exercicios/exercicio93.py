jogador = dict()
jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().title()
i = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for i in range(1, i+1):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez no {i}º jogo? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*40)
print(jogador)
print('-='*40)
for c, o in jogador.items():
    print(f'O campo {c} tem valor {o}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {i} partidas')
for p in range(0, len(jogador["gols"])):
    print(f'    => Na {p+1}º partida, fez {jogador["gols"][p]} gols.')
