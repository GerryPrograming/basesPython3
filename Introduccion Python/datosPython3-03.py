
# Tipos de datos numericos Enteros
numero1 = 32
print(numero1)

# Representacion de un numero en binario 
# usando el 0b antes del numero binario
numero2 = 0b010101
print(numero2)

# Se puede representar los numeros en octal
# usando el 0o numero octal
numero3 = 0o252
print(numero3)

# Se puede representar dentro de los Hexadecimales
# poniendo 0x y el numero 
numero4 = 0xff
print(numero4)

# Se pueden guardar numeros enteros con precisiones grandes 
numero5 = 15485415415468547646468746468468
print(numero5)

# Numeros Reales o decimales
real1 = 12.3
print(real1)
real2 = 0.282
print(real2)

# numeros complejos o imaginarios ( numero entero y imaginario)
# se usan los metodos .real numero real y .imag numero imaginario pero en decimal
complejo = 12 + 3j
print(complejo.real)
print(complejo.imag)
print(complejo)

# Se pueden usar tambien cadenas de texto 
texto = 'cadenaTexto'
print(texto)
texto1 = "hola"
print(texto1)
texto2 = '''
esto es un texto
en varias lineas'''
print(texto2)

# se pueden escapar distintos caracteres.
# https://tutz.tv/python/secuencias-de-escape

# Posibilidad de trabajar con bytes con b
texto4 = b'Hola'
print(texto4)

# Uso de las constrantes booleanas 
verdad = True
falso = False
print(verdad)
print(falso)

# Creacion de una variable para entender 
a = 3
# a es la variable 
# = es lo que permite asignar o darle el valor
# 3 = valor de la variable 
print(a)
