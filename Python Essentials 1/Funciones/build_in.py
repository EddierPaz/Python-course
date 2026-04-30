numeros = [4,7,1,42,15]

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondeando a decimales
#round: redondea el numero y despues del numero va una coma y la cantidad de decimales que quiere
numero = round(12.345678,2)
print(numero)

#Retorna false -> 0, vacio, false, None / True -> distinto a 0, True, cadena, datos no vacio
resultado_bool = bool("Eddier")
print(resultado_bool)

#Retorna True, si todos los datos son verdaderos
resultado_all = all([234,"true,[112,12]"])
print(resultado_all)

#Suma todos los valores de un iterable(deben ser numeros)
sum_total = sum(numeros)
print(sum_total) 

