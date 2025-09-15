from time import sleep
import random
jokes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(jokes)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada inválida! Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('-=' * 11)
    print('Computador jogou {}'.format(computador))
    print('Jogador jogou {}'.format(jokes[jogador]))
    print('-=' * 11)
    if computador == 'Pedra':
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
    elif computador == 'Papel':
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')
    elif computador == 'Tesoura':
        if jogador == 0:
            print('JOGADOR VENCE!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')