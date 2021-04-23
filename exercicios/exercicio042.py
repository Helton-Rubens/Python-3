s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1<s2+3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos acima PODEM formar um triângulo!')
    if s1 == s2 == s3:
        print('\033[1;35mTem todos os lados iguais, portanto, é um triângulo equilátero!\033[m')
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print('\033[1;35mTem\033[m \033[1;4;32mDois Lados Iguais\033[m, \033[1;35mportanto, é um triângulo isósceles!\033[m')
    else:
        print('\033[1;35mO triângulo tem\033[m \033[1;4;32mTodos Os Lados Diferentes\033[m, \033[1;35mportanto, é um triângulo escaleno!\033[m')
else:
    print('\033[1;4;31mOs segmentos acima NÃO conseguem formar um triângulo!\033[m')
