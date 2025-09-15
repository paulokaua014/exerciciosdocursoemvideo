from datetime import date
atual = date.today().year
idade = int(input('Qual é a sua idade? '))
idede = atual - idade
print('O atleta tem {} anos.'.format(idade))
if idede <= 9:
    print('Classificação: MIRIM')
elif idede <= 14:
    print('Classificação: INFANTIL')
elif idede <= 19:
    print('Classificação: JÚNIOR')
elif idede <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
