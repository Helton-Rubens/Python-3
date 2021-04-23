print('\033[1;4;35mTABUADA!\033[m\n')
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('---'*10)
    if numero <= 0:
        break
    for cont in range(1, 11):
        print(f'{numero} x {cont} = {numero * cont}')
    print('---'*10)
print('Programa finalizado!')
