palabra = input('Ingrese una palabra:\n')
cantidad = int(input('Ingrese cantidad:\n'))

print('Con for')
for r in range(cantidad):
    print(palabra)
    
print('Con operador *')
print((palabra+'\n')*cantidad)

print('con while')
while cantidad > 0:
    print(palabra)
    cantidad -= 1