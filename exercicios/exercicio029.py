velocidade = float(input('Digite a velocidade atual do carro em Km/h: ').strip())
if velocidade >= 80.0:
    print('=== ATENÇÃO ===')
    print('O seu carro ultrapassou a velocidade estabelecida, que era de 80Km/h.')
    print('A multa será aplicada da seguinte maneira: \n R$7.00 por cada Km excedente.')
    print('A velocidade do seu carro foi de {}Km/h \ne multa será de: R${:.2f}'.format(velocidade, (velocidade-80.0)*7.0))
else:
    print('Tenha um bom dia! Dirija com segurança!')