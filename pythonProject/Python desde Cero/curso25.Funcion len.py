print("Ahora veremos de que se encarga la funcion 'len' \n")
# la funcion "len" se encarga de contar el numero de caracteres que tiene un cadena de
# texto empezando a contar desde el Cero.

print("Ejemplo 1")
print("La palablar 'HOLA' tiene ", len("hola"), " caracteres. \n")

print("Ejemplo 2")
longitut = len("Emmanuel")
print("el nombre 'Emmanuel' tiene ", longitut, " caracteres. \n")

print("Ejemplo 3")
cadena = input("Ingresa una cadena de caractares.")
print("La cadena que ingresaste tiene ", len(cadena), " caracteres. \n")


print('******BUSQUEDA DE POSICION EN UNA CADENA DE CARASTERES (Metodo "find")******* \n')
# el metodo *find* se encarga de decirte en que numero de pocisiond empieza cierto texto que
#  deseas buscar de alguna cadena de caracteres Original, alojandolo en una variable "int"

mensaje = "Hola Emmanuel"
print("Cadena de caracteres: " + mensaje)

# teenmos que respetar las mayusculas para que funcione la busqueda
cadena = mensaje.find("la Emma")
print("El metodo 'find' detecta que la cadena que buscas empieza desde la pocision numero:", cadena, "\n")

print("*******EXTRACCION DE CADENA DE CARACTERES****** \n")
# Para extraer una parte de texto de alguna cadena de texto deberas encerrar entre corchetes
# de que numero hasta que numero de acaracteres quieres obtener.

mensaje = "Hola Emmanuel"
cadena_de_extarccion = mensaje[2:7]
print("Has extraido estos caracteres: " + cadena_de_extarccion)
print()
