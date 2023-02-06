
from functools import reduce

lista = [2,4,5,6,8,8,2,4,2]

def add(x,y):
    return x + y

sumaValores = reduce(add,lista)
print(sumaValores)