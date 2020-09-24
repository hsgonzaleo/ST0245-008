# Programa que borra elementos duplicados de las listas.

numeros = []

while True:  ## Lectura de datos.
    num = int(input("Ingrese un número positivo: "))
    if num < 0:
        break
    numeros.append(num)

print("Lista original:", numeros)

for num in numeros:
    i = numeros.index(num)
    while i != len(numeros) - 1 and num in numeros[i + 1:]:
        numeros.pop(i + numeros[i + 1:].index(num) + 1)

print("Lista sin duplas:", numeros)