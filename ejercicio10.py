# Ejemplo for

# Podemos recorer 2 objetos con for (por ahora)

# str palabras
saludo = 'Hola mundo'

for c in saludo:
    print(c)
print('Fuera del ciclo')

# recorriendo numeros 
# Asi no funciona: Type error int no se recorre
#for n in 10:
#    print(n)

# funcion range()
# primera forma
for i in range(10): # 0, 1, 2, 3, 4, 5, ..., 9
    print(i)

# segunda forma
#            inicio, fin
for i in range(2, 10): # 2, 3, 4, 5, ..., 9
    print(i)
    
for i in range(10, 2): # -> no genera lista
    print(i)
    
# tercera forma
#         inicio, fin, incremento
for i in range(2, 10, 3): # 2, 5, 8
    print(i)
    
for i in range(10, 2, -1): # 10, 9, 8, 7, 6, ..., 3
    print(i)