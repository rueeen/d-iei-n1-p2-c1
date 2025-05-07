# con retorno
def contar_vocales(palabra): # palbara = 'hola' -> 2 vocales
    contador = 0 # Contador de vocales
    for caracter in palabra:
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
            contador += 1 # Aumentamos en 1 el contador
            
    return contador

# HoLA -> hola     
palabra = input('Ingrese una palabra: ').lower() # Nos aseguramos de siempre tener la vocal en minuscula

cantidad = contar_vocales(palabra)
print(f'Hay {cantidad} vocales en la palabra {palabra}')