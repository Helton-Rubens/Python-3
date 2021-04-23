somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
nomemulhervelha = ''
maioridademulher = 0
mulheresnovas = 0
for p in range(1,5):
    print('\033[34m=+\033[m'*4,' \033[1;35m{}º PESSOA\033[m'.format(p), '\033[34m=+\033[m'*4)
    nome = str(input('\033[1;33mDigite o nome: \033[m').strip())
    idade = int(input('\033[1;36mDigite a idade: \033[m'))
    sexo = str(input('\033[1;33mSexo [M/F]: \033[m').strip().lower())
    somaidade = somaidade + idade
    if p == 1:
        if sexo == 'f':
            if idade < 20:
                mulheresnovas = mulheresnovas + 1
            nomemulhervelha = nome
            maioridademulher = idade
        elif sexo == 'm':
            nomehomemvelho = nome
            maioridadehomem = idade
    else:
        if sexo == 'f':
            if idade < 20:
                mulheresnovas = mulheresnovas + 1
            if idade > maioridademulher:
                maioridademulher = idade
                nomemulhervelha = nome
        if sexo == 'm':
            if maioridadehomem < idade:
                maioridadehomem = idade
                nomehomemvelho = nome
mediaidade = (somaidade) / 4
print('\n\033[1;33mA média de idade do grupo é de\033[m \033[32m{:.2f}\033[m \033[1;33manos.\033[m'.format(mediaidade))
print('\033[1;33mO nome do homem mais velho é\033[m \033[32m{}\033[m\033[1;33m, e tem {} anos de idade.\033[m'.format(nomehomemvelho, maioridadehomem))
print('\n\033[1;35mO nome da mulher mais velha é {}, e tem {} anos de idade.\033[m'.format(nomemulhervelha, maioridademulher))
print('\033[1;35mHá\033[m \033[1;31m{}\033[m \033[1;35mmulheres com menos de 20 anos.\033[m'.format(mulheresnovas))