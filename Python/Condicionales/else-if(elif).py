#ingreso_mensual = 100000

#if ingreso_mensual > 1000:
#    print ("Vives bien en Latinoamerica")

#if ingreso_mensual > 10000:
#    print ("Estas bien en cualquier parte el mundo")

#else:
#    print ("Estas pobre consigue trabajo")

ingreso_mensual = 100

if ingreso_mensual > 10000:
    print ("Vives bien en cualquier parte del mundo")

elif ingreso_mensual > 1000:
    print ("Estas bien en Latinoamerica")
 
elif ingreso_mensual > 800:
    print ("Estas bien en Colombia")

elif ingreso_mensual > 500:
    print ("Estas bien en Argentina")

else:
    print ("Estas pobre consigue trabajo")
    
    
ingreso_mensual = 30000
gasto_mensual = 20000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print ("Estas bien no te asustes")
    elif ingreso_mensual - gasto_mensual > 800:
        print ("Vives bien en cualquier parte del mundo")
    else:
        print ("Estas algo grave")


elif ingreso_mensual > 1000:
    print ("Estas bien en Latinoamerica")
 
elif ingreso_mensual > 800:
    print ("Estas bien en Colombia")

elif ingreso_mensual > 500:
    print ("Estas bien en Argentina")

else:
    print ("Estas pobre consigue trabajo")
    