# ============================================================
# 3.2 Del Enfoque Procedimental al Orientado a Objetos
# ============================================================
# Usamos la PILA (stack) como caso de estudio para comparar
# ambos enfoques y ver por qué la POO es más robusta.
# ============================================================

# --- Ejemplo 1: Pila procedimental (enfoque clásico) ---
# Los datos están expuestos: cualquiera puede modificar la lista.

print("Ejemplo 1 - Pila procedimental:")

pila = []

def push(valor):
    pila.append(valor)

def pop():
    if pila:
        valor = pila[-1]
        del pila[-1]
        return valor
    return None

push(10)
push(20)
push(30)
print("  Pop:", pop())   # 30
print("  Pop:", pop())   # 20

# Problema: alguien puede romper la pila accidentalmente:
pila[0] = 999            # modificación directa permitida
print("  Pila después de modificación directa:", pila)


# --- Ejemplo 2: Pila orientada a objetos (encapsulada) ---
# Los datos están protegidos dentro del objeto.

print("\nEjemplo 2 - Pila orientada a objetos:")

class Stack:
    def __init__(self):
        self.__stack_list = []   # privada

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def is_empty(self):
        return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("  Tamaño:", s.size())   # 3
print("  Pop:", s.pop())       # 30
print("  Pop:", s.pop())       # 20
print("  ¿Vacía?:", s.is_empty())  # False


# --- Ejemplo 3: Múltiples pilas independientes ---
# Una de las grandes ventajas de la POO: cada instancia
# tiene sus propios datos completamente separados.

print("\nEjemplo 3 - Múltiples pilas independientes:")

pila_numeros = Stack()
pila_letras = Stack()

pila_numeros.push(1)
pila_numeros.push(2)
pila_letras.push('a')
pila_letras.push('b')

print("  Números pop:", pila_numeros.pop())  # 2
print("  Letras pop:", pila_letras.pop())    # b
print("  Tamaño números:", pila_numeros.size())  # 1
print("  Tamaño letras:", pila_letras.size())    # 1
# Son completamente independientes entre sí.


# --- Ejemplo 4: Heredar de Stack para crear AddingStack ---
# Herencia: extendemos Stack sin reescribir nada, solo agregamos.

print("\nEjemplo 4 - Herencia: AddingStack:")

class AddingStack(Stack):
    def __init__(self):
        super().__init__()   # inicializa la clase padre
        self.__suma = 0

    def push(self, val):
        self.__suma += val
        super().push(val)   # llama al push del padre

    def pop(self):
        val = super().pop()
        self.__suma -= val
        return val

    def get_sum(self):
        return self.__suma

adding = AddingStack()
adding.push(10)
adding.push(20)
adding.push(30)
print("  Suma acumulada:", adding.get_sum())   # 60
adding.pop()
print("  Suma tras pop:", adding.get_sum())    # 30
