cidade = str(input('Digite o nome da sua cidade: ').strip().capitalize())
print('O nome da cidade é: {}'.format(cidade))
print('O primeiro nome da cidade é: {}'.format(cidade.split()[0]))
print('Há "Santo" no primeiro nome da cidade? {}'.format('Santo' in cidade.split()[0]))