# Programa que imprime un marco de 1s.

marco = []

for indice_fila in range(1, 6):
    fila = []
    for indice_col in range(1, 16):
        if indice_fila == 1 or indice_fila == 5 or indice_col == 1 or indice_col == 15:
            fila.append(1)
        else:
            fila.append(0)
    marco.append(fila)

print()
print("--TABLA--")
for fila in marco:
    for elemento in fila:
        print(elemento, " ", end = "")
    print()