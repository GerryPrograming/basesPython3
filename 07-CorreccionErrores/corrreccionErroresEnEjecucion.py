
# Al referirnos a estos errores tienen que ver con la ejecuccion por lo que 
# se pueden ir corregiendo para evitar que se cuelgue el programa.
# no se puede realizar las operaciones, no se a creado la variable o datos de distinto tipo

# Validacion para una lectura de datos 
while True:
    try: 
        x = int(input('Introduce un numero: '))
        break
    except ValueError:
        print('Deber Introducir un numero')

print(x)

# Validacion para cuando una divicion 0
cad = input('Dame un numero: ')

try:
    print(10/int(cad))
except ValueError:
    print('No se puede convertir a entero')
except ZeroDivisionError:
    print("No se puede dividir por cero")
except:
    print('Otro error')

# Como poder obtener informacion de los errores ya definidos
cad2 = input('Dame un numero ')
try:
    i = int(cad2)
except ValueError as error:
    print(type(error))
    print(error.args)
    print(error)

# excepciones para algunas funciones 
def dividir(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'No se puede dividir'

def dividir2(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        raise # se ha produccido un error dentro de la funcion

print(dividir(5,0))
try:
    print(dividir2(5,0))
except:
    print('No se puede dividir')