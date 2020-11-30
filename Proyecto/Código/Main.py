# Main program

from graphviz import Digraph
import DataManager as dm
import Tree
import pandas as pd
import os

def empezar():
    os.system("cls")
    print("Iniciando...\n")
    os.system("pause")
    lector_de_datos()
    pass

def terminar():
    os.system("cls")
    print("Fin del programa.\n")
    os.system("pause")
    os.system("cls")
    pass

def principal():
    switcher = {
        1: empezar,
        2: terminar
    }
    case = 0
    while True:
        while case < 1 or case > 2:
            os.system("cls")
            print("MENÚ PRINCIPAL.")
            print()
            print("1. Empezar el programa.")
            print("2. Salir del programa.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 3
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: terminar)
        func()
        if case == 2:
            break
        case = 0
    pass

def leer_entrenamiento():
    training, header = dm.read_csv()
    os.system("cls")
    print("Se leyeron", len(training), "datos.\n")
    os.system("pause")
    creador_de_arboles(training, header)
    pass

def leer_arbol():
    os.system("cls")
    tree = Tree.import_tree()
    os.system("cls")
    os.system("pause")
    menu_arbol(tree)
    pass

def volver(tree = None, training = None, header = None):
    os.system("cls")
    print("Regresando...\n")
    os.system("pause")
    pass
    
def lector_de_datos():
    switcher = {
        1: leer_entrenamiento,
        2: leer_arbol,
        3: volver
    }
    case = 0
    while True:
        while case < 1 or case > 3:
            os.system("cls")
            print("Creador de árboles de decisión con algoritmo de Hunt.")
            print()
            print("1. Leer datos de entrenamiento.")
            print("2. Leer un árbol.")
            print("3. Volver al menú anterior.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 4
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: volver)
        func()
        if case == 3:
            break
        case = 0
    pass
    
def imprimir_entrenamiento(training, header):
    os.system("cls")
    print("Imprimiendo...\n")
    os.system("pause")
    os.system("cls")
    for label in header:
        print("\t", label, end=" ")
    print()
    for fila in training:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
    os.system("pause")

def crear_arbol_CART(training, header):
    os.system("cls")
    limit = int(input("Ingrese el nivel de recursión del árbol: "))
    os.system("cls")
    print("Creando árbol...\n")
    C_tree = Tree.CARTTree(training, header, limit)
    os.system("pause")
    menu_arbol(C_tree)
    pass

def crear_arbol_ID3(training, header):
    os.system("cls")
    limit = int(input("Ingrese el nivel de recursión del árbol: "))
    os.system("cls")
    print("Creando árbol...\n")
    I_tree = Tree.ID3Tree(training, header, limit)
    os.system("pause")
    menu_arbol(I_tree)
    pass

def creador_de_arboles(training, header):
    switcher = {
        1: imprimir_entrenamiento,
        2: crear_arbol_CART,
        3: crear_arbol_ID3,
        4: volver
    }
    case = 0
    while True:
        while case < 1 or case > 4:
            os.system("cls")
            print("Creador de árboles de decisión con algoritmo de Hunt.")
            print()
            print("1. Imprimir datos de entrenamiento.")
            print("2. Crear un árbol con algoritmo CART.")
            print("3. Crear un árbol con algoritmo ID3.")
            print("4. Volver al menú anterior.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 5
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: volver)
        func(training, header)
        if case == 4:
            break
        case = 0
    pass


def leer_test(tree):
    testing, header = dm.read_csv()
    os.system("cls")
    print("Se leyeron", len(testing), "datos.\n")
    os.system("pause")
    menu_predicciones(tree, testing, header)
    pass

def imprimir_arbol(tree):
    os.system("cls")
    print("Imprimiendo...\n")
    os.system("pause")
    os.system("cls")
    print(tree)
    print()
    os.system("pause")
    pass

def graficar_arbol(tree):
    os.system("cls")
    try:
        tree.graphic().view()
    except(RuntimeError):
        print(tree.graphic())
        print()
        print("Copiar y pegar este código en webgraphviz.com...")
        print()
    os.system("pause")
    pass

