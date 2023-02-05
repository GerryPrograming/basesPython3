# Se va ha reccorrer hasta que la condicion se cumpla
anio = 2001

while anio <= 2017:
    print(f'El año es { anio}')
    anio += 1
else:
    print('He terminado')

# nor permite recorrer listas tuplas set secuencias etc
for numero in range(10):
    print(numero) # se espera que imprima los valores que pertenen al rango
            # considerando que el primer valor es 0 hasta rango-1
    if numero == 5:
        break  # romper en el valor 5 o salir

for caracter in 'Python':
    
    if caracter == 'h':
        continue # se salta esta letra y no la mostrara

    print(caracter)
else:
    print('He terminado')

# puede conjugar las secuencias que tengan los mismos valores
for i, j in zip(range(1,4), ['pedro', 'luis','pablo' ]):
    print(i,j)