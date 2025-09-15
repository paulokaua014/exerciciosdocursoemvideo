nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if 7 > media < 5.0:
    print('Sua média foi {:.1f}, Você está REPROVADO.'.format(media))
elif 5.0 <= media < 7.0:
    print('Sua média foi {:.1f}, Você está de RECUPERAÇÃO.'.format(media))
else: 
    print('Sua média foi {:.1f}, PARABÉNS! Você está APROVADO.'.format(media))