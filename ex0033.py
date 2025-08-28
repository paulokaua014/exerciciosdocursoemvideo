n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
if n1 >= n2 and n1 >= n3:
    print('O maior valor digitado foi {}'.format(n1))
else:
    if n2 >= n1 and n2 >= n3:
        print('O maior valor digitado foi {}'.format(n2))
    else:
        print('O maior valor digitado foi {}'.format(n3))