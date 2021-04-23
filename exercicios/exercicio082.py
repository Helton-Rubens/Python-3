lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    dec = str(input('Quer continuar? ')).strip().lower()
    if dec[0] in 'Nn':
        break
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'''Você digitou os números: {lista}
Os números pares digitados foram: {par}
Os números impares digitados foram: {impar}''')
