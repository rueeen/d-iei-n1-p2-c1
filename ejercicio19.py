# Parametros por defecto
def sumar(a=5, b=3, c=2):
    print(a + b + c)
    
sumar(1, 2, 3) # 6
sumar(1, 2) # 5
sumar(1) # 6
sumar() # 10
sumar(b=3, c=1) # 9
# sumar(c=10, 2) # Error, debe haber palabra clave
