
print('\nMetodo "rstrip()"\n')
# El metodo "rstrip()" se encarga de eliminar solo los caranteres del final de una cadena
# seria igual que borrar todos los espacios de lado derecho de una cadena es por eso de "r" de right strip.

cadena = "Hola Emmanuel"
print("cadena original: ", cadena)
cadena = cadena.rstrip('eln')
print(cadena)



print('\nAhora veremos el metodo "lstrip()"')
# El metodo "lstrip()" es lo mismo que los anterios metodos solo que este se encarga
# solo de eliminar los carcteres del principio de una cadena de texto
# seria igual que borrar todos los espacios de lado izquierdo de una cadena es por eso de "l" de left strip.


cadena = "hola Emmanuel"
cadena = cadena.lstrip('hoa')
print(cadena)

# NOTA: estos metodos solo actuan de esta manera: los caracteres que ingresamos en los
# parentesis deben ser tal cual se ingresaron en la cadena de texto original y se ira eliminando
# uno por uno, al momento de que el metodo no encuentre uno se saltara al otro
# hasta que encuentre uno que cioncida y lo elimine, entonces  regresara el prinsipio
# de su orden y buscara nuevamente hasta encontrar otro que coincida.
