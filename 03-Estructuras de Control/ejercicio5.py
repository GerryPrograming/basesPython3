'''
Realizar un programa que pida un año e indicar si es bisiesto o no
'''

anio = int(input('Indica el año que deseas saber si es bisiesto: '))

if anio % 4 == 0 or anio % 100 == 0 and anio % 400 == 0:
    print('El año es bisiestio tiene 366')
else:
    print('El año no es bisiesto tiene 365')