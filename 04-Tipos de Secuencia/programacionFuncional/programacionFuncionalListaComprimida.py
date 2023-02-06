

lista = [x ** 3 for x in [1,2,3,4,5]]
print(lista)

listaPares = [x for x in range(10) if x%2 == 0]
print(listaPares)

lista3 = [x + y for x in [1,2,3] for y in [4,5,6]]
print(lista3)