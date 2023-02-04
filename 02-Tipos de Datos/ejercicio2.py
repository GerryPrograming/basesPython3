
'''
Calcula el area del perimetro y area de un triangulo dada su base y altura
'''

base = float(input('Cual es el la base del triangulo '))
altura = float(input('Cual es su altura del triangulo '))
area = base * altura
perimetro = (2 * base) + (2 * altura)
print(f'El triangulo tiene de Area:{round(area,2)} cm^2  y Perimetro:{round(perimetro,2)} cm')