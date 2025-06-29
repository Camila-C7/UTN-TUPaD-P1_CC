# Trabajo Práctico 11: Aplicación de la Recursividad
# Alumna: Camila Castaño 

# Ejercicio 1
# Calcula el factorial de un número y lo muestra desde 1 hasta el número ingresado

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("Ingrese un número para calcular factoriales hasta ese valor: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")


# Ejercicio 2
# Calcula el valor de Fibonacci en una posición y muestra la serie completa hasta esa posición

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese hasta qué posición mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


# Ejercicio 3
# Calcula la potencia de un número de forma recursiva

def potencia(base, exponente):
    if exponente == 0:
        return 1
