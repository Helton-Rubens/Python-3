aluno = {}
aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().title()
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno["Média"] <= 6:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
print('-='*10)
for k, i in aluno.items():
    print(f'    -{k} é igual a {i}')
