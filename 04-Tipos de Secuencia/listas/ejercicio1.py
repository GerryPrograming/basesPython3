
'''
Leer por teclado que se guardaran en una lista este finaliza cuando se meta un numero negativo
Muestra el maximo de los numeros 
Muestra los numeros pares
'''

numeros = []
primos = []

elemento = int(input('Escribe un numero: '))

while elemento > 0:
    numeros.append(elemento)
    elemento = int(input('Escribe un numero: '))

numeroMayor = max(numeros)

for elemen in numeros:
    if elemen % 2 == 0: 
        primos.append(elemen)

print(f'Los numeros primos son {primos}')
print(f'El valor maximo de la lista es {numeroMayor}')