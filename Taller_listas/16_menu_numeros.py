# Programa que crea un menú para trabajar con números.

def añadir(lista):
    lista.append(int(input("Ingrese el número a añadir a la lista: ")))
    print("Hecho.")

def añadir_pos(lista):
    pos = int(input("Ingrese la posición en que va a a añadir un número: "))
    if pos <= len(lista):
        lista.insert(pos - 1, int(input("Ingrese el número a añadir en la posición %d: " % pos)))
        print("Hecho.")
    else:
        print("La posición ingresada no se encuentra en la lista.")

def length(lista):
    print("El número de elementos de la lista es de:", len(lista))

def borrar(lista):
    print("Se eliminó el último elemento que era:", lista.pop())

def remover(lista):
    pos = int(input("Ingrese la posición del número a eliminar: "))
    if pos <= len(lista):
        print("Se eliminó el elemento de la posición %d que era:" % pos, lista.pop(pos - 1))
    else:
        print("La posición ingresada no se encuentra en la lista.")

def contar(lista):
    num = int(input("Ingrese el número a contar en la lista: "))
    print("El número de veces que %d aparece en la lista es:" % num, lista.count(num))

def posiciones(lista):
    num = int(input("Ingrese el número a buscar en la lista: "))
    if num in lista:
        print("%d aparece en la lista en las posiciones: " % num, end="")
        i = 0
        while i < len(lista) and num in lista[i:]:
            i = i + lista[i:].index(num) + 1
            print(i, end = " ")
        print()
    else:
        print("%d no se encuentra en la lista." % num)

def imprimir(lista):
    print("Lista: ", end = "")
    for numero in lista:
        print(numero, end = " ")
    print()

def salir(lista):
    print("Fin del programa.")

def default(lista):
    print("Opción inválida. Intente de nuevo.")

def switch(case, lista):
    switcher = {
        1: añadir,
        2: añadir_pos,
        3: length,
        4: borrar,
        5: remover,
        6: contar,
        7: posiciones,
        8: imprimir,
        9: salir
    }
    func = switcher.get(case, lambda: default)
    return func(lista)

def menu():
    print("======MENÚ DE NÚMEROS======")
    print()
    print("1. Añadir un número a la lista.")
    print("2. Añadir un número a la lista en una posición específica.")
    print("3. Consultar el tamaño de la lista.")
    print("4. Borrar el último elemento de la lista.")
    print("5. Borrar un elemento de la lista en una posición específica.")
    print("6. Contar duplicados de un número en la lista.")
    print("7. Hallar las posiciones en que se encuentra un número de la lista.")
    print("8. Imprimir la lista.")
    print("9. Salir del programa.")
    print()

lista = []
menu()
case = int(input("Seleccione una opción: "))
switch(case, lista)
while case != 9:
    menu()
    case = int(input("Seleccione una opción: "))
    switch(case, lista)