# Revisando ordenamiento de tuplas.

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), 
(3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  
(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), 
(18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

print("Lista desordenada: ", end = "")
for tupla in futbolistasTup:
    print(tupla, end = " ")

futbolistasTup.sort(key = lambda futbolista: futbolista[0])

print()

print("Lista ordenada: ", end = "")
for tupla in futbolistasTup:
    print(tupla, end = " ")

lista1 = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]

print()

print("Lista 1 desordenada: ", end = "")
for elemento in lista1:
    print(elemento, end = " ")

lista1.sort()

print()

print("Lista 1 ordenada: ", end = "")
for elemento in lista1:
    print(elemento, end = " ")

lista2 = [47, 3, 21, 32, 56, 92]

print()

print("Lista 2 desordenada: ", end = "")
for elemento in lista2:
    print(elemento, end = " ")

lista2.sort()

print()

print("Lista 2 ordenada: ", end = "")
for elemento in lista2:
    print(elemento, end = " ")

lista3 = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]

print()

print("Lista 3 desordenada: ", end = "")
for elemento in lista3:
    print(elemento, end = " ")

lista3.sort()

print()

print("Lista 3 ordenada: ", end = "")
for elemento in lista3:
    print(elemento, end = " ")