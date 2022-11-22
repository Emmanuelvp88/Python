print('Ahora veremos el metodo  "literals String" o "f String"')
# Este metodo de concatenacion es el mas eficiente de todos los que emos visti hasta ahora
# Se trata de poner dentro de llaves una variable, no importa el lugar en la cadena
# de texto, solo tienen que ir entre llavez y escritas tal cual fueron declaradas.
# NOTA: tiene que llevar una "f" pegada alprincipio de la cadena de texto

print('Ejemplo 1')

nombre = input("introduce tu nombre: ")
edad = int(input("Intruduce tu edad: "))

# Aqui solo vemos como se concatenan variables con "f" string
print(f"Hola {nombre} tu edad es de {edad} años \n")

print("Ejemplo 2")

num1 = int(input(f'hola {nombre} Ingresa un numero: '))
num2 = int(input(f'{nombre} ahora introduce el segundo numero: '))

# Aqui vemos que no solo nos permite agregar variables si no que tambien nos permite
# Agregar Expreciones dentro de la misma cadena, como es una suma, resta, multiplicacion
# Divivion etc. montrando el resultado de la exprecion.
print(f'{nombre} el resutado de num1 + num2 es igual a:  {num1 + num2}')

