# Trabajo Práctico N°3 - Estructuras condicionales
# Alumna: Camila Castaño


# Ejercicio 1: Mayor de edad
# Este programa pide la edad y verifica si es mayor de 18.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# Ejercicio 2: Nota
# Este programa pide una nota y evalúa si está aprobado.

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3: Número par
# Verifica si el número ingresado es par.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4 - Categorías de edad
# Clasifica la edad ingresada en niño, adolescente, adulto joven o adulto.

edad = int(input("Ejercicio 4 - Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# Ejercicio 5 - Longitud de contraseña
# Verifica si la contraseña tiene entre 8 y 14 caracteres.

contraseña = input("Ejercicio 5 - Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6 - Sesgo estadístico
# Calcula media, mediana y moda de una lista aleatoria y determina el sesgo.

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Ejercicio 6 - Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")


# Ejercicio 7 - String que termina en vocal
# Si termina en vocal, añade un signo de exclamación al final.

texto = input("Ejercicio 7 - Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)


# Ejercicio 8 - Transformación del nombre
# Transforma el nombre ingresado según la opción 1, 2 o 3.

nombre = input("Ejercicio 8 - Ingrese su nombre: ")
opcion = int(input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


# Ejercicio 9 - Clasificación de terremoto
# Clasifica la magnitud según la escala de Richter.

magnitud = float(input("Ejercicio 9 - Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# Ejercicio 10 - Estaciones del año según hemisferio, mes y día
# Este ejercicio determina la estación del año en base al día, mes y hemisferio.

hemisferio = input("Ejercicio 10 - ¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Transformamos mes y día en un solo número para comparar fechas fácilmente
fecha = mes * 100 + dia

if hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print("Estación:", estacion)
