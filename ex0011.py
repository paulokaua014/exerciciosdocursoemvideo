real = float(input('Digite quanto ce tem na carteira pra coverter: '))
conversao_dolar = real / 5.48 #convertendo para dolar
print('Com R${} voce tem em dolar ${:.2f}'.format(real, conversao_dolar))