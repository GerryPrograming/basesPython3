
# Metodos para manejar las listas 

lista = [1,2,3]

lista.append(10)
print(lista)

lista2 = [6,2,3]
lista.extend(lista2)
print(lista)

lista2.insert(0,100)
print(lista2)

valor = lista.pop()
print(valor)

'''
AÑADIR
lista.append => Añadir un elemento al final de la lista
lista.extend => Permide añadir una lista al final de la primera
lista.insert => añadir un elemento en una posicion 

ELIMINAR
lista.pop   => devuelve el ultimo elemento y lo quita de lista
            => permite borrar un elemento en la posicion dada .poo(10)
lista.remove => borrar un elemento indicando en la posicion
                borrando el primer dato de los pedidos

MODIFICACIONES
lista.reverse => Muestra la lista al reves
lista.sort => ordena la lista
            => key=str.lower => pasa a minusculas
lista.clear  => borra la lista y la deja en blanco
lista.count => cuenta cuantos valores existen de un elemento 2
lista.index => saber el inidice a donde esta el elemento tal
lista.copy => permite copiar una lista
'''