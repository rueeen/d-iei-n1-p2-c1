# Contar caracter 'a' dentro de palabra
# paralelepipedo
# hay 2 'a' en paralelepipedo
# Dato de entrada
palabra = input('Ingrese una palabra:\n').lower()
# Proceso
contador = 0
for caracter in palabra: # caracter pasa por cada letra de la palabra
    if caracter == 'a':
        # contarla
        contador += 1        
# Dato de salida
print(f'Hay {contador} letras "a" dentro de {palabra}')