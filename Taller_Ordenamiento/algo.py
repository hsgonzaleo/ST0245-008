# Programa que elimina los números duplicados de una lista.

def mergeSort(lista):
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

