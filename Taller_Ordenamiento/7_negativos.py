# Programa que devuelve una lista con los valores negativos de una lista.

# Función que recorre una lista, retornando una nueva solo con los valores negativos de la original.
def negativos(lista):
    neg = []  # Se crea la nueva lista.
    for i in range(0, len(lista)):  # Se recorre la lista.
        if lista[i] < 0:  # Se comprueba que el valor en la posición i es negativo.
            neg.append(lista[i])  # Se agrega a la nueva lista.
    return neg  # Se retorna la nueva lista.

original = [1, -2, 3, -4, 5, -6, -7, -8, 9, 1, 2, -3]

print("Lista original: ", end = "")
for elemento in original:
    print(elemento, end = " ")

print()

negativos = negativos(original)

print("Números negativos de la lista: ", end = "")
for elemento in negativos:
    print(elemento, end = " ")