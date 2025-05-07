medida = int(input('Ingrese medida triangulo: '))

# 3
# *
# **
# ***

# Forma 1
asterisco = '*'
for i in range(medida): # n repeticiones
    print(asterisco)
    asterisco += '*'
    
# Forma 2
for i in range(medida): # 3 -> 0, 1, 2
    for j in range(i+1): # i = 0+1, 1+1, 2+1 -> 1, 2, 3
        print('*', end='')
    print()

# Forma 3
for i in range(1, medida+ 1):
    print('*'*i)