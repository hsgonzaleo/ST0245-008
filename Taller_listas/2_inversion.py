# Programa que invierte el orden de una lista.

def inversion(lista):
    lista = lista[::-1]
    return lista

lista_de_strings = []

for indice in range (1, 6):
    lista_de_strings.append(str(input("Ingrese el string número %d: " % indice)))

print("Lista original:", lista_de_strings)
print("Lista invertida:", inversion(lista_de_strings))