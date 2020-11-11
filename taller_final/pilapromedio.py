# Programa que busca el promedio de los elementos de una pila en un solo recorrido.

import os  # Para estética del menú.

class Node:  # Creación de clase Nodo.

    #O(1)
    def __init__(self, data):
        self.data = data
        self.next = None

    #O(n)
    def __str__(self):
        return "[" + str(self.data) + "] -> " + str(self.next)

class LinkedStack:  # Creación de la clase Pila.

    #O(1)
    def __init__(self):
        self.head = None

    #O(n)
    def __str__(self):
        return str(self.head)

    #O(n)
    def length(self):
        current = self.head 
        if current is not None:
            count = 1

            while current.next is not None: 
                count += 1
                current = current.next
            return count  
        else: 
            return 0

    #O(1)
    def isEmpty(self): 
        if self.head == None: 
            return True
        else: 
            return False

    #O(1)
    def peek(self):
        if not self.isEmpty():
            return self.head

    #O(1)
    def push(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            new_node = Node(item)  # Crea un nodo.
            new_node.next = self.head
            self.head = new_node

    #O(1)
    def pop(self):
        if not self.isEmpty():
            aux = self.head
            self.head = self.head.next
            aux.next = None
            return aux.data
        return None

#O(1)
def push(stack):
    os.system("cls")
    n = int(input("Ingrese el número a apilar: "))
    stack.push(n)
    os.system("cls")
    print("Hecho\n")
    os.system("pause")
    return stack

#O(1)
def pop(stack):
    os.system("cls")
    stack.pop()
    print("Hecho\n")
    os.system("pause")
    return stack

#O(n)
def imprimir(stack):
    os.system("cls")
    print(stack)
    print("\nHecho\n")
    os.system("pause")
    return stack

#O(1)
def salir(stack):
    os.system("cls")
    print("Fin del programa.\n")
    os.system("pause")
    return stack

#O(n)
def stack_average(stack):
    os.system("cls")
    if stack.isEmpty() == False:
        node = stack.head
        sum = node.data
        while node.next != None:
            node = node.next
            sum += node.data
        prom = sum/stack.length()
        print("El promedio es %.2f...\n" % prom)
    else:
        print("La pila no tiene elementos, el promedio es 0...\n")
    os.system("pause")
    return stack

#O(n)
def default(stack):
    os.system("cls")
    print("Opción inválida. Intente de nuevo.")
    os.system("pause")
    return stack

def menu(stack):
    switcher = {
        1: push,
        2: pop,
        3: imprimir,
        4: stack_average,
        5: salir
    }
    case = 0
    while True:
        while case < 1 or case > 5:
            os.system("cls")
            print("======MENÚ DE PILA======")
            print()
            print("1. Añadir un número a la pila.")
            print("2. Borrar el último número apilado.")
            print("3. Imprimir la pila.")
            print("4. Encontrar el promedio de los números de la pila.")
            print("5. Terminar.")
            print()
            try:
                case = int(input())
            except(ValueError):
                case = 3
                print()
                print("Opción inválida. Intente de nuevo")
                print()
                os.system("pause")
        func = switcher.get(case, lambda: default)
        stack = func(stack)
        if case == 5:
            break
        case = 0
    pass
    

if __name__ == '__main__':
    stack = LinkedStack()
    menu(stack)