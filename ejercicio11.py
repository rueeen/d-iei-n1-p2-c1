# Ejemplo while

# Funciona con condiciones
# validar que el numero ingresado sea positivo

num = int(input('Ingrese numero positivo:\n'))
while num <= 0:
    print('Error: Debe ingresar numeros positivos')
    num = int(input('Ingrese numero positivo:\n'))
print('Fin del ciclo')