#creando un conjunto con set

conjunto = set(["Dato1", "Dato2"])

#conjunto dentro de otro conjunto
conjunto1 = frozenset (["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print (conjunto2)

#teoria del conjunto 

conjunto1 = {1,2,3,4}
conjunto2 = {1,2,3}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) #issubet = subconjunto
resultado = conjunto2 <= conjunto2 # <= igual o menos 

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1) #issubet = superconjunto
resultado = conjunto2 > conjunto2 # > = mayor que 

#verificando si hay algun numero en comun
# Cuando un elemento coincide da false 
# cuadno no hay ninguna coinciencia es true
resultado = conjunto2.isdisjoint(conjunto1)

print (resultado)