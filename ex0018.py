
import math

cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))

hipotenusa = round((math.hypot(cateto_oposto,cateto_adjacente)))

print(f'A hipotenusa vale {hipotenusa}')