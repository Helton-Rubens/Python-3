from math import cos, tan, sin, radians
n1= float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(n1))
print ('O SENO do ângulo {}° é {:.2f}°'.format(n1, seno))
cosseno = cos(radians(n1))
print ('A COSSENO do ângulo {}° é {:.2f}°'.format(n1, cosseno))
tangente = tan(radians(n1))
print ('O TANGENTE do ângulo {} é {:.2f}°'.format(n1, tangente))