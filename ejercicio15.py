# Ejemplo funcion
    
# Queremos validar que un numero sea par y positivo
# Se deben ingresar 3 numeros

# Instruccion def
def validar_numero(n):
    if n > 0 and n % 2 == 0:
        print('Es valido')

numero1 = int(input('Ingrese un numero:\n'))
# invocar funcion
validar_numero(numero1)

numero2 = int(input('Ingrese otro numero:\n'))
validar_numero(numero2)
    
numero3 = int(input('Ingrese ultimo numero:\n'))
validar_numero(numero3)