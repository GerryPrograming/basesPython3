
cadena = 'Hola que tal te va'

# No cambian el objeto cadena

    # Se usa el metodo pero solo en la ejecucion o guardara en una variable

# FORMATO

print(cadena.upper())  # cambia de minuscula a mayuscula
print(cadena.lower())  # cambia de mayuscula a minuscula
print(cadena.capitalize())  # cambia la primera letra en mayuscula
print(cadena.swapcase())  # cambia las minusculas-mayusculas y las mayusculas-minusculas
print(cadena.title())  # Pone los primeros caracteres en Mayuscula
print(cadena.center(50))  # cambia el texto con un espacio centrar(35)
print(cadena.center(50,'-'))  # centrar con un simbolo
print(cadena.ljust(50, '-'))  # Alinear a la izquierda
print(cadena.rjust(50, '-'))  # Alinear a la derecha
print('122'.zfill(12))  # Cuantos ceros se pondran antes del numero 

#BUSQUEDA
print(cadena.count('a'))  # Contar cuantas veces lo encuentra
print(cadena.count('a',4,7)) # contar desde que posicion hasta que
print(cadena.find('ol')) # indica en que posicion se encuentra 
print(cadena.find('oxx')) # si la cadena no existe devuelve un -1
print(cadena.rfind('ol')) # buscar desde la derecha
print(cadena.index('l')) # saber el indice de la letra

# Validacion
print(cadena.startswith('ho')) # si la cadena comienza por una subcadena
print(cadena.startswith('lo',5)) # si en la posicion mencionada empieza con esa palabra
print(cadena.endswith('lo')) # si acaba con la subcadena 
print(cadena.isalnum()) # si son alfanumericos
print(cadena.isalpha()) # si son caracteres del alfabeto
print(cadena.isdigit()) # si es un digito
print(cadena.islower()) # si son minusculas
print(cadena.isupper()) # si son mayusculas
print(cadena.isspace()) # si existe un espacio 

# FORMATOS 
print('{} {}'.format('12', 5)) # dar un formato 
print('{1} {0}'.format('12', 5)) # dar un valor por la posicion
print('{clave2}, {clave3}'.format(clave2 = 'hola', clave3 = 'como estas'))
nuevo = 'hhh'
nuevo2 = '2121'
print(f"{nuevo}, {nuevo2}") # por variables
print('{:^10}'.format('test')) # centra el texto con 10 caracteres

# sustitucion
cadena2 = 'hola como estas'
print(cadena2.replace('o', 'a')) # sustituye los valores dentro de la cadena

cadena3 = '    hola'
print(cadena3.strip()) # devuelve el texto eliminando los espacios
print(cadena3.lstrip()) # elimina espacios a la izquierda
print(cadena3.rstrip()) # elimina los espacios a la derecha
cadena4 = 'xxxxxhola'
print(cadena4.strip('x')) # elimina el valor asignado dentro de parentesis

# metodos de union y division
format_numero_factura = ("N° 0000-0", "-0000 (ID: ", ")")

print("275".join(format_numero_factura)) # coje la cadena y la inserta entre las cadenas 
for i in range(10):
    print(str(i).join(format_numero_factura))

hora = "12:22"
print(hora.partition(':')) # partir un elemento en dos partes convierendo en tupa

hora2 = "12:23:12"
print(hora2.partition(':')) # partir un elemento en dos partes convierendo en tupa
print(hora2.rpartition(':')) # afecta en el orden en que son guardados

print(hora.split(':')) # dividir en una lista

fecha = '12/3/2018'
print(fecha.split('/'))

texto = 'line 1\n line 2\n line 3\n'
print(texto.splitlines())  # hace una lista por cada una de las lineas 

