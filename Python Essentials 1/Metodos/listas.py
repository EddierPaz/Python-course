#list = lista creamos una lista con list
lista =  list(["Eddier Paz", "Soacha", 22])

# len devuelve la cantidad de elementos a la lista
cuantos_caracteres = "Eddier Paz"
caracteres = len(cuantos_caracteres)

print(caracteres)
# append  agrega elementos a la lista
agregando_con_append = lista.append("SENA")

# insert agregadno un elemento a la lista en un indice especifico
lista.insert(3, "NOVIA MIA")

# EXTEND agregamos varios elementos a la lista
lista.extend(["Ciudad verde",2003])

# Elimina elementos de la lista por su indice con -1 elimina el ultimo, -2 para el penultimo
lista.pop(-1)

# remove remueve los elementos de la lista por su valor como se llama
lista.remove("Eddier Paz")

#clear elimina todos los elementos de la lista
#lista.clear()

#sort organiza los elementos de forma ascendente solos con numeros( reverse=True lo hace alreves)
#lista.sort()

# inviertiendo los elememtos de una lista al reves
lista.reverse()

# Index Verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista.index("Soacha")

#print (elemento_encontrado)

