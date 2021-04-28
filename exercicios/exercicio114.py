def leiaInteiro(txt):
    while True:
        try:
            val = int(input(txt))
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar os dados e saiu do programa.')
            return 0
        except ValueError:
            print(f'Erro de dígito. Digite apenas números inteiros.')
        else:
            return val


def leiaFloat(txt):
    while type(txt) != int or type(txt) != float:
        try:
            v = str(input(txt)).replace(',', '.').strip()
        except ValueError:
            print('Erro! Digite apenas números reais.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar os dados e saiu do programa.')
            return 0
        else:
            return float(v)


valor = leiaInteiro('Digite um inteiro: ')
valorf = leiaFloat('Digite um número Real: ')
print(f'foram digitados os valores {valor} e {valorf}')
