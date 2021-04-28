from ex108 import moeda

p = int(input('Digite o preço: R$'))
t = int(input('Digite a taxa: R$'))
print(f'A {moeda.aumentar(p, t)}')
print(f'{moeda.diminuir(p, t)}')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
