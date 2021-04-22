primeirotermo = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
cont = 1
dec = 10
total = 0
while dec != 0:
    total = total + dec
    while cont != total:
        print(primeirotermo, end='-->')
        primeirotermo = primeirotermo + raz
        cont = cont + 1
    print('Fim.')
    dec = int(input('Deseja mostrar mais quantos termos? '))
print('Programa finalizado com {} termos mostrados ao usuário.'.format(total))
