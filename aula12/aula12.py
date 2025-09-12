nome = str(input('Qual é o seu nome? '))
if nome == 'Paulo':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paula':
        print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
elif nome in 'Carlos Miguel Rafael Gabriel':
    print('Belo nome masculino!')
else:
    print('Seu nome é tão normal!')
    print('Bom dia, {}!'.format(nome))