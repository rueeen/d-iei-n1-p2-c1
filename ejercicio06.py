# fucion input() para entrada de datos

input('Escriba algo: ')

# la funcion input() devuelve o retorna informacion
nombre = input('Ingrese su nombre: ')
Nombre = input('Ingrese su nombre:\n')

print(f'El primer nombre es: {nombre} y el segundo es: {Nombre}')


# Vamos a sumar 2 numeros ingresados desde teclado
num1 = input('Ingrese 2 numeros:\n') # 3 str
num2 = input('Ingrese otro numero:\n') # 5 str

resultado = num1 + num2

print(f'El resultado de la operacion es: {resultado}') # 35 concatenan

# casting
# de str a int
num1_int = int(num1)
int(num2)

resultado = num1_int + num2 # ERROR