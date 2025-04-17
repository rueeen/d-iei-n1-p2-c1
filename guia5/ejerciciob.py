n1 = int(input('Ingrese un numero:\n'))
n2 = int(input('Ingrese otro numero:\n'))

if n1 > n2:
    print(f'El mayor es {n1}')
elif n1 < n2:
    print(f'El mayor es {n2}')
else:
    print('Son iguales')