from time import sleep
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))  
reta3 = float(input('Digite o comprimento da terceira reta: '))
print('Analisando as retas...')
sleep(3)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com essas retas é possível formar um triângulo!', end=' ')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO!')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
    
else:
    print('Com essas retas não é possível formar um triângulo!')