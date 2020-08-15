### Este programa determina el número de pasos mínimo para resolver el juego de las torres
# de Hanoi utilizando un algoritmo recursivo e ilustra el proceso (Ejercicio 7).

class cont:  # Contador de pasos utilizados.
    c = 0

class pilas:  # Clase que da un formato a las torres de Hanoi.
    def __init__(self, a, o, d):  # Constructor
        self.o = o
        self.a = a
        self.d = d
    
    def imprimir(self):  # Método que imprime las torres de Hanoi.
        print("O", o, "A", a, "D", d)

def hanoi(n, o, a, d, cont, pilas):  # Algoritmo recursivo para solucionar el juego.
    if n == 1:  # Caso base.
        d.append(o.pop())
        cont.c += 1
        pilas.imprimir()
    else:
        hanoi(n-1, o, d, a, cont, pilas)
        d.append(o.pop())
        cont.c += 1
        pilas.imprimir()
        hanoi(n-1, a, o, d, cont, pilas)

### Programa principal.
print("------------------TORRES DE HANOI-----------------------")
print()
n = int(input("Ingrese el número de discos a utilizar: "))
o = []
a = []
d = []
c = cont()
for i in range(0, n):  # Inicialización de la primera torre.
    o.append(i)
p = pilas(o, a, d)
print()
print("O", o, "A", a, "D", d)  # Impresión del primer momento.
hanoi(n, o, a, d, c, p)  # Llamada al algoritmo de solución.
print()
print("El número de pasos utilizados fue: ", c.c)  # Conclusión.