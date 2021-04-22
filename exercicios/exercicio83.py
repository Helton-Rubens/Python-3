#validador de expressão matemática!
expre = str(input('Digite uma expressão matemática: '))
lista = []
for i in expre:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(i)
            break
if len(lista) > 0:
    print('Expressão é inválida!')
else:
    print('A expressão é válida!')
