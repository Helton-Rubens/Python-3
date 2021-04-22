#o programa escreve o fatorial de um número
#na linha 3 a variável "numero" pede ao usuário para inserir um valor de tipo primitivo int
numero = int(input('Digite um numero: '))
#a variável "cont" recebe o valor da variável "numero"
cont = numero
#"fatorial" recebe o valor inteiro 1
fatorial = 1
#na linha 8 é mostrado na tela o valor da variável numero que o usuário digitou
print('{}! = '.format(numero), end='')
#na linha 11 inicia a estrutura de repetição "while" enquanto a variável "cont" for maior que zero
while cont > 0:
    #toda vez que houver uma repetição, fatorial irá multiplicar o valor da variável cont
    fatorial = fatorial * cont
    #a linha seguinte do código irá mostrar o valor da multiplicação
    print(cont, end='')
    #a linha seguinte aos comentários é uma estrutura de condição.
    #Se "cont" for maior que 1, então deve-se mostrar "X"
    if cont > 1:
        print(' X ', end='')
    #Caso contrário, isso é, se "cont" for igual ou menor que 1,
    #deve ser mostrado a string " = " na tela
    else:
        print(' = ', end='')
    #Na linha 26 do código a cada repetição cont subtrai um inteiro
    #Isso irá ocorrer até o valor de cont ser igual a 0, que é quando a estrutura de repetição para
    cont = cont - 1
#Ao final da repetição, o valor final de fatorial, que
# é derivado das multiplicações durante a repetição, será finalmente mostrado
print(fatorial)