# Trabajo Práctico 4: Estructuras Repetitivas
# Alumna: Camila Castaño


# Ejercicio 1
# Imprimir los números del 0 al 100 en orden creciente

for i in range(101):
    print(i)


# Ejercicio 2
# Contar la cantidad de dígitos de un número ingresado por el usuario

numero = int(input("Ejercicio 2 - Ingresá un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("Cantidad de dígitos:", cantidad_digitos)


# Ejercicio 3
# Sumar los enteros entre dos valores, excluyéndolos

a = int(input("Ejercicio 3 - Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("Suma de los números entre ambos (excluidos):", suma)


# Ejercicio 4
# Sumar números hasta que el usuario ingrese 0

suma = 0
while True:
    n = int(input("Ejercicio 4 - Ingresá un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
print("Suma total:", suma)


# Ejercicio 5
# Juego: adivinar un número aleatorio entre 0 y 9

import random
secreto = random.randint(0, 9)
intentos = 0
acertado = False

while not acertado:
    intento = int(input("Ejercicio 5 - Adiviná el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        acertado = True

print("¡Correcto! Lo lograste en", intentos, "intento(s).")


# Ejercicio 6
# Imprimir los números pares entre 0 y 100 en orden decreciente

for i in range(100, -1, -2):
    print(i)


# Ejercicio 7
# Sumar todos los números desde 0 hasta un número positivo ingresado

limite = int(input("Ejercicio 7 - Ingresá un número positivo: "))
suma = 0
for i in range(limite + 1):
    suma += i
print("Suma total desde 0 hasta", limite, ":", suma)


# Ejercicio 8
# Ingresar 100 números y contar pares, impares, positivos y negativos

cantidad = 100  # cambiar este valor a uno menor para pruebas
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input(f"Ejercicio 8 - Ingresá el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)


# Ejercicio 9
# Ingresar 100 números y calcular la media

cantidad = 100  # cambiar este valor a uno menor para pruebas
suma = 0

for i in range(cantidad):
    num = int(input(f"Ejercicio 9 - Ingresá el número {i+1}: "))
    suma += num

media = suma / cantidad
print("Media de los números ingresados:", media)


# Ejercicio 10
# Invertir los dígitos de un número ingresado

numero = int(input("Ejercicio 10 - Ingresá un número para invertir: "))
invertido = int(str(abs(numero))[::-1])
if numero < 0:
    invertido = -invertido
print("Número invertido:", invertido)
