# Programa que crea la matriz identidad de orden 5.

identidad = []

for indice_fila in range(1, 6):
    fila = []
    for indice_col in range(1, 6):
        if indice_fila == indice_col:
            fila.append(1)
        else:
            fila.append(0)
    identidad.append(fila)

print()
print("--TABLA--")
for fila in identidad:
    print(fila)