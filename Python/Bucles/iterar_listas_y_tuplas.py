
animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [19,89,21,90,21]

#Recorriendo la lista de animales
for animal in animales:
    print (f"Ahora el animal es igual a: {animal}")

#Recorriendo la lista de numeros y multiplicado por 10
for numero in numeros:
    resultado = numero * 10
    print (f"El valor del numero por 10 es: {resultado}")


#Recorriendo dos lista del mismo tamaño al tiempo con zip
for numero, animal in zip(numeros, animales):
    print(f"Recorriendo lista animales: {animal}")
    print(f"Recorriendo lista de numeros: {numero}")
    
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print (f"El indice es: {indice} y el valor es: {valor}")

#usando el for/else    
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual. {numero}")
else:
    print(f"El bucle termino")

#Todo lo anterior funciona exactamente igual para tuplas