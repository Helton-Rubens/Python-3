import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input ('Terceiro aluno: ')
aluno4 = input ('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi: \033[4;32m{}\033[m'.format(random.choice(lista)))