distancia = float(input('Digite a distância da sua viagem em Km: '))
if distancia <=200:
    print('A distância é menor que 200Km, e você irá pagar R$0.45 por Km')
    print('O valor a ser pago pela passagem será de: {:.2f} reais'.format(distancia*0.50))
else:
    print('A distância é maior que 200Km, portanto irá pagar R$0.50 por Km')
    print('O valor a ser pago pela sua passagem será de: {:.2f} reais'.format(distancia*0.45))