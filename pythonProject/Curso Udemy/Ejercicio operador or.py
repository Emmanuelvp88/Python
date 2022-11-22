print('Ejercicio con el operador "and"')
# vamos a realizar un ejercicio donde digamos si un valor esta dentro o fuera
# de rango, para eso pondremos un rango.

valor = int(input('Escrive un valor: '))
Vminimo = 0
Vmaximo = 7

rango = valor >= Vminimo and valor <= Vmaximo

if rango:
    print(f'El valor ingreasdo {valor} esta dentro de rango')
else:
    print(f'El valor ingresado {valor} esta fuera de rango ')

print('\nEjercicio con el operador "or"')
# Este ejerciocio consiste en que si un padre de familia tiene dia  de  descanso o
# vacaiones podra asistir a el juego de su Hijo y sino ps no.

vacaciones = False
Dia_de_descanso = False

if Dia_de_descanso or vacaciones:
   print('Su padre si asistira al juego')
else:
    print('no podra asistir tiene que trabajar')


print('\nEjercicio con el operador "not"')
#invierte totalmente lalogica, es necesario poner toda la exprecion entre parentesis
# ya que si no se hace solo agarrara solo el valo rde la primer variables que es "vacaciones"

if not (vacaciones or Dia_de_descanso):
    print('no podra asistir tiene que trabajar')
else:
    print('Su padre si asistira al juego')
