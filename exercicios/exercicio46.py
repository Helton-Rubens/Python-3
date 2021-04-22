from time import sleep
print('\033[1;36mContagem regressiva para o estouro de fogos de artifício!\033[m')
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print('\033[1;35mCOMEÇOU!\033[m')