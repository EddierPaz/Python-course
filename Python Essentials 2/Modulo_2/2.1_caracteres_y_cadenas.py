# ============================================================
# 2.1 Caracteres y Cadenas versus las Computadoras
# ============================================================
# Las computadoras almacenan los caracteres como números.
# Python usa UNICODE internamente, lo que permite trabajar
# con casi cualquier alfabeto del mundo.
# ============================================================

# --- Ejemplo 1: Punto de código de un carácter (ord) ---
# ord() devuelve el número (punto de código) que representa a un carácter.

letra = 'A'
print("Ejemplo 1 - Punto de código de 'A':", ord(letra))   # 65
print("Punto de código de 'a':", ord('a'))                  # 97
print("Punto de código de ' ':", ord(' '))                  # 32
# Las mayúsculas siempre tienen un punto de código menor que las minúsculas.


# --- Ejemplo 2: De número a carácter (chr) ---
# chr() hace lo contrario: dado un número, devuelve el carácter.

numero = 65
print("\nEjemplo 2 - Carácter del código 65:", chr(numero))   # A
print("Carácter del código 97:", chr(97))                     # a
print("Carácter del código 9786:", chr(9786))                 # ☺ (UNICODE)
# UNICODE permite representar miles de caracteres especiales y emojis.


# --- Ejemplo 3: Recorrer el alfabeto con puntos de código ---
# Podemos construir el alfabeto completo usando ord() y chr() en un bucle.

print("\nEjemplo 3 - Alfabeto en mayúsculas:")
for codigo in range(ord('A'), ord('Z') + 1):
    print(chr(codigo), end=' ')
print()  # salto de línea al final
# Salida: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


# --- Ejemplo 4: Comparando caracteres por su punto de código ---
# Python compara caracteres usando sus valores numéricos (puntos de código).

print("\nEjemplo 4 - Comparación de caracteres:")
print("'A' < 'a':", 'A' < 'a')   # True  → 65 < 97
print("'Z' < 'a':", 'Z' < 'a')   # True  → 90 < 97
print("'b' > 'a':", 'b' > 'a')   # True  → 98 > 97
print("'1' < 'A':", '1' < 'A')   # True  → 49 < 65
# Entender esto es clave para ordenar cadenas correctamente.
