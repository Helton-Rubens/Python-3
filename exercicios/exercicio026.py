frase = input('Digite uma frase qualquer: \n').strip().lower()
print('A letra "A" apareceu na frase {} vezes'.format(frase.count('a')))
print('A letra "A" apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "A" apareceu pela ultima vez na posição {}'.format(frase.rfind('a')))