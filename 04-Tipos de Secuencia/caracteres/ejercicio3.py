'''
Crea un programa que lea una cadena de textos y muestre la siguiente informacion
// primera letra de cada palabra 
// dicha letra en mayuscula
// palabra que comienza con la letra a
'''

cad = input('Cadena de texo: ')

# dividir la lista en palabras 
listaPalabras = cad.split(' ')

for i in listaPalabras:
    print(i[0], end='')
print()

for palabra in listaPalabras:
    print(palabra.capitalize(), end="")
print()

for palabra in listaPalabras:
    if palabra.startswith('a') or palabra.startswith('A'):
        print(palabra, end=",")
print()
