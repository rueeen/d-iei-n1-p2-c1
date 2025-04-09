# variables
# Una variable es una estructura para guardar datos
nombre = 'Perico' # Las variables deben ser declaradas con un valor asignado
# apellido # Esto da error porque apellido no tiene valor asignado 
# Reglas de variables
# 1. Deben comenzar por letras o guion bajo
# 2. No se puede usar guion medio
# 3. No puede comenzar por numero, pero podemos colocar un numero despues de la primera letra

_apellido = 'Lospalotes' # es valida
#3dad = 27 # no es valida
nombre_completo = nombre + _apellido # para palabras compuestas _ (snake case) o mayusuclas (camel case)
nombreCompleto = nombre + _apellido # El simbolo + concatena

print(nombre, _apellido) # Perico Lospalotes
print(nombre, _apellido, sep=" ") # sep es un keyword argument y realiza un espacio por defecto
print(nombre, _apellido, sep="#", end="@") # Perico#Lospalotes
print(nombre, _apellido, end="\n") # \n representa un salto de linea