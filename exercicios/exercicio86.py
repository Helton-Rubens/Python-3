#matriz em python
matriz = [[], [], []]
for c in range(0, 3):
    for cont in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para a posição [{c+1}/{cont+1}]: ')))
print('=-'*30)
for i in range(0, 3):
    print('|', end='')
    for cont in range(0, 3):
        print(f"{matriz[i][cont]:^5}", end='|')
    print()
