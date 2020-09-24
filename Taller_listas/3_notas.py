# Programa que muestra las notas de un estudiante, su nota menor, su nota mayor y su promedio.

def reporte(notas):
    print("Promedio: %.1f" % (sum(notas)/len(notas)))
    print("Nota mayor: %.1f" % max(notas))
    print("Nota menor: %.1f" % min(notas))
    pass

notas = []

for indice in range (1, 6):
    while True:
        nota = float(input("Ingrese la nota número %d: " % indice))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            break

print("Notas:", notas)
reporte(notas)