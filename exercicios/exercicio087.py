matriz = [[], [], []]
par = 0
somatre = 0
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para a posição [{c}/{i}]: ')))
        if matriz[c][i] % 2 == 0:
            par += matriz[c][i]
    somatre = somatre + matriz[c][2]
print('=+'*28)
for c in range(0, 3):
    print('|', end='')
    for i in range(0, 3):
        print(f'{matriz[c][i]:^5}', end='|')
    print()
print('-'*30)
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {somatre}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
