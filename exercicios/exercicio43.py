#O programa calcula o IMC
peso = float(input('Digite o peso: (Kg)'))
altura = float(input('Digite a altura: (m)'))
imc = (peso/(altura**2))
print('O seu \033[4;32mÍndice de Massa Corporal\033[m é {:.2f}'.format(imc))
if imc < 18.5:
    print('Portanto, você está abaixo do peso ideal.')
elif imc < 25:
    print('Portanto, você está no peso ideal.')
elif imc < 30:
    print('Portanto, você está com sobrepeso.')
elif imc <40:
    print('Portanto, você está com obesidade.')
else:
    print('Portanto, você está com obesidade mórbida.')
