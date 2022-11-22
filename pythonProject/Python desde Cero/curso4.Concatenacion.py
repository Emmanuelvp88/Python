print("*****ASIGNACION MEDIENTE ACUMULACION*****")

mensaje1 = "Hola"
mensaje1 += " "
mensaje1 += "Emmanuel"
print(mensaje1)
print()

print("*******Concatenacion de cadenas de caracteres y numeros********")
print()

print("*CONCATENACION DE STRING*")

saludo = "Hola"
espacio = " "
nombre = "Emmanuel"
print(saludo + espacio + nombre)
print()

print("*CONCATENACION  STRING , INT*")

num1 = 7
num2 = 5
resultado = num1 + num2
'''Hay varios  modo de concatenar diferentes tipos de variables en una sola
linea , emos visto la clasica con un signo de + o concatenacion, pero existe
otro modo, que seria con una simple coma" ," en vez del signo de suma "+" y
existe aunotro modo que es convertir en tipo "String" lavariable que quieres
imprimir junto en la misma linea '''

# modo 1 convertImos previamente cualquier variable a String y posterior concatenamos
resultado = str(resultado)
print("1.-El resultado de tu suma es: " + resultado)

# modo 2 convertimos cualquier variable en la misma linea del "Print"
print("2.-El resultado de tu suma es: " + str(resultado))

# metodo 3 Solo concatenamos con una coma y automaticamente se typea
print("3.- El resultaso de tu suma es: ", resultado, "\n \n")

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


print("****COMPARACION DE CADENAS DE TEXTO****")
# si la comparacion coincide solo te marcara "True" y si no te marcara "False"#

cadena1 = "Emmanuel"
cadena2 = "emmanuel"
print(cadena1 == cadena2)
