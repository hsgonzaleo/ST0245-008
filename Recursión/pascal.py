# Este programa imprime un número n de filas del triángulo de Pascal (Ejercicio 8).

filas = []

def pascal(n, filas):  # Esta función construye n filas y las agrega a una lista utilizando recursividad.
    fila = []
    if n == 0:  # Caso base.
        fila.append(1)
        filas.append(fila)
    else:
        pascal(n-1, filas)
        fila.append(1)
        for i in range(0, n-1):
            fila.append(filas[n-1][i]+filas[n-1][i+1])
        fila.append(1)
        filas.append(fila)

n = int(input("Ingrese el número de filas a imprimir (desde 0): "))

pascal(n, filas)

for fila in filas:
    print(fila)
