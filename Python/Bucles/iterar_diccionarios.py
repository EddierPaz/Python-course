
diccionario = {
    "Nombre": "Eddier",
    "Apellido": "Paz",
    "Edad": 22
}

#Recorriendo diccionario para obtener claves
for key in diccionario:
    print(f"la clave es: {key}")

#Recorriendo diccionario con items() para obtener las claves y el valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")
