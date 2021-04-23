soma = 0
contagem = 0
numero = int(input('Digite um número[digite 999 se quiser parar]: '))
while numero != 999:
    contagem = contagem + 1
    soma = soma + numero
    numero = int(input('Digite um número[digite 999 se quiser parar]: '))
print('A soma de todos os números digitados é igual a {}.'.format(soma))
print('Foram digitados {} números sem contar o dígito "999".'.format(contagem))
