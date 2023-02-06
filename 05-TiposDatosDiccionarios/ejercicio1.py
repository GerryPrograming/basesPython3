'''
Escriba un programa que lea una cadena y devuelva un diccionario 
con la cantidad de letras que aparecen en la cadena
'''

cadenaDic = {}
cadena = input('Escribe una cadena: ')

listaPalabras = cadena.split(' ')

for palabra in listaPalabras:
    # agregar el contador
    if palabra in cadenaDic:
        cadenaDic[palabra] += 1
    else:
        cadenaDic[palabra] =1

for campo,valor in cadenaDic.items():
    print(campo, '=>' , valor)