edad = int(input('Ingrese su edad:\n'))

# Quiero saber si la persona es mayor de edad
if edad >= 18: # Verdadero
    print('Usted es mayor de edad')
elif edad >= 13:
    print('Usted es adolescente')
elif edad < 0:
    print('La edad que ingreso no es valida')
else: # Falso
    print('Usted es menor de edad')
    
