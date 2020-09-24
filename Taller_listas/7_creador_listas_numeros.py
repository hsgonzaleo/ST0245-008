# Programa que crea listas de números.

lista_1, lista_2, lista_3 = [], [], []

for numero in range(1, 6):
    lista_1.append(int(input("Ingrese el entero número %d de la lista 1: " % numero)))
    lista_2.append(int(input("Ingrese el entero número %d de la lista 2: " % numero)))
    lista_3.append(lista_1[numero - 1] + lista_2[numero - 1])

print("Lista 1: ", lista_1)
print("Lista 2: ", lista_2)
print("Lista 3 (Lista 1 + Lista 2): ", lista_3)