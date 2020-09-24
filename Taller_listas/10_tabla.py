# Programa que crea un cuadrado sumatorio.

tabla = []
for indice_fila in range(1, 6):
    fila = []
    for indice_col in range(1, 6):
        fila.append(int(input("Ingrese el número de la fila %d y columna %d: " % (indice_fila, indice_col))))
    tabla.append(fila)

print()
print("--TABLA--")
for fila in tabla:
    print(fila)

# Suma de filas.
print()
indice_fila = 1
for fila in tabla:
    print("Suma de fila % d: %d" % (indice_fila, sum(fila)))
    indice_fila += 1

# Suma de columnas.
for indice_col in range(1,6):
    suma = 0
    for fila in tabla:
        suma = suma + fila[indice_col - 1]
    print("Suma de columna % d: %d" % (indice_col, suma))