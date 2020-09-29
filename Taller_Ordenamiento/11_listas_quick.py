# Programa que opera con listas.

import random as r

A = []

for i in range(0, 100):  # Definición de la lista A con números aleatorios.
    num = r.randint(0, 10000)
    A.append(num)

print()
print("Lista A: ", A)

B = []

for i in range(0, 60):  # Definición de la lista B con números aleatorios.
    num = r.randint(0, 10000)
    B.append(num)

print()
print("Lista B: ", B)

def quickSort(lista):  # Función que ordena las listas por el método quickSort.
    if len(lista) < 2:
        return lista
    izquierda = []
    derecha = []
    centro = []  # Siempre será una lista de un solo elemento.
    for i in lista:
        pivote = lista[len(lista)//2]
        if i < pivote:
            izquierda.append(i)
        elif i == pivote:
            centro.append(pivote)
        else:
            derecha.append(i)
    return quickSort(izquierda) + centro + quickSort(derecha)

# Tarea 1: Ordenar A y B.
print()
A = quickSort(A)
print("Lista A ordenada:", A)
print()
B = quickSort(B)
print("Lista B ordenada:", B)

# Tarea 2: Crear a C como la unión de A y B.
print()
C = A
C.extend(B)
print("Lista C (A U B):", C)

# Tarea 3: Ordenar a C y visualizar.
print()
C = quickSort(C)
print("Lista C ordenada: ", C)