def mayor_o_menor(a, b):
    if a > b:
        print(f'El mayor es {a}')
    elif a < b:
        print(f'El mayor es {b}')
    else:
        print('Son iguales')
        
# Invocar funcion
n1 = float(input('Ingrese un numero: '))
n2 = float(input('Ingrese segundo numero: '))

mayor_o_menor(n1, n2)