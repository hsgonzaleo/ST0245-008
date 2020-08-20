### Este programa retorna un número del triángulo de Pascal dada una fila y una columna

def  pascal(row, column):
     if row < 0 or column < 0:
         return 0
     elif column == 0 or row == column:
         return 1
     else:
         return pascal(row-1, column-1) + pascal(row-1, column)

row = int(input("Ingrese el número de la fila en que se ubica el número a buscar: "))
column = int(input("Ingrese el número de la columna en que se ubica el número a buscar: "))
print("El número en la fila", row, "y la columna", column, "es:", pascal(row, column))
             