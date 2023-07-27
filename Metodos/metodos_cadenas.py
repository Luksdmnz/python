cadena1 = "Hola soy Lucas"
cadena2 = "Bienvenido"
#Esta es la manera eficiente de utilizar un "metodo de cadena".

 
#UPPER: Se utiliza para poner todo el texto en mayusculas.
mayusc = cadena1.upper()


#LOWER: Convierte todo a miniscula
minusc = cadena1.lower()

#CAPITALIZE: Convierte la primer letra unicamente en mayuscula.
primer_letra_mayusc = cadena1.capitalize()

#FIND: Metodo para buscar una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find ("Hola")

#INDEX: buscamos una cadena en otra cadena, si no encuentra coincidencia lanza una excepcion.
busqueda_index = cadena1.index("")

#IsNumeric: Si el dato que buscamos es Numerico devuelve TRUE. Si no FALSE.
es_numerico = cadena1.isnumeric()

#IsAlpha: Si el dato que buscamos es Alfanumerico devuelve TRUE. Si no FALSE.
es_alfanumerico = cadena1.isalpha()

#COUNT: Cuenta la cantidad de veces que coincide una cadena dentro de otra cadena. Y las devuelve al usuario.
contar_coincidencias = cadena1.count("Hola")

#LEN: Cuenta la cantidad de caracteres dentro de una cadena.
contar_caracteres = len(cadena1)

print(contar_caracteres)
