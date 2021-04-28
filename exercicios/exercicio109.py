from ex109 import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: R$'))
print(f'O aumento do valor em {t}% é {moeda.aumentar(p, t, formato=True)}')
print(f'O desconto em {t}% é {moeda.moeda(moeda.diminuir(p, t, formato=True))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p, formato=True))}.')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p, formato=True))}')
