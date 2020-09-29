# Programa que implementa una clase matriz y define si tiene determinado objeto.

# Función que realiza la búsqueda de un elemento en una lista ordenada.
def busqueda_binaria(lista, valor):
    encontrado = False
    izquierda = 0
    derecha = len(lista)
    while not encontrado and izquierda < derecha:
        mitad = (derecha+izquierda)//2
        if valor == lista[mitad]:
            encontrado = True
            return encontrado
        elif valor > lista[mitad]:
            izquierda = mitad + 1
        else:
            derecha = mitad
    return encontrado

# Improvisación de la clase Matriz.
class Matriz:
    def __init__(self, filas, columnas):  # Constructor predeterminado.
        self.filas = filas
        self.columnas = columnas
        self.elementos = []
        for indice in range(0, filas):
            fila = []
            for indice_2 in range (0, columnas):
                fila.append(0)
            self.elementos.append(fila)

    def cambiar(self, fila, columna, valor):  # Función para asignar un valor en una posición de la matriz.
        self.elementos[fila][columna] = valor

    def añadir_fila(self):  # Función para añadir una fila nueva.
        fila = []
        for indice in range(0, self.columnas):
                fila.append(0)
        self.elementos.append(fila)
        self.filas += 1

    def añadir_fila(self, fila):  # Función para añadir una fila determinada.
        if len(fila) < self.columnas:
            for indice in range(len(fila), self.columnas):
                fila.append(0)
        self.elementos.append(fila)
        self.filas += 1

    def añadir_columna(self):  # Función para añadir una columna nueva.
        for indice in range(0, self.filas):
            self.elementos[indice].append(0)
        self.columnas += 1

    def añadir_columna(self, columna):  # Función para añadir una columna determinada.
        for indice in range(0, len(columna)):
            self.elementos[indice].append(columna[indice])
        if len(columna) < self.filas:
            for indice in range(len(columna), self.filas):
                self.elementos[indice].append(0)
        self.columnas += 1

    def eliminar_fila(self):  # Función para eliminar la última fila.
        self.elementos.pop()
        self.filas -= 1

    def eliminar_fila(self, indice):  # Función para eliminar una fila determinada.
        self.elementos.pop(indice)
        self.filas -= 1

    def eliminar_columna(self):  # Función para eliminar la última columna.
        for indice in range(0, self.filas):
            self.elementos[indice].pop()
        self.columnas -= 1

    def eliminar_columna(self, indice):  # Función para eliminar una columna determinada.
        for indice in range(0, self.filas):
            self.elementos[indice].pop(indice)
        self.columnas -= 1

    def ordenar_matriz(self):  # Función para ordenar las filas de las matrices y a ellas mismas de forma ascendente.
        for fila in self.elementos:
            fila.sort()
        self.elementos.sort(key = lambda columna: fila[0])
    
    def buscar_elemento(self, elemento):  # Función que determina si un elemento está en la matriz.
        encontrado = False
        for fila in self.elementos:
            encontrado = busqueda_binaria(fila, elemento)
            if encontrado == True:
                return True
        return False

    def imprimir(self):  # Función que imprime la matriz.
        for fila in self.elementos:
            print("|", end=" ")
            for columna in fila:
                print(columna, end = " ")
            print("|")

m = Matriz(4, 6)

m.añadir_fila([1, 2, 2, 2, 3, 4])
m.eliminar_fila(0)
m.añadir_fila([1, 2, 3, 3, 4, 5])
m.eliminar_fila(0)
m.añadir_fila([3, 4, 4, 4, 4, 6])
m.eliminar_fila(0)
m.añadir_fila([4, 5, 6, 7, 8, 9])
m.eliminar_fila(0)

m.imprimir()

print(m.buscar_elemento(7))
print(m.buscar_elemento(0))