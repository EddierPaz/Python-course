# ============================================================
# 3.6 Más sobre Excepciones
# ============================================================
# Las excepciones en Python SON objetos (clases).
# Podemos crear las nuestras, capturar info detallada
# y usar else/finally para controlar el flujo con precisión.
# ============================================================

# --- Ejemplo 1: else y finally en detalle ---
# else  → solo corre si NO hubo excepción en el try.
# finally → SIEMPRE corre, sin importar nada.

print("Ejemplo 1 - else y finally:")

def dividir_seguro(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print(f"  ❌ No se puede dividir {a} entre {b}.")
        return None
    else:
        print(f"  ✅ {a} / {b} = {resultado:.2f}")
        return resultado
    finally:
        print("  🔒 Operación finalizada.\n")

dividir_seguro(10, 2)
dividir_seguro(10, 0)


# --- Ejemplo 2: Las excepciones son clases (capturar con 'as') ---
# Podemos capturar el objeto de excepción y acceder a su información.

print("Ejemplo 2 - Excepciones como objetos:")

try:
    valor = int("no_soy_numero")
except ValueError as e:
    print(f"  Tipo: {type(e).__name__}")  # ValueError
    print(f"  Mensaje: {e}")
    print(f"  Args: {e.args}")

# También podemos capturar la clase padre para agrupar
try:
    lista = [1, 2, 3]
    print(lista[10])
except LookupError as e:
    # IndexError y KeyError son subclases de LookupError
    print(f"  LookupError capturado: {type(e).__name__}: {e}")


# --- Ejemplo 3: Crear jerarquía de excepciones propias ---
# Las excepciones personalizadas son clases que heredan de Exception.
# Podemos crear jerarquías completas para nuestra aplicación.

print("\nEjemplo 3 - Jerarquía de excepciones personalizadas:")

class AppError(Exception):
    """Clase base para errores de nuestra aplicación."""
    pass

class DatabaseError(AppError):
    def __init__(self, tabla, operacion):
        self.tabla = tabla
        self.operacion = operacion
        super().__init__(f"Error en tabla '{tabla}' durante '{operacion}'.")

class ValidationError(AppError):
    def __init__(self, campo, valor):
        super().__init__(f"El campo '{campo}' no acepta el valor '{valor}'.")

def guardar_usuario(nombre, edad):
    if not nombre:
        raise ValidationError("nombre", nombre)
    if not (0 < edad < 150):
        raise ValidationError("edad", edad)
    if nombre == "error_db":
        raise DatabaseError("usuarios", "INSERT")
    print(f"  ✅ Usuario '{nombre}' ({edad} años) guardado.")

for caso in [("Ana", 25), ("", 30), ("Carlos", 200), ("error_db", 40)]:
    try:
        guardar_usuario(*caso)
    except ValidationError as e:
        print(f"  ⚠️  Validación: {e}")
    except DatabaseError as e:
        print(f"  💾 Base de datos: {e}")


# --- Ejemplo 4: Relanzar excepciones con raise ---
# A veces queremos registrar el error y luego relanzarlo.

print("\nEjemplo 4 - Relanzar excepciones (raise):")

def procesar_archivo(nombre):
    try:
        # Simulamos un error de archivo
        if nombre.endswith(".exe"):
            raise PermissionError("Archivos .exe no están permitidos.")
        print(f"  ✅ Procesando: {nombre}")
    except PermissionError as e:
        print(f"  📋 Log: Error registrado → {e}")
        raise   # relanza la misma excepción

archivos = ["datos.csv", "reporte.pdf", "virus.exe"]
for archivo in archivos:
    try:
        procesar_archivo(archivo)
    except PermissionError:
        print(f"  ❌ '{archivo}' fue bloqueado y el error fue propagado.")
