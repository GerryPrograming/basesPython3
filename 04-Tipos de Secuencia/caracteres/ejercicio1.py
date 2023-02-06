'''
Crear un programa que lea por teclado una cadena y un caracter 
E inserte el caracter entre cada letra de la cadena
'''

texto = input('Agrega un texto ')
caracter = input('Agrega un caracter especial ')

# unir los dos valores
agregandoCaracter = caracter.join(texto)
# eliminar los espacios

elimarEspacios = ''.join(agregandoCaracter)
# cambiar el texto a lista

print(elimarEspacios)
