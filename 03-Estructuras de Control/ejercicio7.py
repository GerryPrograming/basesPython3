'''
Pedir por teclado un numero y mostrar la tabla de multiplicar
'''
numero = int(input('Una Tabla de Multiplicar: '))

print('**** Uso del For ****')
for num in range(1,11):
    print(f'{numero} * {num} = {(numero * num)}')

print('**** Uso del while ****')
contador = 1
while contador < 11:
    print(f'{numero} * {contador} = {(numero * contador)}')
    contador += 1