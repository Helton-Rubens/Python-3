preço = float(input('O produto vale em reais: '))
print('O valor do produto é {:.2f} reais. Com 5% de desconto, o valor do produto equivale a: {:.2f} reais!!!'.format(preço, preço - (preço*5/100)))
print ('Economiza {:.2f} reais!!!'.format(preço*5/100))