# Mostrar datos por pantalla

# "Hola nombre, bienvenido a la unidad II de python 2025"
anio = 2025
nombre = 'Perico'
apellido = 'Los Palotes'

print("Hola", nombre, apellido, "bienvenido a la unidad II de python", anio)
# "Hola Perico Los Palotes bienvenido a la unidad II de python 2025"

# "Estoy saludando a Perico los Palotes. Bienvenido Perico"
print("Estoy saludando a", nombre, apellido, ". Bienvenidon", nombre)
# "Estoy saludando a Perico Los Palotes . Bienvenido Perico"

# Formas de imprimir mensajes
# Forma 1 Concatenando
print("Estoy salundado a "+nombre+" "+apellido+". Bienvido "+nombre)

# Forma 2 format()
print("Estoy saludando a {} {}. Bienvenido {}".format(nombre, apellido, nombre))

# Forma 3 format moderno
print(f"Estoy saludando a {nombre} {apellido}. Bienvenido {nombre}")