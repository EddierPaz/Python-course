#Creando una funcion simple
#def = "Es para definir una funcion"
def saludar():
    print("Hola Eddier")
saludar()

#Creando una funcion con parametros
def saludarr(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else :
        adjetivo = "crack"

    print(f"Hola {nombre}, mi {adjetivo} ¿Como estas?")
saludarr("Eddier Paz","HOMBRE")

#Crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars="abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num

password = crear_contraseña_random(5)
frase = f"Tu contraseña nueva es: {password}"
print(frase)

