nome = input ('Qual é o seu nome?\n')
print ('Seu nome é {}{}{}?'.format('\033[1;32m', nome, '\033[m'), 'Olá, \033[1;32m{}\033[m. É um prazer te conhecer.'.format(nome))
idade = input ('\033[1;32m{}\033[m, qual é a sua idade?\n'.format(nome))
peso = input ('\033[1;32m{}\033[m, por favor digite o seu peso:\n'.format (nome))
print ('Seu nome é \033[1;32m{}\033[m,'.format(nome), 'você tem \033[1;32m{}\033[m'.format(idade),
       'e pesa \033[1;32m{}\033[m.'.format(peso))
pergunta = input ('Estou certo?')
if pergunta == ('sim'):
    print ('\033[1;32mObrigado por usar o programa, até mais!')
elif pergunta == ('Sim'):
        print ('\033[1;32mObrigado por usar o programa!')
elif pergunta == ('não'):
    print ('\033[1;31mMe desculpe pelo erro')
elif pergunta == ('Não'):
            print ('\033[1;31mMe desculpe')