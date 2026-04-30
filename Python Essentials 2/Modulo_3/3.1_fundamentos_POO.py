# ============================================================
# 3.1 Los Fundamentos de la POO
# ============================================================
# La Programación Orientada a Objetos une código y datos en
# unidades llamadas OBJETOS, creados a partir de CLASES.
# Pilares: Encapsulamiento, Herencia, Polimorfismo.
# ============================================================

# --- Ejemplo 1: Tu primera clase y objeto ---
# Una clase es el molde. El objeto es la instancia real.

print("Ejemplo 1 - Primera clase y objeto:")

class Perro:
    pass   # clase vacía por ahora

mi_perro = Perro()   # instanciación
print("Tipo:", type(mi_perro))          # <class '__main__.Perro'>
print("Es instancia de Perro:", isinstance(mi_perro, Perro))  # True

# Podemos agregar atributos al vuelo (aunque no es la forma recomendada)
mi_perro.nombre = "Rex"
mi_perro.edad = 3
print(f"Nombre: {mi_perro.nombre}, Edad: {mi_perro.edad}")


# --- Ejemplo 2: Constructor __init__ y atributos ---
# __init__ se ejecuta automáticamente al crear cada objeto.
# self representa al objeto recién creado.

print("\nEjemplo 2 - Constructor y atributos:")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # atributo de instancia
        self.edad = edad

    def presentarse(self):
        print(f"  Hola, soy {self.nombre} y tengo {self.edad} años.")

p1 = Persona("Ana", 30)
p2 = Persona("Luis", 25)

p1.presentarse()   # Hola, soy Ana y tengo 30 años.
p2.presentarse()   # Hola, soy Luis y tengo 25 años.
print("¿Comparten datos?", p1.nombre == p2.nombre)  # False


# --- Ejemplo 3: Jerarquía de clases y herencia ---
# Una subclase hereda todos los métodos y atributos de la superclase.

print("\nEjemplo 3 - Herencia:")

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Gato(Animal):
    def hablar(self):
        return "Miau"

class Pato(Animal):
    def hablar(self):
        return "Cuac"

animales = [Gato("Misi"), Pato("Donald"), Gato("Tom")]
for a in animales:
    print(f"  {a.nombre} dice: {a.hablar()}")
# Cada objeto sabe cómo hablar según su clase.


# --- Ejemplo 4: Encapsulamiento con atributos privados ---
# Dos guiones bajos al inicio hacen el atributo "privado".
# Solo se puede acceder desde dentro de la clase.

print("\nEjemplo 4 - Encapsulamiento:")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial   # privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"  Depósito de {monto}. Nuevo saldo: {self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"  Retiro de {monto}. Nuevo saldo: {self.__saldo}")
        else:
            print("  ❌ Saldo insuficiente.")

    def ver_saldo(self):
        print(f"  Saldo de {self.titular}: {self.__saldo}")

cuenta = CuentaBancaria("María", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.ver_saldo()

# Intento de acceso directo (fallará):
try:
    print(cuenta.__saldo)
except AttributeError:
    print("  ❌ No se puede acceder a __saldo desde afuera.")
