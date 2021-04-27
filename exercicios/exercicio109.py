from ModulosdoEx import moeda

p = int(input('Digite o preço: '))
t = int(input('Digite a taxa: '))
print(f'O aumento do valor em {t}% é {moeda.moeda(moeda.aumentar(p, t))}')
print(f'O desconto em {t}% é {moeda.moeda(moeda.diminuir(p, t))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
