diccionario = {
    "nombre": "Eddier",
    "apellido": "Paz",
    "edad" : 22
}

# keys devuelves las claves 
claves = diccionario.keys()

# get devuelve el valor si no esta el valor arroja None osea no encuentra el valor
claves1 = diccionario.get("nombre")

#clear eliminando todo lo del diccionario 
#diccionario.clear()

# pop elimina un elemento del diccionario 
diccionario.pop("edad")

#items devuelve exacto el diccionario dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)