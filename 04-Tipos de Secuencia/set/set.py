
#RECORDAR QUE ESTOS SON MUTABLES


# Creacion de un tipo set que no se pueden repetir los valres
# usando el constructor {} de esta forma se representan
tiposet = set()
print(type(tiposet))

# lista con repeticiones que son ignoradas 
tiposet2 = set([1,1,2,3,5,4,1,2,4,5,2])
print(tiposet2)

tiposet3 = {1,2,3,4,5}
print(tiposet3)

# AÑADIR UN ELEMENTO
tiposet3.add(100)
print(tiposet3)

# solamente se pueden recorrer, operadores de pertenencia, ordenar.

'''
set.add => añadir elementos
set.clear => limpiar el set
set.copy => copiar 
set.difference => diferencia entre un conjunto y otro
set.diferrence_update
det.discards => intenta borrar un elemento y no lanza error
set.intersection
set.intersection_update
set.isdisjoint
set.issuperset
set.pop
set.remove => borrar un elemento
set.symmettric_difference => distintos del uno y dos
set.symmettric_difference_update => diferencia que permite modificar el conjunto
set.union
set.update
'''