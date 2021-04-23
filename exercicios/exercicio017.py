from math import sqrt
catetoOP = float(input('Digite o cateto oposto do triângulo em cm: '))
catetoADJ = float(input('Digite o cateto adjacente do triângulo em cm: '))
hipotenusa = sqrt(((catetoOP**2) + (catetoADJ**2)))
print ('O comprimento da hipotenusa é: {}cm '.format(hipotenusa))