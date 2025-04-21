# Hacia atras sepados por comas

numero = int(input('Ingrese numero:\n'))
final = ', '
while numero >= 0: 
    if numero == 0:
        final = '\n'
    # impar    
    print(numero, end=final)
    numero -= 1