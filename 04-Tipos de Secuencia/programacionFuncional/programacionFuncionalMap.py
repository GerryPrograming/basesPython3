
# Creacion de la lista con caracteres
listaCaracteres = ['1','2','3','4','5']

# tranformar a enteros 
listaNumeros = list(map(int,listaCaracteres)) # Retorna un mapa por lo que se hace su 
                                                # conversion a list
print(listaNumeros)

# Creando una primer funcion para entender
# cuadrado de un numero
def cuadrado(x):
    return x * 2

print(cuadrado(5))

listaNumeros2 = [2,5,4,8,6,3,4]
print(listaNumeros2)
# se mando llamar a la funcion creada para que realice algo
listaCuadratica = list(map(cuadrado, listaNumeros2))
print(listaCuadratica)



