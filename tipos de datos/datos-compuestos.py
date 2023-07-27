
#Creando una lista (se puede modificar)
lista = ["Lucas Dominguez", "Soy Dalto", True, 1.85]

#creando una tupla(no se pueden modificar)
#Los elementos no se pueden modificar
tupla = ("Lucas Dominguez", "Soy Dalto", True, 1.85)

#esto es valido
lista [3] = "Maquinola"

#Esto no es valido 
tupla[3] = "Maquinola"

#Creando un conjunto (set)
#De esta manera no te permite acceder a los elementos por indice
#Los elementos no se pueden modificar
#No deja repetir valores 
#Datos desordenados
conjunto = {"Lucas Dominguez", "Soy Dalto", True, 1.85}


#creando un diccionario (dict)
diccionario = {
    
    'nombre' : "Lucas Dominguez",
    'esta_emocionado': True,
    'altura' : 1.78,
    'dato_duplicado': "Lucas Dominguez"

}

#para mostrar el dict es "print(diccionario['altura'])" altura seria como el "key"