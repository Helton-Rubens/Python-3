#Função que lê a idade de uma pessoa e diz se ela pode votar ou não
def voto(a):
    from datetime import date
    i = date.today().year - a
    if i < 16:
        return f'Negado. Com {i} ano(s) não vota.'
    elif 16 <= i <= 18 or i > 65:
        return f'Opcional. Com {i} ano(s) o voto é opcional.'
    else:
        return f'Obrigatório. Com {i} ano(s) o voto é obrigatório.'


p = int(input('Qual o ano do seu nascimento? '))
print(voto(p))
