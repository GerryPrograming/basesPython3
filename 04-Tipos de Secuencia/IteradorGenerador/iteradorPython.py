
from itertools import count
from itertools import cycle
from itertools import islice

iterador = iter([1,2,3])
print(type(iterador))

for i in iterador:
    print(i)

iterador2 = iter('hola')
print(type(iterador2))

for i in iterador2:
    print(i)

# existen algnos metodos
iterador3 = iter([1,2,3,4])
print(type(iterador3))

print(next(iterador3)) # => permite iterar cuando se cumple todos los eventos
print(next(iterador3))
print(next(iterador3))
print(next(iterador3))
print()
iterador4 = reversed([1,2,3,4])

print(next(iterador4)) # => permite iterar cuando se cumple todos los eventos
print(next(iterador4))
print(next(iterador4))
print(next(iterador4))
print()

itera = count(start=10) # creasmos un iterador infinito para usar next
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))
print()

# va entrando a cada uno de los valores de la lista
colors = cycle(['rojo', 'verde', 'azul'])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print()

# funciona como cycle pero este limita a donde mandara un error si hay menos casos que el rango
limited = islice(colors,0,5)
print(next(limited))
print(next(limited))
print(next(limited))
print(next(limited))
print(next(limited))