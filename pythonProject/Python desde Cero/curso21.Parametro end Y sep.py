print('Haora veremos los parametros "end" y "sep".')

print('\nParametro "end"')
# El parametro "end" se encarga de Unir unas cadenas de caracteres un que haya
# un salto de linea, cabe mencionar que solo agregara la sigiente linea de codigo
# y la unira en una sola linea con la anterior, ose que la anterior linea sera una
# sola con la sigiente linea.

print("Esto es un ", end=" ")
print("Ejemplo de lo que", end=" ")
print("Hace el parametro end.")

print('\nParametro "sep"')
# El parametro "sep" se encarga de las separaciones  de unas cadenas de caracteres
# dentro de un print ya sea eliminar lso espacion o agragando algo en cada espacio.

# por default Python nos pone un espacio entre cada caracter.
print("1", "2", "3", "4", "5")
# pero lo podemos eliminar con el parametro "sep"
print("1", "2", "3", "4", "5", sep="")
# o complemetarlo con lo que queramos ya sea una "Coma"
print("1", "2", "3", "4", "5", sep=",")
# un "Gion"
print("1", "2", "3", "4", "5", sep="-")
# o un signo
print("1", "2", "3", "4", "5", sep="+")
