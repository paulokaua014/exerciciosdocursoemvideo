reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))  
reta3 = float(input('Digite o comprimento da terceira reta: ')) 
if reta1 < reta2 + reta3:
    print('Com essas retas é possível formar um triângulo!')
else:
    print('Com essas retas não é possível formar um triângulo!')