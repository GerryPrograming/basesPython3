'''
Dada una lista de cadenas 
Escribir una cadena de texto por teclado
Indicar si la palabra esta en la lista, cuantas veces aparace en la lista.
'''

listaTextos = [
    'manzana', 'pera', 'uvas', 'platano', 'cereza', 'durazno','pera', 'uvas', 'platano', 'cereza',
    'pera', 'uvas', 'pera', 'uvas', 'platano', 'cereza', 'nichis','naranja'
    ]

texto = input('Escribe tu fruta favorita: ')

# saber si un valor esta dentro 
if texto in listaTextos:
    print ('Se encuentra en la lista tu fruta preferida')
else:
    print('Muy pronto agregaremos otras frutas ')
    
aparaciones = listaTextos.count(texto)
print(f'La fruta que te gusta existe {aparaciones} veces')