
# Creacion de una tupla
tupla = (1,2,3)
print(type(tupla))
print(tupla)

# Creacion de una lista usando el constructor
tupla2 = tuple([2,3,4,4])
print(tupla2)

tupla3 = tuple(range(2,5))
print(tupla3)

# CONCEPTO DE EMPAQUETADO Y DESEMPAQUETADO
tuplaEmpaquetada = 2,5,6
print(type(tuplaEmpaquetada))
print(tuplaEmpaquetada)

# Desempaquetando la tupla
num1,num2,num3 = tuplaEmpaquetada
print(num1, num2, num3)

tupla4 = (2,4,5,6)
for x in tupla4:
    print(x)

# Operador de pertencia
respuesta = 5 in tupla4
print(respuesta)

# Concatenacion de otra tupla
tupla1 = (2,1,3,4)
tupla2 = (2,3,5,5)
print(tupla1 + tupla2)

# obtencion de valor 
print(tupla1[1])

#Saber los elementos que se repitemn
print(tupla1.count(2))

#Saber el inidice del elemento 
print(tupla1.index(2))
print(tupla1[0])