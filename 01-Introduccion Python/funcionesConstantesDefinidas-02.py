# Imprimir dentro de consola 
# sep="*" => agregar un separador entre cada texto
# end='.'=> agregar un valor al final 
print('Hola esta es una funcion')
# Pedir informacion al usuario
nombre = input('Pedir el valor al usuario algun dado: Cual es tu nombre? ')
print(nombre)
# Calcular el maximo de numero 
maximo = max(5,3,2)
print(maximo)
# El valor hexadecimal de un numero
hexad = hex(121)
print(hexad)
# construccion de objetos 
a = int('a')
print(a)
# El tipo o clase del dato
tipo = type('Hola')
print(tipo)
# Constantes a nuestra disposicion
verdad = True
falso = False
a = None
print(verdad, falso, a)
# Es importante saber que python 3 es dinamico

# Funcion para pedir ayuda 
help()

# Eliminar una variable que es creada 
numero = 10
del numero

# Funcion para evaluar una expresion
# Si es string tipo numero se podria realizar
x = 1
stringNumero = eval('x+1')
print(stringNumero)

# Referenciar para saber si es verdad el tipo de dato 
isinstance(5, float)
# Dara verdadero o falso si esta es verdad o no

# Funcion que permite saber la referencia a donde esta 
# guardado el valor
numero2 = 5
id(numero2)

# OPERADOR DE REFERENCIA PARA SABER SI ESTAN EN LA MISMA INSTANCIA 
a = 5
b = 5
print(id(a))
print(id(b)) 
print(a is b)

# funciones para cambiar o realizar casting a las variables
int()
float()
bool()
complex()
str()

# Funcion para representar el valor absoluto -3 = 3
variable = -3
abs(variable)

# Funcion para devolver el cociente de una divicion 
divmod(3,2) 
# (1,1) seldra el valor que sale en pantalla de forma de tupla

# Funcion para sacar la potencia sabiendo su base y su expo
pow(5,3)

# Funcion para redondear un numero
round(5.3255215645, 3)