from ModulosdoEx import moeda

p = int(input('Digite o preço: R$'))
t = int(input('Digite a taxa: R$'))
print(f'O aumento do valor em {t}% é R${moeda.aumentar(p, t)}')
print(f'O desconto em {t}% é R${moeda.diminuir(p, t)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}.')
print(f'A metade de R${p} é R${moeda.metade(p)}')
