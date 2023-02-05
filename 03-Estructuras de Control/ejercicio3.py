'''
Introduccir un numero del 1 al 12 para referirnos al mes
y determinara cuantos dias tiene ese mes
'''

mes = int(input('Introduce un valor del 1-12: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 12:
    print('El mes indicado tiene 31 dias')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('El mes tiene 30 dias')
else:
    print('El mes tiene  28 dias')