'''
Determinar si el numero ingresado por teclado es primo
'''

numero = int(input('Ingresa un numero: '))

primo = True

for cont in range(2,numero):
    if numero % cont == 0:
        primo = False
        break
if primo:
    print('Es primo ')
else:
    print('No es primo')