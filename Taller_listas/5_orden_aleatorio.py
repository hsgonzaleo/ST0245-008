# Programa que ordena una lista de numeros aleatorios.

import random as r

lista_de_numeros = []

for indice in range(0, 10):
    lista_de_numeros.append(r.randint(1, 100))

print("Lista generada:", lista_de_numeros)

lista_de_numeros.sort()

print("Lista ordenada:", lista_de_numeros)