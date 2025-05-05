# Funciones con retorno

def funcion_con_retorno():
    return 3 + 6

def funcion_sin_retorno():
    print(3 + 6)
    
# print() funcion sin retorno
# n = input() funcion con retorno

resultado = funcion_sin_retorno() # None
resultado = funcion_con_retorno() # 9 

nombre = 'Maria las petunias'
def cambiar_nombre():
    nombre = 'Perico los Palotes'
cambiar_nombre()  
print(nombre) # Maria las petunias
    
def cambiar_nombre_con_retorno():
    return 'Perico los Palotes'
    print('Esto no se ejecuta')
nombre = cambiar_nombre()  
print(nombre) # Perico los Palotes
    