# Ejemplo if

# Es para evaluar condiciones

edad = 15

# Quiero saber si la persona es mayor de edad
if edad >= 18:
    print('No se ejecuta porque edad es menor que 18')
    
edad = 20
if edad >= 18:
    print('Usted es mayor de edad') # Aca si se cumple la condicion
    
#edad = 30
#if edad >= 18:
#print('Usted es mayor de edad') Esto da error por la indentacion

#color = 'rojo'
#if color == 'rojo':
#    print('El color es rojo')
#     print('Me gusta ese color') Da error por la alineacion de la indentacion

if False:
    print('Este es el cuerpo del if')
#print('Esto esta mal') Esta linea da error al salirse del bloque
    print('Esto esta dentro del if')
print('Esta esta fuera del if')