"""Beneficios:
1.Usar cuando queremos algo sencillo y rapido
2.Se retorna automaticamente
No son actas:
1.Para dar mas de una instruccion
"""

numeros = [1,2,3,4,5,6,7,8,9]
#Creando una funcion lambda para multiplicar
multiplicar_por_dos = lambda x : x*2

numeros_pares1 = filter(lambda numero:numero%2== 0,numeros)
print(list(numeros_pares1))
#Creando una funcion comun qur diga si es par o no 
def es_par(num):
    if (num%2==0):
        return True

#Usando filter con una funcion comun
#Agrega en una listo todo lo que sea True
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

