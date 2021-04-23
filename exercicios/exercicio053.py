frase = str(input('Digite um palíndromo: ')).strip().lower()
junta = ''.join(frase.split())
for c in range (len(junta), len(junta)-1, -1):
    if frase == frase[::-1]:
        print('A frase é um palíndromo.')
    else:
        print('A frase não é um palíndromo.')