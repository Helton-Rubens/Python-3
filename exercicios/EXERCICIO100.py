from time import sleep


def maior(*numero):
    numai = 0
    print('Analisando os valores passados....\n')
    sleep(1)
    for c in numero:
        if c > numai:
            numai = c
        print(c, end=' ', flush=True)
        sleep(0.5)
    sleep(1)
    print(f'Fim!\nO maior número foi:', end=' ', flush=True)
    sleep(1)
    print(numai)
    print('-='*28)


maior(4, 50, 185, 1, 4, 89, 58, 30)
