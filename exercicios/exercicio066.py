soma = numero = dig = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        break
    dig = dig + 1
    soma = soma + numero
print(f'A soma dos {dig} números digitados é igual a {soma}')