print('\nAhora veremos el metodo "strip()"\n')
# El metodo "strip()" se encarga de eliminar algunos caracteres especificos
# del inicio y el final de una cadena de texto, dentro de los parentecis del
# "strip()" deveras meter los caranteres que deseas eliminar.

print('Ejemplo 1')
palabra = input('ingresa una cadena de texto: ')
palabra = palabra.strip('n elm')
print(palabra)

print('\nEjemplo 2')
# si el "strip" esta vacio solo eliminara los espacios en blanco, tabulaciones
# y saltos de linea del inicio y final de la cadena.
palabra = input('ingresa una cadena de texto: ')
palabra = palabra.strip('\to Eel\n')
print(palabra)

print('\nAhora veremos el metodo "rstrip()"')
# El metodo "rstrip()" se encarga de eliminar solo los caranteres de el lado derecho
# o que es lo mismo del final de una cadena de carateres.

cadena = "Hola Emmanuel"
cadena = cadena.rstrip('eln')
print(cadena)

print('\nAhora veremos el metodo "lstrip()"')
# El metodo "lstrip()" es lo mismo que los anterios metodos solo que este se encarga
# solo de eliminar los carcteres del lado izquierdo o que es lo mismo, del principio
# de una cadena de texto
cadena = "hola Emmanuel"
cadena = cadena.lstrip('hoa')
print(cadena)

# NOTA: estos metodos solo actuan de esta manera: los caracteres que ingresamos en los
# parentesis deben ser tal cual se ingresaron en la cade de texto y  se ira eliminando
# uno por uno, al momento de que el metodo no encuentre uno se saltara al otro
# hasta que encuentre uno que cioncida y lo elimine, entonces  regresara el prinsipio
# de su orden y buscara nuevamente hasta encontrar otro que coincida.
