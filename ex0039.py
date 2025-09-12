ano = int (input('Em que ano você nasceu? '))
idade = 2024 - ano
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar.')
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))