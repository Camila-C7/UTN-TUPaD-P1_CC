# Trabajo Práctico 5: Funciones
# Alumna: Camila Castaño


# Ejercicio 1
# Imprime un mensaje fijo por pantalla

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Ejercicio 2
# Devuelve un saludo personalizado

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))


# Ejercicio 3
# Muestra la información ingresada por el usuario

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4
# Calcula área y perímetro de un círculo

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


# Ejercicio 5
# Convierte segundos a horas

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese cantidad de segundos: "))
print(f"Horas equivalentes: {segundos_a_horas(segundos):.2f}")


# Ejercicio 6
# Imprime la tabla del número ingresado

def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Ejercicio 7
# Realiza operaciones básicas con dos números

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "No se puede dividir por 0")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")


# Ejercicio 8
# Calcula el índice de masa corporal (IMC)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")


# Ejercicio 9
# Convierte Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}°F")


# Ejercicio 10
# Calcula el promedio de tres números

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es: {promedio:.2f}")
