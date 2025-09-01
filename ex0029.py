from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
numEscolhido = int(input('Escolha um numero de 0 a 10: '))
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('-=-' * 20)
print('Será que você consegue adivinhar qual foi?')
print('-=-' * 20)
print('Analisando o número...')
sleep(3)
if numEscolhido == computador:
    print('VOCE ACERTOU!!!!!')
else:
    print('VOCÊ ERROU!!!!!')