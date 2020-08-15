# Este programa determina el máximo común divisor de dos números a y b (Ejercicio 1).
a = int(input("Ingrese un entero a: "))
b = int(input("Ingrese un entero b: "))

def mcd(a, b):
    if (b > a):  # Ajuste del número mayor.
        t = b
        b = a
        a = t
    if (a%b == 0):  # Caso base.
        return b
    else:
        return mcd(b, a%b)

print("El máximo común divisor de a y b es: ", mcd(a, b))