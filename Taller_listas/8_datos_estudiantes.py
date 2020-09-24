# Programa que almacena datos de estudiantes en listas.

nombres, edades = [], []

while True:  ## Lectura de datos.
    nombre = str(input("Ingrese el nombre de un estudiante: "))
    if nombre == "*":
        break
    nombres.append(nombre)
    edad = int(input("Ingrese la edad del estudiante: "))
    edades.append(edad)

mayor_edad = max(edades)
mayores_de_edad = []
estudiantes_mayores = []

print("Alumnos mayores de edad")
print("=======================")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)

print()

print("Alumnos mayores (%d años)" % mayor_edad)
print("=========================")
for nombre, edad in zip(nombres, edades):
    if edad == mayor_edad:
        print(nombre)