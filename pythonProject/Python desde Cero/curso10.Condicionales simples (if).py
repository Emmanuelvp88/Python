#SENTENCIAS CONDICIONALES SIMPLES (if)

print ("sistema paracalcular el promedio de alumnos.")
print()
nombre =  input(" Para comenzar , ¿Cual es tu nombre?")
matematicas =  int (input(nombre + " Cual es tu califiacacion en matematicas: "))
español = int (input(nombre + "¿ Cual es tu calificacion en español?"))
biologia = int (input(nombre + " ¿Cual es tu calificacion en biologia?"))
promedio = (matematicas + español + biologia)/ 3
promedio = int (promedio)#parseo de float a int
if promedio > 6:
    print ("Felicidades " + nombre + "has aprobado con: " , promedio)
print ("Fin.")
