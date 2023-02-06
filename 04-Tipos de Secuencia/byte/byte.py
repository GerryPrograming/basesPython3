

# definiendo a un byte
byte1 = b"hola"
print(byte1)
print(byte1)

# usando el constructor
byte2 = bytes(2)
print(byte2) 

# se pueden usar secuencias o colecciones
byte3 = bytes(range(10))
print(byte3)

# se pueden utilizar el metodo para tranformar los datos a çhexadecimal
byte4 = bytes.fromhex('2EF0 F1F2')
print(byte4)

# definir un byte array
ba1 = bytearray(b'hola')
print(type(ba1))

# estos son mutables y funcionan como los arrays
ba1[2] = 90
print(ba1)

# se pueden ocupar los metodos 
# byte3. saber los metodos
# ba1. saber los metodos del byte array pero se tienen q crear los caractes


# evitar que lance error por si no conoce la letra en los 255 caracteres
byte4 = bytes('piña', 'utf-8')
print(byte4)
byte4 = bytes('piña', 'latin1')
print(byte4)

# conversion de unicode a byte
cad = 'piña'
bytes6 = cad.encode('utf-8')
print(bytes6)

# conversion de byte a unicode
cad2 = bytes6.decode('utf-8')
print(cad2)

# en el caso que no este el carecter se puede poner 
# ignore = ignorar
# remplace = remplazar por otro caracter


