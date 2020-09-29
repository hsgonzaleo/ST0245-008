# Programa que determina el ganador de una votacion.

def mergeSort(lista):  # Esta función ordena la lista de votos por ID utilizando el ordenamiento por mezcla.
    if len(lista) > 1:
        mid = len(lista) // 2
        midIzq = lista[:mid]
        midDer = lista[mid:]
        mergeSort(midIzq)
        mergeSort(midDer)
        i, j, k = 0, 0, 0
        while i < len(midIzq) and j < len(midDer):
            if midIzq[i] < midDer[j]:
                lista[k] = midIzq[i]
                i = i + 1
            else:
                lista[k] = midDer[j]
                j = j + 1
            k = k + 1
        while i < len(midIzq):
            lista[k] = midIzq[i]
            i = i + 1
            k = k + 1
        while j < len(midDer):
            lista[k] = midDer[j]
            j = j + 1
            k = k + 1
    return lista

def eliminar_duplicado_específico(lista, valor):  # Esta función elimina los votos ya contados.
    i = lista.index(valor)
    igual = True
    while igual and i != len(lista) - 1:
        if lista[i + 1] != valor:
            igual = False
        else:
            lista.pop(i + 1)
    return lista

def votacion(lista):  # Esta función realiza el conteo de votos de cada candidato y retorna el ganador.
    mergeSort(lista)
    ganador = [0, 0]  # Lista de la forma [candidato, votos].
    for candidato in lista:
        votos = lista.count(candidato)
        if votos > ganador[1]:
            ganador = [candidato, votos]
        lista = eliminar_duplicado_específico(lista, candidato)
    return ganador

voto = []

while True:  # Recepción de votos.
    ID = int(input("Ingrese la ID del candidato por el que votará: "))
    if ID < 0:
        break
    voto.append(ID)

print("Lista de votos: ", end = "")
for ID in voto:
    print(ID, end = " ")

ganador = votacion(voto)
print()
print("El ganador de la votación fue el candidato con ID %d, obteniendo %d votos." % (ganador[0], ganador[1]))