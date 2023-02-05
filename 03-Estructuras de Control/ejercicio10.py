'''
Mostrar las tablas de multiplicar del 1 al 5
'''

for i in range(1,6):
    print(f'Tabla {i}')
    for j in range(1,11):
        print(f'{i} * {j} = {(i * j)}')
    print(' ')
    