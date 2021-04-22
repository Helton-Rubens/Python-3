print('\033[1;4;35mGerador de PA\033[m')
print('+='*15)
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
var = 0
while var != 10:
    print(p1, end=' - ')
    var = var + 1
    p1 = p1 + raz
print('Acabou!')