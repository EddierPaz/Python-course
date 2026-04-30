#Creando una funcion de 3 parametros
def frase(nombre,apellido, adjetivo):
    return f'Hola {nombre}{apellido}, eres muy {adjetivo}.'

#Utlizando keyword arguments
frase_modificada = frase(adjetivo="inteliginte",nombre="Eddier", apellido="Paz")
print(frase_modificada)

#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase1(nombre,apellido, adjetivo="tonto"):
    return f'Hola {nombre}{apellido}, eres muy {adjetivo}.'

frase_modificada1 = frase1("Eddier","Paz","inteligente")
print(frase_modificada1)