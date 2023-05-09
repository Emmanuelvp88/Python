print('*************   Metodo center()   ***********\n')
print('El metodo center() se encarga de  centrar una cadena de texto, este metodo recibe para metros es decir que no \n'
      'puede ir solos los pararentesis Ejemplo: cadena.center(10, "*") si cadena contiene 4 caracteres quedarian 3 a la derecha\n'
      'y 3 a la izquierda pro que el primer parametroe es 10 y esto equivale a los espacios en total, el segundo parametro es para\n'
      'llener los espacios en blanco que quedan a los lados, con cualquier caracter que uno indique, solo debe ponerse un caracter\n'
      'entre comillas, en este caso es un parentesis asi qeu la cadena quedaria asi:***hola***\n')

cadena = input('Ingresa una cadena: ')
caracter = input('Ingresa el caracter que deseas tener a los lados, si no, puedes dejarlos en blanco: ')
espacios = int(input('cuantos espacios quieres a los lados?: '))
espacios = len(cadena) + espacios * 2;
if len(caracter) == 0:
      caracter = " "

print(cadena.center(espacios, caracter))