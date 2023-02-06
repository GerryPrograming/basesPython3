
# Forma y creacion de cadenas 
cad1 = 'hola'
cad2 = "Como estas"
cad3 = '''
        que tal 
        te va'''
print(cad1)
print(cad2)
print(cad3)        

# Constructor para convertir un dato entero a cadena
numero = 10
print(type(str(numero)))

# recorrer una cadena 
print(cad1[1:2])

# saber el tamaño de la cadena 
print(len(cad2))

# saber el caracter mas grande pero son las letras
print(max(cad1))
print(min(cad1))

# se puede ordenar la cadena con la funcion sorted
print(sorted(cad1))

# => Cadena es inmutable no se puede cambiar un elemento de la cadena

# comparacion con assci
if 'a'>"A":
    print('a es mayor')
else:
    print('A es mayor')

# DATOS CURIOSOS
# si comparamos dos letras va ir una a una hasta que encuentre un valor que le permita sacer la respuesta
# si una es mas pequeta la otra ganara esto es en cuestion de caracteres

# Representacion de un objeto que representa el estado del objeto)
print(repr(range(1,10)))

# saber el ascii que lo represetan
letra = ascii('á')
print(letra)

