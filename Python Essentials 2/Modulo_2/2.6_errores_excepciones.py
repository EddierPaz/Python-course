# ============================================================
# 2.6 Errores – El Pan Diario del Programador
# ============================================================
# Las excepciones son eventos que interrumpen el flujo normal
# del programa. Con try/except podemos manejarlas con gracia.
# ============================================================

# --- Ejemplo 1: try / except básico ---
# Sin manejo de excepciones el programa se detiene abruptamente.
# Con try/except lo controlamos nosotros.

print("Ejemplo 1 - try/except básico:")

# Sin manejo (esto crashearía):
# print(10 / 0)

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("  ❌ No se puede dividir entre cero.")

try:
    numero = int("abc")
except ValueError:
    print("  ❌ 'abc' no puede convertirse a entero.")

print("  ✅ El programa continúa ejecutándose.")


# --- Ejemplo 2: Capturar múltiples excepciones ---
# Un bloque try puede tener varios except para distintos errores.

print("\nEjemplo 2 - Múltiples except:")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"
    except TypeError:
        return "Error: los argumentos deben ser números"

print(dividir(10, 2))       # 5.0
print(dividir(10, 0))       # Error: división entre cero
print(dividir(10, "dos"))   # Error: los argumentos deben ser números


# --- Ejemplo 3: Capturar el objeto excepción con 'as' ---
# Podemos obtener información detallada sobre el error.

print("\nEjemplo 3 - Capturar información del error:")

datos = [10, 0, "hola", 5]
for valor in datos:
    try:
        resultado = 100 / valor
        print(f"  100 / {valor} = {resultado:.2f}")
    except ZeroDivisionError as e:
        print(f"  ⚠️  División imposible: {e}")
    except TypeError as e:
        print(f"  ⚠️  Tipo incorrecto con '{valor}': {e}")


# --- Ejemplo 4: else y finally ---
# else: se ejecuta si NO hubo excepción.
# finally: se ejecuta SIEMPRE, haya o no excepción.

print("\nEjemplo 4 - else y finally:")

def abrir_recurso(valor):
    print(f"  Intentando procesar: {valor}")
    try:
        resultado = 100 / valor
    except ZeroDivisionError:
        print("  ❌ Error: división entre cero.")
    else:
        print(f"  ✅ Resultado: {resultado:.2f}")
    finally:
        print("  🔒 Limpieza completada (finally siempre corre).")
    print()

abrir_recurso(4)
abrir_recurso(0)
