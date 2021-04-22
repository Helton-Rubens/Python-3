from time import sleep
print('='*10, ' SuperMercado Santana ', '='*10)
produto = float(input('Digite o valor da compra: \033[1;32mR$\033[m'))
print('\033[1;32m+=+\033[m'*5)
print('Escolha a forma de pagamento:')
sleep(1)
print('\033[32m1\033[m - À vista dinheiro/cheque: com \033[1;35m10% de desconto\033[m.')
print('\033[32m2\033[m - À vista no cartão: \033[1;35m5% de desconto\033[m.')
print('\033[32m3\033[m - Em até 2x no cartão: \033[1;35mpreço normal\033[m.')
print('\033[32m4\033[m - 3x ou mais no cartão: \033[1;35m20% de juros\033[m.')
print('\033[1;32m+=+\033[m'*5)
sleep(3)
escolha = int(input('Digite o número referente a sua escolha: '))
if escolha == 1:
    print('''Você escolheu a opção \033[1;35m1\033[m, dinheiro/cheque à vista com \033[32m10% de desconto\033[m. \nPortanto o valor do produto será de \033[1;32m{:.2f} reais\033[m.'''.format(produto - (produto * 10)/100))
elif escolha == 2:
    print('''Você escolheu a opção \033[1;35m2\033[m, à vista no cartão com \033[32m5% de desconto\033[m. \nPortanto o valor do produto será de \033[1;32m{:.2f} reais\033[m.'''.format(produto - (produto * 5) / 100))
elif escolha == 3:
    print('''Você escolheu a opção \033[1;35m3\033[m, em até 2x no cartão com \033[32mpreço normal\033[m. \nPortanto o valor do produto será de \033[1;32m{:.2f} reais\033[m.'''.format(produto))
elif escolha == 4:
    total = produto + (produto * 20/100)
    totalparc = int(input('Em quantas vezes você irá parcelar? '))
    parcela = total / totalparc
    print(print('''Você escolheu a opção \033[1;35m4\033[m, 3x ou mais no cartão com \033[32m20% de juros\033[m. \nPortanto o valor da compra de R${} será de \033[1;32m{:.2f} reais\033[m.'''.format(produto, produto + (produto * 20) / 100)))
else:
    print('\033[1;31mAtenção!\033[m')
    print('\033[1;31mVocê não digitou nenhuma das opções. \nPor favor, escolha uma das opções\033[m')