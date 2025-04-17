# Calculo imc

altura = float(input('Introduce tu altura:\n'))
peso = float(input('Ingresa tu peso:\n'))

imc = peso / altura ** 2
print(imc)
# Redondear
# numero a redondear y cantidad de decimales
print(round(imc, 1))

if imc <= 15:
    print('Delgadez muy severa')
elif imc <= 15.9:
    print('Delgadez severa')
elif imc > 15.9 and imc <= 18.4:
    print('Delgadez')
elif 18.4 < imc <= 24.9:
    print('Peso saludable')
# Faltan algunos elif jiji
else:
    print('Obesidad muy severa')