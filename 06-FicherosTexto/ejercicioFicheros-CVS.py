import csv

# abriendo el archivo 

fichero = open('ejemplo1.csv','r')
contenido = csv.reader(fichero) # leyendo el contenido y guardando en una variable
print(type(contenido)) # saber el tipo de archivo 
datos = list(contenido) # transformar el contenido en lista para verlo mejor 
fichero.seek(0) # regresando el apuntador al incio
fichero.close() # cerrando el fichero
print(datos[0])

print('')

fichero1 = open('ejemplo1.csv','r')
contenido1 = csv.reader(fichero1)
for row in contenido1:
    print("Fila " +str(contenido1.line_num)+ " " + str(row))
fichero1.close()

print(' ')

fichero2 = open('ejemplo2.csv')
contenido2 = csv.reader(fichero2,quotechar='"')
for row in contenido2:
    print(row)
fichero2.close()

# Escribir un fichero
fichero4 = open('ejemplo3.csv','w')
contenido3 = csv.writer(fichero4)

contenido3.writerow(['4/5/2015 13:34', 'Apples', '73']) # escribiendo la informacion
fichero4.close()




