print('*************   Metodo center()   ***********\n')
print('El metodo center() se encarga de  centrar una cadena de texto, este metodo recibe para metros es decir que no \n'
      'pueden estar vacios los pararentesis. Ejemplo: cadena.center(10, "*") si cadena contiene 4 caracteres quedarian 3 a la derecha\n'
      'y 3 a la izquierda pro que el primer parametroe es 10 y esto equivale a los espacios en total, el segundo parametro es para\n'
      'llener los espacios en blanco que quedan a los lados, con cualquier caracter que uno indique, solo debe ponerse un caracter\n'
      'entre comillas, en este caso es un parentesis asi qeu la cadena quedaria asi:***hola***\n')

cadena = input('Ingresa una cadena: ')
espacios = int(input('cuantos espacios quieres a los lados?: '))
caracter = input('Que caracter deseas tener a los lados, o deseas espacios enblanco: ')

espacios = len(cadena) + espacios * 2;   #suma de los espacios mas el numero de caracteres

if len(caracter) == 0:  #validacion por si el usuario no ingresa ningun caracter
      caracter = " "

print(cadena.center(espacios, caracter))

print('\n******* Metoodo ljust()   ******\n')
print('El metodo ljust() es igual que el metodo center(), solo que recorre el contenido de la cadena al lado izquierdo.')

cadena1 = input('Ingresa una cadena: ')
espacios = int(input('cuantos espacios quieres a tu izquierda: '))
caracter1 = input('Que caracter deseas o deseas espacios en blaco: ')

espacios = len(cadena) + espacios;
if len(caracter1) == 0:
      caracter1 = " ";
print(cadena1.ljust(espacios, caracter1))

print('\n********* Metodo rjust() *********\n')
print('El metodo rjust() es igual que el metodo ljust(), solo que este recorre los caracteres de una cadena hacia la derecha.\n')

cadena2 = input('Ingresa una cadena: ')
espacios2 = int(input('Cuantos espacios a la derecha deseas:  '))
caracter2 = input('Que caracter deseas o deseas espacios en blanco: ')

espacios2 = len(cadena2) + espacios2;
if len(cadena2) == 0:
      cadena2 = ' ';
print(cadena2.rjust(espacios2, caracter2))