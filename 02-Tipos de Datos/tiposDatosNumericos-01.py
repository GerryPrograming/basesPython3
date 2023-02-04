
# Usando numeros enteros para trabajar con los signos aritmeticos
numero1 = 15
numero2 = 10

print(numero1 + numero2) # suma
print(numero1 - numero2) # resta
print(numero1 * numero2) # multiplicacion
print(numero1 / numero2) # division
print(numero1 % numero2) # resto o reciduo de la division
print(numero1 // numero2) # division entera
print(numero1 ** numero2) # potencia
print(numero1 **.5) # raiz cuadrada

# numero decimales y agrando un entero para ver su comportamiento

numero3 = 12.3
numero4 = 10.2

print(type(numero3 + numero1 + numero4))

# uso de numeros complejos

numero5 = 12 + 3j
print(numero5.real)
print(numero5.imag)
print(numero5)


# Operadores unarios 
print(+2)
print(-2)

# Usando la funcion para mostrar el valor absoluto 
numero6 = -3
print(abs(numero6))

# Saber el cociente de una division y su residuo por medio de una funcion
numero7 = 3
numero8 = 2
print(divmod(numero7, numero8)) # (1,1) se espera este valor

# saber el numero en hexadecimal
hex(12)
# saber el numero en binario
bin(12)
# saber en octal
oct(12)

# funcion para sacar la potencia 
pow(2,3)

# Redondeando un valor 
round(5.3632652622, 2)

# Pero tambien se pueden usar algunos contructores para asignar el tipo
numero10 = int(12.322)
print(type(numero10))


