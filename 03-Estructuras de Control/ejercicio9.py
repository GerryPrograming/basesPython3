'''
Ser capas de adivinar un numero creado por la computadora
'''
import random, os

# Creando el numero aleatorio por la computadora
numeroAleatorio = random.randint(1,100)
contador = 0

numero = int(input("Adivina el numero que estoy pensando: "))
os.system('clear')

while numeroAleatorio != numero:
    numero = int(input("Adivina el numero que estoy pensando: "))
    os.system('clear')
    if numero < numeroAleatorio:
        print('El numero debe ser mas grande ')
    else:
        print('El numero debe ser mas pequeño')
    contador += 1

print(f'Haz lograro encontrar el numero en {contador} intentos')
