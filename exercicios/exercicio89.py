from time import sleep
tudo = list()
dados = []
continuar = ' '
while continuar[0] not in 'Nn':
    aluno = str(str(input('nome: ').strip().title()))
    notaum = float(input('Nota 1: '))
    notadois = float(input('Nota 2: '))
    dados.append(aluno)
    dados.append(notaum)
    dados.append(notadois)
    tudo.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? '))
    while continuar[0] not in 'SsNn':
        print('Digito inválido')
        continuar = str(input('Quer continuar? '))
print('-='*20)
print(f'{"No.":3}', f'{"NOME":9}', f'{"MÉDIA":>18}')
print('--'*20)
for c in range(0, len(tudo)):
    print(f'{c+1}.', end=' ')
    print(f'{tudo[c][0]}', end='')
    if tudo[c][-1]:
        print('{:.>23.1f}'.format((tudo[c][1] + tudo[c][2])//2))
while True:
    print('-'*30)
    dec = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if dec == 999:
        break
    while dec > len(tudo) or dec < len(tudo):
        print('=-'*10)
        print('\033[1;4;31mDígito inválido. O número referente ao aluno é inexistente.')
        sleep(1)
        print('Por favor, escolha um dígito válido\033[m')
        print('=-'*10)
        sleep(1)
        dec = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if dec == 999:
            break
    print(f'Notas do(a) aluno(a) {tudo[dec-1][0]} são {tudo[dec-1][1]:.1f} e {tudo[dec-1][2]:.1f}!')
print('\nFinalizando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print()
print()
print('-'*20, ' Obrigado por usar o programa ', '-'*20)
