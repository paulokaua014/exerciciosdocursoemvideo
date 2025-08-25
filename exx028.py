nomecompleto = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu primeiro nome é {}'.format(nomecompleto.split()[0]))
print('Seu último nome é {}'.format(nomecompleto.split()[-1]))