viagem = float (input('Qual a distância da sua viagem? '))
if viagem <= 200:
    preço = viagem * 0.50
    print('O preço da sua viagem será de R$ {:.2f}'.format(preço))
else:
    preço = viagem * 0.45
    print('O preço da sua viagem será de R$ {:.2f}'.format(preço))

print('Tenha uma boa viagem!')