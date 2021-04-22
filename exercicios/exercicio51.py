#10 primeiros termos da progressão aritmética
pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da progressão aritmética: '))
for c in range(pt, pt + (11-1) * raz,raz):
    print(c, end = '-')
print('Acabou!')