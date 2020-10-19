#Implementación de la clase árbol binario.

import os  # Para acceder a los comanados del Sistema Operativo.

# Implementación de la clase nodo.
class node():  
    def __init__(self, dato):  # Constructor
        self.left = None
        self.right = None
        self.dato = dato

# Implementación de la clase árbol.
class arbol():  
    def __init__(self):  # Constructor.
        self.root = None
        
    def insert(self, a, dato):  # Método para insertar un nodo al árbol.
        if self.buscar(dato, a, 0) != None: # Comprueba si el elemento ya se encuentra (necesario para ser AB).
            print("\nEl elemento ya se encuentra en el árbol...")
        elif a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):  # Impresión In-orden.
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):  # Impresión Pre-orden.
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):  #Impresión Post-orden.
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a, nivel):  # Función que verifica si un elemento se encuentra en el árbol. Regresa el nivel si lo encuentra.
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato, nivel
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left, nivel + 1)
                else:
                    return self.buscar(dato, a.right, nivel + 1)

    def acceder(self, dato, a):  # Función para acceder a un nodo del árbol, dado el elemento. No lo uso en el menú.
        if self.buscar(dato, a, 0) == None:  # Se verifica que exista el nodo.
            return None
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a
            else:
                if dato < a.dato:
                    return self.acceder(dato, a.left)
                else:
                    return self.acceder(dato, a.right)

    def borrar(self, dato, a):  # Función para borrar un nodo del árbol.
        if self.buscar(dato, a, 0) == None:  # Se verifica que exista el nodo.
            print("\nEl elemento no se encuentra en el árbol...")
            return a
        else:
            if dato == a.dato:
                if a.left == None and a.right == None:  # Caso en que se elimine una hoja.
                    a = None
                    return a
                elif a.left == None:  # Caso en que se elimine un padre con un hijo a la derecha.
                    a = a.right
                    return a
                elif a.right == None:  # Caso en que se elimine un padre con un hijo a la izquierda.
                    a = a.left
                    return a
                else:  # Caso en que se elimine un padre con hijos a ambos lados.
                    a = self.reemplazar(a, a.right)  # Se reemplaza el nodo con el dato por el elemento inmediatamente menor, para luego borrarlo.
                    return a

            else:
                if dato < a.dato:
                    a.left = self.borrar(dato, a.left)
                    return a
                else:
                    a.right = self.borrar(dato, a.right)
                    return a

    def reemplazar(self, a, right):  # Fución que elimina un nodo con dos hijos.
        if right.left == None:
            a.dato = right.dato
            a.right = self.borrar(right.dato, a.right)
            return a
        else:
            a = self.reemplazar(a, right.left)
            return a

tree = arbol()  # Creación del árbol.

### MENÚ.
while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Borrar nodo \n7.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root, 0) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root, 0)[0], " si existe. Nivel", tree.buscar(nodo, tree.root, 0)[1],"...")
        else:
            print("\nIngresa solo digitos...")    
    elif opc == '6':
        nodo = input("\nIngresa el nodo a borrar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.borrar(nodo, tree.root)
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '7':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()