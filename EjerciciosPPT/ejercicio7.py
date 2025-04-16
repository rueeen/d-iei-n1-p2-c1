# Precio producto y su descuento

precio_producto = int(input('Ingrese precio producto:\n'))
descuento_producto = int(input('Ingrese descuento producto:\n'))

descuento = precio_producto * descuento_producto / 100
total = precio_producto - descuento

print(f'El producto de precio {precio_producto} con {descuento}% de descuento es: {total}')