
# Pedir datos al usuario por entrada
num1 = input('Escribe un numero')
num2 = input('Escribe otro numero')

# Realizar la conversion de los valores que estan entrando por pantalla
int(num1)
int(num2)

# Contactendo y realizando un cambio de valor para que sean de nuevo string
print("La suma es " + str(num1 + num2))


# Creacion de darle estilo a las concatenaciones dentro de los textos
numero12 = 10

print(f'el numero12 es {numero12}') # nueva forma

print('El numero 12 es {%i}' %numero12) # forma antigua