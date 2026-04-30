# 📘 Python Essentials 1 – Fundamentos de Python

> Apuntes y ejemplos prácticos del curso Python Essentials 1.  
> Cada carpeta cubre un tema con ejemplos comentados paso a paso.

---

## 📚 Tabla de Contenidos

- [Variables](#variables)
- [Tipos de Datos](#tipos-de-datos)
- [Operadores](#operadores)
- [Condicionales](#condicionales)
- [Bucles](#bucles)
- [Inputs](#inputs)
- [Funciones](#funciones)
- [Métodos](#métodos)
- [Módulos](#módulos)
- [Ejercicios](#ejercicios)

---

## Variables

Declaración y uso de variables en Python. Una variable guarda un valor en memoria para usarlo después.

```python
nombre = "Eddier Paz"
edad = 20
altura = 1.75
es_estudiante = True

print(nombre, edad, altura, es_estudiante)
```

📁 Carpetas: `Variables/` · `variables_2.0/`

> `variables_2.0/` cubre estructuras más avanzadas: conjuntos, diccionarios y tuplas.

---

## Tipos de Datos

Python maneja distintos tipos: cadenas de texto, números, listas, tuplas, diccionarios y conjuntos.

```python
# Datos simples
texto = "Hola"
entero = 10
decimal = 3.14
booleano = True

# Datos compuestos
lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"nombre": "Eddier", "edad": 20}
conjunto = {1, 2, 3}
```

📁 Carpeta: `Tipos_de_Datos/`

---

## Operadores

Python tiene tres grupos principales de operadores.

```python
# Aritméticos
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.33...
print(10 // 3)  # 3  (division entera)
print(10 % 3)   # 1  (residuo)
print(10 ** 3)  # 1000 (potencia)

# Comparación
print(10 > 3)   # True
print(10 == 3)  # False

# Lógicos
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

📁 Carpeta: `Operador/`

---

## Condicionales

Permiten ejecutar código según una condición. Se usan `if`, `elif` y `else`.

```python
edad = 18

if edad >= 18:
    print("Es mayor de edad")
elif edad >= 13:
    print("Es adolescente")
else:
    print("Es menor de edad")
```

📁 Carpeta: `Condicionales/`

---

## Bucles

Permiten repetir código mientras una condición se cumpla (`while`) o recorriendo una secuencia (`for`).

```python
# While: se repite mientras la condicion sea True
contador = 1
while contador < 10:
    contador += 1
    print(contador)

# For: recorre cada elemento de una lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

📁 Carpeta: `Bucles/`

> Incluye: `bucle_while.py` · `iterar_listas_y_tuplas.py` · `max_iteraciones.py`

---

## Inputs

Permiten que el usuario ingrese datos desde el teclado. `input()` siempre devuelve una cadena de texto.

```python
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

print(f"Hola {nombre}, tienes {edad} años.")
```

📁 Carpeta: `inputs/`

> Incluye: `input_nombres.py` · `input_numeros.py`

---

## Funciones

Bloques de código reutilizables que reciben parámetros y pueden devolver un resultado.

```python
# Función básica
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Eddier")

# Función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8

# Lambda: función de una sola línea
cuadrado = lambda x: x ** 2
print(cuadrado(4))  # 16
```

📁 Carpetas: `Funciones/` · `funciones_buenas/`

> `Funciones/` incluye: `build_in.py` · `crear_funciones.py` · `funciones_lambda.py` · `parametro_args.py` · `funciones_datos_extras.py`  
> `funciones_buenas/` incluye ejemplos de buenas prácticas.

---

## Métodos

Los métodos son funciones que pertenecen a un tipo de dato. Se usan con la fórmula `dato.metodo()`.

```python
cadena = "Eddier Paz"

print(cadena.upper())           # EDDIER PAZ
print(cadena.lower())           # eddier paz
print(cadena.capitalize())      # Eddier paz
print(cadena.find("P"))         # 7
print(cadena.count("d"))        # 2
print(cadena.replace("az","ez"))# Eddier Pez
print(cadena.split(" "))        # ['Eddier', 'Paz']
print(cadena.startswith("Ed"))  # True
print(cadena.endswith("az"))    # True
print(len(cadena))              # 10

lista = [3, 1, 4, 1, 5]
lista.append(9)    # agrega al final
lista.sort()       # ordena
print(lista)       # [1, 1, 3, 4, 5, 9]
```

📁 Carpeta: `Metodos/`

> Incluye: `Cadena.py` · `Diccionarios.py` · `listas.py`

---

## Módulos

Un módulo es un archivo Python con funciones y variables que podemos importar y reutilizar.

```python
# Importar módulo completo
import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159...

# Importar función específica
from random import randint
numero = randint(1, 10)
print(numero)
```

📁 Carpeta: `Modulos/`

> Incluye: `modulos.py` · `modulo_saludar.py` · `modulos_2.0.py` · `paquete/`

---

## Ejercicios

Ejercicios prácticos para reforzar los temas aprendidos.

| Carpeta | Contenido |
| :--- | :--- |
| `Ejercicio_1/` | `if-else.py` · `Ejercicio_1.1.py` · `Ejercicio_1.2.py` |
| `Ejercicio_2/` | `ejercicio_2.1.py` · `ejercicio_2.2.py` · `ejercicio_2.3.py` |

---

## 👤 Autor

**Eddier Paz**  
[GitHub](https://github.com/EddierPaz)