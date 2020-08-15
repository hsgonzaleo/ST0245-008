# Este programa determina si una palabra o frase dada por el usuario es un palíndromo (Ejercicio 5).
palabra = str(input("Ingrese una palabra o frase: "))

def invertir(palabra):
    if len(palabra) == 1:  # Caso base.
        return palabra
    else:
        return palabra[len(palabra) - 1] + invertir(palabra[:len(palabra) - 1])

if palabra == invertir(palabra):
    print(palabra, "es un palíndromo.")
else:
    print(palabra, "no es un palíndromo")