# Este programa calcula la potencia de un número x a la n-sima potencia (Ejercicio 2).
x = int(input("Ingrese la base de la potencia: "))
n = int(input("Ingrese el exponente de la potencia: "))

def potencia(x, n):
    if n == 0:  # Caso base.
        return 1
    elif n > 0:
        return x * potencia(x, n - 1)

print("El resultado de elevar ", x, " a la ", n, " es: ", potencia(x,n))