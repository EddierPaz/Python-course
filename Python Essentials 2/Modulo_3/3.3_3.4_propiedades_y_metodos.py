# ============================================================
# 3.3 POO: Propiedades
# 3.4 POO: Métodos
# ============================================================
# Las propiedades son los DATOS del objeto.
# Los métodos son las ACCIONES que el objeto puede hacer.
# Juntos forman la base de cualquier clase bien diseñada.
# ============================================================

# --- Ejemplo 1: Variables de clase vs variables de instancia ---
# Las variables de CLASE son compartidas por todos los objetos.
# Las variables de INSTANCIA son únicas para cada objeto.

print("Ejemplo 1 - Clase vs Instancia:")

class Estudiante:
    escuela = "Instituto Python"   # variable de clase (compartida)
    total_estudiantes = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre       # variable de instancia (única)
        self.nota = nota
        Estudiante.total_estudiantes += 1

e1 = Estudiante("Carlos", 8.5)
e2 = Estudiante("Laura", 9.0)
e3 = Estudiante("Pedro", 7.0)

print(f"  Escuela de Carlos: {e1.escuela}")  # Instituto Python
print(f"  Escuela de Laura : {e2.escuela}")  # Instituto Python (misma)
print(f"  Total estudiantes: {Estudiante.total_estudiantes}")  # 3
print(f"  Nota de Carlos: {e1.nota}")        # 8.5 (propia de e1)


# --- Ejemplo 2: Métodos especiales __str__ y __repr__ ---
# __str__ define cómo se ve el objeto cuando se imprime.
# __repr__ define la representación técnica del objeto.

print("\nEjemplo 2 - Métodos especiales __str__:")

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio}, {self.stock})"

p = Producto("Teclado", 49.99, 15)
print(p)         # usa __str__
print(repr(p))   # usa __repr__

productos = [Producto("Mouse", 25.0, 30), Producto("Monitor", 299.99, 5)]
for prod in productos:
    print(f"  {prod}")


# --- Ejemplo 3: Métodos de instancia, de clase y estáticos ---
# @classmethod recibe la clase (cls) en lugar del objeto.
# @staticmethod no recibe ni self ni cls, es una función auxiliar.

print("\nEjemplo 3 - Tipos de métodos:")

class Temperatura:
    unidad_default = "Celsius"

    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):                        # método de instancia
        return f"{self.valor}° {Temperatura.unidad_default}"

    @classmethod
    def cambiar_unidad(cls, nueva_unidad):    # método de clase
        cls.unidad_default = nueva_unidad

    @staticmethod
    def celsius_a_fahrenheit(c):              # método estático
        return c * 9/5 + 32

t = Temperatura(100)
print(f"  {t.mostrar()}")                    # 100° Celsius
Temperatura.cambiar_unidad("Kelvin")
print(f"  {t.mostrar()}")                    # 100° Kelvin
print(f"  100°C en Fahrenheit: {Temperatura.celsius_a_fahrenheit(100)}")  # 212.0


# --- Ejemplo 4: Introspección con hasattr, getattr, setattr ---
# Python permite explorar y modificar objetos en tiempo de ejecución.

print("\nEjemplo 4 - Introspección de objetos:")

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

carro = Vehiculo("Toyota", "Corolla", 2022)

# Verificar si un atributo existe
print("  ¿Tiene 'marca'?:", hasattr(carro, 'marca'))       # True
print("  ¿Tiene 'color'?:", hasattr(carro, 'color'))       # False

# Obtener atributo dinámicamente
atributo = "modelo"
print(f"  {atributo}:", getattr(carro, atributo))          # Corolla

# Agregar atributo en tiempo de ejecución
setattr(carro, 'color', 'azul')
print("  Color agregado:", carro.color)                    # azul

# Listar todos los atributos de instancia
print("  Atributos:", vars(carro))
