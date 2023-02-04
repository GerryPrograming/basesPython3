'''
Dado dos numeros mostrar la suma, resta, multiplicacion y division
'''

numero1 = float(input('Escribe un primer numero: '))
numero2 = float(input('Escribe un segundo numero: '))

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
div = numero1 / numero2

print(f'Suma:{suma}, Resta:{resta}, Multiplicacion:{multi}, Division:{round(div,3)}')