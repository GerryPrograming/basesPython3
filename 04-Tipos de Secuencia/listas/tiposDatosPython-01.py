
lista = [1,2,3,4,5,6]
# Todos los tipos de datos se pueden recorrer
for elemn in lista:
    print(elemn)

# Podemos ocupar el operador de pertenencia ( si esta el valor )
print(5 in lista) # true
print(12 in lista) # false

# se puede usar el not para saber si no esta en la lista 
print(12.3 not in lista) # true

# se pueden realizar las operaciones 
print(lista + [8,9,10,11,12,13]) * 3

# acediendo a los elementos de lista 
lista[2] # sin olvidar que las listas comienzan en cero referente a su posicion

# obtencion de un conjunto de elementos desde inicio a fin
lista[1,5]

# saber los elementos que tiene la secuencia 
len(lista)

# comparan los elementos para sacar el max y min
max(lista)
min(lista)

# NOTA SI LA SECUENCIA ES MUTABLE SE PUEDE CAMBIAR UN ELEMENTO
lista[2] = 12
lista[1,3] = [5,5] 

# borrar parte de la secuencia 
del lista[1,3]




