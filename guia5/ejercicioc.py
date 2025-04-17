# Formato de str SOLO STRINGS
palabra1 = input('Ingrese una palabra:\n').capitalize()
# capitalize()
# palabra1 = 'HOLA' -> 'Hola'
# upper()
# palabra1 = 'hoLA' -> 'HOLA'
# lower()
# palabra1 = 'hoLA' -> 'hola'
palabra2 = input('Ingrese otra palabra:\n').capitalize()

if palabra1 == palabra2:
    print('Son iguales')
else:
    print('No son iguales')