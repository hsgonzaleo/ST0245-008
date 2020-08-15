### Este programa determina el número de pasos mínimo para resolver el juego de las torres
# de Hanoi utilizando un algoritmo recursivo utilizando un cálculo (Ejercicio 7).

def hanoi(n, c):
    if n == 1:  # Caso base.
        return 2 - c
    else:
        return 2*hanoi(n-1, 0) - c

n = int(input("Ingrese el número de discos a utilizar: "))
print("El número de pasos mínimos a utilizar es:", hanoi(n, 1))