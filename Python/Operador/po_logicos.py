#AND se tienen que cumplir las dos condiciones para devolver true si alguna tiene false devuelve false 

Resultado1 = True & True #Devolver True
Resultado2 = False & True #Devolver False
Resultado3 = True & False #Devolver False
Resultado4 = False & False #Devolver False

#OR Con que se cumpla una de las condiciones devuelve verdadero y si las dos son false devulve false 

Resultado5 = True or True #Devolver True
Resultado6 = False or True #Devolver True
Resultado7 = True or False #Devolver True
Resultado8 = False or False #Devolver False

#NOT Negacion invierta la condicion

Resultado9 = not False #Devolver True
Resultado10 = not True #Devolver False

print (Resultado5)



Es_verdad = not 10 == 10 

print (Es_verdad)