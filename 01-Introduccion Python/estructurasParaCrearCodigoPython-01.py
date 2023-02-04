edad = 25

# Respetar la identacion de cada una de las condiciones
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# Respetar la sangria para su identacion
if num >= 0:
    while num < 10:
        print(num)
        num = num + 1

# No realizar esto aunque es valido poner un ; para continuar escribiendo
edad = 15 ; print(edad) 

# Cuando es el bloque una linea se puede eliminar la sangria
if azul: print('cielo')

# Se puede usar la barra invertida para continuar 
# escrtibiendo texto en la misma linea 
if condicion1 and condicion2 and condicion3 and \
    condiciona4 and condiciona5:

# las listas pueden estar en varias lineas 
# para su entendimiento
dias = ['lunes', 'martes', 'miercoles','jueves',
        'viernes', 'sabado', 'domingo']