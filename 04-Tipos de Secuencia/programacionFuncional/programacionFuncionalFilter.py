
lista = [3,4,5,6,3]

def numerosPares(x):
    return x % 2 == 0

pares = list(filter(numerosPares,lista))
print(pares)