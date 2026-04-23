#Forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
resultado = suma([1,25,5,5,8,59])
print(resultado)


#Forma optima de sumar valores operador args (*)

def suma(numeros):
    return sum([*numeros])
resultado = suma([1,2,3,4,5])

def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros son: {sum(numeros)}"

resultado = suma("Eddier Paz",1,2,3,4,5)
print(resultado)