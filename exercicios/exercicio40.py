from time import sleep
aluno = str(input('Qual o nome do aluno? ')).capitalize().strip()
nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
media = (nota1 + nota2) /2
sleep(1)
print('Calculado...')
sleep(2)
print('A primeira nota do aluno é {:.1f}, a segunda nota é {:.1f}. \n A média entre {:.1f} e {:.1f} é {:.1f}.'.format(nota1, nota2, nota1, nota2, media))
sleep(1)
print('Logo...')
if  media <= 5.0:
    print('\033[1;31m{} não passou de ano.\033[m'.format(aluno))
elif media == 5 or media <=6.9:
    print('\033[1;31m{} está em recuperação.\033[m'.format(aluno))
elif media >= 7:
    print('\033[1;32mO aluno passou de ano.\033[m')