#Função que lê a ficha de um jogador
def fichaJogador(jogador, gols):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


j = input('Digite o nome do jogador: ')
if len(j) == 0:
    j = '<desconhecido>'
g = (input('Digite a quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
fichaJogador(j, g)
