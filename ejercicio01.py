# variables
# Una variable es una estructura para guardar datos
nombre = 'Perico' # Las variables deben ser declaradas con un valor asignado
# apellido # Esto da error porque apellido no tiene valor asignado 
# Reglas de variables
# 1. Deben comenzar por letras o guion bajo
# 2. No se puede usar guion medio
# 3. No puede comenzar por numero, pero podemos colocar un numero despues de la primera letra

_apellido = 'Los palotes' # es valida
#3dad = 27 # no es valida
nombre_completo = nombre + _apellido # para palabras compuestas _ (snake case) o mayusuclas (camel case)
nombreCompleto = nombre + _apellido # El simbolo + concatena