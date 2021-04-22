real = float((input('Digite um valor em reais para descobrir quantos dólares você pode comprar: R$')))
valorD = 5.53
print('No momento, 1 dólar equivale a {:.2f} reais'.format(valorD))
print('Você tem {:.2f} reais na sua carteira e pode comprar {:.2f} dólares!!!\n'.format(real, real // valorD))
print('Se o dólar recebesse um aumento de: 0.5% no mercado,\n o valor do dólar seria: {:.2f} reais.'.format(valorD+0.5/100))
print('Teria em dólar o equivalente a {:.2f} reais.'.format(real//valorD + 0.5/100))