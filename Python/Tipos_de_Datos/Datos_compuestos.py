#Indice es la posición comienza desde 0 y ahi se aloja el elemento 1

#Creanado una lista (se puede modificar) []
#lista = ["Eddier Paz", "SENA", True, 1.68]

#Creandao una tupla (no se puede modificar) ()
#tupla = ("Eddier Paz", "SENA", True, 1.68)

#Esto es valido
#lista[3] = "Maquina"

#Esto no es valido
#tupla[3] = "Maquina"
#print (lista[3])


#Creando un conjutno con (set)- no se pueden repeter datos- no se puede modificar los datos pero si el contenido

conjunto = {"Eddier Paz", "SENA", True, 1.68}
#print (conjunto[3]) -> No puede acceder al elemento

#Creando un diccionario ( dict)

# key : value y se separa con comas_ si es un solo dato no hay comas 

Diccionario = {
    "Nombre" : "Eddier Paz",
    "Estudia en" : "SENA",
    "Esta feliz" : True,
    "Cuanto mide" : 1.68,
    "Dato_repetido" : "SENA"
}

print (Diccionario["Estudia en"])

