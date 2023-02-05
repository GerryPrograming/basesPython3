# Estructiras de control: Alternativas y Repetitivas

La instruccion que vamos a aprender es el if (si), if-else( si, sino), esto se puede anidar para realizar los procesos o condiciones que se cumplen, cabe resaltar que aqui no se usa el SWITCH.

```python

if (condicion):
    acciones ... # Condicion simple

if (condicion):
    acciones..
else:
    acciones.. # Condicion completa ( si una no se cumple entra al otro lado)

 Existen anidadas dentro de la segunda condicion elif
```

Estas instrucciones nos ayudan a repetir una condicion o un caso varias veces o las veces que se cumplan debido a los contadores o sobre todo las indicaciones que deseamos que se repitan while que se ejecuta mientras que una condicion se cumpla

```python

while(condicion):
    acciones...
    condicion += 1     => Funciona como contador o acumulador para incremento de variable
else:
    print('He terminado')

    break => permite romper el bloque cuando este haya terminado o realizado una accion
```

For cambia mucho de otros lenguajes de programacion por lo que se tiene que ver cual es su condiccion ya que nos permite recorrer una secuencia, lista, set, tuplas, etc

```python

for valor in NombreLista:
    print(valor) => Entrara a la lista Nombre lista y tomara cada uno de los elementos 
                de acuerdo con la posicion dentro de ellas 

    continue => permite saltar ese bucle y no mostrar ese valor 
```

**pass** => Nos permite dejar una instruccion para que se salte ese codigo y no lo ejecute

> Funcion para recorrer varias secuencias

zip()=> enparje las secuencias para que se puedan imprimir 

```python
    for i, j in zip(range(1,4), ['pedro', 'luis','pablo' ])
```

Agregando un metodo para limpiar la consola entre las ejecuciones

```python
import os

os.system('clear') => limpia la pantalla entre cada ejecuccion
```