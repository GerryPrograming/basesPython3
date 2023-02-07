# modulos, paquetes, namespace

> Fichero.py : Esto es un modulo esto es que todos sus elementos son modulos que se pueden importar en otros archivos

> modulos se pueden guardar en directorios se conocen como paquetes con nombre __init.py__ teniendo el comportamiento de paquetes 

> if __name__ == "__main__" se ejecuta este codigo como un scrip que aunque sea importantadas los elementos de los datos a otro archivo no correran en ese, solo dentro del principal o prueba de codigo

> formas de importar los archivos
 
* import potencias 
        => todo el archivo
* import potencias as p 
        => usando un alias
* from potencia import cubo
        => solamente voy a ocupar la funcion que es llamada
* from potencia import *
        => importo todo el archivo
* from potencias import cuadrado as pc
* from dibujos import cuadrado as dc
        => evitar que exista duplicidad se usan los alias

**Importacion de paquetes**

* import operaciones.potencias 
        => nombre paquete y modulo
* import operaciones.suma.ejemplo
        => para entrar a subpaquetes
* Funciones predefinicas como dir()
        => muestra los elementos que podremos utilizar

> Conocer los modulos para poder saber a donde podemos ocupar dentro del nucleo de python y otras que son externar en los directorios del import sys.


# Instalacion de modulos pagina de informacion

> pip permite instalar los paquetes del repositorio dentro de nuestro ordenador para poder instalarlo lo cual existen tres formas para instalar 

* Utilizar los modulos de python que estan instalados en nuesto sistema
   1. No se recomienda por que es una version viejita

* Instalo el programa pip => descargar del repositorio 
   2. pip install request 
   3. No se instala como superusuario ya que se usan con usuarios para no tener conflictos
   
* Instalacion por un entorno virtual 
   4. Crear una parpeta y dentro de esta instalar los paquetes para que no dañen 
   5. o modifiquen archivos
   * virtualenv -p /usr/bin/python3 pip  => indico el entorno
     activar el entorno virtual source ejemplo/bin/activate
     pip install entorno o lo que vallas instalar   
   * tener el mismo modulo pip freeze > requierements.txt lista de modulos que se estan usando para el proyecto a un colega etc.
     pip install -r requierements.txt => instala lo mismo modulos.


        
[Pagina de informacion ](https://pipi.python.org)