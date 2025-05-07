def es_par(numero):
    if numero % 2 == 0: # Recorda que el % es el residuo de division
        return True
    return False

numero = int(input('Ingrese numero: '))

if es_par(numero): # Si retoro es True
    print('Es par')
else: # Si retorno es False
    print('Es impar')