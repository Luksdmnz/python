ingreso_mensual = 100000
gasto_mensual = 5000

#Primero el programa ingresa en esta condición y verifica si tu ingreso mensual es igual o mayor al monto establecido.
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit.")
    elif ingreso_mensual - gasto_mensual > 3000:
         print("Estas bien.")
    else: 
        print("Estas gastando mucho.")

#Caso contrario que no sea así ingresa en una segunda condición para verificar.
elif ingreso_mensual > 1000:
    print("Estas bien en Latinoamerica")
 
# Y si la 2da condición no es aceptada entra en el else.
else: 
    print("sos pobre")