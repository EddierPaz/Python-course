# ============================================================
# 4.4 El Módulo os
# ============================================================
# El módulo 'os' permite interactuar con el sistema operativo:
# navegar directorios, crear/eliminar carpetas, obtener rutas.
# ============================================================

import os

# --- Ejemplo 1: Información del sistema y directorio actual ---
print("Ejemplo 1 - Información del sistema:")
print("  Sistema operativo:", os.name)
print("  Directorio actual:", os.getcwd())
contenido = os.listdir('.')
print(f"  Elementos en directorio actual: {len(contenido)}")


# --- Ejemplo 2: Crear y eliminar directorios ---
print("\nEjemplo 2 - Crear y eliminar directorios:")

os.mkdir("temp_dir")
print("  Creado 'temp_dir':", os.path.exists("temp_dir"))

os.makedirs("temp_dir/sub1/sub2")
print("  Subdirectorios anidados creados.")

os.rmdir("temp_dir/sub1/sub2")
os.rmdir("temp_dir/sub1")
os.rmdir("temp_dir")
print("  Eliminados. Existe?:", os.path.exists("temp_dir"))


# --- Ejemplo 3: Trabajar con rutas (os.path) ---
print("\nEjemplo 3 - os.path:")

ruta = "/home/usuario/documentos/archivo.txt"
print("  Directorio:", os.path.dirname(ruta))
print("  Nombre archivo:", os.path.basename(ruta))
print("  Extension:", os.path.splitext(ruta)[1])

ruta_segura = os.path.join("carpeta", "subcarpeta", "archivo.py")
print("  Ruta construida:", ruta_segura)

print("  Existe '.'?:", os.path.exists('.'))
print("  Es directorio?:", os.path.isdir('.'))


# --- Ejemplo 4: Renombrar y estadísticas de archivos ---
print("\nEjemplo 4 - Renombrar y estadísticas:")

with open("prueba_original.txt", 'w') as f:
    f.write("Contenido de prueba\n" * 5)

info = os.stat("prueba_original.txt")
print(f"  Tamaño: {info.st_size} bytes")

os.rename("prueba_original.txt", "prueba_renombrada.txt")
print("  Renombrado correctamente.")
print("  Original existe?:", os.path.exists("prueba_original.txt"))
print("  Nuevo existe?:", os.path.exists("prueba_renombrada.txt"))

os.remove("prueba_renombrada.txt")
print("  Archivo eliminado.")
