"""En este programa aprenderemos los diferentes tipos de DATOS en python
y aprenderemos a declarar los tipo de datos mas importantes y concatenaremos
 su tipo con "type", ya que PYTHON es un lenguaje de programacion de TYPADO DYNAMICO
 que quiere decir que al declarar una variable no necesitamos que pongamos
 el tipo de dato"""

print("***AHORA VEREMOS LOS TIPOS DE DATOS MAS USADOS.***")
print()

print("(int)ENTEROS Y (long)LARGOS")
"Son aquellos que no tienen decimales ya sea Positivos o Negativos"
numero = 15
print(numero, " Es del tipo ", type(numero))
print()

print("(Float) FLOTANTES O REALES")
"Son aquellos que tienes punto decimal ya sean Positivos o Negativos"
numero = 15.834873
print(numero, " Es del tipo ", type(numero))
print()

print("(Complex) COMPLEJOS")
"""Son aquellos que tienen una parte real y una parte imaginaria, la mayor parte
de los lenguajes de origramacion carecen de este tipo, aunque sea mu yutilizado
por ingrnieros y cientificos en general."""
numero = 5 + 6j
print(numero, "Es del tipo: ", type(numero))
print()

print("(String) CAEDENA DE TEXTO")
"""Estas cadenas no son mas que texto to encerrado entre comillas sencillas o dobles
tambien es posible encerrarla entre comillas triples de esta forma podemos escribir
el texto en varias lineasy al imprimir la cadena se respetaria los saltos de linea que
demos, sin la nesecidad de recurir al caracter \n."""
numero = "Emmanuel"
print(numero, "Es del tipo: ", type(numero))
print()

print("(bool) BOLEANO")
'''Este tipo de datos solo pueden tener  cierto "true"  o Falso "False" estos valosres
son realmente importantes para las expresiones condicionales y los bucles .'''
bolean = 2 == 3
print(bolean, "Es del tipo ", type(bolean))
