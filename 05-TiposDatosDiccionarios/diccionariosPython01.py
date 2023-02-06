
# usando el constructor para crearlos
numerosIngles = dict(one=1, two=2,three=3)
print(type(numerosIngles))
print(numerosIngles)

# Accediendo a la informacion del diccionario por medio de clave
print(numerosIngles['one'])

# creando una modificacion en un valor del diccionario
numerosIngles['one'] = 10
print(numerosIngles)

# usando las llaves se pueden crear
letrasIngles = {
    'a':'ei',
    'b':'bi',
    'c':'ci'
}
print(letrasIngles)

# usando la funcion zip
c = dict(zip(['one','two'],[1,2]))
print(c)

# usando una lista de tuplas
d = dict([(1,'one'),(2,'two')])
print(d)

# saber el tamaño de
print(len(d))

# puede modificar un elemento
c['one']+=1
print(c)

# borrar un elemento
del letrasIngles['c']
print(letrasIngles)

# clave de pertencia
print(1 in d)

claves = iter(d)
print(next(claves))
print(next(claves))

# puedo utilizar metodos 
x = c.copy()
print(x)
x['one'] = 100
print(x)



