continuar = ''
countwomen = 0
countmen = 0
maioridade = 0
while continuar != 'N':
    print('\033[1;34mCadastre uma Pessoa\033[m')
    print('===' * 10)
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade = maioridade + 1
    sexo = str(input('Digite o sexo[M/F]: ').upper().strip())
    if sexo == 'F':
        if idade < 20:
            countwomen = countwomen + 1
    elif sexo == 'M':
        countmen = countmen + 1
    while sexo != 'M' and sexo != 'F':
        print('\033[1;4;31mOpção inválida!\033[m')
        print('\033[1;31mDigite uma opção válida\033[m')
        sexo = str(input('Digite o sexo [M/F]: ').upper().strip())
    print('\033[1;35m==\033[m' * 10)
    dec = str(input('Quer continuar[S/N]? ')).upper().strip()
    if dec == 'N':
        break
    print('\033[1;35m==\033[m' * 10)
    while dec != 'S' and dec != 'N':
        print('\033[1;4;31mOpção inválida!\033[m')
        print('\033[1;31mDigite uma opção válida\033[m')
        dec = str(input('Quer continuar[S/N]?')).upper().strip()
print('=' * 10)
print('\033[1;32mPROGRAMA FINALIZADO!\033[m')
print(f'''Ao todo foram {countmen} homens cadastrados,
{countwomen} mulheres com menos de 20 anos,
e {maioridade} pessoas com mais de 18 anos.''')
