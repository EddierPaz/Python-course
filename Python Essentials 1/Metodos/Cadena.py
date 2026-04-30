#Formula dato.metodo()

cadena1 = "Eddier Paz"
cadena2 = "Siempre con Dios"

#upper la convierte todo a mayuscula

resultado = cadena1.upper()
print (resultado)

#lower la convierte todo a minuscula

resultado1 = cadena1.lower()
print (resultado1)

#capitalize la primerla letra en Mayuscula

resultado2 = cadena1.capitalize()
print(resultado2)

#Find busca una cadena en otra cadena - devuelve -1 cuando no encuentra 

busqueda_find = cadena1.find("P")
print(busqueda_find)

#Intex busca una cadena en otra cadena - devuelve ERROR(excepcion) si no encuentra nada

busqueda_intex = cadena1.index("P")
print (busqueda_intex)

#isnumeric si es numerico devuelve true si no false

numerico = cadena1.isnumeric()
print (numerico)

#isalpha si es alfanumerico devuelve true si no false, si hay espacios devuelve false

alfanumerico = cadena1.isalpha()
print (alfanumerico)

#count devuelve el numero de cuantas veces encontro una considencia y si no se ecnuentra devuelve 0

contar_coincidencias = cadena1.count("d")
print(contar_coincidencias)

#cuantos caracteres tiene una cadena 

contar_caracteres = len(cadena1)
print (contar_caracteres) 

#startswith verifica si hay una cadena empieza con otra cadena si es asi devuelve true si no False 

empieza_con = cadena1.startswith("Ed")
print (empieza_con) 

#endswith verifica si hay una cadena termina con otra cadena si es asi devuelve true si no False 

termina_con = cadena1.endswith("az")
print (termina_con)

#replace esta remplaza un valor por otro valor 

cadena_nueva = cadena1.replace("az","ez")
print (cadena_nueva)

#split separar segun el caracter que le pasemos 

cadena_separada = cadena1.split(" ")
print (cadena_separada)
