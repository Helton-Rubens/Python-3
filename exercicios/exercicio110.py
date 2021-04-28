# Outra maneira de resolver o exercício 109
from ex109 import moeda

p = int(input('Digite o preço: R$'))
t = int(input('Digite a taxa: '))
print(f'O aumento do valor em {t}% é {moeda.aumentar(p, t, formato=True)}.')
print(f'O desconto em {t}% é {moeda.diminuir(p, t, formato=True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}.')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}.')
