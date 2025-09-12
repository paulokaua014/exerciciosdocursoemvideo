from time import sleep
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))  
reta3 = float(input('Digite o comprimento da terceira reta: '))
print('Analisando as retas...')
sleep(3)
if reta1 < reta2 + reta3:
    print('Com essas retas é possível formar um triângulo!')
elif reta2 == reta1 == reta3:
    print('Com essas retas é possível formar um triângulo equilátero!')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('Com essas retas é possível formar um triângulo isósceles!')

else:
    print('Com essas retas não é possível formar um triângulo!')