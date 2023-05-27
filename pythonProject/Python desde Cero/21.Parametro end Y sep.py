print('Haora veremos los parametros "end" y "sep".')

print('\nParametro "end"')
# El parametro "end" se encarga de unir cadenas eliminando saltos de linea
# NOTA: solo agregara la sigiente linea de codigo y la unira con la anterior en una sola linea

print("Esto es un ", end=" ")
print("Ejemplo de lo que", end=" ")
print("Hace el parametro end.")

print('\nParametro "sep"')
# El parametro "sep" se encarga de eliminar los espacion o agragar algo
# entre los espacio de una cadena.

# por default Python nos pone un espacio entre cada caracter.
print('cadena original: ', "1", "2", "3", "4", "5")
# pero lo podemos eliminar con el parametro "sep"
print('quitando los espacios: ' + "1", "2", "3", "4", "5", sep="")
# o complemetarlo con cualquier caracter que queramos en este caso usaremos una coma
print("Separacion con coma; 1" , "2" , "3" , "4" , "5", sep=",")
# un "Gion"
print("1", "2", "3", "4", "5", sep="-")
# o un signo
print("1", "2", "3", "4", "5", sep="+")
