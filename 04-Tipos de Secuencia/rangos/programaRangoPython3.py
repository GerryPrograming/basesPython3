
# Inicio: Final: Intervalos
rango = range(10,20,2)

for i in rango:
    print(i)

inicio = list(range(10))
print(inicio)

final = list(range(0,15))
print(final)

intervalos = list(range(10,50, 5))
print(intervalos)

# Se pueden usar operadores de pertencia
print(10 in inicio)

# Saber el valor por la posion
print(inicio[3])

# Usan atributos 
print(rango.start)
print(rango.stop)
print(rango.step)
