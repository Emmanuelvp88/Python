print('Ahora veremos diferentes formas y metodos con lo que podemos concatenar y una de esos metodos es "format"')

nombre = 'Juan'
edad = 22

print('Ejemplo 1: con el signo +')
# Esta es la concatenacion tardicional con la estamos acostumbrados
print('Hola ' + nombre + ' tu edad es de ', edad, ' años \n')

print('Ejemplo 2')
# En este ejemplo ponemos el orden de las variables dentro del format y asi es
# como se mostraran en el print
print('Hola {} tu edad es de {}'.format(nombre, edad), 'años \n')

print('Ejemplo 3')
# En este ejemplo " podemos declarar las variables localmente dentro dentro
# del mismo "format" no importa el orden,es necesario que
# dentro de las llaves, este el mismo nombre de las variables decalradas en el format.
print('Hola {nombre} tu edad es de {edad} \n'.format(nombre='Emmanuel', edad=33))

print('Ejemplo 4')
print(f'Hola {nombre} tu edad es de {edad} años')
