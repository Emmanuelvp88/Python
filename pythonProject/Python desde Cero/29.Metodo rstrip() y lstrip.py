
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
