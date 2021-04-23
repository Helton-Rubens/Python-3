nome = str(input('Digite o nome completo: ').strip().title())
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Ultimo nome: {}'.format(nome.split()[-1]))