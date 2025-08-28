salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Seu salario era de R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Seu salario era de R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))