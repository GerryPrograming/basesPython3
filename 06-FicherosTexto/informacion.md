# Trabajar con ficheros dentro de python

r = lectura
rb = lectura en binario
r+ = lectura y escritura
rb+ = lectura y escritura binaria
w = Solo escritura. Sobreescribir si existe. Crea un archivo si no existe
wb = Solo escritura en modo binario y los mismos conceptos que el anterios
w+ => Escritura y lectura. Se aplica lo de w y wb
wb+ = Escrituta y letecura en binario
a => Añadir (agregar contenido). Crear el archivo si no existe
ab => 
a+ => Añadiendo lectura. crear un archivo si no existe
ab+ = añadiendo lectura en binario

> FUNCION PARA ABRIR UN ARCHIVO TXT
**open** => se pone el nombre y se indica un modo en que se va abrir el fichero (con las opciones de arrba)
**closed** => si el fichero esta cerrado o no (true / fals)
**mode** => saber el modo en el que se esta trabajando
**name** => nombre del fichero
**read** => solo lectura del fichero 
**readline** => lee una linea del fichero
**readlines** => guarda las lineas en un archivo
**tell** => pocision del puntero 
**seek** => mandar al puntero a la posicion que interesa
**write** => permite escribir el texto que se guardara en el archivo
**close** => se tiene que cerrar el archivo cuando se haya terminado de trabajO

> Trabajar con archivos cvs

import csv => trabajar con sus herramientas 

> Trabajar con formatos .json

impor json => importante para trabajar con los diccionarios en python que en json son objetos