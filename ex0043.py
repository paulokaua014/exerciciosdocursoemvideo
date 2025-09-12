from time import sleep
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Calculando seu IMC...')
sleep(3)
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA. CUIDADO!')

print('Seu IMC é de {:.1f}'.format(imc))