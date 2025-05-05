def resta_argumentos(numero_1, numero_2):
    print(numero_1 - numero_2)
a = 4
b = 3
# ARGUMENTOS POR PALABAR CLAVE
resta_argumentos(a, b) # 1
resta_argumentos(numero_2 = a, numero_1 = b) # -1
# resta_argumentos(numero_3 =b, numero_1=a) # ERROR no existe numero_3 como palabra clave

