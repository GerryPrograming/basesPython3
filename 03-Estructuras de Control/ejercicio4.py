'''
Escribe un programa que pida un nombre de usuario y contraseña 
y si atina a los datos usuario: 'pedro' pass:1234 ha entrado al sistema si no 
datos incorrectos
'''

usuario = input('Ingresa el usuario: ')
contrasena = input('Ingresa la contraseña: ')

if usuario == 'pedro' and contrasena == '1234':
    print('Haz entrado al sistema')
else:
    print('Datos INCORRECTOS!! ')