# Programa que elimina los números duplicados de una lista.

# Función que busca el índice de la primera aparición de cada número y lo elimina en las posiciones siguientes.
def eliminar_dup(lista):
    for num in lista:
        i = lista.index(num)  # Primera aparición del número.
        while i != len(lista) - 1 and num in lista[i + 1:]:  # Comprueba si el número se repite en la lista.
            lista.pop(i + lista[i + 1:].index(num) + 1)  # Elimina el duplicado.
    return lista  # Devuelve la lista sin duplicados.

# Inicialización de la lista.
numeros = []  

# Definición de la lista.
while True:  
    num = int(input("Ingrese un número positivo: "))
    if num < 0:
        break
    numeros.append(num)

# Impresión de la lista original.
print("Lista original", numeros)  

# Impresión de la lista sin duplicados.
print("Lista sin duplas:", eliminar_dup(numeros))  