number = list()
while True:
    number.append(int(input('Digite um numero: ')))
    if number.count(number[-1]) == 2:
        print('\033[31mNumeros duplicados não serão adicionados.\033[m')
        number.pop()
    decision = str(input('\033[37mDeseja continuar? \033[m')).strip().lower()
    if decision[0] in 'n':
        break
number.sort()
print(f'Você digitou os números: {number}')

"""
number = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in number:
        number.append(n)
    else:
        print('Números repetidos não serão adicionados!')
    r = str(input('Quer continuar? ')).strip.lower
    if r[0] in 'Nn':
        break
print('-='*30)
numero.sort()
print(f'Você digitou os valores: {number}')"""
