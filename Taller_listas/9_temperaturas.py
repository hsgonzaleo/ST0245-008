# Programa que da informes de temperatura.

temperaturas = []

for indice in range (0, 5):
    temperatura = []
    temperatura.append(float(input("Ingrese la máxima temperatura del día %d: " % (indice + 1))))
    while True:
        temperatura.append(float(input("Ingrese la mínima temperatura del día %d: " % (indice + 1))))
        if temperatura[1] > temperatura[0]:
            temperatura.pop()
            print("Error: Temperatura mínima mayor a la máxima. Intente de nuevo.")
        else:
            temperaturas.append(temperatura)
            break

print("Temperaturas Medias.")
print("====================")

indice = 1
temp_min = temperaturas[0][1]

for temperatura in temperaturas:
    print("Día %d. Temperatura media: %.2f" % (indice, sum(temperatura)/len(temperatura)))
    indice += 1
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]

print()
print("Temperaturas Menores.")
print("====================")

indice = 1
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print("Día %d." % indice)
    indice += 1

print()
temp_max = float(input("Ingrese la temperatura máxima del día a buscar: "))
existe_temp = False
print()
print("Temperaturas Mayores.")
print("====================")

indice = 1
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print("Día %d." % indice)
        existe_temp = True
    indice += 1

if existe_temp == False:
    print("Ningún día tiene esa temperatura máxima.")