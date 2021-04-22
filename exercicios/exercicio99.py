from time import sleep


def linha():
    print("-="*27, end='\n')


def contagem(inicio, fim, salto):
    if salto == 0:
        salto = 1
    if inicio > fim:
        salto = -salto
    for c in range(inicio, fim, salto):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')


print('Contagem de 1 até 10 pulando de 1 em 1')
contagem(1, 10, 1)
linha()
print('Contagem de 10 até 0 de 2 em 2:')
contagem(10, 0, -2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
while True:
    primeiro = int(input('Digite o número onde deverá iniciar a contagem: '))
    segundo = int(input('Digite o número onde a contagem deverá se encerrar: '))
    pulo = int(input('Passo da contagem: '))
    contagem(primeiro, segundo, pulo)
    dec = str(input('deseja continuar[S/N]? ').strip().upper())[0]
    linha()
    while dec[0] not in 'SsNn':
        print('Erro! Digite apenas "Sim" ou "Não"')
        dec = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if dec[0] in "SsNn":
        if dec[0] in 'Nn':
            break
