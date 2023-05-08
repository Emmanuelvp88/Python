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
      'Con forme los valla encontrando los ira eliminando y saltara al siguinte caracter y asi sucesivamente hasta terminar con la cadena, al final '
      'solo mostrara los caracteres restantes de la cadena.')

#si el "strip" esta vacio solo eliminara los espacios en blanco, tabulaciones  y saltos de linea del inicio y final de la cadena.
#Cabe mencionar que si no escuentra ningun caracter indiacado en el principio o el final se saltara
palabra = input('ingresa una cadena de texto: ')
print(f'La cadena que ingresaste es: {palabra}\n')
print('eliminaremos los sigientes caracteres de la cadena que ingresaste: E,m,u')
palabra = palabra.strip('\tE m u\n')
print(f'El restante de la cadena es: {palabra}')