def guardar_arbol(tree):
    os.system("cls")
    g = str(input("Ingrese el nombre del archivo a guardar: "))
    print()
    os.system("pause")
    os.system("cls")
    print("Guardando...\n")
    f = open(g, "w")
    f.write(tree.__str__())
    f.close()
    os.system("pause")
    os.system("cls")
    print("Éxito al guardar.\n")
    os.system("pause")
    pass

def menu_arbol(tree):
    switcher = {
        1: leer_test,
        2: imprimir_arbol,
        3: graficar_arbol,
        4: guardar_arbol,
        5: volver
    }
    case = 0
    while True:
        while case < 1 or case > 5:
            os.system("cls")
            print("Creador de árboles de decisión con algoritmo de Hunt.")
            print()
            print("1. Leer datos de evaluación.")
            print("2. Imprimir el árbol.")
            print("3. Graficar el árbol.")
            print("4. Guardar el árbol.")
            print("5. Volver al menú anterior.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 6
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: volver)
        func(tree)
        if case == 5:
            break
        case = 0
    pass

def imprimir_test(tree, test, header):
    os.system("cls")
    print("Imprimiendo...\n")
    os.system("pause")
    os.system("cls")
    for label in header:
        print("\t", label, end=" ")
    print()
    for fila in test:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
    os.system("pause")
    pass

def imprimir_predicciones(tree, test, header):
    os.system("cls")
    print("Imprimiendo...\n")
    os.system("pause")
    os.system("cls")
    for row in test:
        print ("Actual: %s. Predicted: %s" %
               (row[-1], Tree.print_prediction(Tree.classify(row, tree.root))))
    print()
    os.system("pause")
    pass

def guardar_predicciones(tree, test, header):
    os.system("cls")
    g = str(input("Ingrese el nombre del archivo a guardar: "))
    print()
    os.system("pause")
    os.system("cls")
    print("Guardando...\n")
    f = open(g, "w")
    for row in test:
        f.write("Actual: %s. Predicted: %s" %
               (row[-1], Tree.print_prediction(Tree.classify(row, tree.root))))
        f.write("\n")
    f.close()
    os.system("pause")
    os.system("cls")
    print("Éxito al guardar.\n")
    os.system("pause")
    pass

def imprimir_matriz(tree, test, header):
    os.system("cls")
    M = Tree.error_matrix(test, tree.root)
    columns = ["Positivos", "Negativos"]
    rows = ["Verdaderos", "Falsos"]
    M = pd.DataFrame(M, index = rows, columns = columns)
    print(M)
    print()
    os.system("pause")
    pass

def guardar_matriz(tree, test, header):
    os.system("cls")
    g = str(input("Ingrese el nombre del archivo a guardar: "))
    print()
    os.system("pause")
    os.system("cls")
    print("Guardando...\n")
    M = Tree.error_matrix(test, tree.root)
    columns = ["Positivos", "Negativos"]
    rows = ["Verdaderos", "Falsos"]
    M = pd.DataFrame(M, index = rows, columns = columns)
    f = open(g, "w")
    f.write(str(M))
    f.close()
    os.system("pause")
    os.system("cls")
    print("Éxito al guardar.\n")
    os.system("pause")
    pass

def menu_predicciones(tree, test, header):
    switcher = {
        1: imprimir_test,
        2: imprimir_predicciones,
        3: guardar_predicciones,
        4: imprimir_matriz,
        5: guardar_matriz,
        6: volver
    }
    case = 0
    while True:
        while case < 1 or case > 6:
            os.system("cls")
            print("Creador de árboles de decisión con algoritmo de Hunt.")
            print()
            print("1. Imprimir datos de evaluación.")
            print("2. Imprimir predicciones.")
            print("3. Guardar predicciones.")
            print("4. Imprimir matriz de confusión.")
            print("5. Guardar matriz de confusión.")
            print("6. Volver al menú anterior.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 7
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: volver)
        func(tree, test, header)
        if case == 6:
            break
        case = 0
    pass
        

if __name__ == '__main__':
    principal()
