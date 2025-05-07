def validar_fecha(dia, mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        # Meses con 31 dias
        if dia >= 1 and dia <= 31:
            return True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        # Meses con 30 dias
        if dia >= 1 and dia <= 30:
            return True
    elif mes == 2:
        # Febrero
        # dias entre 1 y 29
        if dia >= 1 and dia <= 29 and es_bisiesto(anio):
            return True
        elif dia >=1 and dia <= 28:
            return True
    
    return False

def es_bisiesto(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

d = int(input('Ingrese dia: '))
m = int(input('Ingrese mes: '))
a = int(input('Ingrese año: '))

respuesta = validar_fecha(d, m, a) # Devuelve True o False

if respuesta == True:
    print('Fecha correcta!')
else:
    print('Fecha incorrecta')