sexo = str(input('Digite o seu sexo [M/F]: ').strip().upper()[0])
while sexo != 'M' and sexo != 'F':
    print('''\033[1;31mAlerta!
Você não digitou nenhuma das opções.
Tente novamente.\033[m''')
    sexo = input('Digite o seu sexo [M/F]: ').strip().upper()
if sexo == 'M':
    sexo = '\033[1;35mMasculino\033[m'
elif sexo == 'F':
    sexo = '\033[1;35mFeminino\033[m'
input('Sexo {} registrado com sucesso.'.format(sexo))