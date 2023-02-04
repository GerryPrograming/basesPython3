'''
Calcular el perimetro y al area de un circulo dado su radio
'''

import math # agregar una libreria

radio = float(input('Cual es el radio de la circunferencia?: '))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio
print(f'La circunferencia tiene una Area:{round(area,2)} cm^2 y Perimetro:{round(perimetro,2)} cm')