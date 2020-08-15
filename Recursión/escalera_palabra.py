# Este programa imprime todas las subcadenas que inician con el inicio de una cadena (Ejercicio 4).
palabra = str(input("Ingrese una palabra o frase: "))

def esc_palabra(palabra):
    if len(palabra) == 1:  # Caso base.
        print (palabra)
    else:
        esc_palabra(palabra[:len(palabra) - 1])
        print (palabra)

print("Impresión: ")
esc_palabra(palabra)