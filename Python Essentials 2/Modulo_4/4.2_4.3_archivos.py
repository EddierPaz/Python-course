# ============================================================
# 4.2 Archivos – Flujos y Procesamiento
# 4.3 Trabajando con Archivos Reales
# ============================================================
# Python maneja archivos mediante streams (flujos).
# open() abre el archivo y devuelve un objeto stream.
# Siempre hay que cerrar el archivo (o usar 'with').
# ============================================================

import os

# --- Ejemplo 1: Escribir y leer un archivo de texto ---
# Modo 'w'  → escritura (crea o sobreescribe).
# Modo 'r'  → lectura.
# 'with' cierra el archivo automáticamente al salir del bloque.

print("Ejemplo 1 - Escribir y leer archivo de texto:")

nombre_archivo = "ejemplo_2.txt"

# Escritura
with open(nombre_archivo, 'w', encoding='utf-8') as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea\n")
print("  ✅ Archivo escrito.")

# Lectura completa
with open(nombre_archivo, 'r', encoding='utf-8') as f:
    contenido = f.read()
print("  Contenido completo:")
print(contenido)


# --- Ejemplo 2: readline() y readlines() ---
# readline() lee una línea a la vez.
# readlines() devuelve una lista con todas las líneas.

print("Ejemplo 2 - readline y readlines:")

with open(nombre_archivo, 'r', encoding='utf-8') as f:
    primera = f.readline()
    print("  Primera línea:", repr(primera))   # incluye '\n'

with open(nombre_archivo, 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    print("  Todas las líneas:")
    for i, linea in enumerate(lineas, 1):
        print(f"    [{i}] {linea.strip()}")


# --- Ejemplo 3: Modo de apertura 'a' (adjuntar) ---
# Modo 'a' → agrega al final sin borrar el contenido existente.

print("\nEjemplo 3 - Modo adjuntar 'a':")

with open(nombre_archivo, 'a', encoding='utf-8') as f:
    f.write("Cuarta línea (agregada)\n")
    f.write("Quinta línea (agregada)\n")

with open(nombre_archivo, 'r', encoding='utf-8') as f:
    for linea in f:
        print(" ", linea.strip())


# --- Ejemplo 4: Manejo de errores con try/except al abrir archivos ---
# FileNotFoundError si el archivo no existe en modo 'r'.
# IOError es la clase base para errores de entrada/salida.

print("\nEjemplo 4 - Manejo de errores con archivos:")

archivos = ["ejemplo_2.txt", "no_existe.txt", "tampoco.csv"]

for nombre in archivos:
    try:
        with open(nombre, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            print(f"  ✅ '{nombre}': {len(lineas)} líneas.")
    except FileNotFoundError:
        print(f"  ❌ '{nombre}': archivo no encontrado.")
    except PermissionError:
        print(f"  ❌ '{nombre}': sin permisos de lectura.")

# Limpieza del archivo de ejemplo
os.remove(nombre_archivo)
print(f"\n  🗑️  '{nombre_archivo}' eliminado.")
