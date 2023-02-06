dic = { }

dic1 = dic.fromkeys(['one', 'two', 'three', 'four'],100)
print(dic1)

dic2 = {'five': 5, 'six' :5}


dic1.update(dic2) # no se tiene que guardar en una variable por lo que asigna los valores
print(dic1) 

dic1.setdefault(('two'),200)  # muestra el valor con el que tiene
print(dic1)

dic1.setdefault(('seven'),200)  # agrega el elemento que no se tiene a la lista
print(dic1)

print(dic1.get('seven'))

valor = dic1.pop('one')
print(valor)


print(dic1.items())
print(dic1.keys())
print(dic1.values())

'''
CREACIO O AÑADIR ELEMENTOS
dic.copy => copiar un diccionario en otro
dic.fromkeys => crear una lista a partir de donde vamos a guardar las claves
            El valor que se les pone es para que todos los ponga en ese valor
dic.update => juntar dos diccionarios 
dic.setdefautl => si la clave existe me devuelve el valor que tenia esa clave
        => si la clve no existe la crea

EXISTEN ELEMENTOS DE RETORNO 
dic.get => indica una clave y devuelve un valord
ic.pop = devuelve el valor de la clave pero la borra
dic.popitem => elimina un conjunto de elementos
dic.item => conocer el conjunto de claves y valores en ()
dic.keys => devuelve objeto con las claves
dic.values => devuelve los valores

dic.clear

'''