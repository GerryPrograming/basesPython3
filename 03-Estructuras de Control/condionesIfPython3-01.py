
numero = -1
# Si numero es menor a 0 entonces entra en la condicion 
if numero < 0:
    print ('ok')

if numero >= 0:
    print('Positivo')
else:
    print('Negativo')

if numero == 0:
    print('Es cero')
elif numero < 0:
    print('Es negativo')
else:
    print('Es positivo')

# forma reducida de if
lang='es'

saludo = 'hola' if lang == 'es' else 'hi'