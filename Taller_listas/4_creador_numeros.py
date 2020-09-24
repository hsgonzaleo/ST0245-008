# Programa que crea una lista de números hasta que se ingrese un número negativo.

lista_de_numeros = []

parada = False
numero = int(input("Ingrese un numero: "))
while not (numero < 0):
    lista_de_numeros.append(numero)
    numero = int(input("Ingrese un numero: "))

for numero in lista_de_numeros:
    print(numero, " ", end = "")