# ============================================================
# 2.5 Cuatro Programas Simples
# ============================================================
# Programas concretos que combinan lo aprendido sobre cadenas:
# cifrado César, procesador de números, validador IBAN y más.
# ============================================================

# --- Ejemplo 1: Cifrado César (encriptar) ---
# Desplaza cada letra del alfabeto N posiciones hacia adelante.
# Muy útil para entender ord() y chr() en acción.

def cifrar_cesar(texto, desplazamiento=1):
    resultado = ""
    for char in texto:
        if char.isalpha():
            char = char.upper()
            codigo = ord(char) + desplazamiento
            if codigo > ord('Z'):
                codigo -= 26      # vuelve al inicio del alfabeto
            resultado += chr(codigo)
        # ignora espacios y signos de puntuación
    return resultado

mensaje = "Hola Mundo"
cifrado = cifrar_cesar(mensaje)
print("Ejemplo 1 - Cifrado César:")
print("Original:", mensaje)
print("Cifrado :", cifrado)   # IPMB NVPEP (cada letra +1)


# --- Ejemplo 2: Cifrado César (descifrar) ---
# La operación inversa: resta el desplazamiento.

def descifrar_cesar(texto, desplazamiento=1):
    resultado = ""
    for char in texto:
        if char.isalpha():
            char = char.upper()
            codigo = ord(char) - desplazamiento
            if codigo < ord('A'):
                codigo += 26
            resultado += chr(codigo)
    return resultado

print("\nEjemplo 2 - Descifrado César:")
criptograma = cifrar_cesar("Python es genial", 3)
print("Cifrado  :", criptograma)
print("Descifrado:", descifrar_cesar(criptograma, 3))


# --- Ejemplo 3: Procesador de números en texto ---
# Toma una línea con números separados por espacios y los suma.

def procesar_numeros(linea):
    partes = linea.split()
    total = 0
    for parte in partes:
        try:
            total += float(parte)
        except ValueError:
            print(f"  ⚠️  '{parte}' no es un número válido, se omite.")
    return total

print("\nEjemplo 3 - Procesador de números:")
linea1 = "10 20.5 30 15.5"
linea2 = "5 hola 10 mundo 20"
print(f"Suma de '{linea1}':", procesar_numeros(linea1))   # 76.0
print(f"Suma de '{linea2}':", procesar_numeros(linea2))   # 35.0


# --- Ejemplo 4: Validador simplificado de formato de correo ---
# Comprueba si una cadena tiene la forma básica de un correo electrónico.

def es_correo_valido(correo):
    correo = correo.strip()
    if '@' not in correo:
        return False
    partes = correo.split('@')
    if len(partes) != 2:
        return False
    usuario, dominio = partes
    if not usuario or not dominio:
        return False
    if '.' not in dominio:
        return False
    return True

print("\nEjemplo 4 - Validador de correo:")
correos = [
    "usuario@ejemplo.com",
    "sin_arroba_ejemplo.com",
    "@sinusuario.com",
    "doble@@arroba.com",
    "correcto@dominio.org",
]
for c in correos:
    estado = "✅ Válido" if es_correo_valido(c) else "❌ Inválido"
    print(f"  {estado}: {c}")
