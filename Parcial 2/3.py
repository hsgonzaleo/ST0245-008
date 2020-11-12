# Programa que devuelve el recorrido postorden de un arbol binario dado el inorden y el preorden

def postorden(preorden, inorden):  # Algoritmo recursivo
    if preorden == "" or inorden == "":  # Caso especial: el árbol no tiene raíz.
        return ""
    if len(preorden) == 1 or len(inorden) == 1:  # Caso base: el árbol solo tiene un elemento.
        return preorden or inorden
    post = ""
    inorden_izq = ""
    inorden_der = ""
    preorden_izq = ""
    preorden_der = ""
    i = 0
    while inorden[i] != preorden[0]:  # Se toma como raíz al primer elemento del preorden. Se obtiene el inorden y el preorden del sub-árbol izquierdo, y luego el derecho.
        inorden_izq = inorden_izq + inorden[i]
        i += 1
    i += 1
    while i < len(inorden):
        inorden_der = inorden_der + inorden[i]
        i += 1
    i = 0
    for char in preorden:  # Se obtiene el preorden a partir de los elementos que hay en el preorden original y los elementos del inorden de los sub-árboles
        if char in inorden_izq:
            preorden_izq = preorden_izq + char
        if char in inorden_der:
            preorden_der = preorden_der + char
    post = post + postorden(preorden_izq, inorden_izq) + postorden(preorden_der, inorden_der) + preorden[0]  # Se retorna los elementos ordenados en post-orden (primero lado izquierdo, luego lado derecho y finalmente raíz).
    return post

print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))  # Prueba con el ejercicio.
