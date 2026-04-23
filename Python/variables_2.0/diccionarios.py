#creando diccionarios dict()

diccionario = dict(nombre="Eddier",apellido="Paz")

#las listas no pueden ser claves y usamos frozenset  para crear conjuntos
diccionario = {("Eddier", "Paz"): "Valentina"}
diccionario = {frozenset(["Eddier","Paz"]): "Valentina"}

#Creando diccionario fromkeys() valor por defecto : none
diccionario = dict.fromkeys (["nombre","apellido"])

#Creando diccionario fromkeys() cambiando el valor por defecto : "No se"
diccionario = dict.fromkeys (["nombre","apellido"], "No se")

print (diccionario)




