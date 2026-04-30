# ============================================================
# 2.3 Métodos de Cadenas
# ============================================================
# Python incluye muchos métodos listos para usar sobre cadenas.
# Todos devuelven una NUEVA cadena (las originales no cambian).
# ============================================================

# --- Ejemplo 1: Métodos de transformación de mayúsculas/minúsculas ---

print("Ejemplo 1 - Cambios de capitalización:")
texto = "hola MUNDO desde Python"

print(texto.upper())        # HOLA MUNDO DESDE PYTHON
print(texto.lower())        # hola mundo desde python
print(texto.capitalize())   # Hola mundo desde python  (solo 1ra letra)
print(texto.title())        # Hola Mundo Desde Python  (cada palabra)
print(texto.swapcase())     # HOLA mundo DESDE pYTHON  (invierte)


# --- Ejemplo 2: Métodos de búsqueda ---
# find() busca una subcadena y devuelve su índice (-1 si no existe).
# count() cuenta cuántas veces aparece.

print("\nEjemplo 2 - Búsqueda dentro de cadenas:")
oracion = "el elefante elegante come en el estanque"

print("Posición de 'ele':", oracion.find('ele'))        # 3
print("Posición de 'xyz':", oracion.find('xyz'))        # -1 (no existe)
print("Cuántas veces 'el':", oracion.count('el'))       # 5
print("Empieza con 'el':", oracion.startswith('el'))    # True
print("Termina con 'que':", oracion.endswith('que'))    # True


# --- Ejemplo 3: Métodos de limpieza y reemplazo ---
# strip() quita espacios (o caracteres) al inicio y al final.
# replace() reemplaza una subcadena por otra.

print("\nEjemplo 3 - Limpieza y reemplazo:")
sucio = "   ¡Hola, mundo!   "
print(repr(sucio.strip()))         # '¡Hola, mundo!'
print(repr(sucio.lstrip()))        # '¡Hola, mundo!   '
print(repr(sucio.rstrip()))        # '   ¡Hola, mundo!'

original = "Me gusta el café con café"
print(original.replace("café", "té"))   # Me gusta el té con té
print(original.replace("café", "té", 1))  # Solo reemplaza la 1ra aparición


# --- Ejemplo 4: split() y join() ---
# split() divide una cadena en una lista de partes.
# join() hace lo contrario: une una lista en una cadena.

print("\nEjemplo 4 - split() y join():")
csv = "manzana,pera,uva,naranja"
frutas = csv.split(',')
print("Lista:", frutas)            # ['manzana', 'pera', 'uva', 'naranja']
print("Elemento 2:", frutas[2])   # uva

# Reunir la lista con otro separador
print(" - ".join(frutas))         # manzana - pera - uva - naranja
print(" | ".join(frutas))         # manzana | pera | uva | naranja

# Dividir por espacios (por defecto)
frase = "Python es genial"
palabras = frase.split()
print(palabras)                   # ['Python', 'es', 'genial']
