# Programa que elimina los números duplicados de una lista.

# Función elimina los números que aparecen nuevamente en la lista de manera secuencial.
def eliminar_dup(lista):  
    i = 0  # Se empieza a recorrer la lista desde la primera posición.
    while i != len(lista) - 1:  # Se comprueba que el elemento no es el último elemento de la lista.
        if lista[i + 1] == lista[i]:  # Se comprueba si el siguiente elemento es un duplicado.
            lista.pop(i + 1)  # Se elimina el duplicado.
        else:
            i += 1  # Se avanza a la siguiente posición de la lista.
    return lista  #Devuelve la lista sin duplicados.

# Inicialización de la lista.
numeros = [] 

# Definición de la lista.
while True:  
    num = int(input("Ingrese un número positivo: "))
    if num < 0:
        break
    numeros.append(num)

# Método para ordenar la lista (no lo tengo en cuenta en el cálculo de complejidad).
numeros.sort()

# Impresión de la lista original.
print("Lista original (ordenada)", numeros)  

# Impresión de la lista sin duplicados.
print("Lista sin duplas:", eliminar_dup(numeros))  