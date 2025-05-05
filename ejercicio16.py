# Funciones
#             parametros
def suma_numeros(): # funcion SIN parametros
    print(5+3)
    
# INVOCAR FUNCION
suma_numeros() # Se envian 0 argumentos

def suma_numeros_con_parametros(a, b, c): # 3 parametros
    print(a + b + c)
    
suma_numeros_con_parametros(1, 2, 3) # Se envian 3 argumentos
# Esto da error #suma_numeros_con_parametros(1, 2) # Se envian 2 argumentos

def resta_argumentos(numero_1, numero_2):
    print(numero_1 - numero_2)
    
a = int(input('Ingrese un numero:\n')) # 3  
b = int(input('Ingrese un numero:\n')) # 4

resta_argumentos(a, b) # -1
resta_argumentos(b, a) # 1
numero_1 = 4
numero_2 = 3
# ARGUMENTOS POSICIONALES
resta_argumentos(numero_2, numero_1) # -1