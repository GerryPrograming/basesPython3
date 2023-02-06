'''
Dada una lista de numeros indica si la lista esta ordenada o no 
'''

numeros = [2,100,6,8]
lista2 = numeros[:]
lista2.sort()

if lista2 == numeros :
    print('La lista esta ordenada')
else:
    print('La lista esta desordenada')