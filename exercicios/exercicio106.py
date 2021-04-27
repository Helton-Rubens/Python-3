def calculanotas(*num, sit=False):
    '''
    Uma função que calcula a média, total e verifica a maior
    e a menor nota.
    :param num: As notas que serão verificadas.
    Podem ser utilizadas quantas notas quiser.
    :param sit: (Opcional) Revela a situação do aluno.
    :return: retorna os dados para a variável em forma de um dicionário,
    revelando a situação do aluno(ou da turma).
    --> Função feita por Helton
    '''
    lista = dict()
    total = 0
    med = 0
    menor = 0
    maior = 0
    for c in num:
        med += c
        total += 1
        if total == 1:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c

            elif c < menor:
                menor = c
    med = med // total
    lista['Total'] = f'{total} nota(s)'
    lista['Média'] = med
    lista['Maior'] = maior
    lista['Menor'] = menor
    if sit:
        if med <= 5:
            lista['situação'] = 'Ruim'
        elif med >= 8:
            lista['situação'] = 'Boa'
        else:
            lista['situação'] = 'Razoável'
    return lista


resp = calculanotas(1.5, 1.5, 9, 10, sit=True)
print(resp)
help(calculanotas)
