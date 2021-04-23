nome = str(input('Seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome com letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas: {}'.format(nome.lower()))
print('{} letras ao todo no seu nome.'.format(len(nome) - nome.count(' ')))
#essa de baixo pode ser feita com ".format(nome.find(' '))"
print('O seu primeiro nome tem {} letras.'.format(len(nome.split()[0])))