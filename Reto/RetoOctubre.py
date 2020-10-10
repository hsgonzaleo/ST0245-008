# Programa que rota los elementos de una lista k veces determinadas por el usuario.

### IMPLEMENTACIÓN.

# Clase Nodo.
class Node:  

    def __init__(self, item):  # Constructor.
        self.item = item
        self.next = None

    def __str__(self):  # Impresión.
        return "[" + str(self.item) + "] -> " + str(self.next)

# Clase Lista Enlazada.
class LinkedList:  

    def __init__(self, head):  # Constructor.
        self.head = head

    def __str__(self):  # Impresión.
        return str(self.head)

    def length(self):  # Método que calcula la longitud de la lista.
        current = self.head 
        if current is not None:
            count = 1

            while current.next is not None: 
                count += 1
                current = current.next
            return count  
        else: 
            return 0

    def insert(self, data, position):  # Método que inserta un elemento en determinada posición de la lista.
        new_node = Node(data)  # Crea un nodo.

        if position == 0:  # Cabeza de la lista.
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def rotate(self, k):  # Método que hace la rotación k veces a la derecha si es negativo, a la izquierda si es positivo. Su complejidad es de O(n).
        if self.head is not None and k != 0:
            len = self.length()
            while k >= len:
                k = k - len
            while k < 0:
                k = len + k
            while k != 0:
                current = self.head
                self.head = current.next
                current.next = None
                self.insert(current.item, len - 1)
                k -= 1
            
"""
###TEST

#Creamos la lista.
linked_list = LinkedList(Node(1))

#Rellenamos la lista.
for i in range(2, 10):
    linked_list.insert(i, i-1)

#Evaluamos algunas salidas.
print("Lista original:", linked_list)
linked_list.rotate(1)
print("Rota 1 a la derecha:", linked_list)
linked_list.rotate(-1)
print("Rota 1 a la izquierda:", linked_list)
linked_list.rotate(10)
print("Rota 10 a la derecha:", linked_list)
linked_list.rotate(-10)
print("Rota 10 a la izquierda:", linked_list)
linked_list.rotate(5)
print("Rota 5 a la derecha:", linked_list)
"""

### PROGRAMA PRINCIPAL.

linked_list = LinkedList(None)
i = int(input("Ingrese un número positivo a incluir en la lista: "))
while i >= 0:
    linked_list.insert(i, 0)
    i = int(input("Ingrese un número positivo a incluir en la lista: "))
print("Esta es su lista: ", linked_list)
cont = (1 == int(input("¿Desea rotar la lista? (0. No, 1. Sí) ")))
while cont:
    i = int(input("Ingrese el número de veces a rotar la lista (negativo a la derecha, positivo a la izquierda): "))
    linked_list.rotate(i)
    print("Lista: ", linked_list)
    cont = (1 == int(input("¿Desea rotar la lista? (0. No, 1. Sí) ")))
print("Fin del programa")
