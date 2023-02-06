
import json

datos_json ={
    'nombre':'juan',
    'edad': '15'
}

#datos = json.loads(datos_json) # permite leer los datos 

# print(datos['edad']) # imprimir los valores

# desde un fichero
with open("ejemplo.json") as fichero:
    datos1 = json.load(fichero)

print(datos1)

# Escribir datos en nuevo fichero json
datos = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie'}
fichero3 = open('ejemplo3.json', 'w')
json.dump(datos,fichero3)
fichero3.close()
print(fichero3)