from datetime import date
trab = dict()
trab['nome'] = str(input('Nome: ').strip().title())
trab['Ano de Nascimento'] = int(input('Ano de nascimento: '))
idade = date.today().year - trab['Ano de Nascimento']
trab['ctps'] = int(input('Carteira de trabalho(0 se não tiver): '))
print('-=+' * 20)
if trab['ctps'] == 0:
    for c, i in trab.items():
        if i == trab['ctps']:
            print(f'   -o {c} tem valor {i} pois o usuário não tem carteira de trabalho')
        else:
            print(f'   -o {c} é {i}')
else:
    trab['Ano de Contratação'] = int(input('Ano de contratação: '))
    trab['salário'] = float(input('Salário: R$'))
    print('-=+'*20)
    for c, i in trab.items():
        print(f'   -o {c} é {i}')
    print(f'O usuário {trab["nome"]} tem {idade} anos\nSe aposenta com {68-idade} anos')
