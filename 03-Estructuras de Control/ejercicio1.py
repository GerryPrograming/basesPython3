
'''
Realiza un ejercicio que pida al usuario dos numeros y si la suma de estos numeros 
indique si es positivo, negativo o cero
'''

numero1 = int(input('Escribe un numero: '))
numero2 = int(input('Escribe otro numero: '))

suma = numero1 + numero2

if suma == 0:
    print('Es igual a cero')
elif suma <= 0:
    print('Es negativo')
else:
    print('Es positivo')