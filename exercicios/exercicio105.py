#Função que lê um número inteiro
def leiaInteiro():
    while True:
        msg = input('Digite um número: ')
        if msg.isnumeric():
            msg = int(msg)
            break
        else:
            print('Erro! Digite um número inteiro válido.')
    return msg


mensagem = leiaInteiro()
print(f'Você acabou de digitar o número {mensagem}')
