# ============================================================
# 2.7 La Anatomía de las Excepciones
# 2.8 Excepciones Útiles
# ============================================================
# Python tiene 63 excepciones integradas en jerarquía de árbol.
# Conocerlas nos ayuda a escribir código más robusto.
# ============================================================

# --- Ejemplo 1: Jerarquía de excepciones más comunes ---
# Todas las excepciones heredan de BaseException.
# Las más usadas heredan de Exception.

print("Ejemplo 1 - Verificando jerarquía de excepciones:")
print("¿ZeroDivisionError es ArithmeticError?:",
      issubclass(ZeroDivisionError, ArithmeticError))   # True
print("¿IndexError es LookupError?:",
      issubclass(IndexError, LookupError))              # True
print("¿ValueError es Exception?:",
      issubclass(ValueError, Exception))                # True
print("¿Exception es BaseException?:",
      issubclass(Exception, BaseException))             # True


# --- Ejemplo 2: Excepciones más comunes en acción ---
# Vemos cuándo se lanza cada una de las más frecuentes.

print("\nEjemplo 2 - Excepciones comunes:")

casos = [
    ("IndexError",       lambda: [1, 2, 3][10]),
    ("KeyError",         lambda: {"a": 1}["z"]),
    ("ValueError",       lambda: int("no soy número")),
    ("TypeError",        lambda: "texto" + 5),
    ("ZeroDivisionError",lambda: 1 / 0),
    ("AttributeError",   lambda: "texto".volar()),
]

for nombre, caso in casos:
    try:
        caso()
    except Exception as e:
        print(f"  {nombre}: {e}")


# --- Ejemplo 3: OverflowError e ImportError ---
# OverflowError: número demasiado grande para float.
# ImportError: módulo que no existe.

print("\nEjemplo 3 - OverflowError e ImportError:")
import math

try:
    x = 1.0
    for _ in range(1000):
        x *= 10
except OverflowError:
    print("  OverflowError: el número se salió del rango de float.")

try:
    import modulo_magico_inexistente
except ImportError as e:
    print(f"  ImportError: {e}")


# --- Ejemplo 4: Crear tu propia excepción ---
# Extendemos la clase Exception para crear errores personalizados.
# Muy útil para dar mensajes claros en nuestras aplicaciones.

print("\nEjemplo 4 - Excepción personalizada:")

class EdadInvalidaError(Exception):
    def __init__(self, edad):
        self.edad = edad
        super().__init__(f"La edad {edad} no es válida. Debe estar entre 0 y 120.")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes {saldo}, intentas retirar {monto}.")

def registrar_usuario(nombre, edad):
    if not (0 <= edad <= 120):
        raise EdadInvalidaError(edad)
    print(f"  ✅ Usuario '{nombre}' registrado con edad {edad}.")

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto

# Pruebas
try:
    registrar_usuario("Ana", 25)
    registrar_usuario("Bot", 999)
except EdadInvalidaError as e:
    print(f"  ❌ {e}")

try:
    nuevo_saldo = retirar(100, 200)
except SaldoInsuficienteError as e:
    print(f"  ❌ {e}")
