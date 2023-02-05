'''
Crear una aplicacion que pida un numero y calcule su factoral
'''

print('**** Uso del while ****')
numero = int(input('Factorial de: '))
factorial = 1

while numero > 0:
    factorial *= numero
    numero = numero -1

print(f'El factorial es {factorial}')

print('**** Uso del For ****')

for num in range(numero):
    factorial *= num

print(f'El factorial es {factorial}')