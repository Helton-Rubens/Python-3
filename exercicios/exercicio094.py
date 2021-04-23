pessoas = list()
cadastro = dict()
total = 0
dec = ' '
while dec not in 'Nn':
    cadastro['nome'] = str(input('Digite o nome: '))
    cadastro['idade'] = int(input('Digite a idade: '))
    total += cadastro['idade']
    cadastro['sexo'] = str(input('Digite o sexo: ')).upper()[0]
    while cadastro['sexo'] not in "MmFf":
        print('Erro! Digite somente M ou F.')
        cadastro['sexo'] = str(input('Digite o sexo: ')).upper()[0]
    dec = str(input('Quer continuar?[S/N] '))
    while dec not in 'SsNn':
        print('Erro! Digite apenas "Sim" ou "Não"')
        dec = str(input('Quer continuar?[S/N] ')).upper()
    pessoas.append(cadastro.copy())
media = total//len(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas!')
print(f'B) A média de idade é de {media:.1f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c["sexo"] == 'F':
        print(c["nome"], end=' ')
print()
print(f'D) Lista de pessoas acima da média:')
for c in pessoas:
    if c["idade"] >= media:
        print('    ', end='')
        for i, k in c.items():
            print(f'{i} = {k} ;', end=' ')
        print()
print('ENCERRADO')
