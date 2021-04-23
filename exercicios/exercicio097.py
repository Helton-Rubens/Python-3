def areaterreno(a, b):
    r = a * b
    print(f'A área de um terreno {a}x{b} é de {r}m²')


print(f'{"Controle de terrenos":>}')
print('--'*(len('Controle de terrenos')))
largura = float(input('Digite a largura(M): '))
comprimento = float(input('Digite a altura(M): '))
areaterreno(largura, comprimento)
