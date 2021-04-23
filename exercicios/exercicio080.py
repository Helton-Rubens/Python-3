#colocar os valores em ordem sem a função .sort()
digito = []
for c in range(1, 6):
    user = int(input('Digite um número: '))
    if c == 1:
        print('Número adicionado no começo da lista')
        digito.append(user)
    elif user > digito[-1]:
        digito.append(user)
        print('Número adicionado no final da lista')
    else:
        pos = 0
        while pos < len(digito):
            if user < digito[pos]:
                digito.insert(pos, user)
                print(f'Número adicionado na posição {pos+1} da lista')
                break
            pos += 1
print('-='*30)
print('Você digitou os números: ',end='')
print(digito)
