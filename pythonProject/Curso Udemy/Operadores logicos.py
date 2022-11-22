print('En esta leccion veremos lso operadores Boleanos "and", "or" y "not"\n')

print('Operador "and"')
# Este operador devuelve "True" solo si mabos valores de la condiocon son verdaderos
# de lo contrario devolvera "False" y es unoperador binario. Ocupa de dos (operandos
# o valores) para poder comparar uno con el otro.
a = True
b = False
resultado = a and b
print(resultado)

print('\nOperador "or"')
# Este operador devuelve "True" si cualquiera de los operandos o valores es verdadero
# solo necesita uno de los dos que sea verdadero para regresar "True" o forzosamente
# necesita que los dos operandos sean falsos para regresar "False".
a = True
b = False
resultado = a or b
print(resultado)

print('\nOperador "not')
# Este es un Operador Unario de negacion, esto queire decir que solo necesita de un
# operando o valor para ser su funcion y lo que hace es invertir un valor de falso a
# verdadero y viseversa, pone lo contrario a lo que tiene este valor.

a = True
resultado = not a
print(resultado)
