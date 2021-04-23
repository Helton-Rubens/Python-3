metros = int(input('\033[30mDigite uma altura em metros para conversão de unidades de medida: \033[m'))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print('\033[36m{} metros\033[m \033[30mequivale a\033[m \033[4;32m{}km\033[m '
      '\n \033[4;32m{} Hm\033[m '
      '\n \033[4;32m{} Dam\033[m '
      '\n \033[4;32m{} Dm \033[m'
      '\n \033[4;32m{} Cm\033[m '
      '\n \033[4;32m{} Mm!\033[m'.format(metros, km, hm, dam, dm, cm, mm))