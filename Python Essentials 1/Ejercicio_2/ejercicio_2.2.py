#Creando una funcion que nos devuelva los numeros primos
#Entre 0 y el argumento que pasamos

#Crear una funcion que verifique si un numero es primo
def es_primo(num):
    #Veridficamos que el numero pasado puede dividirse pro un numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #Si es divisible por alguno retronamos false y termina el bucle 
        if num%i==0: return False
    #si termina el bucle significa que no fue divisible entonces es primo
    return True

#Creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #Creamos una lista
    primos = []
    for i in range(3,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #Devolvemos la lista
    return primos

#Mostramos el resultado
resultado = primos_hasta(13)
print(resultado)
             