#faça um programa que calcula a soma entre todos os números ímpares múltiplos de três
#que se encontram no intervalo entre 1 e 500
soma = 0
contador = 0
for tre in range(1, 501, 2):
    if tre % 3 == 0:
        contador = contador + 1
        soma = soma + tre
print('\033[1;35mA soma entre todos os {} valores requisitados é igual a\033[m \033[4;32m{}\033[m'.format(contador, soma))
