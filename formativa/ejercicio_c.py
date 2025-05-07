def mostrar_palabra_mayor(palabra1, palabra2):
    contador1 = 0
    contador2 = 0
    
    for caracter in palabra1:
        if caracter != " ":
            contador1 += 1
            
    for caracter in palabra2:
        if caracter != " ":
            contador2 += 1
            
    if contador1 > contador2:
        print(f'La palabra mayor es :{palabra1}')
    elif contador1 < contador2:
        print(f'La palabra mayor es :{palabra2}')
    else:
        print('Son iguales')

palabra1 = input('Ingrese una palabra: ') # Hola mundo
palabra2 = input('Ingrese otra palabra: ') # acertijo

mostrar_palabra_mayor(palabra1, palabra2)

if palabra1 > palabra2: 
    print('La palabra 1 es mayor')
    
# 3 > 5 -> False
# 5 > 2 -> True
# 'Hola mundo' > 'zorro' -> False