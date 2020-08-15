# Este programa invierte una palabra o frase que asigna el usuario (Ejercicio 3).
palabra = str(input("Ingrese una palabra o frase: "))

def invertir(palabra):
    if len(palabra) == 1:  # Caso base.
        return palabra
    else:
        return palabra[len(palabra) - 1] + invertir(palabra[:len(palabra) - 1])

print("Inversión: ", invertir(palabra))