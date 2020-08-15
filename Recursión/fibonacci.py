# Este programa determina el número enésimo de la serie Fibonacci (Ejercicio 6).

def fib(n):  # Caso base.
    if (n<=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

m = int(input("Ingrese un número: "))
print("El valor del número", m, "de la serie Fibonacci es:", fib(m))