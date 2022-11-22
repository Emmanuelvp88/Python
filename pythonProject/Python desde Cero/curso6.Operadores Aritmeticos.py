"""Los Operadores aritmeticos con los que cuenta Pythonson
.Suma (+)
.resta(-)
.multiplicacion(*)
.Divicion(/)
.modulo(%)
.Exponente(**)
.Divicion Entera(//)"""
print("SUMA")
num1 = 7
num2= 4

resultado = num1 + num2
print("El resultado de su suma es: " + str(resultado))
print()

print("\nRESTA")
resultado = num1 - num2
print("El resultado de su resta es: "  + str(resultado))
print()

print("\nMULTIPLICACION")

resultado = num1 * num2
print("El resultado de su multiplicacion es: " + str(resultado))


print("\nDIVICION")

resultado = num1 / num2
print("El resultado de su Divicion es: " + str(resultado))
print()

print("\nPOTENCIA O EXPONENTE")

base = 2
exponente = 5
cociente = 2 ** 5
print("El resultado de la potencia es: " + str(cociente))
print()

#el modulo o resto  es el numero sobrante o residuo en la parte de abajo de una divicion
print("\nMODULO O RESTO DE UNA DIVICION")

num1 = 9
num2 = 7
resultado = float (num1 % num2)#Parseamos a float al variable resultado

print("El  de el modulo o resto de tu divicion  es: " + str(resultado))
print ()

"""La divicion estera es aquella que solo te muestra el resultado en
numeros enteros sin decimales."""

print ("\nDIVICION ENTERA")
resultado = num1//num2
print ("El resultado de su divicion entera es: " + str(resultado))
