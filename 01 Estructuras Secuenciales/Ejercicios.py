# Ejercicio 1
print ("Hola Mundo")

# Ejercicio 2
nombre= input("¿Cual es tu nombre?")
print (f"Hola {nombre}!")

# Ejercicio 3
nombre= input("¿Cual es tu nombre?")
apellido=  input("¿Cual es tu apellido?")
edad=  input("¿Cuantos años tienes?")
pais=  input("¿En donde vives?")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

# Ejercicio 4
import math
radio= float(input("Ingresa el radio de tu circulo: "))
area= math.pi * radio
perimetro=  2 * math.pi * radio 
print (f"El area del circulo es {area}")
print(f"El perimetro del circulo es {perimetro}")

# Ejercicio 5
segundos= int(input("Ingresa una cantidad de segundos:"))
horas= segundos / 3600 
print(f" {segundos} segundos equivalen a {horas} horas")

# Ejercicio 6
numero= int(input ("Ingresa un numero: "))
print(f"Tabla de multiplicar de {numero}")
for i in range (1,11):
    print (f" {numero} x {i}= {numero * i}")

# Ejercicio 7
num1= int(input("Ingresa el primer numero (distinto de 0):"))
num2= int(input ("Ingresa el segundo numero (distinto de 0): "))
suma= num1+num2
resta= num1-num2
multiplicacion= num1*num2
division= num1/num2 
print (f"Suma: {suma}")
print (f"Resta: {resta}")
print (f"Multiplicacion: {multiplicacion}")
print (f"Division: {division}")

# Ejercicio 8
peso= float (input("Ingresa tu peso en kilogramos: "))
altura= float(input("Ingresa tu altura en metros: "))
imc= peso / (altura ** 2)
print (f"Tu IMC es {imc}")

# Ejercicio 9
celcius= float (input ("Ingresa la temperatura en grados celcius: "))
fahrenheit= (9/5) * celcius + 32
print (f"{celcius} °C equivale a {fahrenheit}°F ")

# Ejercicio 10
n1= float (input("Ingresa el primer numero: "))
n2= float (input("Ingresa el segundo numero: "))
n3= float (input("Ingresa el tercer numero: "))
promedio= (n1+n2+n3) / 3
print (F"El promedio es {promedio}")
