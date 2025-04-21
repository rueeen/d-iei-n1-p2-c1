# Impares hacia atras

numero = int(input('Ingrese numero:\n'))
final = ', '
contador = 1
while numero >= contador: 
    if contador % 2 != 0: # 15 o 16
        if contador == numero or numero == contador + 1:
            final = '\n'
        # impar    
        print(contador, end=final)
    contador += 1