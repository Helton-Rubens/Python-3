def ajuda(a):
    """
    Uma função que ajuda o programador a conhecer uma função ou biblioteca.
    Recebe
    :param a: Função ou biblioteca
    :return:
    """
    help(a)


def titulo(a):
    """
    Uma função que cria um cabeçalho.
    :param a: Uma mensagem que será mostrado ao usuário.
    :return:
    """
    print('~~~'*len(a))
    print(a)
    print('~~~'*len(a))


titulo('Sistema de Ajuda do Python')
print('\nDigite "exit" para sair')
while True:
    fb = input('Função ou biblioteca >').lower()
    if fb == "exit":
        break
    else:
        ajuda(fb)
print('Até logo!')
