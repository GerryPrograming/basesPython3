# abriendoFichero = open('ejemplo1.txt', 'r')


# abriendo el fichero y guardando su contenido en una variable
with open('ejemplo1.txt', 'r') as archivo:
    contenido = archivo.read() # Metodo para leer

print(contenido)

# abriendo el archivo sin cerrarlo 
f = open('ejemplo2.txt', 'r')

print(f.read()) # solo lectura sin hacer algo 

print(f.tell()) # posicion del puntero

print(f.seek(0)) # enviando el pùntero a tal posicion a donde se va escribir
print(f.read())

print(f.readline()) # lee una linea del fichero
f.close()


# creando un archivo nuevo
oc = open('ejemploCreadoConPython.txt','w')

oc.write('Prueba1 ')
oc.writelines([' Prueba2 ', ' Prueba3 ', ' Prueba4 '])
oc.close()

oc = open('ejemploCreadoConPython.txt','r')
print(oc.read())

# recciendo un fichero 
with open('ejemplo2.txt','r') as fichero:
    for linea in fichero:
        print(linea)