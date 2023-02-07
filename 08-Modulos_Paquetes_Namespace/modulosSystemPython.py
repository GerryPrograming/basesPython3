
# Contrucciones de script
import os # Modulo del Sistema (Metodos)

print(os.getcwd()) # conocer el directorio donde estamos trabajando
print(os.chdir('...')) # cambiar el directorio

print(os.system('ls')) # mandar instrucciones directamente en el sistema (mostrando las salidas)
print(os.system('ls -al')) # muestra todos los directorios del sistema 

import subprocess # La salidas se puedan guardar en variables 

print(subprocess.call('ls')) # ya se puede guardar en variable para trabajar
salida = subprocess.check_output('ls') # guardando la salida en una variable
print(type(salida))
print(salida.decode()) # decodificando para verla como es

salida2 = subprocess.check_output(['df', '-h']) # instrucciones con parametros 
print(salida2.decode())


import shutil
import os

ruta = os.getcwd() + os.sep # ruta actual y el separador 
origen = ruta + 'origen.txt' 
destino = ruta + 'destino.txt'

try:
    shutil.copyfile(origen, destino)
    print('Archivo copiado')
except:
    print('Se ha producido un error ')

import sys # trabajar y pedir informacion del interprete

# sys.exit() # salir del interprete de python
sys.version # saber la version del editor
sys.platform # la plataforma que se usa

# parametros por la linea de comandos van a sumar y se creara una lista con todos los argumentos mandados
print('Has introduccido', len(sys.argv),'argumento')

print(sys.argv)

suma = 0
for i in range(1,len(sys.argv)):
    suma = suma +int(sys.argv[i])
print('La suma es ', suma) 


