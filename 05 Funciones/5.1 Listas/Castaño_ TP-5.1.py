# Trabajo Práctico 5: Listas
# Alumna: Camila Castaño


# Ejercicio 1
# Crear una lista con números del 1 al 100 que sean múltiplos de 4

multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1:", multiplos_de_4)


# Ejercicio 2
# Mostrar el penúltimo elemento de una lista personalizada

gustos = ["chocolate", "música", "viajar", "leer", "gatos"]
print("Ejercicio 2 - Penúltimo elemento:", gustos[-2])


# Ejercicio 3
# Crear lista vacía, agregar 3 palabras con append

palabras = []
palabras.append("sol")
palabras.append("luna")
palabras.append("estrella")
print("Ejercicio 3:", palabras)


# Ejercicio 4
# Reemplazar segundo y último valor de la lista animales

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Ejercicio 4:", animales)


# Ejercicio 5
# Elimina el valor máximo de una lista

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina 22
print("Ejercicio 5:", numeros)


# Ejercicio 6
# Crear lista del 10 al 30 de 5 en 5 y mostrar los 2 primeros

lista = list(range(10, 31, 5))
print("Ejercicio 6 - Dos primeros elementos:", lista[:2])


# Ejercicio 7
# Reemplazar los valores centrales en la lista autos

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["chevrolet", "fiat"]
print("Ejercicio 7:", autos)


# Ejercicio 8
# Crear lista "dobles" con el doble de 5, 10 y 15 usando append

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)


# Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Cambiar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan"
compras[0].remove("pan")

print("Ejercicio 9:", compras)


# Ejercicio 10
# Crear lista anidada con valores específicos

lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Ejercicio 10:", lista_anidada)
