# Operadores adicionales

while True:
    print('Este ciclo es infinito')
    # Intruccion break
    break
    print('Esto no se ejecuta')

print('Fuera del ciclo')

while True:
    opcion = input('Desea continuar? si/no:\n').lower()
    
    if opcion == 'no':
        break
    
    print('Contiuando ciclo...')
