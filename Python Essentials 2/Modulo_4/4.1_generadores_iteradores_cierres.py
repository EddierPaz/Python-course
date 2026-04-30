# ============================================================
# 4.1 Generadores, Iteradores y Cierres
# ============================================================
# Los generadores producen valores uno a uno con 'yield',
# ahorrando memoria. Los cierres (closures) "congelan"
# variables del contexto donde fueron creados.
# ============================================================

# --- Ejemplo 1: Iterador con __iter__ y __next__ ---
# Un iterador es un objeto que recuerda dónde quedó.

print("Ejemplo 1 - Iterador manual:")

class Contador:
    def __init__(self, inicio, fin):
        self.__actual = inicio
        self.__fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.__actual > self.__fin:
            raise StopIteration
        valor = self.__actual
        self.__actual += 1
        return valor

for numero in Contador(1, 5):
    print(numero, end=' ')   # 1 2 3 4 5
print()


# --- Ejemplo 2: Generador con yield ---
# yield es como return pero "pausa" la función y recuerda el estado.

print("\nEjemplo 2 - Generador con yield:")

def pares_hasta(n):
    for i in range(0, n + 1, 2):
        yield i    # pausa aquí y entrega el valor

print("Pares hasta 10:", list(pares_hasta(10)))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci (8):", list(fibonacci(8)))   # [0, 1, 1, 2, 3, 5, 8, 13]

# Los generadores son eficientes: no cargan todo en memoria.
gen = pares_hasta(1000000)
print("Primer par:", next(gen))   # 0
print("Segundo par:", next(gen))  # 2


# --- Ejemplo 3: Expresiones lambda, map() y filter() ---
# lambda crea funciones anónimas de una sola expresión.
# map() aplica una función a cada elemento de una lista.
# filter() filtra los elementos según una condición.

print("\nEjemplo 3 - Lambda, map y filter:")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: aplicar función a cada elemento
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

# filter: solo los que cumplen la condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# Combinados
cuadrados_pares = list(map(lambda x: x ** 2,
                           filter(lambda x: x % 2 == 0, numeros)))
print("Cuadrados de pares:", cuadrados_pares)

# Ordenar con lambda como key
palabras = ["banana", "manzana", "kiwi", "pera", "fresa"]
print("Por longitud:", sorted(palabras, key=lambda p: len(p)))


# --- Ejemplo 4: Cierres (closures) ---
# Un cierre es una función interna que recuerda las variables
# del entorno donde fue creada, incluso después de que la
# función externa ya terminó de ejecutarse.

print("\nEjemplo 4 - Cierres (closures):")

def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor   # 'factor' queda "congelado"
    return multiplicar

doble  = crear_multiplicador(2)
triple = crear_multiplicador(3)

print("Doble de 5:", doble(5))    # 10
print("Triple de 5:", triple(5))  # 15
print("Doble de 10:", doble(10))  # 20

# Aplicación práctica: descuentos
def crear_descuento(porcentaje):
    def aplicar(precio):
        return precio * (1 - porcentaje / 100)
    return aplicar

desc_10 = crear_descuento(10)
desc_20 = crear_descuento(20)

print(f"Precio $100 con 10% descuento: ${desc_10(100):.2f}")  # $90.00
print(f"Precio $100 con 20% descuento: ${desc_20(100):.2f}")  # $80.00
