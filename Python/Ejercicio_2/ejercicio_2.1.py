#Falto el profesor y los alumnos organizaran la clase


#Funcion para obtener al asisitente y el profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista de los compañeros
    compañeros = []
    #Ejecutando un for para pedir la informacin de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero :")
        edad = int(input("Ingrese el edad del compañero: "))
        compañero = (nombre, edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
    #Ordenandolos de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])
    
    #Acceder al nombre de los compañaeros para definir asistente y profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor

#Desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#Mostramos el resultadow
print(f'El profesor es {profesor} y el su asistente es {asistente}')