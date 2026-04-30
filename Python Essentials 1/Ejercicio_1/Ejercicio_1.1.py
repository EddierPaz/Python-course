#duracion de los cursos

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedios = 4
curso_dalto = 1.5

#Crudos promedio del video

crudo_promedio = 5
crudo_dalto = 3.5


#diferencia de duración 
#para que no aparezca tantos decimales se hace asi dato * 1000 // dato /10
# diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10


diferencia_con_min = 100 - curso_dalto / otros_cursos_min *100
diferencia_con_max = 100 - curso_dalto / otros_cursos_max *100
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedios *100

#Mostrando la cantidad de curso vacio

tiempo_vacio_promedio = 100 - otros_cursos_promedios * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10

#Resultado ejercicio A
print("--------------------------")

print(f"La difernecia del curso de Dalto es de {diferencia_con_min}% con el mas rapido")
print(f"La difernecia del curso de Dalto es de {diferencia_con_max}% con el mas lento")
print(f"La difernecia del curso de Dalto es de {diferencia_con_promedio}% con el promedio")
print("--------------------------")

#Resultado ejercicio B
print(f"El tiempo vacio elimando de los cursos es {tiempo_vacio_promedio}% en promedio")
print(f"El tiempo eleimando de este curso {tiempo_vacio_dalto}%")
print("--------------------------")

#Mostrando la diferencia si los cursos duran 10 horas 

print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedios * 100 // curso_dalto / 10 } horas de otros curos")
print(f"Ver 10 horas de otros cursos equivale a ver {curso_dalto * 100 // otros_cursos_promedios / 10} horas de este curso")
print("--------------------------")
