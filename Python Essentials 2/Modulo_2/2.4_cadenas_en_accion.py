# ============================================================
# 2.4 Cadenas en Acción
# ============================================================
# Aquí vemos cómo comparar cadenas, ordenarlas y convertirlas
# hacia y desde números.
# ============================================================

# --- Ejemplo 1: Comparación de cadenas ---
# Python compara cadenas carácter por carácter usando sus puntos de código.
# Las mayúsculas van ANTES que las minúsculas.

print("Ejemplo 1 - Comparación de cadenas:")
print("'apple' == 'apple':", 'apple' == 'apple')   # True
print("'apple' == 'Apple':", 'apple' == 'Apple')   # False (distinto código)
print("'banana' > 'apple':", 'banana' > 'apple')   # True  (b > a)
print("'abc' < 'abd':", 'abc' < 'abd')             # True  (c < d)

# Comparación útil: verificar si una cadena está en rango alfabético
nombre = "carlos"
print("¿Nombre entre 'a' y 'm'?:", 'a' <= nombre[0] <= 'm')  # True


# --- Ejemplo 2: Ordenando listas de cadenas ---
# sorted() devuelve una lista nueva ordenada.
# sort() ordena la lista original en su lugar.

print("\nEjemplo 2 - Ordenamiento de cadenas:")
animales = ["zebra", "elefante", "ardilla", "ballena", "cocodrilo"]

ordenados = sorted(animales)
print("sorted():", ordenados)   # orden alfabético

# Ordenar ignorando mayúsculas/minúsculas
ciudades = ["Madrid", "bogotá", "Lima", "caracas", "Buenos Aires"]
print("Sin key:", sorted(ciudades))
print("Con key=str.lower:", sorted(ciudades, key=str.lower))

animales.sort()
print("sort() in-place:", animales)


# --- Ejemplo 3: Convertir número a cadena y cadena a número ---
# str() convierte a cadena. int() y float() convierten desde cadena.

print("\nEjemplo 3 - Conversiones entre cadenas y números:")
numero = 42
como_cadena = str(numero)
print("Número a cadena:", como_cadena, type(como_cadena))

precio_texto = "19.99"
precio = float(precio_texto)
print("Cadena a float:", precio, type(precio))

edad_texto = "25"
edad = int(edad_texto)
print("Cadena a int:", edad + 5)   # 30

# Ejemplo práctico: sumar números ingresados como texto
numeros_texto = "10 20 30 40 50"
total = sum(int(n) for n in numeros_texto.split())
print("Suma:", total)              # 150


# --- Ejemplo 4: in y not in con cadenas ---
# Verificamos si una subcadena existe dentro de otra.

print("\nEjemplo 4 - Operadores in y not in:")
correo = "usuario@ejemplo.com"

print("¿Tiene '@'?:", '@' in correo)             # True
print("¿Tiene '.com'?:", '.com' in correo)       # True
print("¿Tiene '.org'?:", '.org' not in correo)   # True

# Filtrar palabras que contienen una vocal específica
palabras = ["casa", "libro", "puerta", "techo", "árbol"]
con_u = [p for p in palabras if 'u' in p]
print("Palabras con 'u':", con_u)                # ['puerta']
