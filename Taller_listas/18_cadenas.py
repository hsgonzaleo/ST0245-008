# Programa que maneja un menú de cadenas.

cadenas = []

while True:  ## Lectura de datos.
    cadena = str(input("Ingrese una cadena (o * para terminar): "))
    if cadena == "*":
        break
    cadenas.append(cadena)

def contar(lista):
    cadena = str(input("Ingrese la cadena a contar en la lista: "))
    print("El número de veces que %s aparece en la lista es:" % cadena, lista.count(cadena))
    print()

def modificar_cadena(lista):
    cadena = str(input("Ingrese la cadena a modificar en la lista: "))
    nueva = str(input("Ingrese la cadena por la que la va a modificar: "))
    for cad in lista:
        if cad == cadena:
            lista[lista.index(cadena)] = nueva
    print("Hecho.")
    print()

def eliminar(lista):
    cadena = str(input("Ingrese la cadena a eliminar de la lista: "))
    lista.remove(cadena)
    print("Hecho.")
    print()

def mostrar(lista):
    print("Lista: ", end = "")
    for cadena in lista:
        print(cadena, end = " ")
    print()

def terminar(lista):
    print("Fin del programa.")

def default(lista):
    print("Opción inválida. Intente de nuevo.")

def switch(case, lista):
    switcher = {
        1: contar,
        2: modificar_cadena,
        3: eliminar,
        4: mostrar,
        5: terminar
    }
    func = switcher.get(case, lambda: "default")
    return func(lista)

def menu():
    print("Seleccione una opción.")
    print()
    print("1. Contar una cadena.")
    print("2. Modificar una cadena.")
    print("3. Eliminar una cadena.")
    print("4. Mostrar la lista de cadenas.")
    print("5. Terminar.")
    print()

menu()
case = int(input("Seleccione una opción: "))
switch(case, cadenas)
while case != 5:
    menu()
    case = int(input("Seleccione una opción: "))
    switch(case, cadenas)