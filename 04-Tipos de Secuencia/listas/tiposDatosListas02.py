
# Creacion de una lista vacia
lista = []

# Creacion de una lista con informacion sin compartir sy tipo
lista2 = [1, 'hola', True]
print(type(lista2[0]))
print(type(lista2[1]))
print(type(lista2[2]))

# creando otra lista usando el constructor 
lista3 = ['h','o','l','a']
print(lista3)
lista4 = range(0,10)
print(lista4)

# sacar informacion de la lista 
# lista[inicio:final:saltos]

lista10 = [12,15,10,5,6,2]
# funcion para sumar los valores de la lista
sum(lista10)

# permite ordenar los elementos
sorted(lista10)
sorted(lista10, reverse=True)

# funcion para enumarar los elementos de una lista 
estaciones = ['Primareva', 'Verano', 'Otoño', 'Invierno']

# De esta forma creamos una diccionario a partir de una lista
print(list(enumerate(estaciones)))

# Existen listas multidimencionales o tablas 
lista12 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(lista12[1][1])

for fila in lista12:
    for elemen in fila:
        print(elemen, end="")
    print()
