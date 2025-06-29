# Práctico 7: Estructuras de datos complejas
# Alumna: Camila Castaño


# Ejercicio 1
# Agregar frutas al diccionario

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2
# Actualizar precios

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3
# Lista de frutas sin precios

solo_frutas = list(precios_frutas.keys())
print("Frutas:", solo_frutas)

# Ejercicio 4
# Agenda de contactos

contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

consulta = input("¿Qué contacto desea consultar? ")
if consulta in contactos:
    print("Número:", contactos[consulta])
else:
    print("El contacto no existe.")

# Ejercicio 5
# Contar palabras únicas y frecuencia

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# Ejercicio 6
# Notas de alumnos

alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# Ejercicio 7
# Aprobados en parciales

parcial1 = {"Ana", "Luis", "Pedro", "María"}
parcial2 = {"Luis", "Pedro", "Lucía"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
todos = parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", todos)

# Ejercicio 8
#  Gestión de stock

stock = {
    "arroz": 10,
    "fideos": 15,
    "azúcar": 5
}
producto = input("Ingrese el producto a consultar: ")
if producto in stock:
    cantidad = int(input("Ingrese unidades a agregar: "))
    stock[producto] += cantidad
else:
    cantidad = int(input("Producto nuevo. Ingrese stock inicial: "))
    stock[producto] = cantidad
print("Stock actualizado:", stock)

# Ejercicio 9
# Agenda con tuplas

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
clave = (dia, hora)
if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad programada.")

# Ejercicio 10
# Invertir diccionario de países y capitales

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)
