# ============================================================
# 2.2 La Naturaleza de las Cadenas en Python
# ============================================================
# Las cadenas son secuencias INMUTABLES de caracteres.
# Podemos indexarlas, recortarlas, concatenarlas y replicarlas,
# pero no podemos modificar un carácter directamente.
# ============================================================

# --- Ejemplo 1: Longitud, indexación y recorrido ---
# len() nos dice cuántos caracteres tiene una cadena.
# Podemos acceder a cada carácter usando su índice (desde 0).

frase = "Python"
print("Ejemplo 1 - Longitud e indexación:")
print("Longitud de 'Python':", len(frase))      # 6
print("Primer carácter:", frase[0])             # P
print("Último carácter:", frase[-1])            # n

print("Recorriendo carácter por carácter:")
for caracter in frase:
    print(caracter, end='-')
print()  # salida: P-y-t-h-o-n-


# --- Ejemplo 2: Cadenas multilínea y carácter \n ---
# Las triple comillas permiten escribir cadenas que ocupan varias líneas.

print("\nEjemplo 2 - Cadenas multilínea:")
poema = """Línea uno,
Línea dos,
Línea tres."""
print(poema)
print("Longitud del texto:", len(poema))
# El salto de línea \n cuenta como UN carácter.


# --- Ejemplo 3: Concatenación y replicación ---
# + une cadenas, * las repite.

print("\nEjemplo 3 - Concatenación y replicación:")
saludo = "Hola" + ", " + "mundo"
print(saludo)                       # Hola, mundo

separador = "-" * 20
print(separador)                    # --------------------

# Ejemplo práctico: construir una cadena con un bucle
resultado = ""
for i in range(1, 6):
    resultado += str(i) + " "
print("Números concatenados:", resultado)  # 1 2 3 4 5


# --- Ejemplo 4: Rebanadas (slices) ---
# Con [inicio:fin:paso] extraemos partes de una cadena.

print("\nEjemplo 4 - Rebanadas:")
palabra = "programacion"
print("Primeras 7 letras:", palabra[:7])        # program
print("Desde la letra 7:", palabra[7:])         # acion
print("Cada 2 letras:", palabra[::2])           # pgaain
print("Al revés:", palabra[::-1])               # noicamargorp
print("Letras 3 a 6:", palabra[3:7])            # gram
