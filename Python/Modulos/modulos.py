#Importando un modulo y asignandole un nombre
import modulo_saludar as m_saludar

saludo = m_saludar.saludar("Eddier")
print(saludo)

#Desde ese modulo importamos la funcion y asignamos un nombre
from modulo_saludar import saludar_ingles as ingles

saludo = ingles("Eddier")
print(saludo)

#Importamos todas las funciones pero es una muy mala practica
from modulo_saludar import *

#Para ver las propeidas y metodos de namespace
#print(dir(m_saludar))

#Acceder al nombre del metodo que usamos .__name__
print(m_saludar.__name__)