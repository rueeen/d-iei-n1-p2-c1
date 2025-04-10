# Operaciones

# operacion +
num1 = 5
num2 = 3
resultado = num1 + num2
print(resultado) # 8

num3 = 5.1
num4 = 3
resultado = num3 + num4
print(resultado) # 8.1

num5 = -3
num6 = 1.0 # float
resultado = num5 + num6
print(resultado) # -2.0

# Concatenacion
nombre = 'Perico'
apellido = 'Los palotes'
nombreCompleto = nombre + " " +apellido # str
print(nombreCompleto) # Perico Los palotes
edad = 40 # int
# saludo = "Hola "+nombreCompleto+" tienes "+ edad+" años" ESTO DA ERROR
# Hola Perico Los paotes tienes 40 años
# IMPORTANTE
# en python no puedo usar operador + entre str e int

# Operacion - resta
# Solo funciona entre int y float
n1 = 5
n2 = 6
resultado = n1 - n2 # -1
print(resultado)
n3 = 5.0
resultado = n3 - n2 # -1.0
print(resultado)

# Operacion * multiplicacion
n1 = 3
n2 = 4
n3 = 3.0
resultado = n1 * n2 # 12
resultado = n3 * n2 # 12.0

# Puedo hacer operacion * entre str y int
palabra = "hola"
numero = 3

resultado = palabra * numero # holaholahola
print(resultado)
resultado = (palabra+" ") * numero # hola hola hola
numero = 3.0
#resultado = palabra * numero # Error

# Operacion / division
n1 = 12
n2 = 4
n3 = 0

resultado = n1 / n2 # 3.0 SIEMPRE ES FLOAT EL RESULTADO
#resultado = n1 / n3 # No se puede dividir por 0

# Operacion ** potencia
n1 = 2 # base
n2 = 3 # exponente
resultado = n1 ** n2 # 8

# Operacion % modulo
n1 = 5
n2 = 3

resultado = n1 % n2 # 2 RESIDUO
#resultado = n1 % 0 # ERROR por division por cero

# Operacion //
n1 = 7
n2 = 2
resultado = n1 // n2 # 3.5 -> 3
print(resultado)

n1 = -7
resultado = n1 // n2 # -3.5 -> -4
print(resultado)

# operacion directa
contador = 1
contador = contador + 1 # 2
# Abreviado
contador += 1 # 3 
contador -= 2 # 1
contador *= 3 # 3
contador /= 3 # 1.0
contador **= 2 # 1
 
