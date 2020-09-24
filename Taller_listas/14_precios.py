# Progrma que rastrea artículos.

Precios, Cantidades = [], []

for artículo in range(1, 6):
    Precios.append(float(input("Ingrese el precio del artículo %d: " % artículo)))
    cantidad = []
    for sucursal in range (1, 5):
        cantidad.append(int(input("Ingrese el número de unidades vendidas en la sucursal %d: " % sucursal)))
    Cantidades.append(cantidad)

print("==============REPORTE===============")
print()
print("Cantidades vendidas de cada artículo.")
print()
for artículo in range(1, 6):
    print("Artículo {}: {} unidades vendidas.".format(artículo, sum(Cantidades[artículo - 1])))
print()
print("Cantidad de artículos en la sucursal 2: ", end="")
suma = 0
for artículo in range(1, 6):
    suma = suma + Cantidades[artículo - 1][1]
print(suma)
print()
print("Cantidad del artículo 3 en la sucursal 1: ", Cantidades[2][0])
print()
print("Recaudaciones de cada sucursal.")
suma = 0
recaudaciones = 0
sucursal_mayor = 0
current = 0
for sucursal in range(1, 5):
    for artículo in range(1, 6):
        suma = suma + Precios[artículo - 1] * Cantidades[artículo - 1][sucursal - 1]
    print("Sucursal {}: ${}".format(sucursal, suma))
    recaudaciones = recaudaciones + suma
    if suma > current:
        current = suma
        sucursal_mayor = sucursal
    suma = 0
print()
print("Recaudaciones totales de la empresa: $", recaudaciones)
print()
print("Sucursal de mayor recaudación: ", sucursal_mayor)