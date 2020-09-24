# Programa que devuelve cuadrados y cubos aleatorios.

import random as r

lista_de_numeros = []

for indice in range(0, 10):
    lista_de_numeros.append(r.randint(1, 10))

for numero in lista_de_numeros:
    print("Elemento: {} Cuadrado: {} Cubo: {}".format(numero, numero**2, numero**3))