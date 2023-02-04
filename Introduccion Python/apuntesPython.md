# Python3 

> Primer ejercicio lanza un error, sin embargo, es para acostumbrarnos como debemos escribir el codigo dentro de python para permitir que corra el archivo

[Estructuras Basicas ](estructurasParaCrearCodigoPython-01.py)

> Estructiras predefinidas 

Tener algunas funciones ya definidas que podremos utilizar dentro de python nos puede ayudar a utilizarlas para no estar creando algunas que ya esten difinidas, sin embargo, se podria crecar su uso y si esta no resolviera lo que deseas hacer entonces si es recomendable crear las propias

**Importante** *Python3 es dinamico: que sabe o interpreta el tipo de valor que le fue asignado*

[Funciones Definidas por Python](https://docs.python.org/3/library/functions.html)
[Ejemplo de algunas funciones](funcionesConstantesDefinidas-02.py)

> Datos : Es la informacion que se captura de acuerdo a la solucion que se pretende alcanzar (Entrada-Proceso-Salida); que son las variables, literales, constantes etc.

[Diferentes tipos de datos](datosPython3-03.py)

dentro del texto se pueden usar algunos escapes de caracteres para realizar algunas acciones
[Escape de caracteres](https://tutz.tv/python/secuencias-de-escape)

Tenemos a la disposcion los siguientes operadores sin olvidarnos la importante de la precedencia de los operadores.
* Aritmeticos
* Cadenas
* Asignacion
* Comparacion
* Logicos
* Nivel de bit
* Pertencia 
* Identacion

> Tipos de datos :  Son los valores que podemos usar dentro de nuestra variables y sobre todo lo que vamos a poder ir trabajando a lo largo del programa.

Numericos (int, float, complex)
booleanos (bool)
Datos Secuencia (list, tuple, range)
Caracter (str)
Binarios (bytes, bytearray)
Conjuntos (set, frozenset)
Diccionarios (dict)
Iterador y Generador (iter)

Esto es que nos permite trabajar con tu tipo o clase siento estos tambien tipos de datos.
(Ficheros, Modulos, Funciones, Excepciones, Clases)

Python al usar las **variables** lo que hace es generar una referencia a la memoria para ahorrar espacio, gerando asi el tipado dinamico (los tipos antes vistos).
Tambien es importante saber que dentro de python existen tipos de datos mutables o inmutables
**inmutable** = No se puede modificar el valor sin embargo en python solo cambia la referencia
       Ejemplo : Int, cadenas de texto, 
**mutables** = Se pueden mudificar valores de acuerdo a su posicion en especifico hay que tener cuidado ya que se pueden muficar ambas si existe una referencia a otra variable. 
        Ejemplo = lista, diccionarios o map

```python
a = 5
b = 5
a is b # saber si se apunta a la misma referencia con ayuda del id() si no queda claro el concepto
```
