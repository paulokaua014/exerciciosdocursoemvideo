n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor valor: '))
soma = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1// n2
e = n1 ** n2
print('A soma e {}, o produto e {}, e a divisao e  {:.3f}'.format(soma, m, d), end=' ')
print('A divisao inteira {} e a pontencia {}'.format(di, e))