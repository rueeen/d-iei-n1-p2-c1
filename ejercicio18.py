# Orden de argumentos posicionales y clave
def operacion(a, b, c):
    print(a + b * c)
    
operacion(1, 2, 3) # 7
operacion(c=1, b=2, a=3) # 5
operacion(3, c=1, b=2) # 5
#operacion(b=1, 2, b=3) # Error
#operacion(1, 2, b=3) # Error