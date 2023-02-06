'''
Escribir un programa que dada dos cadenas de caracteres indique si la segunda
es un producto de la primer cadena  y devuelva la que sea anterior 
en orden alfabetico
'''

texto1 = input('Cadena 1: ')
texto2 = input('Cadena 2: ')

# saber si existe la cadena2 dentro de la uno

if texto1.find(texto2)> -1:
    print( 'La cadena 2 es una subcadena de la uno ')
else:
    print('cadena2 no se encuentra en la primera')

# imprimir uno de los dos casos si el texto1 es mejor al texto2
print(texto1 if texto1 < texto2 else texto2)