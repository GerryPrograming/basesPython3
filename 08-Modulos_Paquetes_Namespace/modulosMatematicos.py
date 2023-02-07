
import math # funciones matematicas math.

print(math.factorial(5)) # factorial
print(math.pow(2,3)) # potencia 
print(math.sqrt(30)) # raiz cuadra
print(math.cos(81)) #el coseno de un numerop
print(math.pi) # valor de pi
print(math.log(2)) # logaritmo

from fractions import Fraction

a = Fraction(2,3) # creacion de una fraccion
b = Fraction(1,3)
print(a+b)

import statistics

print(statistics.mean([2,3,5,6,4])) # calcula la media
print(statistics.median([2,3,5,6,4])) # calcula la mediana

import random

print(random.randint(50,120)) # numero al azar entre esos datos
print(random.choice([1,5,2,5,2,1])) # elige de forma aleatoria entre varios elementos
lista =[5,2,6,45,12,8,5,4]
print(random.shuffle(lista)) # toma un valor aleatorio
print(random.sample(lista,2)) # elige de forma aleatoreia el numero de elementos

# EXISTEN MAS METODOS ENTRE CADA UNO DE LOS QUE SE HAN TRABAJADO

