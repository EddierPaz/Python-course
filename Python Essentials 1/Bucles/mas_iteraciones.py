#Creando una lista
frutas = ["Mango", "Durazno", "Granadilla", "Banano", "Manzana"]
cadena ="Hola Eddier"
numeros = [2,5,8,10]

#Evitando que se coma un Mango con la sentencia continue
for fruta in frutas:
    if fruta == "Mango":
        continue
    print(f"Me voy a comer: {fruta}")
    
#Evitar que el bucle se siga ejecutando
for fruta in frutas:
    if fruta == "Granadilla":
        break
    print(f"Me voy a comer una: {fruta}")

print("El bucle ha terminado")

#Recorrer una cadena de texto 
for letra in cadena:
    print(letra)

#for en una solo linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)


