print('\nAhora veremos el metodo "strip()"\n')
# El metodo "strip()" se encarga de eliminar algunos caracteres especificos
# del inicio y el final de una cadena de texto, dentro de los parentecis del
# "strip()" deveras meter los caranteres que deseas eliminar.

print('Ejemplo 1: Si no le espesificamos al metodo '
      'que caracter deseamos eliminar por defecro nos eliminara los espacios '
      'en blanco del preincipio y del final\n')

palabra = " Emmanuel "
print(palabra.strip())

print('\nEjemplo 2')
# si el "strip" esta vacio solo eliminara los espacios en blanco, tabulaciones
# y saltos de linea del inicio y final de la cadena.
palabra = input('ingresa una cadena de texto: ')
palabra = palabra.strip('\to Eel\n')
print(palabra)
