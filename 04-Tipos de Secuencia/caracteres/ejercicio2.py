'''
Crear un programa que lea por pantalla una cadena y caracter 
que remplace todo los digitos por el caracter
'''
contrasenia = input('Escribe tu contraseña')
caracter = input('Escriba un caracter ')

# ejercicio basico para esconder caracteres al mostrar el password
for i in range(0,9):
    contrasenia = contrasenia.replace(str(i), caracter)

print(contrasenia)

