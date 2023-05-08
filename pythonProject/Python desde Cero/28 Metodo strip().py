print('\n***************    Metodo strip()    **********\n')
# El metodo "strip()" se encarga de eliminar caracteres especificos del inicio y el final de una cadena de texto,
# dentro de los parentecis del "strip()" deveras poner los caranteres que deseas eliminar.

print('Ejemplo 1: Si no le espesificamos al metodo '
      'que caracter deseamos eliminar por defecto nos eliminara los espacios '
      'en blanco del principio y del final\n')

palabra = "   Emmanuel   "
print("Cadena original:", palabra)
print("Cadena con el metodo strip():",palabra.strip())

print('\nEjemplo 2: Al ingresar caracteres dentro del metodo "strip()" los caracteres se iran eliminando del principio y del final  de la cadena'
      'Con forme los valla encontrando los ira eliminando y saltara al siguinte caracter y asi sucesivamente hasta terminar con la cadena')
# si el "strip" esta vacio solo eliminara los espacios en blanco, tabulaciones
# y saltos de linea del inicio y final de la cadena.
palabra = input('ingresa una cadena de texto: ')
palabra = palabra.strip('\to Eel\n')
print(palabra)
