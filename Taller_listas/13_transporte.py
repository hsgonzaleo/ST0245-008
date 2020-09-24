# Programa que calcula el total de kilómetros que recorren los conductores.

Días = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
Nombres, Kms = [], []

Fin = False

while not Fin:
    nombre = str(input("Ingrese el nombre de un conductor (o * si terminó): "))
    if nombre == "*":
        break
    else:
        Nombres.append(nombre)
    kms = []
    for dia in Días:
        km = int(input("Ingrese el total de kilómetros que %s recorrió el %s: " % (nombre, dia)))
        kms.append(km)
    Kms.append(kms)

Total_kms = []

for kms in Kms:
    Total_kms.append(sum(kms))

print("--Kilómetros recorridos por conductor--")

for nombre, kms in zip(Nombres, Total_kms):
    print("{}: {} km.".format(nombre, kms))